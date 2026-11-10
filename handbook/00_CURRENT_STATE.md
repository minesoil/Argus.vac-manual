# Current state: dated evidence, not live telemetry

The latest robot evidence is from the 9 November work session. This document
was assembled on 10 November without access to Argus.

| Part | What the evidence supports |
|---|---|
| Orange Pi | Orange Pi 5, Ubuntu 22.04 Jammy, Orange Pi image 1.2.2, kernel 6.1.99-rockchip-rk3588. Mounted with its power bank. |
| ROS 2 | Humble was already installed when this setup work began. Optional isolated LiDAR preview was built and checked. |
| Camera | USB camera is mounted; its assembly also supports the caster. Changing its angle requires mechanical work. |
| LiDAR | RPLIDAR C1 is unavailable following a reported fault. Replacement adapter ordered; failed component unconfirmed. |
| Manual driving | Phone → ESP32 → Mega worked physically before camera assistance. |
| Pi control link | GPIO UART `/dev/ttyS0`; physical 8 → ESP25, physical 10 ← ESP26, physical 6 → ground. Read-only and zero-speed checks passed. |
| Tape following | Phone Start/Stop, phone-lock stop and raised-wheel forward/Stop passed. A short tethered 25% floor run followed tape. Sharp 45° turn improves but still stops early. |
| Untethered floor trial | Not confirmed. User corrected that Ethernet remained attached during the reported floor trials. |
| Camera-assisted manual prototype | Pi source and ESP32 firmware installed; upload hash verified. Real phone buttons visible. Blocked scene refuses assisted drive and shows a warning. |
| Software tests | 103 Python tests passed locally and on the Pi during the assisted-mode session; C++ sketch and browser checks also passed. These are software checks. |
| Real object stop | A held-joystick sock/shoe entry test was requested but no result was received. Loaded stopping and stopping distance are unverified. |

## Last assisted-mode observations

The detector first flagged tape/seams in the watched region. With white paper
covering the whole region, the live preview became clear: no boxes, frame age
about 126 ms and processing about 24 ms in that observation. This establishes
that the preview can change between blocked and clear in the staged scene.
It does not establish reliable detection of every obstacle.

The final application file was 941,568 bytes, SHA-256:

```text
fbc4e7bc6b32263d2866c546ff624dbcaebe4598dac0179ac8768f2fbec5ddba
```

The ESP32 write at application offset `0x10000` completed with esptool's
data-hash verification. That historical binary embeds private Wi-Fi settings
and is not included. A new build with different credentials will have a
different hash.

Last explicit power confirmation for this assisted-mode work: motor power OFF,
Pi/ESP32 USB power ON. The ESP32 was temporarily USB-powered by the Pi for
flashing. Earlier bank-powered GPIO operation passed, but returning to the
bank after this newest upload has not been confirmed. Today's power state is
unknown.

## What the prototype means

It compares a calibrated patch of floor with the visible region ahead. A
different appearance can trigger a stop. It does not classify shoes, measure
distance, detect stairs, cover the rear or prove a clear swept turning area.
Tape, seams, shadows and lighting changes can produce warnings; similar-looking
objects can be missed. Assisted mode is forward-only and capped at 35%.
Unassisted manual and tape following have no camera obstacle stop.

The next robot task is a motors-OFF held-joystick object test, followed by
camera-loss and explicit-rearm checks. Only then consider raised-wheel and
slow supervised floor tests. See [the test record](06_CHECKS_AND_FIRST_TESTS.md).

The exact flashed Mega source remains a separate recovery gap. Do not flash
the reference sketch merely to make this documentation look complete.
