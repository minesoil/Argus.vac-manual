# First software verification — 2026-11-07, Asia/Taipei

Executed `Run-Checks.ps1` using the already installed Python 3.12.14. No runtime
or dependency installation, firmware upload, serial access or physical movement.

- **44 tests passed:** 26 controller tests, 11 offline adapter tests and seven
  geometry/scenario tests. One scenario test executes all nine modeled cases.
- **Nine standalone 2D scenarios passed, zero modeled contact substeps.**
  The [JSON report](standalone-simulation.json) includes geometry, actual
  acceleration-limited trajectories, state transitions and clearance metrics.
- Wall, chair leg and moving-obstruction scenarios turn and resume; minimum
  modeled physical clearances are approximately 0.092, 0.082 and 0.078 m.
  Intentionally constrained corner/rear cases begin with 0.020 m body clearance
  and stay stopped; that is below the configured 0.030 m motion margin.
- Lost/unknown scans stop and latch; fresh input alone does not restart motion.
  Replay, source-age expiry, late guard replies and unsafe topic remapping have
  regression checks. Small unknown scan cones now refuse motion.
- A separate code review found and prompted fixes for unknown rays being treated
  as clear, output remapping bypass, and source-age/guard-response expiry. The
  re-review found no further substantial issue and independently reran all tests.

The controller uses a provisional circular body of radius 0.22 m plus 0.03 m
margin. The simulation uses 720 full-circle rays at 10 Hz, 20 Hz control, 0.4 m/s²
linear and 1.5 rad/s² angular acceleration, and 0.01 s integration/contact checks.
Its positive-infinity no-return convention is explicitly enabled only for this
known model. Footprint and lidar pose on the actual robot remain unmeasured.

**Not verified:** live ROS/DDS/TF/lifecycle behavior, a ROS/colcon deployment,
real sensor returns or visibility, current ESP32/Mega protocol or source
arbitration, firmware/serial behavior, loaded motor performance, mounted fit,
physical collision avoidance, low floor obstacles or drop-offs. Adapter tests
use small ROS stand-ins with actual production callbacks and core; they cannot
establish live integration. ROS source/launch syntax and package XML were checked.
YAML configuration was inspected; no ROS parameter loader was available here.

Current control remains Justin's Wi-Fi → ESP32 → Mega manual path. The new
package is separate software with output disabled; its optional ROS adapter
does not intercept that path or arm motors. Orange Pi use is a later idea.

The old WSL simulator was unavailable at its registered disk path; Justin then
confirmed intentionally removing it and approved a small alternative. No
attempt was made to restore or reinstall it. Project source, tests and the JSON
report occupy well under 1 MB, excluding the existing Python interpreter.
