#!/usr/bin/env bash
# Run as root only inside the new, approved Ubuntu 24.04 WSL distribution.
set -euo pipefail
source /etc/os-release
[[ "${ID}" == ubuntu && "${VERSION_ID}" == 24.04 ]] || { echo 'Requires Ubuntu 24.04.' >&2; exit 1; }
[[ "$EUID" == 0 ]] || { echo 'Run with sudo or wsl --user root.' >&2; exit 1; }
grep -qi microsoft /proc/sys/kernel/osrelease || { echo 'Expected the dedicated WSL environment.' >&2; exit 1; }
export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y ca-certificates curl locales software-properties-common
locale-gen en_US.UTF-8
update-locale LANG=en_US.UTF-8
export LANG=en_US.UTF-8
add-apt-repository -y universe

# Version and hash obtained from the official ros-infrastructure GitHub release.
deb_path=/var/tmp/vacuum-ros2-apt-source-1.3.0.noble_all.deb
curl --fail --location --proto '=https' --tlsv1.2 --retry 3 \
  'https://github.com/ros-infrastructure/ros-apt-source/releases/download/1.3.0/ros2-apt-source_1.3.0.noble_all.deb' \
  --output "$deb_path"
echo "f31d84adf5054c7d60ded0e82c0f776a77ea33af53d08f40b9ad7c94cca55296  $deb_path" | sha256sum --check --strict
dpkg -i "$deb_path"
apt-get update
apt-get upgrade -y
apt-get install -y \
  ros-jazzy-desktop ros-jazzy-ros-gz \
  ros-jazzy-navigation2 ros-jazzy-nav2-bringup ros-jazzy-slam-toolbox \
  ros-jazzy-ros2-control ros-jazzy-ros2-controllers ros-jazzy-gz-ros2-control \
  ros-jazzy-xacro ros-jazzy-teleop-twist-keyboard \
  ros-dev-tools git build-essential cmake python3-venv python3-pip python3-yaml liburdfdom-tools \
  mesa-utils x11-apps xterm

install -d /var/log/vacuum-robot
dpkg-query -W -f='${Package}\t${Version}\n' > /var/log/vacuum-robot/installed-packages.tsv
echo 'ROS and simulator packages installed. GUI and simulation validation are still required.'
