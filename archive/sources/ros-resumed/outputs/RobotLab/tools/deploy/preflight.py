#!/usr/bin/env python3
"""Report hardware prerequisites without opening serial ports or moving motors."""
import json
from pathlib import Path
import platform
import shutil
import sys

repo = Path(__file__).resolve().parents[2]
checks = {
    "architecture": platform.machine(),
    "ros_jazzy": Path("/opt/ros/jazzy/setup.bash").exists(),
    "colcon": bool(shutil.which("colcon")),
    "mega_device": Path("/dev/robot_mega").exists(),
    "lidar_device": Path("/dev/robot_lidar").exists(),
    "hardware_build": (repo / "ros2/install/vacuum_hardware").exists(),
    "lidar_source": (repo / "ros2/src/sllidar_ros2").exists(),
}
print(json.dumps(checks, indent=2))
sys.exit(
    0
    if all(
        checks[k]
        for k in (
            "ros_jazzy",
            "colcon",
            "mega_device",
            "lidar_device",
            "hardware_build",
            "lidar_source",
        )
    )
    else 1
)
