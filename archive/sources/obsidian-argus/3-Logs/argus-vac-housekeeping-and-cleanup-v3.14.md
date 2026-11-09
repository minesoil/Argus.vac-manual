# Argus Vac - Workspace Housekeeping & Cleanup Guide (v3.14)

This registry catalogs the current state of files in the **Argus Vac** workspace. Because the Gemini Notebook workspace can accumulate multiple file versions during iterative development, use this guide as a directory for **which files to keep** and **which files to safely delete** through the user interface.

> ⚠️ **IMPORTANT DELETION POLICY REMINDER:**
> Gemini Notebook operates with high-security access controls and **does not have programmatic permissions to delete files from your project**. Deletions must be performed manually by the developer using the **Gemini Notebook Sources/Studio UI panels**.

---

## 🟢 ACTIVE FILES (KEEP)
Keep these files in your active directory. They represent the compiled, optimized, and active codebase and documentation of the robot.

### 💻 Active Software Files
> 📁 Obsidian vault location: `4-Software/`. (`mega-diagnostic.ino` remains in the Gemini Notebook workspace.)

| Filename | Version | Core Purpose / Active Status |
| :--- | :---: | :--- |
| `obstacle-detector-mediapipe-v10.6.py` | **10.6** | **Active Object Detector.** Two-layer obstacle-risk detection (known classes + training-free chromaticity floor layer), proximity gate on both layers (10.5 fix); static structure like doors/walls goes quiet after 60s parked (10.6), web mission dashboard served live from `dashboard/`, serial sender off by default. Multi-threaded, HTTP port 8000, `/stats` + `/threat`, camera self-healing. |
| `lidar-watch.py` | **1.0** | **Active lidar safety node.** RPLidar C1 is now mounted; live hardware test, wiring check, driver install if needed, and angle calibration still open. |
| `mega-controller.ino` | **1.0** | **Active Arduino firmware draft.** In-vault reconstruction speaking the validator's P/S/B/V/H/G contract plus R threat packets with auto-halt at risk >=85%. Boots HALTED. Bench-test against pi-hardware-validator.py before trusting; original mega-diagnostic.ino still only in Gemini workspace. |
| `pi-hardware-validator.py` | **v1** | **Active Actuator validator.** Interactive python script to execute serial command handshakes to the Arduino. |
| `mega-diagnostic.ino` | **v1** | **Active Arduino Mega Firmware.** Handles pin-mappings, steppers, sweeper L298N drivers, and vacuum fan control over serial. |
| `cv-environment-diagnostic.py` | **1.1** | **Active CV Profiler.** Analyzes floor color histograms and lighting averages to generate diagnostic reports; pre-flight tuning aid for the anomaly layer. |

### 📂 Active Documentation & Logging Files
> 📁 Obsidian vault location: `3-Logs/`.

| Filename | Version | Core Purpose / Active Status |
| :--- | :---: | :--- |
| `argus-vac-version-control-and-change-log-v25.md` | **v25.19** | **Active Change Log.** Master registry and single source of truth for all file versions. Current through v25.19; see its own history section for every wave since v24. |
| `argus-vac-next-steps.md` | **1.12** | **Active Roadmap.** Camera and RPLidar C1 are mounted; remaining sensor work is live testing and angle calibration. |
| `argus-vac-developer-preferences-v4.md` | **v4.2** | **Active Preferences.** Tracks high-level architectural philosophies and styles. Includes the decimal-versioning rule (small fixes bump decimals on one file; whole-version new files only for major rewrites) and native-resolution inference. |
| `argus-vac-historical-troubleshooting-log-v4.6.md` | **4.6** | **Active Troubleshooting Log.** ALL FOUR incidents are real. Incident 4: Justin hit the USB brownout loop in a white USB 2.0 port and fixed it by moving the camera to the blue USB 3.0 port (2026-08-26); dmesg + stream validation still to be recorded. |
| `argus-vac-vscode-setup-v3.md` | **v3** | **Active VS Code SSH Guide.** Steps to configure Remote-SSH development on the Orange Pi 5. Script references point at detector 10.6; leads headless viewing with the MJPEG stream + /stats telemetry. |
| `argus-vac-housekeeping-and-cleanup-v3.14.md` | **v3.14** | **Active Housekeeping Register.** This document. |

---

## 🗂️ Studio Reports Alignment Policy
Per the **Unified Workspace File & Report Review Mandate** added in Developer Preferences (v3), every software or system configuration update requires checking and regenerating the Content Studio reports located in the Studio panel:
1.  **"Argus Vac - Project Progress & Action Plan" (Report):** Must be updated when major coding milestones are reached (e.g., transition from CV troubleshooting to active, multi-threaded 30 FPS HTTP streaming). *Updated for detector v9 (2026-08-25): Section 3 rewritten - the "free" 1280x720 upscale claim was removed (disproven by benchmark) and replaced with native-resolution inference, track smoothing, freshness-gated encoding, and /stats telemetry. Report bumped to v3 in the registry.*
2.  **"Argus Vac - Calibration & Preventive Troubleshooting Guide" (Report):** Must be updated to include new theoretical fail-safes (e.g., current limits and brownout prevention for camera USB ports). *Updated for detector v9 (2026-08-25): brownout reasoning decoupled from the removed upscale step, added Preventive Format Verification section (YUYV fallback detection + camera self-healing), serial-link note advanced to build v9. Guide bumped to v3 in the registry.*
3.  **"Argus Vac - Hardware & Mechanical Architecture Manual" (Report):** Must reflect any structural revisions.
4.  **"Argus Vac - Electrical Wiring & Power Reference" (Report):** Must reflect the latest pinouts, wiring paths, and power distribution schemas.

---

## 🔴 DEPRECATED FILES - PURGE RECORD

Justin ordered the deprecated list purged on 2026-08-25. What actually happened:

**Already absent from disk** (removed in earlier cleanups): obstacle-detector-v5.py, obstacle-detector-mediapipe.py (v1), obstacle-detector-mediapipe-v2 through v6, developer-preferences-v1/v2, historical-troubleshooting-log-v3, housekeeping-and-cleanup-v1, change-log-v18 through v22.

**Deleted tonight:** developer-preferences-v3.md, housekeeping-and-cleanup-v2.md, vscode-setup-v2.md, change-log-v23.md.

**Moved to _Archive/ instead of deleted** (vault policy: keep until detector v10 passes a first live run on the Orange Pi):
- obstacle-detector-mediapipe-v8.py (first working Tasks-API version)
- obstacle-detector-mediapipe-v9.py (last known-good fallback)

Delete those two from _Archive/ after the first successful on-Pi run of v10.

---

## 🟣 PURGE WAVE 2 (2026-08-26, ordered by Justin: delete overlapping info and old things, keep what future development needs)

Deleted:
- `2-Reference/Argus Vac Fritzing Netlist.md` (75.9 KB): pasted netlist exports Justin had already judged inaccurate; one copy had survived his earlier deletion. Superseded by `tools/parse-fritzing-v1.1.py`, which reads wiring straight from the .fzz.
- `New Note For All Obsidian AI Agents.md` (root): porting note; its one live instruction (the .fzz is the wiring source of truth) moved into HANDOFF.md's file map.
- `Chats/` (single 2026-08-24 chat export) and all of `copilot/copilot-conversations/` (8 session transcripts): transcripts duplicate what the change log records.
- Empty junk: root `5-Hardware.md` (0 bytes), empty `Voice Scribe/` folder, `_Archive/create a link.md` (0 bytes), `_Archive/Untitled.base` (39-byte empty base).
- Build/run artifacts: `4-Software/__pycache__/`, `outputs/firmware-check/` (arduino-cli build output, regenerated on next compile), detector-refine run logs (`test_protocol.run`, `test_v10.run`, `last_run.txt`, `r1.txt`).
- One-shot vault-edit scripts from finished waves: `outputs/detector-refine/sync_fuse_upgrade.py`, `sync_registry.py`, `sync_registry_wave3.py`, `sync_wave4.py`, `sync_wave4b.py`, `fix_readme_table.py`.
- Inside `5-Hardware/Argus Vac Final.fzz`: stray `test_code_nema.ino` removed from the zip (Justin confirmed he had dragged it in by accident). Sketch re-verified intact afterwards.

Kept on purpose (future development needs them):
- `_Archive/obstacle-detector-mediapipe-v8.py` + v9.py until 10.6 passes its first live Pi run (rollback net).
- `outputs/detector-refine/`: benchmark scripts, `efficientdet_lite2.tflite`, test jpgs (benchmark inputs), README.
- All active software in 4-Software/, dashboard/, all manuals/logs, tools/ including fzp_cache/.

This file renamed from argus-vac-housekeeping-and-cleanup-v3.md to v3.5 per the filename-carries-version rule.

Renamed again per the same rule: v3.9 -> v3.10 on 2026-08-26, after a drift-sync of the rows above (change log was showing v25.3, next-steps was showing 1.5, vscode guide said detector 10.4; all brought current).

Renamed again per the same rule: v3.10 -> v3.11 on 2026-09-27, after the weekend-only Gantt chart and battery-plan sync brought the change log to v25.16 and next-steps to 1.9.

Renamed again per the same rule: v3.12 -> v3.13 on 2026-09-27, after the Gantt chart was expanded through December 2026.

Renamed again per the same rule: v3.13 -> v3.14 on 2026-09-27, after Justin said the camera and RPLidar C1 are mounted.
