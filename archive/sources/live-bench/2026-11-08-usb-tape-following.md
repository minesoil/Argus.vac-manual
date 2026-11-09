# Camera tape-following integration — November 8, 2026

Justin requests automatic line following now. He confirms motor battery power
is off for upload, light and black tape are ready, and the refreshed ESP32
phone page displays ENABLE MANUAL and STOP. He chooses the ESP32's own hotspot.

## Verified during this session

- Ethernet/SSH to the existing Pi installation works. The ESP32 is connected
  to the Pi by CH340 USB. esptool identifies ESP32-D0WDQ5 revision 3 and 4 MB
  flash; this resolves the earlier unidentified-CH340 stage.
- A narrow BRLTTY udev override exempts the CH340 while preserving other
  device rules. The existing USB socket has `/dev/argus_esp32` as an alias.
- A private complete 4 MB firmware backup was read successfully at 115200 baud.
  It stays outside the knowledge archive because it may contain credentials.
- The new joystick/camera/automatic firmware uploaded successfully with flash
  hash verification. The Mega firmware and physical motor wiring were unchanged.
- The first 460800-baud USB check was unreliable (26 of 50 state reads passed).
  Firmware and Pi transport were changed together to 115200 baud and uploaded
  with flash hash verification. All 50 subsequent read-only state requests
  passed with phone JPEG relaying included; maximum reply time was 61 ms. The
  phone preview is reduced to 96 × 72, at most 1200 bytes and once per second,
  to leave bandwidth for control. This supersedes the first transport setting.
- The existing `argus-bridge.service` now runs the single USB owner through
  a systemd drop-in. Its original camera sender and original unit are preserved.
  Its loopback state endpoint was verified stopped, with both outputs zero.
- A real automatic session sent only zero wheel commands for 60 seconds through
  that loopback bridge and firmware, without a control error. It finished in
  stopped mode with both outputs zero. No operator Stop event was observed
  during that interval, so this is not a phone-Stop validation.
- The actual lit floor/tape view produced 15 fresh consistent LEFT readings,
  offset approximately -0.11 and confidence about 0.94. The usable floor region
  starts at 72% of image height for this mounted view. This is a stationary
  camera check, not physical steering validation.
- A later exposure/background change connected the distant rug to the tape
  and produced STOP. The final floor crop begins at 76% image height, excluding
  that background. Both saved live frames then report LEFT near -0.11 with
  confidence 1.0. This supersedes the initial 72% crop.
- A real zero-speed session with heartbeats withheld for 0.5 seconds reported
  stopped mode, command expiry and both outputs zero.
- A longer idle check later exposed repeated complete USB disconnects and
  bridge restarts, despite the successful short 115200-baud checks above.
  These remain a connection problem to resolve before wheel tests; the baud
  change alone did not establish sustained reliability. The phone preview
  drops correspond to these events. Justin confirms the wheels are raised,
  motor power off and phone page open. He is asked to reseat the USB cable.
- Reseating and moving to another Pi USB controller did not resolve the drops.
  Justin has no replacement cable available. The new socket's alias is scoped
  to `platform-fc840000.usb-usb-0:1:1.0`. The bridge is being tested with
  `--no-phone-preview`, retaining the full-resolution Pi camera and phone
  control page. A subsequent real zero-speed session accepted 314 heartbeats
  and ended on **Operator stop**; the old session received 409 and both wheel
  outputs were zero. This verifies the phone's Stop through actual firmware.
  Sustained USB reliability and physical steering are still being checked.
- All 83 Python checks passed on the Pi. Actual-sketch host checks passed for
  USB framing, HTTP/USB ownership, operator stop, expiry and malformed packets.

## Intended everyday controls

Pi USB → ESP32 → existing Mega UART. Phone Wi-Fi → ESP32 joystick/Stop.
`argus-bridge.service` is the single USB owner; it exposes the automatic API on
Pi loopback port 8766 and keeps the phone preview supplied. `./argus follow`
previews; `./argus follow --drive --seconds 3` explicitly requests a bounded
automatic session. Boot remains stopped. Automatic requests use 6% nominal
wheel rate, 2–10% differential outputs, 350 ms ownership leases and latched
operator Stop. These settings do not establish measured speed or stopping.

Physical automatic movement, wheel direction and loaded floor following
remain unverified at this checkpoint. Phone Stop passed as recorded above.
The C1 remains reported faulty pending adapter replacement. Tape following
does not establish obstacle detection or autonomous room navigation.

Supersedes the November 7 pending-upload and unavailable-tape status in
[the earlier preparation](2026-11-07-current-manual-code-and-tape-preview.md).
User confirmations and live commands in this Codex chat are the evidence.
No credentials or firmware dump are included here.

## Later GPIO UART preparation

USB failed again before either attempted physical pulse could arm; no nonzero
wheel command was sent. A stale serial-descriptor issue was also fixed by
adding read-only bridge health checks. Pausing video did not establish sustained
USB reliability. Justin declines a laptop relay and confirms three jumper
wires for a direct Pi-to-ESP32 connection. He confirms motor power off again,
USB power on and jumpers disconnected for the firmware update.

The separate ESP32 UART uses RX GPIO25 and TX GPIO26. Host checks of the actual
sketch pass for GPIO framing, reply routing, HTTP Stop, manual takeover, expiry,
malformed frames and parser recovery. The target build uses 935408 program
bytes and 95448 global bytes. Its 935552-byte application was uploaded at
115200 baud with flash-hash verification (SHA-256
cd6a27dbfa9f6121431433c3cabe02f5604a571029b64092b8f291859046b2f5).

`/boot/orangepiEnv.txt` was backed up and only `overlays=uart0-m2` added. After
reboot `/dev/ttyS0` exists; live FDT reports UART0 okay and pin mux ALT10.
This board's installed `gpio readall` and manufacturer wiringOP source identify
**Pi physical pin8 TX, pin10 RX, pin6 GND**. Connect Pi8 to ESP25, Pi10 to ESP26,
and Pi6 to ESP GND. These differ from some older manual tables; use the verified
board map. Firmware pin assignments do not prove physical jumper installation.

The bridge now targets `/dev/ttyS0` with phone video paused, and is enabled for
the next boot. Physical wiring, GPIO communication, renewed operator Stop and
actual wheel/floor behavior remain pending. The Mega firmware is unchanged.

## Critical pin-direction correction, later November 8

Justin supplied an online Orange Pi header diagram (not a photo of his actual
board). Its UART0 pad mapping matches the Rockchip-authored upstream Linux
pinctrl definitions: GPIO4_A3 is TX (physical8), GPIO4_A4 is RX (physical10).
The installed wiringOP display has reversed RX/TX names; the earlier assistant
instructions and saved guide were incorrect. Correct wiring is Pi8 TX to ESP25
RX, Pi10 RX from ESP26 TX, and Pi6 GND to ESP GND. Current summaries and wiring
guide were corrected; old immutable snapshots are historical and superseded.
Physical jumper installation has not been confirmed; keep power disconnected
while correcting/connecting the signal wires. Pi overlay and ESP firmware pin
assignments need no change. Evidence: user-attached online diagram and
https://github.com/torvalds/linux/blob/master/arch/arm64/boot/dts/rockchip/rk3588-base-pinctrl.dtsi
(uart0m2_xfer).

Later direct user confirmation: Justin says "alr done" in response to the
corrected three-wire instructions. This records reported jumper installation,
not electrical verification. Restore Pi/ESP32 power with motor power off and
wheels raised, then verify GPIO communication before any wheel request.

After power restoration, Ethernet/SSH returned. The first GPIO read-only check
timed out; the bridge had restarted 14 times without a reply and was stopped
for diagnosis. No automatic arm or nonzero wheel command was sent. Justin
clarifies that his header has two horizontal rows of 13 pins, with 2 top-left
and 25 bottom-right. The earlier assistant's column description did not match
that orientation. Inspect the top row: third pin is 6/GND, fourth is 8/TX to
ESP25, fifth is 10/RX from ESP26. Confirmation of actual wire positions is
pending; do not infer a wiring error or successful GPIO connection yet.

Justin then confirms two horizontal rows and all three Pi wires in top-row
columns 3, 4 and 5, consistent with physical6/8/10. ESP32-end GPIO labels are
being traced separately. A fresh read-only USB state query succeeds and reports
stopped, zero left/right outputs, 350 ms lease and 10% automatic cap. A Pi UART0
internal hardware loopback test returns all 13 transmitted test bytes exactly;
the original modem-control flags are restored afterward. This verifies the
local UART peripheral path, not the external wires or ESP32 GPIO UART receiver.
The serial bridge remains stopped for diagnosis; no wheel request was sent.

Latest wire trace: Justin explicitly says Pi8 reaches the ESP32 pin labelled
RX and Pi10 reaches its pin labelled TX. These do not match the configured
GPIO25 RX/GPIO26 TX link. Pi-side top-row columns 3/4/5 are confirmed in his
horizontal orientation. The Pi was shut down again over SSH for rewiring only
the two ESP32 ends: move the wire on RX to printed GPIO25, and the wire on TX
to printed GPIO26. Ground and Pi endpoints stay in place. Physical correction
and subsequent GPIO communication are pending; no nonzero wheel command sent.

Later corrected-wiring check: Justin reports replugging with updated wiring and
USB power on. Pi Ethernet/SSH returned. Bridge logs explicitly show serial ready
on `/dev/ttyS0`; the state API reports stopped and zero outputs. All 50 fresh
read-only requests through the GPIO bridge passed with both outputs zero.
Three early bridge restarts occurred during board startup; stability beyond
the successful check remains under observation. A zero-speed automatic session
is running for the phone Stop check through GPIO. No nonzero wheel command sent.

GPIO operator Stop is now verified: 570 zero-speed heartbeats completed without
a control error, then the phone's Stop produced a 409 rejection for the old
session. Final firmware state is stopped with both outputs zero and reason
Operator stop. Justin independently confirms seeing AUTO, pressing Stop and
seeing STOPPED. Bridge PID3147 and restart count3 are unchanged through this
check; the three restarts were during initial startup. A one-second 5% wheel
pulse is prepared, awaiting motor-power-on/wheels-raised confirmation. No
nonzero wheel command has been sent yet.

## Later raised-wheel physical checks

Justin confirms motor power ON, wheels raised and phone Stop ready. A real
one-second 5% both-wheel pulse sends ten accepted drive messages and finishes
stopped with both outputs zero. Justin observes both wheels briefly forward
and stopped. This is the first verified nonzero physical control in this work.

The initial raised-camera view contains the battery/cables/workbench and the
follower correctly reports STOP. After Justin aims it at the taped floor,
ten fresh preview frames report LEFT near -0.20 with confidence 0.95–0.96.
A real two-second `./argus follow --drive --seconds 2` completes normally with
fresh LEFT decisions and scoped cleanup. Justin observes both wheels move and
stop, but cannot compare their speeds. Physical steering-channel identity is
therefore still pending, rather than assumed from software output.

A one-second left-only 5% request completes and reports stopped, but Justin
misses observing it. He explicitly confirms watching before a second left-only
test: three-second countdown, three seconds at 5%, 29 accepted messages, then
stopped with both outputs zero. Observation of which wheel moved is pending.
Floor-course following has not been tested. All these movements are with the
wheels raised; camera line following is not obstacle avoidance.

Justin subsequently confirms the watched three-second pulse moved only the
physical left wheel forward and it stopped. Together with the earlier both-wheel
forward/stop observation, this resolves the commanded-left channel identity.
The next required fact is whether the camera is secured to Argus and moves with
it; mounted camera pose and a first short clear floor run remain pending.

## First floor trial and speed-profile update

Justin confirms the camera is mounted on Argus and aimed at floor tape. He
confirms a short tethered floor test is possible, cable slack, motor power ON,
watching and phone Stop ready. A fresh preview reports centered tape near -0.03
with confidence1.0. Following a three-second countdown, the real one-second
floor session completes normally with ten fresh FORWARD decisions near
-0.02 to -0.04. Justin reports it barely moved and says 100% speed is also slow.
This is a short physical ground trial, not validation of a complete course.

Prepare a paired profile of 25% nominal forward wheel rate, correction up to
10 points, 35% firmware cap. The 350 ms lease, phone Stop, session revocation,
camera freshness and manual override remain unchanged. Justin confirms motor
power OFF and USB power on for upload. New target build succeeds (935408 program
bytes, 95448 globals); actual-sketch HTTP, USB and GPIO host checks pass,
including accepting35 and rejecting36. All11 Pi-client tests pass locally.
Pi follow.py and tests are updated and bridge is paused pending firmware
upload. Target application SHA-256 is
fc7fcb1517c0f10bc9b9a99856fbe2bc62ac554ee90caf2632afc9ddcbdfec5f.

All83 tests pass on the Pi after the paired client update. New application
uploads successfully with flash hash verification. GPIO state reports stopped,
zero outputs, lease350 and cap35. A real arm/zero-drive/scoped-stop handshake
with the updated Pi client passes and finishes stopped. Motor power remains
off at this checkpoint; a two-second25% ground test awaits user readiness.
