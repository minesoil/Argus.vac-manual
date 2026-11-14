# C1 floor commissioning — 14 November 2026

Evidence: live Pi serial previews and controller logs, ESP32 `/state` readbacks,
115–120 Python tests on the Pi, Justin's direct wheel/floor observations, and
`workspace/robot_control/progress/2026-11-14-lidar-roaming.md`.

The C1 is live on Pi USB by-id through the CP2102. A front target set raw
robot-forward to about 90°. The Pi bridge has the new Python source; its
private roaming profile remains uncommissioned and the new ESP32 phone Start
firmware has not been flashed. The phone's existing Stop path is present.

Justin visually confirmed both raised wheels move forward and that a left
pivot reverses the left wheel while advancing the right. He confirmed a short
loaded forward crawl and Stop, then a loaded right pivot followed by forward
travel without contact. A later floor trial logged Stop, turn, forward travel
and another Stop/turn; Justin observed repeated right turns and felt the robot
was not close to walls. Side clearance thresholds were tuned for the cramped
room, and moving steering was added for open forward paths. The latest bounded
trial logged a moving right curve, a Stop/pivot, then forward travel; Justin
still perceived the stop-turn-go motion. All sessions ended with ESP32 mode
stopped and wheel outputs zero. 120 Python tests passed on Pi.

Raw diagnostics showed a recurring missing five-degree slice at raw 10–15°.
Adjacent pairs of measured slices now feed 36 ten-degree control bins; a pair
with no return stays unknown. This reduces nuisance stops but can miss a thin
object confined to the missing slice. A close left-side return changed its raw
angle after Justin manually rotated the robot, confirming an external object.
The assistant initially mislabeled that left-side return as right and asked
Justin to move left; this was corrected before further motor motion.

The `--continuous` software mode exists but has not been run on the floor.
Physical sensor offset, full footprint, loaded stopping distance, sustained
room behavior, outdoor open-space coverage and drop-off detection remain
unverified. Floor tape is not a lidar boundary. Last confirmed motor power
was ON for the bounded floor test; switch-off was not confirmed. Source:
GitHub commit `a5896f1abd1b072824ed8b5eda3ec14474d14c3d`.

Dinner handoff: Justin says the C1 is laterally centered and 3.5–4 cm behind
the robot front; he estimates 6 cm from the lidar housing rear to the drive
wheel midpoint. The diagram's origin and scan-center offset are not known.
A stationary preview assuming +0.16 m offset and 0.30 m chassis radius blocked;
that assumption is not the commissioned pose. No more motor motion was sent.
Justin was asked to switch motor power OFF before dinner; not yet confirmed.
