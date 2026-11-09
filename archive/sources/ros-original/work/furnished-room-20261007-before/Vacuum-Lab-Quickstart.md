# Drive your vacuum robot

Double-click **Drive robot.cmd**. It starts the simulator, camera window, and obstacle guard, then opens the controller panel automatically. The connected Honeycomb Alpha is selected by name. Center the yoke, click **Arm drive**, then hold the bound drive button while driving.

- Push the yoke forward to move forward; pull it back to reverse; rotate it to steer.
- Release the drive button to stop. **STOP / disarm** or the bound stop button requires arming again.
- If pulling gives positive speed in the preview, pull the yoke back and click **Set pull = reverse**, then return to neutral. This calibrates direction for your device without guessing its axis sign.
- The default Alpha profile uses Y for speed, X for steering, button 1 for hold-to-drive, and button 3 for stop. Confirm button numbering in the live preview. Use momentary buttons for hold/stop.
- Lost focus, disconnect, or stale commands stop input. Driving begins disarmed and does not automatically resume after a stop or a focus change.

The camera is configured for **60 FPS at 320 x 240**. Direct driving uses the lightweight camera viewer already installed in Ubuntu. Validation measured about **62.2 frames per real second**; Gazebo timing produces a small difference from the configured 60 FPS. Opening more visualization or navigation workloads can reduce the delivered rate.

Keep the launcher files together in this folder. **Vacuum Lab.cmd** opens the main menu instead of starting automatically. Its **Drive now** button opens the same driving workflow. Enable the Gazebo checkbox before startup if you want the separate 3D world view; stop and restart to change that choice.

## Mapping, code, and custom bindings

**Mapping + navigation** starts the full mapping and destination-navigation workflow with RViz. Use RViz **Nav2 Goal** to select a destination. **Save current map** saves a uniquely named map in Ubuntu `~/vacuum_ws/maps`; it requires the mapping workflow. Saving does not switch the session into saved-map localization.

**Open robot code**, **Ubuntu terminal**, and **Workspace and maps** open the same Ubuntu workspace. **Save custom profile** and **Load custom profile** store editable JSON controller bindings. Other devices exposed through the built-in Windows joystick API are supported up to six axes and 32 buttons. USB devices outside that API need another adapter.

Switching between direct driving and mapping restarts the simulator, resetting the current simulated pose and live mapping session. Save your map first if you need it. Closing the controller panel stops its input but leaves the simulator running; **Stop lab** shuts down the launcher-owned processes. Closing the main menu alone also leaves the simulator running.

## Simulation details and validation

All robot software runs in `VacuumRobot-24.04` as `robot`, inside `~/vacuum_ws`. Windows only hosts the launcher and reads the USB controller; no USB forwarding, drivers, packages, sudo, or Windows settings changes are required. Both launcher command sources pass through a command gate and Collision Monitor. The old keyboard teleop publishes directly and must not be used alongside this workflow.

Forward speed is capped at 0.15 m/s, reverse at 0.12 m/s, and turning at 0.5 rad/s. The steady-time input watchdog stops commands after 300 ms. Direct driving retains lidar stop/slow zones and a static predictive footprint; it does not need SLAM or Nav2 planners. The robot has a 30 cm circular body with 2 cm costmap padding, 22 cm wheel separation, and a 3 cm body-center/axle offset. Physics runs at 300 Hz to align with the 50 Hz controller, 60 Hz camera, and 10 Hz lidar. These are simulation choices, not measured hardware specifications.

October 7, 2026 checks passed: PowerShell 5.1 parsing and controller-panel construction; Alpha enumeration and speed-sign mapping; startup/shutdown jobs; camera delivery; forward and reverse displacement; release stopping; stale-input stopping. Results are at `~/vacuum_ws/validation/direct-drive-20261007/results.json`. Prior navigation/map-save checks are at `validation/lab-20261007/results.json`.

Actual button choices and USB-unplug behavior still need confirmation at your desk. No physical robot control, automatic room coverage, or docking is implemented. Original model/config sources are backed up under `model-backups`; logs and process state are under `.lab`.
