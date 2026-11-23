"""Record C1 sweeps from the Pi or run them through roaming without driving."""

import argparse
from collections import deque
import json
import math
from pathlib import Path
import time

from .c1 import Sweep
from .c1_bridge import BridgeC1Reader
from .core import AvoidanceController
from .roam import WALL_FOLLOW_SLOW_PERCENT, navigation_config, run


def capture(output, seconds):
    reader = BridgeC1Reader()
    start = time.monotonic()
    previous = None
    count = 0
    with output.open("x", encoding="utf-8") as stream:
        while time.monotonic() - start < seconds:
            sweep = reader.latest
            if sweep is not None and sweep.sequence != previous:
                previous = sweep.sequence
                record = {
                    "at": time.monotonic() - start,
                    "sequence": sweep.sequence,
                    "started": sweep.started - start,
                    "finished": sweep.finished - start,
                    "ranges": [v if math.isfinite(v) else None for v in sweep.ranges],
                    "nodes": sweep.nodes,
                }
                print(json.dumps(record, allow_nan=False), file=stream, flush=True)
                count += 1
            time.sleep(0.04)
    if count == 0:
        raise ValueError("The bridge returned no sweeps")
    print(f"Saved {count} sweeps to {output}")


class ReplayClock:
    now = 0.0

    def __call__(self):
        return self.now

    def sleep(self, seconds):
        self.now += seconds


class ReplayReader:
    error = None

    def __init__(self, path, clock):
        self.clock = clock
        self.current = None
        self.pending = deque()
        with path.open(encoding="utf-8") as stream:
            for line in stream:
                record = json.loads(line)
                ranges = tuple(math.nan if v is None else float(v) for v in record["ranges"])
                if len(ranges) != 72:
                    raise ValueError("Expected 72 bins per C1 sweep")
                sweep = Sweep(record["sequence"], record["started"], record["finished"],
                              ranges, record["nodes"])
                if self.pending and record["at"] < self.pending[-1][0]:
                    raise ValueError("Capture times must be in order")
                self.pending.append((record["at"], sweep))
        if not self.pending:
            raise ValueError("The capture has no sweeps")
        self.end = self.pending[-1][0]

    @property
    def latest(self):
        while self.pending and self.pending[0][0] <= self.clock():
            _, self.current = self.pending.popleft()
        return self.current


def replay(log, profile):
    clock = ReplayClock()
    reader = ReplayReader(log, clock)
    side = profile.get("follow_wall")
    cruise = profile.get("cruise", 18)
    controller = AvoidanceController(navigation_config(profile["radius"], profile.get("wall_gap", 0.30)),
                                     follow_wall=side,
                                     finish_at_wall_end=profile.get("finish_at_wall_end") is True)
    seconds = min(profile.get("seconds", 30), reader.end + 0.061)
    return run(reader, controller, seconds=seconds, front_deg=profile["front_deg"],
               x=profile["sensor_x"], y=profile["sensor_y"], cruise=cruise,
               slow=profile.get("slow", 12), turn=profile.get("turn", 15), clock=clock,
               sleep=clock.sleep, fast_wall_trial=bool(side and cruise > WALL_FOLLOW_SLOW_PERCENT),
               stop_ahead=profile.get("stop_ahead") is True)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    record = commands.add_parser("capture")
    record.add_argument("output", type=Path)
    record.add_argument("--seconds", type=float, default=10)
    playback = commands.add_parser("replay")
    playback.add_argument("log", type=Path)
    playback.add_argument("--profile", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "capture":
            if not math.isfinite(args.seconds) or args.seconds <= 0:
                parser.error("Capture duration must be finite and positive")
            capture(args.output, args.seconds)
            return 0
        return replay(args.log, json.loads(args.profile.read_text(encoding="utf-8")))
    except (KeyError, OSError, TypeError, ValueError) as error:
        parser.exit(1, f"Replay tool: {error}\n")


if __name__ == "__main__":
    raise SystemExit(main())
