# Argus Vac decisions and chronology

2026-11-09 — Justin requests a less AI-looking dashboard. Prefer a restrained,
practical notebook style with direct labels over slogans and decorative cards.
Implemented and published as 1a1a2a979606716be0a5a10cf918dcbb13a72e72.

2026-11-09 — Replace the Onshape guide at the GitHub Pages root with the Argus
file dashboard, per Justin. Preserve old content in Git history. Auto-discover
new files and label generic explanations and dated milestone snapshots.

2026-11-09 — Justin requests GitHub records for code and documentation and
selects minesoil/Argus.vac-manual. Exclude credentials and private raw archives.
After the tape demo, prioritize camera obstacle warning/stop; steering detours
require verified clearance. Phone Start local tests pass, installation incomplete
because Ethernet is unavailable. See workspace/robot_control/PROJECT-STATUS.md.

Dates below describe the evidence, not a guarantee of physical implementation.

| Date / period | Change or milestone | How to interpret it |
|---|---|---|
| February–May 2026 | Early Arduino/AIVac material; circular Raspberry Pi 4, Pi camera and RPLIDAR A1 concepts. | Historical designs and budgets; superseded hardware concepts. |
| May 2026 | AIVac build specification, CAD modules, material-cost document and component order. | Preserve original dimensions/costs as dated plans; later revisions differ. |
| June 2026 | ArgusVac Roboflow model training notifications. | Provider-reported training metrics; no claim of current deployment or real-world accuracy. |
| July 2026 | Portfolio/FRC/science-fair/vacuum presentations describe the evolving project. | Mixed-topic documents preserved whole because they contain project history. |
| August 2026 | Obsidian manuals, Fritzing wiring, legacy letter protocol and MediaPipe detector development. | Historical implementation branch; retain for troubleshooting and perception work. |
| 2026-08-25 | 10 A fuse / 12 AWG inline-holder preference; native 640×480 inference; decimal versioning. | Preserve dated preference and supporting benchmarks. |
| 2026-08-29 | Dead Mega pin 2 reported; historical left A4988 pins moved to STEP 5 / DIR 6. | Applies to that wiring branch; physical condition was not rechecked during collection. |
| 2026-09-27 | NEMAs moved beneath chassis, camera/lidar mounted, most parts arrived, power-tool battery adapter pending. | Latest physical-status update in the vault; supersedes earlier missing-parts lists and between-plate motor mounting. |
| 2026-09-30 onward | ROS 2/Gazebo workstation setup and GUI driving/navigation. | Desktop simulation development, separate from commissioning the robot. |
| 2026-10-03 | A4988 bench diagnostics and low-speed/noise work; low resistance at MS1 remains unresolved. | Historical A4988 work. Keep its firmware and pin assignments separate from TB6600 code. |
| 2026-10-05 | Wheel shaft variants; final recorded direct-hex/M3/40 mm/uniform-13 mm geometry. | CAD geometry checks reported; physical strength and fit remain open. |
| 2026-10-07–08 | User confirms two TB6600s, two NEMA 17s, 70 mm wheels; 16×12 m world, 1.5 m/s simulation; RobotLab designer and separate hardware package. | Supersedes A4988 as the stated current drive design and old 6 cm bench-wheel assumptions. |
| 2026-10-10 | Barebones TB6600/current-pot discussion; user says motor rating is 1.7 A. | Exact driver variant remains unidentified in text; do not assume the optocoupled module used by the generated hardware guide. |
| 2026-10-10 | This archive compiled, deduplicated and verified. | Snapshot and retrieval infrastructure; no new robot validation implied. |
| 2026-10-13 | Justin requests CAD matching his current physical robot and offers photos from requested angles. [Direct-message evidence](CAD_RECONSTRUCTION.md). | Sets the reconstruction objective; does not supersede confirmed hardware facts. Current photos and scale measurements are pending, and existing CAD estimates are unverified. |
| 2026-10-13, later update | Justin supplies current build stage, Library photos, M12 3 Ah adapter identity, 300 × 300 × 10 mm plates and three triangularly arranged 60–70 mm spacers; requests a completed wiring version and identifies slipping, balance and space issues. [Direct evidence](updates/2026-10-13-current-build-user.md). | Supersedes adapter-pending and installed-computer/cleaning assumptions, and generated chassis/spacer dimensions. C1 is on the detached lid; Orange Pi 5, San Ace/N12 motors and their drivers are uninstalled. Exact models, coordinates and electrical commissioning remain unverified. |
| 2026-10-13, latest correction | Justin corrects acrylic thickness to **3 mm**: “wait nvm the board is 3 mm!!”. [Direct correction](updates/2026-10-13-plate-thickness-correction.md). | Supersedes his earlier10mm statement and reconfirmation. Photos show circular plates;300 ×300 mm describes stated bounds. Exact spacer length remains60–70 mm. |
| 2026-10-13, draft delivery | Saved an editable [current robot draft](../workspace/designs/argus-as-built-v1.json) and [completed-layout proposal](../workspace/designs/argus-complete-layout-v1.json), using seven archived photos and the 3 mm correction. Workshop default now opens the current draft; the original is preserved as [legacy-layout-estimate.json](../workspace/designs/legacy-layout-estimate.json) and in revision history. | Resolves draft generation and delivery. Layout exports and software checks are recorded in the [export notes](../workspace/exports/cad-reconstruction-v1/README.md); exact reconstruction, physical fit, measured balance and terminal wiring remain unverified. |
| 2026-11-07 | Justin requests a basic obstacle-avoidance plan first, implementation later, targeting physical Argus with simulator testing first. [Direct evidence](updates/2026-11-07-obstacle-avoidance-request.md). | Confirms work sequence and target only. The [LiDAR stop-and-turn proposal](plans/2026-11-07-basic-obstacle-avoidance.md) remains an assistant proposal; no existing hardware fact is superseded and no deployment or physical validation is established. |
| 2026-11-07, physical follow-up | Justin confirms the lidar lid still is not fitted, primarily because excess wiring makes the assembly too tall for the current spacers. [Direct evidence](updates/2026-11-07-lidar-lid-wiring-clearance.md). | Reconfirms October's detached-lid state and adds its cause; supersedes any assumption of later lid installation. No new dimensions or other installation changes confirmed. Resolve physical clearance and installed lidar pose before physical avoidance trials; simulator work can proceed. |
| 2026-11-07, latest fit/control update | Justin says the lid now fits and asks to continue; confirms current manual Wi-Fi → ESP32 → Mega control, intentionally removed simulator, and a later Orange Pi/Ethernet/SSH/VS Code idea. [Direct evidence](updates/2026-11-07-lid-fits-and-control-path.md). | Supersedes the same-day fit blocker and uncertainty about the manual route. Does not establish fastening, changed dimensions, protocol, installed Pi or physical avoidance. Small local simulation replaces reliance on the removed environment for this software stage. |
| 2026-11-07, software delivery | Wrote [first avoidance package](../workspace/robot_control/argus_avoidance/README.md); 44 offline tests and nine standalone 2D scenarios pass with zero modeled contact substeps. [Verification](../workspace/robot_control/argus_avoidance/reports/VERIFICATION.md). | Implementation supersedes planning-only software status. Output remains disabled; ESP32 path is not integrated and live ROS, sensor, motor, serial/firmware and physical performance are unverified. |

For each later decision, append its date, Justin's statement or verified artifact,
the previous fact it supersedes, and any remaining physical validation.

2026-11-07, later setup intake: Justin requests assisted Orange Pi configuration
while connecting it to his laptop; explicitly not plugged in yet. This extends
the Ethernet/SSH/VS Code idea without confirming OS, boot or connectivity.
[Direct intake](updates/2026-11-07-orange-pi-setup-intake.md). No hardware state
other than the reported lack of connection is superseded.

2026-11-07, Linux confirmation: Justin says Linux is already installed on the
Orange Pi, resolving the setup intake's OS-installation uncertainty. No reflash
is assumed. Distribution/version, boot medium and SSH access remain unknown.
[Direct confirmation](updates/2026-11-07-orange-pi-setup-intake.md).

2026-11-07, verified Pi setup: Justin connected Ethernet and requested beginner
controls. Use the existing Jammy/Humble installation and a separate workspace
beside his camera scripts. Board tests and an isolated synthetic-scan ROS
preview passed. This supersedes connectivity and software-version uncertainty.
Endpoint of the CH340, physical sensor and wheel behavior remain open.
[Evidence](updates/2026-11-07-verified-orange-pi.md).

2026-11-07, subsequent device check: the CH340 disappeared after Justin unplugged
the ESP32. Treat that association as likely and identify the C1 independently.
Two distinct camera frames confirmed live output, superseding camera-enumeration
evidence alone. [Observation](updates/2026-11-07-esp32-unplug-camera.md).

2026-11-07, later C1 update: Justin reports ordering an adapter while the failed
component remains uncertain. The manual sketch search now has candidate sources.
Confirm flashed versions before changing command handling.
[Evidence](updates/2026-11-07-c1-replacement-and-manual-sketches.md).

2026-11-07, camera course preparation: Justin confirms reliable ESP32/Mega
manual driving and chooses black tape on a light floor. Retrieved recent chats
support the joystick/camera firmware baseline. Prepare a stationary preview,
then explicit manual/automatic ownership before physical automatic steering.
Pi Python checks pass74. Real tape and new firmware upload remain pending.
[Evidence](updates/2026-11-07-current-manual-code-and-tape-preview.md).

2026-11-08, live camera integration: retain the phone on the ESP32 hotspot and
use the existing Pi USB cable for automatic commands and small camera previews.
The new ESP32 firmware is uploaded and hash verified; 115200 baud supersedes
the unreliable initial 460800-baud control transport. The single USB owner is
the existing bridge service with a systemd drop-in. Fifty read-only requests
and all 83 Pi checks pass; the actual lit tape is detected. Phone Stop and
physical wheel/floor behavior remain pending at this checkpoint.
[Evidence](updates/2026-11-08-usb-tape-following.md).

2026-11-08, later transport change: persistent USB disconnects recur after
reseating, changing Pi USB controllers and pausing phone video. Both attempted
wheel pulses fail before arming. Justin prefers onboard Pi control over a
laptop relay and confirms three jumper wires. A separate ESP32 GPIO UART
(RX25/TX26) is implemented, host-tested, target-compiled and flash-hash verified.
Pi uart0-m2 is enabled and ttyS0 verified. Bridge targets ttyS0; all 83 Pi checks
pass. Pi is powered down for user wiring; physical jumpers and GPIO/movement
tests remain pending. Actual Pi pin map: physical8 TX, 10 RX, 6 GND.
[Evidence](updates/2026-11-08-usb-tape-following.md).

2026-11-08, latest wire trace: Justin confirms Pi8→ESP plain RX label and
Pi10→ESP plain TX label. Keep Pi-side positions and GND; move the ESP ends to
printed GPIO25 and GPIO26 to match the uploaded dedicated UART. Pi shut down
again before this physical change. Rewiring and GPIO verification pending.
[Evidence](updates/2026-11-08-usb-tape-following.md).

2026-11-08, corrected GPIO wiring: after Justin moves ESP ends to printed
GPIO25/26 and restores USB power, the ttyS0 bridge returns valid state replies.
All 50 read-only checks pass with zero outputs. Renewed phone Stop check uses
a real zero-speed GPIO automatic session. Physical movement remains untested.
[Evidence](updates/2026-11-08-usb-tape-following.md).

2026-11-08, raised-wheel physical integration: GPIO phone Stop passes570
zero-speed heartbeats. Justin powers motors with wheels raised. He observes
forward motion and stop from a one-second5% pulse, and movement/stop from a
two-second real camera follower. Wheel-channel identity remains under test
because speed comparison was inconclusive. Ground following remains pending.
[Evidence](updates/2026-11-08-usb-tape-following.md).

2026-11-08, floor speed update: a centered-tape one-second6% ground session
completes but Justin reports barely moving and100% manual speed slow. After
motor-off confirmation, upload paired25% cruise/35% cap firmware and Pi client.
All83 Pi checks, actual-sketch handler checks and flash hash verification pass.
GPIO zero-speed handshake ends stopped and cap35 is reported live. Camera
mounted and physical left-channel identity are confirmed. Await motor-on
readiness for a short new-profile ground run.
[Evidence](updates/2026-11-08-usb-tape-following.md).

2026-11-08, power-path check: user reports power restored after the requested
move of ESP USB supply to the same bank as Pi/Mega. Sixty read-only GPIO state
checks pass with one epoch and zero outputs. A four-second floor run then starts
and improves tape offset, but stops early on insufficient tape coverage. User
observation and longer-term power reliability remain pending.
[Evidence](updates/2026-11-08-usb-tape-following.md).

2026-11-08: Justin requests phone-started untethered following and confirms Pi
and power bank secured on Argus. Phone Start and Pi supervisor remain pending;
the local arm client preserves a caller-supplied epoch and passes13 checks.
[Design](../workspace/robot_control/argus_avoidance/PHONE-START-DESIGN.md).

<!-- WORKSHOP_NOTES_START -->
## Dated Workshop notes

Read these notes alongside the source-backed snapshot above. Only an explicit newer claim supersedes an older claim. [All Workshop notes](../workspace/notes/INDEX.md).

- 2026-10-11: [Argus Workshop purpose and collection scope](../workspace/notes/note_f91a410c8fcc.md)
<!-- WORKSHOP_NOTES_END -->
