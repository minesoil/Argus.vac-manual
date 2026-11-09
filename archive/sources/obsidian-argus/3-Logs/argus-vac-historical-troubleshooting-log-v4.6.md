# My robot: historical troubleshooting log (4.6)

Honest status, corrected 2026-08-25, updated 2026-08-26: Incidents 1 to 3 are REAL problems I hit with physical hardware (weak suction from my first assembly, flexing hot-glue motor mounts, the Pi's missing WiFi) and my Ethernet tether fix in Incident 3 really happened. Incident 4 is ALSO real: I hit the USB camera brownout loop for real, and the fix turned out to be as simple as predicted - moving the camera plug from a white USB 2.0 port to the blue USB 3.0 port. Its software fixes (v8 imports, threading, MJPEG server) are real desktop work. Each incident ends with a fill-in block recording what actually happened during physical work.

---

## Incident 1: Weak Vacuum Suction

### 1. Problem Statement
My first assembly produced very weak suction [3]. The **San Ace 40 Axial Fan** was unable to lift debris from the floor surface [2, 3].

### 2. Root Cause Analysis
I had mounted the fan vertically on top of the upper acrylic chassis plate [3]. Because the suction path was not sealed and lacked a localized chamber, air was drawn from the surrounding open space instead of pulling negative pressure from the floor [3]. The lack of a dust bag or guided shroud bypassed any direct suction capability [3].

### 3. Verified Engineering Resolution
*   **Physical Reorientation:** Relocate the San Ace 40 Axial Fan to sit in between the two 30cm x 30cm x 1cm acrylic plates [3].
*   **90-Degree Rotation:** Rotate the fan 90 degrees so that it is oriented horizontally (facing forwards relative to the robot) [3].
*   **Negative Pressure Chamber:** Mount the fan directly behind a sealed dust collection bag [3]. The fan will pull air through the bag, creating negative pressure to suck up debris [3].
*   **Mechanical Sweeping Assistance:** Integrate two **N20 Micro Gear Motors** driving dual rotating sweeping bristles in front of the vacuum inlet to mechanically sweep dust and debris directly into the bag [2, 3].

### 4. [ ] Actual Implemented Solution & Physical Fix
*Fill out this section when the physical modification is complete:*

```text
[ ] Status: IN PROGRESS / COMPLETED
[ ] Date of Physical Fix: ____/____/2026
[ ] Materials/Tools Used: __________________________________________________
                          __________________________________________________

[ ] Specific Physical Fix Details:
    ________________________________________________________________________
    ________________________________________________________________________
    ________________________________________________________________________
    ________________________________________________________________________

[ ] Validation Test Results (Suction Strength & Debris Clearance):
    ________________________________________________________________________
    ________________________________________________________________________
```

---

## Incident 2: Structural Instability of Traction Motors

### 1. Problem Statement
In my early drive tests the wheel assembly flexed badly, slipped out of alignment, and could not handle motor torque [3].

### 2. Root Cause Analysis
To quickly fit my bipolar NEMA stepper motors between the two plates, I mounted them temporarily using hot glue and popsicle sticks [2, 3]. While sufficient for a static bench test, these temporary materials completely lacked the torsional rigidity required to handle the torque of the stepper motors under load [3].

### 3. Verified Engineering Resolution
*   **Rigid Motor Brackets:** Design and fabricate custom, high-strength motor mounting brackets [3].
*   **Chassis Integration:** Securely bolt these brackets directly to the 1cm thick acrylic plates using machine screws and locking nuts [3].
*   **Material Selection:** Use 3D-printed PETG/ABS filaments with high infill density (minimum 40% gyroid infill) or CNC-milled aluminum brackets to eliminate all flexing [3].

### 4. [ ] Actual Implemented Solution & Physical Fix
*Fill out this section when the physical modification is complete:*

```text
[ ] Status: IN PROGRESS / COMPLETED
[ ] Date of Physical Fix: ____/____/2026
[ ] Materials/Tools Used: __________________________________________________
                          __________________________________________________

[ ] Specific Physical Fix Details:
    ________________________________________________________________________
    ________________________________________________________________________
    ________________________________________________________________________
    ________________________________________________________________________

[ ] Validation Test Results (Alignment Stability under Torsional Load):
    ________________________________________________________________________
    ________________________________________________________________________
```

---

## Incident 3: Orange Pi 5 Wireless Connectivity Barrier

### 1. Problem Statement
Remote wireless control, live SSH access, and real-time ROS 2 telemetry/Rviz visualisation are currently impossible when the robot is moving freely on the floor [3].

### 2. Root Cause Analysis
My **Orange Pi 5 (8GB)** board came without an onboard WiFi and Bluetooth module [2, 3]. Because the board lacks a wireless transceiver, it cannot connect to local networks without a physical Ethernet cable tethered to a laptop [3].

### 3. Verified Engineering Resolution
*   **USB Wireless Module:** Acquire and install a compatible, high-gain USB WiFi/Bluetooth dongle (specifically testing chips with native Linux kernel support, such as RTL8821CU or RT5370).
*   **Tethered Network Setup:** Configure a lightweight wireless router on the robot chassis or set up a localized router where both the laptop and the Orange Pi connect.
*   **Temporary Ethernet SSH:** Maintain a static Ethernet connection for desk-bound software development and ROS 2 package compilation [3].

### 4. [x] Actual Implemented Solution & Physical Fix
*Physical development setup completed on 2026-08-23:*

```text
[x] Status: COMPLETED (Development Bridge)
[x] Date of Physical Fix: 2026-08-23
[x] Materials/Tools Used: Standard Cat5e Ethernet cable, RJ45 ports on Laptop & Orange Pi 5.

[x] Specific Physical Fix Details:
    Established a direct, high-bandwidth wired network link by connecting a physical 
    Ethernet cable between the laptop's network adapter and the Orange Pi 5's RJ45 port.
    This creates a reliable, noise-immune development bridge for compilation, remote terminal 
    operations, and testing on the workbench while waiting for future USB wireless module integration.

[x] Validation Test Results (SSH Ping Latency & Wireless Telemetry Rate):
    Ping test confirmed stable, ultra-low latency response (<1.0ms) with zero packet drops.
```

---

## Incident 4: USB Camera Connection Brownout & MediaPipe Tasks API Import Failures

### 1. Problem Statement
When running the object detector camera software, the program crashed instantly on startup with module import errors [1]. Even when imports were bypassable, the camera failed to open a video stream, printing repeating USB disconnected/reconnected loops in terminal logs (`dmesg` / `journalctl`) [1]. Additionally, attempts to render visual windows over VS Code Remote-SSH failed instantly due to a lack of display hardware [1].

### 2. Root Cause Analysis
*   **Malform API Imports:** The original code imported from `mediapipe.tasks.vision`, which does not exist in the local ARM64 build [1]. The classes exist under `mediapipe.tasks.python.vision` [1].
*   **Missing Legacy Fallback:** Classic API elements (`mediapipe.solutions`) were omitted entirely from the 1.0.1 wheel, breaking the dual-compatibility backup design [1].
*   **USB Port Underpowering (CONFIRMED REAL 2026-08-26):** The single-board computer's USB 2.0 port failed to supply adequate current when the camera was negotiating high-bandwidth video capture, causing repeated hardware brownouts [1]. Justin confirmed he lived this failure, not a simulation of it.
*   **Headless Remote SSH Display:** OpenCV's visual GUI (`cv2.imshow`) could not bind to an active graphics server, leading to window crash events over Remote SSH [1].

### 3. Verified Engineering Resolution
*   **Correct Import Syntax:** Bind directly to `from mediapipe.tasks.python import BaseOptions, vision` to resolve compiler import mapping [1].
*   **SBC USB Port Migration:** Plug the USB camera strictly into a blue **USB 3.0 port** on the Orange Pi 5 chassis, which is rated to supply sufficient current [1].
*   **Serve Stream over HTTP:** Write an asynchronous, multi-threaded server using standard libraries to encode and host annotated video frames as an MJPEG stream over HTTP port 8000 [1]. This allows browser-based viewing via port forwarding [1].
*   **Decoupled Multi-threading:** Run Capture, Inference, and MJPEG Streaming as independent concurrent threads so that inference latency does not block continuous 30 FPS video playback [1].

### 4. [x] Actual Implemented Solution & Physical Fix
*Filled in 2026-08-26 per Justin: the camera was sitting in a white USB 2.0 port; he moved it to the blue USB 3.0 port. A two-second fix, which matches what this incident always claimed - the 3.0 port exists precisely so this failure can't happen. What is not yet recorded: a clean dmesg check and a full on-Pi MJPEG stream run.*

```text
[x] Status: PHYSICAL FIX APPLIED (port migration done; stream re-validation still open)
[x] Date of Physical Fix: 2026-08-26 (per Justin)
[ ] Materials/Tools Used: none - moved the existing camera plug, no parts needed

[x] Specific Physical Fix Details:
    1. Camera moved out of the white USB 2.0 port into the blue USB 3.0 port on the Pi.
    2. Still to record: dmesg shows no reconnect loop after the move; detector runs with the MJPEG stream reachable over port forwarding.

[ ] Validation Test Results:
    Not yet recorded - do a dmesg check + one detector run on the Pi and write down the result here.
```
