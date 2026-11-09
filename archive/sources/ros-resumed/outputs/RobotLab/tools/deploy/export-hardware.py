#!/usr/bin/env python3
"""Copy a chosen design into the hardware package; preserve physical speed caps."""
import argparse
import json
from pathlib import Path
import sys

repo = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(repo / "designer"))
from model import compile_model, drive_geometry, footprint, hardware_description


def main():
    import yaml

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("design", type=Path)
    args = parser.parse_args()
    design = json.loads(args.design.read_text())
    geometry = drive_geometry(design)
    urdf, meshes = compile_model(design)
    package = repo / "ros2/src/vacuum_hardware"
    (package / "urdf/robot.urdf").write_text(hardware_description(urdf))
    for name, data in meshes.items():
        destination = package / "meshes/design" / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
    config_path = package / "config/hardware.yaml"
    data = yaml.safe_load(config_path.read_text())
    params = data["motor_bridge"]["ros__parameters"]
    params.update(
        wheel_radius_m=geometry["wheel_radius_m"],
        wheel_separation_m=geometry["wheel_separation_m"],
        motion_enabled=False,
    )
    fp = footprint(design)
    xs, ys = [p[0] for p in fp], [p[1] for p in fp]
    data["collision_monitor"]["ros__parameters"]["StopZone"]["points"] = str(
        [
            [min(xs) - 0.15, min(ys) - 0.05],
            [max(xs) + 0.15, min(ys) - 0.05],
            [max(xs) + 0.15, max(ys) + 0.05],
            [min(xs) - 0.15, max(ys) + 0.05],
        ]
    )
    config_path.write_text(yaml.safe_dump(data, sort_keys=False))
    print(
        "Hardware model and geometry updated. Motion stays disabled until calibration."
    )


if __name__ == "__main__":
    main()
