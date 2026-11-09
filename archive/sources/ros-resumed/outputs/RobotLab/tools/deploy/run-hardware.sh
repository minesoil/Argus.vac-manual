#!/usr/bin/env bash
set -euo pipefail
robot_repo="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
export ROS_DOMAIN_ID="${ROS_DOMAIN_ID:-43}"
export ROS_AUTOMATIC_DISCOVERY_RANGE="${ROS_AUTOMATIC_DISCOVERY_RANGE:-LOCALHOST}"
set +u
source /opt/ros/jazzy/setup.bash
source "$robot_repo/ros2/install/setup.bash"
set -u
exec ros2 launch vacuum_hardware hardware.launch.py "$@"
