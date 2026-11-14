"""C1 stop-turn-continue demo; preview by default, faults require a new Start."""

import argparse
from dataclasses import asdict
import json
import math
import signal
import time

from .c1 import C1Reader
from .core import AvoidanceController, Config
from .follow import ESP32AutoClient, ControlError


class RoamClient(ESP32AutoClient):
    def drive(self, left, right):
        if not self.session:
            raise ControlError("Roaming session is not armed")
        if any(type(v) is not int or not -35 <= v <= 35 for v in (left, right)):
            raise ValueError("Roaming wheel percentage outside commissioned limit")
        self.sequence += 1
        self.request("/auto/drive", {"session": self.session, "seq": self.sequence,
                                     "l": left, "r": right})


def wheels(decision, cruise=18, slow=12, turn=15):
    if decision.state == "TURN":
        # Positive core angular velocity means CCW/left.
        return (-turn, turn) if decision.angular > 0 else (turn, -turn)
    if decision.state == "FORWARD":
        return cruise, cruise
    if decision.state == "SLOW":
        return slow, slow
    return 0, 0


def run(reader, controller, client=None, seconds=30.0, expected_epoch=None,
        front_deg=0.0, x=0.0, y=0.0, cruise=18, slow=12, turn=15,
        clock=time.monotonic, sleep=time.sleep, emit=print, ended=None):
    start = clock()
    last_sequence = 0
    armed = False
    captured_epoch = expected_epoch
    next_report = 0.0
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
                return 0
            now = clock()
            if reader.error:
                raise ControlError("C1 acquisition failed: " + reader.error)
            sweep = reader.latest
            if sweep is not None and sweep.sequence != last_sequence:
                last_sequence = sweep.sequence
                controller.observe(sweep.scan(front_deg, x, y, coalesce=True))
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
            if seconds is not None and clock() - start >= seconds:
                return 0 if armed else 1
            if armed and client:
                # Recheck receipt age immediately before each leased command.
                healthy, reason = controller.health(clock())
                if not healthy:
                    raise ControlError(reason)
                client.drive(*wheels(decision, cruise, slow, turn))
            if now >= next_report:
                report = asdict(decision)
                report.update(preview=client is None, sweep=last_sequence,
                              scan_age_s=round(now-sweep.started, 3) if sweep else None,
                              known_bins=sum(math.isfinite(v) for v in sweep.ranges) if sweep else 0)
                report = {key: (None if isinstance(value, float) and not math.isfinite(value)
                                else value) for key, value in report.items()}
                emit(json.dumps(report, allow_nan=False))
                next_report = now + 0.5
            sleep(0.06)
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
    parser.add_argument("--commissioned", action="store_true",
                        help="Confirm sensor pose, footprint, low-speed wheel direction and braking checks")
    parser.add_argument("--cruise", type=int, default=18)
    parser.add_argument("--slow", type=int, default=12)
    parser.add_argument("--turn", type=int, default=15)
    parser.add_argument("--expected-epoch", type=int, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    values = (args.seconds, args.sensor_x, args.sensor_y, args.radius,
              args.front_deg if args.front_deg is not None else 0)
    if not all(math.isfinite(v) for v in values) or args.seconds <= 0 or args.radius <= 0:
        parser.error("Geometry and duration must be finite; duration and radius positive")
    if not 1 <= args.slow <= args.cruise <= 25 or not 1 <= args.turn <= 20:
        parser.error("Require 1 <= slow <= cruise <= 25 and 1 <= turn <= 20")
    if args.trial:
        if args.continuous or args.seconds > 5 or args.cruise > 12 or args.turn > 12:
            parser.error("Trial requires <=5 seconds, <=12% cruise and turn, no continuous run")
        args.drive = True
    if args.drive and (args.front_deg is None or not (args.commissioned or args.trial)):
        parser.error("Driving needs measured --front-deg and completed --commissioned checks")
    controller = AvoidanceController(Config(robot_radius_m=args.radius, margin_m=0.06,
                                             scan_timeout_s=0.6))
    stopped = [False]
    for sig in (signal.SIGINT, signal.SIGTERM):
        signal.signal(sig, lambda *_: stopped.__setitem__(0, True))
    reader = C1Reader(args.lidar)
    try:
        reader.start()
        client = RoamClient(args.esp32, timeout=0.15) if args.drive else None
        return run(reader, controller, client, None if args.continuous else args.seconds,
                   args.expected_epoch, args.front_deg or 0, args.sensor_x, args.sensor_y,
                   args.cruise, args.slow, args.turn, ended=lambda: stopped[0])
    except (OSError, ValueError) as error:
        print("STOP " + str(error), flush=True)
        return 1
    finally:
        reader.close()


if __name__ == "__main__":
    raise SystemExit(main())
