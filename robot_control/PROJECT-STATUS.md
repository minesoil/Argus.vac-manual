# Argus progress — recorded 10 November 2026

The camera-assisted manual prototype is installed on the Pi and ESP32.
Latest robot evidence is from November9; today's work is documentation while
Justin is at school, without connecting to Argus.

## Latest assisted-manual checkpoint

103 Python tests passed locally and on the actual Pi; updated actual-sketch
C++ and browser checks passed. The final ESP32 application upload passed
esptool data-hash verification. Justin confirmed new phone controls and that
a blocked/unavailable scene refuses assisted drive with STOPPED/warning,
motor power OFF. Paper covering the watched region produced a clear preview.

The held-joystick sock/shoe-entry test was requested but no result received.
Real object-triggered stopping, camera-loss stopping on hardware and loaded
braking remain unverified. No stopping distance has been measured. See
[ASSISTED-MANUAL.md](ASSISTED-MANUAL.md).

The detector compares calibrated floor appearance. Tape, seams and shadows
can warn; similar-looking objects can be missed. It is not an object classifier
or distance sensor. Assisted mode is forward-only, capped at 35%, and latches
a stop on hazard or lost guard health. Clear reports never resume motion.
Unassisted manual and tape following have no camera obstacle stop.

The last explicit motor-OFF confirmation is dated November9. ESP32 USB was
temporarily connected to the Pi for this update; returning it to bank power
afterward is unconfirmed. Earlier bank-powered GPIO operation passed.
These are dated observations, not today's live power/connection state.

## Physical results preserved

Pi and power bank are mounted. Current GPIO UART: Pi physical8 TX→ESP25 RX,
physical10 RX←ESP26 TX, physical6 GND. Phone uses the ESP32 hotspot; ESP32
relays percentage commands to the Mega. The recovered Mega baseline is in
the handbook, but its exact installed firmware identity remains unknown.

Both raised wheels moved forward and stopped; left-only matched the left
wheel. Phone Start/Stop and phone-lock stop passed. A two-second tethered 25%
floor trial followed tape and stopped. Joined 45° turns improved but still
stopped early on excess dark coverage. Tape tuning ended to prioritize manual
warning/stop. No completed corner or untethered floor trial is verified;
Justin confirmed Ethernet remained connected in reported floor tests. See
[CORNER-CHECK.md](argus_avoidance/reports/CORNER-CHECK.md).

The camera assembly supports the caster and cannot tilt independently.
Reported ~12cm remaining tape is not a measured camera blind distance.
RPLIDAR C1 is unavailable after a reported failure; adapter ordered, failed
component unconfirmed. ROS2 Humble's LiDAR preview is separate from the
Python/GPIO camera route. No ROS motor integration is commissioned.

## Reproduction and learning records

The [handbook](https://github.com/minesoil/Argus.vac-manual/tree/main/handbook)
contains recovered Pi commands, an ordered reconstruction recipe, reviewed
code snapshots, Mega provenance, hashes and beginner Linux/ROS explanations.
Initial OS/ROS setup was already present; its full history is unavailable.
Historical reports retain their dates.

Next robot task: motors-OFF object/held-joystick stop, then rearm/dropout,
raised-wheel and supervised floor checks. No hardware work occurred during
the November10 documentation session.

## GitHub records

Use minesoil/Argus.vac-manual for reviewed source and dated build records.
Commit meaningful changes; no background upload service exists. Exclude real
configuration/passwords, private calibration, credential-bearing firmware
and caches. Public historical chats/images are sanitized archive copies.
Keep planned, tested, installed and physically verified states distinct.
