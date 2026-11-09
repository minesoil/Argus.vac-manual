# Orange Pi first verified connection

On 2026-11-07 Justin reported physically connecting Ethernet, opening VS Code
and connecting to the board. He requested a setup understandable to someone
familiar with Arduino motors and new to ROS/Linux. When asked about the USB
serial adapter's endpoint, he selected “Something else or unsure.”

The Windows USB Ethernet adapter had a 1 Gbps link from 192.168.137.1 to
192.168.137.195 on SSH port 22. The board identified itself as `orangepi5`.
Its image reports Orange Pi 1.2.2, Ubuntu 22.04.5 Jammy, ARM64, Python 3.10.12
and ROS 2 Humble under `/opt/ros/humble`. The regular account is `orangepi`.
Installed camera scripts, VS Code Server and two lidar workspaces were present.
The address is a dated observation and may change. No authentication secrets
are included in project memory.

A new workspace was installed as the regular user at `~/argus/avoidance`.
The board built the package, passed 44 software tests and ran an isolated live
Humble preview with synthetic scans, transforms and zero output throughout.
Five targeted packages occupied about 7.6 MB. The direct real-network lidar
listener received no scan. USB enumeration and kernel logs showed a camera and
a CH340 adapter whose ttyUSB0 disappeared when BRLTTY claimed the interface.

This supersedes earlier uncertainty about boot, OS version, Ethernet/SSH and
ROS installation. The Pi is configured for bench use. Mounting on the robot,
ESP32/Mega integration, physical lidar performance and automatic driving
remain unverified. [On-board report](../../workspace/robot_control/argus_avoidance/reports/ORANGE-PI-CHECK.md).
