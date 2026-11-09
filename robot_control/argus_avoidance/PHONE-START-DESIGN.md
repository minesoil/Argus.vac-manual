# Phone start for the tape follower

Status, 2026-11-09: ESP32 upload hash verified; 88 tests pass on the actual Pi.
The GPIO bridge is restarted and reports stopped/zero. Live phone and floor
commissioning remain pending. The camera is fresh but initially rejects the
current dark/ambiguous tape view. The paragraphs below retain earlier history.

The 88 Python tests, actual-sketch C++ tests and embedded browser tests passed.
The ESP32 image compiled at 938244 bytes. The new Pi modules were copied to
the robot on November 8 and its bridge was stopped for deployment. The attempted
Pi test used a nonexistent virtual-environment path and did not run; rerun with
the service's actual interpreter. ESP32 firmware has NOT been updated. Ethernet
is disconnected and Justin cannot reconnect now. Do not call this ready to drive.

The implemented phone Start queues one request bound to a control epoch and
random token. The Pi claims it and launches a session limited to 30 seconds.
The visible phone page sends a heartbeat every 400 ms; one second without it
stops the session. The existing Pi command lease remains 350 ms. Stop/manual
takeover invalidate old requests. Camera/tape uncertainty ends the follower.

To finish: reconnect Ethernet with motor power off, verify deployed files and
the service interpreter, temporarily reconnect ESP USB data for a verified
flash, then test phone Start/Stop with motor power off. Return ESP USB power
to the bank, check raised wheels, and finally perform a supervised untethered
floor trial. Keep the phone page visible and unlocked during a run.

The phone uses the ESP32 hotspot. The Pi and ESP32 exchange control packets
over GPIO UART, so the laptop Ethernet cable is needed for setup and monitoring,
not for carrying the driving commands. A separate on-board Pi and power source
must be secured before moving untethered.

Add an explicit Start request to the phone page and forward that request over
the existing UART to a persistent Pi supervisor. The supervisor should launch
one bounded follower session, only after fresh camera and tape checks. The
request must be one-shot and tied to the ESP32's current epoch: a Stop, manual
takeover, reboot or expired request must invalidate it. It must not start
automatically at boot or restart itself after a fault. Display starting, running,
stopped and failure status on the phone.

Keep the existing 350 ms command lease, phone Stop priority, manual takeover,
stale-camera checks, and scoped automatic cleanup. Verify races involving Stop
before arm, delayed start, duplicate start, restart, link loss and stale camera
in tests; then verify zero-speed operation and raised-wheel Stop before a
supervised floor trial. The current follower is line following: broken lidar
and floor-obstacle detection remain separate unfinished project work.
