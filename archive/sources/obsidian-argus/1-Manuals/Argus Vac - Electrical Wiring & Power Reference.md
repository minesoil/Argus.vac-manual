# My robot's electrical wiring and power reference (1.11)

Voice pass 2026-08-25: written as my build reference. Facts unchanged. **v1.11 (2026-09-27): Justin confirmed the correct Vref is already known and all parts have arrived except the newest battery system. v1.10 (2026-09-27): power plan changed from LiPo to a power-tool battery adapter with 14 AWG red/black leads pending verification.**

## 1. Two separate power sources

I keep motor current and computing current on completely separate sources. My steppers and brushes pull big sudden currents when they start or stall; if my Pi shared that rail, every motor kick would dent its voltage and risk a crash or SD card corruption. So:

| Domain | Source | Feeds |
| --- | --- | --- |
| Actuators | Power-tool battery through adapter, replacing the earlier 11.1V 3S LiPo plan | Stepper drivers, brush motors, fan, only after voltage is checked |
| Logic | 5000mAh USB power bank | Orange Pi 5 (Raspberry Pi 4B stands in during prototyping) |

The adapter I am waiting for ends in 14 AWG red/black leads. That is not the same thing as changing to a 14 AWG fuse holder. The fuse still belongs close to battery positive. Before I connect this pack to the robot rail, I meter:

- Pack voltage at the adapter leads.
- Polarity, red to positive and black to negative.
- Whether the pack is a 12 V-class pack or an 18 V/20 V tool pack.
- Whether 12 V-only loads need their own buck converter.

If the pack is 18 V or 20 V, the A4988 VMOT input can handle that range, but the N20 motors, fan, and any 12 V-only boards may not. Do not feed those directly until their voltage ratings are checked.

## 2. Distribution with Wago blocks

I wire everything through Wago 221 lever-nut blocks instead of soldering. They clamp tight under vibration, and I can swap any single wire in seconds with no iron. I give positive and negative sides their own blocks so a mixed-up return path cannot happen by accident.

- 12V actuator rail: four Wago 221-415 (5-way) blocks, two positive/negative pairs.
- 5V logic rail: four Wago 221-413 (3-way) blocks, two positive/negative pairs.
- Two Wago 221-412 (2-way) blocks spare for the switch wiring or short jumpers.

All eight 413/415 blocks and the two 412 blocks are on hand as of the 2026-08-25 store run.

My LM2596 buck converter makes the 5 V rail from battery voltage. I check its output with a meter before plugging in logic boards; the L298N refuses to switch cleanly if its logic pin sags.

## 3. The serial link

I connect the Pi to the Mega with a USB cable rather than raw GPIO pins:

- No ground-loop or 3.3 V versus 5 V level problems.
- The shielded cable shrugs off the noise my motors make.
- Connectors survive vibration far better than jumper wires.
- Either board can be replaced without rewiring.

## 4. Arduino Mega pin assignments

This is my authoritative pin map. Both firmware and validator scripts follow it.

| Component                                                                           | Pins        | Signal                        |
| ----------------------------------------------------------------------------------- | ----------- | ----------------------------- |
| Left stepper (A4988)                                                                | 5, 6        | Step, direction               |
| Right stepper (A4988)                                                               | 3, 4        | Step, direction               |
| L298N brush driver                                                                  | 7, 8, 9, 10 | Frontish/Backish motor inputs |
| San Ace 40 fan (drv-1012(marked by fritzing as drv-1012, but is actually an IBT-2)) | 11, 12, 2   | PWM, direction, brake         |

**Mega pin 2 dead (confirmed 2026-08-29). Do not use pin 2 for STEP/DIR. Left stepper uses STEP=5, DIR=6. Right stepper uses STEP=3, DIR=4.**

## 5. Protection parts

A 10 A blade fuse sits on my main battery positive lead, as close to the battery adapter as practical. The old 2026-08-25 plan used a 12 AWG inline fuse holder and rejected 14 AWG because no 14 AWG holder existed. The 2026-09-27 plan is different: the incoming power-tool battery adapter itself has 14 AWG red/black output leads. I still keep the fuse close to battery positive and check wire temps by hand during the first powered bench run. Four electrolytic capacitors (C2 to C5) at the stepper driver inputs absorb back-EMF spikes that would otherwise punch through the A4988 chips.

Parts on hand as of the 2026-08-25 store run:

- 5x 10 A blade fuses (the main fuse spec is 10 A).
- 2x 12 AWG inline fuse holders (old LiPo/final-lead plan). The new adapter has 14 AWG leads, so I need to choose the cleanest fused adapter layout once it arrives.
- DaKoang On-Off-On toggle switch, 6 screw terminals, rated 250 VAC 10 A / 125 VAC 15 A. Its wiring role is not assigned yet; it could be a master power cutoff or a manual brush-direction override.
- 100uF 35V electrolytic caps on hand: enough. All four (C2 to C5) are covered, no more to buy.

Wire status:

- On hand right now: 10 AWG. Fine for bench runs behind the 10 A fuse.
- Still pending: only the newest battery system.

Key specs:

- Battery: power-tool battery, exact voltage to confirm when adapter arrives. Earlier plan was 11.1 V 30C 3S LiPo, 5000 mAh.
- Stepper drivers: Pololu A4988, one per wheel.
- **A4988 power pins (CRITICAL): VMOT <- 12V battery rail (motor power), VDD <- 5V buck rail (logic power), GND common. 12V on VDD destroys logic (max 5.5V). 5V on VMOT starves motor. Verify before powering any driver.**
- Brush driver: L298N running the Frontish and Backish N20 gear motors.
- Cooling: San Ace 40 axial fan via drv-1012.

**NEMA status (2026-09-27): both steppers are mounted below the chassis. One NEMA is wired so far. The other still needs A4988 wiring and wheel-off-ground testing. Justin already knows the correct Vref. Left wheel status from 2026-08-29 remains valid: VMOT=12V in the old bench setup, VDD=5V, GND common, motor cable order correct, STEP=5, DIR=6.**
