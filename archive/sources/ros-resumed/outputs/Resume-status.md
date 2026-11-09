# Vacuum Lab / updated

The launcher, controller and file browser use the new dark interface. The model includes two under-chassis NEMA 17 motors, two TB6600 modules, Arduino Mega 2560, Orange Pi 5, RPLIDAR C1 and 7 cm diameter wheels.

Arm once and drive with the yoke; return to neutral to stop. A held button is optional and disabled by default. Manual simulator speed is 1.5 m/s forward, 0.9 m/s reverse and 2.4 rad/s turning. The room is 16 x 12 m with living, dining, kitchen, reading and office areas.

Current tests passed for motion, neutral/disarmed/stale-input stopping, directional obstacle escape and braking, navigation and map saving. Drive validation measured about 61 camera frames per second and 0.34 seconds to reach 90% of requested forward speed. Simulator shutdown and restart were checked after fixing orphaned Gazebo processes. See the JSON reports beside this document.

Open Vacuum Lab.exe. All project files is available in the launcher and controller. See Vacuum-Lab-Quickstart.md and Hardware-Profile.md for controls, model dimensions and provisional hardware assumptions. This launcher controls the simulator and uses the existing VacuumRobot-24.04 WSL installation.