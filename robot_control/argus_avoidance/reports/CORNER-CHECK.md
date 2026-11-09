# Sharp-corner commissioning — 9 November 2026

Phone Start is installed and hash verified. All 88 checks pass on the Pi.
Phone Start/Stop and phone-lock stop pass motors-off; the restored bank-powered
ESP GPIO link survives Pi reboot and starts stopped. User confirms both raised
wheels forward and stopped under phone control. Floor trials below retain
Ethernet; a completed untethered run has not been verified.

## First stop: visible gap

User reports a stop roughly 12 cm before a 45° tape turn. This does not measure
the camera's physical blind spot. Logs show "Tape must extend continuously
through the lower floor view" and automatic scoped stop, rather than a timer.

A stationary 640×480 frame at the stopped position splits the tape into two
dark components in the configured bottom 116 rows (crop begins at row 364).
The lower component covers 60.3% of those rows, below the 70% requirement;
the upper component covers 34.5%. A light break is visible between them.

Justin chooses to retain the sharp corner and overlaps the joins, motor off.
At the same pose, the original detector now returns FORWARD, error +0.0558,
confidence 1.0. No controller thresholds or driving code have been changed.

## Second stop: inadequate corner view

User starts another short floor trial from the phone with Ethernet attached.
Logs progress from FORWARD +0.06 to RIGHT +0.14, then stop on the same continuity
condition. User observes the robot beginning to turn, then stopping after only
a small part of the turn. State confirms automatic stop with zero outputs.

The subsequent frame shows mostly room/background, a dark edge inside the
analysis region, and tape exiting the bottom-right of the picture. The near
tape component covers 58.6% of the band; a separate dark component spans the
full image width. Simply widening the crop upward (0.74 through 0.68) includes
more dark background and produces STOP, not a usable lookahead view.

Next step is motor-off downward camera adjustment and secure mounting while
preserving the 45° course. Inspect a fresh frame, calibrate the usable floor
region, and test any detector/steering changes before another drive. Do not
continue blindly or relax gap checks to force this view to pass.

Private diagnostic frames stay local in .tmp/corner-check and on the Pi under
.tools/corner-check. They are not included in the public report.
