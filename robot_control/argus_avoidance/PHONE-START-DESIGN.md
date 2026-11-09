# Phone start for the tape follower

Status, 2026-11-09: ESP32 upload hash verified; 88 tests pass on the actual Pi.
The GPIO bridge is restarted and reports stopped/zero. Real phone Start/Stop
and phone-lock stop now pass with motor power OFF, and the adjusted tape view
is clear on a continuous strip. Bank-powered GPIO operation and raised-wheel
phone Start/Stop pass. A tethered phone-started floor trial stops near a gapped
angled tape join; the untethered trial remains pending.

The 88 Python tests pass on the actual Pi; actual-sketch C++ and browser tests
pass locally. The ESP32 target image uses 938244 bytes and its uploaded data
hash verifies. Both services start automatically after Pi reboot, then wait
for an explicit Start. Historical deployment issues remain in the dated archive.

The implemented phone Start queues one request bound to a control epoch and
random token. The Pi claims it and launches a session limited to 30 seconds.
The visible phone page sends a heartbeat every 400 ms; one second without it
stops the session. The existing Pi command lease remains 350 ms. Stop/manual
takeover invalidate old requests. Camera/tape uncertainty ends the follower.

Remaining commissioning step: a short supervised floor trial with Ethernet
unplugged, a continuous tape path and phone Stop ready. Keep the phone page
visible and unlocked during a run.

The phone uses the ESP32 hotspot. The Pi and ESP32 exchange control packets
over GPIO UART, so the laptop Ethernet cable is needed for setup and monitoring,
not for carrying the driving commands. A separate on-board Pi and power source
must be secured before moving untethered.

The phone forwards an explicit Start request over the existing UART to a
persistent Pi supervisor. The supervisor launches
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
