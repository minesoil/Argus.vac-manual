# ESP32 manual and automatic control

This is based on the October 28 joystick-and-camera sketch. It was uploaded and
flash-hash verified on the connected ESP32 on November 8. Physical wheel and
floor checks are tracked separately in the Pi's tape-following report.
The original sketches remain in the Arduino sketchbook and the earlier GitHub
draft folder. On this laptop, an ignored `config.h` has been prepared from
the original sketch's local hotspot settings. On another machine, copy
`config.h.example` to `config.h` and set the hotspot credentials before upload.

The Mega still receives `M:left,right` percentages over the existing UART.
An explicit stop sends a newline followed by `S` and another newline. This
finishes a partial packet before requesting the Mega's immediate pulse stop.

## Operator controls

The ESP32 boots in **stopped** mode. Press **ENABLE MANUAL** to use the joystick.
Releasing the joystick requests zero wheel speed. Press **STOP** to latch the
stopped mode. Select control again before driving after a stop or command timeout.
The camera relay and its `/frame` endpoint retain the existing JPEG protocol.

The Pi requests automatic mode only on an explicit start action. Moving the
joystick takes manual control from automatic mode. Automatic commands are capped
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

## Pi USB connection

The current robot control connection uses the separate GPIO UART: Pi physical
8 TX to ESP32 GPIO25 RX, Pi physical10 RX from ESP32 GPIO26 TX, and shared GND.
See the Pi workspace's `PI-ESP32-WIRING.md`. It uses the same framed session
protocol described below. USB is retained for programming and power; phone
JPEG relaying is paused while the USB data issue is unresolved.

The Pi connects through the ESP32's programming USB cable at 115200 baud.
`argus-bridge.service` runs the Pi's `argus_avoidance.usb_bridge` as the single
serial owner. It forwards small JPEGs for the phone preview and exposes the
automatic session API on the Pi's loopback address, port 8766. The phone keeps
using the ESP32 hotspot. The firmware ownership and expiry rules apply to both
USB and HTTP commands.

USB requests start with hexadecimal `A5 DA C3 BC`, then two 7-bit length bytes
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
The ESP32 target is `esp32:esp32:nodemcu-32s`. A compile uses example credentials
only. Loaded stopping and real camera/control timing need a separate physical check.
