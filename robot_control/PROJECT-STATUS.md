# Argus robot progress — 2026-11-09

Latest commissioning update: Justin reconnects the Pi and ESP32 and confirms
motor power OFF. ESP32 identity matches the recorded MAC. The prepared phone
Start application uploads successfully, with esptool's data hash verified.
All 88 tests pass using /usr/bin/python3 on the actual Pi. The restarted GPIO
bridge reports STOPPED and zero wheel outputs. Camera preview receives fresh
frames but rejects the initial view as too broadly dark. User phone Start/Stop
and untethered floor tests remain pending. This supersedes the disconnected
and upload-pending state in the earlier deployment section below.

The user now confirms START LINE FOLLOWING appears on the phone, starts AUTO,
and STOP returns it to STOPPED. GPIO verifies zero outputs afterward. Locking
the phone during another motors-off session also returns it to STOPPED. Tape
preview is now clear (offset -0.04, confidence 0.91). These verify software
control with motor power OFF; restored bank power and physical trials remain.

This folder records source, tests, wiring documentation and progress. The
existing website/manual outside this folder preserves earlier project history.

## Confirmed physical results

Orange Pi 5 and power bank are mounted on Argus. The camera is mounted and
aimed at black tape on a light floor. Pi UART physical 8 TX connects to ESP32
GPIO25 RX; physical 10 RX connects to ESP32 GPIO26 TX; physical 6 is common GND.
ESP32 relays commands to the Mega. ESP USB power was moved from the Pi to the
shared power bank; control travels over the three GPIO wires.

Raised wheels moved forward and stopped; the left-only test moved the correct
wheel. A two-second floor run at 25% followed tape and stopped. A later requested
four-second run ended early when the tape became uncertain. Justin reported
about 12 cm of tape remained. Curved-course and untethered operation are unverified.

## Phone Start deployment

Source includes phone Start, one-use request tokens, a 30-second session limit,
a phone heartbeat watchdog, operator Stop and manual takeover. Local validation:
88 Python tests, actual-sketch C++ route/control tests, and browser race tests
passed. Target ESP32 firmware compiled successfully (938244 bytes).

The updated Pi modules were copied on November 8 and argus-bridge.service was
stopped. An attempted Pi test used a missing interpreter path and did not run.
The ESP32 upload and all new live tests remain pending. On November 9 the laptop
Ethernet link is disconnected; Justin cannot reconnect now. This prevents
finishing installation. Do not enable motor power as a substitute for these checks.

## After tape following: camera obstacle warning and stop

Justin wants the camera to warn and stop or steer around obstacles. First build
a stationary detection preview with timestamped frames, bounding boxes, inference
latency and recorded examples from the actual camera. Evaluate cables, shoes,
small dark objects and floor shadows; a class detector will miss unknown objects.

Then add a stop gate in the shared automatic command path. A detected hazard
in the robot's intended path, a stale frame or a detector fault should stop and
require a deliberate restart. Validate with motors off, raised wheels, and slow
supervised trials against soft obstacles. Record false detections and misses.
A monocular camera alone does not establish reliable distance or a clear path.

The RPLIDAR C1 is unavailable after a reported failure; an adapter was ordered,
but the failed component is unconfirmed. Once ranging works, fuse camera labels
with measured clearance before attempting detours. The current tape follower
does not provide obstacle detection, mapping or autonomous room navigation.

## GitHub recording policy

Justin selected minesoil/Argus.vac-manual on November 9. Record source, tests,
sanitized setup instructions, dated decisions and physical test outcomes there.
Keep planned, locally tested, installed and physically verified states distinct.
Future work should end with a reviewed commit and push plus a dated progress
entry. This is a workflow, not an automatic background upload service.

Exclude real Wi-Fi credentials, SSH credentials, config.h, compiled firmware
(which embeds Wi-Fi credentials), private raw chat archives, caches and camera
footage. Retain config examples and test stubs. Review diffs before each push.
