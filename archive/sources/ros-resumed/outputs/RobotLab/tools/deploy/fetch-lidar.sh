#!/usr/bin/env bash
# The lock file pins the official SLAMTEC source used by this project.
set -euo pipefail
robot_repo="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.." && pwd)"
robot_revision="$(python3 - "$robot_repo/config/dependencies.json" <<'PY'
import json,sys
print(json.load(open(sys.argv[1]))['sllidar_ros2']['commit'])
PY
)"
robot_target="$robot_repo/ros2/src/sllidar_ros2"
if [[ -d "$robot_target" ]]; then
  if [[ ! -d "$robot_target/.git" ]]; then
    echo 'Bundled lidar source is present; see config/dependencies.json for its revision.'
  elif [[ "$(git -C "$robot_target" rev-parse HEAD)" != "$robot_revision" ]]; then
    echo 'Existing lidar source has a different revision; preserved without reset.' >&2; exit 1
  fi
else
  git clone https://github.com/Slamtec/sllidar_ros2.git "$robot_target"
  git -C "$robot_target" checkout --detach "$robot_revision"
fi
echo "SLAMTEC driver ready at $robot_revision"
