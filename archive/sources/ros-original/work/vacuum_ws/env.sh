#!/usr/bin/env bash
# Source from each development terminal. Intended exclusively for local simulation.
export ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST
export ROS_DOMAIN_ID=42
export GZ_PARTITION=vacuum_sim_42
export GZ_IP=127.0.0.1
# Verified WSLg hardware rendering on this PC. Applies only to this workspace.
export GALLIUM_DRIVER=d3d12
export MESA_D3D12_DEFAULT_ADAPTER_NAME=NVIDIA
source /opt/ros/jazzy/setup.bash
vacuum_workspace="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "$vacuum_workspace/install/setup.bash" ]]; then
  source "$vacuum_workspace/install/setup.bash"
fi
unset vacuum_workspace
