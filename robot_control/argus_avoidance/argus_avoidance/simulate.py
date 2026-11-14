"""Small, deterministic 2D avoidance simulation; no ROS, Gazebo or hardware.

Run ``python -m argus_avoidance.simulate --output report.json``. A successful
report validates this simplified model only. It cannot establish physical fit,
lidar visibility, motor performance, serial integration or stopping distance.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, replace
import json
import math
from pathlib import Path
from typing import Optional

from .core import AvoidanceController, Config, Scan


@dataclass(frozen=True)
class Segment:
    ax: float
    ay: float
    bx: float
    by: float


@dataclass(frozen=True)
class Circle:
    x: float
    y: float
    radius: float
    vx: float = 0.0
    vy: float = 0.0
    start_at: float = 0.0
    stop_at: float = float("inf")

    def position(self, now: float) -> tuple[float, float]:
        elapsed = max(0.0, min(now, self.stop_at) - self.start_at)
        return self.x + elapsed * self.vx, self.y + elapsed * self.vy


def _cross(ax: float, ay: float, bx: float, by: float) -> float:
    return ax * by - ay * bx


def ray_segment(ox: float, oy: float, dx: float, dy: float,
                segment: Segment) -> float:
    """Return the first nonnegative ray intersection, or infinity."""
    sx, sy = segment.bx - segment.ax, segment.by - segment.ay
    denominator = _cross(dx, dy, sx, sy)
    qx, qy = segment.ax - ox, segment.ay - oy
    if abs(denominator) < 1e-12:
        # Preserve a collinear return instead of silently losing a thin wall.
        if abs(_cross(qx, qy, dx, dy)) > 1e-12:
            return float("inf")
        a = qx * dx + qy * dy
        b = (segment.bx - ox) * dx + (segment.by - oy) * dy
        lo, hi = sorted((a, b))
        return max(0.0, lo) if hi >= 0.0 else float("inf")
    distance = _cross(qx, qy, sx, sy) / denominator
    fraction = _cross(qx, qy, dx, dy) / denominator
    return distance if distance >= 0.0 and 0.0 <= fraction <= 1.0 else float("inf")


def ray_circle(ox: float, oy: float, dx: float, dy: float,
               cx: float, cy: float, radius: float) -> float:
    qx, qy = ox - cx, oy - cy
    projection = qx * dx + qy * dy
    discriminant = projection * projection - (qx * qx + qy * qy - radius * radius)
    if discriminant < -1e-12:
        return float("inf")
    root = math.sqrt(max(0.0, discriminant))
    near, far = -projection - root, -projection + root
    if near >= 0.0:
        return near
    return far if far >= 0.0 else float("inf")


def point_segment_distance(x: float, y: float, segment: Segment) -> float:
    sx, sy = segment.bx - segment.ax, segment.by - segment.ay
    length_squared = sx * sx + sy * sy
    t = 0.0 if length_squared == 0.0 else max(
        0.0, min(1.0, ((x - segment.ax) * sx + (y - segment.ay) * sy) / length_squared)
    )
    return math.hypot(x - segment.ax - t * sx, y - segment.ay - t * sy)


@dataclass(frozen=True)
class World:
    segments: tuple[Segment, ...] = ()
    circles: tuple[Circle, ...] = ()

    def clearance(self, x: float, y: float, radius: float, now: float) -> float:
        distances = [point_segment_distance(x, y, s) - radius for s in self.segments]
        distances.extend(
            math.hypot(x - cx, y - cy) - radius - circle.radius
            for circle in self.circles
            for cx, cy in (circle.position(now),)
        )
        return min(distances, default=float("inf"))

    def scan(self, x: float, y: float, heading: float, now: float,
             sensor_x: float = 0.0, sensor_y: float = 0.0,
             sensor_yaw: float = 0.0, samples: int = 720,
             range_min: float = 0.05, range_max: float = 12.0,
             unknown: bool = False) -> Scan:
        cosine, sine = math.cos(heading), math.sin(heading)
        ox = x + cosine * sensor_x - sine * sensor_y
        oy = y + sine * sensor_x + cosine * sensor_y
        increment = 2.0 * math.pi / samples
        ranges = []
        circles = [(c, c.position(now)) for c in self.circles]
        for index in range(samples):
            angle = heading + sensor_yaw - math.pi + index * increment
            dx, dy = math.cos(angle), math.sin(angle)
            distance = min(
                (ray_segment(ox, oy, dx, dy, segment) for segment in self.segments),
                default=float("inf"),
            )
            for circle, (cx, cy) in circles:
                distance = min(distance, ray_circle(ox, oy, dx, dy, cx, cy, circle.radius))
            if unknown or distance < range_min:
                distance = float("nan")
            elif distance > range_max:
                # Explicit simulator convention: infinity is a known max-range
                # no-return, enabled through Config.no_return_is_clear below.
                distance = float("inf")
            ranges.append(distance)
        return Scan(
            ranges=tuple(ranges), angle_min=-math.pi, angle_increment=increment,
            range_min=range_min, range_max=range_max, received_at=now,
            sensor_x=sensor_x, sensor_y=sensor_y, sensor_yaw=sensor_yaw,
        )


@dataclass(frozen=True)
class Scenario:
    name: str
    world: World
    duration_s: float = 60.0
    expect_turn: bool = False
    expect_blocked: bool = False
    dropout: Optional[tuple[float, float]] = None
    rearm_at: Optional[float] = None
    unknown_after: Optional[float] = None
    sensor_x: float = 0.0
    sensor_y: float = 0.0
    sensor_yaw: float = 0.0


def scenarios() -> tuple[Scenario, ...]:
    return (
        Scenario("open_path", World(), duration_s=30.0),
        Scenario("wall", World(segments=(Segment(1.1, -3.0, 1.1, 3.0),)),
                 duration_s=90.0, expect_turn=True),
        Scenario("chair_leg", World(circles=(Circle(1.0, 0.0, 0.035),)),
                 duration_s=70.0, expect_turn=True),
        Scenario("corner_trapped", World(segments=(
            Segment(0.47, -0.24, 0.47, 0.24),
            Segment(-0.5, -0.24, 0.47, -0.24),
            Segment(-0.5, 0.24, 0.47, 0.24),
        )), duration_s=8.0, expect_blocked=True),
        Scenario("blocked_rotation", World(segments=(
            Segment(0.47, -1.0, 0.47, 1.0),
            Segment(-0.24, -0.15, -0.24, 0.15),
        )), duration_s=8.0, expect_blocked=True),
        Scenario("scan_dropout", World(), duration_s=10.0,
                 dropout=(3.0, 4.0), rearm_at=5.0),
        Scenario("unknown_ranges", World(), duration_s=7.0, unknown_after=2.0),
        Scenario("moving_obstruction", World(circles=(
            Circle(1.2, 0.8, 0.08, vy=-0.1, stop_at=8.0),
        )), duration_s=70.0, expect_turn=True),
        Scenario("offset_lidar", World(circles=(Circle(1.0, 0.0, 0.035),)),
                 duration_s=70.0, expect_turn=True,
                 sensor_x=-0.03, sensor_y=0.015, sensor_yaw=0.17),
    )


def _approach(value: float, target: float, maximum_change: float) -> float:
    return value + max(-maximum_change, min(maximum_change, target - value))


def _number(value: Optional[float]) -> Optional[float]:
    return round(value, 6) if value is not None and math.isfinite(value) else None


def run_scenario(scenario: Scenario, config: Optional[Config] = None) -> dict:
    """Exercise the real controller with synthetic scans and independent geometry."""
    config = replace(config or Config(), no_return_is_clear=True)
    controller = AvoidanceController(config)
    dt, scan_period = 0.05, 0.1
    acceleration, angular_acceleration = 0.4, 1.5
    x = y = heading = actual_v = actual_w = travelled = 0.0
    minimum_clearance = scenario.world.clearance(x, y, config.robot_radius_m, 0.0)
    contacts = 0
    transitions = []
    trace = []
    failures = []
    previous_state = None
    previous_turn_sign = 0
    turn_direction_flips = 0
    saw_turn = resumed_after_turn = saw_fault = False
    fault_motion_commands = 0
    rearmed = False
    rearm_result = None
    stopped_during_fault = False
    next_scan = 0.0
    first_arm = None
    end_decision = None
    times = int(round(scenario.duration_s / dt))
    for tick in range(times + 1):
        now = tick * dt
        if now + 1e-9 >= next_scan:
            next_scan += scan_period
            missing = scenario.dropout and scenario.dropout[0] <= now < scenario.dropout[1]
            if not missing:
                controller.observe(scenario.world.scan(
                    x, y, heading, now, scenario.sensor_x, scenario.sensor_y,
                    scenario.sensor_yaw,
                    unknown=scenario.unknown_after is not None and now >= scenario.unknown_after,
                ))
        if tick == 0:
            first_arm = controller.arm(now)
        if scenario.rearm_at is not None and now + 1e-9 >= scenario.rearm_at and not rearmed:
            rearm_result = controller.arm(now)
            rearmed = True
        decision = controller.step(now)
        end_decision = decision
        state = str(getattr(decision.state, "value", decision.state))
        if state != previous_state:
            transitions.append({
                "time_s": round(now, 3), "state": state,
                "reason": decision.reason,
                "front_clearance_m": _number(decision.front_clearance),
            })
            previous_turn_sign = 0
        if state == "TURN" or (decision.linear > 0.0 and abs(decision.angular) > 1e-9):
            # A forward arc is also a successful obstacle turn. The geometry
            # checks below still require clearance and meaningful progress.
            saw_turn = True
        if state == "TURN":
            sign = 1 if decision.angular > 0.0 else -1 if decision.angular < 0.0 else 0
            if previous_turn_sign and sign and sign != previous_turn_sign:
                turn_direction_flips += 1
            if sign:
                previous_turn_sign = sign
        elif saw_turn and decision.linear > 0.0 and abs(decision.angular) < 1e-9:
            resumed_after_turn = True
        if state == "FAULT":
            saw_fault = True
        if saw_fault and not rearmed:
            if abs(decision.linear) + abs(decision.angular) > 1e-9:
                fault_motion_commands += 1
            if abs(actual_v) + abs(actual_w) < 1e-9:
                stopped_during_fault = True
        previous_state = state
        if tick % 5 == 0 or tick == times:
            # These are the actual integrated pose/velocity at this control
            # instant; the decision applies to the following integration step.
            trace.append([
                round(now, 4), round(x, 4), round(y, 4), round(heading, 4), state,
                round(actual_v, 4), round(actual_w, 4),
            ])
        if tick == times:
            break
        # Integrate actual acceleration separately from requested commands. Small
        # substeps also check contact between scan/control ticks.
        for substep in range(5):
            sub_dt = dt / 5.0
            actual_v = _approach(actual_v, decision.linear, acceleration * sub_dt)
            actual_w = _approach(actual_w, decision.angular, angular_acceleration * sub_dt)
            mid_heading = heading + 0.5 * actual_w * sub_dt
            x += actual_v * math.cos(mid_heading) * sub_dt
            y += actual_v * math.sin(mid_heading) * sub_dt
            heading += actual_w * sub_dt
            travelled += abs(actual_v) * sub_dt
            sub_time = now + (substep + 1) * sub_dt
            clearance = scenario.world.clearance(x, y, config.robot_radius_m, sub_time)
            minimum_clearance = min(minimum_clearance, clearance)
            if clearance <= 0.0:
                contacts += 1

    if not first_arm or not first_arm[0]:
        failures.append("Controller did not arm from the initial complete healthy scan.")
    if contacts:
        failures.append(f"Robot contacted obstacle geometry on {contacts} integration substeps.")
    if minimum_clearance < config.margin_m - 0.005 and not scenario.expect_blocked:
        failures.append("Minimum physical clearance fell below the configured margin.")
    if scenario.expect_turn and not saw_turn:
        failures.append("The obstruction did not produce a turn.")
    if scenario.expect_turn and not resumed_after_turn:
        failures.append("The controller did not resume forward motion after turning.")
    if scenario.expect_turn and travelled < 0.8:
        failures.append("The obstacle scenario did not make meaningful forward progress.")
    if scenario.expect_blocked:
        if previous_state != "BLOCKED":
            failures.append("The obstructed swept footprint did not finish BLOCKED.")
        if travelled > 0.005 or abs(heading) > 0.005:
            failures.append("The robot moved despite an initially blocked swept footprint.")
    if scenario.name == "open_path" and (x < 1.4 or abs(y) > 0.005 or abs(heading) > 0.005):
        failures.append("Open-path motion did not travel straight at the intended crawl speed.")
    if scenario.dropout or scenario.unknown_after is not None:
        if not saw_fault:
            failures.append("Lost/unknown scans did not produce a latched FAULT.")
        if fault_motion_commands:
            failures.append("A nonzero motion command was issued before explicit fault re-arming.")
        if not stopped_during_fault:
            failures.append("The independently integrated body never stopped during the fault.")
    if scenario.rearm_at is not None:
        if not rearm_result or not rearm_result[0]:
            failures.append("Explicit re-arm failed after fresh healthy scans returned.")
        if end_decision is None or end_decision.linear <= 0.0:
            failures.append("Forward motion did not recover after deliberate re-arming.")
    if scenario.unknown_after is not None and previous_state != "FAULT":
        failures.append("Fully unknown scan data did not remain faulted.")
    if turn_direction_flips:
        failures.append("Turn direction changed within an uninterrupted TURN state.")
    return {
        "name": scenario.name,
        "passed": not failures,
        "failures": failures,
        "duration_s": scenario.duration_s,
        "distance_travelled_m": round(travelled, 6),
        "displacement_m": round(math.hypot(x, y), 6),
        "final_pose": {"x_m": round(x, 6), "y_m": round(y, 6), "yaw_rad": round(heading, 6)},
        "minimum_physical_clearance_m": _number(minimum_clearance),
        "contact_substeps": contacts,
        "turned": saw_turn,
        "resumed_after_turn": resumed_after_turn,
        "turn_direction_flips_within_turn": turn_direction_flips,
        "fault_motion_commands_before_rearm": fault_motion_commands,
        "stopped_during_fault": stopped_during_fault,
        "explicit_rearm_succeeded": None if rearm_result is None else bool(rearm_result[0]),
        "final_state": previous_state,
        "transitions": transitions,
        "geometry": {
            "robot_radius_m": config.robot_radius_m,
            "sensor_pose": [scenario.sensor_x, scenario.sensor_y, scenario.sensor_yaw],
            "segments": [[s.ax, s.ay, s.bx, s.by] for s in scenario.world.segments],
            "circles": [[c.x, c.y, c.radius, c.vx, c.vy, _number(c.stop_at)]
                        for c in scenario.world.circles],
        },
        "trace_columns": ["time_s", "x_m", "y_m", "yaw_rad", "state",
                          "actual_linear_m_s", "actual_angular_rad_s"],
        "trace": trace,
    }


def run_suite() -> dict:
    results = [run_scenario(scenario) for scenario in scenarios()]
    return {
        "validation_scope": "Standalone deterministic 2D raycast and kinematic simulation only",
        "not_validated": [
            "Gazebo or ROS integration", "physical robot or sensors", "serial/firmware",
            "installed footprint and lidar pose", "loaded motor stopping performance",
            "low objects, reflective materials, drop-offs or real lidar occlusion",
        ],
        "model": {
            "body": "circular differential drive; provisional 0.22 m radius",
            "scan_samples": 720, "scan_period_s": 0.1, "control_period_s": 0.05,
            "integration_period_s": 0.01, "linear_acceleration_m_s2": 0.4,
            "angular_acceleration_rad_s2": 1.5,
            "no_return_convention": "positive infinity is known clear to maximum range",
        },
        "passed": all(result["passed"] for result in results),
        "scenario_count": len(results),
        "scenarios": results,
    }


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Write the full JSON simulation report here.")
    args = parser.parse_args(argv)
    report = run_suite()
    encoded = json.dumps(report, indent=2, allow_nan=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded + "\n", encoding="utf-8")
    print(report["validation_scope"])
    for result in report["scenarios"]:
        status = "PASS" if result["passed"] else "FAIL"
        clearance = result["minimum_physical_clearance_m"]
        clearance_text = "no obstacles" if clearance is None else f"clearance={clearance:.3f} m"
        print(f"{status}: {result['name']}; {clearance_text}; contacts={result['contact_substeps']}")
        for failure in result["failures"]:
            print(f"  {failure}")
    if args.output:
        print(f"JSON report: {args.output.resolve()}")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
