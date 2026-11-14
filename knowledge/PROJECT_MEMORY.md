# Argus Vac — project memory

Latest 2026-11-14 floor checkpoint: C1 live on Pi; Python roaming source is
installed, the private profile stays uncommissioned, and the new ESP32 phone
firmware is unflashed. Justin confirmed a loaded right pivot then forward crawl
without contact, and observed repeated stop-turn-go in the cramped room. A
moving curve was added for clearer paths; continuous floor and outdoor runs
remain untested. 120 Python tests passed on Pi. The earlier same-day paragraph
below predates this checkpoint. [Dated evidence](updates/2026-11-14-lidar-floor-commissioning.md).

2026-11-14: Justin requests C1 autonomous obstacle avoidance tonight and an outdoor showcase tomorrow. Outdoor area may be open, marked with floor tape only; lidar does not see floor tape, so plan supervised runs with Stop available. Justin confirms motor power OFF and Pi/lidar/Ethernet connected; laptop network sharing must be toggled off/on after laptop restart. Pi is reachable but SSH authentication remains unresolved. Lidar roaming prototype implemented and 114 Python, C++ host, browser and ESP32 dummy-config target checks pass; source published commit 6bd87628f51f2fd9345c1af18892e6f21554da92. It is not installed, scanner runner is not live-tested, and robot motion/braking and outdoor coverage remain unverified. See workspace/robot_control/progress/2026-11-14-lidar-roaming.md.


2026-11-14 verified laptop bench test: CP2102 on COM3; C1 identity responds at 460800 8N1 (model 0x41, firmware 1.02). Health status/error both zero before and after a bounded three-second scan. Received 4584 valid nodes, including 4153 positive nonzero-quality ranges at 138.5–3376 mm. STOP sent, subsequent idle stream zero bytes, port closed. Short live ranging passes; sustained power, calibrated accuracy, scan-rate stability, physical standstill and Pi/ROS integration remain unverified. Supersedes earlier unknown communication/function; no robot drive commanded. Evidence: updates/2026-11-14-c1-laptop-bench-test.md.


2026-11-14 follow-up: Justin reports finishing the C1-to-USB-TTL wiring and wants to connect it to his laptop. Interpreted his wording in the context of the CP2102 discussion; exact terminations/soldering, pin mapping, supply capability and working lidar remain unverified. This supersedes wiring-not-yet-reported only. A read-only Windows baseline shows COM13/COM14 Bluetooth and USB Serial Device COM15; none identified as this CP2102. No serial command, scan or motor operation performed.


Latest hardware update, 2026-11-14: Justin's five-pin CP2102 USB-to-TTL module
has arrived, labelled `3v3`, `TXD`, `RXD`, `GND`, `5v`. His C1 has red/yellow/
green/black wires crimped into a user-described JST-XH connector. This supersedes
the November 7 adapter-order-pending status only; exact module/connector,
power capability, wiring, fault diagnosis and live lidar operation remain
unverified. [Arrival evidence](updates/2026-11-14-cp2102-arrival.md).

Latest learning context, 2026-11-10: Justin finds the handbook overwhelming.
He reports barely knowing Linux/Python, some C++, and understanding Arduino
code. He clarifies that basic boolean/if/else examples are already familiar
and too simple. Teach real Argus command/program/file flow with Arduino/C++
comparisons, using the handbook as a reference. Do not equate unfamiliar
Linux/Python tooling with unfamiliar programming logic. No broader proficiency
or lesson completion inferred.
Justin also explicitly requests code alongside teaching: show small actual
source excerpts with filenames/language and explain how they run.
[Learning baseline](updates/2026-11-10-learning-baseline.md).

Latest recovered checkpoint, 2026-11-10: the later November 9 camera-assisted
manual prototype **was installed**, superseding the earlier same-day
not-installed/93-test summaries below. 103 Python tests passed locally and on
the actual Pi; final 941568-byte ESP application was flash-hash verified.
Justin confirmed the real phone's assisted-drive refusal/warning on a blocked
view; a paper-covered preview later reported CLEAR. Actual-camera held-joystick
object-stop, raised-wheel assisted stopping and loaded braking remain pending.
No complete 45° tape corner or untethered floor trial is established.
[Recovered evidence and limits](updates/2026-11-10-assisted-checkpoint-and-handbook.md).

Latest dated arrangement: ESP USB was reconnected to the Pi for the assisted
upload; restoring bank power afterward is unconfirmed. GPIO remains the control
link. Last motor-power OFF confirmation is from November 9, not a live November
10 state. Today Justin is at school without Argus; no hardware access was used.
He requests an organized reproduction/learning folder with exact recovered Pi
commands, source files, human steps and Linux/ROS explanations. Completed at
[workspace/argus-handbook](../workspace/argus-handbook/README.md): 93 packaged
files including 74 reviewed source files, a command ledger and hash inventory.
Published to GitHub main in f8af59b, with dashboard fallback refresh3f4c25f.
Offline checks:103 Python tests, C++/browser checks, ESP32 example-config
target compile and dashboard browser checks pass. ZIP is in workspace/exports.
Preserve unknown initial-install history
and the unverified exact installed Mega sketch rather than inventing them.

Earlier dated checkpoints follow; newer evidence above supersedes their
pending-installation and power-state claims.

Latest outcome 2026-11-09: Phone Start installed and working; bank-powered GPIO
and raised-wheel Start/Stop pass.93 software tests pass on actual Pi after
fixed-view framing and tighter-turn changes. Tethered floor turns improve but
still stop on insufficient/dark tape view; no completed sharp-corner or untethered
run. User delegates stopping tape tests; we stop here and prioritize manual
camera warning/braking (not yet installed). Final controller state stopped/zero;
physical motor power OFF requested, not yet confirmed. Current report:
[corner checks](../workspace/robot_control/argus_avoidance/reports/CORNER-CHECK.md).

Latest intent/constraint, 2026-11-09: Justin reiterates the main goal is manual
driving with camera obstacle warning and automatic stop. Line following is a
demo; obstacle detours are not the immediate priority. That manual protection
is not installed. He also confirms the camera assembly serves as the caster
holder, so its angle cannot be changed without structural changes. Keep the
45° tape course per his preference and work within the fixed camera view.

Phone commissioning progression, 2026-11-09: actual phone Start/Stop and
phone-lock stop pass with motor power off. User restores ESP USB power to bank;
Pi services start automatically and GPIO works without USB data. Raised-wheel
phone Start makes both wheels move forward and Stop zeros outputs. An untethered
floor trial is requested; outcome pending. See the installation evidence below.

Latest robot commissioning, 2026-11-09: user reconnects Pi/ESP and confirms
motor power OFF. Phone Start firmware is now uploaded and data-hash verified;
all 88 tests pass on the actual Pi. GPIO bridge restarted; 30 state checks
are stopped/zero with one boot epoch. Fresh camera view initially too broadly
dark for tape detection. Real phone Start/Stop and untethered checks pending.
This supersedes earlier upload/disconnected status. [Installation evidence](updates/2026-11-09-phone-start-installed.md).

2026-11-09 archive publication: Justin requests all available project docs,
Gemini/Obsidian chats and images in the dashboard. Published a sanitized archive
accounting for 1,449 original records plus 39 current notes; includes three saved
Gemini-model chats and 55 images/diagrams. Complete Gemini-app history remains
unavailable. See [public archive handoff](updates/2026-11-09-public-documentation-archive.md).

Dashboard style preference, 2026-11-09: Justin asks for it to look less AI.
Revised to a plain project notebook: system fonts, flatter file browser and one
dated progress note; removed marketing slogans, milestone cards and badges.
Published commit 1a1a2a979606716be0a5a10cf918dcbb13a72e72; browser checks pass.

2026-11-09 dashboard: Justin requests replacing the old Onshape site with a
formatted repository browser and file explanations. Source is workspace/dashboard;
published commit 19637658bc0318a98e04bc75c876d4a948e5cf5b. Future repository files
are discovered dynamically; milestone cards remain dated/manual. See
[dashboard update](updates/2026-11-09-file-dashboard.md).

Latest status 2026-11-09: Justin selected `minesoil/Argus.vac-manual` for code
and documentation logging. Phone Start is implemented and locally tested
(88 Python tests plus C++/browser checks); ESP32 upload and live checks remain
pending. New Pi modules were copied and bridge service stopped on November 8;
the attempted Pi test used a missing interpreter. Ethernet is disconnected and
Justin cannot reconnect now. This supersedes the earlier design-only status.
After tape following he wants camera obstacle warning/stop, then avoidance.
See [current software status](../workspace/robot_control/PROJECT-STATUS.md).

Compiled 2026-10-10, Asia/Taipei. This is a source-backed snapshot, not a live
hardware inventory. Later confirmed updates should replace individual facts while
preserving their history in [DECISIONS.md](DECISIONS.md).

**Latest untethered request, 2026-11-08:** Justin wants to start the line
follower from his phone without the laptop tether. He confirms the Orange Pi
and its power bank are both secured on Argus, superseding the October uninstalled
Pi status. [Phone-start design](../workspace/robot_control/argus_avoidance/PHONE-START-DESIGN.md)
is prepared; the phone button and supervisor are not yet installed. The local
Pi client now supports preserving a captured start epoch; 13 client tests pass.

**Earlier GPIO check, 2026-11-08:** Justin reports correcting the ESP32 ends to
GPIO25/26. Camera is confirmed mounted on Argus and aimed at the tape. The
left-only physical check passed. A first one-second tethered floor session
completed with fresh centered tape readings; Justin says it barely moved and
that even 100% manual speed is slow. Motor power is now confirmed **OFF** for
an updated 25% cruise / 35% cap profile. Target build and actual-sketch host
checks pass, as do all83 Pi checks. Paired firmware is now uploaded and hash
verified; GPIO state reports cap35 and a zero-speed handshake finishes stopped
with zero outputs. A real two-second25% floor run succeeds: Justin observes
forward movement along the tape and stopping. His requested four-second run
fails during arming (503); ESP32 state shows a new boot epoch and Start stopped,
while Pi logs more USB disconnects. Motor power is confirmed OFF again. ESP32
is confirmed powered only by USB. Justin confirms a USB power bank already
powers Mega and Pi. The Pi is shut down for moving ESP USB power from the Pi
to a free5V output on that bank, keeping GPIO control unchanged. That physical
change was requested and Justin reports it is powered back on. The Pi is online
and GPIO state responds stopped with zero outputs; 60 read-only requests share
one boot epoch and all return zero outputs. This is a short stability check;
the requested four-second ground run subsequently starts and steers toward the
tape, with offset improving from -0.15 to about -0.09. It stops early when tape
visibility becomes uncertain. Justin observes about12 cm of tape remained ahead;
camera angle and software crop also affect visibility, so this does not establish
the physical blind-spot length. He wants a noticeable demo for his dad today and
reiterates lidar mapping/distance and camera floor-obstacle recognition goals.

**Earlier GPIO check:** Justin reports correcting the ESP32 ends to
GPIO25/26 and restoring USB power. The Pi now receives valid firmware replies
on `/dev/ttyS0`; all 50 read-only requests passed with both outputs zero. A
real zero-speed GPIO session completed 570 heartbeats and ended on the phone's
Operator Stop, revoking the old session with both outputs zero. Justin confirms
AUTO→Stop→STOPPED. He then confirms motor power on, wheels raised and Stop ready.
A one-second 5% both-wheel pulse completes; Justin observes both wheels forward
and stopped. A two-second live camera follower also moves both wheels and stops;
he cannot compare their speeds. Justin now observes the three-second left-only
5% pulse: left wheel only, forward, then stopped. This resolves the left-channel
identity check. Camera mounting and floor-course following remain unverified.

**Earlier camera integration, 2026-11-08:** the new ESP32 firmware is uploaded
with a separate GPIO UART input (ESP32 RX25/TX26). After persistent USB faults,
Justin chooses to keep control on the Pi and confirms three jumper wires.
Pi `uart0-m2` is enabled and `/dev/ttyS0` verified after reboot. Actual board
pin map is **physical 8 TX, 10 RX, 6 GND**. The GPIO firmware upload is hash
verified; bridge configuration targets ttyS0. Justin now reports connecting
the jumpers. Latest trace confirms Pi8 goes to the ESP32's plain RX label and
Pi10 to its plain TX label, rather than the configured GPIO25 and GPIO26.
The Pi is shut down again so only those ESP32 ends can be moved: RX-labelled
wire to GPIO25, TX-labelled wire to GPIO26; Pi ends and GND stay as placed.
GPIO communication and wheel tests remain pending. No nonzero
wheel command has been sent: both attempted pulse checks failed before arming.
[Wiring guide](../workspace/robot_control/argus_avoidance/PI-ESP32-WIRING.md).

**Earlier same-day USB integration:** the new ESP32 firmware was uploaded
and flash-hash verified. The Pi now uses the existing USB cable for automatic
control; Justin's phone remains on the ESP32 hotspot. The CH340 is identified,
BRLTTY conflict addressed, and all 50 read-only checks pass at 115200 baud with
camera relay. All 83 Pi Python checks pass. The real lit black tape is detected
consistently, slightly left. A longer run exposed USB disconnects and bridge
restarts. Reseating and another Pi socket did not resolve them. With phone video
relay paused, a real zero-speed session accepted 314 heartbeats and ended on
Justin's **Operator stop**, with zero outputs and the old session rejected.
The Pi still reads the full camera image. Justin confirms wheels raised and
motor power off; physical steering remains pending.
[Live integration evidence](updates/2026-11-08-usb-tape-following.md).

**Earlier driving/demo update, 2026-11-07:** Justin confirms reliable standalone
ESP32/Mega driving, turns and stop. Recent chats identify the joystick/camera
code family and October 28 editable draft. Black tape on a light floor is his
selected first camera course. The Pi passed 74 Python checks and the live
stationary preview reported STOP without tape. A separate ESP32 automatic-mode
draft and Pi client are prepared. Physical tape testing and firmware upload
remain pending. [Evidence](updates/2026-11-07-current-manual-code-and-tape-preview.md).

**Earlier 2026-11-07:** Justin reports a C1 fault and is ordering an adapter.
The failed component is unknown. Local ESP32 and Mega manual-control sketch
candidates were found in his Arduino sketchbook. Their shared wheel-percent
protocol and timeouts can be examined offline; flashed versions remain unknown.
[Report and source paths](updates/2026-11-07-c1-replacement-and-manual-sketches.md).

**USB check, 2026-11-07:** after Justin unplugged the ESP32, the CH340
disappeared. This points to the ESP32 connection. Two different live camera
JPEGs were received at 640 × 480. No live lidar scan arrived in ten seconds.
[Evidence](updates/2026-11-07-esp32-unplug-camera.md).

**Earlier bench setup, 2026-11-07:** Ethernet and SSH to `orangepi5` are verified.
Ubuntu 22.04.5 ARM64, Python 3.10.12 and ROS 2 Humble are installed. The
regular-user project is `/home/orangepi/argus/avoidance`. The board passed 44
checks and a live ROS preview with synthetic scans and zero output. A live
lidar scan is pending identification of a CH340 adapter claimed by BRLTTY.
[Setup evidence](updates/2026-11-07-verified-orange-pi.md) and
[beginner guide](../workspace/robot_control/argus_avoidance/START-HERE.md).

**Earlier stages, 2026-11-07:** after requesting a plan, Justin said "keep going".
Later he asks for assisted Orange Pi setup while connecting it to his laptop;
it is **not yet plugged in** at that intake. He subsequently confirms **Linux is
already installed**; distribution/version, boot medium, network and SSH access
remain unknown. A reflash is not an assumed prerequisite.
[Setup intake and confirmation](updates/2026-11-07-orange-pi-setup-intake.md).

The [first avoidance package](../workspace/robot_control/argus_avoidance/README.md)
now contains a pure Python controller, small 2D test environment and optional ROS
adapter with output disabled. **44 offline tests and nine modeled scenarios pass**;
this does not establish ROS, sensor, firmware or physical validation. See the
[verification scope](../workspace/robot_control/argus_avoidance/reports/VERIFICATION.md).
Justin intentionally deleted the old simulator and accepts a small alternative;
do not assume the historical WSL/Gazebo environment remains usable.

**Latest physical/control update, 2026-11-07:** the lidar lid **now fits**, which
supersedes the earlier same-day wiring-height fit blocker. Fastening, dimensions
and installed sensor pose remain unconfirmed. Justin currently controls Argus
manually over **Wi-Fi → ESP32 → Mega**. He is considering the Orange Pi later,
initially configured over Ethernet/SSH using VS Code. Neither an installed Pi
control stack nor the newer CRC motor protocol is established. The new package
does not intercept the present ESP32 path; firmware/source arbitration is still
needed before physical automatic control.
[Direct evidence](updates/2026-11-07-lid-fits-and-control-path.md).

**Other physical-stage evidence, dated 2026-10-13:** read
[CURRENT_BUILD_STATE.md](CURRENT_BUILD_STATE.md) first for installed versus planned
components. Justin has not installed the Orange Pi 5, San Ace suction motors,
N12 12 V brush motors or their drivers. The C1 is on the separate lid. The red
item is his M12 3 Ah adapter. These direct statements supersede older assumptions.

Justin is building an autonomous vacuum robot. The aim is room mapping and
navigation with lidar, plus camera-based avoidance of floor obstacles such as
socks and cables. An Orange Pi runs the high-level software; an Arduino controls
the actuators. The project has earlier names/concepts recorded as AIVac.

## Latest confirmed hardware and design

2026-10-13: Justin requested both a close reconstruction of the present robot and
a proposed completed wiring/layout version. Seven Library photos are now archived
in the [photo evidence catalog](../workspace/exports/cad-reference/photo-evidence.json).
His chassis dimensions and spacer count below replace older generated CAD estimates;
component positions reconstructed from photos still need measurements. See the
[initial request](CAD_RECONSTRUCTION.md) and [current update](updates/2026-10-13-current-build-user.md).

2026-10-13 draft delivery: the [current robot draft](../workspace/designs/argus-as-built-v1.json)
and [completed-layout proposal](../workspace/designs/argus-complete-layout-v1.json)
are saved as editable CAD. Workshop now opens the current draft by default; the
original estimate is preserved as [legacy-layout-estimate.json](../workspace/designs/legacy-layout-estimate.json)
and in revision history. [Export notes](../workspace/exports/cad-reconstruction-v1/README.md)
describe layout-only exports and software checks. Exact geometry, component
envelopes, mounting fit, measured balance and terminal wiring remain unverified.

| Item | Best available evidence / status |
|---|---|
| Main computer | Orange Pi 5, **not installed**, confirmed 2026-10-13. Older raw notes specify 8 GB and no onboard Wi-Fi/Bluetooth module. |
| Microcontroller | Arduino Mega 2560. |
| Sensors | RPLIDAR C1 carried by the lid; **lid now fits**, latest confirmation 2026-11-07, superseding the earlier same-day fit blocker. Fastening and measured pose unconfirmed. USB camera reported mounted in earlier physical notes; CAD placement is estimated from archived photos. |
| Drive | Two NEMA 17 motors under the chassis, one TB6600 per motor, wheels **70 mm in diameter**. Explicitly confirmed in the October robotics chat. |
| Driver variant | On 2026-10-10 Justin asked about a **barebones TB6600 with a blue current potentiometer** and said the NEMA 17 is rated **1.7 A**. Exact board identification/control interface was not confirmed in the recovered text. |
| Chassis | Circular acrylic plates visible in new photos, stated **300 × 300 mm bounds** and latest corrected thickness **3 mm**; **three metal spacers in a triangle**, lengths **60–70 mm**. Latest2026-10-13 correction supersedes earlier10mm and generated4mm/four-spacer estimates. Exact spacer length remains open. |
| Cleaning hardware | Justin confirms **San Ace suction motors, N12 12 V brush motors and their drivers are not installed** on 2026-10-13. Older records say San Ace 40, dust bag, two N20 motors, L298N and IBT-2 proposal; exact current models/counts/driver selection remain unverified. |
| Power | Justin identifies the red item as the **adapter for his M12 3 Ah battery** on 2026-10-13, superseding September's adapter-pending state. Exact pack/adapter variant and final protection/wiring/commissioning are not established. |
| Wiring materials | Justin settled on 10 A blade fuses and 12 AWG inline holders in August. September's **14 AWG adapter leads** are a separate item; they do not revise the holder specification. Actual fuse choice should be reassessed for any changed power system. |

Primary references: [raw user notes](text/87b42cf22476245ab36c--ROBOT_MASTER.md.md),
[October robotics chat](text/2dda853c7eb12414d740--conversation.md.md),
[latest TB6600 discussion](text/5ff50638ee53f122f835--conversation.md.md),
[battery discussion](text/1f68beb4fd47998232dd--conversation.md.md),
[historical hardware manual](text/77e307eb5d96605d25c4--Argus%20Vac%20-%20Hardware%20_%20Mechanical%20Architecture%20Manual.md.md).

## Software branches and interfaces

2026-11-07 current manual route is Wi-Fi → ESP32 → Mega. Its firmware, protocol
and command arbitration are not recovered in the targeted archive/source search.
The separately written [avoidance package](../workspace/robot_control/argus_avoidance/README.md)
is offline-tested software for future integration, not deployed avoidance.

Recent direct-user bench chat retrieved2026-10-13 confirms a stated4:1 gearbox,
only one TB wired at that session, and suspicion that the old right driver was
shorted. A pasted log reports successful manual-control firmware upload. Exact
present pin map and successful two-driver commissioning remain unverified; this
does not establish deployment of the newer CRC firmware.
[User-message evidence](updates/recent-microstepping-chat-2026-10-13.json).

The Obsidian branch contains `obstacle-detector-mediapipe-v10.6.py`: MediaPipe
EfficientDet-Lite2, a training-free unknown-obstacle layer, decoupled capture /
inference / rendering / statistics, and a dashboard/MJPEG feed on port 8000.
Its documented detector input is native 640 × 480. Proximity gating applies to
both known and unknown objects; static unknown objects can be suppressed after
60 seconds. The stored desktop benchmark does not establish mounted-camera
performance on the Orange Pi. Serial output is disabled by default.

The historical `mega-controller.ino` and validator use letter commands
`P/S/B/V/H/G` plus `R` threat packets at 115200 baud. That firmware was described
as a draft, not confirmed as flashed. Historical A4988 pin maps include left
STEP 5 / DIR 6, right STEP 3 / DIR 4, and a reported dead Mega pin 2. Some old fan
maps also use pin 2, an unresolved inconsistency. Preserve those records for
diagnosis; do not treat them as the present TB6600 wiring.

The newer `RobotLab` branch separates the Windows desktop app, 3D robot designer,
saved designs, ROS packages, Mega firmware, deployment tools and tests. It has:

- Simulator: ROS 2 Jazzy/Gazebo in WSL distribution `VacuumRobot-24.04`, with live
  workspace `/home/robot/vacuum_ws`. Camera, differential drive, mapping/navigation,
  furnished world, and Honeycomb Alpha/yoke control appear in the records.
- Designer: add/move/rotate parts, exact dimensions, undo/redo, STL import and
  saved design revisions. Default design lives in `designs/default.json`.
- Hardware path: `/cmd_vel_raw` → collision monitor → `/cmd_vel` → Orange Pi
  motor bridge → USB → Mega → wheel drivers.
- Firmware protocol: newline ASCII `V1,...,CRC` commands and `S1,...,CRC`
  telemetry using CRC-16/CCITT-FALSE. It is incompatible with the legacy
  letter-command protocol. Pair firmware and bridge from the same branch.
- Supplied module wiring/configuration: Mega D22/D23 STEP, D24/D25 DIR, optional
  D26 ENA, D27 stop loop. Defaults assume a common-anode driver module. This is
  **a software wiring proposal**, not verification of Justin's barebones board.
- Physical defaults: 0.035 m wheel radius, estimated 0.22 m separation, 200 full
  steps × 8 microsteps, motion disabled, 0.15 m/s forward and 0.08 m/s reverse.
  Defaults need matching measurements and actual driver configuration.
- Software safety: neutral arming handshake, command freshness checks, serial
  and lidar failure handling, and a 350 ms firmware command watchdog. Issued-step
  odometry is open loop; it cannot detect missed steps or wheel slip.

See [RobotLab overview](text/c646a0a5dbae397b6f75--README.md.md),
[interface reference](text/1c00e63e2dbdf342de4b--architecture.md.md),
[hardware guide](text/8d2072f762edb271d396--hardware.md.md), and
[Orange Pi deployment guide](text/d4cfba56e203be99305b--orange-pi.md.md).

## Simulator settings and verification

Justin confirmed a 16 × 12 m room and 1.5 m/s forward simulation limit. Driving
can arm once; centring the yoke stops movement. Prior reports measured roughly
61 camera FPS and 0.34 seconds to reach 90% of forward speed, with motion,
directional obstacle escape, navigation/map saving and shutdown tests.

Those are historical simulator measurements. Collection did not rerun the
simulation, flash the Mega, or test the physical robot. The later RobotLab guide
describes compilation/host-harness/fake-serial testing, but its referenced
`reports/quality-review.json` was absent from the collected folder. The last
robotics chat's cleanup/designer work has no recovered final completion answer.
Treat that audit as unfinished until a final report and current checks exist.

## Mechanics and failure history

The wheel-shaft work started from `planetary-gearbox-+slim.shapr`. Earlier printed
shafts broke where the thick body met the thin neck. Justin has PLA and said the
newer variant had not yet been printed at that point. The latest saved variant
uses a direct wheel hex, captive M3 nut pocket, uniform 13 mm lower/middle body,
5.6 mm bottom bore, and 40 mm from mounting-base top to hex tip. The hex was
specified as 11.8 mm across flats and 5.8 mm long. Two copies are arranged side
by side. Real fit, M3 screw engagement and loaded strength remain unverified.

Historical electrical issues include a reported dead Mega pin 2, a swapped
A4988 VMOT/VDD connection, camera disconnects improved after moving USB ports,
and A4988 MS1-to-ground readings consistent with a very low resistance path.
October A4988 bench work used quarter stepping to avoid driving MS1 high;
that workaround did not establish repair of the short. Battery failures and
a charger showing only two cells are also recorded. These are dated incident
records, not proof that the current hardware still has every old fault.

See [shaft chat](text/a67e6567414fd102db4a--conversation.md.md),
[A4988 bench status](text/0a7d338063f0650b815d--WIRING_STATUS.md.md), and
[troubleshooting history](text/83b9aac5e26a584d4765--argus-vac-historical-troubleshooting-log-v4.6.md.md).

## Justin's working preferences

Keep code clearly separated by component, and make transfer to the Orange Pi
straightforward. Write direct, useful documentation without AI filler. Preserve
his raw notes in his voice. Search past records before asking him to repeat
details. Benchmark performance claims rather than adopting plausible optimizations
without measurements. Older preferences use decimal version bumps for small
changes and new whole-number files only for major rewrites; keep history.

Use [TOPICS.md](TOPICS.md) for retrieval, [OPEN_QUESTIONS.md](OPEN_QUESTIONS.md) for
unresolved facts, and [COVERAGE.md](COVERAGE.md) before claiming completeness.

<!-- WORKSHOP_NOTES_START -->
## Dated Workshop notes

Read these notes alongside the source-backed snapshot above. Only an explicit newer claim supersedes an older claim. [All Workshop notes](../workspace/notes/INDEX.md).

- 2026-10-11: [Argus Workshop purpose and collection scope](../workspace/notes/note_f91a410c8fcc.md)
<!-- WORKSHOP_NOTES_END -->
