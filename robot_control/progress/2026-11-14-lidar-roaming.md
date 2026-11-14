# C1 roaming prototype — 14 November 2026

Justin requests wall/obstacle avoidance for a room tonight and an outdoor
Hsinchu showcase tomorrow. He later clarifies the outdoor area may be open;
floor tape can mark it for an operator but cannot be sensed by the C1.

Implemented a C1 reader, coverage checks, reactive stop/turn/continue runner,
separate phone roaming Start, and opt-in measured configuration. Unknown or
stale scans stop the session; Stop cannot be automatically overridden. The
example profile disables roaming until physical commissioning is complete.
See `robot_control/LIDAR-ROAMING.md` for method, calibration and limits.

Laptop verification: 114 Python tests passed; C++ host tests exercised actual
firmware routes including separate roaming Start, pivot and Stop; browser tests
passed; ESP32 Arduino target compiled with example configuration (942120 bytes).
An initial full Python run showed one timing-sensitive existing tape test fail;
it passed in isolation and in the later full suite. These are software results.

Justin says motor power is OFF and Pi, Ethernet and C1 are connected. Pi SSH at
192.168.137.195 responds but rejected key-based login; prior credentials were not
recoverable. No new code has been installed, flashed, run on Pi, or tested on
the robot. Sensor orientation and position, footprint, wheel pivot direction,
braking, scan coverage and outdoor performance remain unmeasured. The prior
three-second C1 laptop scan succeeded, but this new reader has not seen live data.

Justin says laptop internet sharing must be switched off and on again after a
laptop restart for sharing to the Pi to work; this restored reachability today.

Later 14 November checkpoint: Justin installed the laptop public key for the
`orangepi` SSH account. The C1 is live on the Pi by its CP2102 by-id path;
stationary full-circle previews returned 72 known bins and fresh scan ages.
An upright front target established raw 90° as the approximate robot-forward
direction. The tight indoor room has limited space. The first controller rule
rejected a pivot when neither side corridor was wide; revised core now allows
in-place rotation when the full swept footprint is clear. 115 Python tests
passed on the actual Pi. With wheels raised, the new controller sent bounded
forward and differential wheel pulses through the existing bridge. Justin
visually confirmed both wheels move forward for a forward command; pivot
directions were initially missed and remain to be confirmed. Every pulse ended
with the ESP32 stopped and outputs zero. This does not validate loaded motion.

The Pi bridge now has the new Python package and an opt-in `roam.json` profile
with `commissioned: false`; service is active and controller stopped. The
installer's final HTTP check raced the service startup and printed a connection
error after installation; a later readback confirmed staged files match, the
profile is readable by `orangepi`, and the corrected override is effective.
Installer wait logic has been fixed in source. The new ESP32 firmware is not
flashed, so its phone roaming Start is not yet available. Current source was
published as GitHub commit ed5168b2517585f7290974496eac406b11aa4373.
Floor stopping, true footprint and sensor offset remain unverified; outdoor
open-space scan coverage and boundary control also remain unverified.

Later floor checkpoint: Justin visually confirmed a raised-wheel left pivot
turns left wheel backward/right wheel forward. Raw C1 diagnostics showed a
repeatable single 5° bin without a return at raw 10–15° in 17 of 30 sampled
revolutions. The runner now groups adjacent bins into 36 ten-degree control
bins, taking the nearest measured return and retaining unknown for an entirely
missing pair. This allowed an eight-second raised-wheel closed-loop crawl;
ESP32 returned to stopped/zero. 116 Python tests passed on Pi at that stage.
The grouping cannot reveal an object confined to that missing slice, so this
remains a supervised prototype.

An explicit CLI `--trial` mode caps uncommissioned floor runs at 20 seconds
and 12% wheel commands. Justin reported the first actual four-second floor
trial moved forward a little and stopped. In the following 20-second trial,
the runner stayed in SLOW as side clearance shrank, then latched BLOCKED for
an object within the 290 mm swept-footprint proxy; ESP32 stopped with outputs
zero. Justin thinks it stopped about 22 cm before a wall, but did not establish
contact or travel direction. A later stationary scan showed a 286 mm closest
return at raw 0–10°, which maps to robot LEFT with calibrated raw front 90°.
The assistant incorrectly called it right and asked Justin to move left; a
subsequent scan found 274 mm at raw 10–20°. The error was corrected to Justin;
the controller itself uses left/right correctly. He was asked to reposition
about 20 cm right by hand with motor power off before any more motion.

The staged controller now stops forward motion when either side corridor is
within 150 mm beyond its inflated footprint, then pivots toward more room;
118 Python tests passed on Pi. This is staged, not yet installed in the active
bridge. No loaded turn/continue validation, measured stopping distance,
continuous room run, or outdoor trial has been completed.
