# ROS 2 and Gazebo resumed

The furnished-room simulator, camera viewer, and Alpha controller panel are running. The panel starts disarmed: center the yoke, click **Arm drive**, then hold the bound drive button. Release it to stop.

The recovered changes provide 0.50 m/s forward and 0.30 m/s reverse commands, a furnished 8 x 7 m living room, directional obstacle escape, and status messages explaining why motion is blocked. The original agent had completed these changes and tests before stopping at a Windows-to-WSL file access error.

Recovery checks passed for controller logic, Windows joystick detection, live guard status, zero-input stopping and bridge cleanup, active drive controllers, lidar, and camera. Saved motion tests passed forward/reverse movement and stopping on release or stale input; the latest saved camera measurement was 61.7 frames per second. Saved obstacle, navigation-goal, and map-save tests also passed.

Use **Drive robot.cmd** to reopen this workflow or **Vacuum Lab.cmd** for the menu. Keep the files in this folder together. See **Vacuum-Lab-Quickstart.md** for controls and mapping. The room overview is **Furnished-room-preview.png**.

The Linux workspace remains `/home/robot/vacuum_ws` in `VacuumRobot-24.04`. This session controls the simulated robot.
