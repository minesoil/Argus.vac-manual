"""Small, ROS-independent reactive controller. Distances and speeds use SI units.

The circular footprint is a conservative configurable proxy, not a measurement
of Argus. Missing range data is unknown; +inf means clear only when explicitly
enabled for a driver with that documented convention.
"""

from dataclasses import dataclass, fields
from itertools import combinations
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
    wall_gap_estimate_m: float | None = None
    wall_heading_rad: float | None = None


@dataclass(frozen=True)
class _Observation:
    received_at: float
    front: float
    left: float
    right: float
    nearest: float
    points: tuple[tuple[float, float], ...]


@dataclass(frozen=True)
class _Wall:
    distance: float
    heading: float


class AvoidanceController:
    def __init__(self, config: Config | None = None, *, follow_wall=None):
        self.config = config or Config()
        if follow_wall not in (None, "left", "right"):
            raise ValueError("Wall following needs a left or right side")
        self.follow_wall = follow_wall
        self._wall = None
        self._front_obstacle = math.inf
        self._front_close_scans = 0
        self._front_open_scans = 0
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
            self._wall = None
            self._scan_reason = f"Invalid scan: {error}"
            self._clear_count = 0
            return
        self._last_received = scan.received_at
        self._observation = observation
        if self.follow_wall:
            self._wall = self._fit_side_wall(observation.points)
            self._front_obstacle = self._front_beyond_wall(observation)
            self._front_close_scans = (self._front_close_scans + 1
                                       if self._front_obstacle <= self.config.curve_start_clearance_m else 0)
            self._front_open_scans = (self._front_open_scans + 1
                                      if self._front_obstacle > self.config.curve_release_clearance_m else 0)
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
        wall = self._wall
        return Decision(self.state, self.reason, linear, angular,
                        obs.front if obs else None, obs.left if obs else None,
                        obs.right if obs else None,
                        wall.distance - self.config.robot_radius_m if wall else None,
                        wall.heading if wall else None)

    def _fit_side_wall(self, points):
        """Fit a nearby side surface only if it extends fore and aft."""
        side = 1 if self.follow_wall == "left" else -1
        radius = self.config.robot_radius_m
        samples = sorted((x, y) for x, y in points
                         if -0.45 <= x <= 0.50 and radius <= side * y <= radius + 0.40)
        if len(samples) < 5:
            return None
        if len(samples) > 24:
            samples = [samples[round(index * (len(samples) - 1) / 23)]
                       for index in range(24)]
        # Fit the dominant face at joints between boxes. Keep every original
        # scan point in the swept-path and obstacle checks.
        best = (-1, 0.0)
        wall_points = []
        for (x1, y1), (x2, y2) in combinations(samples, 2):
            if x2 - x1 < 0.20:
                continue
            slope = (y2 - y1) / (x2 - x1)
            if abs(slope) > 0.45:
                continue
            offset = y1 - slope*x1
            inliers = [(x, y) for x, y in samples if abs(y - offset - slope*x) <= 0.035]
            if (len(inliers) < 5 or 3 * len(inliers) < 2 * len(samples) or
                    inliers[0][0] > -0.05 or inliers[-1][0] < 0.12):
                continue
            score = (len(inliers), -sum(abs(y - offset - slope*x) for x, y in inliers))
            if score > best:
                best, wall_points = score, inliers
        if not wall_points:
            return None
        mean_x = sum(x for x, _ in wall_points) / len(wall_points)
        mean_y = sum(y for _, y in wall_points) / len(wall_points)
        variance = sum((x - mean_x)**2 for x, _ in wall_points)
        slope = sum((x - mean_x) * (y - mean_y) for x, y in wall_points) / variance
        offset = mean_y - slope * mean_x
        if abs(slope) > 0.45:
            return None
        return _Wall(abs(offset) / math.hypot(1, slope), math.atan(slope))

    def _front_beyond_wall(self, observation):
        """Use separate obstacles for early turns; raw clearance still gates motion."""
        if self._wall is None:
            return observation.front
        inflated = self.config.robot_radius_m + self.config.margin_m
        side = 1 if self.follow_wall == "left" else -1
        sine, cosine = math.sin(self._wall.heading), math.cos(self._wall.heading)
        return min((max(0.0, x - inflated) for x, y in observation.points
                    if x >= 0 and abs(y) <= inflated and
                    abs(-sine*x + cosine*y - side*self._wall.distance) > 0.035),
                   default=math.inf)

    def _sides_clear(self):
        cfg, obs = self.config, self._observation
        if self._wall is None:
            return min(obs.left, obs.right) > cfg.side_stop_clearance_m
        near, far = (obs.left, obs.right) if self.follow_wall == "left" else (obs.right, obs.left)
        inflated = cfg.robot_radius_m + cfg.margin_m
        if self._wall.distance <= inflated + 0.02 or near <= 0.02 or far <= cfg.side_stop_clearance_m:
            return False
        side = 1 if self.follow_wall == "left" else -1
        sine, cosine = math.sin(self._wall.heading), math.cos(self._wall.heading)
        return all(abs(-sine*x + cosine*y - side*self._wall.distance) <= 0.035
                   for x, y in obs.points
                   if abs(x) <= inflated and 0 <= side*y <= inflated+cfg.side_stop_clearance_m)

    def _curve_path_clear(self, direction):
        """Require clearance along a short family of plausible forward arcs.

        Wheelbase and wheel speed have not been calibrated on the floor. Checking
        straight travel as well as several curved paths avoids assuming that a
        requested wheel ratio produces one exact radius. This is a local guard;
        the front stop threshold and fresh-scan requirement still apply.
        """
        return self._paths_clear((direction*c for c in (0.0, 1.5, 3.0, 4.5, 6.0)), 0.03)

    def _paths_clear(self, curvatures, extra_margin):
        cfg, obs = self.config, self._observation
        curvatures = tuple(curvatures)
        clearance = cfg.robot_radius_m + cfg.margin_m + extra_margin
        limit_sq = clearance * clearance
        for step in range(1, 13):
            distance = cfg.curve_lookahead_m * step / 12
            for curvature in curvatures:
                if curvature == 0:
                    x, y = distance, 0.0
                else:
                    angle = curvature * distance
                    x = math.sin(angle) / curvature
                    y = (1 - math.cos(angle)) / curvature
                if any((px-x)**2 + (py-y)**2 <= limit_sq for px, py in obs.points):
                    return False
        return True

    def _track_wall(self):
        cfg, wall = self.config, self._wall
        side = 1 if self.follow_wall == "left" else -1
        gap_error = wall.distance - cfg.robot_radius_m - (cfg.margin_m + 0.04)
        approach_heading = 0.0
        if self._observation.front > cfg.curve_start_clearance_m:
            approach_heading = math.atan2(side * gap_error, cfg.curve_lookahead_m)
        # Aim toward a point at the desired clearance. The measured wall angle
        # reduces the correction as the chassis approaches that line.
        steering = 0.8 * (wall.heading + approach_heading)
        steering = max(-0.20, min(0.20, steering))
        if abs(steering) < 0.015:
            steering = 0.0
        # The floor turn radius is uncalibrated. Check straight and two
        # nearby curvatures before allowing a wheel-speed correction.
        curve = 15 * steering
        if not self._paths_clear((0.0, curve / 2, curve), 0.0):
            if not self._paths_clear((0.0,), 0.0):
                return self._halt("BLOCKED", "Wall-follow path blocked")
            steering = 0.0
        self.state, self.reason = "SLOW", f"Following {self.follow_wall} wall"
        return self._decision(cfg.slow_m_s, steering)

    def _drive(self):
        cfg, obs = self.config, self._observation
        slow = obs.front <= cfg.slow_clearance_m
        self.state = "SLOW" if slow else "FORWARD"
        speed = cfg.slow_m_s if slow else cfg.forward_m_s
        self.reason = "Obstacle approaching" if slow else "Forward corridor clear"
        turn_clearance = self._front_obstacle if self.follow_wall else obs.front
        if turn_clearance > cfg.curve_release_clearance_m and (
                not self.follow_wall or self._front_open_scans >= 3):
            self._curve_direction = 0
        start_curve = turn_clearance <= cfg.curve_start_clearance_m and (
            self._wall is None or self._front_close_scans >= 3)
        if start_curve or self._curve_direction:
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
        if self._wall is not None and not start_curve and not self._curve_direction:
            return self._track_wall()
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
        sides_clear = self._sides_clear()
        if self._counted_sequence != self._sequence:
            path_clear = obs.front > cfg.resume_clearance_m and sides_clear
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
            if obs.front > cfg.stop_clearance_m and sides_clear:
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
            if obs.front > cfg.resume_clearance_m and sides_clear:
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
