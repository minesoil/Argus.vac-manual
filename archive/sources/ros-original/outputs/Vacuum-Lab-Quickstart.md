# Drive your vacuum robot

Double-click **Drive robot.cmd**. It starts the simulator, camera window, and obstacle guard, then opens the controller panel automatically. The connected Honeycomb Alpha is selected by name. Center the yoke, click **Arm drive**, then hold the bound drive button while driving.

- Push the yoke forward to move forward; pull it back to reverse; rotate it to steer.
- Release the drive button to stop. **STOP / disarm** or the bound stop button requires arming again.
- If pulling gives positive speed in the preview, pull the yoke back and click **Set pull = reverse**, then return to neutral. This calibrates direction for your device without guessing its axis sign.
- The default Alpha profile uses Y for speed, X for steering, button 1 for hold-to-drive, and button 3 for stop. Confirm button numbering in the live preview. Use momentary buttons for hold/stop.
- **Keep drive armed when switching windows** is enabled so you can select the camera or Gazebo while holding the drive button. Uncheck it to require controller-panel focus; changing this option disarms the robot. Disconnect, STOP, lost bridge status, or stale commands stop input. Driving begins disarmed.
- The panel shows whether the hold button is detected, the axes are in their dead zone, STOP is pressed, the Ubuntu guard is unavailable, or an obstacle is blocking the requested direction. It also compares guard output with actual odometry speed and flags missing feedback or a robot that is not moving despite commands. Follow the displayed reason instead of repeatedly arming.

The camera is configured for **60 FPS at 320 x 240**. Direct driving uses the lightweight camera viewer already installed in Ubuntu. Validation in the furnished scene measured about **62.3 frames per real second**; Gazebo timing produces a small difference from the configured 60 FPS. Opening more visualization or navigation workloads can reduce the delivered rate.

The new **8 x 7 m living room** includes an upholstered sofa, coffee table, woven rug, TV console, bookcase, dining table and chairs, home office, plants, curtains, wall art, and wood flooring. Furniture has collision shapes and clearance under tables. The renderer batches the static room by material; its 72 collision shapes belong to one fixed body, avoiding contact checks between stationary furniture and the floor. Dynamic shadows are disabled in the default scene to preserve camera performance. The room overview is `validation/furnished-20261007/room-overview.png` in Ubuntu and `Furnished-room-preview.png` beside this guide.

Keep the launcher files together in this folder. **Vacuum Lab.cmd** opens the main menu instead of starting automatically. Its **Drive now** button opens the same driving workflow. Enable the Gazebo checkbox before startup if you want the separate 3D world view; stop and restart to change that choice.

## Mapping, code, and custom bindings

**Mapping + navigation** starts the full mapping and destination-navigation workflow with RViz. Use RViz **Nav2 Goal** to select a destination. **Save current map** saves a uniquely named map in Ubuntu `~/vacuum_ws/maps`; it requires the mapping workflow. Saving does not switch the session into saved-map localization.

The navigation launch starts the six servers this robot's destination behavior tree uses, then its lifecycle manager after local discovery has settled. Lifecycle checks retry lost responses. DWB and its goal checker share a 0.10 m position tolerance so the controller does not stop outside the accepted goal radius.

**Open robot code**, **Ubuntu terminal**, and **Workspace and maps** open the same Ubuntu workspace. **Save custom profile** and **Load custom profile** store editable JSON controller bindings. Other devices exposed through the built-in Windows joystick API are supported up to six axes and 32 buttons. USB devices outside that API need another adapter.

Switching between direct driving and mapping restarts the simulator, resetting the current simulated pose and live mapping session. Save your map first if you need it. Closing the controller panel stops its input but leaves the simulator running; **Stop lab** shuts down the launcher-owned processes. Closing the main menu alone also leaves the simulator running.

## Simulation details and validation

All robot software runs in `VacuumRobot-24.04` as `robot`, inside `~/vacuum_ws`. Windows only hosts the launcher and reads the USB controller; no USB forwarding, drivers, packages, sudo, or Windows settings changes are required. Both launcher command sources pass through a command gate and Collision Monitor. The old keyboard teleop publishes directly and must not be used alongside this workflow.

Manual forward speed is capped at **0.50 m/s**, reverse at **0.30 m/s**, and turning at **1.2 rad/s**, with 0.8 m/s² acceleration limits. Autonomous destination navigation retains its 0.20 m/s planner limit. The steady-time input watchdog stops commands after 300 ms. Directional lidar stop/slow zones protect the requested direction: a front obstacle stops forward travel while allowing reverse into clear space, and a rear obstacle allows forward escape. Rotation has an all-around clearance zone; the predictive padded footprint and 500 ms lidar timeout remain active. The manual bridge also checks lidar freshness using steady time, including when the simulator clock is paused. This uses Nav2's [velocity polygons](https://docs.nav2.org/jazzy/tutorials/general_tutorials/using_collision_monitor/using_collision_monitor/).

Direct driving does not need SLAM or Nav2 planners. The robot has a 30 cm circular body with 2 cm costmap padding, 22 cm wheel separation, and a 3 cm body-center/axle offset. Physics runs at 180 Hz, with 60 Hz drive control, 60 Hz camera, 30 Hz odometry, and 10 Hz lidar. These are simulation choices, not measured hardware specifications.

October 7, 2026 checks passed: PowerShell 5.1 parsing and controller-panel construction; Alpha enumeration and speed-sign mapping; Windows-to-Ubuntu live guard status and EOF cleanup; startup/shutdown jobs; furnished-scene camera delivery; faster forward and reverse displacement; release and stale-input stopping; front/rear directional escape, collision stopping, predictive padded-body stopping, and stale-lidar stopping. Results are at `~/vacuum_ws/validation/direct-drive-20261007/results.json` and `validation/furnished-20261007/directional-guard.json`. Navigation/map-save checks are at `validation/lab-20261007/results.json`.

Actual button choices and USB-unplug behavior still need confirmation at your desk. No physical robot control, automatic room coverage, or docking is implemented. Original model/config sources are backed up under `model-backups`; the pre-furnished-room rollback is `model-backups/furnished-20261007-215930/before.tar.gz`. Logs and process state are under `.lab`. The launcher now waits for its camera process group to stop, preventing a leftover viewer from adding load to the next session. Delayed lifecycle health requests are retried rather than leaving the input bridge permanently stuck.
