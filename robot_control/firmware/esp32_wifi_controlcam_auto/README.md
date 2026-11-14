# ESP32 manual and automatic control

This is based on the October 28 joystick-and-camera sketch. The latest assisted
manual application was uploaded and flash-hash verified on November9; its
commissioning checkpoint is in [ASSISTED-MANUAL.md](../../ASSISTED-MANUAL.md).
Physical tape wheel/floor checks are tracked separately from assisted stops.
The original sketches remain in the Arduino sketchbook and the earlier GitHub
draft folder. On this laptop, an ignored `config.h` has been prepared from
the original sketch's local hotspot settings. On another machine, copy
`config.h.example` to `config.h` and set the hotspot credentials before upload.

The Mega still receives `M:left,right` percentages over the existing UART.
An explicit stop sends a newline followed by `S` and another newline. This
finishes a partial packet before requesting the Mega's immediate pulse stop.

## Operator controls

The ESP32 boots in **stopped** mode. **ENABLE CAMERA-ASSISTED DRIVE** requires
a fresh clear camera guard and limits wheels to forward, at most35%.
**UNASSISTED MANUAL (NO CAMERA STOP)** selects the standalone joystick.
Releasing the joystick requests zero wheel speed. Press **STOP** to latch the
stopped mode. Select control again before driving after a stop or command timeout.
The camera relay and its `/frame` endpoint retain the existing JPEG protocol.

## LiDAR phone map (source update, not yet flashed)

The phone page opens on a live LiDAR map. Its Camera tab retains the optional
`/frame` preview for later use. The map is display-only; it does not change
motor control or replace the Pi's avoidance decisions. It marks itself stale
when no complete scan arrives for more than 1 second.

The Pi can send map frames over the ESP32 programming USB connection while
drive commands continue over the separate GPIO UART. One map frame is `AVL1`,
a four-byte little-endian payload length of 72, then 72 raw unsigned range
bytes. Bin 0 points robot-forward; bins increase clockwise in 5° steps (bin
18 right, 36 back, 54 left). Each byte is distance **from the C1 scanner** in
5 cm units: 0 means no valid return, 1–240 mean 5 cm–12 m. The Pi rotates the
scanner readings into robot heading, preserving their scanner origin. The
browser plots those returns from a marker 8 cm forward of the drive-wheel
midpoint, matching the measured build estimate.

`GET /lidar` returns `fresh`, `age_ms`, `step_deg`, `unit_cm`,
`sensor_forward_cm`, and `bins` (144 uppercase hex characters). Bad frame
lengths and range bytes above 240 are discarded. `/lidar` is read-only and
the USB map link has no access to the GPIO drive session.

The Pi requests automatic mode only on an explicit start action. Moving the
joystick requests assisted manual control from automatic mode; it refuses
when camera health is unavailable. Automatic commands are capped
at 35% per wheel. The Pi cruises at 25% with differential corrections after
the initial 6% ground trial barely moved. These are step-rate settings;
ground speed is not measured.

Each control selection grants a new session. Commands need that session and a
strictly increasing sequence number. Stop and timeout revoke the session, so a
delayed command cannot restart motion. The command lease is 350 ms. The Pi should
send fresh requests every 100 ms and stop when camera readings expire.

## HTTP interface

Use URL-encoded form bodies for POST requests. A session is an opaque 16-character
hexadecimal string. An epoch is an unsigned decimal integer read from `/state`.

| Method and route | Fields | Result |
|---|---|---|
| GET `/state` | none | JSON with mode, epoch, reason, lease, output percentages and automatic cap. Session is omitted. |
| POST `/manual/arm` | `epoch` | Select manual and return a new session. |
| POST `/assist/arm` | `epoch` | Select assisted manual only with a fresh clear guard. |
| POST `/auto/arm` | `epoch` | Select automatic and return a new session. |
| POST `/drive` | `session`, `seq`, `l`, `r` | Manual command, wheel percentages from -100 to 100. |
| POST `/auto/drive` | `session`, `seq`, `l`, `r` | Automatic command, wheel percentages from -35 to 35. |
| POST `/auto/stop` | `session` | Stop only if this session still owns automatic control. |
| POST `/stop` | none | Operator stop, always latches and revokes the current session. |

Successful drive commands return 204. Malformed values or percentages beyond the
mode's cap return 400. Changed ownership, expired sessions and replayed sequence
numbers return 409. Rejected requests do not extend the command lease.

Arm responses include `mode`, `epoch`, `session`, `lease_ms` and
`max_auto_percent`. The Pi must stop trying to drive after a 409. Its cleanup
uses `/auto/stop` with its session, so an old automatic process cannot stop a
new manual session. `/stop` belongs to the operator and intentionally stops any
owner.

The epoch check also rejects a queued arm request when Stop has changed the
state. Each boot starts with a random epoch and new selections get random
64-bit sessions. These values coordinate ownership on the existing hotspot.

## Pi serial connection

The current robot control connection uses the separate GPIO UART: Pi physical
8 TX to ESP32 GPIO25 RX, Pi physical10 RX from ESP32 GPIO26 TX, and shared GND.
See the Pi workspace's `PI-ESP32-WIRING.md`. It uses the same framed session
protocol described below. USB is retained for programming and power; phone
JPEG relaying is paused while the USB data issue is unresolved.

`argus-bridge.service` runs `argus_avoidance.usb_bridge` as the single GPIO
serial owner at115200 baud and exposes the automatic-session API on Pi
localhost:8766. The installed flags `--no-phone-preview --manual-guard` pause
JPEG relaying and publish camera guard health. USB data remains an earlier
transport/programming option; the phone keeps using the ESP32 hotspot.

Serial requests start with hexadecimal `A5 DA C3 BC`, then two 7-bit length bytes
with bit 7 set, followed by ASCII CSV with bit 7 set on every byte. Payloads are
`id,state`, `id,arm,epoch`, `id,drive,session,sequence,left,right` or
`id,stop,session`. All request bytes are non-ASCII so a mistaken port probe
cannot produce legacy Mega ASCII drive commands. Replies use `AVR1`, a four-byte
little-endian length and JSON carrying `request_id` and `status`.

## Software checks

`tests/host_check.cpp` compiles the actual sketch with small Wi-Fi, HTTP, serial
and clock stand-ins. It exercises the registered HTTP routes, including delayed
packets, explicit stops, manual takeover, timeout, input bounds, rollover and
camera frame parsing. `tests/browser_check.js` executes the actual embedded
browser script with DOM/HTTP stand-ins and tests state-poll ordering and Stop
while a drive request is in flight.

From this folder, a host compiler and Node can run these checks. Write binaries
to the project's `.tmp/argus-auto-tests` folder outside this source directory.
The ESP32 target is `esp32:esp32:nodemcu-32s`. Compilation uses the private
config.h; firmware binaries contain those credentials and must not be published.
Loaded stopping and real camera/control timing need a separate physical check.

## Assisted manual stop gate

ManualGuard.h adds an opt-in, latched camera guard. GPIO-only `id,garm,epoch`
returns a guard_token; `id,gupdate,token,sequence,code` accepts code0 clear,
1 blocked, or2 unavailable. Reports expire after800ms. Tokens and sequence
numbers reject previous publishers and replay. State includes assist, guard
and guard_latched. `/assist/arm` requires a current clear report and explicit
epoch; it caps forward commands at35%. A current assisted selection with an
unavailable camera stops an older unassisted drive instead of silently keeping
that unprotected drive active. A stale selection preserves the newer owner.

Default `/manual/arm` is explicitly labeled unassisted; it keeps the original
standalone joystick. `/auto/arm` and phone tape Start are also outside this
manual-assistance mode. See robot_control/ASSISTED-MANUAL.md for limits and
commissioning state. The preview's generic floor anomalies are not guaranteed
object recognition or measured obstacle clearance.
