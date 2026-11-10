# ESP32 build and Mega source recovery

These are build instructions and historical deployment evidence. No board is
being flashed while Justin is at school. Keep motor power OFF for later
firmware work, even if USB power is needed for programming.

## Which code is which?

| Board | Included source | Confidence |
|---|---|---|
| ESP32 | `code/robot_control/firmware/esp32_wifi_controlcam_auto/` | Current reviewed assisted-manual source; Nov9 application upload verified. |
| Mega | `code/mega-reference/editable/Arduino_Mega_Manual_Control/` | Best editable recovered M-command baseline; exact running binary unknown. |
| Mega original | `code/mega-reference/original/Arduino_Mega_Manual_Control/` | Original recovered sketchbook source; comments/banner differ from baseline. |

Read [FIRMWARE_PROVENANCE.md](evidence/FIRMWARE_PROVENANCE.md) for source
hashes, pins and incompatible historical firmware families. The current
Pi/ESP32 work deliberately preserved the functioning Mega. Nothing here
establishes that it was reflashed with the supplied baseline.

## Build the ESP32 on the laptop

Recorded toolchain: Arduino CLI, FQBN `esp32:esp32:nodemcu-32s`, Espressif core
**3.3.11**. The sketch uses core WiFi/WebServer and the included local headers.
If configuring Arduino tools on another machine, use the official
[Espressif installation guide](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html)
and [Arduino CLI guide](https://docs.arduino.cc/arduino-cli/getting-started/),
then select the recorded core version rather than silently changing it.

In a **private working copy**, copy `config.h.example` to `config.h` and choose
your hotspot name/password. Do not place that real file back into this public
snapshot. This reconstructed PowerShell example assumes Arduino IDE's
bundled CLI exists at the recorded path; otherwise substitute your CLI path.
Run from the handbook folder:

```powershell
$argusCli = 'C:/Program Files/Arduino IDE/resources/app/lib/backend/resources/arduino-cli.exe'
$argusSketch = Join-Path $env:TEMP 'argus-private-build-source/esp32_wifi_controlcam_auto'
$argusBuild = Join-Path $env:TEMP 'argus-private-build-output'
if (Test-Path -LiteralPath $argusSketch) { throw 'Choose a new private source folder; do not overwrite existing config.' }
if (Test-Path -LiteralPath $argusBuild) { throw 'Choose a new private output folder; avoid stale firmware.' }
New-Item -ItemType Directory -Path $argusSketch | Out-Null
Copy-Item -Path 'code/robot_control/firmware/esp32_wifi_controlcam_auto/*' -Destination $argusSketch -Recurse -Force
Copy-Item -LiteralPath (Join-Path $argusSketch 'config.h.example') -Destination (Join-Path $argusSketch 'config.h')
notepad (Join-Path $argusSketch 'config.h')
```

Finish editing, save and close Notepad before running the next block in the
same terminal:

```powershell
& $argusCli compile --fqbn esp32:esp32:nodemcu-32s --jobs 2 --output-dir $argusBuild $argusSketch
if ($LASTEXITCODE -ne 0) { throw 'Compile failed; do not upload any leftover output.' }
```

Compilation does not upload. The existence checks protect earlier private
work and avoid mistaking a stale `.bin` for a successful new build.

The recorded final build used 941,416 program bytes and 95,512 global-data
bytes; its application file was 941,568 bytes. Those are the November9
build's results, not a requirement for all future builds. Credentials,
compiler and source changes can change the bytes and hash.

## Historical Pi upload path

The Pi's esptool 4.8.1 method is in [the exact command ledger](commands/RECORDED_PI_COMMANDS.md).
It temporarily connected ESP32 USB data to the Pi, stopped the shared bridge,
identified the ESP32 with `read_mac`, and updated the application at `0x10000`.
That update relied on an existing compatible bootloader and partition table.

For a future update, first confirm motor power OFF, preserve the functioning
firmware/build settings, identify the attached device and stop the serial
owner. Transfer your newly compiled application to a private Pi staging path
and compare its SHA-256 on both computers. Then adapt the ledger's flash
command to that file. Never choose a port merely because it says CH340.
For a blank board or changed partition layout, use the Arduino board
upload recipe and all its matching images; the single-offset historical
application command is insufficient.

After upload, restart the matching Pi bridge, read its state, refresh the
phone page and perform motors-OFF checks first. Returning USB power to the
bank is a separate powered-down wiring/power step; GPIO still carries data.

## Build the Mega reference without overwriting the robot

Recorded build environment for the recovered family: Arduino AVR core
**1.8.8**, `AccelStepper` **1.64**, FQBN `arduino:avr:mega`.
With those dependencies installed, a compile-only example from this handbook is:

```powershell
& $argusCli compile --fqbn arduino:avr:mega --output-dir (Join-Path $env:TEMP 'argus-mega-reference-build') code/mega-reference/editable/Arduino_Mega_Manual_Control
```

This checks whether that reference builds; it does not establish what is
installed. Do not upload it until the source, pins, direction signs, driver
settings and command family have been deliberately reconciled with the
working robot. Old CRC firmware has a different protocol **and different pin
roles**. The historical A4988 sketches form another separate family.
