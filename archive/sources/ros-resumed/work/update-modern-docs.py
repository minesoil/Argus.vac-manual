from pathlib import Path
out=Path(__file__).resolve().parents[1]/'outputs'
(out/'Vacuum-Lab-Quickstart.md').write_text('''# Vacuum Lab

Open **Vacuum Lab.exe**. The dark launcher includes driving, mapping/navigation, the project file browser, a room preview and your hardware profile. **Drive now** opens the simulator, camera viewer and Alpha controller panel.

## Drive with the yoke

1. Center the yoke and release STOP.
2. Click **Arm drive** once.
3. Push forward, pull back to reverse, and rotate to steer.
4. Center the yoke to stop. **STOP / disarm** or the configured STOP button stops drive and requires arming again.

You do **not** have to hold a drive button. **Require drive button** is optional and starts unchecked. Disconnect, panel closure, lost commands and stale lidar stop input. The obstacle guard remains active. It allows reversing away from a front obstacle or moving forward away from a rear obstacle when that direction is clear.

The Alpha profile uses Y for speed, X for steering and button 3 for STOP. The dead zone is 5%. If pulling gives positive preview speed, pull back and click **Set pull = reverse**, then return to neutral. **Set neutral center** recalibrates axes. Save/load profiles preserve the optional button requirement; older profiles load without requiring a button.

**Keep drive armed when switching windows** starts enabled so you can select the camera or Gazebo while driving. Disable it to require panel focus. Changing bindings or focus behavior disarms drive. Status compares requested, guarded and actual speed and explains blocked movement.

Manual limits are **1.5 m/s forward**, **0.9 m/s reverse** and **2.4 rad/s turning**. Windows input and ROS command forwarding run at 50 Hz. Acceleration is 6 m/s²; odometry uses three samples at 60 Hz. Camera target remains 60 FPS at 320 × 240. Current performance and response measurements are in **modern-drive-validation.json**.

## Your robot and world

The model uses **two NEMA 17 motors beneath the chassis**, **two TB6600 drivers**, **Arduino Mega 2560**, **Orange Pi 5**, **RPLIDAR C1** and **7 cm diameter wheels**. Chassis diameter remains 30 cm; wheel separation is 22 cm. The model has acrylic decks, motor brackets, electronics, scanner and front camera. **Robot profile** opens **Hardware-Profile.md**, which identifies provisional dimensions and hardware limits.

The **16 × 12 m room** includes living, dining, kitchen, reading and home-office areas. Its furniture collision shapes belong to a shared static body with batched visual materials. Enable **Open the Gazebo 3D view as well** before startup for the separate world view; stop/restart to change this.

**All project files** browses/searches the live Ubuntu workspace and hidden files, source, maps, logs, validation, rollback backups, installed ROS packages, original Windows files, Ubuntu disk/image and full backups. The first location contains files extracted from the EXE. Open files, reveal them in Explorer or copy their paths.

## Mapping and shutdown

**Mapping + navigation** starts SLAM/Nav2 and RViz. Use **Nav2 Goal** in RViz to choose a destination. Autonomous navigation retains its 0.20 m/s planner limit. **Save current map** writes a unique map in `~/vacuum_ws/maps` while mapping runs. Switching workflows restarts the simulator and resets the current pose and live map; save first if needed.

**Stop lab** shuts down the launcher-owned simulation. Closing the main menu leaves the simulator running; closing the controller stops its commands. **Open robot code** connects VS Code to the workspace; **Ubuntu terminal** opens a shell.

The existing WSL distro is `VacuumRobot-24.04`, user `robot`, workspace `/home/robot/vacuum_ws`. The executable bundles the launcher and source snapshot and uses the installed Ubuntu/ROS/Gazebo environment. It controls the simulator. Actual motor/driver variants and mechanical measurements remain unverified. Physical firmware/control, cleaning coverage and docking are not implemented; 1.5 m/s is not a verified real-robot speed.
''',encoding='utf-8')
(out/'Robot-Guide.md').write_text('''# Robot workspace

Open **Vacuum Lab.exe** and follow **Vacuum-Lab-Quickstart.md**. Click **Drive now**, center the yoke and arm once. You can drive without holding a button; center the yoke to stop.

The model has two under-chassis NEMA 17 motors, two TB6600 modules, 7 cm wheels, Arduino Mega 2560, Orange Pi 5 and RPLIDAR C1. Read **Hardware-Profile.md** for specifications and provisional geometry. Manual simulator limits are 1.5 m/s forward, 0.9 m/s reverse and 2.4 rad/s turning. The furnished world is 16 × 12 m.

**All project files** finds source, models/world/configuration, maps, logs and backups. The Linux workspace is `/home/robot/vacuum_ws` in WSL distro `VacuumRobot-24.04`. **Open robot code** connects VS Code to it. Use the launcher for driving, mapping/navigation, map saving and shutdown. Legacy keyboard teleop publishes directly and should not run alongside the launcher's controller.

Historical setup reports are retained with their dates. **modern-drive-validation.json** covers current motion and response; **directional-guard-validation.json** covers the guard; **executable-verification.json** covers the packaged launcher and file browser.
''',encoding='utf-8')
print('Guides updated for the current model and no-hold control.')
