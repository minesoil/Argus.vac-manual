# Check software now; commission the robot later

## At school: no robot required

In a terminal with Python 3.10+ and camera dependencies installed, change to
`code/robot_control/argus_avoidance`. On Justin's Windows laptop, plain
`python` currently points to a Windows Store alias; use the verified launcher
`py -3.12` instead:

```powershell
py -3.12 -m unittest discover -s tests -v
py -3.12 -m argus_avoidance.simulate --output "$env:TEMP/argus-simulation.json"
```

On Linux with a working interpreter:

```bash
python3 -m unittest discover -s tests -v
python3 -m argus_avoidance.simulate --output /tmp/argus-simulation.json
```

On Windows, use an output such as `"$env:TEMP/argus-simulation.json"` instead
of `/tmp/...`. The package is run from its folder, so it is importable without
an installation. OpenCV/NumPy tests may be skipped if those dependencies are
missing: inspect the summary before saying all camera checks passed.

These tests model sensors and controllers. They open no motor port and do
not prove physical stopping. The standalone simulation is deliberately small;
there is no Gazebo download or old WSL disk to restore.

For ESP32 host checks, run from `code/robot_control/firmware/esp32_wifi_controlcam_auto`:

```bash
g++ -std=c++17 -Wall -Wextra -Werror -Itests/stubs tests/host_check.cpp -o /tmp/argus-host-check
/tmp/argus-host-check
g++ -std=c++17 -Wall -Wextra -Werror tests/phone_start_check.cpp -o /tmp/argus-phone-start-check
/tmp/argus-phone-start-check
node tests/browser_check.js
```

On Windows choose output paths ending in `.exe`, for example
`$env:TEMP/argus-host-check.exe`, then invoke with PowerShell's `&` operator.
This uses a host compiler, not the ESP32 board compiler. The target firmware
build is described in [04_FIRMWARE.md](04_FIRMWARE.md).

## Recorded physical checks

| Test | Recorded result |
|---|---|
| GPIO state and zero-speed sessions | Passed |
| Phone Stop during zero-speed automatic session | Passed |
| Both raised wheels forward then stopped | Passed |
| Left-only command matches physical left | Passed |
| Short tethered tape course | Forward along tape then stopped |
| Sharp joined 45° tape turn | Improved, still incomplete |
| Phone lock during tape session | Returned STOPPED |
| New assisted button on blocked scene, motors OFF | Refused movement, STOPPED/warning |
| Paper covering watched region | Preview became clear |
| Held joystick plus actual object entering region | No result received; pending |
| Camera unplug/freeze during assisted commands | Software tests only; real check pending |
| Loaded obstacle stopping distance | Not measured |
| Fully untethered floor course | Not confirmed |

## Next time at the robot

Start by looking at its actual condition, not this dated power note. Press
STOP, switch motor power OFF, restore the setup connection and inspect the
preview. Do not remove or alter the caster/camera assembly to match a drawing.

1. With motor power OFF, calibrate on a genuinely clear floor patch and check
   that an object entering the watched region becomes blocked. Tape and paper
   are staged test surfaces, not proof about every household floor.
2. Still with motor power OFF, enable assisted mode and hold a small forward
   joystick command. Introduce a soft dark object in the watched region.
   Verify warning, STOPPED and both outputs zero while still holding.
3. Remove the object. Verify that driving does not resume by itself; explicitly
   re-enable only after clear status. Repeat with camera unavailable and guard
   service unavailable, recording the observed stop.
4. Return ESP USB power to the secured bank if appropriate, with boards powered
   down while moving connections. Recheck GPIO and startup. Reboot with motors
   OFF and verify no automatic drive selection.
5. After the software-state checks pass, use raised wheels for motion checks,
   then a short supervised level-floor trial against a soft object. Keep phone
   STOP ready and test at low speed. Record misses and distance, not just success.

These are future commissioning steps. No commands in this documentation task
performed them. Stop a failing stage and investigate before progressing.

## One test log entry

```text
Date/time:
Code commit + board firmware/config versions:
Power source and Ethernet connected? Wheels raised or floor?
Floor/light/camera pose and test object:
Expected behavior:
What I actually observed (including warning and wheel/output state):
Frame age / latency / logs:
Pass, fail, or inconclusive:
Next change:
```
