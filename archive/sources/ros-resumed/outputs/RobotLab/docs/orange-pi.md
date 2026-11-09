# Transfer to the Orange Pi 5

Copy the `RobotLab` folder or unpack the source ZIP into a directory you own, such as `~/robot-lab`. The hardware scripts resolve paths relative to that folder. They do not assume your Windows user name, WSL paths, or `/home/robot/vacuum_ws`.

Use a working Ubuntu 24.04 arm64 image for your Orange Pi 5. Jazzy supports Ubuntu Noble arm64; board boot/kernel support still depends on the image. Check with `cat /etc/os-release` and `dpkg --print-architecture`. The setup script refuses a different OS release or a 32-bit architecture.

## Install and build

From the copied folder:

```bash
bash tools/deploy/install-deps.sh
bash tools/deploy/fetch-lidar.sh
bash tools/deploy/build-hardware.sh
```

`install-deps.sh` installs the official ROS repository package and hardware dependencies using sudo. `fetch-lidar.sh` accepts the bundled SLAMTEC source, or fetches its pinned commit if missing. `build-hardware.sh` builds only the motor bridge and lidar driver; the Orange Pi does not need Gazebo.

## Stable USB device names

Connect the Mega and C1 adapter, then inspect each device:

```bash
ls -l /dev/serial/by-id/
udevadm info -a -n /dev/ttyACM0
udevadm info -a -n /dev/ttyUSB0
sudo usermod -aG dialout "$USER"
```

Use your actual port names. Edit `tools/deploy/99-robot-lab.rules.example` with each device's serial number. Copy the edited rules into `/etc/udev/rules.d/99-robot-lab.rules`, reload rules with `sudo udevadm control --reload-rules`, then reconnect the devices. Log out/in after adding the dialout group. The expected aliases are `/dev/robot_mega` and `/dev/robot_lidar`. If an adapter has no unique serial, configure its stable `/dev/serial/by-path/` path in the YAML and launch argument instead of using an ambiguous vendor/product match.

Upload the Mega sketch using [the firmware guide](hardware.md). Run `python3 tools/deploy/preflight.py` to report prerequisites. It does not open ports or move motors.

## Use your saved assembly

Copy your editor JSON into `designs/`, then:

```bash
python3 tools/deploy/export-hardware.py designs/your-design.json
bash tools/deploy/build-hardware.sh
```

The exporter updates sensor frames, geometry, wheel dimensions and the obstacle envelope. It copies imported STL files into the hardware package. Physical speed limits stay separate; motion is disabled after a model export so you can recalibrate.

## First drive

Start with wheels raised and the stop circuit working. Inspect `hardware.yaml`, confirm matching microsteps and wheel direction, then enable `motion_enabled` for the bench test. Start the bridge/lidar/obstacle monitor:

```bash
bash tools/deploy/run-hardware.sh
```

It starts disarmed. In another terminal, source `/opt/ros/jazzy/setup.bash` and `ros2/install/setup.bash`, and set `ROS_DOMAIN_ID=43`. Publish zero continuously on `/cmd_vel_raw` before arming, and inspect `/drive/status`:

```bash
ros2 topic pub --rate 20 /cmd_vel_raw geometry_msgs/msg/Twist '{}'
ros2 topic echo /drive/status
ros2 service call /drive/arm std_srvs/srv/SetBool '{data: true}'
```

Use separate terminals for the continuous publisher, status and service. After the zero handshake, use a teleop publisher on `/cmd_vel_raw`. The monitor publishes filtered commands on `/cmd_vel`; a command older than 250 ms disarms the bridge. A stale scan, inactive guard, serial failure or firmware fault also disarms it. Re-arm only at neutral. Disarm with the service using `{data: false}` or open the stop loop.

Domain 43 isolates hardware from the simulator's domain 42. Discovery defaults to this computer. If you intentionally control the robot over a network, configure the same hardware domain and discovery settings on both hosts; do not carry the simulator's local-only environment into that session.

The hardware code was built/tested on the Ubuntu x86_64 development machine with fake serial devices. Orange Pi USB timing, real torque/current and loaded motion remain bench checks. [ROS Jazzy installation reference](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html) and [supported platforms](https://www.ros.org/reps/rep-2000.html#jazzy-jalisco-may-2024-may-2029).
