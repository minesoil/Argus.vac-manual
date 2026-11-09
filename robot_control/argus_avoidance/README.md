# Argus basic obstacle avoidance

**On the Orange Pi, open [START-HERE.md](START-HERE.md).** The workspace is
`/home/orangepi/argus/avoidance`. Run `./argus demo` to try the first example.
The installed ROS version is Humble. The
[board check](reports/ORANGE-PI-CHECK.md) records the tested preview and current
USB finding. The Windows verification below describes the earlier offline stage.

For the current black-tape driving setup, use the **Camera line following**
section in [START-HERE.md](START-HERE.md). The Pi sends camera steering over
USB to the updated ESP32, while a phone on its hotspot provides manual control
and Stop. The lidar controller described below remains a separate preview.

A small first implementation: crawl forward, slow for an obstacle, stop, turn
toward a clear side, then resume after several clear scans. Trapped, stale or
unknown input produces a latched stop. Automatic reversing is omitted.

The controller and standalone tests use **Python 3.10+ and the standard library
only**. They do not require Ubuntu, WSL, Gazebo, ROS, downloads or a serial port.
No physical hardware is started by the test runner.

## Run the lightweight checks on Windows

Open PowerShell in this folder and run:

```powershell
.\Run-Checks.ps1
```

The script uses an existing Python installation, runs the behavior and adapter
checks, then generates `reports/standalone-simulation.json`. It installs nothing.
You can supply an interpreter explicitly with `-PythonPath 'C:\path\python.exe'`.

With Python on PATH, the equivalent commands are:

```powershell
python -m unittest discover -s tests -v
python -m argus_avoidance.simulate --output reports/standalone-simulation.json
```

The simulation casts 720 lidar rays against simple walls and circles. An
independent body model includes acceleration/deceleration and checks for contact
every 0.01 simulated seconds. Scenarios cover open space, a wall, a thin chair
leg, a trapped corner, blocked rotation, lost/unknown scans, a moving obstacle
and an offset/yawed lidar. Simulated seconds run faster than real time.

Reports include actual integrated trajectories for replay. This is a simplified
2D simulation, not a Gazebo, ROS, lidar, motor, firmware or physical validation.
Adapter tests use small ROS stand-ins to exercise the real Python callbacks;
they do not verify DDS transport, real TF timing or ROS launch behavior.

## Files and behavior

- `argus_avoidance/core.py`: independent controller and configurable geometry.
- `argus_avoidance/simulate.py`: small raycast/kinematic test environment.
- `argus_avoidance/node.py`: optional ROS 2 Jazzy connection to the existing
  RobotLab control path. ROS is only needed when using this adapter.
- `config/avoidance.yaml`: disabled output and conservative physical defaults.
- `config/simulation.yaml`: explicitly allows this simulator's documented
  positive-infinity no-hit convention; do not assume it matches a real lidar.
- `tests/`: controller, geometry, scenario and offline adapter checks.

Initial settings are a provisional 0.22 m circular robot radius plus 0.03 m
margin, 0.05 m/s forward, 0.025 m/s slow and 0.30 rad/s turning. Distances are
relative to the inflated footprint: slow at 0.60 m, stop at 0.30 m, resume above
0.40 m over three distinct scans. A stop/settle interval precedes turning and
resuming. These are software defaults, not measured robot geometry or safe
loaded performance. The circle must contain every chassis protrusion.

The first version requires a fully known 360-degree scan for motion. **Even one
unknown ray prevents clearance approval**; a small missing cone could hide a
chair leg. Coverage ratio/gap settings provide diagnostics, not permission to
ignore unknown rays. Real no-return behavior must be established before changing
its interpretation. Tilted/missing transforms, stale/replayed scans and missing
guard health stop the ROS adapter. Fault recovery requires explicit mode selection.

## Optional ROS connection, once the robot computer is ready

Justin's latest confirmed manual route is **Wi-Fi → ESP32 → Mega**. The optional
ROS selector cannot intercept commands sent directly through that route. Its
firmware/protocol and stop/manual/automatic arbitration must be identified before
automatic robot control. The controller core can also support a future non-ROS
adapter; this work does not require choosing or installing ROS on the Pi now.
Orange Pi setup over Ethernet/SSH using VS Code is Justin's later setup idea.

This new package is separate from preserved RobotLab originals. It does not
change motor firmware, pin assignments, current settings or existing launches.
On a computer already configured for ROS 2 Jazzy, copy this package into its
colcon workspace's `src` folder and build `argus_avoidance` with its declared ROS
dependencies available. No ROS installation was performed during this work.

The initial launch only observes and publishes zeros to a preview topic:

```bash
ros2 launch argus_avoidance avoidance.launch.py
```

It expects `/scan`, a valid `lidar_link` → `base_link` transform and an active
Collision Monitor at `/collision_monitor/get_state`. Missing dependencies keep
it disarmed. `/avoidance/status` contains state, reason, candidate commands and
clearances. With output disabled, selected nonzero candidates appear in status
only. The adapter does not start the lidar driver or motor bridge.

For a guard-only dry run, `guarded_preview.launch.py` creates an isolated monitor
from `/avoidance/guard_input` to `/avoidance/guarded_cmd_vel`, without any motors.
It still needs live or replayed scans and valid robot/odom transforms. Defaults
remain `enable_output:=false`. Start a separate domain for such tests and ensure
no hardware consumes these topics.

Select automatic mode explicitly with:

```bash
ros2 service call /avoidance/set_auto std_srvs/srv/SetBool '{data: true}'
```

`false` cancels automatic mode and selects manual control when inputs are healthy;
it waits for a **new** Twist on `/avoidance/manual_cmd_vel` (0.25 s freshness).
Faults require mode selection again. Stop the node to end its command stream;
downstream command watchdogs must remain enabled.

When measured geometry, directions, lidar output and stopping are established,
the intended physical path is:

`manual OR automatic → this selector → /cmd_vel_raw → existing Collision Monitor → /cmd_vel → motor bridge → Mega`

The adapter rejects final `/cmd_vel` output, including unsafe topic remapping.
It does not arm the motor bridge. Keep `motion_enabled: false` until a separate
physical commissioning step. There must be exactly one selected command source
into the guard; stop/re-route competing teleop/navigation publishers. The old
simulator's command gate and the hardware path use different topic names.

Justin confirms on 2026-11-07 that the lidar lid now fits. This does not establish
fastening, cable clearance in motion, the final lidar transform, Orange Pi
installation, deployed Mega protocol or loaded stopping. Read the project build
notes before commissioning. A 2D scan cannot cover low cables/socks or drop-offs;
initial physical trials need a controlled level floor. Camera hazards are later work.

ROS references checked 2026-11-07:
[LaserScan definition](https://github.com/ros2/common_interfaces/blob/jazzy/sensor_msgs/msg/LaserScan.msg),
[Nav2 Jazzy monitor](https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/collision_monitor/configuring_collision_monitor_node/),
[guard placement](https://docs.nav2.org/jazzy/tutorials/general_tutorials/using_collision_monitor/using_collision_monitor/).
