# Robot Lab

Open **Vacuum Lab.exe** beside this folder. Choose **Design robot** to edit the assembly, **Drive now** to test it, or **All project files** to find the source and saved data. The Windows app uses the existing `VacuumRobot-24.04` WSL installation.

The supplied robot has two NEMA 17 motors below its acrylic chassis, two 70 mm wheels, two TB6600 drivers, an Arduino Mega 2560, an Orange Pi 5 and an RPLIDAR C1. Manual simulation runs in a 16 × 12 m room at up to 1.5 m/s forward. Arm once and centre the yoke to stop; holding a drive button is optional.

## Where things live

| Folder | Contents |
| --- | --- |
| `desktop/` | Windows launcher, yoke control and file browser |
| `designer/` | Offline 3D editor, save API and model exporter |
| `designs/` | Supplied editable design |
| `config/` | Simulator profile and pinned dependency versions |
| `ros2/src/vacuum_sim/` | Gazebo model, world, controllers, mapping and navigation |
| `ros2/src/vacuum_hardware/` | Orange Pi serial bridge, physical configuration and launch |
| `ros2/src/sllidar_ros2/` | Official SLAMTEC driver, pinned to the recorded commit |
| `firmware/mega_drive/` | Mega sketch, motor settings and serial protocol |
| `simulation/tools/` | Simulator startup, command guard and motion checks |
| `tools/deploy/` | Orange Pi setup, build, run and design export |
| `docs/` | Instructions and interface reference |
| `tests/` | Model, protocol, firmware and ROS checks |
| `assets/` | Preview images, app icon and editor screenshot |
| `reports/` | Current checks and historical measurements |
| `archive/` | Earlier files, preserved for reference |

Saved designs and their history live in `%LOCALAPPDATA%\VacuumLab\designs`. They survive executable updates. The live simulator workspace remains `/home/robot/vacuum_ws`; its logs, maps and model backups are runtime data, rather than source files.

## Start with the task you need

- [Move parts, add shapes or import STL](docs/designer.md)
- [Transfer the project to the Orange Pi](docs/orange-pi.md)
- [Wire and configure the Mega and TB6600s](docs/hardware.md)
- [Understand the control paths and serial messages](docs/architecture.md)
- [Build, test and maintain the code](docs/development.md)
- [See the checks and remaining limits](reports/README.md)

Component dimensions and masses are editable estimates. The physical profile starts at 0.15 m/s and with motion disabled. Simulation at 1.5 m/s does not establish that the real motor, driver and power system can achieve that speed. Issued-step odometry cannot detect wheel slip or missed steps.
