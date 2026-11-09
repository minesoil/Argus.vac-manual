# Argus Vac - VS Code Remote SSH Setup Guide (v3)

This guide outlines the step-by-step engineering workflow to connect your laptop's **Visual Studio Code (VS Code)** environment directly to your **Orange Pi 5** over a local network (such as your wired Ethernet tether). This allows you to write code, manage files, and run OpenCV or ROS 2 scripts directly on the robot from the comfort of your laptop.

> 🆕 **v3 changes:** Script references updated from `obstacle-detector-v1.py` to the current active detector, `obstacle-detector-mediapipe-v10.6.py`. The Headless Display section now leads with the MJPEG HTTP stream (the modern default since v8) instead of X11 forwarding.

---

## 📋 Prerequisites
1.  **Laptop:** VS Code installed.
2.  **Orange Pi 5:** Powered up (via your 5000mAh power bank) and connected to your laptop via an Ethernet cable or local network.
3.  **SSH Server:** SSH must be enabled on your Orange Pi (installed by default on Armbian/Ubuntu images; can be verified or installed using `sudo apt install openssh-server`).
4.  **IP Address:** The local IP address of your Orange Pi 5.

---

## 🛠️ Step 1: Install the Remote - SSH Extension in VS Code
1.  Open VS Code on your laptop.
2.  Click on the **Extensions** icon on the left Activity Bar (or press `Ctrl+Shift+X` on Windows/Linux, `Cmd+Shift+X` on macOS).
3.  Search for **\"Remote - SSH\"** (developed by Microsoft).
4.  Click **Install**.

---

## 🔌 Step 2: Configure the SSH Connection

When configuring your direct Ethernet tether, there are two ways to set up the connection.

### Method A: The Command Palette Way (Correct Syntax)
1.  In VS Code, press `F1` or `Ctrl+Shift+P` (`Cmd+Shift+P` on macOS) to open the Command Palette.
2.  Type **\"Remote-SSH: Add New SSH Host...\"** and press Enter.
3.  Enter the SSH connection command. **You must type the word "ssh" at the beginning, followed by the user and IP:**
    ```bash
    ssh orangepi@169.254.X.Y
    ```
    *Replace `169.254.X.Y` with your actual Orange Pi IP address. Do not type a bare IP address or use bare spaces, as this triggers VS Code's `argv must be string array` crash.*
4.  Select the default SSH configuration file to save this host (usually `~/.ssh/config`).
5.  Click **Connect** on the popup.

### Method B: Directly Editing the SSH Config File (Highly Recommended & Foolproof)
If the Command Palette input box crashes or acts buggy, you can bypass it entirely by writing directly to your SSH config file:
1.  Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`).
2.  Type and select **\"Remote-SSH: Open SSH Configuration File...\"**.
3.  Choose the top configuration file in the list (usually `~/.ssh/config`).
4.  Paste this exact clean text block at the bottom:
    ```text
    Host orangepi
        HostName 169.254.X.Y  # Put your exact Orange Pi IP address here!
        User orangepi         # Change to 'root' if logging in as root
        Port 22
    ```
5.  Save the file (`Ctrl+S` or `Cmd+S`).

---

## 🔌 Step 3: Establish the Connection & Authenticate
1.  Click the green **\"Open a Remote Window\"** indicator in the bottom-left corner of the VS Code window (looks like `><`).
2.  Select **\"Connect to Host...\"** and choose **`orangepi`** from the list.
3.  A new VS Code window will open. Select the platform type: **Linux**.
4.  If prompted to verify the fingerprint, select **Continue**.
5.  Enter your Orange Pi's user account **password** when prompted at the top of the screen.
6.  Once connected, the green indicator in the bottom-left will display: **`SSH: orangepi`**. You are now operating directly inside the Orange Pi 5 filesystem!

---

## 📂 Step 4: Open Your Project Workspace
1.  In VS Code, go to **File > Open Folder...**.
2.  Navigate to or create your robot workspace directory (e.g., `/home/orangepi/argus_vac/`) and click **OK**.
3.  Enter your password again if prompted. The remote directory tree will load in the VS Code Explorer pane.
4.  Copy your python scripts (like `obstacle-detector-mediapipe-v10.6.py`) directly into this workspace folder.

---

## 🐍 Step 5: Install Python & Remote Extensions
To get full syntax highlighting, auto-complete, and debugger support on your Orange Pi:
1.  While connected to the Orange Pi, go back to the **Extensions** tab in VS Code.
2.  Search for the **\"Python\"** extension (Microsoft).
3.  You will see a button labeled **\"Install on SSH: orangepi\"**. Click it to install the extension directly onto the Orange Pi's filesystem.
4.  Open `obstacle-detector-mediapipe-v10.6.py` to start coding!

---

## 🚨 Critical Troubleshooting: Direct Tethering Network Obstacles

Developing over a direct laptop-to-Pi Ethernet cable is highly convenient but prone to specific network blocks. Here is how we engineered past them today:

### 1. VS Code Crash: "argv must be string array"
*   **Symptom:** VS Code crashes immediately after entering the connection command in the Command Palette.
*   **Root Cause:** The Command Palette input parser expected a full command beginning with `ssh` (e.g., `ssh orangepi@169.254.103.42`), but received an incomplete command, a bare IP address, or misplaced spaces. This prevents VS Code from splitting the input into its internal argument array (`argv`).
*   **Engineered Solution:** Use the correct `ssh user@ip` syntax, or bypass the Command Palette entirely by writing a clean Host block directly to the `~/.ssh/config` file (as shown in Step 2, Method B).

### 2. Windows Loop: "Identifying... Unidentified Network"
*   **Symptom:** The Ethernet status in Windows is stuck in an "Identifying..." loop for minutes before falling back to "Unidentified Network" with **No Internet Access**.
*   **Root Cause:** Since there is no router (gateway) between the laptop and the Pi, Windows is looking for a network identifier and a DHCP server. 
*   **Engineered Solution:** This is actually **normal and expected**. Direct links do not need a gateway or Internet access to function. Let the devices fall back to their Link-Local IP autoconfigurations (`169.254.X.Y`).

### 3. The One-Way Block: "Packets Sent: 8,774, Packets Received: 0"
*   **Symptom:** The physical link LEDs are green and blinking yellow, but running `arp -a` in Command Prompt does not show the Orange Pi, and "Packets Received" is stuck at exactly 0.
*   **Root Cause:** Because the direct cable link is an "Unidentified Network", Windows automatically classifies it as a **Public Network** and activates aggressive firewall shielding. Windows Defender Firewall (or third-party antivirus suites like McAfee, Norton, or Avast) silently drops all incoming packets from the Pi, making the laptop completely "deaf".
*   **Engineered Solution:** 
    *   Temporarily disable Windows Defender Firewall for **Public Networks** under "Turn Windows Defender Firewall on or off" in the Control Panel.
    *   Temporarily pause any active third-party antivirus "Smart Firewalls" or network shields.
    *   Once connected, add an explicit inbound rule in Windows Firewall to permanently allow **Port 22 (SSH)** traffic, then re-enable your firewall.

### 4. IP Subnet Mismatch & Virtual Adapter Conflicts
*   **Symptom:** Assigning manual static IPs (like `192.168.137.1` or `10.42.0.1`) to the laptop's Ethernet card fails or causes IP address conflicts.
*   **Root Cause:** Standard subnets like `192.168.137.X` are often pre-reserved by Windows for background virtual switches (WSL2, Hyper-V, Docker, or VPN clients). Trying to assign them manually causes a conflict. Furthermore, if the laptop and Pi are on different subnets (e.g. laptop on static `10.42.0.x` and Pi on auto-IP `169.254.x.x`), they cannot see each other.
*   **Engineered Solution:** Revert the laptop's Ethernet adapter to "Obtain an IP address automatically" to force both devices to use the default Link-Local (`169.254.X.Y`) range.

### 5. The Ultimate Breakthrough: Selecting "Autoethernet" on the Orange Pi 5
*   **Symptom:** Both devices are plugged in, but the Orange Pi refuses to negotiate a link-local address, remaining offline.
*   **Root Cause:** The Orange Pi's network interface manager is waiting for an active DHCP server lease instead of automatically spinning up a local link.
*   **Engineered Solution:** Connect a temporary monitor/keyboard to the Pi, open its network configuration settings, and explicitly enable/select **`autoethernet`** (or configure the physical interface to standard dynamic link-local / direct-connect mode). This tells the Pi's NetworkManager to automatically establish a local Link-Local connection the moment it senses the laptop's physical link.

---

## 📺 Troubleshooting: Headless OpenCV Display Issues
The Orange Pi has no physical monitor attached, so any attempt to show a local GUI fails:
```text
cv2.error: OpenCV(4.x) ... Gtk-WARNING: cannot open display
```

### Method A (RECOMMENDED): View the MJPEG HTTP Stream
Since build v8 the detector ships with its own streaming server, and v9 extends it with live pipeline telemetry:
1.  Confirm `SHOW_GUI = False` and `STREAM_HTTP = True` at the top of `obstacle-detector-mediapipe-v10.6.py` (these are the defaults - no edit needed).
2.  Run the script: `python3 obstacle-detector-mediapipe-v10.6.py`.
3.  In VS Code, open the **Ports** tab, forward port **8000**, then open `http://localhost:8000/` in your laptop browser for the annotated live feed.
4.  Open `http://localhost:8000/stats` (or check the console) for one-line pipeline health: capture FPS, inference rate/latency, encode FPS, and end-to-end latency.

### Method B: Run Fully Headless (Console Only)
If you only want console output (AI alerts plus periodic `[stats]` lines):
1.  Set `STREAM_HTTP = False` near the top of `obstacle-detector-mediapipe-v10.6.py`.
2.  Keep `SHOW_GUI = False`.
3.  Run the script. It captures frames, runs detection, prints throttled AI alerts and stats to your VS Code terminal without launching any window.

### Method C: Enable X11 Forwarding (Legacy - rarely needed)
Only if you specifically need a native `cv2.imshow` desktop window on your laptop:
1.  **On your laptop, install an X Server:**
    *   **Windows:** Install [VcXsrv](https://sourceforge.net/projects/vcxsrv/) or [Xming](https://sourceforge.net/projects/xming/). Start it on your laptop (choose \"Disable access control\" during startup setup).
    *   **macOS:** Install [XQuartz](https://www.xquartz.org/). Start it and enable \"Allow connections from network clients\" in preferences, then restart your Mac.
    *   **Linux Laptop:** No install needed; X11 is native.
2.  **Configure SSH Config in VS Code:**
    *   Open the SSH configuration file (`~/.ssh/config`) and add these three lines to your Orange Pi Host block:
        ```text
        ForwardX11 yes
        ForwardX11Trusted yes
        ForwardAgent yes
        ```
3.  **On the Orange Pi Terminal (inside VS Code):**
    *   Set your temporary display environment variable to route X11 traffic back to your laptop:
        ```bash
        export DISPLAY=localhost:10.0
        ```
    *   Now run `python3 obstacle-detector-mediapipe-v10.6.py` with `SHOW_GUI = True`. The window will render on your laptop screen.
