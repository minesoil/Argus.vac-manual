# Read the code in a useful order

All paths here are inside [code/robot_control](code/robot_control/README.md).
The [complete index](inventory/FILES.md) covers every included file. This page
explains the main pieces before you open their implementation.

## Orange Pi

| File in `argus_avoidance/` | Responsibility |
|---|---|
| `argus` | Friendly Bash commands such as `check`, `obstacle-status` and `preview`. |
| `argus_avoidance/line_preview.py` | Timestamped camera reads and tape detection; prints decisions without driving by default. |
| `argus_avoidance/follow.py` | Converts tape offset to left/right percentages; manages a bounded automatic session. `--drive` is explicit. |
| `argus_avoidance/serial_control.py` | Maps Pi requests to serial messages and validates replies. |
| `argus_avoidance/usb_bridge.py` | Sole serial owner, localhost API, phone-start supervisor and optional guard publisher. Currently uses `/dev/ttyS0`. |
| `argus_avoidance/obstacles.py` | Calibrates floor appearance, detects changes, serves annotated preview and status. It cannot command motors directly. |
| `argus_avoidance/manual_guard.py` | Converts fresh preview status into token/sequence-protected ESP32 guard messages. |
| `argus_avoidance/core.py` | ROS-independent LiDAR stop/turn decision logic. Not the current camera driver. |
| `argus_avoidance/simulate.py` | Lightweight 2D scenario model for the LiDAR controller. |
| `argus_avoidance/node.py` | Optional ROS 2 subscriptions, transforms, status and preview output around `core.py`. |
| `argus_avoidance/bench.py` | Board/status checks, wall demo and scan listener. |
| `systemd/` | Service definition and bridge override. Startup is separate from explicit drive selection. |
| `config/`, `launch/` | ROS/simulation settings and launch descriptions. Defaults keep output disabled. |
| `setup.py`, `setup.cfg`, `package.xml`, `resource/` | Python/ROS package metadata and discoverability. |
| `tests/` | Behavior, serial, bridge, camera and adapter checks. |
| `reports/` | Dated reports. A historical report is evidence for its date, not a live status page. |
| `.vscode/tasks.json` | Named VS Code tasks around the same command script. |

## ESP32

Read `firmware/esp32_wifi_controlcam_auto/` in this order:

1. `DriveControl.h`: the drive state, ownership and command timeout.
2. `ManualGuard.h`: assisted-mode guard lease, bounds and latched stops.
3. `PhoneStart.h`: phone heartbeat and one-use line-follow request handling.
4. `ControlPacketParser.h`: bounded parsing of Pi serial packets.
5. `esp32_wifi_controlcam_auto.ino`: Arduino `setup()`/`loop()`, UART wiring,
   HTTP routes and embedded phone-page HTML/JavaScript connecting these parts.

`config.h.example` gives the shape of private hotspot settings. The real
`config.h` is excluded. `tests/stubs/config.h` is a harmless test fixture,
not the real credentials; keep it so the host tests compile.

The browser sends requests, but the ESP32 enforces drive ownership and guard
conditions. A red warning in HTML alone would not be a motor stop gate.
The host C++ tests include the actual sketch using fake clocks/network/UART;
the browser tests execute the actual embedded JavaScript using stand-in DOM
and HTTP objects. Neither substitutes for physical timing tests.

## Mega reference

Open [the Mega provenance note](evidence/FIRMWARE_PROVENANCE.md) first.
The M-command sketch uses `AccelStepper`, accepts percentage commands on
Serial1, and repeatedly calls its motor update logic. That is why the Pi can
do slow, irregular camera work while the Mega supplies regular step pulses.

The original and editable baseline differ in comments/startup text; the
control logic matches. A startup banner correction does not prove which
binary is on the Mega. Old CRC and A4988 examples in the project archive are
incompatible families, not interchangeable replacements.

## A few changes you can trace

Search for `wheel_percentages` in `follow.py` to understand sharper tape turns.
Search for `GUARD` and `800` in `ManualGuard.h` to locate the independent guard
deadline. Read the tests next to each behavior before changing it. A speed cap
or deadline is a system setting: changing it on one side may require the Pi
and ESP32 to be updated together.

The dashboard code in `code/dashboard/` is a separate static website. It lists
repository files and renders explanations. It has no access to the robot's
GPIO, motor API or live telemetry.
