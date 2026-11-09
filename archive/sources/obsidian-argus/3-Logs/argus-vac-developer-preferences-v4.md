# Argus Vac - Developer Preferences & Engineering Principles (v4.2)

This document logs the core architectural preferences, engineering philosophies, and development styles selected for the **Argus Vac** autonomous robot project. It focuses on high-level design choices and developer styles that guide engineering decisions.

---

## 🔌 1. Hardware & Electrical Preferences

### ⚡ Dual Isolated Power Scheme
*   **The Preference:** Keep the high-level processing unit (Orange Pi 5) completely isolated from the primary motor/actuator power rails [24].
*   **Why:** Stepper and brush motors draw massive transient currents under load, which can cause voltage sags (brownouts) on the Orange Pi 5, leading to system crashes or SD card corruption.
*   **Implementation:** A 3S LiPo battery (11.1V, 5000mAh) protected by a 10A blade fuse drives heavy actuators via an LM2596 buck converter [24], while a dedicated 5000mAh USB power bank drives the Orange Pi 5.

### 🔌 Wago 221 Lever Connectors over Soldering
*   **The Preference:** Use **Wago 221 series lever nut connectors** (221-413 for 5V, 221-415 for 12V/11.1V) rather than permanent soldering or friction-fit breadboards [24].
*   **Why:** Lever connectors provide highly reliable, vibration-resistant, and easily reconfigurable power distribution blocks, which are essential during rapid prototyping and hardware iteration.

### 💻 USB-Serial Bridge over Direct GPIO
*   **The Preference:** Connect the Orange Pi 5 brain to the Arduino Mega 2560 microcontroller using a standard USB-to-USB cable instead of direct TTL GPIO pins.
*   **Why:** Provides electrical isolation, prevents logic level mismatch (3.3V vs. 5V), is physically secure against physical vibration, and permits independent desk-bound software debugging.

### 🔌 USB 3.0 Port Allocation for High-Current Peripherals
*   **The Preference:** Plug the USB Camera into a USB 3.0 port instead of a USB 2.0 port on the Orange Pi 5 single-board computer [1].
*   **Why:** SBC USB ports often restrict power output. While low-current control interfaces enumerate fine over USB 2.0, initiating video streaming draws higher current, which can brown out the camera and cause repeated USB disconnect/reconnect cycles [1]. A USB 3.0 port provides sufficient current to maintain a stable, uninterrupted stream [1].

---

## 👁️ 2. Software & Computer Vision Preferences

### 🧠 Deep Learning (AI) over Manual HSV Calibration
*   **The Preference:** Rely on pre-trained, deep-learning-based neural networks (like **Google MediaPipe Object Detector**) rather than traditional HSV color-masking or manual edge-threshold tuning [1].
*   **Why:** Classic computer vision requires manual, brittle adjustments of slider thresholds that break instantly when the robot moves into different lighting environments or shadow zones.
*   **Model Choice:** **EfficientDet-Lite2** is the preferred model [1, 5], setting a **50% confidence threshold** [4] to strike the optimal balance between high precision on small/obscured floor obstacles and execution speed.

### 🧵 Multi-Threaded Decoupled CV Pipeline
*   **The Preference:** Split the computer vision pipeline into independent, concurrent threads (Capture, Inference, Render/Stream, Stats) guarded by locks [1, 5].
*   **Why:** Original serial loops (capture -> inference -> encode -> stream in one thread) capped the display frame rate at whatever speed inference ran, making the video feel extremely laggy [1]. Decoupling threads allows the render/stream thread to run at a steady target rate (e.g. 30 FPS) completely independent of the inference cycle, giving perceived visual smoothness [1, 6]. Detection boxes update as they complete and simply "hold" on screen [1].

### 🕸️ Headless GUI Bypass via MJPEG HTTP Stream
*   **The Preference:** Serve the annotated video feed as an MJPEG stream over HTTP (running a lightweight, built-in standard library `http.server` on port 8000) with GUI disabled (`SHOW_GUI = False`) [1, 4].
*   **Why:** Developing remotely over VS Code Remote-SSH means there is no local display attached to the Pi session [1]. Serving over HTTP lets you forward port 8000 in VS Code and view the live stream on your laptop browser at `http://localhost:8000/` [1].

### 📉 Native-Resolution Inference (REVISED in v4)
*   **The Preference:** Capture, stream, AND run detector inference at the same native resolution (**640x480**) [9]. *This supersedes the former v3 preference of upscaling frames to 1280x720 for inference.*
*   **Why:** A controlled benchmark (synthetic camera + real model + real-photo tests) disproved the upscale assumption: EfficientDet-Lite2 resizes input internally regardless, so upscaling added zero detection value while costing CPU every cycle and stretching the sensor's native 4:3 onto 16:9 (a distortion that measurably reduced confidence on test images). Native-resolution inference measured identical detections (box IoU 0.97-0.99), roughly 31% higher detection throughput, ~24% lower average latency, and a 9x cheaper preprocessing step [9].
*   **Caveat kept from v3:** Capturing/streaming at 640x480 remains correct for USB bandwidth, decode cost, and network lag reasons [1].

### 🚀 Video Processing Mode over Static Images
*   **The Preference:** Run the MediaPipe Tasks Object Detector in `RunningMode.VIDEO` instead of `RunningMode.IMAGE` [1].
*   **Why:** `RunningMode.VIDEO` is built specifically for continuous frame streams and tracks state across frames, avoiding the CPU overhead of re-initializing internal detector states on every single image call [1].

---

## 📝 3. Documentation & Engineering Log Style

### 🗃️ Separation of Theory and History
*   **The Preference:** Maintain a strict separation between *potential/preventative troubleshooting* (calibration calculations, electrical safety limits) and *historical physical failure logs*.
*   **Why:** Avoids cluttering active design manuals with past mishaps, keeping diagnostic formulas clean while providing an honest, unvarnished history of physical incidents for retro-analysis.

### 📝 Incremental Versioning Control (REVISED 4.1)
*   **The Preference (updated by Justin, 2026-08-25):** Small fixes and updates edit the SAME file and bump a decimal version: v10 -> 10.1 -> 10.2. Only a major rewrite or architecture change creates a new file with the next whole version (10.x -> 11). Every bump gets logged in the change log under that file's history section.
*   **Why:** The old rule (new file per fix) buried the vault in near-duplicate detector files and stale registries. Decimal bumps keep one authoritative file per component while preserving full history in the change log.

### 🧪 Benchmark Before Optimizing (ADDED in v4)
*   **The Preference:** Before adopting any performance- or accuracy-motivated technique in the perception pipeline, validate it by executing the pipeline against a controlled harness (deterministic synthetic camera source plus fixed real-image tests) and comparing measured numbers - not intuition [9].
*   **Why:** The 1280x720 upscale preference survived multiple development sessions because it *sounded* correct. Running the pipeline exposed it as pure waste within minutes. Harnesses for the detector live in the vault under `outputs/detector-refine/` (`bench_synth.py`, `bench_accuracy.py`, `test_v9.py`) and can be rerun after future changes.

### 🗂️ Unified Workspace File & Report Review Mandate (The "Housekeeping Rule")
*   **The Preference:** ALWAYS inspect and review every single file in the Studio panel, including both standalone markdown/code documents and Content Studio compiled reports, before finalizing any technical modifications.
*   **Why:** Code and configuration updates (like changing camera capture modes, frame rates, or port mappings) naturally ripple through physical manuals, calibration guides, and project plans. Inspecting and updating all files (including reports) guarantees that the entire engineering repository remains 100% accurate, fully synchronized, and safe for the hardware developer to execute.
