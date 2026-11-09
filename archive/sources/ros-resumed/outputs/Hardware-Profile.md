# Your vacuum robot

The Gazebo model now represents two NEMA 17 motors mounted below two acrylic chassis plates, one 7 cm diameter wheel on each motor, two TB6600 modules, an Arduino Mega 2560, an Orange Pi 5, an RPLIDAR C1, and the existing front camera. The wheel radius is 0.035 m in both the robot geometry and differential-drive controller. The lower chassis plate sits above the wheels and motor bodies; brackets connect the motors beneath it.

The 30 cm chassis diameter and 22 cm wheel separation are retained from the previous model. Motor body length, driver enclosure size, brackets, mass, and electronics positions are provisional because the exact NEMA 17 and TB6600 variants and your mechanical measurements were not supplied. These visual components do not implement physical stepper electronics or measure torque, missed steps, battery sag, or real motor temperature.

The simulated control path is yoke → Windows controller panel → ROS command gate → Collision Monitor → Gazebo differential-drive controller. Your intended physical architecture is Orange Pi 5 running ROS 2, Arduino Mega producing step/direction signals, and one TB6600 driving each NEMA 17. No firmware or physical motor commands are sent by this launcher.

Manual simulator limits are **1.5 m/s forward**, **0.9 m/s reverse**, and **2.4 rad/s turning**. Input and command forwarding run at 50 Hz. The dead zone starts at 5%, acceleration is 6 m/s², and odometry averaging uses three samples at 60 Hz. Arm once to drive with the yoke; center it to stop. **Require drive button** is an optional setting that starts off. STOP, disconnect, stale commands, and lidar/obstacle protection remain active. Autonomous navigation retains its existing 0.20 m/s planner limit.

At 1.5 m/s, direct-drive 70 mm wheels turn at approximately 409 RPM. This is a simulator setting, not a verified loaded speed for your particular NEMA 17/TB6600 setup.

The C1 sensor approximation uses 10 Hz scans, 500 samples per revolution, and a 0.05–12 m range. Its hardware profile records the 460800-baud UART interface. These values follow [SLAMTEC's C1 specifications](https://www.slamtec.com/en/c1/spec); Gazebo approximates its returns and does not reproduce reflectivity-dependent limits. The Arduino board outline uses the published dimensions in [Arduino's Mega 2560 product information](https://store-usa.arduino.cc/products/arduino-mega-2560-rev3).

The room is now **16 × 12 m**, with living, dining, kitchen, reading and home-office areas. The world uses a shared static body with batched materials to retain camera performance. Changes have a rollback archive in `~/vacuum_ws/model-backups/modern-hardware-20261007/before.tar.gz`.

The editable profile is `robot-profile.json`; the live ROS model is `src/vacuum_sim/urdf/vacuum.urdf.xacro`, its wheel/speed configuration is `config/controllers.yaml`, and the room generator is `tools/build_furnished_room.py`. Find these through **All project files**. Scene or robot changes need a simulation restart.

See **Robot-model-preview.png** for the assembled model and **Furnished-room-preview.png** for the room. Current drive, obstacle, navigation/map-save and executable reports are included beside this guide. Simulator shutdown now waits for its owned Gazebo child processes before releasing the single-simulator lock; startup checks use fresh ROS discovery.
