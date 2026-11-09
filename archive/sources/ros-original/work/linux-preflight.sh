#!/usr/bin/env bash
set -euo pipefail
cat /etc/os-release
id
df -h /
free -h
cat /etc/wsl.conf
cat /etc/apt/sources.list.d/ubuntu.sources
printf 'DISPLAY=%s\nWAYLAND_DISPLAY=%s\nXDG_RUNTIME_DIR=%s\n' "${DISPLAY:-}" "${WAYLAND_DISPLAY:-}" "${XDG_RUNTIME_DIR:-}"
ls -l /dev/dxg /mnt/wslg/.X11-unix/X0
getent hosts packages.ros.org archive.ubuntu.com
