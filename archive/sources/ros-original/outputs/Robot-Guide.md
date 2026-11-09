# Your Windows + Ubuntu robot environment

Windows remains your operating system. Ubuntu runs in WSL 2, with Linux programs opening their own graphical windows through WSLg. You do not need to dual boot.

## Start here

1. Double-click **Vacuum Simulator.cmd** to open Gazebo and RViz with the example vacuum robot. Keep its terminal open. Wait for both wheel controllers to become active.
2. Double-click **Ubuntu Terminal.cmd** for a Linux shell. Your Linux username is `robot`; `sudo` uses the private password you set. Password typing is invisible.
3. Double-click **Robot Code.cmd** to open `/home/robot/vacuum_ws` in VS Code through WSL. Choose **WSL: VacuumRobot-24.04** if VS Code asks which environment to use.

Use the commands below **inside Ubuntu**, not in a Windows PowerShell prompt. In each new terminal:

```bash
cd ~/vacuum_ws
source env.sh
```

## Drive the simulation

The default settings now reduce rendering load: camera **320 × 240 at 5 Hz**, RViz **15 frames/s**, and scene shadows disabled. Physics, drive control and the lidar configuration are unchanged. Original source configuration files are preserved at `~/vacuum_ws/performance-originals`; the full export on F: contains the original settings.

If the two graphical windows still feel slow, stop the current simulation first and use **Vacuum Simulator - RViz only.cmd**. Gazebo then runs the simulation without its separate 3D window, while RViz remains available for the robot, lidar, map and camera.

To request the original camera resolution/rate, start from an Ubuntu terminal:

```bash
ros2 launch vacuum_sim sim.launch.py camera_width:=640 camera_height:=480 camera_rate:=10
```

This increases rendering and image-transfer work. Only run one simulator instance at a time.

```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -p speed:=0.15 -p turn:=0.5
```

Focus the teleoperation terminal. `i` moves forward, `j` turns left, `l` turns right, `,` reverses, and `k` stops. Read the help printed by the program. The adapter clamps commands to 0.25 m/s forward, 0.15 m/s reverse and 1 rad/s rotation. The simulated drive controller stops when commands expire after 0.5 seconds; it also limits acceleration.

Only run one movement command source at a time. Stop teleoperation before starting autonomous navigation.

## Mapping and navigation

With the simulator running, start a second Ubuntu terminal:

```bash
cd ~/vacuum_ws
source env.sh
ros2 launch vacuum_sim mapping.launch.py
```

Drive slowly around the room to build a lidar map. RViz displays `/map`, `/scan`, the robot and camera image. For navigation, start another terminal:

```bash
cd ~/vacuum_ws
source env.sh
ros2 launch vacuum_sim navigation.launch.py
```

Keep mapping running. In RViz, set **Global Options → Fixed Frame** to `map`, choose **Nav2 Goal**, then click and drag a destination arrow in observed free space. This example navigates using the live SLAM map.

Save a map with:

```bash
mkdir -p ~/vacuum_ws/maps
ros2 run nav2_map_server map_saver_cli -f ~/vacuum_ws/maps/room --ros-args -p use_sim_time:=true
```

A saved map is data; this live-mapping launch does not automatically load it. AMCL localization and saved-map startup can be configured when your world and robot geometry are ready.

## Edit and rebuild

The workspace is in Ubuntu's filesystem for good Linux build performance. Windows Explorer can reach it at `\\wsl.localhost\VacuumRobot-24.04\home\robot\vacuum_ws`.

Key files are `src/vacuum_sim/urdf/vacuum.urdf.xacro` (body/sensors), `config/controllers.yaml` (drive geometry/limits), `config/nav2.yaml` (navigation), and `worlds/room.sdf` (room).

Wheel radius and separation must match in the URDF and controller configuration. The starting values are **50 mm wheel radius**, **290 mm wheel separation**, and a **300 × 250 mm** body. Body mass, caster behavior, inertias and sensor properties are placeholders. Replace them with measured dimensions and specifications.

```bash
cd ~/vacuum_ws
source env.sh
colcon build --symlink-install
source env.sh
```

Stop and restart the simulator after editing geometry or controller configuration. Build errors should be fixed before restarting.

## Stop and resume safely

Press **Ctrl+C** in teleoperation/navigation first, then mapping, then the simulator terminal. Wait for processes to exit. Windows PowerShell can stop this specific Ubuntu instance using:

```powershell
wsl --terminate VacuumRobot-24.04
```

Restart using the launchers. Do not use `wsl --unregister`: it deletes the Linux environment.

## Storage and isolation

Ubuntu is stored at `E:\WSL\VacuumRobot\Ubuntu-24.04`. The virtual disk grows as files are written, up to 40 GB. WSL is capped at 10 GB RAM, six processors, and 2 GB swap. These resource settings apply to all WSL 2 distributions on this Windows account. Keep free space on E: for disk growth.

`env.sh` uses ROS domain 42, localhost discovery, and a dedicated local Gazebo transport partition. These prevent accidental ROS discovery of other computers in the normal setup; WSL still has Internet access. No robot USB devices are attached or flashed, no robot motor commands are sent, and no Windows firewall rules have been opened.

## Backup

The full Ubuntu export is in `F:\VacuumRobotBackups`; its exact filename and SHA-256 are recorded in `backup-verification.json` beside this guide. Keep F: connected when accessing that backup. The export includes Linux programs, robot code, and Linux account settings; keep it private. Archive structure and checksum were checked; a separate restore-and-boot test was not performed.

If restoration is needed, use a **new distribution name and an empty storage location**. For example, in Windows PowerShell, replace `FULL_BACKUP_PATH` with the path in the verification file:

```powershell
wsl --import VacuumRobot-Restored E:\WSL\VacuumRobot-Restored "FULL_BACKUP_PATH" --version 2
wsl --manage VacuumRobot-Restored --set-default-user robot
wsl -d VacuumRobot-Restored -u robot --cd /home/robot/vacuum_ws
```

This preserves the current distribution. Run only one copy of the example simulator at a time. The launchers target `VacuumRobot-24.04`; change their distribution name if using a restored copy. There is also a small `vacuum-workspace-source.tar.gz` beside this guide containing the starter source and example saved map.

## Moving toward your physical vacuum

- **Orange Pi 5:** run the onboard ROS 2 stack on a compatible Ubuntu 24.04 ARM64 image, after checking its board kernel, camera and serial support. WSL is your PC development/simulation environment.
- **RPLIDAR C1:** add and test Slamtec's C1 driver on the actual Linux board. This simulation uses a generic 360-sample lidar and does not certify C1 performance.
- **Arduino Mega:** use ordinary firmware and a serial ROS bridge. The Mega is not a supported target of `micro_ros_arduino`; it should not run the full ROS stack.
- **NEMA 17 drive:** motor model, driver, gearing, wheel size and encoder feedback still need to be specified. The simulation assumes ideal velocity-controlled wheels and does not model lost steps, electrical current or motor torque limits.
- **Acrylic plates/camera:** measure plate dimensions, thickness, mass and sensor mounts. Simulation does not establish chassis strength, suction performance, battery safety or camera driver compatibility.

Before driving hardware, add a physical emergency stop, an onboard command watchdog, motor/current limits, and independent tests with the wheels lifted. Those hardware protections are separate from this simulator's timeout.

Official references: [ROS 2 Jazzy](https://docs.ros.org/en/jazzy/Installation/Ubuntu-Install-Debs.html), [Gazebo Harmonic with ROS](https://gazebosim.org/docs/harmonic/ros_installation/), [WSLg GUI applications](https://learn.microsoft.com/en-us/windows/wsl/tutorials/gui-apps), [Slamtec ROS 2 driver](https://github.com/Slamtec/sllidar_ros2), [micro-ROS Arduino supported boards](https://github.com/micro-ROS/micro_ros_arduino).
