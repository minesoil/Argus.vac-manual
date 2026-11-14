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

Subsequent 14 November verification: Justin rotated the robot 90° by hand;
the near return shifted roughly 100° in raw scanner angle and grew from 282
to 435 mm, identifying an external object rather than fixed robot structure.
With the wheels on the floor, a seven-second trial logged right pivot → Stop →
forward crawl → Stop; Justin confirmed all three happened without contact.
The next bounded trial logged obstacle Stop, turn, forward travel and another
Stop/turn. Justin confirmed the turns, but said the robot did not look close
to walls. Side clearance was still about 118 mm beyond the 290 mm inflated
footprint, so the 150 mm side rule was overly cautious in this room.

The side travel threshold was tuned to 50 mm beyond the inflated footprint.
The controller now steers gently away from a nearer side obstacle while both
wheels drive forward, only when forward clearance exceeds 500 mm. A later
ten-second loaded trial logged an initial moving right curve, then Stop/pivot,
followed by forward travel. Justin still observed the conspicuous stop-turn-go
sequence; the moving curve is subtle at a two-percentage-point wheel difference.
In tight clearance the stop/pivot remains the intended safety behavior. The
ESP32 ended stopped with zero outputs. 120 Python tests passed on the Pi;
source is installed in the Pi package with backups and published as commit
a5896f1abd1b072824ed8b5eda3ec14474d14c3d. The running bridge process
has not been restarted for the last source sync. The private roaming profile
remains `commissioned: false`, and new phone firmware is not flashed. No
continuous floor run or outdoor validation has occurred. Last confirmed motor
power state was ON during the floor trial; switch-off was not confirmed.

Justin later corrected sensor placement: C1 is horizontally centered and about
3.5–4 cm behind the robot front. His illustrative coordinates put front at
`(0, 20 cm)` and lidar at `(0, 16 cm)`; whether `(0,0)` is the drive-wheel
midpoint and the farthest chassis extent are still being checked. Earlier
trials used placeholder `sensor_x=0`, so their clearance estimates are not
fully calibrated. A stationary preview assuming the diagram's origin is the
drive center (`sensor_x=+0.16 m`, radius `0.30 m`, margin `0.06 m`) latched
BLOCKED for an obstacle within the swept footprint. No further motor motion
was commanded after this geometry correction, and continuous mode remains
disabled pending measured geometry.

Dinner pause: Justin estimates about 6 cm from the back of the C1 to the
midpoint between drive wheels. This does not establish the lidar measurement
origin's forward offset, because the C1 housing size and diagram origin were
not specified. The +0.16 m preview above was hypothetical, not final
calibration. The last drive session was stopped/zero; Justin was asked to turn
drive-motor power OFF before leaving. Power-off confirmation remains pending.

Justin then supplied working dimensions: the robot is 30 cm in diameter, so
the farthest body point from the wheel midpoint is 15 cm, and the C1 scan
center is roughly 8 cm forward of that midpoint. This supersedes the old
`sensor_x=0`, `radius=0.23 m` placeholders and the hypothetical +0.16 m pose.
The Pi private profile was updated to `sensor_x=0.08 m`, `sensor_y=0`,
`radius=0.15 m` while the controller was stopped/zero; `commissioned` remains
false and no motor command or stationary scan was run after the update.
Continuous mode remains disabled through dinner.

Later source-only update, 14 November: the new source assigns one Pi bridge
process ownership of the C1 USB port. The roaming runner reads the latest
sweep from its loopback `/lidar/sweep` endpoint. The same raw 72-bin sweep can
be relayed over a separate
Pi-to-ESP32 USB serial link to a new phone LiDAR canvas. The phone page selects
LiDAR by default and retains an optional camera view. This is a live relative
range display, not a saved room map or localization. A missing map USB link
does not interrupt the GPIO control link; invalid or stale C1 data still stops
roaming. This paragraph describes the new source, not a verified phone view or
firmware installation.

The controller source now attempts a slow forward-moving arc when front
clearance narrows, checking the inflated chassis circle along a short family
of straight and curved paths against current scan returns. If a moving arc
cannot be supported, the existing stop/pivot behavior remains. The wheel mix
keeps both wheels forward for a curve; Stop, blocked scans and faults command
zero immediately. CLI `--wall-gap` and optional private-profile `wall_gap` set
front stop and side-steering thresholds, default 300 mm and bounded to
200–400 mm until loaded stopping is measured. The side-steer threshold is the
requested gap minus the unchanged 60 mm footprint margin, while the hard side
stop remains 50 mm beyond the inflated footprint. With Justin's estimated
150 mm radius and 60 mm margin, the inflated circle is 210 mm. The sensor origin is
still an approximate +80 mm from the wheel midpoint. These values have not
been physically calibrated after the geometry correction; a smaller requested
gap does not guarantee that the body will reach it or clean a corner.

At this source checkpoint, 135 Python tests passed locally. In independent
geometry simulations using radius 150 mm, margin 60 mm and sensor x +80 mm,
the wall, chair-leg and moving-obstacle scenarios had no contact. The simulated
wide wall left about 300 mm of physical body clearance at the default gap and
about 200 mm with `--wall-gap 0.20`, with no extra Stop/pivot or contact in that
simulation. These are simulator outcomes, not loaded robot measurements. No
new motion was commanded during this source work.
The new map firmware, USB relay on the Pi, corrected-geometry floor behavior,
loaded stopping distance, sustained room run and outdoor performance remain
unverified at this checkpoint. Continuous mode stays disabled.

Later 14 November installation and physical check: the Pi single-owner C1
bridge and ESP32 LiDAR page were installed. The first ESP32 app flash was
interrupted by the Pi bridge reopening its programming USB port; the app was
restored from a private, locally built image and its flash hash verified. The
Pi bridge was then launched as an unprivileged process because its systemd
service had exited cleanly and requires local sudo to restart. The service
remains inactive, although the manual process serves GPIO control and C1 map
data. Justin refreshed his phone and confirmed live dots/arcs; the first
display felt laggy. Motor power was OFF during both flashes.

Two corrected-geometry, eight-second, 12% floor trials were then supervised.
The first logged a left pivot followed by a moving left curve; Justin saw both
and confirmed no contact. Its initial front-corridor clearance was 0.31 m
beyond the inflated footprint, despite no obvious object straight ahead.
That corridor spans the robot's full width and nearby returns can trigger it.
The second trial used `--wall-gap 0.20` and coupled side-steer clearance to
0.14 m; its log stayed in a moving left curve throughout and ended stopped,
left/right zero. Justin confirmed the smooth curve and no contact, estimating
about 35 cm from the body to a bag of markers at scanner height. That is a
visual estimate, not a measured close-wall stop or a cleaning validation.
135 Python tests passed on the Pi before this second run. Continuous mode and
phone autonomous Start remain uncommissioned.

After Justin switched motor power OFF again, the map relay interval and browser
poll were reduced from 500 to 250 ms and the phone scan styling changed to a
technical instrument layout. The ESP32 target compiled at 950580 program bytes;
the 950736-byte application flash was hash-verified. Actual-sketch host and
embedded-browser checks passed. The Pi manual bridge was relaunched, reporting
ESP32 stopped/zero and a 72-bin C1 sweep. Justin refreshed the final phone
page and said its technical display looks better and updates more smoothly.
Outdoor performance, sustained room operation, loaded braking and
close-wall/corner cleaning remain unverified.
