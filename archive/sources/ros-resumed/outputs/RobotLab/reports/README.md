# Verification scope

Current review includes the 3D editor, saved-design model compiler, Arduino firmware, Orange Pi ROS bridge, deployment scripts and reorganized executable. `quality-review.json` records the final checks and their scope.

Earlier motion/navigation/FPS results are preserved under `history/`. They measured the previous simulator build: about 61 camera FPS, forward 90% response in 0.34 seconds, directional obstacle protection, successful navigation/map save and clean simulator shutdown. The current review reruns relevant checks after model/export changes rather than treating those older results as proof for every editable assembly.

Firmware compiles for Mega 2560. Its host harness tests the actual sketch logic with fake registers. ROS serial tests use fake devices and exercise arming/timeout behavior. Both the hardware ROS package and official lidar driver build on Ubuntu x86_64. The physical robot, Orange Pi board and power electronics were not connected for testing.

Editable layouts can be mechanically impossible. Wheel alignment is checked before simulation; mounting clearances, measured mass, wiring, torque and loaded motor performance need inspection on the assembled robot. Issued-step odometry has no encoder confirmation.
