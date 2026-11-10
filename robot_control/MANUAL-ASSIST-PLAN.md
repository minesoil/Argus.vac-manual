# Camera assistance plan and remaining checks

Updated 10 November: the preview, phone warning and latched firmware gate below
are now implemented and installed. See [ASSISTED-MANUAL.md](ASSISTED-MANUAL.md)
for the recovered November9 checkpoint. The motors-OFF object-entry test and
physical stopping stages remain pending. Earlier planning text follows.

Justin wants to drive manually while the camera warns him and stops Argus on
a detected obstacle. Tape following remains a demo. The installed prototype
compares floor appearance; it has not completed real object-stop commissioning.

## 1. Stationary detection preview

Use the existing fresh, timestamped camera stream. Review archived detector
code/models before selecting what to deploy; archived results do not prove
current detection quality. Display detections, proposed driving-path region,
warning state and frame/inference age. Check shoes, cables, boxes, shadows and
missed objects without sending motor commands.

The fixed camera assembly holds the caster. Do not assume independent tilt.
Use the actual full frame for obstacle perception; the tape demo's dark-band
trim is not an obstacle-clearance rule. Measure the near blind area rather
than treat the observed tape stopping gap as a calibrated distance.

## 2. Phone warning and latched stop

In an explicitly enabled assisted-manual mode, a hazard should show a clear
phone warning and stop the drive. Repeated joystick commands must not override
the stop. Require a clear view and deliberate driver acknowledgement to resume.
A stale camera or lost guard heartbeat in that mode should also stop.

Add guard state/lease and arbitration in the shared drive path. An ordinary
automatic-session stop is insufficient because it preserves a newer manual
owner. Preserve operator Stop priority and reject stale guard packets. Any
standalone, unassisted manual fallback must be clearly labeled unprotected.

## 3. Verification

With motor power off, test actual phone warnings, hazard while joystick is held,
command rejection, camera/guard dropout, restart and attempted premature re-enable.
Then use raised wheels, followed by a slow supervised trial against a soft object.

Monocular class detection can miss unknown objects and does not prove distance
or a clear path. Measure latency and physical stopping behavior. Restoring LiDAR
remains useful later; automatic detours are not the immediate goal.
