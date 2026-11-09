#!/usr/bin/env bash
# Build only the physical-robot packages. Gazebo is not required on the Orange Pi.
set -euo pipefail
robot_repo="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
if [[ ! -f /opt/ros/jazzy/setup.bash ]]; then
  echo 'ROS 2 Jazzy is missing. Run tools/deploy/install-deps.sh first.' >&2; exit 1
fi
set +u
source /opt/ros/jazzy/setup.bash
set -u
cd "$robot_repo/ros2"
if [[ ! -d src/sllidar_ros2 ]]; then
  echo 'Lidar source is missing. Run tools/deploy/fetch-lidar.sh.' >&2; exit 1
fi
colcon build --symlink-install --packages-select vacuum_hardware sllidar_ros2
echo 'Build complete. Run tools/deploy/run-hardware.sh to start disarmed.'
