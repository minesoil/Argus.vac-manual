# Argus robot progress — 2026-11-09

Phone Start firmware is installed and hash verified. All 88 tests pass on the
actual Pi. The real phone Start/Stop and phone-lock stop checks pass; after
restoring ESP USB power to the bank, both raised wheels turn forward from
phone Start and stop on command. The Pi camera/bridge start automatically.

A phone-started floor trial, with Ethernet still connected, stops automatically
near the angled tape. Logs confirm tape-continuity loss, not a session timer.
A stationary frame shows separate straight/diagonal tape components; the lower
piece covers 60.3% of the 116-row analysis band, below the required 70%.
Justin keeps the sharp corner and overlaps the joins; the stationary tape view
then passes at confidence 1.0. Another tethered run starts turning but stops
early: the next image has too little floor visible and tape leaving the lower
right edge. A downward camera adjustment is pending. See
[corner test report](argus_avoidance/reports/CORNER-CHECK.md). A completed
untethered floor trial remains unverified.

This folder records source, tests, wiring documentation and progress. The
dashboard and archive outside this folder provide access to earlier project history.

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

On November 9, the ESP32 application upload passes esptool's data-hash check.
The actual service uses /usr/bin/python3 and /dev/ttyS0; its 88 tests pass.
After reboot with ESP USB powered from the bank, the camera/bridge autostart
and GPIO state remains stopped/zero until an explicit phone Start. USB data
and laptop Ethernet are not part of the driving-command path. Phone controls
pass motors-off and raised-wheel tests; the untethered floor check remains.

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
