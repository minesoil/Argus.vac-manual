"""Run the roaming wheel mixer in a synthetic box lane, without hardware."""

import argparse
from dataclasses import replace
import json
import math

from .core import AvoidanceController
from .roam import navigation_config, wheels
from .simulate import Segment, World


def simulate(seconds, track, wheel_gain, seam):
    config = replace(navigation_config(0.15, 0.25), no_return_is_clear=True)
    box_y, row_end = -0.30, 0.65
    world = World((
        Segment(-1, box_y, 0.25, box_y),
        Segment(0.25 + seam, box_y, row_end, box_y),
        Segment(-2, -2, 2, -2), Segment(2, -2, 2, 2),
        Segment(2, 2, -2, 2), Segment(-2, 2, -2, -2),
    ))
    controller = AvoidanceController(config, follow_wall="right")
    period = 0.1
    x = y = heading = 0.0
    minimum_gap = -box_y - config.robot_radius_m
    previous = None
    transitions = []
    reached_end_at = None
    pauses = 0
    moved = False
    for tick in range(int(seconds / period)):
        now = tick * period
        controller.observe(world.scan(x, y, heading, now, sensor_x=0.08, samples=72))
        if tick == 0:
            controller.arm(now)
        decision = controller.step(now)
        left, right = wheels(decision, 35, 12, 12, fast_wall_trial=True)
        gap = y - box_y - config.robot_radius_m
        if decision.reason != previous:
            transitions.append({"at_s": round(now, 2), "x_m": round(x, 3),
                                "reason": decision.reason, "wheels": [left, right]})
            previous = decision.reason
        if decision.state in ("BLOCKED", "FAULT"):
            break
        if moved and left == right == 0:
            pauses += 1
        moved = moved or (left > 0 and right > 0)
        if x <= row_end:
            minimum_gap = min(minimum_gap, gap)
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
        "row_end_reached_at_s": reached_end_at,
        "zero_command_ticks_after_motion": pauses,
        "transitions": transitions,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seconds", type=float, default=10.0)
    parser.add_argument("--track", type=float, default=0.22, help="Assumed wheel track in metres")
    parser.add_argument("--wheel-gain", type=float, default=0.004,
                        help="Assumed wheel speed in m/s per percent command")
    parser.add_argument("--seam", type=float, default=0.04, help="Gap between boxes in metres")
    args = parser.parse_args()
    if not all(math.isfinite(value) and value > 0 for value in
               (args.seconds, args.track, args.wheel_gain)) or not 0 <= args.seam < 0.40:
        parser.error("Time, track and wheel gain must be positive and seam must be below 0.40 m")
    print(json.dumps(simulate(args.seconds, args.track, args.wheel_gain, args.seam), indent=2))


if __name__ == "__main__":
    main()
