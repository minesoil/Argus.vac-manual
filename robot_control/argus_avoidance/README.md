# Argus Pi software

Read [START-HERE.md](START-HERE.md), [current status](../PROJECT-STATUS.md)
and the [handbook](https://github.com/minesoil/Argus.vac-manual/tree/main/handbook).

## Physical camera path

Ordinary Python reads camera snapshots. Tape following and opt-in manual
camera assistance share one GPIO UART bridge on `/dev/ttyS0`,115200baud.
ESP32 hosts phone controls and sends Mega percentage commands. ROS2 is not
in this drive path.

- `line_preview.py`: timestamped snapshots and tape decisions.
- `follow.py`: bounded tape sessions; preview unless `--drive` is explicit.
- `serial_control.py`: framed Pi/ESP32 requests.
- `usb_bridge.py`: one serial owner, local API and phone-start supervisor.
- `obstacles.py`: calibrated appearance preview on localhost:8767.
- `manual_guard.py`: fresh guard reports forwarded by the bridge.
- `systemd/`: observer service and bridge drop-in.

[ASSISTED-MANUAL.md](../ASSISTED-MANUAL.md) explains limits and pending
real-object stop checks. Unassisted manual and tape mode are unprotected.

## Offline LiDAR algorithm and small simulator

`core.py` implements stop/turn decisions; `simulate.py` supplies simplified2D
scans and modeled motion. These use Python3.10+ and the standard library.
Camera features/tests need OpenCV/NumPy; serial runtime needs pyserial.

```bash
python -m unittest discover -s tests -v
python -m argus_avoidance.simulate --output reports/standalone-simulation.json
```

Tests open no motor port. Windows can use Run-Checks.ps1 with an existing
interpreter. Inspect skips if dependencies are absent. Simulation is not
physical lidar or braking validation.

## Optional ROS2 preview

`node.py` wraps the pure algorithm with ROS subscriptions, TF and status.
Verified physical Pi distribution is Humble. Guarded launch selects its
Humble Collision Monitor schema; package/config/launch files describe this
separate path. `./argus preview` uses isolated `/avoidance/` topics with
output disabled. It starts no lidar driver or motor bridge. Missing scans,
TF or guard health keep it disarmed. `/avoidance/set_auto` is not wired to
the ESP32 drive path.

Physical integration still needs a single guarded command owner, measured
geometry, unit conversion and commissioning. Provisional radius0.22m plus
0.03m margin, forward0.05m/s and turn0.30rad/s are software estimates, not
measured hardware settings. Unknown/stale/replayed data deny clearance.

[ORANGE-PI-CHECK.md](reports/ORANGE-PI-CHECK.md) records dated synthetic ROS
tests. [CORNER-CHECK.md](reports/CORNER-CHECK.md) records incomplete tape
turns. Current status supersedes older reports' pending/installed claims.
