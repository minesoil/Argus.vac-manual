"""Fill an existing literal HTML replay template with verified simulation traces."""

import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("template", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--report", type=Path,
                        default=Path(__file__).resolve().parents[1] / "reports/standalone-simulation.json")
    args = parser.parse_args()
    report = json.loads(args.report.read_text(encoding="utf-8"))
    scenes = [{key: scenario[key] for key in ("name", "geometry", "trace")}
              for scenario in report["scenarios"]]
    fragment = args.template.read_text(encoding="utf-8")
    if fragment.count("__ARGUS_REPLAY_DATA__") != 1:
        raise ValueError("Expected exactly one replay data placeholder")
    data = json.dumps(scenes, separators=(",", ":"), allow_nan=False).replace("<", "\\u003c")
    args.destination.parent.mkdir(parents=True, exist_ok=True)
    args.destination.write_text(fragment.replace("__ARGUS_REPLAY_DATA__", data), encoding="utf-8")
    print(f"Replay generated from {len(scenes)} recorded scenarios; {args.destination.stat().st_size} bytes")


if __name__ == "__main__":
    main()
