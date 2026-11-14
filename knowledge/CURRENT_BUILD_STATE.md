# Argus Vac — current physical build

Dinner pause, 2026-11-14: C1 is laterally centered, about 3.5–4 cm behind
the front. Justin estimates 6 cm from the C1 rear to the drive-wheel midpoint.
Exact measurement-origin offset and farthest chassis radius are unverified;
do not use the hypothetical +0.16 m pose as commissioned geometry. Last drive
session stopped/zero; continuous mode disabled; motor power-off was requested
and not yet confirmed. [Evidence](updates/2026-11-14-lidar-floor-commissioning.md).

Latest 2026-11-14: C1 connected to Pi through CP2102; live scans and bounded
floor roaming trials succeeded. Justin confirmed raised-wheel forward and left
pivot directions, a short loaded forward crawl, and a loaded right pivot then
forward motion without contact. Repeated stop-turn-go was observed in the tight
room. Python source is installed; profile remains `commissioned: false`, and
new ESP32 phone Start firmware is unflashed. The last trial ended stopped/zero;
motor power switch-off was not confirmed. Continuous and outdoor operation are
unverified. [Evidence](updates/2026-11-14-lidar-floor-commissioning.md).

2026-11-14: Justin requests C1 autonomous obstacle avoidance tonight and an outdoor showcase tomorrow. Outdoor area may be open, marked with floor tape only; lidar does not see floor tape, so plan supervised runs with Stop available. Justin confirms motor power OFF and Pi/lidar/Ethernet connected; laptop network sharing must be toggled off/on after laptop restart. Pi is reachable but SSH authentication remains unresolved. Lidar roaming prototype implemented and 114 Python, C++ host, browser and ESP32 dummy-config target checks pass; source published commit 6bd87628f51f2fd9345c1af18892e6f21554da92. It is not installed, scanner runner is not live-tested, and robot motion/braking and outdoor coverage remain unverified. See workspace/robot_control/progress/2026-11-14-lidar-roaming.md.


2026-11-14 verified laptop bench test: CP2102 on COM3; C1 identity responds at 460800 8N1 (model 0x41, firmware 1.02). Health status/error both zero before and after a bounded three-second scan. Received 4584 valid nodes, including 4153 positive nonzero-quality ranges at 138.5–3376 mm. STOP sent, subsequent idle stream zero bytes, port closed. Short live ranging passes; sustained power, calibrated accuracy, scan-rate stability, physical standstill and Pi/ROS integration remain unverified. Supersedes earlier unknown communication/function; no robot drive commanded. Evidence: updates/2026-11-14-c1-laptop-bench-test.md.


2026-11-14 follow-up: Justin reports finishing the C1-to-USB-TTL wiring and wants to connect it to his laptop. Interpreted his wording in the context of the CP2102 discussion; exact terminations/soldering, pin mapping, supply capability and working lidar remain unverified. This supersedes wiring-not-yet-reported only. A read-only Windows baseline shows COM13/COM14 Bluetooth and USB Serial Device COM15; none identified as this CP2102. No serial command, scan or motor operation performed.


2026-11-14 direct user update: CP2102 USB-to-TTL module has arrived with five
pins labelled `3v3`, `TXD`, `RXD`, `GND`, `5v`. C1 has four red/yellow/green/black
wires crimped into a user-described JST-XH connector; cavity count and exact
variant unverified. Adapter arrival supersedes November 7 order-pending only.
No installed wiring, repaired sensor or live scan is established. Module UART
voltage and 5 V current capability remain unchecked.
[Evidence](updates/2026-11-14-cp2102-arrival.md).

Latest evidence recovery, 2026-11-10: the later November 9 assisted-manual
prototype is installed on Pi and ESP32, with 103 Python tests passing locally
and on the actual Pi and final application flash-hash verification. Justin
confirmed assisted selection refused a blocked/unavailable view and warned on
the phone; a later paper-covered preview reported CLEAR. The requested actual
object/held-joystick stop result was not recorded. Raised-wheel assisted braking,
loaded obstacle braking, complete 45° tape traversal and untethered floor
operation remain unverified. This supersedes earlier same-day not-installed
and 93-test summaries below.
[Detailed checkpoint](updates/2026-11-10-assisted-checkpoint-and-handbook.md).

Latest dated wiring/power arrangement: ESP32 USB was reconnected to the Pi for
the assisted upload; restoring its bank power afterward is not confirmed.
The three-wire GPIO UART remains the Pi-to-ESP control link. Earlier bank-powered
phone/raised-wheel checks predate this assisted build. Latest explicit motor
power OFF is a November 9 confirmation, not a live November 10 reading. Justin
is at school without the robot today; no hardware connection or new physical
check was made for the handbook. Camera/caster structure remains unchanged.
Older dated checkpoints follow as history.

Final 2026-11-09 checkpoint: phone control is installed,93 Pi software tests
pass, and bank-powered GPIO/raised-wheel checks pass. Floor tests were tethered;
sharp turns improve but stop early. Tape testing ends by assistant choice after
Justin delegates the decision. Last GPIO state is stopped/zero; requested final
motor-power switch-off not yet confirmed. No manual obstacle guard is installed.

2026-11-09 direct user correction: the camera assembly also holds the caster
wheel. Its angle cannot be changed without changing structure. Do not assume
it is an independently adjustable camera mount. Current motor power confirmed
OFF during software-only framing calibration; preserve structure.

Latest commissioning progression 2026-11-09: ESP USB now bank-powered, GPIO
bridge autostarts after Pi reboot; no USB data needed. Both raised wheels move
forward from phone Start and stop from phone Stop. Untethered floor trial pending;
last user confirmation had motor ON with wheels raised. See installation update.

Latest 2026-11-09: Pi online, ESP USB connected to Pi for flashing; motor power
confirmed OFF. Phone Start application now hash-verified on ESP32; 88 tests
pass on Pi and GPIO bridge runs stopped/zero. User phone and physical drive
checks remain pending. See updates/2026-11-09-phone-start-installed.md.

2026-11-09 handoff: Pi and bank are secured on Argus per Justin's confirmation.
Phone Start remains pending ESP32 upload and live commissioning; the updated
Pi modules were copied and bridge stopped. Ethernet is disconnected and Justin
cannot reconnect now. Latest motor-power confirmation was OFF on November 8;
reconfirm before hardware work. See workspace/robot_control/PROJECT-STATUS.md.

Updated 2026-11-08, Asia/Taipei; earlier component evidence retains its dates.
Read this before historical plans, simulator
results or generated CAD. Explicit newer statements supersede older statements.

Justin is assembling the physical chassis and electrical system. As last
confirmed on 2026-10-13, the complete cleaning system and Orange Pi integration
are not installed; the November update does not recheck those components. No CAD, software
test or assistant answer establishes that a physical subsystem is finished.

## Latest bench integration on 2026-11-08

Justin confirms the Orange Pi and its power bank are both secured on Argus,
superseding the 2026-10-13 uninstalled-Pi statement. He requests phone-started
untethered line following. Phone Start is not installed yet; the local client
has an epoch-preserving arm prerequisite and passes 13 targeted checks.

Latest: after the requested USB power move, sixty GPIO state checks pass with
one boot epoch and zero outputs. User confirms motor ON and clear floor path.
The four-second tape-following run steers toward the tape (offset -0.15 to about
-0.09) and stops early on insufficient tape coverage. User observation of the
stop location is pending; sustained power stability is not yet established.

Latest physical test: two-second25% floor run succeeds; user observes moving
along tape and stopping. Requested four-second run fails during arming before
drive requests, with ESP32 reboot/new epoch and further CH340 USB disconnects.
Pi and GPIO bridge remain running. Motor power is now confirmed **OFF**.
ESP32 is powered only by USB; no VIN/5V/3V3 power wire. Separate USB supply
availability is being checked. Sustained power/reset reliability remains open.

Latest power state: motor power **OFF**, Pi/ESP USB power on, confirmed for a
speed-profile upload. Camera mounted on Argus is now user-confirmed. Left-wheel
identity check passed. One-second tethered floor session completes with clear
centered tape, but user reports barely moving and 100% manual speed also slow.
A 25% cruise /35% cap profile is built, uploaded and flash-hash verified;
all83 Pi checks pass. A live GPIO zero-speed handshake returns cap35 and stops
with both outputs zero. Bridge is active with no restarts after this update.
New-profile physical run awaits motor-on readiness. Earlier motor-ON and
pending-floor paragraphs below are historical checkpoints.

Latest physical stage: Justin confirms **motor power ON, wheels raised and
phone Stop ready**. GPIO phone Stop passes after570 zero-speed heartbeats.
The first real one-second5% both-wheel pulse is physically observed forward
and stopped. A two-second live camera-guided run also moves both wheels and
stops, but the user cannot compare speeds. A longer left-only pulse has finished
stopped; wheel-channel observation is pending. No floor-course following has
been validated. Earlier motor-off/pending-movement paragraphs below describe
prior stages; do not use them as current power-state confirmation.

Latest corrected wiring now gives valid GPIO UART replies on ttyS0. Fifty of
fifty read-only requests pass with both outputs zero after Justin reports
moving the ESP ends to GPIO25/26 and restoring USB power. Motor power remains
off; a zero-speed automatic phone Stop check is running. Actual movement is
still untested. This supersedes the pending correction described below.

Latest wire trace resolves a mismatch: Pi8 was connected to the ESP32's plain
RX label and Pi10 to its plain TX label. The firmware expects GPIO25 RX and
GPIO26 TX. Pi-side top-row columns 3/4/5 are confirmed. Pi was shut down again
for moving only the ESP32 ends to 25 and 26; physical correction and GPIO
communication are pending. Motor power remains off; no nonzero command sent.

Latest stage: USB failures blocked both physical pulse attempts before arming.
Justin chooses a direct GPIO serial connection and has three jumper wires.
The ESP32 GPIO RX25/TX26 firmware is uploaded and hash verified. Pi uart0-m2
and ttyS0 are enabled and verified after reboot. Physical Pi8 TX→ESP25,
Pi10 RX←ESP26 and Pi6 GND are the verified pin assignments. The Pi was shut
down for power-disconnected wiring; user confirmation of wiring is pending.
All 83 Pi checks pass. Motor power was confirmed off again. No nonzero motor
command or automatic physical movement has been established.
[Wiring guide](../workspace/robot_control/argus_avoidance/PI-ESP32-WIRING.md).

The Pi's USB cable is connected to the ESP32. New ESP32 manual/automatic
firmware is flash-hash verified and boots stopped. Phone hotspot control is
retained; the Pi uses a single-owner USB bridge at 115200 baud. Fifty read-only
requests pass with camera relaying, and all 83 Python checks pass. Justin has
placed black tape and turned on the light; stationary detection is consistent.
Motor power is confirmed off during upload and the wheels are now raised.
Later USB disconnects persist across reseating and another Pi socket; pausing
phone video permits a 314-heartbeat zero-speed session and a verified phone
Stop. The Pi camera remains full resolution. Wheel direction and physical
automatic floor following are pending at this checkpoint. These bench
observations do not confirm final Pi mounting or cleaning-system installation.
[Evidence](updates/2026-11-08-usb-tape-following.md).

## Earlier confirmation on 2026-11-07

- Justin confirms reliable manual forward/turn/stop via standalone ESP32/Mega.
  The Pi now has a stationary black-tape preview. All 74 Python tests pass on
  the board, including mocked control requests. Actual tape is unavailable
  for a live check at this stage. The new ESP32 draft is pending upload.
  [Current code and demo evidence](updates/2026-11-07-current-manual-code-and-tape-preview.md).

- Justin reports the C1 is faulty and is ordering an adapter. Which part failed
  remains undiagnosed. Candidate manual firmware files have been located on the
  laptop. [Evidence](updates/2026-11-07-c1-replacement-and-manual-sketches.md).

- After Justin unplugged the ESP32, the CH340 disappeared from USB enumeration.
  This suggests the adapter was on that connection. The camera produced live
  640 × 480 frames, and the scan listener received no lidar data in ten seconds.
  [Sensor check](updates/2026-11-07-esp32-unplug-camera.md).

- Later bench check verifies Ethernet/SSH, Ubuntu 22.04.5 ARM64 and ROS 2 Humble.
  Avoidance workspace built and preview-tested on the Pi. USB camera and CH340
  enumerated. BRLTTY claimed the adapter and its serial port disappeared. Justin
  is unsure what is connected to it. No live scans or robot motion were tested.
  [Direct confirmation and board checks](updates/2026-11-07-verified-orange-pi.md).

- Earlier setup confirmation: Justin says **Linux is already installed** on the
  Orange Pi. Distribution/version, boot medium and SSH access remain unknown.
  At intake it was not yet plugged into his laptop; connection has not been
  established. [Intake and confirmation](updates/2026-11-07-orange-pi-setup-intake.md).
- Justin now says the lidar lid **fits**. This resolves the earlier same-day
  fit blocker; fastening, cable clearance during motion and installed lidar pose
  remain unverified. No new dimensions or explanation of the change supplied.
- Current manual control is **Wi-Fi → ESP32 → Mega**. The physical interconnect,
  firmware protocol and automatic/manual arbitration remain unidentified.
- Orange Pi use is a later idea: configure it remotely over SSH, with Ethernet
  connected, using VS Code. Linux installation is now confirmed above; a working
  SSH connection or ROS stack is not established.
- Justin intentionally deleted the old simulator and permits a small alternative.
  New standalone Python tests do not establish physical or live ROS validation.

Evidence: [latest direct messages](updates/2026-11-07-lid-fits-and-control-path.md).

## Earlier 2026-11-07 fit blocker — superseded for fit

- The lid carrying the lidar **is still not fitted**. Excess wiring makes the
  robot too tall for the clearance provided by the current spacers; Justin
  identifies this as the primary reason the lid remains off.
- No new spacer length or wiring height was supplied. The earlier 60–70 mm
  range remains dated evidence. No other component installation change or
  wiring fault is established by this update.
- This was the earlier reason physical mounting could not proceed. The later
  message resolves fit; secure mounting and the installed pose still need checking.

Evidence: [direct user update](updates/2026-11-07-lidar-lid-wiring-clearance.md).
This reconfirms October's detached-lid state and adds its current cause; it
supersedes any assumption of subsequent lid installation.

## Confirmed by Justin on 2026-10-13

- The lid shown beside the main robot carries the RPLIDAR C1. Model the detached
  lid separately in the present-build scene; assembly onto the chassis is a
  separate proposed state.
- San Ace suction motors, N12 12 V brush motors, their respective drivers and
  the Orange Pi 5 are **not installed**. They belong only in a proposed completed
  layout until Justin confirms installation.
- Justin calls the brush motors **N12 12 V**. Older notes say N20; do not silently
  substitute one for the other. Exact models and counts require evidence.
- The red item is the adapter for Justin's **M12 3 Ah battery**. The older
  adapter-pending statement is superseded. This does not prove protection or
  battery wiring has been commissioned.
- Chassis and lid plates have stated **300 × 300 mm bounds**, a **circular outline
  visible in the photos**, and **3 mm acrylic thickness**, from Justin's latest
  correction. This supersedes his earlier10mm statement/reconfirmation. Three
  metal spacers in a triangle separate them, lengths **60–70 mm**. Do not
  substitute old generated4mm plates/four spacers or claim65mm was measured.
- Present problems: components slide off, weight is unbalanced, and messy wiring
  leaves insufficient usable space.
- Requested outputs: CAD matching the present robot, plus a proposed completed
  wiring/layout version informed by photos, recent chats and an outdated Fritzing.
- Justin has supplied photos in ChatGPT Library and permits internet searches
  for exact component sizes, weights and dimensions.

Evidence: [direct user update](updates/2026-10-13-current-build-user.md),
[latest thickness correction](updates/2026-10-13-plate-thickness-correction.md).
All seven supplied Library photos are archived with readable names under source
family `current-build-photos`; [photo catalog](../workspace/exports/cad-reference/photo-evidence.json).

## Recent bench chat adds context

In **Clarify Microstepping Setting**, Justin states a4:1 gearbox is already used
and only one TB was wired in that dated session. He suspects the old right driver
is short/broken. A pasted Mega flashing log reports successful upload of manual
control firmware. This does not confirm both present drivers work or establish
the present sketch/pin map. [Retrieved direct-user evidence](updates/recent-microstepping-chat-2026-10-13.json).

## Earlier confirmed design facts still applicable

- Arduino Mega 2560, two NEMA 17 motors beneath the chassis, two TB6600 drivers,
  70 mm diameter wheels, USB camera, Orange Pi 5 planned main computer, RPLIDAR C1.
  Evidence: October robotics chat `2dda853c7eb12414d740`.
- Justin described a barebones TB6600 board with blue current potentiometer and
  a 1.7 A NEMA 17. Exact variant/interface unverified. Evidence: 2026-10-10 chat
  `5ff50638ee53f122f835`.

## Evidence limits and pending details

The old Fritzing and A4988 sketches describe a historical wiring branch. Recent
physical evidence takes priority; old connection labels and proposed CRC pin maps
must not be presented as measured present wiring. Wire routes in completed CAD
are proposals unless their endpoints have been positively identified.

Component positions reconstructed from photos are estimates until measured.
Manufacturer dimensions apply only to the matched model; generic housings,
adapter shapes, heatsinks and clone boards need their own identification.

See [project memory](PROJECT_MEMORY.md) and [open questions](OPEN_QUESTIONS.md) for
dated references. Preserve the raw archive; use readable display names and
explicit statuses to distinguish current physical facts, historical records and
proposals.
