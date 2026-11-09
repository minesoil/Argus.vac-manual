# Prepared source — runtime validation pending

This workspace is being prepared while WSL is installed. It is not yet a validated robot simulation.
Gazebo, ROS, controller activation, graphics, sensor frames, mapping and navigation must be tested in Ubuntu before delivery.

All dimensions, mass, lidar settings and camera settings are provisional. The geometry is a 0.30 x 0.25 m chassis with two visual acrylic plates, a simplified collision body, 0.05 m radius wheels, a 0.29 m wheel separation and a low-friction caster approximation. No real motor or sensor is attached or configured.

URDF and controller wheel geometry must remain consistent. Controller command timeout is 0.5 seconds. Its simulated limit is 0.25 m/s forward, 0.15 m/s reverse, 1.0 rad/s yaw; these are software test settings, not validated physical-robot limits.

## Planned validation in Ubuntu

1. Source env.sh, run python3 tools/prepare_nav2.py, then colcon build --symlink-install.
2. Source env.sh again; run ros2 launch vacuum_sim sim.launch.py.
3. Confirm both controllers are active; clock, odom, joint states, laser and image topics publish; confirm sensor frames line up with the model in RViz.
4. Confirm WSLg is using hardware OpenGL and that camera and lidar rendering work.
5. Drive slowly in simulation with ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -p speed:=0.15 -p turn:=0.5. The adapter forwards Twist to stamped controller commands; stopping input must stop the simulated wheels within the configured timeout (allowing configured deceleration).
6. Launch mapping.launch.py, drive a loop and inspect /map, then start navigation.launch.py. Check Nav2 goal acceptance and successful movement to a free-space target. Inspect whether current Nav2 velocity smoother/collision monitor remaps feed /cmd_vel correctly.
7. Validate a saved map and localization workflow, shutdown/relaunch, and the Windows launch shortcuts before delivering.

Specific runtime checks still pending: URDF-to-SDF fixed-joint conversion; camera_info_topic and frame headers; ros2_control odometry remapping; RViz plugin/topic configuration; current Jazzy controller-limit parameter validation; SLAM launch parameter name; Nav2 defaults adapted by prepare_nav2.py. Do not report these as tested from static XML/Python checks.
