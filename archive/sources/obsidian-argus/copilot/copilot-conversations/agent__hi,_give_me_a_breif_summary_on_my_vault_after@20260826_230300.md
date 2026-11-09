---
epoch: 1787756580139
mode: agent
backendId: opencode
sessionId: "ses_fc167c886ffebwgGpbUzH77p7v"
usage: '{"usedTokens":17949,"contextWindow":1000000,"updatedAt":1787756809158}'
tags:
  - copilot-conversation
---

**user**: hi, give me a breif summary on my vault after reading through the files.
[Timestamp: 2026/08/26 23:03:00]

**ai**: ## Vault Summary: Argus Vac Brain

**What this is:** Your knowledge base for building an autonomous vacuum robot (Argus Vac) — Orange Pi 5 brain, Arduino Mega 2560 muscle layer, camera + RPLidar sensors.

### Structure at a glance

| Folder | Contents |
|--------|----------|
| `1-Manuals/` | 4 manuals in your voice: Hardware/Mechanical, Electrical Wiring (authoritative pin map), Calibration/Troubleshooting, Progress & Action Plan |
| `2-Reference/` | `ROBOT_MASTER.md` — your raw source notes (do not restyle) |
| `3-Logs/` | Change log v25, next steps roadmap, developer preferences, housekeeping record, VS Code SSH guide, historical troubleshooting log (4 real incidents) |
| `4-Software/` | Active detector `obstacle-detector-mediapipe-v10.6.py` (two-layer: MediaPipe + training-free anomaly), `mega-controller.ino` (unflashed draft), validator scripts, dashboard HTML/JS/CSS |
| `5-Hardware/` | Single source of truth: `Argus Vac Final.fzz` (Fritzing) |
| `outputs/detector-refine/` | Benchmark harness (29 tests) |
| `tools/` | `vaultsync.py`, `parse-fritzing-v1.1.py` |
| `copilot/`, `.opencode/` | Agent skills (web search, fetch, YouTube, X, PDF, Obsidian markdown, bases, canvas, symposium) |

### Current state (from HANDOFF.md)

- **Chassis:** Built (acrylic plates, spacers, castor wheel)
- **Detector:** v10.6 — proximity gate on both layers, static-structure suppression (doors/walls go quiet after 60s), file-backed dashboard, serial sender ready but OFF by default
- **Arduino firmware:** Draft in vault, never flashed or bench-tested
- **Serial link:** Protocol defined, validator ready, not commissioned
- **RPLidar C1:** On hand, unmounted, no software
- **Missing parts:** N20 motors + 0.1µF caps (shipping), wire to buy (22/18/12 AWG sizes researched)
- **Power:** 12 AWG inline 10A fuse finalized; no 14 AWG in this build

### Key facts to remember
- Pin map: Left stepper STEP 5/DIR 6, Right STEP 3/DIR 4, L298N inputs 7–10, fan PWM 11/DIR 12/BRAKE 2
- Serial contract: `P` ping, `S` steppers, `B` brushes, `V` vacuum, `H` halt, `G` release, `R` threat (auto-halt at ≥85% risk)
- Battery: 11.1V 3S LiPo 5000mAh (drive) + separate 5000mAh power bank (logic) — never merge
- Camera must use USB 3.0 port (USB 2.0 brownout loop is a real, confirmed risk)

### Next steps (short version)
1. Live-test detector v10.6 on Pi
2. Wait for N20 motors + caps
3. Flash + bench Mega via validator
4. Enable serial link
5. Mount lidar
6. ROS 2 SLAM

The vault is lean — durable facts live in the change log and HANDOFF, not scattered notes.
[Timestamp: 2026/08/26 23:03:00]