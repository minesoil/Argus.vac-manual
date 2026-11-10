# Camera-assisted manual driving — prototype

This is a calibrated floor-appearance detector plus a firmware stop gate. It
does not identify every object or measure distance. It can flag tape, seams,
shadows or a different floor as well as actual obstacles. Detection performance
and loaded stopping must be checked before relying on it for driving.

## Phone controls

- **ENABLE CAMERA-ASSISTED DRIVE:** requires a fresh clear detector report.
  Forward wheels only, at most 35%. A hazard or lost/stale camera guard stops
  the drive, invalidates its session, and shows a warning. Continuing to hold
  the joystick cannot override that stop.
- When the region becomes clear, driving stays stopped. Deliberately enable
  assisted driving again to acknowledge it and obtain a new session.
- **UNASSISTED MANUAL (NO CAMERA STOP):** preserves the standalone joystick,
  including reverse. This explicit fallback has no obstacle protection.
- **STOP:** always ends the current drive. Tape following also remains a
  separate mode without obstacle protection.

The watched front region is approximate and visible in the Pi preview. It does
not cover the rear, all swept space during turns, or every part of the chassis.
The camera/caster assembly stays physically unchanged.

## Calibration and preview

In the Pi terminal, run from `/home/orangepi/argus/avoidance`:

```sh
./argus obstacle-status
./argus obstacle-calibrate
```

Press STOP and keep motor power OFF for calibration. The default sample is the
lower-left floor patch: normalized x0.04–0.25, y0.86–0.98. That patch must really
be clean floor, not an object. A custom sample uses `--sample x1 y1 x2 y2`.
Ten fresh frames build a frozen color/brightness/texture profile. The profile
is never automatically trained on newly seen objects. Calibration expires
after 15 minutes, fails on geometry changes, and remains private in `.state/`.
While calibration is running the preview reports unavailable, so the guard
cannot treat an in-progress update as clear. The preview reloads an atomic new
profile; a stopped drive still needs explicit acknowledgement.

The preview server listens on Pi localhost port8767; it sends no motor commands.
An SSH tunnel can expose it to the laptop. Its amber box is the watched region;
red boxes are appearance changes. Current status includes camera age and
processing time. The tape-demo background crop is NOT used by this detector.

## How the stop reaches the motors

The single GPIO owner (`argus-bridge.service --manual-guard`) reads local preview
status. Only finite observations no more than250ms old with processing time
at most200ms may report clear. Missing, malformed or stale data reports fault.
Each guard stream has an ESP32-generated token and increasing sequence numbers.
Replacing the stream stops an active assisted session. Invalid/old reports
cannot clear a latch or keep the guard alive.

The ESP32 guard expires after800ms without an accepted update, even if fresh
phone joystick commands continue. The existing350ms driving-command lease is
independent. Those are software deadlines, not measured physical stopping
distances or a safety certification. An obstacle report latches the stop;
later clear reports never resume driving by themselves.

## Commissioning status

Recovered checkpoint, 9 November; documented 10 November without contacting
the robot: Pi source and matching ESP32 firmware are installed. All 103 Python
tests passed locally and on the Pi; actual-sketch C++ and browser checks passed.
The 941568-byte application upload passed esptool's data-hash verification.

Justin confirmed the new buttons are visible and a blocked/unavailable camera
view leaves assisted driving STOPPED with a warning (motor power OFF). After
paper covered the watched region, the live preview reported clear. The next
held-joystick sock/shoe-entry test was requested but no result was received.
Real object-triggered stopping, camera-loss stopping on hardware and loaded
trials remain pending. Do not treat software tests as physical braking evidence.

ESP32 USB was temporarily returned to the Pi for this upload. Restoration to
bank power after this newest update is unconfirmed. Earlier bank-powered GPIO
and raised-wheel tape tests passed before this update. The latest explicit
motor-OFF confirmation is dated 9 November, not a live power-state claim.
