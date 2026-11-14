# Arc/map software checks and interrupted ESP32 update — 14 November 2026

**Later recovery, about 21:11 Asia/Taipei: ESP32 application flash succeeded
and the phone live map is confirmed.** The interruption below is retained as
history; see the final recovery checkpoint for the current dated status.

Evidence: Justin's direct geometry and motor-power statements in the current
14 November chat, plus the parent agent's reported Pi tests, source checks,
target compile and flash logs. The original interruption and later verified
application recovery are dated separately; neither establishes new physical
arc/map validation or completed roaming commissioning.

## Confirmed dimensions and power

Justin states a 30 cm robot diameter and a maximum body radius of 15 cm from
the drive-wheel midpoint. He estimates the C1 scan origin about 8 cm forward
of that midpoint, centered laterally. The private Pi profile uses
`sensor_x=0.08 m`, `sensor_y=0`, `radius=0.15 m`, `commissioned=false`.
The lidar offset remains approximate. These dimensions supersede earlier
zero-offset/0.23 m placeholders and the hypothetical +0.16 m preview.

Tonight Justin explicitly confirmed drive-motor power **OFF** for the ESP32
update. This resolves the earlier dinner switch-off-confirmation gap as a
dated user confirmation; it is not a continuing live measurement.

## Checked software and installation scope

Smooth arcs and `--wall-gap` are implemented. All 133 Python tests passed on
the actual Pi twice. Actual-sketch host and browser tests passed, and the
ESP32 target compiled to a 950160-byte application. The Pi map-hub is installed.
These results establish software checks and that Pi installation only; they
do not establish completed ESP32 deployment or physical arc/map performance.

## Earlier interruption and recovery requirement

During the ESP32 application flash, the CH340 serial connection clashed with
the bridge service. The attempt failed at 2.7% after application-sector erase.
At this checkpoint the ESP32 application is incomplete and the phone
controller/service is unavailable until recovery. Recovery is in progress.
A private flash backup was read before the write; keep it private and do not
archive or publish firmware containing credentials.

Do not rely on the earlier phone Stop/controller-availability statements while
the application remains incomplete. Successful recovery needs a completed
flash, verification and restored phone/controller checks; none is established
by this checkpoint. Keep motor power OFF during recovery.

## Physical limits retained

Earlier same-day loaded trials included a right pivot then forward motion
without contact, and Justin observed repeated stop-turn-go. Continuous drive,
outdoor operation and close-wall behavior remain physically unvalidated.
The private profile remains uncommissioned. Passing software tests or target
compilation does not complete those checks.

## Recovery checkpoint — about 21:11 Asia/Taipei, 14 November

Evidence: parent agent's esptool, process/service and HTTP readbacks from this
chat, plus Justin's direct phone-map confirmation. Esptool wrote the
950160-byte application at `0x10000`, verified the flash hash and performed a
hard reset. This supersedes the incomplete-application/phone-unavailable
condition above. The original private Pi profile was restored.

The systemd bridge service was **inactive after a clean stop**. A manual,
unprivileged bridge process, PID 16802 at this checkpoint, was running the
exact service command. Do not describe this as systemd running or infer
service persistence from that manual process. Localhost state was stopped,
left/right outputs zero, and `/lidar/sweep` returned 72 bins.

Justin refreshed his phone and confirmed the live map. He described it as
slightly laggy and requested a more technical interface. This establishes
phone/map restoration and records the next UI preference; latency resolution
and a redesigned interface are not yet established by this checkpoint.

A stationary C1 bridge preview with the revised geometry returned a fresh
72-bin sweep, 1.115 m forward clearance and a forward software decision. No
motor command was sent for this preview. The latest dated motor-power
confirmation remains OFF. No new floor-drive, continuous, outdoor or close-wall
physical validation occurred. The earlier loaded trials retain their limited
scope, and the roaming profile remains uncommissioned.
