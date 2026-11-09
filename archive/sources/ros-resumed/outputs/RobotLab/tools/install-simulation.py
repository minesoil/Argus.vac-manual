#!/usr/bin/env python3
"""Install this repository's simulator source into a selected ROS workspace.

The source tree is copied, not linked across Windows/WSL. Existing source/tools
are backed up first. Applied designs remain selected across launcher updates.
"""
import argparse
from datetime import datetime
import json
from pathlib import Path
import shutil
import subprocess
import sys

repo = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo / "designer"))
from model import compile_model


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, required=True)
    args = parser.parse_args()
    workspace = args.workspace.expanduser().resolve()
    if not (workspace / "env.sh").exists():
        workspace.mkdir(parents=True, exist_ok=True)
        (workspace / "env.sh").write_text(
            """#!/usr/bin/env bash
export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST
export ROS_DOMAIN_ID=42
export GZ_PARTITION=vacuum_sim_42
export GZ_IP=127.0.0.1
source /opt/ros/jazzy/setup.bash
robot_workspace="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "$robot_workspace/install/setup.bash" ]]; then source "$robot_workspace/install/setup.bash"; fi
unset robot_workspace
"""
        )
    state = workspace / ".lab"
    state.mkdir(exist_ok=True)
    if (state / "processes.json").exists():
        result = subprocess.run(
            ["python3", "tools/lab_controller.py", "stop"], cwd=workspace
        )
        if result.returncode:
            raise SystemExit("Stop the current simulator before updating source.")
    backup = (
        workspace
        / "model-backups"
        / ("source-update-" + datetime.now().strftime("%Y%m%d-%H%M%S-%f"))
    )
    backup.mkdir(parents=True, exist_ok=True)
    (workspace / "model-backups/COLCON_IGNORE").touch()
    for name in ("src/vacuum_sim", "tools"):
        path = workspace / name
        if path.exists():
            shutil.copytree(
                path, backup / name, ignore=shutil.ignore_patterns("__pycache__")
            )
    selected = (
        json.loads((state / "custom-design.json").read_text())
        if (state / "custom-design.json").exists()
        else None
    )
    shutil.copytree(
        repo / "ros2/src/vacuum_sim", workspace / "src/vacuum_sim", dirs_exist_ok=True
    )
    shutil.copytree(
        repo / "simulation/tools",
        workspace / "tools",
        dirs_exist_ok=True,
        ignore=shutil.ignore_patterns("__pycache__"),
    )
    if not selected:
        shutil.copy2(
            repo / "config/simulation.json", workspace / "tools/robot-profile.json"
        )
        model, meshes = compile_model(
            json.loads((repo / "designs/default.json").read_text())
        )
        (workspace / "src/vacuum_sim/urdf/designed.urdf").write_text(model)
    else:
        model, meshes = compile_model(selected["design"])
        (workspace / "src/vacuum_sim/urdf/designed.urdf").write_text(model)
        # Preserve controller and guard geometry for the selected assembly.
        for filename in ("controllers.yaml", "nav2.yaml", "vacuum_nav2.yaml"):
            previous = backup / "src/vacuum_sim/config" / filename
            if previous.exists():
                shutil.copy2(previous, workspace / "src/vacuum_sim/config" / filename)
    for name, data in meshes.items():
        path = workspace / "src/vacuum_sim/meshes/design" / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    result = subprocess.run(
        [
            "/bin/bash",
            "-lc",
            "source env.sh; colcon build --symlink-install --packages-select vacuum_sim",
        ],
        cwd=workspace,
    )
    if result.returncode:
        raise SystemExit(f"Build failed. Source backup: {backup}")
    print(f"Simulation installed in {workspace}. Previous source: {backup}")


if __name__ == "__main__":
    main()
