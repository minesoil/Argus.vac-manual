"""Small, ROS-independent reactive controller. Distances and speeds use SI units.

The circular footprint is a conservative configurable proxy, not a measurement
of Argus. Missing range data is unknown; +inf means clear only when explicitly
enabled for a driver with that documented convention.
"""

from dataclasses import dataclass, fields
import math


@dataclass(frozen=True)
class Config:
    robot_radius_m: float = 0.22
    margin_m: float = 0.03
    forward_m_s: float = 0.05
    slow_m_s: float = 0.025
    turn_rad_s: float = 0.3
    slow_clearance_m: float = 0.60
    stop_clearance_m: float = 0.30
    resume_clearance_m: float = 0.40
    side_stop_clearance_m: float = 0.05
    side_steer_clearance_m: float = 0.25
    steer_front_clearance_m: float = 0.50
    steer_balance_m: float = 0.07
    steer_rad_s: float = 0.10
    curve_start_clearance_m: float = 0.68
    curve_release_clearance_m: float = 0.85
    curve_lookahead_m: float = 0.24
    curve_rad_s: float = 0.20
    scan_timeout_s: float = 0.5
    clear_scans: int = 3
    stop_hold_s: float = 0.25
    turn_timeout_s: float = 15.0
    min_coverage_ratio: float = 0.90
    max_unknown_gap_rad: float = 0.20
    no_return_is_clear: bool = False

    def __post_init__(self):
        for item in fields(self):
            value = getattr(self, item.name)
            if item.name == "no_return_is_clear":
                if type(value) is not bool:
                    raise ValueError("no_return_is_clear must be boolean")
            elif isinstance(value, bool) or not math.isfinite(value) or value <= 0:
                raise ValueError(f"{item.name} must be positive and finite")
        if type(self.clear_scans) is not int:
            raise ValueError("clear_scans must be an integer")
        if not self.stop_clearance_m < self.resume_clearance_m < self.slow_clearance_m:
            raise ValueError("Require stop < resume < slow clearances")
        if not self.side_stop_clearance_m < self.side_steer_clearance_m or (
                self.steer_front_clearance_m <= self.stop_clearance_m):
            raise ValueError("Steering thresholds must exceed stop thresholds")
        if not (self.stop_clearance_m < self.curve_start_clearance_m <
                self.curve_release_clearance_m):
            raise ValueError("Curve thresholds must exceed stop clearance")
        if self.curve_rad_s > self.turn_rad_s:
            raise ValueError("Moving curve cannot turn faster than an in-place pivot")
        if self.slow_m_s > self.forward_m_s:
            raise ValueError("Slow speed cannot exceed forward speed")
        if self.min_coverage_ratio > 1 or self.max_unknown_gap_rad > math.pi:
            raise ValueError("Invalid coverage settings")


@dataclass(frozen=True)
class Scan:
    ranges: tuple[float, ...]
    angle_min: float
    angle_increment: float
    range_min: float
    range_max: float
    received_at: float
    sensor_x: float = 0.0
    sensor_y: float = 0.0
    sensor_yaw: float = 0.0


@dataclass(frozen=True)
class Decision:
    state: str
    reason: str
    linear: float = 0.0
    angular: float = 0.0
    front_clearance: float | None = None
    left_clearance: float | None = None
    right_clearance: float | None = None


@dataclass(frozen=True)
class _Observation:
    received_at: float
    front: float
    left: float
    right: float
    nearest: float
    points: tuple[tuple[float, float], ...]


class AvoidanceController:
    def __init__(self, config: Config | None = None):
        self.config = config or Config()
        self.state = "DISARMED"
        self.reason = "Disarmed"
        self.armed = False
        self._observation = None
        self._scan_reason = "No scan received"
        self._last_received = None
        self._sequence = 0
        self._counted_sequence = -1
        self._clear_count = 0
        self._stopped_at = 0.0
        self._turn_started = 0.0
        self._turn_direction = 0
        self._curve_direction = 0
        self._last_step = None

    def observe(self, scan: Scan):
        """Accept a fresh full-circle scan; invalid input invalidates clearance."""
        try:
            if self._last_received is not None and scan.received_at <= self._last_received:
                if scan.received_at == self._last_received:
                    return  # Reusing a scan must not count as another clear scan.
                raise ValueError("Scan receipt time moved backwards")
            observation = self._parse_scan(scan)
        except (ValueError, TypeError, OverflowError, AttributeError) as error:
            self._observation = None
            self._scan_reason = f"Invalid scan: {error}"
            self._clear_count = 0
            return
        self._last_received = scan.received_at
        self._observation = observation
        self._scan_reason = "Healthy scan"
        self._sequence += 1

    def _parse_scan(self, scan):
        cfg = self.config
        metadata = (scan.angle_min, scan.angle_increment, scan.range_min,
                    scan.range_max, scan.received_at, scan.sensor_x,
                    scan.sensor_y, scan.sensor_yaw)
        if not all(math.isfinite(v) for v in metadata):
            raise ValueError("nonfinite metadata")
        count = len(scan.ranges)
        delta = abs(scan.angle_increment)
        if not 16 <= count <= 200000 or not 0 < delta <= cfg.max_unknown_gap_rad:
            raise ValueError("insufficient angular resolution")
        span = delta * count
        if abs(span - math.tau) > delta * 1.1:
            raise ValueError("full-circle coverage required for turning")
        reach = cfg.robot_radius_m + cfg.margin_m + cfg.slow_clearance_m
        if not 0 < scan.range_min < scan.range_max or (
            scan.range_max - math.hypot(scan.sensor_x, scan.sensor_y) <= reach
        ):
            raise ValueError("insufficient measurement range")
        known, points = [], []
        for index, value in enumerate(scan.ranges):
            finite = math.isfinite(value) and scan.range_min <= value <= scan.range_max
            clear = cfg.no_return_is_clear and value == math.inf
            known.append(finite or clear)
            if finite:
                angle = scan.angle_min + index * scan.angle_increment + scan.sensor_yaw
                points.append((scan.sensor_x + value * math.cos(angle),
                               scan.sensor_y + value * math.sin(angle)))
        if sum(known) / count < cfg.min_coverage_ratio:
            raise ValueError("insufficient valid scan coverage")
        # Check wraparound too: a gap straddling -pi/pi is still one gap.
        run = longest = 0
        for valid in known + known:
            run = 0 if valid else run + 1
            longest = max(longest, min(run, count))
        if (longest + 1) * delta > cfg.max_unknown_gap_rad + 1e-9:
            raise ValueError("unknown angular gap too wide")
        # Even a small missing cone can hide a chair leg. Coverage ratios alone
        # cannot prove that corridor or rotation space is clear. V1 deliberately
        # refuses motion with any unknown ray, even with lenient diagnostics.
        if not all(known):
            raise ValueError("unknown ray prevents proving swept clearance")
        radius = cfg.robot_radius_m + cfg.margin_m

        def corridor(heading):
            cosine, sine = math.cos(heading), math.sin(heading)
            candidates = []
            for x, y in points:
                along, across = x * cosine + y * sine, -x * sine + y * cosine
                if along >= -1e-9 and abs(across) <= radius:
                    candidates.append(max(0.0, along - radius))
            return min(candidates, default=math.inf)

        return _Observation(scan.received_at, corridor(0), corridor(math.pi / 2),
                            corridor(-math.pi / 2),
                            min((math.hypot(x, y) for x, y in points), default=math.inf),
                            tuple(points))

    def health(self, now):
        if not math.isfinite(now):
            return False, "Invalid control time"
        obs = self._observation
        if obs is None:
            return False, self._scan_reason
        age = now - obs.received_at
        if age < -1e-6:
            return False, "Scan receipt time is in the future"
        if age > self.config.scan_timeout_s:
            return False, "Scan expired"
        return True, "Healthy scan"

    def arm(self, now):
        healthy, reason = self.health(now)
        if not healthy:
            self.disarm(reason)
            return False, reason
        self.armed = True
        self.state, self.reason = "STOP", "Armed; checking clear scans"
        self._stopped_at = now
        self._turn_direction = 0
        self._curve_direction = 0
        self._clear_count = 0
        self._counted_sequence = -1
        self._last_step = now
        return True, self.reason

    def disarm(self, reason="Disarmed"):
        self.armed = False
        self.state, self.reason = "DISARMED", reason
        self._clear_count = 0
        self._turn_direction = 0
        self._curve_direction = 0

    def _halt(self, state, reason):
        self.armed = False
        self.state, self.reason = state, reason
        return self._decision()

    def _decision(self, linear=0.0, angular=0.0):
        obs = self._observation
        return Decision(self.state, self.reason, linear, angular,
                        obs.front if obs else None, obs.left if obs else None,
                        obs.right if obs else None)

    def _curve_path_clear(self, direction):
        """Require clearance along a short family of plausible forward arcs.

        Wheelbase and wheel speed have not been calibrated on the floor. Checking
        straight travel as well as several curved paths avoids assuming that a
        requested wheel ratio produces one exact radius. This is a local guard;
        the front stop threshold and fresh-scan requirement still apply.
        """
        cfg, obs = self.config, self._observation
        clearance = cfg.robot_radius_m + cfg.margin_m + 0.03
        limit_sq = clearance * clearance
        for step in range(1, 13):
            distance = cfg.curve_lookahead_m * step / 12
            for curvature in (0.0, 1.5, 3.0, 4.5, 6.0):
                if curvature == 0:
                    x, y = distance, 0.0
                else:
                    angle = curvature * distance
                    x = math.sin(angle) / curvature
                    y = direction * (1 - math.cos(angle)) / curvature
                if any((px-x)**2 + (py-y)**2 <= limit_sq for px, py in obs.points):
                    return False
        return True

    def _drive(self):
        cfg, obs = self.config, self._observation
        slow = obs.front <= cfg.slow_clearance_m
        self.state = "SLOW" if slow else "FORWARD"
        speed = cfg.slow_m_s if slow else cfg.forward_m_s
        self.reason = "Obstacle approaching" if slow else "Forward corridor clear"
        if obs.front > cfg.curve_release_clearance_m:
            self._curve_direction = 0
        if obs.front <= cfg.curve_start_clearance_m or self._curve_direction:
            if self._curve_direction:
                directions = (self._curve_direction,)
            else:
                directions = (1, -1) if obs.left >= obs.right else (-1, 1)
            for direction in directions:
                if self._curve_path_clear(direction):
                    self._curve_direction = direction
                    self.state = "SLOW"
                    self.reason = "Curving left around obstacle" if direction > 0 else "Curving right around obstacle"
                    return self._decision(cfg.slow_m_s, cfg.curve_rad_s * direction)
        if obs.front > cfg.steer_front_clearance_m and min(obs.left, obs.right) < cfg.side_steer_clearance_m:
            if obs.left + cfg.steer_balance_m < obs.right:
                if self._curve_path_clear(-1):
                    self.reason = "Steering right away from left obstacle"
                    return self._decision(speed, -cfg.steer_rad_s)
            if obs.right + cfg.steer_balance_m < obs.left:
                if self._curve_path_clear(1):
                    self.reason = "Steering left away from right obstacle"
                    return self._decision(speed, cfg.steer_rad_s)
        return self._decision(speed)

    def step(self, now):
        if not self.armed:
            return self._decision()
        healthy, reason = self.health(now)
        if not healthy:
            return self._halt("FAULT", reason)
        if self._last_step is not None and now < self._last_step:
            return self._halt("FAULT", "Control clock moved backwards")
        self._last_step = now
        cfg, obs = self.config, self._observation
        # A circle containing the whole chassis covers every in-place rotation.
        if obs.nearest <= cfg.robot_radius_m + cfg.margin_m:
            return self._halt("BLOCKED", "Obstacle inside swept footprint clearance")
        if self._counted_sequence != self._sequence:
            path_clear = (obs.front > cfg.resume_clearance_m and
                          min(obs.left, obs.right) > cfg.side_stop_clearance_m)
            self._clear_count = self._clear_count + 1 if path_clear else 0
            self._counted_sequence = self._sequence
        if self.state == "TURN":
            if now - self._turn_started >= cfg.turn_timeout_s:
                return self._halt("BLOCKED", "Turn timed out; re-arm required")
            if self._clear_count >= cfg.clear_scans:
                self.state, self.reason = "STOP", "Path cleared; settling before moving"
                self._stopped_at = now
                return self._decision()
            return self._decision(angular=cfg.turn_rad_s * self._turn_direction)
        if self.state in ("FORWARD", "SLOW"):
            if (obs.front > cfg.stop_clearance_m and
                    min(obs.left, obs.right) > cfg.side_stop_clearance_m):
                return self._drive()
            self.state, self.reason = "STOP", "Obstacle near travel path; stopping before turn"
            self._stopped_at = now
            self._clear_count = 0
            self._curve_direction = 0
            return self._decision()
        if self.state == "STOP":
            if now - self._stopped_at < cfg.stop_hold_s:
                return self._decision()
            if self._clear_count >= cfg.clear_scans:
                self._turn_direction = 0
                return self._drive()
            # Wait for actual distinct clear observations, not repeated timer ticks.
            if (obs.front > cfg.resume_clearance_m and
                    min(obs.left, obs.right) > cfg.side_stop_clearance_m):
                return self._decision()
            # Turning in place sweeps the circular footprint already checked
            # above. Side corridors need not fit a forward-moving chassis.
            if not self._turn_direction:
                self._turn_direction = 1 if obs.left >= obs.right else -1
            self.state, self.reason = "TURN", "Turning left" if self._turn_direction > 0 else "Turning right"
            self._turn_started = now
            self._clear_count = 0
            return self._decision(angular=cfg.turn_rad_s * self._turn_direction)
        return self._halt("FAULT", "Unexpected controller state")
