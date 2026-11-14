# Lidar roaming — implementation and tonight's commissioning

Goal requested 14 November 2026: drive around a closed room, curve around an
obstacle when the scan leaves room, otherwise stop, pivot and continue. On 15
November Justin plans an outdoor showcase in Hsinchu. He cannot guarantee an
enclosure and may mark an area with floor tape. Tape is an operator marker,
not a lidar boundary.

## Pipeline

`C1 USB (460800) → one Pi scanner owner → complete revolutions → local /lidar/sweep → body-relative clearance → STOP / FORWARD / SLOW / TURN → Pi HTTP bridge → GPIO UART → ESP32 leased session → Mega → wheels`

The same Pi scanner owner sends a display copy over the separate Pi-to-ESP32 USB
serial link. The ESP32 serves that copy to the phone's LiDAR canvas. This map
path is independent of the GPIO UART drive link and does not command motion.

This reuses the reviewed state machine and drive arbitration. ROS mapping,
localization and navigation are not prerequisites for this reactive demo.
It is not room coverage planning; loops and unvisited patches are possible.

Each revolution is reduced to 72 five-degree diagnostic bins, then adjacent
pairs are grouped into 36 ten-degree control bins using the nearest measured
return. A pair without a return stays unknown. All control bins must have a
valid observation; receipt age uses the start of the revolution, with a 600 ms
limit. Acquisition corruption invalidates that revolution; large UART backlogs
and disconnects stop the run. The conservative policy may refuse to run in open
outdoor space or when the robot's own structure occludes the scanner.

Forward clearance is calculated across the full footprint width with sensor
translation and orientation applied. Justin's latest working dimensions are a
150 mm maximum body radius from the drive-wheel midpoint and a C1 scan centre
roughly 80 mm forward, centred left-to-right. The Pi private profile uses
`radius=0.15`, `sensor_x=0.08`, `sensor_y=0`; these are user estimates that have
not had a loaded motion trial since the correction. They supersede the earlier
230 mm radius/zero-offset placeholders. The runner adds a 60 mm margin, giving
a 210 mm inflated circular footprint for the current profile. A standalone
command without that profile still defaults to its old 230 mm radius, so pass
the measured arguments explicitly.

Distance thresholds are measured beyond the inflated footprint: slow at
600 mm, stop at 300 mm, resume above 400 mm after three distinct clear scans.
`--wall-gap` sets front stop clearance beyond the inflated footprint from
200–400 mm; the default is 300 mm and front resume remains 100 mm farther
away. Side steering begins at the requested gap minus the 60 mm margin, measured
beyond the inflated footprint (240 mm at the default, 140 mm at the 200 mm
setting). This makes the requested value roughly a side body-to-wall steering
gap, while front stopping still includes the extra 60 mm margin relative to the
body. The 50 mm hard side-stop threshold and the 60 mm footprint margin do not
change. The same optional `wall_gap` field can be put in the private roaming
profile. These are control thresholds, not a guaranteed final physical gap to
a wall. The lower limit must not be used to claim close-wall cleaning until the
loaded stopping distance, scan-origin pose and full chassis extent have been
checked.
Forward travel also stops when either side has less than 50 mm beyond the
inflated footprint, to catch drift toward a wall before the turn clearance is lost.
With an obstacle narrowing the front clearance to 680 mm, the controller can
start a forward-moving left or right curve at slow speed. It checks a 240 mm
lookahead for the whole inflated circular footprint against current scan points
over straight and several plausible arc curvatures. It chooses a scanned-clear
side and holds that direction until the front opens; both wheels keep turning
forward, with the inner wheel slowed by at most half the requested power.
This sampled path check cannot replace wheelbase or loaded braking measurements.
When the front is otherwise open, the robot can also gently steer away from a
nearer side obstacle after checking the same short path. If a forward curve is
not clear, the front and side stop rules still apply: stop, wait 250 ms, then
pivot toward the clearer side. The side need not
fit a forward path for an in-place pivot; the full swept footprint must still
be clear. An obstacle inside the rotation footprint stops the run. A turn that
cannot clear in 15 s latches
BLOCKED instead of repeatedly reversing or spinning.

Default commands are 18% cruise, 12% slow, 15% pivot. Percent is not a calibrated
linear/angular speed. Confirm that both wheels move reliably at these values
and measure stopping before a floor trial. The old core SI speed fields select
states; this runner deliberately uses commissioned wheel percentages rather
than claiming an unmeasured metres/second conversion.

## Phone LiDAR view

The proposed phone page opens on **LiDAR map**. It draws 72 five-degree rays
with robot-forward at the top, a body outline, the roughly 8 cm forward scan
origin, selectable range and a visible stale/disconnected state. The Pi encodes
each raw range in 5 cm steps and sends at most one map packet every 250 ms over
the ESP32 USB serial port. Zero means unknown. The ESP32 serves `/lidar`; the
browser polls every 250 ms and marks data stale after one second. This is a live relative
range view, not a persistent room map or localization. A **Camera** selection
remains as an optional preview placeholder for future use.

The bridge owns the C1 port so the phone and roaming runner do not compete for
USB serial access. The runner reads the latest sweep from the bridge's loopback
`/lidar/sweep` endpoint. Failure of the separate map USB link leaves the drive
link available; stale or invalid C1 data still stops autonomous roaming.

## Operator behaviour

The updated ESP32 page adds **START LIDAR ROAMING**, separately from tape
following. Start is a one-shot request bound to the stopped epoch. The bridge
claims its selected kind, so a roaming request cannot fall back to the tape
follower. Missing/uncommissioned roaming configuration disables that Start.
Phone Stop, page hidden/locked, lost phone heartbeat, manual takeover, expired
350 ms drive lease, bad scans or connection faults end the session. New clear
scans never rearm a faulted/stopped run. Only another deliberate Start can do so.

Thirty seconds is the initial run limit. A measured profile can explicitly set
`continuous: true` to remove that timer. Battery, motor temperature, traction,
people and sensor performance still limit the run: continuous means no software
duration cap, not an assurance of indefinite or unattended operation.

## Install and commission in order

1. Connect Pi Ethernet and C1 USB; leave drive-motor power OFF. Confirm the actual
   Pi address, working SSH access, current stopped controller state and existing
   service configuration. Preserve a backup before installation. Give C1 a stable
   `/dev/serial/by-id/...` path, distinct from the GPIO control `/dev/ttyS0`.
2. Copy the updated Python package and matching ESP32 sources. Run Python tests
   on the Pi. Build/flash the matched ESP32 only with motor power OFF and verify
   the upload; retain private `config.h` without publishing it. Restore its normal
   power arrangement afterward and check GPIO Stop/zero outputs.
   For this Pi, staged Python files and a stopped, uncommissioned bridge installer
   are under `/home/orangepi/argus/roam-stage-20261114/`.
3. Stationary preview, with no drive client:

   ```sh
   cd /home/orangepi/argus/avoidance
   ./argus roam --lidar bridge --front-deg 90 --sensor-x 0.08 --sensor-y 0 --radius 0.15 --seconds 30
   ```

   This `bridge` form applies once the single-owner Pi bridge is running with
   the C1 profile; stop that bridge before using a direct serial reader. A
   healthy control stream needs all 36 grouped bins, fresh ages and no sensor
   fault. Raw diagnostics may show 71 of 72 bins because the 10–15° slice
   intermittently lacks returns on this indoor setup. If control refuses on
   missing coverage, investigate power, scanner occlusion and targets. Do not
   convert missing returns into invented clear distances.
4. Measure raw scanner direction by placing a broad upright target in front of
   the robot, at lidar height. Use `python3 -m argus_avoidance.c1_preview` to print
   its nearest raw-angle bins. Verify front, left and right. Set `front_deg` to
   the raw clockwise angle pointing forward. Measure sensor x/y from the drive
   rotation centre (x forward, y left) and a radius containing every protrusion.
5. Copy `config/roam.example.json` to private `.state/roam.json`. Fill measured
   geometry and device path; leave `commissioned` false until checks below pass.
   The map can run from this profile while driving remains disabled. Optional
   `map_port` selects the ESP32 USB device and `wall_gap` sets the bounded front
   stop clearance; neither enables roaming by itself.
   Add `--roam-config .state/roam.json` to the existing bridge's ExecStart, keeping
   `--serial /dev/ttyS0 --no-phone-preview --manual-guard`. The optional drop-in
   template is `systemd/argus-bridge-roam.conf`. Boot never starts moving.
6. With wheels raised, check both forward and in-place left/right direction
   using short supervised sessions. Check phone Stop, phone lock and dropped
   lidar/control link. Confirm no automatic restart. On the floor, use a short
   low-speed approach to a large upright box with Stop ready and ample space;
   measure the stopped gap. Stop and retune if the margin is inadequate.
   The command-line `--trial` mode is limited to 20 seconds and 12% wheel
   commands for that first supervised floor check; pass `--cruise 12 --turn 12`
   or lower. It does not mark the profile commissioned or enable the phone
   roaming Start. Check a moving curve as well as a pivot with Stop in hand.
7. After those physical checks, set `commissioned: true`, restart the bridge,
   press Stop, then **START LIDAR ROAMING** for the initial 30-second room test.
   Validate several different walls/corners and a placed object, then extend
   duration. Only then consider `continuous: true` while supervising.

## Outdoor showcase

Test in the actual lighting and on the actual level floor before the demo. The
manufacturer rates ambient-light resistance to 40,000 lux; this is not a promise
of reliable ranging under every sunlight condition. Missing coverage stops the
run. Prefer shade, large upright obstacles, slow speed and short supervised runs.
Keep the phone page open and Stop reachable. Floor tape does not constrain this
controller: an open arena needs an operator to stop/reset it at the marked line.
Upright barriers crossing lidar height can provide detectable boundaries.

The horizontal scanner does not establish clearance below its plane or detect
steps/drop-offs. It is not suitable for running loose among moving people, near
roads/steps, or unattended. This mode does not use the camera guard for low
objects; that remains a separate assisted-manual prototype.

## Verification status

The earlier C1 laptop test passed identity, health and three seconds of live
ranging. Later Pi and bounded loaded trials established C1 scans, forward motion,
a right pivot and no-contact continuation in the cramped room. Those trials
predate the corrected +80 mm sensor pose and new moving-curve code. Source now
also checks arc path selection, wall stop, stale/unknown scans, swept-footprint
hazards, phone Stop, turn timeout, raw-angle conversion and separate phone
request routing. Test results and installation status are recorded in
`progress/2026-11-14-lidar-roaming.md`. Source, simulations and a compiled
target do not establish close-wall physical validation or unattended roaming.

Source: [SLAMTEC C1 specification](https://www.slamtec.com/en/c1/spec).
