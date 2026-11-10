# Argus on your Orange Pi

The [handbook](https://github.com/minesoil/Argus.vac-manual/tree/main/handbook)
has the full walkthrough. Latest robot evidence is dated November9;
[current status](../PROJECT-STATUS.md) was assembled November10 offline.

## Open the right folder

In VS Code Remote SSH open `/home/orangepi/argus/avoidance`, then Terminal →
New Terminal. Use the everyday orangepi account. Run:

```bash
cd /home/orangepi/argus/avoidance
./argus status
./argus check
```

Services use `/usr/bin/python3`. `~` means the current user's home; it is
`/root` in a root terminal. Use the absolute project path when uncertain.

## Phone controls

Join the ESP32 hotspot and open http://192.168.4.1. Refresh after updates.

- ENABLE CAMERA-ASSISTED DRIVE: forward only, at most35%; requires a fresh
  clear guard. Hazard/unavailable camera stops and latches. Enable again
  deliberately after clear status; it never resumes by itself.
- UNASSISTED MANUAL (NO CAMERA STOP): standalone joystick including reverse.
- START LINE FOLLOWING: requests up to30seconds of tape following. Keep the
  page visible/unlocked. Tape loss, stale camera, phone loss or STOP ends it.
  This mode has no obstacle stop.
- STOP revokes the current drive session.

Assisted mode is installed, but real object/held-joystick and loaded stops
remain pending. Motors-OFF blocked-view refusal passed; paper produced a
clear preview. Read [ASSISTED-MANUAL.md](../ASSISTED-MANUAL.md).

## Commands without driving

| Command | Purpose |
|---|---|
| `./argus` | Help. |
| `./argus status` | Board, Python, ROS and device information. |
| `./argus check` | Software tests; opens no motor port. |
| `./argus demo` | Modeled wall approach. |
| `./argus line-preview --seconds 20` | Tape decisions without driving. |
| `./argus follow` | Tape preview; requires explicit `--drive` for motion. |
| `./argus obstacle-status` | Floor-appearance preview status. |
| `./argus scan` | Up to10seconds listening for scans; starts no driver. |
| `./argus preview` | Optional ROS LiDAR/guard preview, output disabled. |

With motors OFF and controller stopped/zero, `./argus obstacle-calibrate`
samples ten fresh frames from a genuinely clear floor patch. Calibration
expires after15minutes. On first setup inspect raw camera before calibration;
the annotated localhost:8767 preview needs a readable profile. This compares
appearance; it does not identify every object or measure distance.

Current data link is [GPIO UART](PI-ESP32-WIRING.md), `/dev/ttyS0`:
Pi8→ESP25, Pi10←ESP26, Pi6→GND. `argus-bridge.service` is the single serial
owner; `usb_bridge.py` retains its old name. Phone video relay is paused;
Pi processing reads timestamped camera snapshots. Ethernet is for setup/SSH.
Fully untethered floor operation remains unconfirmed.

## Inspect background programs

```bash
systemctl is-active argus-camera.service argus-obstacle-preview.service argus-bridge.service
curl --max-time 5 -sS http://127.0.0.1:8766/state
journalctl -u argus-bridge.service -n 40 --no-pager
```

Services start at boot; the robot starts stopped. Do not run another serial
bridge alongside the service. Press STOP and switch motor power OFF before
maintenance. Closing SSH is not an operator stop.

## ROS is a separate learning path

Pi runs Ubuntu22.04 with ROS2 Humble. Camera/manual drive is ordinary Python
and UART, outside ROS. Run optional colcon builds as orangepi, not root.
C1 is unavailable. Synthetic ROS tests do not prove real scans, transforms
or motor integration; read the handbook before changing launch output.
