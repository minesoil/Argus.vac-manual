# Current manual code review and camera tape preview

Justin confirms that forward driving, turning and stopping work reliably through
the standalone ESP32 and Arduino Mega. This is his direct operational report,
not a measurement of stopping distance or automatic control. He asks to consult
recent chats for current code and says to keep going. He selected black tape
on a light floor for a first camera course but cannot place it for a live test
at this stage.

## Retrieved recent evidence

- [Motor Driver Setup](https://chatgpt.com/c/6add9cb7-5628-83e8-a9d3-4a84394b8eae),
  October 25, supplies user logs for the Pi camera bridge, ESP32 CH340 and
  missing serial port. Its camera bridge uses AVF1 JPEG packets at 460800 baud.
- [ESP32 Upload Steps](https://chatgpt.com/c/6addd85e-f9a8-83ee-9e59-2e7bd487eb82),
  October 25, records the joystick/camera setup and a compile-stage discussion.
  Assistant summaries in that chat alone do not prove a completed upload.
- Codex chat **Prepare Arduino and ESP32 code for G**, October 28, contains
  Justin's explicit selection of **Joystick + camera**. It prepared
  `workspace/github/argus-vac-firmware` from October 25 source. Local comparison
  finds matching control logic, credential separation and a corrected startup
  banner. Existing compiled artifacts support a successful draft build.
  The read-thread source ID is 01a18280-a098-7ca2-aaca-29b27d3de665.

This is the best available editable baseline. The recovered message pages and
local files do not independently identify the binary flashed on each board.

## Camera and software results

The Pi was reachable again over Ethernet. Its camera was online and OpenCV 4.11.0
and NumPy 1.26.4 were already installed. The new black-tape preview and future
ESP32 control client were copied into `~/argus/avoidance`.

All **74 Python tests passed on the Pi**. They cover the existing controller,
camera image cases, frozen/offline snapshots and a local test HTTP control
server. A live three-second tape preview on the current floor view produced
STOP. Real tape and wheel behavior remain to be checked.

Use `./argus line-preview --tape black --seconds 20` for the stationary test.
`./argus follow` also defaults to preview. Explicit future `--drive` requests
require the prepared ESP32 automatic-session API. No such requests were sent
to actual robot hardware during this work.

Source freshness uses uStreamer capture metadata and Linux CLOCK_MONOTONIC_RAW,
matching [uStreamer 4.9](https://github.com/pikvm/ustreamer/blob/v4.9/src/libs/tools.h).
The Pi client limits its first automatic requests to 2–10 percent forward
wheel commands. These are step-rate percentages, not measured travel speeds.

The prepared ESP32 change lives separately under
`workspace/robot_control/firmware/esp32_wifi_controlcam_auto`. It introduces
explicit manual/automatic ownership, a 350 ms automatic command lease, scoped
automatic cleanup and a latched operator Stop. Firmware compilation and host
test results are recorded with that draft. The final source compiled for
NodeMCU-32S using ESP32 core 3.3.11, taking 933,052 bytes of program storage and
95,120 bytes of globals. Tests of its actual HTTP handlers and embedded browser
passed, including delayed commands, manual takeover and a Stop arriving during
an outstanding request. An ignored local configuration was prepared from the
original sketch's hotspot settings. A physical upload has not occurred.
