# Mega 2560 and TB6600 drive

The firmware controls one driver per NEMA 17 using step/direction signals. The Orange Pi connects to the Mega over USB and to the C1 using its USB serial adapter. No Orange Pi GPIO connection to a motor driver is needed for this implementation.

## Signal wiring

The supplied firmware assumes common-anode step/direction wiring. Check the labels and manual for your particular TB6600 module; modules sold under this name differ.

| Mega connection | Left driver | Right driver |
| --- | --- | --- |
| 5 V | PUL+ and DIR+ | PUL+ and DIR+ |
| D22 | PUL− | — |
| D23 | — | PUL− |
| D24 | DIR− | — |
| D25 | — | DIR− |
| D26 | Optional ENA− after polarity check | Optional ENA− after polarity check |

ENA is unused by default. With this setting, disarming stops pulses but does not promise removal of motor holding torque. Each driver's motor supply comes from the rated external supply, not the Mega's USB/5 V pin. Connect each motor's two coil pairs to A+/A− and B+/B− as labelled on the driver. Identify coil pairs with the motor datasheet or continuity measurement.

D27 has a pull-up and expects a normally closed stop loop to Mega GND. A closed loop is healthy; an open loop stops pulses. For a bench test, a jumper from D27 to GND closes the loop. The physical emergency-stop switch should also interrupt the motor power through a suitable circuit. The software stop input is not a substitute for cutting motor power.

## Settings to measure and check

Edit `firmware/mega_drive/drive_config.h`. Defaults are 200 full steps/revolution and 8 microsteps, so one wheel revolution needs 1600 pulses. Set both TB6600 microstep DIP switches to match. Set current according to your actual motor rating and driver instructions. The default right direction is inverted for mirrored motor mounting; verify both directions with wheels raised.

Edit `ros2/src/vacuum_hardware/config/hardware.yaml`. Match wheel radius, wheel separation and `steps_per_revolution` to the assembled robot. The supplied wheel radius is 0.035 m and separation is 0.22 m. `motion_enabled` starts false; change it after wiring and calibration checks. Physical limits start at 0.15 m/s forward, 0.08 m/s reverse and 0.8 rad/s turn.

At 1.5 m/s, a 70 mm wheel needs about 409 RPM. That simulation speed requires a loaded motor/driver/power test before use on the real chassis.

## Compile and upload

With Arduino CLI installed:

```bash
arduino-cli core install arduino:avr@1.8.8
arduino-cli compile --fqbn arduino:avr:mega firmware/mega_drive
arduino-cli board list
arduino-cli upload --fqbn arduino:avr:mega -p /dev/robot_mega firmware/mega_drive
```

Select your actual Mega port if the stable device alias has not been created yet. Alternatively open `mega_drive.ino` in the Arduino IDE, select Mega 2560, then compile/upload. Stop the ROS bridge before uploading because it owns the serial port.

Firmware boot/reset is disarmed. Valid commands require CRC, a sequence number and a fresh disabled-zero handshake followed by an enabled-zero handshake. The 40 kHz timer produces pulses of at least 25 µs with a separate low tick. It stops pulses after a 350 ms command timeout, a broken stop loop or invalid frame. The main loop ramps reversals through zero; its watchdog resets a stalled loop into disarmed boot.

Telemetry reports issued pulses. It does not confirm that the motor turned. The specified hardware has no wheel encoders; check step accuracy under load, and add encoders if you need measured wheel odometry.

The C1 configuration uses 460800 baud and its published range of 0.05–12 m. References: [SLAMTEC C1 specification](https://www.slamtec.com/en/c1/spec), [official C1 ROS launch](https://github.com/Slamtec/sllidar_ros2/blob/34300099fadfc772965962dec837bf436706188f/launch/sllidar_c1_launch.py), [DFRobot TB6600 module reference](https://wiki.dfrobot.com/dri0043). The DFRobot module is a wiring reference, not identification of your exact driver.
