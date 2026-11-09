#!/usr/bin/env bash
set -euo pipefail
source /etc/os-release
[[ "$ID" == ubuntu && "$VERSION_ID" == 24.04 && "$EUID" == 0 ]]
if getent passwd robot >/dev/null; then
  echo 'User robot already exists; inspect before modifying.' >&2
  exit 1
fi
if getent passwd 1000 >/dev/null; then
  echo 'UID 1000 already exists; inspect before creating the development user.' >&2
  exit 1
fi
adduser --disabled-password --gecos 'Robot development' --uid 1000 robot
usermod -aG sudo,video,render robot
install -d -m 0755 -o robot -g robot /home/robot/vacuum_ws
cp -a /mnt/c/Users/justi/Documents/Codex/2026-09-30/pl/work/vacuum_ws/. /home/robot/vacuum_ws/
chown -R robot:robot /home/robot/vacuum_ws
cp /etc/apt/sources.list.d/ubuntu.sources /etc/apt/sources.list.d/ubuntu.sources.before-vacuum-setup
sed -i 's#http://archive.ubuntu.com/#https://archive.ubuntu.com/#; s#http://security.ubuntu.com/#https://security.ubuntu.com/#' /etc/apt/sources.list.d/ubuntu.sources
id robot
passwd -S robot
echo 'Regular development user created with locked password. Set a private password in the interactive terminal.'
