# Robot development environment installed

Completed on 2026-09-30 on this Windows PC.

| Component | Installed / location |
|---|---|
| Windows Subsystem for Linux | 3.0.1.0, WSL 2 with WSLg |
| Ubuntu | 24.04.5 LTS, distribution `VacuumRobot-24.04` |
| Linux storage | `E:\WSL\VacuumRobot\Ubuntu-24.04` |
| Linux account | `robot`, regular sudo user with privately set password |
| ROS 2 | Jazzy desktop and development tools |
| Gazebo | Harmonic / Gazebo Sim 8.15.0, ROS bridge and ros2_control integration |
| Navigation / mapping | Nav2 1.3.13 and SLAM Toolbox 2.8.5 |
| Graphical tools | Gazebo, RViz, VS Code WSL extension |
| Graphics | Verified D3D12 hardware acceleration on RTX 3060 laptop GPU |
| Workspace | `/home/robot/vacuum_ws` |
| Backup | New tar export under `F:\VacuumRobotBackups`; see `backup-verification.json` |

## Verification

- Ubuntu boots with systemd and WSLg; package database audit is clean.
- `colcon build --symlink-install` succeeds; URDF parses and Gazebo world validates.
- Both joint-state and differential-drive controllers become active.
- Simulated movement measured **0.468 m**; velocity falls effectively to zero after command expiry.
- Lidar publishes **360 finite samples** in `lidar_link`; RGB images and camera info publish in `camera_optical_frame` at **640 × 480**.
- SLAM publishes a **119 × 119** map; Nav2 reaches **(1.0, 0.0)** with success status and zero error code.
- Map saving succeeds; ROS dependency checks report all system dependencies satisfied.
- Gazebo and RViz graphical windows open; VS Code opens `vacuum_ws [WSL: VacuumRobot-24.04]`.
- The full Ubuntu export was created and its tar structure and SHA-256 verified. See `backup-verification.json`; the archive is approximately 6.8 GiB. A separate restoration/boot test was not run.

Visual inspection of the graphical windows was not completed because its permission prompt timed out. The simulation, sensor and navigation checks above exercised the running programs through ROS interfaces. These are startup and functional checks, not extended stress tests or validation of your physical robot.

## Windows changes

WSL and Virtual Machine Platform were installed/enabled. Two existing Microsoft devices that were disabled were enabled: Virtual Drive Enumerator and Hyper-V Virtualization Infrastructure Driver. Those targeted repairs allowed WSL to start. No unrelated disk/virtual-drive devices were changed.

The new account-level `.wslconfig` caps WSL at 10 GB RAM, six processors and 2 GB swap, with a 40 GB maximum Ubuntu virtual disk, NAT networking, GUI support and the WSL firewall enabled. These settings also apply to future WSL 2 distributions under this Windows account.

Windows remains installed. No partitioning, Windows replacement, firewall exceptions, firmware flashing, robot USB attachment, passwordless sudo or physical motor commands were performed.

Start with **[Robot-Guide.md](Robot-Guide.md)** and the three `.cmd` launchers in this folder. Geometry, masses, motor behavior and sensors are explicitly provisional.
