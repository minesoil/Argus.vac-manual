# Unresolved project facts

Latest 2026-11-14: confirm physical C1 offset from the drive rotation center,
full robot turning radius, loaded stopping gap, phone Stop takeover during a
roaming run, sustained continuous room behavior, and outdoor scan coverage.
The phone roaming Start firmware is not flashed; profile remains uncommissioned.
Floor tape cannot bound an outdoor autonomous run. [Current evidence](updates/2026-11-14-lidar-floor-commissioning.md).

2026-11-14: Justin requests C1 autonomous obstacle avoidance tonight and an outdoor showcase tomorrow. Outdoor area may be open, marked with floor tape only; lidar does not see floor tape, so plan supervised runs with Stop available. Justin confirms motor power OFF and Pi/lidar/Ethernet connected; laptop network sharing must be toggled off/on after laptop restart. Pi is reachable but SSH authentication remains unresolved. Lidar roaming prototype implemented and 114 Python, C++ host, browser and ESP32 dummy-config target checks pass; source published commit 6bd87628f51f2fd9345c1af18892e6f21554da92. It is not installed, scanner runner is not live-tested, and robot motion/braking and outdoor coverage remain unverified. See workspace/robot_control/progress/2026-11-14-lidar-roaming.md.


2026-11-14 verified laptop bench test: CP2102 on COM3; C1 identity responds at 460800 8N1 (model 0x41, firmware 1.02). Health status/error both zero before and after a bounded three-second scan. Received 4584 valid nodes, including 4153 positive nonzero-quality ranges at 138.5–3376 mm. STOP sent, subsequent idle stream zero bytes, port closed. Short live ranging passes; sustained power, calibrated accuracy, scan-rate stability, physical standstill and Pi/ROS integration remain unverified. Supersedes earlier unknown communication/function; no robot drive commanded. Evidence: updates/2026-11-14-c1-laptop-bench-test.md.


2026-11-14 follow-up: Justin reports finishing the C1-to-USB-TTL wiring and wants to connect it to his laptop. Interpreted his wording in the context of the CP2102 discussion; exact terminations/soldering, pin mapping, supply capability and working lidar remain unverified. This supersedes wiring-not-yet-reported only. A read-only Windows baseline shows COM13/COM14 Bluetooth and USB Serial Device COM15; none identified as this CP2102. No serial command, scan or motor operation performed.


2026-11-14 C1 update: replacement CP2102 module has arrived, resolving adapter
order-pending. Still unknown: exact module design and UART voltage, usable 5 V
power path/current capacity, JST-XH variant/cavity count and suitable breakout,
actual completed wiring, earlier failed component, and successful lidar scan.
Four coloured wires are confirmed by Justin; no electrical measurement or
physical validation occurred. [Evidence](updates/2026-11-14-cp2102-arrival.md).

Latest corrected checkpoint, 2026-11-10: assisted-manual code **is installed**
from later November 9 work; 103 Pi/local tests and verified final flash supersede
the earlier not-installed/93-test notes. Phone blocked-drive refusal/warning is
confirmed and paper preview reported CLEAR. Remaining commissioning is the
unanswered motors-off held-joystick actual-object entry/stop check, then
raised-wheel assisted stopping and loaded braking. No complete 45° tape corner
or untethered floor run is established. Confirm current readiness before future
hardware work; today's work uses no robot connection.
[Evidence](updates/2026-11-10-assisted-checkpoint-and-handbook.md).

Latest USB arrangement was ESP connected to Pi for the assisted upload; restoring
bank power and checking the final guarded build on it remain unconfirmed.
Last motor-OFF confirmation was November 9, not a current state today.

The requested reproduction handbook is complete under `workspace/argus-handbook`
and published in f8af59b / fallback refresh3f4c25f. Its 93-file ZIP is under
workspace/exports. A blank spare-Pi rebuild remains untested.
Original Linux/ROS/camera installation commands were already absent at the first
verified connection, and the exact currently installed Mega sketch remains an
evidence gap. Label a replacement installation recipe as reconstructed and any
historical Mega sketch as a candidate. Earlier dated gaps below are retained;
installation-pending statements are superseded by the latest checkpoint.

Final 2026-11-09 checkpoint: stop tape tuning after improved but incomplete
sharp-corner trials. Phone start/stop and bank-powered GPIO/raised wheels pass;
untethered floor operation remains unverified. Prioritize stationary camera
obstacle preview, then warning plus latched stop in manual mode.93 checks pass.
Final GPIO stopped/zero; physical motor-power switch-off requested but unconfirmed.

Latest priority correction 2026-11-09: assisted manual driving needs camera
warning and a latched stop gate that cannot be bypassed by continuing joystick
commands. No such obstacle protection is installed yet. Fixed camera/caster
mount limits visible floor; stationary framing adjustment and sharp-corner
tracking are being checked separately. Structural camera remount is not assumed.

Phone control 2026-11-09 progression: motor-off phone checks, restored bank
power/autostart and raised-wheel phone Start/Stop have passed. Remaining current
check is user-operated floor trial with Ethernet unplugged. Longer-term tracking
and obstacle detection remain separate unverified work.

Latest phone Start status 2026-11-09: firmware and Pi checks are installed/pass;
verify actual phone button, Stop and heartbeat loss, then restored bank power,
raised wheels and untethered floor behavior. Fresh camera currently rejects an
overly dark tape view. No longer blocked on Ethernet or firmware upload.

Public archive 2026-11-09: complete Gemini-app export and the previously referenced
Gemini-only diagnostic workspace remain unavailable. Three saved Gemini-model
Copilot conversations were found and published. One PDF original needs privacy
review; sanitized extracted text is available. Runtime/packages/cache omissions
are explicit in archive/manifest.json. Do not claim universal account-history access.

Dashboard visual revision 2026-11-09: simplified layout is published and browser
checks pass; Justin's response to the revised appearance is not yet recorded.

2026-11-09 dashboard maintenance: update milestone snapshots after verified
hardware progress and add specific explanations for important new files.
Dynamic discovery handles file additions; it does not invent explanations or
measure live robot state.

2026-11-09 priority: finish ESP32 phone-Start flash, rerun Pi tests with its
actual interpreter, restart bridge, and verify phone Stop and untethered driving.
Justin cannot reconnect Ethernet now. Camera obstacle detection is next-stage
work; no physical detection performance or distance accuracy is established.

Collected 2026-10-10. These are recorded gaps, not requests to repeat everything.
Consult the archive first when the relevant task comes up.

1. Identify the exact barebones TB6600 board and its control/current-setting
   circuit. The generated RobotLab guide assumes a common-anode module; compatibility
   with the pictured board has not been established.
2. Justin confirms his M12 3 Ah battery adapter is present on 2026-10-13; adapter
   arrival is resolved. Identify exact pack/adapter variant, fuse and low-voltage
   protection and their physical wiring/commissioning from current evidence.
3. Confirm current physical Mega wiring and whether pin 2 still fails. Historical
   fan maps reuse pin 2 despite the reported fault; the new drive uses different pins.
4. Complete the previous RobotLab audit. `reports/quality-review.json` is referenced
   by its guide but was absent at collection. No final answer was recovered for the
   last cleanup/designer turn. Existing historical test reports remain available.
5. Determine which firmware/bridge is actually deployed. The legacy letter protocol
   and newer CRC protocol are separate branches; neither should be silently substituted.
6. Check the newest shaft's actual print, bearing/gearbox fit, M3 engagement,
   robot weight and loaded strength. CAD checks alone do not answer these.
7. Verify loaded wheel performance, geometry, current settings, microsteps and
   direction. The 1.5 m/s value belongs to simulation; actual speed is unmeasured here.
8. Justin confirms suction motors, N12 12 V brush motors and their respective
   drivers are uninstalled on 2026-10-13. Confirm exact San Ace/N12 models/counts
   and driver selection; reconcile older N20/L298N/IBT-2 proposals. A proposed
   completed CAD does not establish achieved suction or debris pickup.
9. Validate the mounted camera detector and lidar on the Orange Pi. Desktop
   benchmarks, USB-port history and simulated sensor tests have different scopes.
10. Additional older ChatGPT/Gemini files may exist outside exposed tools and local
    exports. Some TB6600 answers are reference placeholders, not recovered answer text.
11. 2026-10-13 CAD drafts are saved from the seven archived photographs; see
    [draft delivery](CAD_RECONSTRUCTION.md). Remaining evidence needs are exact
    spacer length, component coordinates, underside mounts, battery-adapter
    mating fit and wire endpoints. Unidentified component envelopes, retention
    clearances and harness routes in the completed-layout proposal need matching
    measurements. Estimated masses do not establish measured balance; software
    checks do not establish physical fit or terminal wiring.
    [Latest build evidence](updates/2026-10-13-current-build-user.md).

12. 2026-11-07 obstacle avoidance: initial software now written, with 44 offline
    tests and nine small 2D scenarios passing. Physical and live ROS integration
    remain unverified. Measure footprint/lidar pose and loaded stopping, and
    identify current ESP32/Mega protocol and command arbitration before deploying.
    These extend items 5, 7 and 9; do not infer a commissioned drive.
    [Request](updates/2026-11-07-obstacle-avoidance-request.md) and
    [assistant proposal](plans/2026-11-07-basic-obstacle-avoidance.md).

13. 2026-11-07: lid-fit blocker **resolved by Justin's later statement that it
    now fits**. No rerouting or spacer change is confirmed. Remaining checks are
    secure mounting, cable clearance in motion and final sensor pose.
    [Latest evidence](updates/2026-11-07-lid-fits-and-control-path.md).
14. Confirm which ESP32 and Mega sketches are flashed and how they arbitrate
    drive commands. The Arduino sketchbook now supplies candidate firmware.
    [Sketch evidence](updates/2026-11-07-c1-replacement-and-manual-sketches.md).
    The new ROS selector cannot guard manual commands sent directly via ESP32.
    Orange Pi Ethernet/SSH/VS Code setup is a future idea; OS, storage, networking
    and software requirements have not been selected. Do not restore the removed
    simulator as a prerequisite.

15. Orange Pi boot, Ethernet/SSH, OS version and ROS installation are resolved.
    Ubuntu 22.04.5 and Humble were verified. Identify what is attached to the
    CH340 before addressing its BRLTTY conflict. Verify stationary C1 scans,
    measured lidar pose and ESP32/Mega arbitration before physical avoidance.
    [Board check](updates/2026-11-07-verified-orange-pi.md).

16. Subsequent unplug comparison points to the ESP32 connection for the CH340.
    With ESP32 unplugged, identify the C1's own adapter and verify live scans.
    USB camera capture is confirmed. [Evidence](updates/2026-11-07-esp32-unplug-camera.md).

17. Justin reports ordering a replacement adapter. Verify the replacement with
    the C1 when it arrives; the failed part is still unknown.

18. November 8 resolves actual tape detection, new ESP32 upload and Pi control
    connectivity. Pi uses USB; its own hotspot connection is unnecessary.
    Fifty short USB checks pass, but later complete USB disconnects occur.
    Phone Stop is now verified in a 314-heartbeat zero-speed automatic session
    with phone video paused. Pi still reads the full camera. Next are raised-wheel
    direction/stop and a short clear floor course. Motor power is confirmed off
    and wheels raised. Final Pi
    mounting and loaded stopping remain unverified.
    [Latest integration evidence](updates/2026-11-08-usb-tape-following.md).

19. Latest November 8 transport is prepared GPIO UART, superseding USB for
    automatic control. Pi8→ESP25, Pi10←ESP26, Pi6↔ESP GND; ttyS0 and new firmware
    are verified. Pi shut down for safe wiring. Confirm the physical jumpers,
    GPIO read-only/zero-speed sessions and phone Stop before raised-wheel and
    floor motion. Both USB pulse attempts failed before arming; no nonzero wheel
    command was sent. USB/ESP power stability remains to be distinguished from
    USB data-adapter failures. [Evidence](updates/2026-11-08-usb-tape-following.md).

20. Latest wire trace confirms use of ESP plain RX/TX labels instead of
    configured GPIO25/26. Pi is shut down for moving the ESP ends only; Pi8→25,
    Pi10←26, Pi6↔GND. Confirm this physical change, then check GPIO replies and
    zero-speed phone Stop before any wheel request.

21. GPIO endpoint correction and communication are now resolved: after moving
ESP ends to 25/26, all 50 read-only ttyS0 requests pass. Finish the renewed
zero-speed phone Stop check, then raised-wheel direction/stop and short floor
following. Motor power remains off; no nonzero wheel command sent.

22. Latest GPIO phone Stop and physical raised-wheel forward/stop are verified.
    Camera-guided two-second wheel movement completes, but differential speeds
    were not observed. Identify the physical left/right channels from the
    three-second left-only pulse, then confirm mounted camera pose and a short
    clear floor course. Last user-confirmed power state is motor ON, wheels
    raised. No floor-course validation yet.

23. Camera mounting and left-channel identity are now confirmed. First1s floor
    trial barely moves at6%. Paired25% cruise/35% cap update is uploaded and
    verified with zero-speed GPIO handshake. Motor power last confirmed OFF;
    two-second new-profile floor test awaits user readiness. Actual ground
    speed and sustained course performance remain unmeasured.

24. Four-second GPIO floor retry begins and corrects toward tape but stops early
    when coverage becomes uncertain. Ask user where it stopped, then decide
    whether camera position or a longer tape course is needed. ESP reset cause
    remains unconfirmed despite a successful short power-path check.

25. User reports ~12 cm of tape remained when the early stop happened. The logs
    show insufficient tape view, not timeout. Determine camera/crop contribution
    without assuming a measured blind spot. User requests a visible demo today;
    retain lidar mapping and camera obstacle recognition as the longer-term goal.

26. Implement and verify phone-initiated bounded runs over the existing GPIO
    protocol, including Stop/start races, manual takeover, link loss and stale
    camera. User confirms Pi and power bank secured. Phone Start is not installed.

<!-- WORKSHOP_NOTES_START -->
## Dated Workshop notes

Read these notes alongside the source-backed snapshot above. Only an explicit newer claim supersedes an older claim. [All Workshop notes](../workspace/notes/INDEX.md).

<!-- WORKSHOP_NOTES_END -->
