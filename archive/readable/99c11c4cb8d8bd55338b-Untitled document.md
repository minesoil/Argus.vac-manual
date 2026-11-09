# Untitled document

Historical source: connector-intake


## word/document.xml
================================================================================
AIVAC — AI VISION ROBOT VACUUM
COMPLETE BUILD SPECIFICATION
Version 1.0 | All units in millimetres unless otherwise stated
================================================================================
TABLE OF CONTENTS
-----------------
1.  Project Overview
2.  Bill of Materials
3.  Structural Parts & Dimensions
4.  Electronic Components & Specifications
5.  Drivetrain Specifications
6.  Power System
7.  Sensor Suite
8.  Vacuum & Dustbin Module
9.  Wiring & Cable Routing
10. CAD Assembly Positions
11. Mechanical Assembly Instructions
12. Electronics Assembly Instructions
13. Wiring Diagram & Connections
14. Software & Firmware Notes
15. Design Notes & Constraints
================================================================================
1. PROJECT OVERVIEW
================================================================================
Name:          AIVac
Type:          Autonomous AI-vision robot vacuum
Form factor:   Circular, Roomba-style differential-drive platform
Diameter:      296 mm (outer shell)
Height:        ~148 mm (floor to LiDAR top)
Drive type:    Differential drive — two NEMA 17 stepper motors
Navigation:    360-degree LiDAR (RPLIDAR A1) + front Pi Camera V2
Compute:       Raspberry Pi 4 (main AI/vision) + Arduino Mega 2560 (motor control)
Power:         3S1P 18650 lithium-ion pack (~11.1 V nominal)
Cleaning:      DIY centrifugal fan vacuum module with dustbin and pleated filter
Coordinate system (used throughout this document):
  - Origin: floor-level centre of robot
  - +Y axis: rear of robot (battery/dustbin side)
  - -Y axis: front of robot (bumper/camera side)
  - +X axis: right side of robot when viewed from above
  - +Z axis: upward
================================================================================
2. BILL OF MATERIALS
================================================================================
STRUCTURAL / PRINTED PARTS
---------------------------
  1x  Chassis Base Deck        PETG or MDF, circular, 236 mm dia, 8 mm thick
  1x  Outer Shell              3D printed or vacuum-formed, 296 mm dia
  1x  Front Bumper             Flexible rubber or TPU, 3-pad arc
  1x  Vacuum Module Housing    3D printed, multi-part sub-assembly
  8x  M3 Brass Heat-Set Insert 5.2 mm OD, 5 mm depth (Pi standoffs only)
  8x  M3x8 Pan-Head Screw      Shell service screws
  Various M3x6 screws         General electronics mounting
ELECTRONICS
-----------
  1x  Raspberry Pi 4 (any RAM variant)
  1x  Arduino Mega 2560
  2x  A4988 Stepper Motor Driver (Pololu-style carrier)
  1x  RPLIDAR A1 (Slamtec 360-degree LiDAR)
  1x  Raspberry Pi Camera Module V2
  1x  DC-DC Buck Converter, 12V to 5V, 5A minimum
DRIVETRAIN
----------
  2x  NEMA 17 Stepper Motor, 42 mm frame, 34 mm body
  2x  Drive Wheel, 65 mm OD, 24 mm wide, rubber tyre
  2x  D-shaft hub adapter, 5 mm bore
  1x  Front caster wheel assembly, 30 mm roller OD
POWER
-----
  3x  18650 Lithium-Ion Cell, 3.7V nominal, 68 mm length
  1x  BMS (Battery Management System), 3S, min 5A continuous
  1x  XT60 connector pair
  1x  Heat-shrink wrap, 72 mm wide minimum
  Assorted 18 AWG wire (red, black) for power
  Assorted 22 AWG wire (various) for signal
VACUUM MODULE
-------------
  1x  DC Brushed Motor, ~35.8 mm diameter, 57 mm body length
  1x  Centrifugal impeller, 60 mm OD (custom print or purchase)
  1x  Pleated paper or foam filter, ~92 mm x 36 mm
  1x  Dustbin container, transparent, 105 x 70 x 45 mm
  Rubber gasket strip for dustbin seal
FASTENERS & MISC
----------------
  4x  M3x6 standoff screws (Pi board mount)
  4x  M3x6 screws (Arduino board mount)
  Various M2.5 screws (LiDAR mount ears)
  Wire management clips or zip ties
  Double-sided foam tape (electronics mounting)
================================================================================
3. STRUCTURAL PARTS & DIMENSIONS
================================================================================
--------------------------------------------------------------------------------
3A. CHASSIS BASE DECK
--------------------------------------------------------------------------------
Source file: chassisBase.kcl
Material:    PETG (recommended) or MDF
Colour:      Dark brown / black
Overall shape:       Circular disc
Diameter:            236 mm (radius 118 mm)
Thickness:           8 mm
FRONT INTAKE CUTOUT:
  Width:             126 mm
  Depth (Y):         22 mm
  Position:          Centred on X-axis, near front edge at Y = -120 mm
  Z position:        Cuts full 8 mm through disc (remove operation, starts at Z = -1 mm)
PI BOARD STANDOFFS (x4):
  Standoff outer diameter:  8.4 mm (radius 4.2 mm)
  Standoff height:          10 mm (above disc top face)
  Pattern origin:           X = -76 mm, Y = 14 mm
  Pattern offsets:          X-spacing = 58 mm, Y-spacing = 49 mm
  Four positions:
    Standoff 1:  X = -76,  Y = 14
    Standoff 2:  X = -18,  Y = 14
    Standoff 3:  X = -76,  Y = 63
    Standoff 4:  X = -18,  Y = 63
ARDUINO BOARD STANDOFFS (x4):
  Standoff outer diameter:  8.4 mm (radius 4.2 mm)
  Standoff height:          10 mm
  Pattern origin:           X = 31 mm, Y = 18 mm
  Pattern offsets:          X-spacing = 72 mm, Y-spacing = 42 mm
  Four positions:
    Standoff 1:  X = 31,   Y = 18
    Standoff 2:  X = 103,  Y = 18
    Standoff 3:  X = 31,   Y = 60
    Standoff 4:  X = 103,  Y = 60
THREADED INSERT HOLES (Pi standoffs only, x4):
  Bore diameter:     5.2 mm
  Depth:             5 mm (drilled into top of Pi standoffs)
  Z position:        Standoff top face (Z = 18 mm above deck origin)
  Positions:         Same XY as the 4 Pi standoffs above
INTAKE SEAL LEDGES (rubber gasket seats, x3 strips):
  Height above deck: 4 mm
  Back strip:        126 x 5 mm, centred at X = 0, Y = -105
  Left strip:        5 x 34 mm, centred at X = -63, Y = -122
  Right strip:       5 x 34 mm, centred at X = +63, Y = -122
--------------------------------------------------------------------------------
3B. OUTER SHELL / TOP COVER
--------------------------------------------------------------------------------
Source file: outerShell.kcl
Material:    3D printed (translucent filament) or vacuum-formed clear plastic
Opacity:     ~68% translucent on skirt, ~78% on top lid
LOWER SKIRT:
  Outer diameter:    296 mm (radius 148 mm)
  Height:            38 mm
  Position offset:   Z = -4 mm relative to shell origin
TOP LID:
  Outer diameter:    256 mm (radius 128 mm)
  Height:            16 mm
  Position offset:   Z = +23 mm relative to shell origin
LIDAR COLLAR (raised ring on top lid):
  Outer diameter:    110 mm (radius 55 mm)
  Inner diameter:    74 mm (radius 37 mm)
  Height:            7 mm
  Z position:        +36 mm relative to shell origin
  Inner opening cue disc:  74 mm dia, 1.2 mm thick at Z = +40
FRONT CAMERA BEZEL:
  Width:             42 mm
  Depth (Y protrusion): 5 mm
  Height:            18 mm
  Position:          X = 0, Y = -149 mm, Z = +11 mm (relative to shell origin)
STATUS BUTTON (teal):
  Diameter:          22 mm
  Height proud:      3 mm
  Position:          X = -22, Y = -16, Z = +33 mm
STOP BUTTON (orange):
  Diameter:          22 mm
  Height proud:      3 mm
  Position:          X = +22, Y = -16, Z = +33 mm
REAR DUSTBIN WINDOW (transparent cutout):
  Width:             92 mm
  Height:            38 mm
  Depth:             4 mm (shallow recess or separate window panel)
  Position:          X = 0, Y = +87 mm, Z = +31 mm
SERVICE SCREWS (x8):
  Screw hole diameter:     4.4 mm
  Bolt circle radius:      108 mm
  Angular spacing:         45 degrees (8 evenly spaced)
  Z position:              33 mm relative to shell origin
  Centre of bolt circle:   X = 0, Y = 0, Z = 33 mm
--------------------------------------------------------------------------------
3C. FRONT BUMPER
--------------------------------------------------------------------------------
Source file: bumper.kcl
Material:    TPU rubber or similar compliant material (~90 Shore A)
Colour:      Matte black
FRONT PAD:
  Width:    124 mm
  Depth:    13 mm
  Height:   18 mm
  Position: X = 0, Y = -151 mm, Z = 0 (relative to bumper origin)
LEFT ANGLED PAD:
  Width:    76 mm
  Depth:    13 mm
  Height:   18 mm
  Rotation: -34 degrees about Z-axis
  Position: X = -96, Y = -128 mm, Z = 0
RIGHT ANGLED PAD:
  Width:    76 mm
  Depth:    13 mm
  Height:   18 mm
  Rotation: +34 degrees about Z-axis
  Position: X = +96, Y = -128 mm, Z = 0
FRONT SENSOR WINDOW (IR/obstacle sensor slot):
  Width:    50 mm
  Depth:    2.4 mm
  Height:   9 mm
  Position: X = 0, Y = -159 mm, Z = +2 mm
LEFT SENSOR WINDOW:
  Width:    30 mm
  Depth:    2.4 mm
  Height:   8 mm
  Rotation: -32 degrees about Z-axis
  Position: X = -100, Y = -136 mm, Z = +2 mm
RIGHT SENSOR WINDOW:
  Width:    30 mm
  Depth:    2.4 mm
  Height:   8 mm
  Rotation: +32 degrees about Z-axis
  Position: X = +100, Y = -136 mm, Z = +2 mm
================================================================================
4. ELECTRONIC COMPONENTS & SPECIFICATIONS
================================================================================
--------------------------------------------------------------------------------
4A. RASPBERRY PI 4
--------------------------------------------------------------------------------
Source file: raspberryPi4.kcl
Role:        Main compute — AI vision processing, SLAM, high-level control
PCB dimensions:      85 x 56 x 1.6 mm
Mount hole pattern:  58 mm (X) x 49 mm (Y) rectangle
Mount hole diameter: 2.7 mm clearance (pad OD = 5.2 mm)
Mount hole positions (relative to PCB centre):
  Hole 1:  X = -29, Y = -24.5
  Hole 2:  X = +29, Y = -24.5
  Hole 3:  X = -29, Y = +24.5
  Hole 4:  X = +29, Y = +24.5
Key components on board (for clearance modelling):
  SoC (BCM2711):       14 x 14 x 1.8 mm at X = -5, Y = 0
  RAM package:         12 x 10 x 1.5 mm at X = +12, Y = +6
  WiFi/BT shield:      14 x 10 x 1.2 mm at X = -23, Y = +15
  GPIO header (2x20):  51 x 5 x 6 mm at X = +3, Y = +24.3 (2.54 mm pin pitch)
Port locations (for shell cutout planning):
  USB-C power:         9 x 3.2 mm, left edge (X = -36 to -27, Y = -31.5)
  Micro HDMI x2:       8 x 3 mm each, left edge
  Ethernet:            16.5 x 13.5 mm, right end (X = +33)
  USB-A x2:            15 x 15 mm each, right end (X = +10 and +26)
Global assembly position:  X = -46, Y = +36, Z = +66 mm
Mounted on:                Pi standoffs, 4x M3 screws into brass heat-set inserts
--------------------------------------------------------------------------------
4B. ARDUINO MEGA 2560
--------------------------------------------------------------------------------
Source file: arduinoMega.kcl
Role:        Motor control bridge — receives commands from Pi, drives A4988 drivers,
             reads encoders and sensors, sends feedback to Pi via UART
PCB dimensions:      101.52 x 53.3 x 1.6 mm
Main chip (ATmega2560): 15 x 15 x 1.7 mm
USB chip:            9 x 9 x 1.3 mm
Crystal can:         Dia 7 mm, 8 mm long (horizontal orientation)
Port locations:
  USB-B port:          16 x 18 x 11 mm, left end (X = -45 relative to PCB centre)
  Barrel jack (7-12V): Dia 11 mm, 12 mm long, left end at Y = +19
Header rows (for clearance):
  Left row:     78 x 5 x 7 mm at Y = +24.5
  Right row:    78 x 5 x 7 mm at Y = -24.5
  Rear row:     5 x 36 x 7 mm at X = +46
Global assembly position:  X = +52, Y = +38, Z = +64 mm
--------------------------------------------------------------------------------
4C. A4988 STEPPER MOTOR DRIVER (x2)
--------------------------------------------------------------------------------
Source file: a4988Driver.kcl / a4988DriverRight.kcl
Role:        Microstepping driver for each NEMA 17 motor
Carrier:     Pololu-style 0.6" x 0.8" (15.2 x 20.3 mm)
PCB dimensions:      20.3 x 15.2 x 1.6 mm
Driver IC (A4988):   5.4 x 5.4 x 1.4 mm (centred on board)
Heatsink base:       8 x 8 x 2 mm
Heatsink fins:       3x fins, each 8 x 1 x 4 mm, spaced 3 mm apart
Trim potentiometer:  Dia 4.8 mm, 1.6 mm tall, at X = -6, Y = +4.3
Electrolytic cap:    Dia 4.2 mm, 5 mm tall, at X = +6, Y = -4.4
Pin headers:
  2 rows of 8 pins, 2.54 mm pitch
  Pin diameter:  0.9 mm
  Pin height:    6 mm above PCB
  Row spacing:   15.2 mm between rows
Global assembly positions:
  Left driver:   X = -82, Y = -2, Z = +58 mm
  Right driver:  X = +82, Y = -2, Z = +58 mm
Wiring (A4988 to Arduino Mega):
  STEP pin  → Arduino digital PWM pin
  DIR pin   → Arduino digital pin
  EN pin    → Arduino digital pin (active LOW)
  VMOT      → 12V rail (battery)
  GND       → Common ground
  VDD       → 5V logic (from buck converter or Arduino 5V pin)
  1A, 1B, 2A, 2B → NEMA 17 motor coil wires
--------------------------------------------------------------------------------
4D. RASPBERRY PI CAMERA MODULE V2
--------------------------------------------------------------------------------
Source file: piCameraV2.kcl
Role:        Forward-facing visual input — object detection, obstacle avoidance,
             AI vision processing
PCB dimensions:      25 x 24 x 1.4 mm
Lens housing:        Dia 10.4 mm, 4 mm tall (black)
Lens glass:          Dia 6 mm, 0.8 mm thick
Mount holes (x4):    Dia 2.1 mm at corners of 20.4 x 19 mm rectangle
Ribbon connector:    18 x 4 x 2 mm clamp on PCB bottom edge
Ribbon cable:        16 mm wide, 0.5 mm thick, flexible flat cable (FFC)
Global assembly position:  X = 0, Y = -153, Z = +61 mm
Orientation:               Rotated 90 degrees about X-axis (lens faces -Y direction)
Connects to:               Raspberry Pi 4 CSI camera port via FFC ribbon cable
================================================================================
5. DRIVETRAIN SPECIFICATIONS
================================================================================
--------------------------------------------------------------------------------
5A. DRIVE WHEEL (x2 — left and right)
--------------------------------------------------------------------------------
Source file: driveWheel.kcl / driveWheelRight.kcl
TYRE:
  Outer diameter:    65 mm (radius 32.5 mm)
  Width:             24 mm
  Material:          Rubber (high-traction, soft compound)
  Colour:            Matte black
PLASTIC HUB:
  Outer diameter:    36 mm (radius 18 mm)
  Width:             28 mm
  Sits inside tyre, press-fit or bonded
SHAFT ADAPTER:
  Outer diameter:    10 mm (radius 5 mm)
  Width/length:      30 mm
  Bore:              5 mm D-shaft (flat on shaft for set-screw keying)
  Material:          Aluminium or brass
TREAD BLOCKS:
  Count:             18 evenly spaced (20 degrees apart)
  Block size:        26 x 5 x 4 mm (width x Y x Z proud of tyre)
  Pattern:           Circular array around X-axis
  Inner radius:      32.5 mm + 1.5 mm gap = 34 mm from wheel CL to block inner face
Wheel centre-to-centre track width:    302 mm (X = -151 to X = +151)
Left wheel global position:            X = -151, Y = 0, Z = +18 mm
Right wheel global position:           X = +151, Y = 0, Z = +18 mm
Drive axis (wheel rotation axis):      X-axis
--------------------------------------------------------------------------------
5B. NEMA 17 STEPPER MOTOR (x2 — left and right)
--------------------------------------------------------------------------------
Source file: nema17Stepper.kcl / nema17StepperRight.kcl
FRAME:
  Face dimensions:    42.3 x 42.3 mm
  Body depth:         34 mm
  Front plate:        2.4 mm thick (aluminium, on shaft side)
  Rear plate:         2.4 mm thick (aluminium, on wire side)
  Total length:       34 + 2.4 + 2.4 = 38.8 mm (body + plates)
PILOT BOSS (front face, shaft-side):
  Outer diameter:    22 mm (radius 11 mm)
  Protrusion:        4 mm from front plate face
OUTPUT SHAFT:
  Diameter:          5 mm (D-shaft — 5 mm with one flat)
  Length:            20 mm (from pilot boss face)
MOUNT HOLES (M3, x4, standard NEMA 17 pattern):
  Pattern:           31 mm x 31 mm square (holes at ±15.5 mm in Y and Z)
  Hole size:         M3 clearance (3.2 mm dia)
  Location:          On front face (shaft side)
LEAD WIRES (x4):
  Colours:           Red, Black, Green, Yellow (standard bipolar wiring)
  Wire diameter:     1.8 mm
  Wire length:       44 mm from rear plate face
  Spacing:           7 mm apart vertically
Global assembly positions:
  Left motor:   X = -101, Y = 0, Z = +25 mm (shaft faces -X)
  Right motor:  X = +101, Y = 0, Z = +25 mm (rotated 180 deg about Z, shaft faces +X)
Motor-to-wheel shaft coupling:
  Motor shaft:       5 mm D-shaft, 20 mm long
  Wheel adapter bore: 5 mm
  Recommended:       Set-screw D-shaft hub coupler or press-fit adapter
  Engagement length: Minimum 15 mm insertion
--------------------------------------------------------------------------------
5C. FRONT CASTER WHEEL
--------------------------------------------------------------------------------
Source file: casterWheel.kcl
MOUNT PLATE (top of assembly):
  Width:    44 mm
  Depth:    34 mm
  Thickness: 4 mm
  Material:  Steel or printed composite
SWIVEL STEM:
  Outer diameter:  12 mm (radius 6 mm)
  Height:          18 mm
  Material:        Steel
FORK CHEEKS (x2):
  Thickness:       4 mm each
  Width (Y):       28 mm
  Height:          28 mm
  Spacing (gap):   24 mm between inner faces (26 mm between outer faces?)
  Positions:       X = -12 mm and X = +12 mm from fork centre
ROLLER:
  Outer diameter:  30 mm (radius 15 mm)
  Width:           18 mm
  Material:        Rubber
AXLE:
  Diameter:        5 mm
  Length:          34 mm (spans across both fork cheeks with excess)
Total assembly height (mount plate top to roller bottom): ~32 mm
Global assembly position:  X = 0, Y = -104, Z = +2 mm
================================================================================
6. POWER SYSTEM
================================================================================
--------------------------------------------------------------------------------
6A. BATTERY PACK — 3S1P 18650
--------------------------------------------------------------------------------
Source file: batteryPack.kcl
CELLS (x3):
  Chemistry:       Lithium-Ion
  Format:          18650 (18 mm dia, 65 mm length, actual 68 mm with wrap)
  Nominal voltage: 3.7 V per cell
  Pack voltage:    11.1 V nominal, 12.6 V max charge, 9.0 V cutoff
  Cell diameter:   18.6 mm (with wrapper)
  Cell length:     68 mm
  Cell pitch:      19 mm (centre-to-centre in pack)
  Configuration:   3 cells in series (3S), 1 parallel (1P)
PACK BODY:
  Outer shrink-wrap dimensions:  72 x 58 x 22 mm
  Wrap material:                 Heat-shrink PVC
BMS BOARD:
  Dimensions:    36 x 42 x 1.6 mm
  Function:      Overcharge, overdischarge, short-circuit protection
  Rating:        Minimum 5A continuous discharge
  Position:      Side-mounted on pack body at X = +38 mm
OUTPUT CONNECTOR:
  Type:     XT60 (male on pack)
  Body:     13 x 10 x 9 mm
  Colour:   Yellow
LEAD WIRES:
  Red (positive):   2.2 x 2.2 mm cross-section, 46 mm length from pack
  Black (negative): 2.2 x 2.2 mm cross-section, 46 mm length from pack
  Wire gauge:       Minimum 18 AWG (recommend 16 AWG for motor current)
Global assembly position:  X = 0, Y = +82, Z = +46 mm
Orientation:               Rotated 90 degrees about Z (cells run along X-axis)
--------------------------------------------------------------------------------
6B. DC-DC BUCK CONVERTER (12V to 5V / 5A)
--------------------------------------------------------------------------------
Source file: buckConverter.kcl
Input:       12V (from battery pack, post-BMS)
Output:      5V, minimum 5A (powers Raspberry Pi 4, camera, LiDAR)
BODY:
  Length:    52 mm
  Width:     31 mm
  Height:    18 mm
  Type:      Waterproof enclosure style
LABEL PLATE:
  Size:      38 x 24 mm on top face
INPUT WIRES:
  Red:       2.2 mm dia, 28 mm lead length
  Black:     2.2 mm dia, 28 mm lead length
OUTPUT WIRE:
  Yellow:    2.2 mm dia, 28 mm lead length
Global assembly position:  X = 0, Y = +96, Z = +68 mm
Power distribution:
  Battery 12V raw  → A4988 VMOT pins (motor power)
  Battery 12V raw  → Buck converter input
  Buck 5V output   → Raspberry Pi 4 USB-C (via appropriate connector)
  Buck 5V output   → Arduino Mega Vin or 5V pin (check regulator capacity)
  Buck 5V output   → LiDAR RPLIDAR A1 power
================================================================================
7. SENSOR SUITE
================================================================================
--------------------------------------------------------------------------------
7A. RPLIDAR A1 (360-degree LiDAR)
--------------------------------------------------------------------------------
Source file: lidarA1.kcl
Role:        SLAM (Simultaneous Localisation and Mapping), obstacle detection
BASE SLED:
  Length:    96.8 mm
  Width:     70.3 mm
  Height:    8 mm
LOWER ROTOR HOUSING:
  Outer diameter:  72 mm
  Height:          28 mm
UPPER ROTOR HOUSING:
  Outer diameter:  64 mm
  Height:          18 mm
TOTAL SENSOR HEIGHT:  ~55 mm
SCAN WINDOWS (semi-transparent openings):
  Front window:  18 x 8 mm, at X = +18, Y = -36, Z = +4 (relative to lidar origin)
  Side window:   15 x 7 mm, rotated 24 deg about Z, at X = -26, Y = -28, Z = +3
MOUNT EARS (x2):
  Size:      12 x 18 x 5 mm each
  Positions: X = -53 and X = +53, Y = 0, Z = -19
  Fasteners: M2.5 screws (2 per ear)
CABLE:
  Diameter:  2.2 mm
  From sled: 36 mm horizontal run, then routes to Arduino Mega USB
Power:       5V, 500 mA typical
Interface:   UART (TTL), 115200 baud default (or USB via included adapter)
Global assembly position:  X = 0, Y = 0, Z = +93 mm (sits in shell collar)
--------------------------------------------------------------------------------
7B. OBSTACLE / BUMPER SENSORS
--------------------------------------------------------------------------------
Sensor type:  IR proximity sensors (recommended) or micro-switches
Quantity:     3 (one behind each bumper sensor window)
Mounting:     Behind the 3 sensor windows in the front bumper
Sensor window positions (global Z = bumper Z + 2 mm = ~41 mm):
  Front:  X = 0,    Y = -159
  Left:   X = -100, Y = -136  (at -32 deg)
  Right:  X = +100, Y = -136  (at +32 deg)
Interface:    Arduino Mega digital input pins
================================================================================
8. VACUUM & DUSTBIN MODULE
================================================================================
Source file: vacuumModule.kcl
--------------------------------------------------------------------------------
8A. DUSTBIN
--------------------------------------------------------------------------------
Body:         105 x 70 x 45 mm, transparent (polycarbonate or clear PETG)
Position:     Centred at X = 0, Y = +48, Z = +7 (relative to vacuum module origin)
Construction: Shell wall ~2 mm, open top (hinged or removable lid)
Dustbin seal strip (front-face rubber gasket):
  Dimensions:  108 x 5 x 8 mm
  Position:    Y = +10, Z = +10 relative to module origin
Filter (inside dustbin, or between fan and dustbin):
  Type:        Pleated paper or foam
  Pleat count: 23 pleats
  Pleat size:  2 x 8 x 36 mm each
  Pleat pitch: 4 mm (centre-to-centre)
  Origin:      First pleat at X = -44, Y = +13, Z = +8
--------------------------------------------------------------------------------
8B. FAN HOUSING
--------------------------------------------------------------------------------
Outer diameter:  76 mm (radius 38 mm)
Height:          16 mm
Centre position: X = 0, Y = -36, Z = +4 (relative to module origin)
Material:        Printed composite or aluminium, dark grey
IMPELLER DISC:
  Outer diameter:  60 mm (radius 30 mm)
  Thickness:       3 mm
  Z position:      Z = +14 relative to module origin (inside housing)
IMPELLER BLADES (x9):
  Blade dimensions:  18 x 4 x 3 mm
  Blade rotation:    18 degrees sweep offset each
  Count:             9 blades, 40-degree arc each
  Pattern:           Circular, 360 degrees about Z through (0, -36)
  First blade at:    X = +14, Y = -36, Z = +18 relative to module origin
--------------------------------------------------------------------------------
8C. DC MOTOR
--------------------------------------------------------------------------------
Body:
  Diameter:    35.8 mm (radius 17.9 mm)
  Length:      57 mm
  Orientation: Horizontal — spins on X-axis (shaft faces -X)
  Centre:      X = 0, Y = -36, Z = +42 (relative to module origin)
Rear cap:
  Diameter:    37 mm
  Thickness:   5 mm
  Position:    X = +31 from motor centre
Output pinion (shaft):
  Diameter:    8 mm
  Length:      13 mm
  Position:    X = -35 from motor centre (drives impeller)
Motor specs:
  Type:        DC brushed
  Voltage:     12V nominal
  Drive:       Direct drive to impeller (no gearbox)
  Estimated RPM: 15,000–25,000 RPM at 12V
--------------------------------------------------------------------------------
8D. INTAKE DUCT & NOZZLE
--------------------------------------------------------------------------------
INTAKE DUCT:
  Width:      122 mm
  Depth (Y):  24 mm
  Height:     12 mm
  Position:   X = 0, Y = -102, Z = -6 (relative to module origin)
  Connects:   Floor intake to fan housing
NOZZLE LIP (floor-level rubber strip):
  Width:      132 mm
  Depth (Y):  8 mm
  Height:     6 mm
  Position:   X = 0, Y = -118, Z = -8 (relative to module origin)
  Material:   Rubber or soft TPU (2 mm gasket for floor compliance)
  Note:       Sits at floor level; global Z = 34 (module Z) - 8 = 26 mm above floor
Global assembly position of module:  X = 0, Y = 0, Z = +34 mm
================================================================================
9. WIRING & CABLE ROUTING
================================================================================
Source file: wiringHarness.kcl
All cable global positions given at their midpoint origin:
--------------------------------------------------------------------------------
9A. CAMERA RIBBON CABLE (FFC)
--------------------------------------------------------------------------------
Type:         Flexible flat cable (FFC), 16 mm wide, 0.5 mm thick
Connector:    Standard CSI FFC, locks into Pi 4 CSI port and camera board
Route:
  Segment A:  17 mm wide x 86 mm long, runs Y direction
              Global position: X = -44, Y = -82, Z = +57
  Segment B:  48 mm wide x 17 mm long, horizontal bend section
              Global position: X = -22, Y = -42, Z = +57
Total length: ~103 mm routed path from Pi to camera
--------------------------------------------------------------------------------
9B. PI TO ARDUINO SIGNAL WIRES (x2)
--------------------------------------------------------------------------------
Type:    Single-core 22 AWG, 1.4 mm diameter
Colour:  Teal
Use:     UART TX/RX between Raspberry Pi GPIO and Arduino Mega Serial pins
Length:  82 mm
Global positions:
  Wire 1:  X = +16 to X = +98, Y = +38, Z = +73
  Wire 2:  Same, Y = +42
Pi connection:    GPIO UART TX (BCM 14, Pin 8) and RX (BCM 15, Pin 10)
Arduino connection: Serial1 TX (Pin 18) and RX (Pin 19) on Mega
--------------------------------------------------------------------------------
9C. BATTERY POWER WIRES (main 12V rail)
--------------------------------------------------------------------------------
Type:    18 AWG stranded, 2.4 mm diameter
Red (+):   From battery XT60+ to buck converter input (+)
           Global: X = +24, Y = +83, Z = +66 — runs 54 mm in X direction
Black (-): 6 mm offset from red wire (Y = +77)
           Same dimensions, same length
--------------------------------------------------------------------------------
9D. MOTOR HARNESS BUNDLES (x2)
--------------------------------------------------------------------------------
Type:    4-conductor bundle (R/B/G/Y wires), 2.2 mm dia per bundle
Use:     Connects each A4988 driver output to NEMA 17 motor coils
Length:  70 mm each
Left motor bundle:
  Global position:  X = -92, Y = -14, Z = +52
  Runs from A4988 left driver to left NEMA 17 motor
Right motor bundle:
  Global position:  X = +92, Y = -14, Z = +52
  Runs from A4988 right driver to right NEMA 17 motor
NEMA 17 coil wiring (standard bipolar):
  Coil A+:  Red
  Coil A-:  Blue (Black in some variants)
  Coil B+:  Green
  Coil B-:  Yellow
A4988 motor output pins:
  1A → Coil A+
  1B → Coil A-
  2A → Coil B+
  2B → Coil B-
--------------------------------------------------------------------------------
9E. LIDAR CABLE
--------------------------------------------------------------------------------
Type:    Multi-conductor, 2 mm diameter
Route:
  Vertical run:    2 mm x 2 mm x 54 mm, at X = 0, Y = +8, Z = +86
                   (runs vertically from LiDAR sled down into chassis)
  Horizontal tail: 44 mm long, at X = -22, Y = -17, Z = +86
                   (routes toward Arduino Mega)
LiDAR interface:  USB (via RPLIDAR USB adapter) to Raspberry Pi USB-A port
                  OR UART TTL to Arduino Mega for relay to Pi
================================================================================
10. CAD ASSEMBLY POSITIONS
================================================================================
All coordinates in millimetres. Origin at floor-level robot centre.
+Y = rear, -Y = front, +X = right, +Z = up.
Part                    X       Y       Z       Pre-rotation        Notes
----                    ---     ---     ---     ------------        -----
Chassis Base            0       0       +18     none                Disc top face at Z=26
Outer Shell             0       0       +49     none                Skirt bottom at Z=45
Front Bumper            0       0       +39     none                Front-facing
Left Drive Wheel        -151    0       +18     none                Wheel CL
Right Drive Wheel       +151    0       +18     none                Wheel CL
Front Caster            0       -104    +2      none                Swivel type
Left NEMA 17            -101    0       +25     none                Shaft faces -X
Right NEMA 17           +101    0       +25     180 deg about Z     Shaft faces +X
Vacuum Module           0       0       +34     none                Nozzle at floor
Raspberry Pi 4          -46     +36     +66     none                On Pi standoffs
Arduino Mega            +52     +38     +64     none                On Arduino standoffs
Left A4988 Driver       -82     -2      +58     none                Left stepper driver
Right A4988 Driver      +82     -2      +58     none                Right stepper driver
Battery Pack            0       +82     +46     90 deg about Z      Cells run X-axis
Buck Converter          0       +96     +68     none                Above battery
Pi Camera V2            0       -153    +61     90 deg about X      Lens faces -Y
LiDAR A1                0       0       +93     none                Top of robot
Wiring Harness          —       —       —       none                At global coords
================================================================================
11. MECHANICAL ASSEMBLY INSTRUCTIONS
================================================================================
RECOMMENDED BUILD ORDER:
  1. Chassis Base (structural anchor — build or print first)
  2. Install brass heat-set inserts into Pi standoffs
  3. Caster wheel (bottom mount, front of chassis)
  4. NEMA 17 motors (mount inside chassis, shafts facing outward)
  5. Drive wheels (press onto motor shafts)
  6. Vacuum module (mount in chassis centre)
  7. Battery pack (rear of chassis)
  8. Arduino Mega (right side of chassis, on standoffs)
  9. Raspberry Pi 4 (left side of chassis, on standoffs with inserts)
  10. A4988 drivers (mount near motors)
  11. Buck converter (above battery)
  12. Pi Camera (mount in shell bezel, ribbon cable routed)
  13. LiDAR (mount in shell collar)
  14. Outer Shell (fit over chassis, 8 service screws)
  15. Bumper (press-fit or snap onto shell front)
  16. Wiring (final routing and connections)
CHASSIS ASSEMBLY:
  - Fix chassis base as the ground reference for all other parts
  - All motor and electronics mount points are relative to chassis top face (Z = 26 mm global)
  - Chassis sits 18 mm off floor (wheel radius = 32.5 mm, wheel CL at Z = 18 mm)
  - Ensure intake cutout (126 x 22 mm at Y = -120) aligns with vacuum nozzle
DRIVE WHEEL INSTALLATION:
  - Slide wheel shaft adapter onto NEMA 17 D-shaft
  - Minimum 15 mm shaft engagement
  - Tighten set-screw against the shaft flat
  - Wheel outer edge should clear chassis rim by minimum 5 mm
  - Wheel CL at X = ±151 mm; chassis radius = 118 mm; 33 mm overhang each side
  - Ensure shell wheel-well cutout provides ≥5 mm clearance around full tyre
CASTER INSTALLATION:
  - Mount plate (44 x 34 mm) bolts to bottom of chassis
  - Position at X = 0, Y = -104 from chassis centre
  - Caster roller at Z = +2 mm global (slightly above floor for slight forward tilt)
  - Swivel must rotate freely 360 degrees
MOTOR MOUNTING:
  - Left motor: shaft faces -X, body mounts inside chassis left pocket
  - Right motor: rotate body 180 degrees about Z so shaft faces +X
  - Mount face (front plate with 4 screw holes) faces outward
  - M3 screws through chassis into motor front face holes (31 mm pitch)
VACUUM MODULE:
  - Module drops into chassis centre opening, centred at X=0, Y=0
  - Nozzle lip (Z = 26 mm global) should brush the floor or have a 1–2 mm gap
  - Dustbin rear (+Y side) aligns with rear dustbin window in shell
  - Intake duct front (-Y side) aligns with chassis front intake cutout
SHELL INSTALLATION:
  - Lower skirt diameter (296 mm) slides over chassis (236 mm) with 30 mm overhang
  - 8 service screws on 216 mm bolt circle (M3x8 pan head)
  - Shell sits with bottom of skirt at Z = 45 mm global (5 mm overlap with chassis rim)
  - LiDAR collar (74 mm inner dia) aligns with LiDAR sensor on collar
  - Camera bezel (Y = -149 in shell) aligns with camera at Y = -153 global
BUMPER INSTALLATION:
  - Bumper three pads snap or bolt onto shell front exterior
  - Front pad (124 x 13 mm) spans the -Y face of the shell
  - Side pads angle back at ±34 degrees from front centreline
  - Sensor windows must align with IR sensor mounting holes inside
================================================================================
12. ELECTRONICS ASSEMBLY INSTRUCTIONS
================================================================================
PCB MOUNTING:
  - Install 4 brass heat-set inserts (M3, Dia 5.2 mm, 5 mm deep) into Pi standoffs
    using a soldering iron at ~200°C — press in flush to standoff top
  - Raspberry Pi 4: 4x M3x6 screws through PCB holes into inserts
  - Arduino Mega: 4x M3x6 screws directly into Arduino standoffs (no inserts)
  - A4988 drivers: mount on small PCB carrier or foam-taped to chassis wall
    at positions X = ±82, Y = -2, Z = +58
RASPBERRY PI 4 SETUP:
  - Install Raspberry Pi OS (64-bit recommended) or Ubuntu Server
  - Enable CSI camera: add `camera_auto_detect=1` to /boot/config.txt
  - Enable UART: add `enable_uart=1` to /boot/config.txt
  - Install ROS2 or custom Python scripts for SLAM and motor control
  - Connect camera FFC ribbon to CSI port (blue tab side faces away from HDMI ports)
  - Connect LiDAR USB adapter to USB-A port
ARDUINO MEGA SETUP:
  - Flash motor control firmware via USB-B cable from Pi or laptop
  - Firmware receives velocity commands over Serial1 (UART, 115200 baud)
  - Firmware outputs step/direction signals to A4988 drivers
  - Firmware reads bumper sensor GPIO inputs and sends to Pi
A4988 DRIVER SETUP:
  - Set microstepping via MS1/MS2/MS3 pins (leave floating for full-step,
    or wire to appropriate logic levels for 1/2, 1/4, 1/8, 1/16 step)
  - Adjust current limit potentiometer BEFORE connecting motor:
    Vref = I_limit x 8 x Rsense (Rsense = 0.05 ohm on Pololu A4988)
    Typical NEMA 17 @ 1.5A: Vref = 1.5 x 8 x 0.05 = 0.6V
  - Connect VMOT to 12V rail, GND to common ground
  - Connect VDD to 5V, GND to common ground
  - Connect STEP, DIR, EN to Arduino Mega digital pins
BUCK CONVERTER SETUP:
  - Connect input to battery positive and negative via XT60 or screw terminals
  - Adjust output voltage to exactly 5.0V before connecting Pi
  - Connect output to Pi 4 GPIO Pin 2 (5V) and Pin 6 (GND)
    OR use USB-C cable if converter has USB output
  - Ensure converter can supply minimum 3A for Pi + camera + LiDAR
================================================================================
13. WIRING DIAGRAM & CONNECTIONS
================================================================================
POWER DISTRIBUTION:
  Battery (+) ─────────┬──────────────────────────── Buck Converter IN(+)
                       └── A4988 Left VMOT
                       └── A4988 Right VMOT
                       └── DC Motor (vacuum fan) (+)
  Battery (-) ──────────────────────────────────────── Common Ground (GND rail)
  Buck OUT 5V ──────────┬───────────────────────────── Raspberry Pi 4 5V
                        └── Arduino Mega 5V (or via VIN with appropriate check)
                        └── LiDAR A1 5V
  Common GND ──────────── All ground pins on all boards
SIGNAL CONNECTIONS:
  Pi GPIO 14 (UART TX) ─────────────── Arduino Mega Pin 19 (Serial1 RX)
  Pi GPIO 15 (UART RX) ─────────────── Arduino Mega Pin 18 (Serial1 TX)
  Pi GPIO common GND ───────────────── Arduino GND
  Arduino Mega → Left A4988:
    Digital Pin X ────── STEP
    Digital Pin X ────── DIR
    Digital Pin X ────── EN (pull low to enable)
  Arduino Mega → Right A4988:
    Digital Pin X ────── STEP
    Digital Pin X ────── DIR
    Digital Pin X ────── EN
  Left A4988 → Left NEMA 17:
    1A ── Coil Red
    1B ── Coil Black/Blue
    2A ── Coil Green
    2B ── Coil Yellow
  Right A4988 → Right NEMA 17:
    Same colour mapping as left
  LiDAR → Raspberry Pi 4:
    USB (via RPLIDAR USB adapter board) ── Pi USB-A port
    Appears as /dev/ttyUSB0 on Pi
  Pi Camera → Raspberry Pi 4:
    FFC Ribbon cable ── CSI camera port (between HDMI ports and USB ports)
    /dev/video0 on Pi with libcamera drivers
  Bumper Sensors → Arduino Mega:
    Front sensor  ── Digital Pin (INPUT_PULLUP)
    Left sensor   ── Digital Pin (INPUT_PULLUP)
    Right sensor  ── Digital Pin (INPUT_PULLUP)
================================================================================
14. SOFTWARE & FIRMWARE NOTES
================================================================================
RASPBERRY PI SOFTWARE STACK:
  OS:          Raspberry Pi OS 64-bit or Ubuntu 22.04 Server
  Framework:   ROS2 Humble (recommended) or custom Python
  Key packages:
    - rplidar_ros2: LiDAR driver (publishes /scan topic)
    - nav2: Navigation stack (uses LiDAR for SLAM and path planning)
    - opencv-python: Camera image processing
    - picamera2: Pi Camera V2 interface
    - pyserial: UART communication with Arduino Mega
  Launch sequence:
    1. Start LiDAR node (rplidar_ros2)
    2. Start SLAM node (slam_toolbox or cartographer)
    3. Start camera node (pi_camera or v4l2_camera)
    4. Start navigation stack (nav2)
    5. Start motor control node (serial bridge to Arduino)
ARDUINO MEGA FIRMWARE:
  Language:    C++ (Arduino IDE or PlatformIO)
  Libraries:   AccelStepper (stepper motion control)
  Serial:      Serial1 at 115200 baud (UART pins 18/19)
  Protocol:    Custom simple text or binary protocol
                Example: "L120 R120\n" = left 120 steps/sec, right 120 steps/sec
  Loop:        Read Serial1 for velocity commands
               Update AccelStepper speeds
               Read bumper sensors
               Send sensor state back to Pi on Serial1
MOTOR CONTROL NOTES:
  - Differential drive: left and right speed difference creates turns
  - Full stop: set both speeds to 0
  - Spin in place: equal and opposite speeds on left and right
  - NEMA 17 steps per revolution: 200 (full step) to 3200 (1/16 step)
  - Wheel circumference: pi x 65 = 204.2 mm per revolution
  - Distance per step (full step): 204.2 / 200 = 1.02 mm
================================================================================
15. DESIGN NOTES & CONSTRAINTS
================================================================================
CLEARANCES:
  - Drive wheel track width 302 mm exceeds shell diameter 296 mm
    Wheels protrude 3 mm beyond shell on each side — this is intentional
    Shell side walls must have open wheel-well cutouts at X = ±118 mm
  - Battery pack (72 mm long when rotated 90 deg) ends at X = ±36 mm
    A4988 drivers at X = ±82 mm — clearance of 46 mm on each side
  - Vacuum nozzle bottom at global Z = 26 mm; chassis deck bottom at Z = 18 mm
    Nozzle extends 8 mm below deck bottom — requires chassis front cutout
HEIGHT STACK:
  Floor (Z = 0)
  Z = 2   Front caster contact point
  Z = 18  Drive wheel axle height / chassis deck underside
  Z = 26  Chassis deck top face
  Z = 34  Vacuum module base
  Z = 39  Bumper base
  Z = 45  Shell skirt bottom
  Z = 49  Shell origin
  Z = 58  A4988 drivers
  Z = 61  Pi Camera (rotated 90 deg, faces forward)
  Z = 64  Arduino Mega top
  Z = 66  Raspberry Pi 4
  Z = 68  Buck converter
  Z = 83  Shell top lid top
  Z = 87  LiDAR collar top
  Z = 93  LiDAR assembly base
  Z = ~148 LiDAR top (93 + 55 mm sensor height)
WEIGHT DISTRIBUTION:
  - Battery (heaviest component) mounted rear-centre (Y = +82)
  - Motors mounted symmetrically at X = ±101 for balance
  - Pi and Arduino mounted slightly rear of centre (Y = +36, Y = +38)
  - Caster at front (Y = -104) for 3-point stability triangle
  - Aim for centre of gravity close to drive axle line (Y = 0) and low (Z < 50)
IMPORTANT TOLERANCES:
  - Chassis disc (236 mm dia) inside shell skirt (296 mm inner dia):
    30 mm radial clearance — generous, used for wiring and component overhang
  - LiDAR sled (96.8 x 70.3 mm) in collar (74 mm inner dia):
    Sled width 70.3 mm — 3.7 mm clearance in narrow axis — tight fit, measure carefully
    Mount using 4 M2.5 screws through LiDAR mount ears
  - Standoff OD 8.4 mm, insert bore 5.2 mm: 1.6 mm wall — sufficient for PETG
  - Shaft adapter bore 5 mm, NEMA 17 shaft 5 mm: zero-clearance — use set screw
PRINTING NOTES (for 3D printed parts):
  - Chassis Base: Print flat (horizontal). 4 perimeters, 30% infill minimum.
    Use PETG for heat resistance near motors. Bed adhesion critical for 236 mm part.
  - Outer Shell: Print upright or on side. Requires supports for overhang.
    Consider printing in 2 halves (upper/lower) and joining with screws.
  - Bumper: Print in flexible TPU 95A. No supports needed. 3 perimeters, 15% infill.
  - Vacuum Module: Print in PETG or ABS. Multiple parts. Ensure airtight seals
    between fan housing and dustbin using silicone RTV if needed.
  - All threaded holes: Print slightly undersized and tap, or use heat-set inserts.
ELECTRICAL SAFETY:
  - Always connect battery LAST after all wiring is complete
  - Include a main power switch or fuse (3A blade fuse recommended) on battery positive
  - The BMS provides cell-level protection but does not replace a fuse for the motors
  - A4988 drivers generate heat — ensure the heatsink is firmly attached
  - Keep motor wires (A4988 to NEMA 17) as short as possible to reduce EMI
  - Add 100uF capacitor across VMOT and GND on each A4988 if not already present on carrier
KNOWN ISSUES / WATCH POINTS:
  - The chassis is modelled without wheel-well cutouts in the base disc
    In practice, drill or cut slots to allow wheel spokes/hub to clear chassis edge
  - Vacuum motor at 12V may pull 2–5A during suction peaks — size power wires accordingly
  - RPLIDAR A1 must have clear 360-degree line of sight — do not obstruct with wires
  - Pi Camera FFC ribbon cable (segment A: 17 x 86 mm) routes between Pi and camera
    Ensure routing does not kink or stress the ribbon at any bend point
================================================================================
END OF DOCUMENT
AIVac Build Specification v1.0
Derived from KCL source files: chassisBase, outerShell, bumper, driveWheel (x2),
nema17Stepper (x2), casterWheel, raspberryPi4, arduinoMega, a4988Driver (x2),
batteryPack, buckConverter, piCameraV2, lidarA1, vacuumModule, wiringHarness
================================================================================

## word/fontTable.xml


## word/numbering.xml


## word/settings.xml


## word/styles.xml


## word/theme/theme1.xml
