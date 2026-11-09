"""Resolve source-repository and deployed-workspace paths in one place."""

import json
import os
from pathlib import Path


def workspace():
    override = os.environ.get("ROBOT_LAB_WORKSPACE")
    if override:
        return Path(override).expanduser().resolve()
    deployed = Path(__file__).resolve().parents[1]
    if (deployed / "src/vacuum_sim").exists():
        return deployed
    return Path(__file__).resolve().parents[2] / "ros2"


def profile_path():
    deployed = workspace() / "tools/robot-profile.json"
    if deployed.exists():
        return deployed
    return Path(__file__).resolve().parents[2] / "config/simulation.json"


def load_profile():
    return json.loads(profile_path().read_text())
