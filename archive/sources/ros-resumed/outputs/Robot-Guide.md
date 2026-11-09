# Robot workspace

Open **Vacuum Lab.exe** and follow **Vacuum-Lab-Quickstart.md**. Click **Drive now**, center the yoke and arm once. You can drive without holding a button; center the yoke to stop.

The model has two under-chassis NEMA 17 motors, two TB6600 modules, 7 cm wheels, Arduino Mega 2560, Orange Pi 5 and RPLIDAR C1. Read **Hardware-Profile.md** for specifications and provisional geometry. Manual simulator limits are 1.5 m/s forward, 0.9 m/s reverse and 2.4 rad/s turning. The furnished world is 16 × 12 m.

**All project files** finds source, models/world/configuration, maps, logs and backups. The Linux workspace is `/home/robot/vacuum_ws` in WSL distro `VacuumRobot-24.04`. **Open robot code** connects VS Code to it. Use the launcher for driving, mapping/navigation, map saving and shutdown. Legacy keyboard teleop publishes directly and should not run alongside the launcher's controller.

Historical setup reports are retained with their dates. **modern-drive-validation.json** covers current motion and response; **directional-guard-validation.json** covers the guard; **executable-verification.json** covers the packaged launcher and file browser.
