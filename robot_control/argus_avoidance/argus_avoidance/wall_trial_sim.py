"""Run the roaming wheel mixer in a synthetic box lane, without hardware."""

import argparse
from dataclasses import replace
import json
import math

from .core import AvoidanceController
from .roam import navigation_config, wheels
from .simulate import Segment, World


def simulate(seconds, track, wheel_gain, seam, *, finish_at_wall_end=False, cruise=35,
             tire_width=0.0254, start_side_gap=0.15):
    config = replace(navigation_config(0.15, 0.25), no_return_is_clear=True)
    box_y, row_end = -(config.robot_radius_m + start_side_gap), 0.65
    world = World((
        Segment(-1, box_y, 0.25, box_y),
        Segment(0.25 + seam, box_y, row_end, box_y),
        Segment(-2, -2, 2, -2), Segment(2, -2, 2, 2),
        Segment(2, 2, -2, 2), Segment(-2, 2, -2, -2),
    ))
    controller = AvoidanceController(config, follow_wall="right",
                                     finish_at_wall_end=finish_at_wall_end)
    period = 0.1
    x = y = heading = 0.0
    minimum_gap = -box_y - config.robot_radius_m
    minimum_tire_gap = math.inf
    tire_outer_offset = (track + tire_width) / 2
    peak_command = 0
    previous = None
    transitions = []
    trace = []
    reached_end_at = None
    pauses = 0
    moved = False
    for tick in range(int(seconds / period)):
        now = tick * period
        controller.observe(world.scan(x, y, heading, now, sensor_x=0.08, samples=72))
        if tick == 0:
            controller.arm(now)
        decision = controller.step(now)
        left, right = wheels(decision, cruise, 12, 12, fast_wall_trial=cruise > 15)
        peak_command = max(peak_command, abs(left), abs(right))
        gap = y - box_y - config.robot_radius_m
        # Axle-end projection only. Tread length and rigid protrusions are
        # excluded, so the simulator still checks the circular footprint.
        tire_gap = y - box_y - abs(math.cos(heading)) * tire_outer_offset
        trace.append({"at_s": round(now, 2), "x_m": round(x, 5), "y_m": round(y, 5),
                      "heading_rad": round(heading, 5), "side_gap_m": round(gap, 5),
                      "axle_tire_edge_gap_m": round(tire_gap, 5),
                      "reason": decision.reason, "wheels": [left, right]})
        if decision.reason != previous:
            transitions.append({"at_s": round(now, 2), "x_m": round(x, 3),
                                "reason": decision.reason, "wheels": [left, right]})
            previous = decision.reason
        if x <= row_end:
            minimum_gap = min(minimum_gap, gap)
            minimum_tire_gap = min(minimum_tire_gap, tire_gap)
        if decision.state in ("BLOCKED", "FAULT", "COMPLETE"):
            break
        if moved and left == right == 0:
            pauses += 1
        moved = moved or (left > 0 and right > 0)
        if reached_end_at is None and x >= row_end:
            reached_end_at = round(now, 2)
        forward = wheel_gain * (left + right) / 2
        yaw_rate = wheel_gain * (right - left) / track
        x += forward * period * math.cos(heading + yaw_rate * period / 2)
        y += forward * period * math.sin(heading + yaw_rate * period / 2)
        heading += yaw_rate * period
    return {
        "forward_travel_m": round(x, 3),
        "minimum_modeled_side_gap_m": round(minimum_gap, 3),
        "minimum_projected_axle_tire_edge_gap_m": round(minimum_tire_gap, 3),
        "peak_wheel_command_percent": peak_command,
        "row_end_reached_at_s": reached_end_at,
        "zero_command_ticks_after_motion": pauses,
        "transitions": transitions,
        "trace": trace,
        "scene": {"box_y_m": box_y, "row_start_m": -1.0, "row_end_m": row_end,
                  "first_box_end_m": 0.25, "seam_m": seam,
                  "radius_m": config.robot_radius_m, "sensor_x_m": 0.08},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seconds", type=float, default=10.0)
    parser.add_argument("--track", type=float, default=0.22, help="Assumed wheel track in metres")
    parser.add_argument("--wheel-gain", type=float, default=0.004,
                        help="Assumed wheel speed in m/s per percent command")
    parser.add_argument("--seam", type=float, default=0.04, help="Gap between boxes in metres")
    parser.add_argument("--tire-width", type=float, default=0.0254, help="Tire width in metres")
    parser.add_argument("--start-side-gap", type=float, default=0.15,
                        help="Initial gap from the modeled circle in metres")
    parser.add_argument("--finish-at-wall-end", action="store_true")
    parser.add_argument("--cruise", type=int, choices=range(12, 36), default=35,
                        metavar="12–35")
    parser.add_argument("--trace", action="store_true", help="Include pose and wheel commands for each tick")
    args = parser.parse_args()
    dimensions = (args.seconds, args.track, args.wheel_gain, args.tire_width, args.start_side_gap)
    if not all(math.isfinite(value) and value > 0 for value in dimensions) or not 0 <= args.seam < 0.40:
        parser.error("Use positive finite dimensions and timing, with a seam below 0.40 m")
    report = simulate(args.seconds, args.track, args.wheel_gain, args.seam,
                      finish_at_wall_end=args.finish_at_wall_end, cruise=args.cruise,
                      tire_width=args.tire_width, start_side_gap=args.start_side_gap)
    if not args.trace:
        del report["trace"]
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
