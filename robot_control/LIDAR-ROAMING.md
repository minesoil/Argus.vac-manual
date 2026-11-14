# Lidar roaming — implementation and tonight's commissioning

Goal requested 14 November 2026: drive around a closed room, stop before a wall
or obstacle, pivot toward more clearance, and continue. On 15 November Justin
plans an outdoor showcase in Hsinchu. He cannot guarantee an enclosure and may
mark an area with floor tape. Tape is an operator marker, not a lidar boundary.

## Pipeline

`C1 USB (460800) → complete revolutions → body-relative clearance → STOP / FORWARD / SLOW / TURN → Pi HTTP bridge → GPIO UART → ESP32 leased session → Mega → wheels`

This reuses the reviewed state machine and drive arbitration. ROS mapping,
localization and navigation are not prerequisites for this reactive demo.
It is not room coverage planning; loops and unvisited patches are possible.

Each revolution is reduced to 72 five-degree bins using the nearest valid
return in each bin. Invalid/zero returns stay unknown. All bins must have a
valid observation; receipt age uses the start of the revolution, with a 600 ms
limit. Acquisition corruption invalidates that revolution; large UART backlogs
and disconnects stop the run. The conservative policy may refuse to run in open
outdoor space or when the robot's own structure occludes the scanner.

Forward clearance is calculated across the full footprint width with sensor
translation and orientation applied. Default footprint radius is 230 mm plus
60 mm margin; these are commissioning placeholders, not measured dimensions.
Distance thresholds are measured beyond that inflated footprint: slow at
600 mm, stop at 300 mm, resume above 400 mm after three distinct clear scans.
First stop, wait 250 ms, then pivot toward the clearer side. An obstacle inside
the rotation footprint stops the run. A turn that cannot clear in 15 s latches
BLOCKED instead of repeatedly reversing or spinning.

Default commands are 18% cruise, 12% slow, 15% pivot. Percent is not a calibrated
linear/angular speed. Confirm that both wheels move reliably at these values
and measure stopping before a floor trial. The old core SI speed fields select
states; this runner deliberately uses commissioned wheel percentages rather
than claiming an unmeasured metres/second conversion.

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
3. Stationary preview, with no drive client:

   ```sh
   cd /home/orangepi/argus/avoidance
   ./argus roam --lidar /dev/serial/by-id/ACTUAL_C1 --seconds 30
   ```

   A healthy stream needs 72 known bins, fresh ages and no sensor fault. If it
   refuses on missing coverage, investigate power, scanner occlusion, targets and
   illumination. Do not convert missing returns into invented clear distances.
4. Measure raw scanner direction by placing a broad upright target in front of
   the robot, at lidar height. Use `python3 -m argus_avoidance.c1_preview` to print
   its nearest raw-angle bins. Verify front, left and right. Set `front_deg` to
   the raw clockwise angle pointing forward. Measure sensor x/y from the drive
   rotation centre (x forward, y left) and a radius containing every protrusion.
5. Copy `config/roam.example.json` to private `.state/roam.json`. Fill measured
   geometry and device path; leave `commissioned` false until checks below pass.
   Add `--roam-config .state/roam.json` to the existing bridge's ExecStart, keeping
   `--serial /dev/ttyS0 --no-phone-preview --manual-guard`. The optional drop-in
   template is `systemd/argus-bridge-roam.conf`. Boot never starts moving.
6. With wheels raised, check both forward and in-place left/right direction
   using short supervised sessions. Check phone Stop, phone lock and dropped
   lidar/control link. Confirm no automatic restart. On the floor, use a short
   low-speed approach to a large upright box with Stop ready and ample space;
   measure the stopped gap. Stop and retune if the margin is inadequate.
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
ranging. This implementation adds software checks for wall-stop-turn-resume,
stale/unknown scans, swept-footprint hazards, phone Stop, turn timeout, raw-angle
conversion and separate phone request routing. Test results and installation
status are recorded in `progress/2026-11-14-lidar-roaming.md`. No source file,
compiled target or software test establishes physical commissioning.

Source: [SLAMTEC C1 specification](https://www.slamtec.com/en/c1/spec).
