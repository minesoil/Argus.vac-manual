#!/usr/bin/env bash
set -euo pipefail
cd /home/robot/vacuum_ws
cp /mnt/c/Users/justi/Documents/Codex/2026-09-30/pl/outputs/Robot-Guide.md README.md
cat > PREPARATION_STATUS.md <<'EOF'
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
EOF
if ! grep -q '# Vacuum ROS environment' /home/robot/.bashrc; then
    cp /home/robot/.bashrc /home/robot/.bashrc.before-vacuum-setup
    cat >> /home/robot/.bashrc <<'EOF'

# Vacuum ROS environment: only this dedicated WSL user/workspace.
if [ -f "$HOME/vacuum_ws/env.sh" ]; then
    source "$HOME/vacuum_ws/env.sh"
fi
EOF
fi
cp simulation-check.json navigation-check.json /mnt/c/Users/justi/Documents/Codex/2026-09-30/pl/outputs/
tar -czf /mnt/c/Users/justi/Documents/Codex/2026-09-30/pl/outputs/vacuum-workspace-source.tar.gz \
    src tools env.sh README.md PREPARATION_STATUS.md maps simulation-check.json navigation-check.json
echo 'Workspace documentation and source archive prepared.'
