# Put the Pi setup back in a sensible order

This is a **reconstructed rebuild recipe** based on the current source,
recorded commands and installed layout. The historical commands are preserved
separately in [the ledger](commands/RECORDED_PI_COMMANDS.md). This recipe has
not been used to commission a blank spare Pi. Do not run it over a working
robot without first inspecting and backing up its actual configuration.

No robot is available during preparation of this guide. The steps here are
for later, with motor battery power OFF. Keep it OFF through installation,
firmware work, calibration and state checks.

## 1. Establish the starting point

The known base is Orange Pi 5, Ubuntu 22.04 Jammy ARM64, regular user
`orangepi`, and ROS 2 Humble already installed. The initial OS flashing,
account creation, SSH setup and full ROS installation were not recovered.
An arbitrary current Orange Pi image may use different device names or boot
overlay syntax. Do not replace the working OS just to follow this document.

Run **on the Pi**:

```bash
cat /etc/os-release
uname -r
id orangepi
ls -l /opt/ros/humble/setup.bash
command -v ustreamer
/usr/bin/python3 -c "import cv2, numpy, serial; print(cv2.__version__, numpy.__version__, serial.__version__)"
```

The last command checks OpenCV, NumPy and pyserial in the **system Python**
used by the services. A VS Code Python extension or a different virtual
environment does not install modules into that interpreter.

If these application packages are missing on the known Jammy image, a new
dependency-install recipe is:

```bash
sudo apt-get update
sudo apt-get install --no-install-recommends python3-opencv python3-numpy python3-serial ustreamer unzip
```

This is not claimed as the original install command. Ubuntu lists
[uStreamer 4.9-1 for Jammy](https://packages.ubuntu.com/en/jammy/ustreamer),
matching the recorded executable version; a repository update can still
change a rebuilt environment. Capture actual versions after installing.
ROS is optional for the present camera/manual path.

## 2. Transfer the reviewed source

Unzip this handbook on the laptop. Open PowerShell **in that handbook folder**.
Replace the IP if the Pi's address changed:

```powershell
scp -r code/robot_control/argus_avoidance root@192.168.137.195:/home/orangepi/argus/avoidance-incoming-20261110
```

The destination must be new. If it already exists, stop and inspect it so
`scp` does not create an extra nested directory. On a fresh image create
`/home/orangepi/argus` first. On the Pi, with motor power OFF:

```bash
sudo systemctl stop argus-bridge.service argus-obstacle-preview.service
cd /home/orangepi/argus
ls -la avoidance-incoming-20261110
```

On a fresh installation the two service names may not exist yet; that is
different from a failure to stop an existing service. If an existing
`avoidance` folder is present, preserve it under a dated backup name first:

```bash
sudo cp -a /home/orangepi/argus/avoidance /home/orangepi/argus/avoidance-before-handbook-20261110
```

Use that line only when the source exists and the backup destination is new.
Then create/update the destination without deleting its private `.state/`:

```bash
sudo mkdir -p /home/orangepi/argus/avoidance
sudo cp -a /home/orangepi/argus/avoidance-incoming-20261110/. /home/orangepi/argus/avoidance/
sudo chown -R orangepi:orangepi /home/orangepi/argus/avoidance
sudo chmod 755 /home/orangepi/argus/avoidance/argus
cd /home/orangepi/argus/avoidance
sudo -u orangepi /usr/bin/python3 -m unittest discover -s tests -v
```

This copy does not remove old files. Review any obsolete module rather than
deleting it blindly. A retained calibration may already be expired; it is not
trusted merely because the file exists. Tests do not open the motor port.

## 3. Inspect the UART before changing boot settings

```bash
cat /boot/orangepiEnv.txt
ls -l /dev/ttyS0
id orangepi
```

The recorded image used `overlays=uart0-m2`. If that is already active and
`/dev/ttyS0` works, leave it alone. If enabling it on the same image is
necessary, first back up the boot file, then edit it deliberately:

```bash
sudo cp -n /boot/orangepiEnv.txt /boot/orangepiEnv.txt.before-argus-uart
sudo nano /boot/orangepiEnv.txt
```

Add `uart0-m2` to the image's existing overlay configuration; preserve any
other entries. A different image needs its own board documentation. Reboot
only with motor power OFF and after saving work. After reboot verify the
device and that `orangepi` has serial access through `dialout`; if necessary:

```bash
sudo usermod -aG dialout,video orangepi
```

New groups take effect in a new login or restarted service. Wiring is in
[01_HOW_IT_WORKS.md](01_HOW_IT_WORKS.md). Do not use a generic USB adapter
identity as proof of which board is attached.

## 4. Restore background services

Inspect existing units before replacing anything:

```bash
systemctl cat argus-camera.service
systemctl cat argus-bridge.service
systemctl cat argus-obstacle-preview.service
```

Keep the working camera base unit when it exists. Its exact original unit
was not recovered, so [argus-camera.RECONSTRUCTED.service](commands/templates/argus-camera.RECONSTRUCTED.service)
is a new minimal replacement around the observed uStreamer command. Likewise
[argus-bridge.RECONSTRUCTED.service](commands/templates/argus-bridge.RECONSTRUCTED.service)
is a complete new base unit for a fresh system, not the historical file that
ran `camera_sender.py`. The current module replaces that old script.

For a fresh system only, transfer the templates first; the source-only `scp`
in step2 does not include them. From the laptop handbook folder:

```powershell
scp -r commands root@192.168.137.195:/home/orangepi/argus/handbook-commands-20261110
```

That creates `/home/orangepi/argus/handbook-commands-20261110/templates/` if
the destination was new. Review the device/path/user settings, then on the Pi:

```bash
sudo install -m 644 /home/orangepi/argus/handbook-commands-20261110/templates/argus-camera.RECONSTRUCTED.service /etc/systemd/system/argus-camera.service
sudo install -m 644 /home/orangepi/argus/handbook-commands-20261110/templates/argus-bridge.RECONSTRUCTED.service /etc/systemd/system/argus-bridge.service
```

Do not replace a working camera unit solely because this guide supplies one.

For the current installed base bridge, its reviewed drop-in is the normal
update. Run from the installed Pi package:

```bash
cd /home/orangepi/argus/avoidance
sudo install -m 644 systemd/argus-obstacle-preview.service /etc/systemd/system/argus-obstacle-preview.service
sudo mkdir -p /etc/systemd/system/argus-bridge.service.d
sudo install -m 644 systemd/argus-bridge-avoidance.conf /etc/systemd/system/argus-bridge.service.d/avoidance-usb.conf
sudo systemctl daemon-reload
```

The filename `avoidance-usb.conf` is historical; its command uses GPIO UART.
Use [the firmware guide](04_FIRMWARE.md) before starting this bridge against
older ESP32 firmware. Preview can run without sending motor commands:

```bash
sudo systemctl enable --now argus-camera.service argus-obstacle-preview.service
```

After matching ESP32 firmware is installed, motor power remains OFF:

```bash
sudo systemctl enable --now argus-bridge.service
systemctl is-active argus-camera.service argus-obstacle-preview.service argus-bridge.service
curl --max-time 5 -sS http://127.0.0.1:8766/state
journalctl -u argus-bridge.service -n 40 --no-pager
```

Confirm STOPPED and zero outputs. If services are restarting, read their
logs; do not try to fix that by starting multiple manual serial processes.
Exactly one bridge owns the Pi-to-ESP32 serial port.

## 5. Calibrate the camera while stopped

Open the [SSH tunnel](02_LINUX_AND_VSCODE.md). On a fresh installation there
is no calibration profile yet, so the annotated preview can report a fault
without displaying an image. First inspect the raw camera at laptop
`http://127.0.0.1:18080`. The default sample is x=4–25% of image width,
y=86–98% of image height: a small lower-left patch. It must genuinely be
clear floor. After calibration, inspect the blue sample box and amber watched
region at laptop `http://127.0.0.1:18767`. With motor power OFF and controller
stopped/zero:

```bash
cd /home/orangepi/argus/avoidance
sudo -u orangepi ./argus obstacle-calibrate
./argus obstacle-status
```

Ten fresh frames build a frozen profile in `.state/floor.json`. It expires
after 15 minutes and is not shared as a universal model. The custom command
used in the recorded scene was `--sample .04 .86 .25 .98`; only use those
coordinates if that patch is actually clear in your current view.

No motor-on instruction is needed to finish the software installation.
Proceed to [the separate physical checks](06_CHECKS_AND_FIRST_TESTS.md) later.

## 6. Optional ROS package build

Only do this for learning or the LiDAR preview. It does not connect ROS to
the current wheel path. On a Pi with the existing Humble base and colcon,
install the additions as administrator:

```bash
sudo apt-get install --no-install-recommends ros-humble-nav2-collision-monitor ros-humble-nav2-lifecycle-manager
```

Build as `orangepi`. If your terminal is root, switch first with
`sudo -iu orangepi`, then run:

```bash
cd /home/orangepi/argus/avoidance
source /opt/ros/humble/setup.bash
colcon --log-base .ros/log build --base-paths . --packages-select argus_avoidance --build-base .ros/build --install-base .ros/install
source .ros/install/local_setup.bash
ros2 pkg prefix argus_avoidance
```

The two Nav2 packages were the additions recorded in the original setup;
they are not a complete ROS installation command. Do not change Humble to
Jazzy merely because an older project plan mentions it. Continue with
[the ROS guide](07_ROS_2_WITH_ARGUS.md).
