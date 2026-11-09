#!/usr/bin/env bash
# For Ubuntu 24.04 arm64/amd64. Inspect this script before running it with sudo access.
set -euo pipefail
source /etc/os-release
if [[ "$ID" != ubuntu || "$VERSION_ID" != 24.04 ]]; then
  echo 'This deployment targets Ubuntu 24.04. Install a supported Orange Pi image first.' >&2; exit 1
fi
case "$(dpkg --print-architecture)" in arm64|amd64) ;; *) echo '64-bit arm64 or amd64 is required.' >&2; exit 1;; esac
sudo apt-get update
sudo apt-get install -y curl ca-certificates python3 git software-properties-common
sudo add-apt-repository -y universe
if ! dpkg-query -W ros2-apt-source >/dev/null 2>&1; then
  robot_tmp="$(mktemp -d)"
  trap 'rm -rf -- "$robot_tmp"' EXIT
  curl -fsSL https://api.github.com/repos/ros-infrastructure/ros-apt-source/releases/latest -o "$robot_tmp/release.json"
  robot_url="$(python3 - "$robot_tmp/release.json" <<'PY'
import json, sys
release = json.load(open(sys.argv[1]))
urls = [a['browser_download_url'] for a in release['assets'] if a['name'].startswith('ros2-apt-source_') and a['name'].endswith('.noble_all.deb')]
if len(urls) != 1 or not urls[0].startswith('https://github.com/ros-infrastructure/ros-apt-source/releases/download/'):
    raise SystemExit('No unique official Ubuntu Noble ROS repository package found.')
print(urls[0])
PY
)"
  curl -fsSL "$robot_url" -o "$robot_tmp/ros2-apt-source.deb"
  sudo dpkg -i "$robot_tmp/ros2-apt-source.deb"
fi
sudo apt-get update
sudo apt-get install -y ros-jazzy-ros-base ros-jazzy-robot-state-publisher ros-jazzy-nav2-collision-monitor ros-jazzy-nav2-lifecycle-manager python3-serial python3-colcon-common-extensions python3-rosdep
echo 'Dependencies installed. Run fetch-lidar.sh, then build-hardware.sh.'
