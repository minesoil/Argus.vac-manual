# Basic obstacle avoidance proposal — 2026-11-07

Status: first software implementation written and offline-tested after Justin
said "keep going". Hardware integration and live ROS validation remain pending.
Confirmed target: physical Argus; use the small Python alternative because the
previous simulator was intentionally removed. Latest direct context:
[lid fit, ESP32 manual control and future Pi idea](../updates/2026-11-07-lid-fits-and-control-path.md).
[Implementation and verification](../../workspace/robot_control/argus_avoidance/README.md).
[Direct user evidence](../updates/2026-11-07-obstacle-avoidance-request.md).

## Intended first behavior

Use the existing RPLIDAR C1 design for a reactive controller: drive slowly,
slow for an approaching obstruction, stop, turn toward a sufficiently clear
side, then resume when the forward path stays clear. Camera alerts for low floor
objects are a follow-up increment. Mapping and room coverage are later work.

## Integration proposal

The new core is independent of ROS. Its optional adapter targets the archived
RobotLab path, whose documented Collision Monitor, bridge and watchdog are
software references, not confirmed installed components. Current actual control
is Wi-Fi → ESP32 → Mega, manually; its protocol and command arbitration must be
identified before adding automatic input. Orange Pi/Ethernet/SSH/VS Code is a
future setup idea. The proposed guarded integration remains:

`manual OR reactive avoidance → command selection → Collision Monitor → motor bridge → Mega → TB6600 drive`

Only the selected source supplies commands; manual mode must not initiate
automatic turns. All sources pass through the final guard. Automatic mode
requires deliberate arming; leaving it cancels its motion request. Recovery
from sensor/communication faults requires fresh input and re-arming. The active
bridge and firmware must use the same protocol; legacy letter commands and the
newer CRC protocol are incompatible.

## Proposed sequence

1. **Confirm the baseline.** Inspect working source, firmware/protocol, both
   motor directions and driver operation, lidar orientation and scan timing.
   Measure the full footprint including protrusions and the lidar offset. The
   latest lidar update is 2026-11-07: the lid now fits, superseding the earlier
   same-day wiring-height blocker. Check secure mounting and installed sensor
   pose before physical trials. Manual Wi-Fi/ESP32/Mega control is confirmed,
   but its protocol is not identified. Pi use is planned for later; current
   two-driver commissioning details remain unverified.
2. **Display sensor readings without driving.** Transform scan returns into
   the robot frame and display forward/left/right clearance and scan age. Check
   a corridor wide enough for the whole robot. Reject malformed/out-of-range
   samples, respecting the selected driver's documented no-return semantics.
   Detached-lidar bench readings can check sensor operation; robot-relative
   clearance checks require the sensor's final mounted position.
   Inadequate sector coverage is unknown, not proof of free space. Do not
   average away a thin nearby obstacle.
3. **Add simple states.** DISARMED → FORWARD → SLOW → STOP → TURN → FORWARD,
   with BLOCKED/FAULT as stopped states. Stop before choosing a turn; check the
   full swept footprint before and during rotation. Hold the chosen direction
   until a sufficiently wide forward corridor stays clear across several fresh
   scans. Separate stop/resume thresholds prevent rapid switching. If both
   turns are blocked, attempts repeat without progress or a turn times out,
   remain stopped. Omit automatic reversing in this first version.
4. **Preserve independent stopping.** Start avoidance outside the existing
   Collision Monitor stop zone; its fixed polygon can suppress rotation too.
   Do not bypass it to escape. Choose thresholds from the footprint, scan/control
   delay and measured stopping distance. The archived bridge ramps velocity, so
   a zero command is not an instantaneous physical stop. Stop on stale scans,
   invalid required transforms, command expiry or serial failure. Retain the
   firmware watchdog.
5. **Test simulator, then hardware.** Simulate an empty path, wall, chair leg,
   corner, blocked sides, moving obstruction and lost/invalid scans. Check mode
   changes, guard intervention, controller/serial loss, timeouts and restart
   behavior. Then verify stationary sensor readings and raised-wheel direction/
   watchdog behavior before supervised floor trials. Begin with one obstacle
   on a level clear floor; measure stopping before adding chair legs and corners.

## Initial tuning proposals

- First floor-test crawl target: **0.05 m/s**, subject to reliable loaded drive
  operation and measured stopping. This is unvalidated. Set a separate low turn
  limit after checking the drive.
- Illustrative zones: slow within **0.60 m** of the leading body edge; stop
  within **0.30 m**; resume above **0.40 m** for several fresh scans. These are
  proposals, not validated clearances. Convert through the measured lidar
  transform, check against the existing stop polygon, and tune from trials.
- Keep speed, clearances and timeouts configurable. Display state, clearances,
  scan age and the reason motion is stopped.

## Acceptance and limits

For tested obstacles: stop before contact, turn only with sufficient swept
clearance, resume without repeated left/right switching, and stay stopped when
trapped or input is lost. Record actual speed, closest clearance and stopping
distance. Simulation and raised-wheel results do not prove loaded performance.

A single 2D scan cannot establish clearance below its scan plane or detect
drop-offs. Initial trials need controlled obstacles on a level floor. Add the
camera later as an additional hazard input after checking mounted visibility,
latency and failure behavior. Review the existing detector's suppression of
static unknown objects before using it to authorize motion. A monocular
detection alone is not a validated metric distance measurement.

## Evidence

- [Current physical build, updated 2026-11-07](../CURRENT_BUILD_STATE.md).
- [Latest lidar-lid clearance evidence](../updates/2026-11-07-lidar-lid-wiring-clearance.md).
- [RobotLab architecture snapshot, 2026-10-07](../text/1c00e63e2dbdf342de4b--architecture.md.md).
- [Hardware configuration](../text/2d65f22d8a96c5384fe0--hardware.yaml.md):
  fixed StopZone and scan timeout.
- [Motor bridge](../text/73d3414d80f3109f5de1--motor_bridge.py.md):
  scan freshness, command handling and velocity ramp.
- [Camera detector](../text/3ed6887665294227ae51--obstacle-detector-mediapipe-v10.6.py.md).
- [Nav2 Jazzy Collision Monitor](https://ros-navigation.github.io/mkdocs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/collision_monitor/configuring_collision_monitor_node/):
  stop/slowdown actions and stale-source handling; checked 2026-11-07.
- [Nav2 integration tutorial](https://docs.nav2.org/rolling/tutorials/general_tutorials/using_collision_monitor/using_collision_monitor/):
  monitor last in command processing; checked 2026-11-07. Match implementation
  to the installed ROS distribution.
- [SLAMTEC C1](https://www.slamtec.com/en/c1): 360-degree scan for navigation
  and avoidance; checked 2026-11-07.
