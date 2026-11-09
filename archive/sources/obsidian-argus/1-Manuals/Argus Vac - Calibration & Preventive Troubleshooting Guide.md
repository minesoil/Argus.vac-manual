# My robot's calibration and preventive troubleshooting guide (3.7)

Voice pass 2026-08-25: my procedures, written from my point of view. Updated 2026-09-27 for the power-tool battery switch. Header drift fixed too: the file had still said 3.5 even though the registry already tracked 3.6.

## 1. Why I calibrate

Small hardware mistakes become big navigation errors later. A stepper that skips steps makes my robot think it drove farther than it did. An overheating driver shuts everything down mid-run. These are the settings I check before trusting the hardware.

| Component | Role |
| --- | --- |
| Orange Pi 5 | Vision and AI (runs efficientdet_lite2) |
| Arduino Mega 2560 | Low-level control logic |
| Pololu A4988 | Stepper drivers for locomotion |
| L298N | Driver for the two brushes |
| N20 gear motors | Frontish and Backish brushes |
| Power-tool battery | Main actuator power source, voltage to confirm before wiring |
| LM2596 buck converter | Makes the 5V logic rail |

## 2. Setting the A4988 current limit (Vref)

I set each A4988's current limit with a multimeter. Too low and my motor skips steps under load; too high and the driver cooks itself.

**My formula:** $V_{ref} = I_{trip} \times 8 \times R_{sense}$

Most of my Pololu boards use $R_{sense} = 0.1\,\Omega$. For a 1.0 A limit: $V_{ref} = 1.0 \times 8 \times 0.1 = 0.8$ V.

How I do it:

1. Disconnect the 12 V motor power. Keep the 5 V logic supply on.
2. Meter positive probe on the potentiometer wiper, negative on GND.
3. Turn the screw in small steps until I read the target voltage.

I pick the lowest setting that climbs my carpet without skipping. Higher current buys torque but makes heat, so I stop at "just enough".

## 3. L298N thermal behavior

The L298N is an old BJT design and burns roughly 1.4 to 3 V across itself. If I use a 12 V-class actuator rail, the brush motors see less than rail voltage and the lost power becomes heat in the chip. If the power-tool pack is 18 V or 20 V, I do not feed the N20 motors directly until I confirm their voltage rating or add a buck converter.

What I check:

- The heat sink sits tight; vibration loosens them.
- Neither brush drags. One blocked brush loads one half of the H-bridge harder than the other and ages it faster.

I also confirm my LM2596 holds a steady 5 V into the L298N logic pin under load. When it sags, the H-bridge misbehaves even though everything looks wired right.

## 4. Battery safety

The battery is the most dangerous part on my robot.

- I am switching from the LiPo plan to a power-tool battery adapter. The adapter should have 14 AWG red/black leads.
- I meter adapter voltage and polarity before connecting it to the robot.
- The 10 A inline fuse is my last line of defense against a dead short in the motor rails. It goes close to battery positive.

| Battery state | Symptom | Action |
| --- | --- | --- |
| Voltage sag | Motors stutter or driver resets | Stop and recharge or swap pack |
| Polarity wrong | Meter reads negative voltage | Do not connect it |
| Pack voltage too high for a load | Part may overheat or burn out | Add a buck converter or choose a matching part |

## 5. Camera power integrity

My detector runs efficientdet_lite2.tflite; I chose it over smaller models for accuracy.

**USB port rule I follow:** USB 3.0 ports only for the camera. This rule started as pre-build analysis and was then confirmed the hard way: on 2026-08-26 I confirmed the USB 2.0 brownout loop is real - I lived it, not a simulation. An SBC USB 2.0 port fails to supply enough current when the camera starts negotiating its MJPG stream, and the result is a reset/re-enumerate loop that kills the detection thread. The risk comes from stream negotiation itself, not inference resolution; build 10.x no longer upscales frames, but I still start on USB 3.0 and watch for the warning signs.

**Format check (build 9+):** my script reads back what the driver actually applied and warns me if the camera fell back to YUYV. YUYV moves about four times the data of MJPG at 640x480, which halves framerate and makes any current-limiting problem worse. If I see that warning on first live run, I change ports or cable first.

**Floor learning (build 10+):** my unknown-obstacle layer calibrates itself during the first ~25 detection cycles. It must see bare clean floor during those seconds, because whatever it sees becomes its definition of normal. My startup routine: place the robot facing open floor, start the script, wait for "Floor profile learned", then test objects. On patterned carpet I raise ANOMALY_SENSITIVITY if clean floor triggers false boxes; I lower it if subtle items slip through. The layer notices when nearly everything deviates at once (scene changed) and automatically re-learns.

## 6. Serial link rules (not yet commissioned)

As of build 10.x my Pi-to-Mega link is still pre-commissioning: the robot detects but does not move itself yet. Build 10.1 already formats threat packets and can auto-send H above the risk threshold once I flip SERIAL_ENABLED true.

Requirements for when it goes live:

1. Packet framing: commands need clear start/end boundaries so my Mega never executes a half-received fragment.
2. Watchdog: if no valid packet arrives within 500 ms while driving, my Mega must stop all motors on its own. mega-controller.ino has WATCHDOG_MS for exactly this; I leave it at 0 while bench testing.

Framing cuts command jitter. For a vacuum, fast reliable packets are what turn "obstacle detected" into braking instead of a collision.

## 7. My maintenance schedule

- Weekly: inspect Wago lever connectors; confirm levers locked, no migrated wires.
- Bi-weekly: check the tool battery adapter, fuse holder, and battery contacts for heat marks or oxidation.
- Monthly: re-measure A4988 Vref; pots drift.
- After each run: pull hair and debris out of the Frontish/Backish brushes to protect the L298N.
