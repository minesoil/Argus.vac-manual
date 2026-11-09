# Argus Vac: master AI handoff (1.20)

Created 2026-08-25 by Claude (session records live in the change log). Justin switches to a paid AI setup around 2026-09-01; this document exists so the next assistant loses nothing in the move. If you are that assistant: start here, then read AGENTS.md, then skim the change log.

## 0. Read order for a new AI session

1. `AGENTS.md` (vault root): Justin's standing rules.
2. This file: complete context.
3. `3-Logs/argus-vac-version-control-and-change-log-v25.md`: what changed when, per file.
4. `3-Logs/argus-vac-next-steps.md`: current position and ordered next steps.
5. Only then touch anything.

## 1. What this project is

Justin is building an autonomous vacuum robot ("Argus Vac"): Orange Pi 5 brain, Arduino Mega 2560 muscle layer, USB camera + RPLidar C1 sensors, stepper drive, brush sweepers, fan-based suction through a dust bag. The vault is his knowledge base (notes, manuals, logs, software). Development happens from a Windows laptop over OneDrive; runtime target is the Pi over SSH.

## 2. Current state (2026-09-27, NEMAs and sensors mounted)

| Area | State |
| --- | --- |
| Chassis | Built (two 30x30x1cm acrylic plates, spacers, castor front wheel). Both NEMA steppers are now mounted below the chassis. |
| Suction | Reorientation designed (fan horizontal between plates behind dust bag); physical rework still open |
| Camera pipeline | Camera is physically mounted. Detector **10.6** is desk-harness validated (proximity gate on both layers per 10.5; static-structure suppression per 10.6). Needs live mounted-camera test on the robot. |
| Arduino firmware | `mega-controller.ino` draft in vault (reconstruction from documented contract); never flashed/benched; original mega-diagnostic.ino still only in Gemini workspace |
| Serial link | Not commissioned. Validator script ready; protocol defined (P/S/B/V/H/G + R threat packets) |
| RPLidar C1 | Physically mounted. Needs wiring/software live test and mount-angle calibration. |
| ROS 2 | Installed on Pi, unused |
| Missing parts | Only the newest battery system is still pending. Justin says basically all other parts have arrived. |
| Power note | Power plan changed 2026-09-27: Justin is switching from the LiPo plan to a power-tool battery adapter for easier use and safer handling. Adapter should end in 14 AWG red/black leads. Before connecting: meter pack voltage and polarity, keep a 10 A fuse close to battery positive, and do not feed 12 V-only loads from an 18 V/20 V pack without a buck converter. |
| **NEMA drive state (2026-09-27)** | **Both NEMAs mounted below chassis. One NEMA wired so far. Justin already knows the correct Vref. Left-wheel bench facts from 2026-08-29 still matter: VMOT/VDD corrected, Mega pin 2 dead, official left pins STEP=5 DIR=6, motor cable order correct.** |

## 3. File map

```
AGENTS.md                     Justin's standing rules for agents (read first)
CLAUDE.md                     points at AGENTS.md
HANDOFF.md                    this file (v1.16)
  1-Manuals/                    four reports, written in Justin's voice:
    Hardware & Mechanical Architecture Manual   (1.2)
    Electrical Wiring & Power Reference         (1.9) - authoritative pin map
    Calibration & Preventive Troubleshooting    (3.2) - Vref math, LiPo limits, camera rules
    Project Progress & Action Plan              (3.2)
2-Reference/
  ROBOT_MASTER.md             Justin's raw source notes (do not restyle; it is his voice)
3-Logs/
  argus-vac-next-steps.md            roadmap with weekend-only Gantt chart through December 2026
  argus-vac-version-control-...v25   master change log + registry
  argus-vac-developer-preferences-v4.md (v4.2) engineering principles
  argus-vac-housekeeping-and-cleanup-v3.14.md  file purge record and active-file registry
  argus-vac-vscode-setup-v3.md       SSH workflow guide
  argus-vac-historical-troubleshooting-log-v4.6.md (4.6) all four incidents REAL;
                                     Incident 4 fixed by moving camera to a USB 3.0 port
4-Software/
  obstacle-detector-mediapipe-v10.6.py  ACTIVE detector (two layers + proximity gate + dashboard)
  mega-controller.ino                   ACTIVE firmware draft (unvalidated)
  pi-hardware-validator.py              interactive serial test suite
  cv-environment-diagnostic.py          floor/lighting profiler (v1.1)
outputs/detector-refine/       benchmark + test harness (see its README.md)
tools/                         vaultsync.py, parse-fritzing-v1.1.py + fzp_cache/
                               (parses real wiring out of the .fzz; run with --fetch-missing
                               when a new standard part appears)
_Archive/                      v8/v9 detectors, kept until live validation of the current detector (10.6)
5-Hardware/                    Fritzing sketch only (`Argus Vac Final.fzz`) - the wiring
                               source of truth. Netlist exports + pinout PNG deleted
                               (netlist was inaccurate; PNG deleted 2026-08-26 on Justin's order).
copilot/skills/, .agents/skills/, .claude/skills/, .opencode/skills/   agent skills
```

## 4. Hardware facts worth memorizing

- Pin map (authoritative, in the Electrical reference): Left stepper STEP 5 / DIR 6; Right STEP 3 / DIR 4; L298N inputs 7,8,9,10; drv-1012 fan PWM 11, DIR 12, BRAKE 2.
- **Mega pin 2 dead (confirmed 2026-08-29) — left stepper must use STEP=5, DIR=6. Do not use pin 2 for STEP/DIR.**
- Serial contract (matches pi-hardware-validator.py AND mega-controller.ino):
  - `P` ping -> reply contains ACK
  - `S 1`/`S 0` steppers forward/stop
  - `B 1`/`B 0` brushes on/off
  - `V 1`/`V 0` vacuum fan on/off
  - `H` immediate halt (latches), `G` release latch (actuators stay off until re-commanded)
  - `R <name> <risk%> <cx> <cy>` threat report; Mega auto-halts at risk >= 85
  - Baud 115200, port `/dev/ttyACM0`
- Actuator battery plan changed 2026-09-27: power-tool battery adapter with 14 AWG red/black leads, replacing the 11.1 V 3S LiPo plan. Exact pack voltage must be metered before connection. Logic rail is still a separate 5000 mAh power bank. Never merge Pi power with the actuator rail.
- A4988 Vref formula: $V_{ref} = I_{trip} \times 8 \times R_{sense}$, Rsense 0.1 ohm typical, e.g. 0.8 V for 1.0 A.
- **A4988 power pins (CRITICAL - was swapped 2026-08-28): VMOT <- 12V battery rail (motor power), VDD <- 5V buck rail (logic power), GND common. 12V on VDD destroys logic (max 5.5V). 5V on VMOT starves motor. Verify before powering any driver.**
- LiPo alarm at 3.4 V/cell; fuse 10 A on a 12 AWG inline holder (final, settled 2026-08-25: no 14 AWG in this build).

## 5. Detector architecture (obstacle-detector-mediapipe-v10.6.py)

Four threads: capture / inference(+anomaly) / render / stats. MJPEG stream + `/stats` endpoint on port 8000. Single self-contained file by design (copy one file to the Pi).

- Layer 1: MediaPipe EfficientDet-Lite2 float16, VIDEO mode, native 640x480 input, max 10 Hz (INFERENCE_MAX_HZ). Known classes -> green boxes.
- - Web endpoints: `/` mission dashboard (THREAT banner), `/stream` MJPEG, `/stats`, `/threat` JSON.
- Shadow policy: blobs spanning >=85% of view width or height are capped at warning risk (light lines never halt).
- Static-structure suppression (10.6): an unknown-obstacle parked >60s goes quiet (no box/alert/serial); reappears instantly if it moves. Doors/walls are lidar's job.
- Proximity gate (10.4, extended to known classes in 10.5): halt-level risk requires a blob low in frame (center below NEAR_BAND_Y_FRAC=0.70) AND covering >=HALT_MIN_AREA_FRAC=0.06 of view; anything else caps at WARN_RISK_CAP=0.60 so distant or small clutter can never stop the robot. 10.5 fix: known detections (person/chair/...) used to carry raw model confidence and bypassed the gate - a far person at 90% confidence could auto-halt. Now gated like everything else.
- Layer 2 (training-free unknown obstacles): 160x120 analysis copy, 16x12 block grid, per-block hue/saturation/texture features vs a robust floor profile (median+MAD learned over first 25 cycles; must see clean floor at boot). Deviating blocks merge into blobs -> orange "OBSTACLE?" boxes with risk = size + stringy-shape bonus + proximity bonus. Ignores brightness => shadow resistant. Auto re-learns if >70% of ROI flags persistently (scene change).
- Tracks: EMA smoothing (alpha 0.5) matched by name+IoU 0.2, 300 ms hold before expiry. Top threat published as `_latest_risk_summary`.
- Serial (10.1): SERIAL_ENABLED=False default. Sends `R ...` on meaningful threat change; auto-H above THREAT_HALT_RISK=0.85 with 3 s resend cap; NEVER auto-sends G.
- Measured: detect ~107 ms avg desktop (expect slower on Pi), anomaly layer ~2 ms/cycle, 0% false alarms on synthetic clean floor, 100% debris flag rate. Harness: `outputs/detector-refine/test_v10.py` (29 checks).

Key lesson baked into preferences: do NOT upscale frames for inference. Benchmark showed zero accuracy gain, real CPU cost, plus 4:3-to-16:9 distortion. See bench_accuracy.py evidence.

## 6. Conventions Justin set (follow without being asked)

- Address him as Justin, every response. Plain simple language, short replies, no walls of text.
- Humanizer style for anything written into the vault: no em dashes, no inflated claims, no bold-label list spam, plain verbs.
- Manuals are written in JUSTIN'S voice (first person). Agent contributions go in clearly separated agent-note sections or agent-log blocks.
- Versioning: decimal bumps on the SAME file for small changes, AND rename the filename to match (10 -> 10.1 means renaming the file and updating every reference). New whole-version file only for major rewrites (old file to `_Archive/`). Log every bump in the change log.
- Registry sync mandate: code changes ripple into manuals/logs same-session; the change log registry is the source of truth. Sync every affected file every time without asking first (Justin's standing rule, added 2026-08-26).
- Benchmark before optimizing: validate performance claims with the harness, not intuition.
- Do not always assume Justin is right (his own rule); push back politely with evidence when he is not.

## 7. Environment quirks

Windows laptop (development):
- Python 3.12 at `%LOCALAPPDATA%\Programs\Python\Python312\python.exe` (has opencv 5.0.0, mediapipe 1.0.1, numpy 2.5.2 installed).
- Python's SSL fails cert verification on this machine (`certificate has expired`) - use curl.exe for downloads, not urllib/pip index issues aside.
- Node.js v24 installed via winget at `C:\Program Files\nodejs` (npx works; skills CLI used it).
- arduino-cli 1.5.2 at `%LOCALAPPDATA%\argus-tools\arduino-cli\arduino-cli.exe`; AVR core present; mega-controller.ino compiles for arduino:avr:mega.
- pyserial 3.5 installed into Python 3.12.
- Vault lives under OneDrive Desktop; git repo root is accidentally the user home dir with ZERO tracked files - deletions are NOT recoverable via git. OneDrive recycle bin is the only net.
- PC timezone is already Taipei/GMT+8; get time via PowerShell Get-Date.

Orange Pi 5 (runtime):
- No WiFi/BT module; Ethernet tether to laptop, VS Code Remote-SSH.
- No display attached ever: SHOW_GUI=False, watch via MJPEG stream port 8000 forwarded through VS Code Ports tab.
- mediapipe 1.0.1 ARM64 (mediapipe.solutions does not exist there; import from mediapipe.tasks.python).
- Camera goes into a USB 3.0 port. USB 2.0 brownout-loop risk is REAL - Justin confirmed on 2026-08-26 he lived it (Incident 4), it is no longer flagged as simulation.
- Watch for YUYV fallback warning at startup (halves framerate).

## 8. Known risks and blind spots (honest list)

- **Mega pin 2 dead (2026-08-29)** — left stepper uses STEP=5, DIR=6. Right stepper uses STEP=3, DIR=4. Do not use pin 2.
- **Power-tool battery gate (2026-09-27)** — do not connect the adapter until voltage, polarity, fuse placement, and 12 V load compatibility are checked. If the pack is 18 V/20 V, N20 motors and fan may need a buck converter.
- **VMOT/VDD wiring swap fixed (2026-08-28)** — both A4988s had 12V on VDD and 5V on VMOT. First driver killed by VMOT-GND spark during probe test. Second killed by 12V on VDD (exceeds 5.5V max). Both discarded. Verify VMOT=12V, VDD=5V before powering any driver.
- Current hardware caveat (2026-09-27): camera and lidar are mounted, both NEMAs are mounted, and one NEMA is wired. Full robot wiring and live sensor validation are still incomplete. All four troubleshooting-log incidents are real: 1-3 (weak suction first build, flexing hot-glue motor mounts, missing WiFi solved by Ethernet tether) plus Incident 4's USB brownout loop, which Justin confirmed real on 2026-08-26.
- 10.1's anomaly layer was validated against SYNTHETIC debris modeled on Justin's descriptions, not his actual floor. First live run WILL need ANOMALY_SENSITIVITY tuning. Expected, not a bug.
- Dark objects on dark floors are invisible to layer 2 (it ignores brightness to stay shadow-proof). Lidar fusion is the planned fix.
- mega-controller.ino is a reconstruction; the original firmware exists but was never compared. Bench-test via validator before powering drive motors. WATCHDOG_MS ships 0 (disabled) for bench safety.
- The detector has never run on the Pi itself yet; all numbers are desktop-relative.
- OneDrive sync + Obsidian: avoid editing the same file from two machines simultaneously.
- `git` here tracks nothing; do not rely on it for rollback.

## 9. History in one paragraph

Legacy CV filters (v1-v6 era) died in MediaPipe import hell until v8 (2026-08-24) fixed imports, threaded the pipeline, and streamed MJPEG. v9 (2026-08-25) ran the pipeline under a controlled benchmark, disproved the 720p-upscale assumption with data, fixed ghost boxes, added track smoothing, freshness-gated encoding, and camera self-healing. v10 (same night) answered Justin's real requirement - catch ANYTHING that could clog the vacuum - with a training-free floor-anomaly layer. 10.1 added the finished Pi-side serial sender behind a flag. Wave 3 (same night): purge of deprecated files, decimal versioning + filename renames per Justin, Node + skills tooling installed, all docs rewritten in Justin's voice, and this handoff created. Later the same day: 10.2 shipped the HTML mission dashboard (/ + /stream + /stats + /threat), 10.3 replaced hue/saturation block features with brightness-normalized chromaticity to kill moving-shadow false alarms, and 10.4 added Justin's proximity gate plus a file-backed dashboard served fresh from disk on every request.

## 10. Where things go next

Read `3-Logs/argus-vac-next-steps.md`. Short version: finish second NEMA wiring, apply the known Vref, wait only for the newest battery system, flash + bench Mega with validator, live-test the mounted camera, test the mounted lidar, enable serial, then ROS 2 SLAM.
