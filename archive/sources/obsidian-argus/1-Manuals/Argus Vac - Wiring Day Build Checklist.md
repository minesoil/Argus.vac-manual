# Argus Vac wiring day build checklist

Agent-assembled bench sheet, built 2026-08-25 at Justin's request. Every pin and value comes from my own vault sources: Electrical Wiring & Power Reference v1.11, Calibration Guide v3.7, and the pin definitions inside `mega-controller.ino` and `pi-hardware-validator.py`. Where sources disagreed, the Electrical Reference plus firmware won, because those are marked authoritative and the code actually runs on them. Fuse-holder correction synced 2026-08-25: 12 AWG holders only, no 14 AWG fuse holder; 10 A blade fuses; 10 AWG wire on hand. Power update 2026-09-27: I am switching from LiPo to a power-tool battery adapter with 14 AWG red/black leads, pending voltage and polarity checks. **v1.7 (2026-09-27): Justin confirmed the correct Vref is already known and all parts have arrived except the newest battery system. v1.6 (2026-09-27): power-tool battery adapter gate added; both NEMAs mounted below chassis, one NEMA wired.**

## 0. One warning before anything

The Fritzing netlist (`Argus Vac_netlist_Final.xml`) and the pinout PNG are from the OLD design (Aug 23 sketch). They show steppers on D2-D5 and the L298N on D46-D52. Do NOT wire from them. The current authoritative map, confirmed identical in all three live sources, is:

| Component | Mega pins |
| --- | --- |
| Left A4988 | STEP 5, DIR 6 |
| Right A4988 | STEP 3, DIR 4 |
| L298N brush inputs | IN1 7, IN2 8, IN3 9, IN4 10 |
| drv-1012 fan driver | PWM 11, DIR 12, BRAKE 2 |

**Mega pin 2 dead (confirmed 2026-08-29). Do not use pin 2 for STEP/DIR. Left stepper uses STEP=5, DIR=6. Right stepper uses STEP=3, DIR=4.**

Serial: USB cable, 115200 baud, `/dev/ttyACM0`.

## 1. What cannot be finished today

- Newest battery system: still pending. Do not do final battery-side power-up until it arrives and passes voltage/polarity checks.
- Vref: correct value is already known. Use that setting instead of treating Vref as an unknown tuning task.

## 2. Bench setup

Have within reach:

- [ ] Multimeter with fresh battery
- [ ] Wire strippers and spare hookup wire
- [ ] Dupont jumper wires for all Mega signal connections
- [ ] USB A-to-B cable (Pi to Mega)
- [ ] Power-tool battery adapter, when it arrives
- [ ] Multimeter leads ready for adapter voltage and polarity checks
- [ ] Fire-safe charging spot for whatever battery chemistry the tool pack uses

Color code so mistakes are visible: red battery positive, black battery negative, red thin for 5 V positive, black thin for 5 V ground, any colors for signal jumpers. The new adapter should already bring out red/black 14 AWG leads. Confirm with a meter anyway.

Golden rules for the whole day:

1. Battery and power bank stay separate forever. Positives never meet.
2. All grounds DO meet, at the negative Wago blocks. Signals cannot work without a shared ground reference.
3. No wire moves until the battery is disconnected.
4. Never unplug a stepper motor while the driver has motor power. That kills A4988s instantly.

## 3. Stage A: battery adapter and main fuse

- [ ] 1. Battery disconnected from everything.
- [ ] 2. Inspect the new adapter. Confirm red is positive and black is negative with the meter, not by trust.
- [ ] 3. Write down pack voltage at the adapter leads. If it is an 18 V or 20 V tool pack, stop and decide which loads need buck converters before connecting motors or fan.
- [ ] 4. Put the 10 A blade fuse on the POSITIVE path, as close to the battery adapter as practical.
- [ ] 5. Seat the fuse with a firm push, then tug it. It should not move.
- [ ] 6. Meter across the fuse: should read about 0 ohms with the battery unplugged.

## 4. Stage B: 12V distribution (Wago 221-415, one pair)

- [ ] 1. Take one 5-way block for positive, one for negative. These are the heart of the 12V rail.
- [ ] 1a. If the tool pack is not 12 V-class, do not call this a 12V rail until a buck converter creates 12 V. Label the raw battery rail by its real voltage.
- [ ] 2. Into POSITIVE block: fused battery positive, LM2596 input plus, L298N supply only if voltage rating is safe, left A4988 VMOT, right A4988 VMOT. That fills four of five slots; the fifth stays free for the fan driver's supply.
- [ ] 3. Into NEGATIVE block: battery negative, LM2596 input minus, L298N GND, left A4988 GND, right A4988 GND.
- [ ] 4. Wago technique: strip about 1 cm, lift the lever fully, push wire in until it stops, snap the lever down, tug each wire hard. A wire that survives a firm pull is in.
- [ ] 5. The second 221-415 pair is spare. Use its slots when the fan driver needs a tap.

## 5. Stage C: the 5V rail (LM2596)

- [ ] 1. Buck INPUT terminals go to the 12V pair. Polarity matters: plus to plus, minus to minus. Double-check before moving on.
- [ ] 2. Nothing connected to the OUTPUT yet. Connect the battery for ten seconds ONLY to power the buck.
- [ ] 3. Meter on the output screws. Turn the trimmer screw slowly with a small screwdriver until it reads 5.05 V (accept 5.00 to 5.10).
- [ ] 4. Battery off again.
- [ ] 5. Now wire the OUTPUT to a Wago 221-413 pair. This is the 5V logic rail.
- [ ] 6. Feeders into the 5V POSITIVE block: both A4988 VDD pins, the L298N 5V pin, and the drv-1012 logic supply.
- [ ] 7. Feeders into the 5V NEGATIVE block: matching returns. The negative blocks of both rails connect through the buck's own input-minus and output-minus, which makes one continuous ground network. That is correct and wanted.

## 6. Stage D: A4988 stepper drivers

For EACH driver (left and right):

- [ ] 1. VMOT to the 12V positive block, GND to a negative block.
- [ ] 2. One 100 uF 35V electrolytic directly across VMOT and GND at the driver. Striped leg to GND. This cap is the driver's seatbelt.
- [ ] 3. VDD to the 5V positive block, and the driver's other GND pin to the 5V negative block.
- [ ] 4. **VERIFY VMOT/VDD ORIENTATION: VMOT must go to 12V rail, VDD to 5V rail. 12V on VDD (max 5.5V) destroys the driver. 5V on VMOT starves the motor. Check twice before powering.**
- [ ] 5. Jumper SLEEP to RESET on the board itself. Without this the driver sleeps forever.
- [ ] 6. Leave MS1-MS3 and ENABLE unwired for now (full-step mode, always enabled). Microstepping comes later in software-friendly steps.
- [ ] 7. Signal wires to the Mega: LEFT driver STEP to pin 5, DIR to pin 6. RIGHT driver STEP to pin 3, DIR to pin 4.
- [ ] 8. Motor coils: find the two coil pairs with the meter (a few ohms between wires of the SAME coil, open between different coils). Coil one goes to 1A and 1B, coil two goes to 2A and 2B. Write down which color went where on both sides, so a future rewiring keeps wheel directions matching.

Motors stay UNPLUGGED until after the known Vref setting is applied.

## 7. Stage E: Vref, the setting that cooks or starves drivers

Formula: $V_{ref} = I_{trip} \times 8 \times R_{sense}$, with $R_{sense} = 0.1\,\Omega$. For 1.0 A: $V_{ref} = 0.8$ V.

**Vref is already known. These are the two ways to apply or re-check it:**

**With multimeter (precise):**
- [ ] 1. 12V motor power DISCONNECTED (battery unplugged). 5V logic powered (buck output live).
- [ ] 2. Black probe on GND, red probe on the little potentiometer wiper.
- [ ] 3. Turn the screw in tiny steps until the meter reads 0.80 V.
- [ ] 4. Repeat for the second driver.
- [ ] 5. Write the date and value on tape on each board. Pots drift; re-measure monthly.

**By feel (no meter):**
- [ ] 1. 12V motor power DISCONNECTED. 5V logic powered (USB).
- [ ] 2. Turn pot fully counter-clockwise (minimum).
- [ ] 3. Power on 12V. Send step command (diagnostic sketch `f`).
- [ ] 4. Turn pot clockwise 1/8 turn at a time. After each turn, try to hold motor shaft.
- [ ] 5. Stop when shaft holds firmly (solid holding torque). Driver warm, not hot.
- [ ] 6. Write date on tape. Re-check after 5 min warm-up.

Start at 0.8 V and only raise if the robot fails to climb carpet without skipping. Heat kills these chips faster than low torque annoys you.

## 8. Stage F: L298N brush driver

- [ ] 1. 12V terminal to the 12V positive block, GND to negative.
- [ ] 2. Remove the onboard 5V-enabler jumper and feed the board's 5V pin from the logic rail instead. Your calibration guide checks for a steady 5V into the L298N logic pin under load, so it expects the external feed.
- [ ] 3. IN1 to pin 7, IN2 to pin 8, IN3 to pin 9, IN4 to pin 10.
- [ ] 4. Keep BOTH enable jumpers (ENA, ENB) installed so the bridge is always active; the firmware does not drive enable pins.
- [ ] 5. OUT1-OUT4: leave empty, put tape labels FRONTISH-A, FRONTISH-B, BACKISH-A, BACKISH-B next to them.
- [ ] 6. Know ahead of time: the L298N burns 1.4 to 3 V internally. If the new tool battery is higher than 12 V, do not assume the N20s are safe. Check their voltage rating first.

N20s are now available: motor wires to OUT terminals, one 100 uF cap across each motor's terminals (C4 and C5 in the plan), then `B 1` over serial.

## 9. Stage G: fan driver (drv-1012)

- [ ] 1. Motor supply side to the actuator rail only after the pack voltage and fan rating match. Use the spare 221-415 pair.
- [ ] 2. Logic supply to the 5V rail.
- [ ] 3. PWM to pin 11, DIR to pin 12, BRAKE to pin 2.
- [ ] 4. Fan leads onto the driver's output per the silkscreen labels.
- [ ] 5. Mount the fan horizontally between the plates behind the dust bag per the mechanical manual. Blowing DOWN was the failed v1 layout.

## 10. Stage H: brains

- [ ] 1. Power bank to the Orange Pi 5. Nothing from the robot touches the Pi's power.
- [ ] 2. USB cable from a Pi port to the Mega's USB-B. This is the entire serial link and it also powers the Mega during bench work.
- [ ] 3. While the USB link exists, do NOT also feed the buck's 5V into the Mega's VIN or 5V pin. Two supplies fighting on one pin ends badly. Untethered power for the Mega is a decision for another day.
- [ ] 4. Camera into a USB 3.0 port on the Pi. The USB 2 reconnect loop is CONFIRMED REAL (Incident 4; Justin confirmed 2026-08-26), so this is not optional: blue port, then check dmesg for reconnect spam.

## 11. First power-up, in this exact order

With battery STILL disconnected:

- [ ] 1. Visual audit: every red on a positive path, every black on ground, no stray strands in the Wagos, cap stripes on minus.
- [ ] 2. Meter, resistance mode: fuse reads about 0 ohms. Between 12V positive block and negative block: should NOT beep steadily (the caps may blip the meter, that is fine).
- [ ] 3. Flash the firmware from the laptop:
   `%LOCALAPPDATA%\argus-tools\arduino-cli\arduino-cli.exe upload --input-dir <compiled dir>` or compile-and-upload with `-b arduino:avr:mega`. WATCHDOG_MS ships 0, correct for bench.
- [ ] 4. Plug the Pi/Mega USB in. Open the validator, send `P`. Expect a reply containing ACK. No battery involved yet.

Then battery on:

- [ ] 5. Measure in order: battery 11.0 to 12.6 V, same at the fuse output, same at the 12V block, 5.00 to 5.10 V at the logic block.
- [ ] 6. Wait two minutes, feel-check by hand: fuse holder, buck, both A4988s, L298N. Warm is fine, hot is stop-and-find-out.
- [ ] 7. Wheels off the ground, send `S 1`. Both wheels should turn forward. If ONE wheel spins backward, flip its DIR behavior in software or swap that motor's coil pair at 1A/1B and 2A/2B, never both coils.
- [ ] 8. Send `H`: everything stops instantly and latches. `G` releases with actuators staying off.
- [ ] 9. Send `V 1`: fan spins. Adjust PWM response later.
- [ ] 10. Threat rehearsal without the camera: send `R SOCK 90 320 240`. At risk 85 or higher the Mega auto-halts by itself. That proves the kill chain end to end.

## 12. After wiring day

- [ ] Log the session in the Project Progress note.
- [ ] When the newest battery system arrives, finish Stage A, then update the parts status in HANDOFF.
- [ ] Weekly from now on: check Wago levers locked, no migrated wires. Bi-weekly: balance charge, inspect fuse holder. Monthly: re-measure Vref.
