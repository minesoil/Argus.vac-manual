# Verified installation — 2026-09-30

Ubuntu 24.04.5 / ROS 2 Jazzy / Gazebo Sim 8.15.0 (Harmonic) / Nav2 1.3.13.
The workspace builds, URDF and world validate, both drive controllers activate,
and simulated lidar, RGB image, camera info, joint state, TF and odometry publish.
The robot moved 0.468 m and stopped on command expiry. SLAM published a map;
Nav2 reached (1.0, 0.0) successfully and map saving succeeded.
All rosdep system dependencies are satisfied.

WSLg windows opened. VS Code connected to this WSL workspace. Hardware OpenGL
was verified as D3D12 on the NVIDIA RTX 3060 laptop GPU using env.sh settings.
Visual window inspection was not completed because its permission prompt timed out.

See README.md. Geometry, mass, sensor and drive properties remain placeholders.
These tests do not establish safety or performance of the physical robot.
