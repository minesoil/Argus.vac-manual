"""Stationary C1 angle/coverage check. This module has no wheel-control client."""

import argparse
import json
import math
import time

from .c1 import C1Reader


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lidar", required=True)
    parser.add_argument("--seconds", type=float, default=15)
    args = parser.parse_args(argv)
    if not math.isfinite(args.seconds) or args.seconds <= 0:
        parser.error("Use a finite positive duration")
    reader = C1Reader(args.lidar)
    try:
        reader.start()
        deadline = time.monotonic() + args.seconds
        sequence = 0
        while time.monotonic() < deadline:
            if reader.error:
                raise OSError(reader.error)
            sweep = reader.latest
            if sweep and sweep.sequence != sequence:
                sequence = sweep.sequence
                pairs = [(index*5+2.5, value) for index, value in enumerate(sweep.ranges)
                         if math.isfinite(value)]
                nearest = sorted(pairs, key=lambda pair: pair[1])[:12]
                print(json.dumps({"sweep": sequence, "known_bins": len(pairs),
                                  "age_s": round(time.monotonic()-sweep.started, 3),
                                  "nearest_raw_deg_metres": nearest}), flush=True)
            time.sleep(0.2)
        if not sequence:
            raise OSError("No complete revolutions received")
        return 0
    except (OSError, ValueError) as error:
        print("STOP " + str(error), flush=True)
        return 1
    except KeyboardInterrupt:
        return 0
    finally:
        reader.close()


if __name__ == "__main__":
    raise SystemExit(main())
