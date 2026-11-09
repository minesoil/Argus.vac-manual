# My robot: progress log and action plan (3.13)

Voice pass 2026-08-25: my build story, from my point of view. Updated 2026-09-27 for NEMA mounting, one wired NEMA, mounted camera, mounted lidar, the known Vref, and the power-tool battery plan.

## 1. Mechanical build so far

I built the frame from two acrylic plates (30 x 30 x 1 cm) on metal spacers. The brain is an Orange Pi 5; the nervous system is my Arduino Mega 2560 with the motor drivers.

Early testing exposed a suction problem: with my fan blowing straight down, air recirculated instead of pulling from the floor. I fixed it by reorienting the fan horizontal between the plates, right behind a dust bag.

Milestones I have completed:

- Chassis assembled and stress-tested.
- Suction reorientation designed (fan between plates, behind bag).
- Dust bag housing installed.
- Both NEMA steppers mounted below the chassis.
- One NEMA wired so far.
- Camera mounted.
- RPLidar C1 mounted.

## 2. Compute setup

My Orange Pi 5 runs ROS 2 and the vision stack (reached over the Ethernet tether). Two hardware items from pre-build analysis by a previous AI session - robot wiring has not started yet, so neither has been seen for real:

- **Camera brownouts (real - confirmed 2026-08-26).** A USB 2.0 port fails to supply enough current for stream negotiation, producing a disconnect/reconnect loop; I have now confirmed this happens for real, not just in analysis. Rule: camera goes into a USB 3.0 port from day one.
- **No screen on the robot.** I will develop over VS Code Remote-SSH, so the detector already serves an MJPEG stream on port 8000 and I can watch the annotated feed in my laptop browser once the Pi is live.

## 3. Vision system status

My detector runs as decoupled threads (capture, inference, render, stats), so video stays smooth at ~30 FPS no matter how long AI inference takes.

Builds 9 through 10.1 made it accurate and honest:

- Inference runs at native 640x480. A controlled benchmark showed upscaling to 720p added no accuracy while costing CPU, so that idea was dropped.
- A second layer watches the floor itself. It learns what clean floor looks like in its first seconds, then flags anything foreign on it (socks, cables, toy parts) with a clog-risk score, even though no model was ever trained on those items.
- Every cycle it picks the single most dangerous object as "top threat" and can send it to my Arduino over serial (built in 10.1, switched off until I commission the link).

| Metric | Capture | Inference |
| --- | --- | --- |
| Resolution | 640x480 | 640x480 native |
| Format | MJPG | RGB task input |
| Buffer size | CAP_PROP_BUFFERSIZE = 1 | n/a |
| Rate strategy | newest-frame only | 10 Hz cap for CPU headroom |

The software stack uses MediaPipe 1.0.1 Tasks API imports directly (the old mediapipe.solutions fallback is gone from modern builds).

## 4. Parts inventory

| Category             | Items                                                                                                      |
| -------------------- | ---------------------------------------------------------------------------------------------------------- |
| Acquired / installed | Orange Pi 5, Arduino Mega 2560, steppers L/R, RioRand LM2596, Pololu A4988 x2, L298N, DaKoang On-Off-On switch (6-terminal, 250VAC-10A), 5x 10A blade fuses, 2x 12 AWG inline fuse holders, 10 AWG wire (on hand), 2x Wago 221-412, 4x Wago 221-415, 4x Wago 221-413, 2x 100uF 35V electrolytic caps |
| Power plan           | Switching from the 11.1V LiPo plan to a power-tool battery. Adapter parts are shipping and should end in 14 AWG red/black leads. I still need to meter pack voltage and polarity before connecting it to the robot. |
| Pending              | Only the newest battery system. The other robot parts have arrived. |

My RPLidar C1 is mounted now. It still needs wiring/software live testing. It is my bridge to 360-degree sensing later.

*Agent note, 2026-08-25 (evening correction): Justin settled the fuse-holder question: 12 AWG only. The 14 AWG holder claim is gone from every active doc and he did not want 14 AWG at that time. Wire status then: 10 AWG on hand, 12 AWG red/black added to the buy list to pair with the holders.*

*Agent note, 2026-09-27: Justin changed the battery plan. The 14 AWG item now refers to the power-tool battery adapter leads, not a 14 AWG fuse holder. The safety gate is to meter voltage and polarity first, then keep a fuse close to battery positive.*

*Agent note, 2026-09-27 correction: Justin already knows the correct Vref. All parts have arrived except the newest battery system.*

## 5. What comes next

My three-phase plan for making the robot react:

1. **Electrical validation.** Finish pin mapping, apply the known A4988 Vref setting, then test both wheels off the ground.
2. **Protocol.** Define the serial packets from Pi to Mega (threat reports, movement commands).
3. **Reactions.** Mega turns box position and risk into turning or reversing.

After that: SLAM. My RPLidar C1 plus ROS 2 nav2 moves the robot from "avoid what I see" to "map the room and cover it."

Priority sprints:

1. Locomotion and power: verify the new battery adapter, finish the second NEMA, then calibrate stepper currents.
2. Serial link: establish Pi-to-Mega communication (firmware draft exists as mega-controller.ino; validator script ready).
3. Spatial mapping: test the mounted RPLidar C1 and calibrate its angle.

---

*Agent note, 2026-08-25: the benchmark numbers behind section 3 live in `outputs/detector-refine/` if you want the raw data.*
