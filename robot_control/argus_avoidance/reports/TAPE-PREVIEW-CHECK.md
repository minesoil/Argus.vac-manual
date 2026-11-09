# Camera line following checks

## Current speed profile: 25% cruise, 35% automatic cap

User confirms the camera is mounted on Argus. The watched left-only physical
pulse moves only the left wheel forward and stops. The first tethered floor
trial runs for one second with clear centered tape (-0.02 to -0.04, confidence
1.0), but user reports barely moving and says100% manual speed is also slow.

The initial6% cruise/10% cap is replaced by25% cruise with corrections up to
10 points and a35% firmware cap. Paired client and firmware are deployed. All83
Pi tests and actual-sketch HTTP/USB/GPIO tests pass, including accepting35 and
rejecting36. Application hash verification passes. A real GPIO zero-speed
handshake reports cap35, lease350 and ends stopped with zero outputs. This
profile's ground run is pending; percentages are not measured ground speed.

## Later November 8: GPIO and raised-wheel movement

Corrected GPIO wiring is Pi physical8 TX→ESP25 RX, Pi10 RX←ESP26 TX,
Pi6 GND↔ESP GND. The ESP32 plain RX/TX labels are not the configured GPIO link.
All 50 read-only GPIO requests pass. A real zero-speed automatic session sends
570 heartbeats and ends on the phone's Operator Stop; old session gets409 and
outputs are zero. User confirms the displayed mode transition.

With motor power on and wheels raised, a one-second 5% both-wheel pulse sends
ten accepted messages. User observes both wheels turn forward and stop.
After camera re-aiming, a two-second camera-guided session follows a tape
slightly left (-0.20, confidence0.95–0.96) and finishes normally. User observes
both wheels move and stop, but cannot compare speeds. A three-second left-only
5% pulse has completed; physical channel identification is awaiting observation.
No floor-course following is established. These results supersede the earlier
pending-physical-movement checkpoints below.

## November 8: live tape and USB integration

The lit physical tape produced 15 consistent LEFT readings, approximately
-0.11 normalized error and 0.94 confidence. The floor region was adjusted to
the bottom 28% of this camera view. A later exposure/background change joined
the tape to the distant rug and correctly caused STOP. Restricting the region
to the bottom 24% separates that rug; both saved live frames then report LEFT
at about -0.11 with confidence 1.0. This establishes stationary detection.
The final live two-second preview accepted ten fresh frames with the same LEFT
reading, confidence 1.0 and no failed readings. All 20 camera tests also passed
on the Pi after this final crop adjustment.

The updated ESP32 firmware is uploaded with flash hash verification. It uses
the existing Mega `M:left,right` UART path and boots stopped. The Pi's existing
USB cable carries automatic sessions and small JPEGs, with one bridge process
owning the port. The phone stays on the ESP32 hotspot.

The initial 460800-baud control link failed 24 of 50 state reads. Both ends now
use 115200 baud. Fifty subsequent reads passed, including concurrent JPEG relay;
maximum reply time was 0.061 seconds. The phone preview uses at most 1200 bytes
once per second. The new systemd drop-in starts the USB owner without arming.

A real automatic session ran for 60 seconds through that bridge using only
zero wheel commands. It completed without a control error and returned to
stopped mode with zero outputs. No phone Stop event was observed in that run.
A separate zero-speed session stopped after command expiry when no heartbeat
arrived for 0.5 seconds; the firmware reported both outputs zero.
All 83 Python tests pass on the Pi after the final transport changes. The
actual-sketch host checks pass for USB and HTTP ownership, stops and expiry.
The final ESP32 build uses 934,892 program bytes and 95,280 global bytes.

**Pending physical checks:** raised-wheel direction and steering, and a short
clear floor run. Motor battery power was
confirmed off for uploads; no physical automatic movement is established.
The longer-running bridge later logged USB input/output failures and complete
device disconnects (seven service restarts observed). Its recovery starts the
ESP32 stopped. The successful short link checks above do not establish sustained
reliability. Resolve this connection before physical driving; cable reseating
has been requested with wheels raised and motor power off.
Reseating and another Pi socket did not resolve the drops. With phone video
paused (`usb_bridge --no-phone-preview`), a subsequent real zero-speed session
accepted 314 heartbeats and ended on the phone's Operator Stop. Firmware then
rejected the old session with 409 and reported zero outputs. The Pi continues
reading the full-resolution camera. This is the current control profile.

## November 7: preparation

The Orange Pi ran all **74 Python tests successfully** with its existing OpenCV
and NumPy. These include 20 camera/freshness tests, ten future-control-client
tests and the earlier 44 controller/ROS-adapter/simulation tests.

A three-second run of `./argus follow --seconds 3` used 15 fresh camera frames
and printed STOP throughout the untaped floor view. It reported zero failed
readings. A deliberate unavailable snapshot endpoint produced STOP and a
failure exit status. A real tape course is pending because Justin cannot place
the tape at this stage.

The preview checks the camera's online flag, advancing grab timestamps and
capture age using the same Linux RAW clock as uStreamer 4.9. It rechecks age
after processing. Missing, repeated or expired frames invalidate the reading.
[uStreamer clock source](https://github.com/pikvm/ustreamer/blob/v4.9/src/libs/tools.h).

The future `follow --drive` path was tested against a local HTTP test server.
Tests exercised explicit arming, command sequences, tape loss, camera loss,
manual takeover, bounded wheel requests and session cleanup. Default
`./argus follow` uses preview. No automatic request was sent to an actual ESP32.

The prepared ESP32 draft accepts explicitly selected manual or automatic
sessions. Operator Stop latches stopped mode and invalidates the old session.
Automatic cleanup only stops its own session, so it preserves a newer manual
owner. Requests expire after 350 ms. The first Pi wheel requests use a base of
6 percent, differential corrections of up to 4 percent and no reverse. This
is an uncalibrated step-rate setting. Physical tape, direction, timing, loaded
stopping and manual override remain to be tested.
