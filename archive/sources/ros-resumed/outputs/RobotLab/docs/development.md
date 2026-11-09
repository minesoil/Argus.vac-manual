# Build and maintain

The source folders are the editable project. Executable extraction and ROS build output are generated files. Change a source file, run the relevant checks, then rebuild the affected target. Keep historical reports in `reports/history/`; a report is evidence for the version/date it names.

## Simulator update

From Ubuntu/WSL with ROS/Gazebo installed:

```bash
python3 tools/install-simulation.py --workspace /home/robot/vacuum_ws
cd /home/robot/vacuum_ws
python3 tools/lab_controller.py drive
```

The installer preserves a selected assembly and backs up source/tools before updating. Stop the drive panel before installing. On this Windows PC, run it through `wsl.exe -d VacuumRobot-24.04 -u robot --exec python3` with the script's `/mnt/c/...` path. Runtime workspace paths in Python resolve through `workspace_paths.py`; `ROBOT_LAB_WORKSPACE` overrides them for another deployment.

`build_furnished_room.py` regenerates the room. Sensor/control configuration lives inside `vacuum_sim/config`. `validate_drive.py` moves the robot; run it only with the Windows drive panel closed. The simulator uses domain 42 and a local Gazebo partition. NVIDIA/WSLg renderer overrides remain in this PC's existing `env.sh`, rather than the Orange Pi scripts.

## Tests

```bash
source /opt/ros/jazzy/setup.bash
ROS_DOMAIN_ID=43 ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST bash tests/run.sh
```

This runs Python model/export/save-conflict/wire/serial/ROS tests and compiles a host harness around the actual Mega sketch. The harness replaces AVR registers and serial I/O; it checks boot refusal, pulse generation, reversal, timeout, stop input, corrupt/replayed messages and reconnect. It does not establish electrical pulse shape or loaded motor behavior. Without sourced ROS, the hardware ROS tests report skipped.

The Mega target also needs an AVR compile using Arduino CLI or IDE. The official Arduino core may emit unused-parameter warnings. The official SLAMTEC source also emits upstream compiler warnings; it is pinned and kept separate from our code. Dependency versions are recorded in `config/dependencies.json`, with license files beside vendored graphics/driver source.

Own Python code is formatted with Black 25.1.0 and checked for F-series errors using Ruff 0.11.13. The editor uses Prettier 3.6.2. Vendor code is preserved as supplied. Comments describe units, ownership and failure behavior; ordinary assignments do not need narrating comments.

## Windows executable

In PowerShell:

```powershell
powershell.exe -NoProfile -File desktop\build\Build.ps1
```

The compiler embeds the separated source tree, excluding archives, ROS builds, caches and generated logs. If a sibling `RobotLab/` source folder exists, the executable opens it so edits remain visible. A standalone executable extracts its embedded tree to a versioned local cache. Saved designs and controller profiles live outside that cache. `--check --report PATH` verifies menu construction without driving; `--files`, `--drive` and `--designer` open the corresponding workflow.

To change an interface, edit both sides and add a test that would fail under the old behavior. Physical verification belongs in a separate dated report; keep the distinction between a compile, a fake-device test and a measured hardware result.
