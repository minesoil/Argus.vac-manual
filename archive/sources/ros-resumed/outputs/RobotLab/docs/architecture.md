# Control paths and file ownership

The desktop controller sends JSON over WSL stdin to the simulator bridge. The bridge checks input freshness, lidar freshness and guard state, then publishes the manual command source. The source gate selects manual/navigation output. Nav2 Collision Monitor filters that command before Gazebo receives it. Closing stdin, disarming or losing health produces zero.

Hardware uses a separate path: teleop `/cmd_vel_raw` → Collision Monitor `/cmd_vel` → Orange Pi `motor_bridge` → USB → Mega → two TB6600s. The motor bridge has an explicit `/drive/arm` service. It clamps physical velocities, converts differential-drive velocities to pulse rates and sends commands at 50 Hz. The serial worker has its own 200 ms caller heartbeat. The Mega also has a 350 ms command watchdog.

## Geometry and saved data

`designs/default.json` is the editable seed. A saved design records each part's dimensions, position, rotation, mass, colour and collision flag. Template attachments preserve functional wheel joints and sensor frames. New parts become fixed links. `designer/model.py` validates the format and compiles models; `designer/templates/reference.urdf` preserves the sensor/plugin detail from the checked model.

The browser uses the same X/Y/Z frame as ROS. Three.js Euler order `ZYX` implements URDF roll/pitch/yaw. Stored sizes use metres, rotations radians. Assembly geometry is a set of primitive visuals; STL geometry is stored as base64 inside the design and copied to mesh files on export. Chassis collisions and navigation footprints update conservatively from the design. Collision boxes/masses remain estimates.

Each save uses a content revision. The local API rejects stale revisions and keeps older versions. The server binds to loopback, requires a random session token for API calls, rejects foreign origins, bounds payload sizes and constrains save names. It exposes fixed operations rather than a command or arbitrary-path interface.

`config/simulation.json` owns the simulator drive defaults. `vacuum_hardware/config/hardware.yaml` owns physical geometry, limits and serial paths. `drive_config.h` owns Mega pins, pulse polarity, timing, microsteps and direction inversion. Keep steps/revolution and driver DIP settings consistent; the exporter never raises physical speed limits.

## Serial protocol, version 1

All frames are ASCII lines ending in newline. The last field is four hexadecimal digits of CRC-16/CCITT-FALSE over bytes before the final comma. Initial CRC is `0xFFFF`, polynomial `0x1021`. The check string `123456789` yields `0x29B1`.

```text
V1,sequence,enabled,left_steps_per_second,right_steps_per_second,CRC
S1,sequence,armed,fault,left_issued_steps,right_issued_steps,CRC
```

Sequence is unsigned 16-bit. Enabled/armed is 0 or 1. Command rates are signed integers capped at 16000 pulses/s per wheel. Both wheel rates scale together if a limit is reached, preserving requested curvature. Status counts are signed presentations of modular 32-bit counters. The host uses modular differences to handle rollover.

Firmware fault codes: 0 healthy; 1 boot/timeout/handshake required; 2 stop loop open; 3 malformed, corrupt or replayed enabled frame. Disabled zero frames may reset the sequence after a host restart and cannot cause motion. Re-arming requires disabled zero, then enabled zero. Replayed enabled sequences disarm.

Wheel travel is `2π × radius × issued_steps / steps_per_revolution`. The bridge integrates it into `/odom` and publishes `/joint_states` and the `odom → base_footprint` transform. This is open-loop odometry. Missing steps and slipping wheels are unobserved; scan matching can correct the mapped pose but does not measure individual wheel motion.

## Runtime processes

The simulator launcher records PID plus Linux start identity and only stops processes it owns. `run_sim.py` tracks its child sessions and retains the single-simulator lock until cleanup ends. Applied-design updates reserve the manual-input lock and refuse to rebuild while a drive panel is open. Backups stay under `model-backups/`, marked `COLCON_IGNORE` so colcon cannot mistake them for active ROS packages.
