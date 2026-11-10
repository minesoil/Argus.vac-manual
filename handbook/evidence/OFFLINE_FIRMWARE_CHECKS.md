# Offline firmware checks — 2026-11-10

The three host/browser checks and the ESP32 target compile below passed against the sanitized handbook snapshot. No hardware was contacted, serial port opened or firmware uploaded. Compilation outputs were written outside the handbook, under `.tmp/handbook-checks/`.

Before testing, the root firmware `config.h` was confirmed absent. The retained `tests/stubs/config.h` contains only test placeholders. The tested sketch SHA256 was `71C88323C9439787644EBA524D361FFF53EE2C02A45D421B18F5BD34CB285E81`, matching the audited source.

Tools: g++ 10.3.0 (TDM-GCC), Node v24.22.1, Windows PowerShell-compatible commands. Run these exact commands from the project workspace root containing `workspace/argus-handbook/`:

```powershell
if (Test-Path 'workspace/argus-handbook/code/robot_control/firmware/esp32_wifi_controlcam_auto/config.h') { throw 'Snapshot has a root config.h; refusing host build.' }
New-Item -ItemType Directory -Force -Path '.tmp/handbook-checks' | Out-Null

g++ -std=c++17 -I 'workspace/argus-handbook/code/robot_control/firmware/esp32_wifi_controlcam_auto/tests/stubs' 'workspace/argus-handbook/code/robot_control/firmware/esp32_wifi_controlcam_auto/tests/host_check.cpp' -o '.tmp/handbook-checks/host-check.exe'
if ($LASTEXITCODE -ne 0) { throw 'Host check compilation failed.' }
& '.tmp/handbook-checks/host-check.exe'
if ($LASTEXITCODE -ne 0) { throw 'Host check failed.' }

g++ -std=c++17 'workspace/argus-handbook/code/robot_control/firmware/esp32_wifi_controlcam_auto/tests/phone_start_check.cpp' -o '.tmp/handbook-checks/phone-start-check.exe'
if ($LASTEXITCODE -ne 0) { throw 'Phone Start check compilation failed.' }
& '.tmp/handbook-checks/phone-start-check.exe'
if ($LASTEXITCODE -ne 0) { throw 'Phone Start check failed.' }

node 'workspace/argus-handbook/code/robot_control/firmware/esp32_wifi_controlcam_auto/tests/browser_check.js'
if ($LASTEXITCODE -ne 0) { throw 'Browser check failed.' }
```

| Check | Compilation | Execution | Result |
| --- | --- | --- | --- |
| Actual-sketch HTTP/serial/control checks | Exit 0 | Exit 0 | Seven PASS lines below |
| Phone Start state-machine checks | Exit 0 | Exit 0 | Assertions passed; no stdout |
| Embedded browser script | Not required | Exit 0 | PASS line below |

Actual-sketch output:

```text
PASS actual HTTP routes: ownership, stop races, expiry, bounds, malformed input, rollover, camera relay
PASS USB packets: framing, HTTP/USB ownership, stop, expiry, malformed input
PASS GPIO UART: framing, reply routing, phone Stop, manual takeover, expiry and malformed-packet recovery
PASS phone start: one-shot, stop-before-arm, heartbeat watchdog, and operator Stop
PASS assisted manual: stale guard, hazard latch, joystick rejection, deliberate re-arm, forward limits and fallback
PASS guard heartbeat: sustained control, replacement invalidation and clock rollover
PASS assisted selection: unavailable camera stops old unassisted drive; stale selection preserves newer owner
```

Browser output:

```text
PASS embedded UI: stale poll, manual arm/takeover, idle auto, in-flight drive/independent stop
```

The tests compile the actual ESP32 sketch with host stand-ins for Wi-Fi, HTTP, clocks and UART. The browser check runs the actual embedded JavaScript with a mock DOM and mock HTTP. These results verify software behavior under those test conditions; they do not verify an ESP32 target build, real radio/UART timing, camera detection accuracy or physical stopping.

## ESP32 target compile

A new staging sketch was copied from the sanitized snapshot. Only this staging copy received a root `config.h`, copied from `config.h.example`. Its SHA256 was `61C28F1B8FBCBBC6A8C1669445978B2C35217E781A9C69BA4337B36169A9BAAD`, matching the public example. The public source copy still had no root `config.h` after compilation.

Arduino CLI 1.5.1 used the already installed ESP32 Arduino core 3.3.11. No platform/library was installed. The FQBN was `esp32:esp32:nodemcu-32s`. Exact staging and compilation commands, from the project workspace root:

```powershell
$argusStageSource = 'workspace/argus-handbook/code/robot_control/firmware/esp32_wifi_controlcam_auto'
$argusStageTarget = '.tmp/handbook-checks/sketch/esp32_wifi_controlcam_auto'
if (Test-Path "$argusStageSource/config.h") { throw 'Public source contains root config.h.' }
if (Test-Path $argusStageTarget) { throw 'Expected a new staging folder.' }
New-Item -ItemType Directory -Force -Path '.tmp/handbook-checks/sketch' | Out-Null
Copy-Item -LiteralPath $argusStageSource -Destination $argusStageTarget -Recurse
Copy-Item -LiteralPath "$argusStageTarget/config.h.example" -Destination "$argusStageTarget/config.h"

& 'C:/Program Files/Arduino IDE/resources/app/lib/backend/resources/arduino-cli.exe' compile --fqbn esp32:esp32:nodemcu-32s --build-path '.tmp/handbook-checks/build' '.tmp/handbook-checks/sketch/esp32_wifi_controlcam_auto'
if ($LASTEXITCODE -ne 0) { throw 'ESP32 target compilation failed.' }
```

Compilation exited **0** with this output:

```text
Sketch uses 941432 bytes (71%) of program storage space. Maximum is 1310720 bytes.
Global variables use 95512 bytes (29%) of dynamic memory, leaving 232168 bytes for local variables. Maximum is 327680 bytes.
```

The generated application `.bin` was 941584 bytes, SHA256 `A68470B092071F61CD38DB2C33BE7BDD1D95B854720448503A52353810428C2B`. It is a new example-config build and differs from the recorded real-config application uploaded on November 9. It was **not flashed**, and is kept outside the handbook. A successful target compile does not validate real camera performance, communications timing or physical stopping.
