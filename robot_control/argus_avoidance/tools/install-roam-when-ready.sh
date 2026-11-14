#!/usr/bin/env bash
# Explicit install step; requires sudo. Always leaves roaming uncommissioned.
set -euo pipefail
root=/home/orangepi/argus/avoidance
stage=/home/orangepi/argus/roam-stage-20261114
backup="$root/.state/before-roam-$(date -u +%Y%m%dT%H%M%SZ)"
if ! systemctl is-active --quiet argus-bridge.service; then
  echo 'The existing bridge must be active; stopping without changes.' >&2
  exit 1
fi
if ! python3 -c 'import json,urllib.request;s=json.load(urllib.request.urlopen("http://127.0.0.1:8766/state",timeout=2));assert s["mode"]=="stopped" and s["left"]==0 and s["right"]==0'; then
  echo 'Controller is not stopped with zero outputs; stopping without changes.' >&2
  exit 1
fi
mkdir -m 700 "$backup"
for name in core.py usb_bridge.py; do cp -a "$root/argus_avoidance/$name" "$backup/"; done
for name in c1.py c1_bridge.py c1_preview.py lidar_hub.py core.py roam.py usb_bridge.py; do
  install -m 644 "$stage/argus_avoidance/$name" "$root/argus_avoidance/$name"
done
if [[ ! -f "$root/.state/roam.json" ]]; then
  install -o orangepi -g orangepi -m 600 "$stage/config/roam.json" "$root/.state/roam.json"
fi
mkdir -p /etc/systemd/system/argus-bridge.service.d
if [[ -f /etc/systemd/system/argus-bridge.service.d/roam.conf ]]; then
  cp -a /etc/systemd/system/argus-bridge.service.d/roam.conf "$backup/"
fi
install -m 644 "$stage/systemd/argus-bridge-roam.conf" /etc/systemd/system/argus-bridge.service.d/roam.conf
systemctl daemon-reload
systemctl restart argus-bridge.service
systemctl is-active --quiet argus-bridge.service
python3 - <<'PY'
import json
import time
import urllib.request

for attempt in range(30):
    try:
        state = json.load(urllib.request.urlopen('http://127.0.0.1:8766/state', timeout=2))
        assert state['mode'] == 'stopped' and state['left'] == state['right'] == 0
        print(json.dumps({key: state.get(key) for key in ('mode', 'left', 'right', 'epoch')}))
        break
    except (OSError, AssertionError):
        if attempt == 29:
            raise
        time.sleep(0.25)
PY
echo "Installed stopped and uncommissioned. Backup: $backup"
