# My robot's hardware and mechanical architecture (1.6)

Voice pass 2026-08-25: this is my build log now, written as I did it. Updated 2026-09-27 for the below-chassis NEMA mounting, mounted camera, mounted lidar, and power-tool battery plan.

## 1. Chassis structure

I built the chassis from two acrylic plates, each 30 cm x 30 cm x 1 cm, held apart by metal spacers. I made it rigid on purpose: if the frame flexes, my camera and lidar move with it, and their readings pick up that wobble as noise. Keeping the sensors at a fixed height above the floor means what they see stays comparable between runs.

For stability I went with three contact points: two drive wheels at the back and a castor wheel in front. That keeps the robot steady while the differential steering turns it.

| Component | Spec | Purpose |
| --- | --- | --- |
| Upper/lower plates | 30cm x 30cm x 1cm acrylic | Main structure |
| Spacers | Metal standoffs | Set internal clearance |
| Castor wheel | Front-mounted, 360° | Third contact point |

## 2. Drive system

Two bipolar stepper motors move the robot, driven by Pololu A4988 drivers. As of 2026-09-27, both NEMAs are mounted below the chassis and one NEMA is wired. Four electrolytic capacitors (C2 to C5) sit across the motor supply lines because stepper coils kick voltage spikes back down the wire when they switch, and without those caps the spikes can kill an A4988.

The old between-plate mount with hot glue and popsicle sticks was too weak. The new mount puts the NEMAs below the chassis. I still treat odometry as approximate until both wheels are wired, Vref is set, and the wheel mounts survive a drive test.

## 3. Vacuum airflow

My first suction attempt barely lifted anything: I had the San Ace 40 fan blowing straight down from the top plate, so air just recirculated. The fix was to rotate the fan 90 degrees and mount it between the plates, directly behind a dust bag. Now it pulls air through the bag, pressure drops, and debris comes along with it. The drv-1012 board takes a PWM signal so I can vary fan speed.

## 4. Sweeper brushes

Suction alone struggles with heavier particles stuck to the floor, so I run two N20 micro gear motors spinning brushes in front of the intake. I call them "Frontish" and "Backish". They run from an L298N dual H-bridge off the raw 11.1 V rail, because the L298N wastes about 1.5 to 2 V internally and would starve on 5 V. I angled the bristles to sweep debris toward the intake opening.

## 5. Compute and sensors

An Orange Pi 5 (8 GB) is the brain: camera detection now, ROS 2 and SLAM later. While prototyping I use a Raspberry Pi 4B as a physical stand-in. Underneath it, an Arduino Mega 2560 handles the timing-critical work like step pulses and PWM, so Linux jitter can never stall a motor mid-step. The two boards talk over USB serial.

As of 2026-09-27, the USB camera and RPLidar C1 are physically mounted. They still need live software tests on the robot.

| Sensor/board | Role |
| --- | --- |
| Orange Pi 5 (8GB) | Vision, AI, later ROS 2 navigation |
| Arduino Mega 2560 | Real-time motor control (HAL) |
| RPLidar C1 | Mounted 360-degree scanner for mapping |
| USB camera | Mounted obstacle camera above the lidar scan plane |

## 6. Power distribution

I am switching the motor-side source from the 11.1 V LiPo plan to a power-tool battery adapter. The adapter parts are still shipping and should end in 14 AWG red/black leads. Before it powers the robot, I need to meter pack voltage and polarity. A RioRand LM2596 buck converter drops battery voltage to 5 V for the Arduino Mega and the driver/fan logic. The Orange Pi 5 does NOT run from this rail: it has its own dedicated 5000 mAh USB power bank, kept separate so motor noise never reaches the brain.

| Rail | Feeds | Connector |
| --- | --- | --- |
| Actuator battery rail | A4988 drivers, L298N, San Ace 40 after voltage is confirmed | Wago 221-415 |
| 5V regulated | Arduino Mega, driver logic (A4988 VDD, L298N 5V, fan logic) | Wago 221-413 |
| Pi power bank | Orange Pi 5 only (never merged with the battery side) | USB |
| Logic signals | drv-1012, L298N control, A4988 logic | Arduino Mega pins |
