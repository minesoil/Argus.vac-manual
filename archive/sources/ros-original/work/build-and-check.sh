#!/usr/bin/env bash
set -eo pipefail
cd /home/robot/vacuum_ws
source /opt/ros/jazzy/setup.bash
python3 tools/prepare_nav2.py
chmod +x src/vacuum_sim/scripts/twist_adapter.py
colcon build --symlink-install
source env.sh
xacro src/vacuum_sim/urdf/vacuum.urdf.xacro > /tmp/vacuum-verified.urdf
check_urdf /tmp/vacuum-verified.urdf
gz sdf -p /tmp/vacuum-verified.urdf > /tmp/vacuum-verified.sdf
gz sdf -k src/vacuum_sim/worlds/room.sdf
echo '=== Graphics ==='
glxinfo -B
echo '=== Versions ==='
gz sim --versions
ros2 doctor --report
