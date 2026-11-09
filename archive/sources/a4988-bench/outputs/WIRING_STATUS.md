# Left-wheel troubleshooting record

Updated: 2026-10-03, record revision 2.2. Sketch revision 1.5.

## Current reported hardware

- Arduino Mega and an A4988 driver, soldered/direct wiring without a breadboard.
- Motor described as NEMA 17HS840; complete model number remains unconfirmed.
- Wheel diameter: 6 cm. User-selected test target: 30 cm/second,
  approximately 95.5 wheel RPM assuming direct drive.
- Direct wheel-to-motor drive and 1.8-degree step angle are calculation assumptions.
- VMOT supply is 12 V. VDD was measured at approximately 5 V.
- User now confirms MS1 disconnected, MS2 connected to 5 V, MS3 disconnected.
  This selects quarter stepping and matches sketch revision 1.5.
- User clarified that revision 1.4 runs smoothly at the 10 cm/second setting;
  it is not jittery. It sounds louder at 10 than at the 60 cm/second setting.
  No sound-level measurement or actual wheel-speed measurement was reported
  for this comparison. No pauses or backward kicks reported for this test.
- At 1 to 5 cm/second the user reports possible skipping and loud operation;
  at 6 to 8 it is reduced, and at 9 to 10 it is minimal. The user clarifies
  that the skipping happens only during startup or speed changes, rather than
  continuing at a fixed speed after five seconds with the wheel raised.
- The nominal command at 10 cm/second is about 424 quarter steps/second,
  or 31.8 wheel RPM. Actual speed is not measured by the sketch.
- EN remains connected; the sketch expects EN on Mega D8.
- The sketch expects STEP on D4 and DIR on D3. Physical pin mapping still needs inspection.
- A shared Arduino/A4988 ground is required; its physical connection still needs inspection.

## Fault to resolve

The Mega shut off when an MS1 connection to its 5 V supply was attempted.
Before that, MS1 and MS2 were reported connected to GND. Whether those original
ground connections were fully removed before adding 5 V is not yet clear.
Connecting an MS input to both 5 V and GND creates a supply short. Wrong pin
identification, solder bridges or driver damage are other possibilities.

Do not reconnect an MS pin to 5 V until its wiring has been inspected with all
power disconnected. Do not reconnect or disconnect motor wires while powered.

## Tracked code

The accompanying `left_wheel_diagnostic/left_wheel_diagnostic.ino` is revision 1.5.
It is a new tracked copy; the original sketch under OneDrive/Desktop was not edited.
Revision 1.0 compilation passed for Arduino Mega 2560 (`arduino:avr:mega`) with Arduino AVR
Boards 1.8.8. The compiler reported only unused-parameter warnings in the Arduino
core. The sketch has not been uploaded or tested on the robot.
Revision 1.1 also compiled successfully for the Mega 2560: 3,902 bytes of program
storage and 209 bytes of global RAM. It has not been uploaded or hardware-tested.
Revision 1.2 compiled successfully for the Mega 2560: 5,338 bytes of program
storage and 209 bytes of global RAM. That revision changed wheel diameter and target speed to
6 cm and 2 cm/second; the running message uses these configured values.
This revision has not been uploaded or hardware-tested.
Revision 1.3 compiled successfully for the Mega 2560: 5,382 bytes of program
storage and 218 bytes of global RAM. It has not been uploaded or hardware-tested.
Revision 1.4 compiled successfully for the Mega 2560 with the already installed
AccelStepper 1.64: 13,336 bytes of program storage and 1,274 bytes of global RAM.
The user has since reported motor behavior with the AccelStepper sketch; Codex
has not uploaded it or observed hardware directly. Host simulation using the actual
installed AccelStepper source with simulated Arduino time, pins and serial passed:
disabled startup, numeric speed commands, increments/decrements, smooth ramps in
both directions, immediate disable/hold, range limits, CRLF, invalid/overlong input,
repeated run commands, serial backpressure and micros() rollover.
Revision 1.5 compiled successfully for the Mega 2560 with AccelStepper 1.64:
13,600 bytes of program storage and 1,396 bytes of global RAM. This revision
has not been uploaded or hardware-tested. The host simulation also passed the
new default gentler ramp, live acceleration changes without a speed jump,
acceleration bounds and invalid acceleration input, plus all prior regression cases.

- MICROSTEPS = 4 matches the requested quarter-step wiring above.
- Motor is disabled after setup and waits for a Serial Monitor command.
- Serial Monitor uses 115200 baud and Newline or Both NL & CR. Send one command:
  r runs, s immediately stops stepping and disables, h immediately stops and holds.
  Uppercase R/S/H also work.
- a2 sets acceleration/deceleration to 2 cm/second squared; a1 makes the ramp
  gentler, a5 makes it faster, and a10 restores revision 1.4's ramp rate.
  The allowed acceleration range is 0.1 to 50 cm/second squared. A commands
  do not enable the motor. Acceleration changes take effect at the next ramp
  update and do not immediately change the current commanded speed.
- + increases the target by 1 cm/second; - decreases it by 1 cm/second.
  A number such as 2, 2.5 or 30 sets the target directly. p reports state,
  target, commanded speed and acceleration; ? shows help. Speed changes alone do not enable
  the motor. Each command executes when its line ending arrives.
- The initial target remains 30 cm/second. The adjustable range is 0 to
  60 cm/second, a software limit rather than a verified motor maximum.
- AccelStepper supplies STEP/DIR pulses with runSpeed(). That function does not
  apply setAcceleration(); an explicit nonblocking velocity ramp applies
  a default 2 cm/second squared during startup and speed increases/decreases.
  From rest to 10 cm/second therefore takes about five seconds; from rest to
  30 takes about fifteen seconds. The prior default was 10 cm/second squared.
- Sending 0 while running ramps down to zero and keeps holding torque.
  s and h act immediately instead of waiting for this ramp.
- Speed converts to steps/second using the 6 cm diameter, 200 full steps/revolution
  and quarter stepping. At 30 cm/second the nominal rate is about 1,273 steps/second,
  or 785 microseconds per step. AccelStepper is serviced repeatedly in loop().
- Serial input avoids blocking reads, and output is queued. If the output queue
  fills under a command flood, feedback may be dropped; commands still execute.
- The minimum STEP pulse width is explicitly set to 5 microseconds.
- Changing MICROSTEPS changes timing only; it does not change physical MS wiring.
- Do not select 1/8 or 1/16 stepping while MS1 has a low-resistance ground path;
  those modes require MS1 HIGH. Quarter stepping requires only MS2 HIGH.
- Sketch still starts disabled; send r with a line ending at 115200 baud to start.
  It does not start automatically and does not set the MS pins.

## Next hardware check

On the 200 Ohm range, MS1-to-GND was reported as 1.2 to 1.3 Ohm and touching
the probe tips together as 0.5 Ohm. The apparent path resistance after accounting
for leads is approximately 0.7 to 0.8 Ohm: effectively a short for a 5 V input.
This is established at the measured points; correct identification of MS1 and
whether the path is on the board or in external wiring still require checking.
Earlier 200 kOhm readings other than MS1-to-GND were described as approximately
90. Earlier steady 1 indications matching separated probes were likely over-range,
not measured 1 Ohm values.
No photograph is currently available; continue with power-off meter checks.

Do not connect MS1 to 5 V while this low-resistance path remains. With all power
disconnected, verify the actual MS1 label and inspect both sides for a ground
link or solder bridge. If inspection does not locate it, isolate the driver board
from external wiring and repeat MS1-to-GND on the board itself. A persistent
near-zero resistance then points to an on-board short or damaged input, provided
pin identification is correct. If it disappears, the external wiring is responsible.
The user requested quarter stepping as a practical workaround rather than further
MS1 isolation. This does not repair the MS1 fault. It avoids tying that pin to 5 V.
The quarter-step configuration may be tested with the wheels raised after all
rewiring is completed with all power disconnected. Stop if the Mega resets or
the motor kicks backward. MS1 must remain disconnected from 5 V.

A photograph of both sides of the driver and its soldered wiring would be helpful
when available, but is not required to continue the resistance checks.

## Current motion and noise observations

Revision 1.5 tests whether a gentler ramp helps the newly reported skipping during
startup and speed changes. The default acceleration is reduced from 10 to 2
cm/second squared, and an a command allows tuning without another upload.
This is a trial adjustment, not a confirmed hardware fix. Slower ramps can also
spend more time in a resonance band, so the result must be observed on the motor.
If it worsens, a10 restores the previous ramp rate while stopped or running.

Recommended first test: upload revision 1.5, raise the wheel, use Serial Monitor
at 115200 baud with Newline, and send a2, then 2, then r as separate commands.
Wait at least five seconds and check startup, then send 3 to compare a speed
change. If improved, a1 gives a gentler ramp for another comparison. If the
skipping instead persists at a fixed speed after the ramp, isolate the driver
and motor's low-speed behavior rather than assuming acceleration is the cause.

At a fixed target, the sketch stops changing commanded speed and continues
polling AccelStepper. Noise does not necessarily increase with speed.
Speed-dependent resonance and phase-current effects remain possible; neither
has been confirmed. The A4988 datasheet describes low-speed microstepping problems
associated with current regulation (Mixed Decay Operation, page 7). This can be
separate from VREF accuracy. No ROSC hardware modification was recommended or made.
Commanded speed is not measured speed.

The user requests reducing sound/vibration at 1 to 5 cm/second without changing
microstepping. Keep the physical quarter-step configuration and MICROSTEPS = 4.
No sketch change was made for this question. Acceleration tuning affects
transitions, not steady-speed step spacing. A suggested first experiment is a
10% reduction from the existing VREF/current setting, recording the original
value and restoring it if motion or load-carrying ability worsens. This is a
trial working-current adjustment, not a claim that the original VREF was wrong.
It has not been performed or reported. Shaft damping and mechanical gearing are
other options; mounting isolation reduces noise transmitted into the chassis.
A hypothetical 10:1 motor-to-wheel reduction would let the motor spin ten times
faster for the same wheel speed, but no gearing change has been made. That would
require multiplying the sketch's steps-per-centimeter by the actual gear ratio.

Reference: Oriental Motor, "Is there a way to reduce vibration during rotation?"
https://faq.orientalmotor.com/is-there-a-way-to-reduce-vibration-during-rotation
The A4988 datasheet also documents a low-speed current-decay adjustment via ROSC;
this is board-specific hardware work, not an Arduino Serial setting. No board
modification was recommended or attempted without verified board identification.

Finer stepping can reduce vibration, but A4988 eighth/sixteenth stepping requires
MS1 HIGH. The measured low-resistance MS1 ground path must be resolved before
enabling those modes on this hardware. Changing MICROSTEPS alone changes the
commanded pulse rate, not the driver's physical step resolution.

Do not use powered reconnection attempts to locate the short. A disabled motor
does not protect the 5 V rail against a wiring short.
