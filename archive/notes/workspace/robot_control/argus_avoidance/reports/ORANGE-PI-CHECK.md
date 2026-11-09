# Orange Pi setup and ROS verification

Verified on November 7, 2026 over Ethernet. Host `orangepi5` runs Ubuntu
22.04.5 Jammy on ARM64 with Python 3.10.12 and ROS 2 Humble. VS Code uses the
`orangepi` account. Its existing `~/argus` camera scripts and ROS/lidar
workspaces are alongside the new project at `~/argus/avoidance`.

The package built with colcon. The existing ROS installation supplied the
runtime and lidar packages. Installing Humble's Collision Monitor and lifecycle
manager added five packages, about 7.6 MB. The preview uses Humble's floating
point array for the stop polygon and a zero `max_points` threshold.
[Humble reference](https://github.com/ros-navigation/navigation2/blob/humble/nav2_collision_monitor/params/collision_monitor_params.yaml)

| Board check | Observed result |
|---|---|
| `./argus status` | Reported the board, Python, ROS and workspace path. |
| `./argus demo` | Simulated wall, 9.2 cm closest modeled clearance, zero contacts. |
| `./argus check` | All 44 tests passed on the Pi. |
| `./argus preview` | Controller, Collision Monitor and lifecycle manager launched and shut down cleanly. |
| Isolated ROS test | With synthetic full-circle scans and two test transforms, the guard became active. The controller requested forward motion for an open path and a turn for an obstacle. Loss of scans latched FAULT. All 46 sampled guard input commands and 23 sampled guard output commands were zero. The test ran on localhost-only ROS domain 84. |
| `./argus scan` on the regular ROS network | No live scan arrived in ten seconds. |

Linux enumerated a USB camera and a CH340 adapter. The kernel logged
`ttyUSB0` attaching, then disappearing when BRLTTY claimed the USB interface.
Justin is unsure which device is attached. Device identification, sensor
mounting, live scans and physical stopping remain open. The next hardware
step is tracing the cable to its endpoint. No serial port was opened and no
wheel command was sent. Wi-Fi → ESP32 → Mega remains the manual control route.
