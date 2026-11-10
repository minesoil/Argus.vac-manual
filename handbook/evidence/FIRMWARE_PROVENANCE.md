# Firmware provenance and connections

Audited on 2026-11-10 from saved files and dated project records. No robot was contacted during this audit. Source identity, a successful build, a verified upload and an observed wheel test are different kinds of evidence.

## What the files do

| File or group | Job | Dependencies |
| --- | --- | --- |
| Mega `Arduino_Mega_Manual_Control.ino` | Reads left/right percentages, ramps speed and generates motor-driver step pulses | Arduino Mega 2560; AccelStepper 1.64; recoverable build uses Arduino AVR core 1.8.8 |
| ESP32 `esp32_wifi_controlcam_auto.ino` | Serves the phone page, accepts selected control sessions and sends Mega commands | ESP32 Arduino core 3.3.11, its WiFi/WebServer libraries; board `esp32:esp32:nodemcu-32s` |
| `DriveControl.h` | Manual/automatic ownership, session numbers, command limits and 350 ms command expiry | Local C++ header |
| `ControlPacketParser.h` | Parses framed Pi serial requests | Local C++ header |
| `PhoneStart.h` | Phone request/claim handshake for the line follower | Local C++ header |
| `ManualGuard.h` | Opt-in camera guard, 800 ms report expiry and latched Stop | Local C++ header |
| Pi `serial_control.py` / `usb_bridge.py` | Owns one Pi-to-ESP serial connection and exposes local control/status | Python3, pyserial; OpenCV for optional phone frames |
| Pi `obstacles.py` / `manual_guard.py` | Compares the floor with a frozen calibration and forwards fresh clear/blocked/unavailable reports | Python3, OpenCV, NumPy; existing camera stream |

The current phone and camera-assistance path does not require ROS 2. The ROS package and lidar controller are separate preview/future-integration code. Their presence does not establish a working lidar or a ROS-controlled motor link.

## Recoverable Mega source

The handbook contains both the prepared baseline and the original Arduino sketchbook file under `code/mega-reference/`. They are reference copies, not an instruction to flash the Mega.

| Source label | SHA256 |
| --- | --- |
| Prepared baseline: `workspace/github/argus-vac-firmware/mega/Arduino_Mega_Manual_Control/Arduino_Mega_Manual_Control.ino` | `965F5D7AA05DFDD30E1572036F926F463B5C0E83A4690641009F9177C6B3EC3E` |
| Original Arduino sketchbook: `Arduino_Mega_Manual_Control/Arduino_Mega_Manual_Control.ino` | `F4340354BE985F3F0ACAECB970F1DB86ECF33FE20A84640354524BCB914881B3` |

The control logic matches. The prepared copy changes comments and fixes the startup banner: the original prints 3000 steps/s although its actual maximum constant is 3500. The recoverable Mega build metadata identifies `arduino:avr:mega`, AVR core 1.8.8 and the installed AccelStepper 1.64 library.

The November7 source review identifies this as the best editable baseline. It does **not** identify the exact binary currently flashed on the Mega. An older October upload log and recent working wheel observations do not establish byte-for-byte identity with this copy.

## Source pin assignments and protocol

These are source assignments with dated wiring evidence; they are not a fresh inspection of the robot.

| Connection | Assignment |
| --- | --- |
| Mega left motor STEP / DIR | D24 / D25 |
| Mega right motor STEP / DIR | D22 / D23 |
| ESP32 motor-command TX | GPIO17 → Mega D19/RX1; shared ground |
| ESP32 motor UART | Serial2, 9600 baud; RX is configured as GPIO16 |
| Pi control UART | `/dev/ttyS0`, 115200 baud |
| Pi transmit | Physical header 8/TX → ESP32 GPIO25/RX |
| Pi receive | Physical header 10/RX ← ESP32 GPIO26/TX |
| Pi signal ground | Physical header 6 → ESP32 GND |

The Pi GPIO wires carry 3.3 V serial signals. They do not supply board power. ESP32 USB power and GPIO serial data are separate connections.

The ESP32 sends `M:left,right` plus a newline to the Mega. Each value is a signed percentage from −100 to 100. The current ESP32 sends `\nS\n` for an immediate stop. The Mega also recognizes F/B/L/R/1/2/S/X, reads USB at 115200 and Serial1 at 9600, and stops pulses after 900 ms without a valid command. Its maximum 3500 steps/s and ramp 4500 steps/s² are configured pulse rates, not measured floor speed. Stopping pulses does not disconnect motor power.

The Pi-to-ESP protocol is a different framed protocol. `ControlPacketParser.h` and `serial_control.py` implement it; do not send the Mega ASCII protocol to this GPIO endpoint. A single bridge owns the serial port.

## Current ESP32 and Pi source identity

ESP32 hashes below refer to the current local `workspace/robot_control/firmware/esp32_wifi_controlcam_auto/` source, rather than the older standalone ESP32 sketch.

| File | SHA256 |
| --- | --- |
| `esp32_wifi_controlcam_auto.ino` | `71C88323C9439787644EBA524D361FFF53EE2C02A45D421B18F5BD34CB285E81` |
| `DriveControl.h` | `5FF277E23DBF5A1C8F22E64497865B6826DFBE6E20BDCBAD09F011B31EBA77DA` |
| `ControlPacketParser.h` | `F5EE30B43DA09CE27C67F86AB1B6F67772AB08A12F2117EF06352D56E0BDD056` |
| `PhoneStart.h` | `1DBA7F6FA93213921FEACC0AD30BCD696256F0FF3F7F525A49A83D19302E071E` |
| `ManualGuard.h` | `6D463925D3EA5B602BAAF2D79EC0B7F3FFC497BBC122E7F30B393196A43630A5` |
| `config.h.example` | `61C28F1B8FBCBBC6A8C1669445978B2C35217E781A9C69BA4337B36169A9BAAD` |

Pi hashes refer to `workspace/robot_control/argus_avoidance/argus_avoidance/`.

| File | SHA256 |
| --- | --- |
| `obstacles.py` | `DEE4187E10D4A534CF084CB2F466962C6D3D5ECE4FB3A614C5B2596BCF23B282` |
| `manual_guard.py` | `C118926CFD7276EDA1E613344688714145715E924AECFC18910650677EB144B7` |
| `serial_control.py` | `16A3385F01A9C2B5F76E1E4D900F1C54B40812CE1C5F37D6CCA00AE8CDF2A154` |
| `usb_bridge.py` | `114DB68A64BCEC4B5C7B559EBC39C61CBE7684878652D7DC59E14C18FD5C7AAD` |

The saved final 941568-byte ESP32 application has SHA256 `FBC4E7BC6B32263D2866C546FF624DBCAEBE4598DAC0179AC8768F2FBEC5DDBA`, matching the November 9 recorded verified upload. The binary contains private compile-time Wi-Fi settings and is excluded from this handbook.

## Offline firmware checks

These are reproducible commands assembled from the current test source. They are not a claim that this exact command spelling was preserved from the earlier terminal history. Run them in the **sanitized ESP32 source folder** with `tests/` present and no real root-level `config.h`.

PowerShell; requires `g++` and `node` on PATH. The audit found g++ 10.3.0 at `C:/TDM-GCC-64/bin/g++.exe` and Node v24.22.1. The command block passed PowerShell's syntax parser with zero errors. Subsequent host, Phone Start and browser checks passed against the sanitized handbook snapshot; an ESP32 target compile with example settings also passed. Exact executed commands and results are in `OFFLINE_FIRMWARE_CHECKS.md`. These test programs use mock serial/Wi-Fi/HTTP implementations and do not open the robot's serial port or contact the robot.

```powershell
if (Test-Path './config.h') { throw 'Use the sanitized source copy for host tests.' }
$argusCheckDir = Join-Path $env:TEMP 'argus-offline-firmware-check'
New-Item -ItemType Directory -Force -Path $argusCheckDir | Out-Null

g++ -std=c++17 -I tests/stubs tests/host_check.cpp -o "$argusCheckDir/host-check.exe"
if ($LASTEXITCODE -ne 0) { throw 'Host check compilation failed.' }
& "$argusCheckDir/host-check.exe"
if ($LASTEXITCODE -ne 0) { throw 'Host check failed.' }

g++ -std=c++17 tests/phone_start_check.cpp -o "$argusCheckDir/phone-start-check.exe"
if ($LASTEXITCODE -ne 0) { throw 'Phone Start check compilation failed.' }
& "$argusCheckDir/phone-start-check.exe"
if ($LASTEXITCODE -ne 0) { throw 'Phone Start check failed.' }

node tests/browser_check.js
if ($LASTEXITCODE -ne 0) { throw 'Browser check failed.' }
```

Keep `tests/stubs/config.h`: it contains dummy test settings. Because the actual sketch uses a quoted `#include "config.h"`, a real root-level configuration would take precedence over the test include directory. Exclude the real file before building a public host-test copy.

## Verification limits and older incompatible firmware

The camera-assisted implementation has a 350 ms drive-command lease and an independent 800 ms guard-report lease. Assisted mode allows forward wheel commands up to 35%. A blocked/unavailable report stops and invalidates the session; a later clear report cannot resume it. Unassisted manual and tape following remain explicitly outside this camera guard.

Recorded November 9 evidence includes 103 Pi software tests, firmware upload/data-hash verification and the user's confirmation that the new assisted button stays stopped with a warning on the blocked scene. The real-camera held-joystick obstacle-entry test, raised-wheel assisted braking and loaded floor stopping remain unverified. A late paper-covered view reported clear, but that alone is not a braking test. The latest upload used ESP32 USB connected to the Pi; a later return to bank power was not confirmed.

The archived RobotLab `mega_drive.ino` is a **different firmware family**. It uses D22/D23 for left/right STEP, D24/D25 for left/right DIR, a 115200-baud `V1,sequence,enabled,left,right,CRC` protocol, and an NC stop loop on D27. Its physical deployment is unverified. Its source object SHA256 is `cacfb08d3800d1f1cc7cbc6759d227c1fe5a911301eebf1ce1353cdaef0d660b` (catalog source ID `7d05537bdc3a1f67d603`). It cannot be substituted for the M-command Mega reference with the current ESP32 source and pin assumptions. Older A4988/letter-threat firmware is another historical family.

Real configurations, credentials, compiled firmware, ELF/MAP/build artifacts and private calibration `.state/` data are excluded. Historical documentation is preserved as dated evidence; older draft verification statements do not describe the current source.
