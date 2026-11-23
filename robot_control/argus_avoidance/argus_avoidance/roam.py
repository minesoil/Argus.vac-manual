"""C1 reactive roaming demo; preview by default, faults require a new Start."""

import argparse
from dataclasses import asdict
import json
import math
import signal
import time

from .c1 import C1Reader
from .c1_bridge import BridgeC1Reader
from .core import AvoidanceController, Config
from .follow import ESP32AutoClient, ControlError

WALL_FOLLOW_MAX_PERCENT = 35
WALL_FOLLOW_SLOW_PERCENT = 15
CLOSE_WALL_MAX_PERCENT = 18
FAST_WALL_MAX_SECONDS = 3


class RoamClient(ESP32AutoClient):
    def drive(self, left, right):
        if not self.session:
            raise ControlError("Roaming session is not armed")
        if any(type(v) is not int or not -35 <= v <= 35 for v in (left, right)):
            raise ValueError("Roaming wheel percentage outside commissioned limit")
        self.sequence += 1
        self.request("/auto/drive", {"session": self.session, "seq": self.sequence,
                                     "l": left, "r": right})


def wheels(decision, cruise=18, slow=12, turn=15, *, fast_wall_trial=False):
    if not math.isfinite(decision.angular):
        return 0, 0
    if decision.state == "TURN":
        # Positive core angular velocity means CCW/left.
        if decision.angular > 0:
            return -turn, turn
        if decision.angular < 0:
            return turn, -turn
        return 0, 0
    if decision.state in ("FORWARD", "SLOW"):
        if not decision.close_wall_tracking:
            slow = min(slow, WALL_FOLLOW_SLOW_PERCENT) if fast_wall_trial else slow
        power = cruise if decision.state == "FORWARD" else slow
        if fast_wall_trial:
            clearances = (decision.front_clearance, decision.left_clearance,
                          decision.right_clearance)
            aligned = decision.wall_heading_rad is None or abs(decision.wall_heading_rad) <= 0.12
            clear = (all(value is not None for value in clearances) and
                     clearances[0] >= 0.80 and min(clearances[1:]) >= 0.10)
            power = cruise if aligned and clear and abs(decision.angular) <= 0.20 else slow
        if decision.wall_gap_estimate_m is not None and decision.wall_gap_estimate_m <= 0.13:
            cap = 12
            if decision.close_wall_tracking:
                # Allow faster travel farther from the surface. Taper back
                # before the tightest part of the pass.
                cap = 13
                extra = max(0.0, min(1.0, (decision.wall_gap_estimate_m - 0.061) / 0.026))
                cap += round(extra * (CLOSE_WALL_MAX_PERCENT - cap))
            power = min(power, cap)
        # Keep the slow wall-follow steering authority at higher cruise.
        # Scaling the wheel difference with cruise makes the same correction
        # turn faster and can drive an otherwise clear approach into a stop.
        steering_power = min(power, slow) if fast_wall_trial else power
        differential = min(power - 1, max(1, round(
            steering_power * min(0.5, abs(decision.angular) * 1.8))))
        if decision.angular > 0:
            return power - differential, power
        if decision.angular < 0:
            return power, power - differential
        return power, power
    return 0, 0


def navigation_config(radius, wall_gap):
    """Use one wall spacing target for front stopping and side correction.

    Both readings are measured beyond the inflated circle. Side correction
    starts at wall_gap minus the fixed margin, aiming for roughly wall_gap
    measured from the actual circular body. Front stopping remains more
    conservative: its actual-body gap also includes the margin. The side hard
    stop remains independent and unchanged.
    """
    margin = 0.06
    return Config(robot_radius_m=radius, margin_m=margin,
                  stop_clearance_m=wall_gap,
                  resume_clearance_m=wall_gap + 0.10,
                  side_steer_clearance_m=wall_gap - margin,
                  tracked_wall_stop_m=0.01,
                  tracked_wall_target_m=0.02,
                  scan_timeout_s=0.6)


def run(reader, controller, client=None, seconds=30.0, expected_epoch=None,
        front_deg=0.0, x=0.0, y=0.0, cruise=18, slow=12, turn=15,
        clock=time.monotonic, sleep=time.sleep, emit=print, ended=None, *,
        fast_wall_trial=False, stop_ahead=False, fast_window_s=None):
    start = clock()
    last_sequence = 0
    armed = False
    captured_epoch = expected_epoch
    next_report = 0.0
    last_report = None
    front_close_scans = 0
    try:
        # Capture once BEFORE waiting for the sensor: Stop during startup must
        # invalidate this run instead of being silently acknowledged by arm().
        if client and captured_epoch is None:
            state = client.request("/state")
            if state.get("mode") != "stopped":
                raise ControlError("Press Stop before requesting roaming")
            captured_epoch = state.get("epoch")
            if type(captured_epoch) is not int:
                raise ControlError("Missing ESP32 epoch")
        while seconds is None or clock() - start < seconds:
            if ended and ended():
                emit("END Interrupted")
                return 0
            now = clock()
            if reader.error:
                raise ControlError("C1 acquisition failed: " + reader.error)
            sweep = reader.latest
            new_sweep = sweep is not None and sweep.sequence != last_sequence
            if new_sweep:
                last_sequence = sweep.sequence
                full_resolution = controller.follow_wall and all(map(math.isfinite, sweep.ranges))
                controller.observe(sweep.scan(front_deg, x, y, coalesce=not full_resolution))
            healthy, reason = controller.health(now)
            if not armed:
                if healthy:
                    controller.arm(now)
                    if client:
                        client.arm(expected_epoch=captured_epoch)
                    armed = True
                elif now - start > 5.0:
                    raise ControlError("Cannot start: " + reason)
            decision = controller.step(clock())
            if decision.state in ("FAULT", "BLOCKED"):
                raise ControlError(decision.reason)
            if decision.state == "COMPLETE":
                emit("END " + decision.reason)
                return 0
            if healthy and stop_ahead and new_sweep:
                front = decision.front_obstacle_clearance
                if front is None:
                    front = decision.front_clearance
                if front is not None and front <= 0.30:
                    front_close_scans += 1
                else:
                    front_close_scans = 0
                if front_close_scans >= 3:
                    emit(f"END Front obstacle at {front:.2f} m clearance")
                    return 0
            if seconds is not None and clock() - start >= seconds:
                break
            active_cruise = slow if fast_window_s is not None and now - start >= fast_window_s else cruise
            left, right = wheels(decision, active_cruise, slow, turn, fast_wall_trial=fast_wall_trial)
            if armed and client:
                # Recheck receipt age immediately before each leased command.
                healthy, reason = controller.health(clock())
                if not healthy:
                    raise ControlError(reason)
                client.drive(left, right)
            state = (decision.state, decision.reason)
            if now >= next_report or state != last_report:
                report = asdict(decision)
                report.update(preview=client is None, sweep=last_sequence,
                              wheel_left=left, wheel_right=right,
                              scan_age_s=round(now-sweep.started, 3) if sweep else None,
                              known_bins=sum(math.isfinite(v) for v in sweep.ranges) if sweep else 0)
                report = {key: (None if isinstance(value, float) and not math.isfinite(value)
                                else value) for key, value in report.items()}
                emit(json.dumps(report, allow_nan=False))
                next_report = now + 0.5
                last_report = state
            sleep(0.06)
        emit("END Duration limit reached" if armed else "STOP Duration elapsed before arming")
        return 0 if armed else 1
    except (ControlError, OSError, ValueError) as error:
        emit("STOP " + str(error))
        return 1
    finally:
        if client:
            client.stop()
            client.close()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lidar", required=True)
    parser.add_argument("--drive", action="store_true")
    parser.add_argument("--stop-ahead", action="store_true",
                        help="End after three close front scans at 0.30 m clearance")
    parser.add_argument("--trial", action="store_true",
                        help="Bounded low-power floor commissioning trial; requires explicit duration")
    parser.add_argument("--esp32", default="http://127.0.0.1:8766")
    duration = parser.add_mutually_exclusive_group()
    duration.add_argument("--seconds", type=float, default=30)
    duration.add_argument("--continuous", action="store_true")
    parser.add_argument("--front-deg", type=float,
                        help="Raw C1 angle pointing robot-forward, measured with a front target")
    parser.add_argument("--sensor-x", type=float, default=0.0)
    parser.add_argument("--sensor-y", type=float, default=0.0)
    parser.add_argument("--radius", type=float, default=0.23,
                        help="Circle about drive rotation centre containing the whole robot, metres")
    parser.add_argument("--wall-gap", type=float, default=0.30,
                        help="Front clearance beyond inflated radius; adjusts side steering (0.20 to 0.40 m)")
    parser.add_argument("--follow-wall", choices=("left", "right"),
                        help="Track the selected wall during a bounded low-speed demo")
    parser.add_argument("--finish-at-wall-end", action="store_true",
                        help="Finish a wall pass after confirming the end of the tracked surface")
    parser.add_argument("--close-wall-radius", type=float,
                        help="Verified clearance from the axle midpoint for a tracked side wall, in metres")
    parser.add_argument("--commissioned", action="store_true",
                        help="Confirm sensor pose, footprint, low-speed wheel direction and braking checks")
    parser.add_argument("--cruise", type=int, default=18)
    parser.add_argument("--slow", type=int, default=12)
    parser.add_argument("--turn", type=int, default=15)
    parser.add_argument("--expected-epoch", type=int, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    values = (args.seconds, args.sensor_x, args.sensor_y, args.radius, args.wall_gap,
              args.front_deg if args.front_deg is not None else 0)
    if not all(math.isfinite(v) for v in values) or args.seconds <= 0 or args.radius <= 0:
        parser.error("Geometry and duration must be finite; duration and radius positive")
    max_cruise = WALL_FOLLOW_MAX_PERCENT if args.follow_wall else 25
    if not 1 <= args.slow <= args.cruise <= max_cruise or not 1 <= args.turn <= 20:
        parser.error(f"Require 1 <= slow <= cruise <= {max_cruise} and 1 <= turn <= 20")
    if not 0.20 <= args.wall_gap <= 0.40:
        parser.error("Require 0.20 <= wall-gap <= 0.40 m pending loaded stopping validation")
    if args.finish_at_wall_end and not args.follow_wall:
        parser.error("--finish-at-wall-end requires --follow-wall")
    if args.trial:
        cruise_limit = WALL_FOLLOW_MAX_PERCENT if args.follow_wall else 12
        if args.continuous or args.seconds > 20 or args.cruise > cruise_limit or args.turn > 12:
            parser.error(f"Trial requires <=20 seconds, <={cruise_limit}% cruise and <=12% turn")
        args.drive = True
    if args.drive and (args.front_deg is None or not (args.commissioned or args.trial)):
        parser.error("Driving needs measured --front-deg and completed --commissioned checks")
    fast_wall_trial = bool(args.follow_wall and args.cruise > WALL_FOLLOW_SLOW_PERCENT)
    close_wall = args.close_wall_radius is not None
    slow_limit = CLOSE_WALL_MAX_PERCENT if close_wall else WALL_FOLLOW_SLOW_PERCENT
    if args.drive and args.follow_wall and (args.continuous or args.seconds > 20 or
                                          args.slow > slow_limit or args.turn > 12):
        parser.error(f"Wall-follow driving requires <=20 seconds, <={slow_limit}% slow speed and <=12% turn")
    fast_limit = 10 if args.stop_ahead else FAST_WALL_MAX_SECONDS
    if args.drive and fast_wall_trial and (not args.trial or (not close_wall and args.seconds > fast_limit)):
        parser.error(f"Wall-follow cruise above 15% requires a trial of at most {fast_limit} seconds")
    if close_wall and args.drive and not args.trial:
        parser.error("Close wall driving requires a bounded trial")
    try:
        controller = AvoidanceController(navigation_config(args.radius, args.wall_gap),
                                         follow_wall=args.follow_wall,
                                         finish_at_wall_end=args.finish_at_wall_end,
                                         close_wall_radius_m=args.close_wall_radius)
    except ValueError as error:
        parser.error(str(error))
    stopped = [False]
    for sig in (signal.SIGINT, signal.SIGTERM):
        signal.signal(sig, lambda *_: stopped.__setitem__(0, True))
    reader = BridgeC1Reader() if args.lidar == "bridge" else C1Reader(args.lidar)
    try:
        reader.start()
        client = RoamClient(args.esp32, timeout=0.15) if args.drive else None
        return run(reader, controller, client, None if args.continuous else args.seconds,
                   args.expected_epoch, args.front_deg or 0, args.sensor_x, args.sensor_y,
                   args.cruise, args.slow, args.turn, ended=lambda: stopped[0],
                   fast_wall_trial=fast_wall_trial, stop_ahead=args.stop_ahead,
                   fast_window_s=fast_limit if close_wall else None)
    except (OSError, ValueError) as error:
        print("STOP " + str(error), flush=True)
        return 1
    finally:
        reader.close()


if __name__ == "__main__":
    raise SystemExit(main())
