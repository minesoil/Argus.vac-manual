# Draft verification on November 7, 2026 (historical)

This report identifies the November7 draft, not the current sketch bytes.
The November9 assisted update was built and upload-hash verified; 103 Pi/Python
tests plus updated actual-sketch C++ and browser checks passed. Actual object
entry/held-joystick stopping remains pending. Current status is in
[ASSISTED-MANUAL.md](../../ASSISTED-MANUAL.md); source hashes are in the
[handbook provenance](https://github.com/minesoil/Argus.vac-manual/blob/main/handbook/evidence/FIRMWARE_PROVENANCE.md).

The final sketch compiled for `esp32:esp32:nodemcu-32s` using ESP32 Arduino
core 3.3.11. Compile-time hotspot values came from the example configuration.

- Program storage uses **933,052 bytes**, 71% of the 1,310,720-byte partition.
- Globals use **95,120 bytes**, 29% of 327,680 bytes of dynamic memory.
- The compiler reports **232,560 bytes** remaining for local variables.
- Firmware build artifacts are under `.tmp/argus-auto-tests/esp32` in the project
  root. The source folder contains about 40 KB of source, examples and tests.

The native C++ check includes the actual sketch and dispatches its registered
HTTP handlers through small WebServer, clock and UART stand-ins. It passed
automatic/manual ownership, stop followed by delayed drive or arm, manual
takeover followed by stale automatic cleanup, the 350 ms expiry boundary,
percentage limits, malformed input, replay rejection, millis rollover and the
camera packet/HTTP relay checks.

The browser check executes the embedded JavaScript with DOM/HTTP stand-ins. It
passed stale and out-of-order state-poll handling, manual selection/takeover,
idle automatic mode, and operator Stop during an outstanding drive request.
The native test binary is `.tmp/argus-auto-tests/host-check.exe`.

The sketch uses the existing synchronous WebServer. Camera writes check expiry
between chunks and use an 80 ms total send budget. Physical upload, UART timing,
camera/control concurrency and loaded stopping remain untested. The host checks
cannot prove those timings. No firmware was flashed or drive request sent.

Final source SHA-256 values:

| File | SHA-256 |
|---|---|
| `esp32_wifi_controlcam_auto.ino` | `6020e61811834514c5abcbe3125d8078238e92b518e01bb3a61964e19bdf9186` |
| `DriveControl.h` | `b656216be965c9d381e05b268e462670ebfdff15020bae55ef224f50b4c16e44` |
