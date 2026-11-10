# How the boards work together

Think of the Mega as the part that repeatedly makes motor pulses, the ESP32
as the phone interface and drive gate, and the Pi as the computer that looks
at images. The Pi does not need to generate precisely timed step pulses.

```text
Phone browser --Wi-Fi/HTTP--> ESP32 --M:left,right / 9600 baud--> Mega
                                  |                              |
                                  |                           STEP/DIR
                                  |                              |
                                  |                         TB6600 drivers
                                  |                              |
                                  |                         NEMA 17 wheels
                                  |
USB camera -> Pi camera server -> Python vision
                                  |
                  Pi UART /dev/ttyS0, 115200 baud
                                  |
                      ESP32 GPIO25 RX / GPIO26 TX
```

Power and data are different connections. An ESP32 powered from a USB bank
can still exchange data with the Pi through the three GPIO wires. Ethernet
lets the laptop reach the Pi for SSH; it is not the robot's driving-command
path. The current setup has no established wireless SSH link to the Pi.

## The wire table

| Connection | Pi end | ESP32 end |
|---|---|---|
| Pi sends | physical pin 8, UART TX | GPIO25, UART RX |
| Pi receives | physical pin 10, UART RX | GPIO26, UART TX |
| Common reference | physical pin 6, GND | GND |

These are **physical header numbers** on the Pi and **GPIO labels** on the
ESP32. They are different numbering systems. The ESP32's plain TX/RX labels
are not the configured GPIO25/26 connection. Both UARTs use 3.3 V signals;
never substitute the Pi's 5 V power pins. Only inspect or alter wiring with
the relevant boards powered down.

The ESP32 sketch uses GPIO17 TX for the Mega's Serial1 input D19 (RX1), at
9600 baud. Verify actual wiring before changing it. The recovered Mega
baseline declares left STEP/DIR D24/D25 and right STEP/DIR D22/D23, but that
file does not prove the exact installed sketch or every physical connection.

## Follow one manual command

1. You enable a control mode on the phone.
2. Moving the joystick sends a request to the ESP32 page's HTTP server.
3. The ESP32 checks ownership, sequence, command age and selected mode.
4. In assisted manual mode, it also checks the camera guard and forward/35%
   bounds. A blocked or expired guard ends the drive session.
5. The ESP32 sends percentage values such as `M:20,25` to the Mega.
6. The Mega's M-command family turns those percentages into step rates. The
   TB6600 drivers provide the motor current.

`25%` is a fraction of a configured step rate, not a measured speed in m/s.
Microstepping, gearbox ratio, wheel size and available torque affect actual
motion. The recovered baseline's maximum is 3500 steps/s; do not assume this
is the exact installed constant without identifying the running firmware.

## Follow one camera warning

`argus-camera.service` provides timestamped snapshots on Pi localhost:8080.
`obstacles.py` reads them and compares a watched floor region against a
short-lived calibration. It publishes status on localhost:8767.
`usb_bridge.py --manual-guard` reads that status and sends a compact health
report over UART. Despite its old filename, this bridge now uses GPIO.

`ManualGuard.h` on the ESP32 owns the assisted-mode stop decision. A hazard,
fault or lost report stops the session and latches it. Later clear frames do
not start the wheels; the driver must deliberately enable assisted mode again.

| Software deadline | What it checks |
|---|---|
| 250 ms | Maximum age of an accepted guard observation on the Pi |
| 200 ms | Maximum accepted reported processing time |
| 800 ms | ESP32 guard-report lease |
| 350 ms | ESP32 driving-command lease |
| 900 ms | Timeout in the recovered Mega reference sketch |
| 15 minutes | Calibration lifetime |

These are software limits. They are not physical braking distances. The
latest real held-joystick object-stop test is still pending.

## ROS 2's place

The camera/manual path above is ordinary Python, HTTP and serial code. It
does not currently send wheel commands through ROS 2. A separate ROS adapter
can consume `/scan` and publish isolated avoidance-preview topics. The
[ROS guide](07_ROS_2_WITH_ARGUS.md) explains that path and the missing work
before it could become part of the physical drive system.
