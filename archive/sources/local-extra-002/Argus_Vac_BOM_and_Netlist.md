# Argus Vac — Bill of Materials and Complete Wiring Netlist

> Extracted directly from the supplied Fritzing netlist XML (`Argus Vac_netlist_Final.txt`).
> No electrical corrections or inferred connections have been applied.

## Source

- Fritzing netlist date: `Sun Aug 23 18:13:50 2026`
- Sketch: `Argus Vac.fz`
- XML `<net>` elements: **148**
- Unique part IDs: **26**

## Bill of Materials (BOM)

| Qty | Fritzing Part ID | Label / Reference | Title |
|---:|---|---|---|
| 1 | `855132670` | 12V Negative Wago 1 | Wago 221-415 |
| 1 | `854114700` | 12V -> 5V DC-DC Buck Converter | RioRand LM2596 |
| 1 | `855139860` | 12V Negative Wago 2 | Wago 221-415 |
| 1 | `63160` | 5000 Mah 11.1V 30C 3s Lipo | Lithium Ion Polymer Battery 11.1v 5000mah |
| 1 | `854105670` | Right Motor Driver | Pololu A4988 |
| 1 | `854105590` | Left Motor Driver | Pololu A4988 |
| 1 | `855161530` | L298N1( Brush Motors Driver) | L298N DC motor driver |
| 1 | `854119220` | C3 | Electrolytic Capacitor |
| 1 | `67810` | C2 | Electrolytic Capacitor |
| 1 | `855130850` | 12V Positive Wago 1 | Wago 221-415 |
| 1 | `855148550` | San Ace 40 Motor Driver | drv-1012 |
| 1 | `855139890` | 12V Positive Wago 2 | Wago 221-415 |
| 1 | `855134960` | 12AWG 7.5AMP Fuse | FUSE |
| 1 | `59040` | Arduino mega | Arduino Mega 2560 (Rev3) |
| 1 | `855143060` | 5V Negative Wago 1 | Wago 221-413 |
| 1 | `855151510` | 5V Negative Wago 2 | Wago 221-413 |
| 1 | `62690` | Left Wheel Motor | Stepper Motor - Bipolar |
| 1 | `854115500` | Right Wheel Motor | Stepper Motor - Bipolar |
| 1 | `855143230` | 5V Positive Wago 1 | Wago 221-413 |
| 1 | `855151480` | 5V Positive Wago 2 | Wago 221-413 |
| 1 | `855157800` | C5 | Electrolytic Capacitor |
| 1 | `855139800` | Frontish Brush Motor | DC Mini Metal Gear Motor |
| 1 | `855157770` | C4 | Electrolytic Capacitor |
| 1 | `855139830` | Backish brush Motor | DC Mini Metal Gear Motor |
| 1 | `855148500` | San Ace 40 Axial Fan | DC Motor |
| 1 | `62460` | OrangePi 5(Raspberry Pi image as substitute) | Raspberry Pi 4B |

**BOM quantity rule:** each unique Fritzing `<part id>` is counted once. Repeated appearances in multiple nets are pin references to the same part, not additional BOM items.

## Complete Pin-to-Pin Netlist

Each `NET n` below is one Fritzing `<net>` element. Endpoints are written as `Part Label : Connector Name`.

### Connected nets (2+ endpoints)

### NET 1

`12V Negative Wago 1 : Pin 2` - `12V -> 5V DC-DC Buck Converter : Pin 2` - `12V Negative Wago 1 : Pin 4` - `12V Negative Wago 1 : Pin 3` - `12V Negative Wago 1 : Pin 1` - `12V Negative Wago 1 : Pin 5` - `12V Negative Wago 2 : Pin 5` - `5000 Mah 11.1V 30C 3s Lipo : negative` - `12V Negative Wago 2 : Pin 2` - `12V Negative Wago 2 : Pin 4` - `12V Negative Wago 2 : Pin 3` - `12V Negative Wago 2 : Pin 1` - `Right Motor Driver : GND` - `Left Motor Driver : GND` - `L298N1( Brush Motors Driver) : GND` - `C3 : -` - `C2 : -` - `12V Positive Wago 1 : Pin 3` - `12V Positive Wago 1 : Pin 2` - `12V Positive Wago 1 : Pin 4` - `12V Positive Wago 1 : Pin 1` - `12V Positive Wago 1 : Pin 5` - `San Ace 40 Motor Driver : Pin 11` - `12V Positive Wago 2 : Pin 1` - `12V Positive Wago 2 : Pin 2` - `12V Positive Wago 2 : Pin 4` - `12V Positive Wago 2 : Pin 3` - `12V Positive Wago 2 : Pin 5` - `12V -> 5V DC-DC Buck Converter : Pin 1` - `Right Motor Driver : VMOT` - `12AWG 7.5AMP Fuse : 2` - `C3 : +` - `L298N1( Brush Motors Driver) : 12V` - `San Ace 40 Motor Driver : Pin 12`

### NET 2

`C2 : +` - `Left Motor Driver : VMOT`

### NET 3

`Right Motor Driver : DIR` - `Arduino mega : D5 PWM`

### NET 4

`Left Motor Driver : DIR` - `Arduino mega : D3 PWM`

### NET 5

`Arduino mega : D4 PWM` - `Right Motor Driver : STEP`

### NET 6

`Left Motor Driver : STEP` - `Arduino mega : D2 PWM`

### NET 7

`Right Motor Driver : RESET` - `Right Motor Driver : SLEEP`

### NET 8

`Left Motor Driver : RESET` - `Left Motor Driver : SLEEP`

### NET 9

`Arduino mega : GND` - `Arduino mega : GND` - `Arduino mega : GND` - `Arduino mega : GND` - `Arduino mega : GND` - `5V Negative Wago 1 : Pin 1` - `Right Motor Driver : GND` - `5V Negative Wago 2 : Pin 1` - `5V Negative Wago 1 : Pin 2` - `5V Negative Wago 1 : Pin 3` - `5V Negative Wago 2 : Pin 2` - `5V Negative Wago 2 : Pin 3` - `Left Motor Driver : GND` - `12V -> 5V DC-DC Buck Converter : Pin 4` - `San Ace 40 Motor Driver : Pin 1` - `San Ace 40 Motor Driver : Pin 3`

### NET 10

`Left Wheel Motor : C` - `Left Motor Driver : 1B`

### NET 11

`Left Wheel Motor : D` - `Left Motor Driver : 2B`

### NET 12

`Left Wheel Motor : B` - `Left Motor Driver : 2A`

### NET 13

`Left Wheel Motor : A` - `Left Motor Driver : 1A`

### NET 14

`Right Wheel Motor : B` - `Right Motor Driver : 2A`

### NET 15

`Right Wheel Motor : D` - `Right Motor Driver : 2B`

### NET 16

`Right Wheel Motor : C` - `Right Motor Driver : 1B`

### NET 17

`Right Wheel Motor : A` - `Right Motor Driver : 1A`

### NET 18

`Arduino mega : VIN` - `5V Positive Wago 1 : Pin 3` - `5V Positive Wago 1 : Pin 2` - `5V Positive Wago 1 : Pin 1` - `12V -> 5V DC-DC Buck Converter : Pin 3` - `L298N1( Brush Motors Driver) : 5V`

### NET 19

`Arduino mega : 5V` - `Arduino mega : 5V` - `Arduino mega : 5V` - `Right Motor Driver : VDD` - `5V Positive Wago 2 : Pin 1` - `5V Positive Wago 2 : Pin 2` - `5V Positive Wago 2 : Pin 3` - `Left Motor Driver : VDD` - `San Ace 40 Motor Driver : Pin 7` - `San Ace 40 Motor Driver : Pin 5`

### NET 20

`C5 : +` - `Frontish Brush Motor : IN1` - `L298N1( Brush Motors Driver) : OUT4`

### NET 21

`C5 : -` - `Frontish Brush Motor : IN2` - `L298N1( Brush Motors Driver) : OUT3`

### NET 22

`C4 : +` - `Backish brush Motor : IN1` - `L298N1( Brush Motors Driver) : OUT1`

### NET 23

`C4 : -` - `Backish brush Motor : IN2` - `L298N1( Brush Motors Driver) : OUT2`

### NET 24

`Arduino mega : D9 PWM` - `San Ace 40 Motor Driver : Pin 4`

### NET 25

`Arduino mega : D8 PWM` - `San Ace 40 Motor Driver : Pin 8`

### NET 26

`San Ace 40 Axial Fan : pin 1` - `San Ace 40 Motor Driver : Pin 9`

### NET 27

`San Ace 40 Axial Fan : pin 2` - `San Ace 40 Motor Driver : Pin 10`

### NET 28

`Arduino mega : D46` - `L298N1( Brush Motors Driver) : IN3`

### NET 29

`Arduino mega : D48` - `L298N1( Brush Motors Driver) : IN4`

### NET 30

`Arduino mega : D50` - `L298N1( Brush Motors Driver) : IN2`

### NET 31

`Arduino mega : D52` - `L298N1( Brush Motors Driver) : IN1`

### NET 32

`Arduino mega : D12 PWM` - `L298N1( Brush Motors Driver) : ENB`

### NET 33

`Arduino mega : D13 PWM` - `L298N1( Brush Motors Driver) : ENA`

### NET 34

`5000 Mah 11.1V 30C 3s Lipo : positive` - `12AWG 7.5AMP Fuse : 1`

### NET 44

`OrangePi 5(Raspberry Pi image as substitute) : GND` - `OrangePi 5(Raspberry Pi image as substitute) : GND` - `OrangePi 5(Raspberry Pi image as substitute) : GND` - `OrangePi 5(Raspberry Pi image as substitute) : GND` - `OrangePi 5(Raspberry Pi image as substitute) : GND` - `OrangePi 5(Raspberry Pi image as substitute) : GND` - `OrangePi 5(Raspberry Pi image as substitute) : GND` - `OrangePi 5(Raspberry Pi image as substitute) : GND` - `OrangePi 5(Raspberry Pi image as substitute) : GND`

### NET 56

`OrangePi 5(Raspberry Pi image as substitute) : 3V3` - `OrangePi 5(Raspberry Pi image as substitute) : 3V3`

### NET 69

`OrangePi 5(Raspberry Pi image as substitute) : 5V` - `OrangePi 5(Raspberry Pi image as substitute) : 5V`

### NET 107

`Arduino mega : D21/SCL` - `Arduino mega : SCL`

### NET 122

`Arduino mega : D20/SDA` - `Arduino mega : SDA`

### Singleton / unconnected nets

> These are present in the Fritzing XML as nets with only one endpoint. They are included for completeness but do not define a pin-to-pin connection.

- **NET 35:** `Left Motor Driver : ENABLE`
- **NET 36:** `Left Motor Driver : MS2`
- **NET 37:** `Left Motor Driver : MS3`
- **NET 38:** `Left Motor Driver : MS1`
- **NET 39:** `Right Motor Driver : ENABLE`
- **NET 40:** `Right Motor Driver : MS2`
- **NET 41:** `Right Motor Driver : MS3`
- **NET 42:** `Right Motor Driver : MS1`
- **NET 43:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO18`
- **NET 45:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO16`
- **NET 46:** `OrangePi 5(Raspberry Pi image as substitute) : RUN`
- **NET 47:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO3`
- **NET 48:** `OrangePi 5(Raspberry Pi image as substitute) : ID_SD`
- **NET 49:** `OrangePi 5(Raspberry Pi image as substitute) : TR03_TAP`
- **NET 50:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO6`
- **NET 51:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO12`
- **NET 52:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO23`
- **NET 53:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO26`
- **NET 54:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO8`
- **NET 55:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO9`
- **NET 57:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO25`
- **NET 58:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO7`
- **NET 59:** `OrangePi 5(Raspberry Pi image as substitute) : ID_SC`
- **NET 60:** `OrangePi 5(Raspberry Pi image as substitute) : GLOBAL_EN`
- **NET 61:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO2`
- **NET 62:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO11`
- **NET 63:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO21`
- **NET 64:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO10`
- **NET 65:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO15`
- **NET 66:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO14`
- **NET 67:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO24`
- **NET 68:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO13`
- **NET 70:** `OrangePi 5(Raspberry Pi image as substitute) : TR02_TAP`
- **NET 71:** `OrangePi 5(Raspberry Pi image as substitute) : TR00_TAP`
- **NET 72:** `OrangePi 5(Raspberry Pi image as substitute) : TR01_TAP`
- **NET 73:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO22`
- **NET 74:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO4`
- **NET 75:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO5`
- **NET 76:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO20`
- **NET 77:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO19`
- **NET 78:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO17`
- **NET 79:** `OrangePi 5(Raspberry Pi image as substitute) : GPIO27`
- **NET 80:** `San Ace 40 Motor Driver : Pin 6`
- **NET 81:** `San Ace 40 Motor Driver : Pin 2`
- **NET 82:** `L298N1( Brush Motors Driver) : 5VEN`
- **NET 83:** `L298N1( Brush Motors Driver) : 5VEN`
- **NET 84:** `L298N1( Brush Motors Driver) : 5V`
- **NET 85:** `L298N1( Brush Motors Driver) : 5V`
- **NET 86:** `Arduino mega : A2`
- **NET 87:** `Arduino mega : A13`
- **NET 88:** `Arduino mega : D11 PWM`
- **NET 89:** `Arduino mega : A5`
- **NET 90:** `Arduino mega : A12`
- **NET 91:** `Arduino mega : D0 RX0`
- **NET 92:** `Arduino mega : D22`
- **NET 93:** `Arduino mega : A7`
- **NET 94:** `Arduino mega : D28`
- **NET 95:** `Arduino mega : D6 PWM`
- **NET 96:** `Arduino mega : D18/TX1`
- **NET 97:** `Arduino mega : D47`
- **NET 98:** `Arduino mega : D23`
- **NET 99:** `Arduino mega : D7 PWM`
- **NET 100:** `Arduino mega : D1 TX0`
- **NET 101:** `Arduino mega : D38`
- **NET 102:** `Arduino mega : D51`
- **NET 103:** `Arduino mega : D42`
- **NET 104:** `Arduino mega : A0`
- **NET 105:** `Arduino mega : D33`
- **NET 106:** `Arduino mega : 3V3`
- **NET 108:** `Arduino mega : A11`
- **NET 109:** `Arduino mega : D32`
- **NET 110:** `Arduino mega : A6`
- **NET 111:** `Arduino mega : A14`
- **NET 112:** `Arduino mega : D43`
- **NET 113:** `Arduino mega : D14/TX3`
- **NET 114:** `Arduino mega : D49`
- **NET 115:** `Arduino mega : IOREF`
- **NET 116:** `Arduino mega : A9`
- **NET 117:** `Arduino mega : D17 PWM/RX2`
- **NET 118:** `Arduino mega : A3`
- **NET 119:** `Arduino mega : D15/RX3`
- **NET 120:** `Arduino mega : D24`
- **NET 121:** `Arduino mega : D40`
- **NET 123:** `Arduino mega : D29`
- **NET 124:** `Arduino mega : D45`
- **NET 125:** `Arduino mega : D30`
- **NET 126:** `Arduino mega : D36`
- **NET 127:** `Arduino mega : D39`
- **NET 128:** `Arduino mega : A8`
- **NET 129:** `Arduino mega : D53`
- **NET 130:** `Arduino mega : D35`
- **NET 131:** `Arduino mega : D19/RX1`
- **NET 132:** `Arduino mega : D31`
- **NET 133:** `Arduino mega : D27`
- **NET 134:** `Arduino mega : D25`
- **NET 135:** `Arduino mega : A10`
- **NET 136:** `Arduino mega : IOREF`
- **NET 137:** `Arduino mega : D10 PWM`
- **NET 138:** `Arduino mega : D44`
- **NET 139:** `Arduino mega : D26`
- **NET 140:** `Arduino mega : D41`
- **NET 141:** `Arduino mega : A1`
- **NET 142:** `Arduino mega : A15`
- **NET 143:** `Arduino mega : D37`
- **NET 144:** `Arduino mega : AREF`
- **NET 145:** `Arduino mega : D16 PWM/TX2`
- **NET 146:** `Arduino mega : RESET`
- **NET 147:** `Arduino mega : D34`
- **NET 148:** `Arduino mega : A4`

## Netlist Summary

- Total XML nets: **148**
- Connected nets (2+ endpoints): **39**
- Singleton/unconnected nets: **109**
- Unique BOM parts: **26**

## Important Source-Fidelity Note

The extraction intentionally preserves the XML exactly, including nets that appear electrically unusual. For example, **NET 1** places multiple 12 V negative/positive Wago terminals, the LiPo negative, the LiPo fuse-side supply path, both A4988 VMOT/GND references, the L298N 12V/GND references, capacitors, the buck converter input pins, and the San Ace driver supply pins on the same Fritzing net. This is reported as encoded; it has not been interpreted or 'fixed'.

Likewise, the many Arduino Mega and OrangePi pins that appear as singleton nets are retained rather than silently omitted.
