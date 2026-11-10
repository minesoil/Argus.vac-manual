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

## Fixed mounting constraint and framing adjustment

Justin confirms that the camera assembly also holds the caster. It cannot be
tilted independently without structural changes. Preserve the mount.

An upward crop extension fails because it includes more dark background. A
simple narrower crop accepts the original gapped frame as well, so it was not
deployed. Instead, usable_floor excludes only a shallow, separate dark band
touching the top and both sides of the original floor ROI, with at least half
the rows and 48 rows retained. Joined tape, deep patches, crossings and gaps
retain the normal stop rules. This is framing for the tape demo, not obstacle
clearance detection.

Saved-frame regression: original gap STOP, joined tape FORWARD/confidence 1.0,
post-turn tape RIGHT/error +0.712/confidence 0.944. Four new regression tests
cover the isolated band, a gap below it, a connected crossbar and a deep band.
All 92 tests pass locally and on Pi. Two-second live stationary preview returns
RIGHT consistently with 0.94–0.96 confidence. User attempts a short floor run;
it turns a little and stops again. Logs show excessive dark coverage. The next
frame's band reaches 63 of 116 rows, beyond the permitted trim; the tape itself
covers only 35.3% of the original band. The stop gate remains intact.

## Tighter turns, awaiting physical verification

The original large-error command keeps both wheels moving quickly (e.g.32/18),
creating a wide arc. A revised wheel law reduces forward motion for |error|>0.35;
the outside wheel is 25%, the inside wheel decreases smoothly to zero at 0.65.
Small corrections and all camera freshness, Stop, ownership and lease checks
are unchanged. No reverse or blind-search motion is added.

A test sweeps large errors to verify mirrored left/right commands, bounds,
decreasing forward travel and increasing turn curvature. All 93 tests pass
locally and on the actual Pi. User confirms motor OFF; code installed, bridge
restarted. Repositioning onto the straight section before the corner is pending
before the next drive. A successful sharp-corner or untethered run is not claimed.

Justin reiterates the primary goal: manual driving with camera obstacle warning
and automatic stop. This remains separate, unimplemented work; these tape tests
do not provide obstacle protection to manual driving.

Final trial: after repositioning, camera reports FORWARD -0.08/confidence 0.99–1.0.
User runs the tighter-turn version and observes sharper turning, then another
early stop. Logs show RIGHT errors +0.51 through +0.55, confidence declining
0.85 to0.76, followed by "Too much of the floor matches the tape colour".
Final GPIO state is STOPPED/zero. User delegates when to stop tape testing;
assistant stops it here to prioritize assisted manual warning/braking. No
successful complete sharp-corner or untethered floor run is claimed. Ethernet
remained connected during the reported floor tests.
