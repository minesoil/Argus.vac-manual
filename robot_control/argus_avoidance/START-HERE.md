# Argus on your Orange Pi

## Phone line following (firmware installed 9 November)

Connect your phone to the ESP32 hotspot and open http://192.168.4.1. Refresh the
page after a firmware update. START LINE FOLLOWING asks the Pi to run the camera
follower for up to 30 seconds. Keep the phone page visible and unlocked: switching
away or losing its connection stops the phone-started session. STOP ends the run;
ENABLE MANUAL selects the joystick. A stopped run never restarts itself.

The Pi sends commands over GPIO UART, so Ethernet is for setup/monitoring and is
not needed by the follower. The camera, Pi, ESP32 and power supply stay on Argus.
The bridge starts at boot but waits for an explicit Start request. If the camera
cannot see a continuous strip of tape, it refuses to drive. Press STOP before
retrying a failed start. No camera obstacle detection is installed in this demo.

Commissioning status: the ESP32 upload is hash verified and all 88 software tests
pass on the Pi. The real phone button, operator Stop and untethered floor checks
still need to be completed. Keep motor power off for the first phone test.

The current bridge uses `/dev/ttyS0`, not USB data. ESP USB is temporarily plugged
into the Pi for the upload; the planned bank-powered arrangement needs restoring
and checking before the untethered trial.

In your connected VS Code window, choose **File → Open Folder** and enter
`/home/orangepi/argus/avoidance`. Choose **Terminal → New Terminal**. Commands
typed there run on the Pi over Ethernet. Use the everyday `orangepi` account.

Run these first, one line at a time:

```bash
cd ~/argus/avoidance
./argus status
./argus demo
```

`~` means your home folder. `./argus` runs the command file in this folder.
The wall demo prints the controller's decisions with simulated timestamps.
Look for the transition from SLOW to STOP to TURN, then forward motion again.
The demo finishes by reporting the modeled distance between the wall and the
edge of the robot. You can also choose **Terminal → Run Task → Argus: Wall demo**.

| Command | What you'll see |
|---|---|
| `./argus` | List the available commands. |
| `./argus status` | Board name, Linux version, Python, ROS and available serial ports. |
| `./argus demo` | Run the controller against a simulated wall. No robot connection needed. |
| `./argus check` | Run the software tests. Allow a little time for the simulated scenarios. |
| `./argus scan` | Listen for up to ten seconds on the lidar channel. If a driver publishes scans, show the sensor frame, valid range count and closest measured return. |
| `./argus preview` | Start the ROS controller and its collision monitor with output disabled. Press **Ctrl+C** to stop them. |

## Camera line following

The Pi reads the USB camera, finds the tape and chooses wheel speeds. The
current setup uses [three GPIO serial wires](PI-ESP32-WIRING.md) to the ESP32,
which passes the commands to the Mega. Your phone stays connected to the
ESP32 hotspot. Open **http://192.168.4.1** for the joystick
and **STOP**. **ENABLE MANUAL** selects joystick control. The phone video relay
is currently paused while resolving USB disconnects; the Pi continues using
the full 640 × 480 camera image for tape detection.

The ESP32 starts stopped. Automatic driving starts only when you run a command
with `--drive`; starting the Pi or opening the phone page does not start it.
The `argus-bridge` background service handles the shared USB connection.
You do not need a ROS command for this tape follower.

For the first camera course, place black tape on a light floor so it extends
away from the stationary camera through the lower part of the image. Run:

```bash
./argus line-preview --tape black --seconds 20
```

The preview prints LEFT, RIGHT, FORWARD or STOP. A negative offset places the
tape to the left of image center. STOP also appears when the image is unclear,
the line is missing, or several paths compete. The program ends after twenty
seconds. You can select **Terminal → Run Task → Argus: Black tape preview**.
Move the tape while keeping the robot still to check each decision. The next
stage is to test manual override and steering with the wheels raised.

After the raised-wheel steering and phone Stop checks, a short driving run is:

```bash
./argus follow --drive --seconds 3
```

For a supervised demo on a longer, clear strip, use the same command with
`--seconds 8`. Keep the phone's **STOP** ready and leave the Ethernet and power
cables slack. The live lidar is awaiting repair, so the tape follower needs a
clear course. This is an initial demonstration of line following; mapping and
floor-obstacle recognition are later stages.

It uses a base of 25 percent wheel speed and small left/right corrections,
capped at 35 percent. The initial 6 percent floor trial barely moved, so this
profile replaces it. Percentages refer to the Mega's step-rate setting; they
are not measured ground speed. It stops when time runs out, tape is lost,
the camera becomes stale, or you press **STOP** on the phone. **Ctrl+C** also
ends the run. After an uncertain reading or operator Stop, rerun the command
to start another session. Moving the phone joystick takes manual control.
Use a short, clear course: tape following does not detect obstacles or stairs.

The preview requires fresh capture timestamps from the Pi's camera server.
A frozen or old frame produces STOP. `./argus follow` runs the same preview.
Its explicit `--drive` option is for the separately prepared ESP32 automatic
firmware after a stationary tape check and raised-wheel control checks.
The [camera check report](reports/TAPE-PREVIEW-CHECK.md) records the current
results. The prepared ESP32 page starts in stopped mode and adds an
**ENABLE MANUAL** button before joystick use. Its **STOP** button stays latched
until control is explicitly enabled again.

## From a lidar reading to a wheel command

In an Arduino sketch, your loop might read a sensor, decide whether to turn,
and send the motors a speed. On the Pi, ROS lets separate programs handle those
jobs. Each running program is called a **node**. A **topic** is a named channel
on which one node sends readings or commands and other nodes listen.

The lidar driver publishes a ring of distance readings on `/scan`. The
controller checks those readings against the space the whole robot needs.
Its candidate speed has two parts: forward speed in metres per second and
turn rate in radians per second. The preview reports the decision on
`/avoidance/status`. With preview running, open another terminal and run:

```bash
source /opt/ros/humble/setup.bash
ros2 topic echo /avoidance/status --once
```

`source` loads the ROS commands into that terminal. With no scan or measured
sensor position available, expect a waiting or disarmed status. Preview commands
stay on the isolated `/avoidance/` topics. The commands in the table do not
start either a motor bridge or a serial connection to the Mega.

The camera follower uses the USB/manual ownership described above. The optional
ROS lidar preview is a separate controller and does not command the wheels.

## Live lidar check

The CH340 USB adapter is now identified as the ESP32 and has the stable name
`/dev/argus_esp32` on its current Pi USB socket. Justin reports that the C1 is
faulty and is awaiting a replacement adapter. When it arrives, identify its
own port and use `./argus scan` for a stationary reading. Check sensor direction
and mounting position before using its distances as chassis clearance.

## Files to start with

- `argus_avoidance/core.py` contains the stop-and-turn decisions and demo defaults.
- `config/avoidance.yaml` contains the ROS preview settings. The radius and
  stopping distances are estimates until measured on Argus.
- `README.md` covers the software and interfaces in more detail.

The Pi uses Ubuntu 22.04 and ROS 2 Humble. This workspace has its own build
files in `.ros/`. If you edit the optional ROS adapter, rebuild from this
folder:

```bash
source /opt/ros/humble/setup.bash
colcon --log-base .ros/log build --base-paths . --packages-select argus_avoidance --build-base .ros/build --install-base .ros/install
```
