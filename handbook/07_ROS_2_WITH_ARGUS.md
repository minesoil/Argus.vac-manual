# Understanding ROS 2 through Argus

Prepared on 10 November 2026 from the saved project source and dated checks. No connection to Argus was made for this guide. Commands described as learning exercises are instructions to try later, not a claim that they were all run during setup.

For Pi commands in this chapter use the `orangepi` account. If logged in as
root, first run `sudo -iu orangepi`; otherwise `~/argus` means `/root/argus`
and colcon can create root-owned build files. For Windows Python exercises,
use `py -3.12` on Justin's laptop rather than its `python` Store alias.

## Start with what is actually running

Argus's current camera control uses ordinary Python programs on the Orange Pi. The phone page is served by the ESP32. ROS 2 is installed on the Pi, but it is **not required by the current line follower or camera-assisted manual-drive prototype**.

There are two camera paths:

```text
Line following:
USB camera -> Pi Python tape detector/follower -> Pi GPIO serial
           -> ESP32 -> Mega -> motor drivers

Camera-assisted manual driving:
Phone joystick --------------------------------> ESP32 -> Mega -> motor drivers
USB camera -> Pi Python obstacle preview -> guard updates over GPIO serial --^
```

In assisted manual mode, the camera guard can block the ESP32's commands. It is a separate implementation from the optional ROS lidar preview described below. The camera prototype compares part of the picture with a calibrated floor appearance; it is not yet a general object-recognition system. The last recorded phone check confirmed that a blocked/unavailable view refused assisted driving. A completed moving-robot camera-braking test is not established by that check.

The Pi's `usb_bridge.py` name comes from an earlier USB control link. Its current configuration uses `/dev/ttyS0`, the GPIO UART. USB can still provide ESP32 power or firmware uploads. Ethernet is used for laptop access; it is not the camera controller's command link.

## Linux, Python and ROS have different jobs

| Thing | Job on Argus | Arduino comparison |
|---|---|---|
| Orange Pi | The physical computer with memory, USB and networking. | The board that runs your program. |
| Linux / Ubuntu | Runs programs, manages devices, files and networking. | More capable system software beneath your sketch. |
| Terminal / Bash | Accepts commands such as changing folders or starting a program. | A way to control the computer, rather than sketch code. |
| Python | The language used for camera processing and the avoidance controller. | Like using C++ for an Arduino sketch. |
| ROS 2 | Libraries, communication rules and tools for connecting robot software. | A structured way for multiple programs to exchange sensor readings and commands. |
| ESP32 firmware | Hosts the phone page, selects control modes, enforces command/guard expiry and talks to the Mega. | A sketch with Wi-Fi and control supervision. |
| Mega firmware | Converts its accepted wheel commands into driver signals. | The motor-control part you already know. |

An ordinary Python process does not become a ROS node just because it runs on a robot. A program becomes a ROS participant when it uses a ROS client library, such as Python's `rclpy`, and creates nodes/interfaces.

Also, a **Linux service** and a **ROS service** are different things. Linux's `systemd` starts background programs such as `argus-bridge`. A ROS service is a named request-and-response interface between ROS nodes.

## The ROS words, using this repository

| Word | Meaning | Argus example |
|---|---|---|
| Node | One participant doing a logical job in the ROS network. A process can contain more than one node. | `AvoidanceNode` in `node.py`, named `/argus_avoidance`. |
| Topic | A named channel for a stream of typed messages. Publishers send; subscribers receive. | `/scan` carries lidar scans. |
| Message | The agreed structure of one item sent on a topic. | `sensor_msgs/msg/LaserScan` contains a timestamp, frame, angles and ranges. |
| Service | A request followed by a response. | `/avoidance/set_auto` accepts a `std_srvs/srv/SetBool` request. |
| Parameter | A setting supplied to a node. | `enable_output: false`, or `robot_radius_m: 0.22`. |
| Package | A named unit of ROS source, dependencies and installed files. | `argus_avoidance`, identified by `package.xml`. |
| Workspace | A folder used to build and combine packages. | The Pi folder `~/argus/avoidance` is built using colcon, with generated files in `.ros/`. |
| Launch file | A Python recipe for starting nodes with settings. | `guarded_preview.launch.py` starts the controller and its preview guard. |
| Transform / TF | Describes where one coordinate frame is relative to another. | Where the lidar's scan frame is relative to `base_link`, the robot body. |
| Lifecycle | Managed node states such as unconfigured, inactive and active. | The Collision Monitor must be active before this adapter considers it healthy. |

These meanings follow the official Humble documentation for [nodes](https://github.com/ros2/ros2_documentation/blob/humble/source/Concepts/Basic/About-Nodes.rst), [topics](https://github.com/ros2/ros2_documentation/blob/humble/source/Concepts/Basic/About-Topics.rst) and [services](https://github.com/ros2/ros2_documentation/blob/humble/source/Concepts/Basic/About-Services.rst).

`geometry_msgs/msg/Twist` has linear and angular vectors. In this controller, `linear.x` is forward speed in metres per second and `angular.z` is turn rate in radians per second. They are **not** the current Mega's percentage wheel commands. A future hardware adapter needs a measured conversion between those units and wheel step rates. See the official [Twist](https://github.com/ros2/common_interfaces/blob/humble/geometry_msgs/msg/Twist.msg) and [LaserScan](https://github.com/ros2/common_interfaces/blob/humble/sensor_msgs/msg/LaserScan.msg) definitions.

## What was verified about ROS on the Pi

The dated [Orange Pi report](code/robot_control/argus_avoidance/reports/ORANGE-PI-CHECK.md) records Ubuntu 22.04.5, Python 3.10.12 and **ROS 2 Humble** on 7 November 2026. It records a successful colcon build and a live ROS preview using synthetic scans and test transforms, with all sampled command messages zero. This is saved evidence, not a fresh check of today's Pi.

Some early README paragraphs mention Jazzy and the removed RobotLab simulator. Those paragraphs describe the original optional adapter target. The later Pi report establishes Humble for the physical Pi. `guarded_preview.launch.py` selects `preview_guard_humble.yaml` when `ROS_DISTRO` is `humble`.

Justin reported the RPLIDAR C1 as faulty and ordered an adapter replacement. The exact failed component remains uncertain. Synthetic ROS scans working does not prove that the real lidar works, that its mounting transform is correct, or that ROS can stop the physical robot.

## Read the code in this order

All paths below are within `robot_control/argus_avoidance/` in GitHub, or the corresponding local/Pi package folder.

| File | What to look for |
|---|---|
| `argus_avoidance/core.py` | `Config`, `Scan` and `AvoidanceController`. This is ordinary Python: validate a scan, calculate clearances, decide STOP/SLOW/FORWARD/TURN. No ROS or serial port is required. |
| `argus_avoidance/simulate.py` | Supplies modeled scans and moves a modeled robot to exercise the controller. It does not move Argus. |
| `argus_avoidance/node.py` | Imports `rclpy`, receives ROS scans, obtains TF, calls the same controller and publishes ROS status/velocity messages. This is the adapter between the pure algorithm and ROS. |
| `config/avoidance.yaml` | Provisional geometry, distances, timeouts and output-disabled settings. These values are not measurements of loaded Argus. |
| `launch/avoidance.launch.py` | Starts only the controller. It does not start a lidar driver, Collision Monitor or motor bridge. |
| `launch/guarded_preview.launch.py` | Adds an isolated Collision Monitor and a lifecycle manager. It still starts no lidar driver or motor bridge. |
| `config/preview_guard_humble.yaml` | Humble's guard settings: input/output topics, scan source and rectangular stop zone. |
| `package.xml` | Declares ROS dependencies, including `rclpy`, message types, TF and Nav2 guard packages. |
| `setup.py` | Installs Python files, launch/config files and the executable entry point `avoidance_controller = argus_avoidance.node:main`. |
| `setup.cfg` | Places the installed executable where ROS expects package executables. |
| `argus` | A small Bash shortcut menu. Its `preview` command loads ROS and launches the output-disabled guarded preview. |

For the physical camera system, read `line_preview.py`, `follow.py`, `obstacles.py`, `manual_guard.py` and `usb_bridge.py` separately. They do not call the ROS adapter to reach the ESP32.

## The exact optional ROS preview path

The guarded launch uses these interfaces:

```text
external scan publisher -> /scan ----------------------+
external TF publishers -> /tf and /tf_static -----------+--> /argus_avoidance
                                                       |
/avoidance/manual_cmd_vel ------------------------------+

/argus_avoidance -> /avoidance/guard_input -> /avoidance_preview_guard
                                                    -> /avoidance/guarded_cmd_vel
```

| Name | Type or purpose |
|---|---|
| `/scan` | `sensor_msgs/msg/LaserScan`; expected input, not created by this launch. |
| `/avoidance/manual_cmd_vel` | `geometry_msgs/msg/Twist`; optional ROS manual input. It is separate from the phone joystick route. |
| `/avoidance/guard_input` | `geometry_msgs/msg/Twist`; controller output in the guarded preview. |
| `/avoidance/guarded_cmd_vel` | `geometry_msgs/msg/Twist`; preview Collision Monitor output. No physical bridge is launched to consume it. |
| `/avoidance/status` | `std_msgs/msg/String` containing JSON with state, reason, mode, candidate velocities, clearances and fault/guard flags. |
| `/avoidance/preview_stop_zone` | Guard polygon visualization. |
| `/avoidance/set_auto` | `std_srvs/srv/SetBool` mode-selection service. |
| `/avoidance_preview_guard/get_state` | Lifecycle health service queried by the adapter in the guarded launch. |

With the controller-only launch, its output defaults to `/avoidance/preview_cmd_vel` and its expected guard health service defaults to `/collision_monitor/get_state`. The guarded launch overrides those two names. It does not change the physical ESP32/Mega route.

The Humble guard has a rectangle from x=-0.30 to +0.30 m and y=-0.22 to +0.22 m in `base_link`. Its `max_points: 0` is Humble's configuration for stopping once the allowed count is exceeded. The other guard YAML uses a different Nav2 schema (`min_points: 1`, nested polygon text and a guard-state topic). Do not copy those newer settings into the Humble file just because their spelling looks clearer.

### Why a preview might remain DISARMED or FAULT

The controller begins disarmed. `enable_output: false` makes every published velocity zero even if status reports a nonzero candidate. The guard must be active and its health response fresh. The adapter also needs a valid source timestamp, scan geometry and a transform from the scan's actual `header.frame_id` into `base_link` at the scan time. The guard additionally uses its configured `odom` frame.

The default source-age limit is 0.50 s, future timestamp tolerance 0.05 s, guard health limit 0.75 s and ROS manual-command lifetime 0.25 s. A stale/repeated/out-of-order scan, a missing/tilted transform, unknown range data or lost guard health prevents motion approval. The core requires full-circle clearance and refuses motion with **any unknown ray**; the coverage ratio is diagnostic, not permission to ignore holes.

The physical YAML treats infinity/no-return as unknown. `simulation.yaml` allows positive infinity only for a simulator with a known no-hit convention. Changing that setting would not repair missing real lidar information.

`/avoidance/set_auto` with true requests automatic selection; false cancels automatic selection and, when healthy, selects ROS manual mode while waiting for a *new* manual message. A fault needs explicit mode reselection. Fresh scans alone do not resume a faulted session. This service never arms the ESP32 or Mega. There is no need to call it for the read-only learning session below.

The node rejects final `/cmd_vel` as an output, including remapping that would bypass the guard. That check helps preserve the intended downstream guard path. It does not make the separate phone/manual route protected by ROS.

## Exercises you can do away from Argus

Use the current package source, not historical code under `archive/` or `knowledge/objects/`. In Windows PowerShell, change to the current package folder and use your existing Python 3.10+ installation:

```powershell
cd 'C:\Users\justi\OneDrive\Documents\ChatGPT\Argus Vac\workspace\robot_control\argus_avoidance'
py -3.12 -m argus_avoidance.bench demo
```

This runs the wall example using Python's standard library. It needs no Pi, ROS, firmware, serial cable or simulator installation. Read its transition messages alongside `core.py`; ask which condition makes STOP become TURN, and which condition permits forward movement again. Reported distances are model results.

To run the saved software checks:

```powershell
py -3.12 -m unittest discover -s tests -v
```

The controller's software tests do not establish real stopping performance. Adapter tests with ROS stand-ins also do not establish live ROS networking or TF behavior; the dated on-Pi report supplies the separate live-preview evidence.

## A later stationary ROS reading session on the Pi

These are reproduction/learning commands backed by the current wrapper, launch files and START-HERE build recipe. They were not run again while writing this guide. They require an existing Humble installation and the saved package on the Pi. Keep motor power off for the bench session.

In a **Pi terminal**, establish the folder and load the two software layers:

```bash
cd ~/argus/avoidance
source /opt/ros/humble/setup.bash
source .ros/install/local_setup.bash
```

`source` changes that terminal's environment so commands can find installed ROS software. `/opt/ros/humble` is the base ROS installation; `.ros/install` adds this project's built package. A new terminal needs its own environment loaded.

If the package has been changed or the second file does not exist, the saved build command is:

```bash
colcon --log-base .ros/log build --base-paths . --packages-select argus_avoidance --build-base .ros/build --install-base .ros/install
source .ros/install/local_setup.bash
```

`colcon build` prepares and installs the ROS package into the selected local folder. It does not flash an Arduino or start a robot. `setup.py` tells it which Python modules, launch files and YAML files to install.

For an isolated, output-disabled preview, use the same localhost-only domain as the dated test:

```bash
export ROS_DOMAIN_ID=84
export ROS_LOCALHOST_ONLY=1
./argus preview
```

The domain separates this ROS discovery group, and localhost-only limits discovery to this computer. These settings are an extra boundary; use this domain only for the bench preview and keep hardware output disabled. The wrapper explicitly launches `guarded_preview.launch.py enable_output:=false`. Nothing here starts the lidar driver, supplies pretend hardware transforms, selects automatic mode or opens the ESP32 serial link.

In a **second Pi terminal**, load the same ROS environment and use the same domain settings:

```bash
cd ~/argus/avoidance
source /opt/ros/humble/setup.bash
source .ros/install/local_setup.bash
export ROS_DOMAIN_ID=84
export ROS_LOCALHOST_ONLY=1
ros2 node list
ros2 topic list -t
ros2 service list
ros2 topic echo /avoidance/status --once
```

The first three ROS commands list participants and interfaces; they do not send driving commands. The last listens for one status message. Without an external scan and valid transforms, waiting/disarmed/fault information is expected. A listed `/scan` topic alone does not prove fresh scans are arriving. Press **Ctrl+C** in the preview terminal when finished. Closing this learning session is not a substitute for the physical phone Stop.

Later, when a working lidar and its driver are available on the intended ROS network, `./argus scan` is the existing ten-second read-only listener. It starts no driver and listens for at most three scans. The isolated localhost/domain-84 preview above will not discover an unrelated network/domain publisher automatically.

## Where ROS could fit later

Keep the existing tested motor firmware while learning. First establish real lidar scans, measured sensor placement and robot geometry. Then compare ROS decisions with recorded scans while command output stays disabled. A physical ROS integration would still need a deliberate bridge into the current ESP32 command ownership and stop rules, wheel-unit conversion, freshness checks and commissioning.

The proposed ROS route is selected manual/autonomous command -> Collision Monitor -> physical command bridge -> ESP32/Mega. It is a future integration, not a description of today's wiring. Camera warnings and stopping can continue to improve in the present Python/ESP32 system before that work. Mapping, navigation and choosing detours are further steps; installing ROS by itself does not add them.

Source trail: current `node.py`, both launch files, four YAML files, `package.xml`, `setup.py`, `setup.cfg`, `argus`, `bench.py`, START-HERE and the dated Orange Pi report were read for this guide. Older README status paragraphs must be interpreted against the later dated hardware checks.
