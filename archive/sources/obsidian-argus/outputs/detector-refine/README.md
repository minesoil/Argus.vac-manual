# Detector test harness (outputs/detector-refine)

Everything here is overnight work from 2026-08-25. Safe to delete, but cheap to keep:
rerun after any detector change to prove nothing broke.

| File | What it does |
| --- | --- |
| `efficientdet_lite2.tflite` | The model, downloaded once. |
| `bench_synth.py` | Runs the threaded pipeline against a fake 30fps camera; measures capture/inference/render rates and latencies. Variants: v8 style vs v9 style. |
| `bench_accuracy.py` | Real photos through both preprocessing paths; proved native-resolution inference loses no accuracy vs the old 720p upscale. |
| `fetch_images.py` | Downloaded the four test photos (Wikimedia). Python SSL fails on this PC; curl was used instead. |
| person/dog/chair/cat jpg files | Test images for bench_accuracy. |
| `test_v9.py` | 21 checks: v9 pipeline logic + integrated run. Still valid for the archived v9. |
| `test_v10.py` | 29 checks: anomaly layer math, two-phase clean-floor/debris run, serial decision logic for 10.1+. Run this one after any change to obstacle-detector-mediapipe-v10.6.py. |
| `sync_registry.py` | One-off script that updated the changelog registry rows during wave 2. Kept as an example of bulk registry edits. |

To run tests: `python test_v10.py` from THIS folder (the model file is here).

Known quirk: this PC's Python has a broken SSL cert store, so any new downloads
should use curl.exe instead of urllib.


| File | What it does |
| --- | --- |
| `virtual_mega.py` | Software twin of mega-controller.ino's serial behavior; lets tests prove the Pi-Mega contract with no hardware attached. |
| `test_protocol.py` | Full dress rehearsal: real detector threads + serial wire + VirtualMega. Proves obstacle -> AUTO-HALT on the wire (0.05 s) and that the Pi never sends G. |
| `test_dashboard.py` | Route checks for the v10.2+ mission dashboard (/ , /stream, /stats, /threat, 404). |
| `test_lidar.py` | Cone math incl. 0/360 wrap, risk mapping, and a live mock run: obstacle enters cone -> R LIDAR packet -> Mega AUTO-HALT (0.20 s). |
| `test_robustness.py` | Six-scene stress matrix for the anomaly layer (baseline, exposure ramp, moving shadow, striped carpet, small sock, thin cable). This is what drove the v10.3 chromaticity redesign. |
| `outputs/firmware-check/` note | arduino-cli itself lives at %LOCALAPPDATA%\argus-tools\arduino-cli\; outputs/firmware-check holds a compilable sketch-folder copy of mega-controller.ino. |
