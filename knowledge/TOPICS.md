# Argus Vac topic map

[Latest 2026-11-14 evening: two bounded loaded curves without contact,
final technical LiDAR app hash-verified, motor power OFF; no sustained or
close-wall validation](updates/2026-11-14-arc-map-flash-interruption.md).

[Latest 2026-11-14 about 21:11: ESP32 flash recovered and phone live map
confirmed; manual bridge active, systemd inactive, UI lag/technical preference,
stationary geometry preview only](updates/2026-11-14-arc-map-flash-interruption.md).

2026-11-14: Justin requests C1 autonomous obstacle avoidance tonight and an outdoor showcase tomorrow. Outdoor area may be open, marked with floor tape only; lidar does not see floor tape, so plan supervised runs with Stop available. Justin confirms motor power OFF and Pi/lidar/Ethernet connected; laptop network sharing must be toggled off/on after laptop restart. Pi is reachable but SSH authentication remains unresolved. Lidar roaming prototype implemented and 114 Python, C++ host, browser and ESP32 dummy-config target checks pass; source published commit 6bd87628f51f2fd9345c1af18892e6f21554da92. It is not installed, scanner runner is not live-tested, and robot motion/braking and outdoor coverage remain unverified. See workspace/robot_control/progress/2026-11-14-lidar-roaming.md.


2026-11-14 verified laptop bench test: CP2102 on COM3; C1 identity responds at 460800 8N1 (model 0x41, firmware 1.02). Health status/error both zero before and after a bounded three-second scan. Received 4584 valid nodes, including 4153 positive nonzero-quality ranges at 138.5–3376 mm. STOP sent, subsequent idle stream zero bytes, port closed. Short live ranging passes; sustained power, calibrated accuracy, scan-rate stability, physical standstill and Pi/ROS integration remain unverified. Supersedes earlier unknown communication/function; no robot drive commanded. Evidence: updates/2026-11-14-c1-laptop-bench-test.md.


[CP2102 adapter arrived; C1 four coloured wires and JST-XH connector, electrical
and operating checks pending — 2026-11-14](updates/2026-11-14-cp2102-arrival.md).

[Learning baseline, 2026-11-10: beginner Linux/Python, familiar Arduino/C++,
handbook overwhelming](updates/2026-11-10-learning-baseline.md).

[Latest corrected checkpoint — 2026-11-10: assisted manual installed, 103 tests,
phone blocked-drive warning, paper preview, remaining physical checks and
reproduction handbook request](updates/2026-11-10-assisted-checkpoint-and-handbook.md).
Today is documentation-only while Justin is at school. Earlier not-installed,
93-test and bank-connection summaries below are dated checkpoints superseded
where the latest update says so. Handbook: [workspace/argus-handbook](../workspace/argus-handbook/README.md).

[2026-11-09 phone Start installed; live phone checks pending](updates/2026-11-09-phone-start-installed.md).

[2026-11-09 public archive: Gemini chats, Obsidian and images](updates/2026-11-09-public-documentation-archive.md).

[2026-11-09 file dashboard replacement](updates/2026-11-09-file-dashboard.md).

Latest handoff: [2026-11-09 GitHub publication and pending phone Start deployment](updates/2026-11-09-github-phone-start-handoff.md).

Start with [PROJECT_MEMORY.md](PROJECT_MEMORY.md). These links point to preserved source snapshots. Consult dates and statuses before treating them as current.

For the complete catalog, use [INDEX.md](INDEX.md) or [catalog.jsonl](catalog.jsonl). Search: `python tools/knowledge.py search "TB6600"`.

## Latest camera/USB integration — 2026-11-08

Current: GPIO Stop and raised-wheel forward/stop/left-channel checks pass.
Camera is mounted on Argus. A first one-second tethered floor trial barely
moves at6%; paired25% cruise/35% cap update is prepared, motor power off for
upload. [Latest evidence](updates/2026-11-08-usb-tape-following.md).

Earlier: GPIO UART firmware is uploaded and hash verified, Pi ttyS0 enabled,
and bridge configured. User has three jumpers; Pi shut down for wiring. Physical
connection and GPIO/wheel tests are pending. [Three-wire guide](../workspace/robot_control/argus_avoidance/PI-ESP32-WIRING.md).

[Uploaded ESP32, verified USB control link and real tape detection](updates/2026-11-08-usb-tape-following.md).
All 83 Pi checks and 50 read-only USB requests pass. A longer run exposes USB
disconnects. Pausing phone video permits 314 zero-speed heartbeats and a verified
phone Stop. Physical automatic driving remains pending at this checkpoint.

## Earlier build/control and avoidance software — 2026-11-07

[Current manual firmware family, reliable manual driving and black-tape preview](updates/2026-11-07-current-manual-code-and-tape-preview.md).
Pi checks pass74. Separate ESP32 automatic-mode draft is pending upload.

[Verified Orange Pi bench and beginner controls](updates/2026-11-07-verified-orange-pi.md)
supersede the earlier offline-only stage below. Ethernet/SSH and a Humble preview
with synthetic scans are verified. Real lidar scans remain pending.

[Direct user messages](updates/2026-11-07-lid-fits-and-control-path.md): lid now
fits (superseding earlier blocker); current manual Wi-Fi → ESP32 → Mega;
Orange Pi Ethernet/SSH/VS Code is a future idea; old simulator intentionally deleted.
[New controller and small tests](../workspace/robot_control/argus_avoidance/README.md)
and [verification limits](../workspace/robot_control/argus_avoidance/reports/VERIFICATION.md).
Offline tests only; no deployed or physical avoidance established.

## Earlier lidar-lid clearance blocker — superseded later 2026-11-07

[Direct user update](updates/2026-11-07-lidar-lid-wiring-clearance.md): lid still
not fitted because excess wiring height exceeds current spacer clearance.
No new dimensions or other installation changes confirmed. See
[current build](CURRENT_BUILD_STATE.md).

## Basic obstacle avoidance — 2026-11-07 planning

[Direct request and simulator-first physical target](updates/2026-11-07-obstacle-avoidance-request.md)
and [assistant proposal](plans/2026-11-07-basic-obstacle-avoidance.md).
Planning only; no deployment or updated physical build status established.

## Vault manuals, physical history and preferences

Current CAD reconstruction request: 2026-10-13 direct user statement, source
`3b1c40e5d87877efe46e`, [intake](CAD_RECONSTRUCTION.md). Photos and measurements
are pending; earlier CAD dimensions are estimates.

Latest2026-10-13 physical stage: [current build](CURRENT_BUILD_STATE.md),
[direct update](updates/2026-10-13-current-build-user.md),
[3mm thickness correction](updates/2026-10-13-plate-thickness-correction.md),
[seven current Library photo sources](../workspace/exports/cad-reference/photo-evidence.json),
[recent drive bench messages](updates/recent-microstepping-chat-2026-10-13.json).
The latest correction supersedes earlier10mm; photo positions remain estimates.

| Source | ID | Snapshot |
|---|---|---|
| obsidian-argus:1-Manuals/Argus Vac - Calibration & Preventive Troubleshooting Guide.md | `7c19470ff556001fabbe` | [read](text/7c19470ff556001fabbe--Argus%20Vac%20-%20Calibration%20_%20Preventive%20Troubleshooting%20Guide.md.md) · [raw](objects/sha256/9e/9e9587d4b22434e7ccbb926a2a1a3c5bc9ca7b761a37cba96742c12eb57d3395.md) |
| obsidian-argus:1-Manuals/Argus Vac - Electrical Wiring & Power Reference.md | `e84583dda7f9bde230e9` | [read](text/e84583dda7f9bde230e9--Argus%20Vac%20-%20Electrical%20Wiring%20_%20Power%20Reference.md.md) · [raw](objects/sha256/bb/bb24d90a1317e199d3ee054c693fe43f53055be4842c95a683593159576f3c32.md) |
| obsidian-argus:1-Manuals/Argus Vac - Hardware & Mechanical Architecture Manual.md | `77e307eb5d96605d25c4` | [read](text/77e307eb5d96605d25c4--Argus%20Vac%20-%20Hardware%20_%20Mechanical%20Architecture%20Manual.md.md) · [raw](objects/sha256/c3/c393826334a74c977ffa4ee2f7fc82c1f192546f9b4fb2e5564af78977f814d0.md) |
| obsidian-argus:1-Manuals/Argus Vac - Project Progress & Action Plan.md | `a5b2a28e2eb12404412a` | [read](text/a5b2a28e2eb12404412a--Argus%20Vac%20-%20Project%20Progress%20_%20Action%20Plan.md.md) · [raw](objects/sha256/a2/a222adb0633344cb75d5e58364a5609c01094ebbb8cc6ce51e84045b2e0e7093.md) |
| obsidian-argus:1-Manuals/Argus Vac - Wiring Day Build Checklist.md | `90ccc3d3adc3f65a06e3` | [read](text/90ccc3d3adc3f65a06e3--Argus%20Vac%20-%20Wiring%20Day%20Build%20Checklist.md.md) · [raw](objects/sha256/c4/c46c047205c005c60e0f8d5ba55457ae5987c3a5d3e5d2fdf051c2718e648920.md) |
| obsidian-argus:2-Reference/ROBOT_MASTER.md | `87b42cf22476245ab36c` | [read](text/87b42cf22476245ab36c--ROBOT_MASTER.md.md) · [raw](objects/sha256/4b/4b08b4bd0fa4e17c8f1c5e8980cf004e8650cf0eb92856be168ff202993418fd.md) |
| obsidian-argus:3-Logs/argus-vac-developer-preferences-v4.md | `5c377f077e2aba98af1c` | [read](text/5c377f077e2aba98af1c--argus-vac-developer-preferences-v4.md.md) · [raw](objects/sha256/a5/a54ccad8cc475e36eed5b35b5f8977c6a152008d13e8839a1adfc900988b1ea4.md) |
| obsidian-argus:3-Logs/argus-vac-historical-troubleshooting-log-v4.6.md | `83b9aac5e26a584d4765` | [read](text/83b9aac5e26a584d4765--argus-vac-historical-troubleshooting-log-v4.6.md.md) · [raw](objects/sha256/04/04dc081bdaf66305bab3ba60fd2547673e98e799aad1ca2a9166019d7c525ef2.md) |
| obsidian-argus:3-Logs/argus-vac-housekeeping-and-cleanup-v3.14.md | `5514ba5fed1f387e8bed` | [read](text/5514ba5fed1f387e8bed--argus-vac-housekeeping-and-cleanup-v3.14.md.md) · [raw](objects/sha256/35/35530cebb85a2357ed6b357767cc86799362e622668fbbc262e9dfda743836f5.md) |
| obsidian-argus:3-Logs/argus-vac-next-steps.md | `6e81792afcd6d3c5263a` | [read](text/6e81792afcd6d3c5263a--argus-vac-next-steps.md.md) · [raw](objects/sha256/f9/f99f9c2bae49b9c66c1e3e62f995e285c17b3fdffcc94b5ccadf325a562e627d.md) |
| obsidian-argus:3-Logs/argus-vac-version-control-and-change-log-v25.md | `6214747d10768808285d` | [read](text/6214747d10768808285d--argus-vac-version-control-and-change-log-v25.md.md) · [raw](objects/sha256/48/4825a3ce69d66e0924a429d11ca178dfbde71415cd3eb6f53d72ffb5c1f69077.md) |
| obsidian-argus:3-Logs/argus-vac-vscode-setup-v3.md | `93abd815a6f011bd5e96` | [read](text/93abd815a6f011bd5e96--argus-vac-vscode-setup-v3.md.md) · [raw](objects/sha256/92/92a753bb8e0f4d2f1c88528cb7b3cfe4b7bbc312aad66fdd795ad232f1eec7e0.md) |
| obsidian-argus:HANDOFF.md | `f37f98b9fc923eeae76e` | [read](text/f37f98b9fc923eeae76e--HANDOFF.md.md) · [raw](objects/sha256/e5/e575dd36ec3830de109ce5070e9110fa9bb054fa0d8ee2c777c0cc23d938f9c0.md) |

## Legacy perception and actuator software

| Source | ID | Snapshot |
|---|---|---|
| obsidian-argus:4-Software/cv-environment-diagnostic.py | `b97b3628e16e83a0b167` | [read](text/b97b3628e16e83a0b167--cv-environment-diagnostic.py.md) · [raw](objects/sha256/81/81a9b23d27f3801b88c2e9ea23cd1adc9227b310c1ca00fb2c173ae3196f9278.py) |
| obsidian-argus:4-Software/dashboard/app.js | `df797c393a3935a9665c` | [read](text/df797c393a3935a9665c--app.js.md) · [raw](objects/sha256/a3/a3ea6ac1be45888e5d6e9597008fbb685778ebc9b1e2daa950e538ccb3a8c1c0.js) |
| obsidian-argus:4-Software/dashboard/app1.js.ts | `0f98ca89a5e84cb95fd5` | [read](text/0f98ca89a5e84cb95fd5--app1.js.ts.md) · [raw](objects/sha256/e3/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855.ts) |
| obsidian-argus:4-Software/dashboard/index.html | `0ff191b17185932390a8` | [read](text/0ff191b17185932390a8--index.html.md) · [raw](objects/sha256/b4/b4ab313d0cbde7dfbd5be5681156a6718043236d62b3e357040cdf684e3d34b1.html) |
| obsidian-argus:4-Software/dashboard/style.css | `3fc4cc17950ad9b5f16d` | [read](text/3fc4cc17950ad9b5f16d--style.css.md) · [raw](objects/sha256/47/47f724f81fa818304280b5144d787b9bc864c5775b08d7bbf104dc1b377ab1b0.css) |
| obsidian-argus:4-Software/lidar-watch.py | `ebab948c30ea713d44cd` | [read](text/ebab948c30ea713d44cd--lidar-watch.py.md) · [raw](objects/sha256/c9/c9518e68d32eeadf8d7451b7e586a6d60124c99390c7ae1c3a110a587b4e2944.py) |
| obsidian-argus:4-Software/mega-controller.ino | `e989fcb35418f5304bff` | [read](text/e989fcb35418f5304bff--mega-controller.ino.md) · [raw](objects/sha256/66/660e8c3d3a734916dcd3a7974f4b4c800e9dc4344323a490ab54c1cc3a3f4026.ino) |
| obsidian-argus:4-Software/obstacle-detector-mediapipe-v10.6.py | `3ed6887665294227ae51` | [read](text/3ed6887665294227ae51--obstacle-detector-mediapipe-v10.6.py.md) · [raw](objects/sha256/7c/7c0aef1c356d430d5bda2d4efb91231be8074e665d16dfb70b1fd8fa304fa92c.py) |
| obsidian-argus:4-Software/pi-hardware-validator.py | `9afa508c440192f90632` | [read](text/9afa508c440192f90632--pi-hardware-validator.py.md) · [raw](objects/sha256/3f/3fdbb0905c076dacecae3524c9b7b3f90846b5a294a2e8fa9377de459b526518.py) |
| obsidian-argus:_Archive/obstacle-detector-mediapipe-v8.py | `03690ecc452c53d44023` | [read](text/03690ecc452c53d44023--obstacle-detector-mediapipe-v8.py.md) · [raw](objects/sha256/9a/9a4491df9af33f65fa9857fbd81cbfdc598d0dd7ca9c3d2200991f0006b5c9fd.py) |
| obsidian-argus:_Archive/obstacle-detector-mediapipe-v9.py | `c072e81ad5c494da0920` | [read](text/c072e81ad5c494da0920--obstacle-detector-mediapipe-v9.py.md) · [raw](objects/sha256/5c/5c404faf38cdf26f6a6cc040721c46f6405e7af7d816d369206e7b76ec13395e.py) |

## Fritzing wiring and netlists

| Source | ID | Snapshot |
|---|---|---|
| obsidian-argus:5-Hardware/Argus Vac Final.fzz | `06eae1cb21dfcba8d63f` | [read](text/06eae1cb21dfcba8d63f--Argus%20Vac%20Final.fzz.md) · [raw](objects/sha256/39/399278298d2cbf89443c7cfaf4eb988bf1fe1b485db0f8c8ed5d0229485637b6.fzz) |
| obsidian-argus:5-Hardware/Argus Vac_netlist_Final.xml | `c78dfd96fd1275c2e95a` | [read](text/c78dfd96fd1275c2e95a--Argus%20Vac_netlist_Final.xml.md) · [raw](objects/sha256/89/89db8928f8170173523db2be2efbd841d4d75e08ba50db8469743e7e62ed9cac.xml) |

## Saved Obsidian conversations and voice notes

| Source | ID | Snapshot |
|---|---|---|
| obsidian-argus:copilot/copilot-conversations/agent__based_off_the_pinouts,_write_me_a_test_code_for@20260827_231221.md | `ae7a070116369db00129` | [read](text/ae7a070116369db00129--agent__based_off_the_pinouts__write_me_a_test_code_for_20260827_231221.md.md) · [raw](objects/sha256/80/80f605cfd00e335008da1df7ee39f5ed6bcfb6b8772cf4b2bcf0522756ab650e.md) |
| obsidian-argus:copilot/copilot-conversations/agent__based_off_the_pinouts,_write_me_a_test_code_for@20260827_231307.md | `bfdb77c3d0615f7ec150` | [read](text/bfdb77c3d0615f7ec150--agent__based_off_the_pinouts__write_me_a_test_code_for_20260827_231307.md.md) · [raw](objects/sha256/8c/8cd2841e34f74a737f2def17f9a174b5a2cb4a00c5b63333d6339d901252be40.md) |
| obsidian-argus:copilot/copilot-conversations/agent__based_off_the_pinouts,_write_me_a_test_code_for@20260827_231330.md | `d7196f4eff97858d1f2d` | [read](text/d7196f4eff97858d1f2d--agent__based_off_the_pinouts__write_me_a_test_code_for_20260827_231330.md.md) · [raw](objects/sha256/54/541f0e544c1be20acc35a808c29f442df3021d1190d5cba69d3b7b05956bb35a.md) |
| obsidian-argus:copilot/copilot-conversations/agent__hi,_are_you_able_to_recruit_other_AIs@20260826_225938.md | `5ae8cb7377425aaa1c66` | [read](text/5ae8cb7377425aaa1c66--agent__hi__are_you_able_to_recruit_other_AIs_20260826_225938.md.md) · [raw](objects/sha256/be/be2261aaa9834eab4c1f28b6e7992691c289868471714c2f4b603cf6c1bbdcd7.md) |
| obsidian-argus:copilot/copilot-conversations/agent__hi,_give_me_a_breif_summary_on_my_vault_after@20260826_230300.md | `de60c61757a07dbb2995` | [read](text/de60c61757a07dbb2995--agent__hi__give_me_a_breif_summary_on_my_vault_after_20260826_230300.md.md) · [raw](objects/sha256/df/df9623d679975244b24276931b61ffa49f05f8f54f391649785d4ac24b59889c.md) |
| obsidian-argus:copilot/copilot-conversations/agent__Its_been_a_hwile_since_I_update_everything._As_of@20260927_122746.md | `7f085054584151be08fb` | [read](text/7f085054584151be08fb--agent__Its_been_a_hwile_since_I_update_everything._As_of_20260927_122746.md.md) · [raw](objects/sha256/4d/4dc5d4e91428632df68241a6e7571deb8aa3e13e987c547ca4907b018a376f14.md) |
| obsidian-argus:copilot/copilot-conversations/agent__today,_i_was_doing_research_on_wire_sizes,_and_it@20260826_193027.md | `f55ffb5b858767e6c90a` | [read](text/f55ffb5b858767e6c90a--agent__today__i_was_doing_research_on_wire_sizes__and_it_20260826_193027.md.md) · [raw](objects/sha256/b7/b7ad2de2422e68a21701b92f2a7f333d61c5df4ba0d2f421561304a1ecc3f569.md) |
| obsidian-argus:copilot/copilot-conversations/agent__yo,_my_last_convo_with_another_AI_Agent_got_cut@20260826_005256.md | `1c52bbe3dc8fb66597bd` | [read](text/1c52bbe3dc8fb66597bd--agent__yo__my_last_convo_with_another_AI_Agent_got_cut_20260826_005256.md.md) · [raw](objects/sha256/af/af5847e91eb6cc7a57e391dc6714883f6d3a48587f9592e780645cfe55275b17.md) |
| obsidian-argus:copilot/copilot-conversations/Argus_Vac_Obstacle_Detector_Explained@20260826_004340.md | `286aecbae85b464482d4` | [read](text/286aecbae85b464482d4--Argus_Vac_Obstacle_Detector_Explained_20260826_004340.md.md) · [raw](objects/sha256/55/558f41ac4d0608419028c4da63687198e9d3bcecc86bcd088b7140f8387f0868.md) |
| obsidian-argus:copilot/copilot-conversations/Argus_Vac_Obstacle_Risk_Detector@20260826_004340.md | `218e00142b2b68823b2b` | [read](text/218e00142b2b68823b2b--Argus_Vac_Obstacle_Risk_Detector_20260826_004340.md.md) · [raw](objects/sha256/87/87c072b2f76efd70335f40a88949782ca4dfdbc66ef2ce6ca5f6f6710e8d3621.md) |
| obsidian-argus:copilot/copilot-conversations/Multi-Model_Task_Delegation_Plan@20260826_204340.md | `78420317566f16e9ac5e` | [read](text/78420317566f16e9ac5e--Multi-Model_Task_Delegation_Plan_20260826_204340.md.md) · [raw](objects/sha256/bd/bd0a9d15915648e5799bb504081aa0ac4ea8cbc395916843612c355bf4c6bada.md) |
| obsidian-argus:Voice Scribe/voice-2026-08-25-1210-2.md | `039fd0ca10eda133fbbe` | [read](text/039fd0ca10eda133fbbe--voice-2026-08-25-1210-2.md.md) · [raw](objects/sha256/fd/fd36a56d16f5b09d8e22acdd84be91e7e4eae2c8d84fd4928242b6c489a7b85b.md) |
| obsidian-argus:Voice Scribe/voice-2026-08-25-1210-3.md | `8afc150166c5f7e77d9a` | [read](text/8afc150166c5f7e77d9a--voice-2026-08-25-1210-3.md.md) · [raw](objects/sha256/ae/aedcce1fa8199d3f168434983dc396a84f82e91967dc3730f0b51922f87d4ce0.md) |
| obsidian-argus:Voice Scribe/voice-2026-08-25-1210.md | `14593096f0b7d6e5fc28` | [read](text/14593096f0b7d6e5fc28--voice-2026-08-25-1210.md.md) · [raw](objects/sha256/54/5481859523424a4a72b52826f7a0462d81e35a20bc9ad2121a5b7f22e99ba39a.md) |

## Latest RobotLab guides and design

| Source | ID | Snapshot |
|---|---|---|
| ros-resumed:outputs/RobotLab/config/dependencies.json | `c4c852d8bbf9b3c87f44` | [read](text/c4c852d8bbf9b3c87f44--dependencies.json.md) · [raw](objects/sha256/76/762d8568c87a2ce750c2f8d40faecfc50695bc143e2c36bee7ad59f53db73077.json) |
| ros-resumed:outputs/RobotLab/config/simulation.json | `8fffa9a4960f3d83adc7` | [read](text/8fffa9a4960f3d83adc7--simulation.json.md) · [raw](objects/sha256/a3/a33867dccb9467d4a6459e8272040980085e0943304ff8fb843a8ec947c37307.json) |
| ros-resumed:outputs/RobotLab/designs/default.json | `c12b4e948b923dce1e12` | [read](text/c12b4e948b923dce1e12--default.json.md) · [raw](objects/sha256/c2/c25dd5511964f7991ac285556d249498700d3734b2dcc869fc4499791b3ca68d.json) |
| ros-resumed:outputs/RobotLab/docs/architecture.md | `1c00e63e2dbdf342de4b` | [read](text/1c00e63e2dbdf342de4b--architecture.md.md) · [raw](objects/sha256/58/58404ae91fb46feb76a801bb367104f31892db3c840a875ebafb93af2651a146.md) |
| ros-resumed:outputs/RobotLab/docs/designer.md | `b8aa4c452d1ba59f166f` | [read](text/b8aa4c452d1ba59f166f--designer.md.md) · [raw](objects/sha256/e5/e5e2cf2f77dd177b1885fc24c088ab2a202fafbaa27ec20ac31b0b6cd78baa75.md) |
| ros-resumed:outputs/RobotLab/docs/development.md | `9685cc0ec3b84ebbc382` | [read](text/9685cc0ec3b84ebbc382--development.md.md) · [raw](objects/sha256/7b/7bd0923c801ddbb3402f12b77e52d174ad4a238790ed3988587d7dbdd8e4e7cb.md) |
| ros-resumed:outputs/RobotLab/docs/hardware.md | `8d2072f762edb271d396` | [read](text/8d2072f762edb271d396--hardware.md.md) · [raw](objects/sha256/79/79818079c08427d4237b2b2365835616c451482b33b5247f5eb6d0748ec8e52b.md) |
| ros-resumed:outputs/RobotLab/docs/orange-pi.md | `d4cfba56e203be99305b` | [read](text/d4cfba56e203be99305b--orange-pi.md.md) · [raw](objects/sha256/ef/efbb698e48ad8b282597582c334bdba567e5ba08939db049700d2a6de1eb8ca0.md) |
| ros-resumed:outputs/RobotLab/README.md | `c646a0a5dbae397b6f75` | [read](text/c646a0a5dbae397b6f75--README.md.md) · [raw](objects/sha256/be/bee3ad6027e9652c793bb39425cf980c62cdb8cb2178cf58060dbdf0fd268c43.md) |

## Latest proposed hardware firmware and bridge

| Source | ID | Snapshot |
|---|---|---|
| ros-resumed:outputs/RobotLab/firmware/mega_drive/drive_config.h | `d8f3e6d87dcfc7e41172` | [read](text/d8f3e6d87dcfc7e41172--drive_config.h.md) · [raw](objects/sha256/07/0776dc712d0d65160669ca0574c653d63354407cf438806815616b85e31b6301.h) |
| ros-resumed:outputs/RobotLab/firmware/mega_drive/mega_drive.ino | `7d05537bdc3a1f67d603` | [read](text/7d05537bdc3a1f67d603--mega_drive.ino.md) · [raw](objects/sha256/ca/cacfb08d3800d1f1cc7cbc6759d227c1fe5a911301eebf1ce1353cdaef0d660b.ino) |
| ros-resumed:outputs/RobotLab/firmware/mega_drive/protocol.h | `2dd93b08e664fead267c` | [read](text/2dd93b08e664fead267c--protocol.h.md) · [raw](objects/sha256/a3/a37c06ec99acf18b4008ee8d3c950feacdf6156ff0547051e813ef1ef99090dd.h) |
| ros-resumed:outputs/RobotLab/ros2/src/vacuum_hardware/config/hardware.yaml | `2d65f22d8a96c5384fe0` | [read](text/2d65f22d8a96c5384fe0--hardware.yaml.md) · [raw](objects/sha256/d1/d1199abe31f7f19bbe3840fe25044fc224e4156c7d2ffd0fa8d38c2a3466fd10.yaml) |
| ros-resumed:outputs/RobotLab/ros2/src/vacuum_hardware/vacuum_hardware/motor_bridge.py | `73d3414d80f3109f5de1` | [read](text/73d3414d80f3109f5de1--motor_bridge.py.md) · [raw](objects/sha256/41/4164b30c9c4fa24dd41c0ca9c3af4fa6acdbf194082af809132d58f56e03890a.py) |
| ros-resumed:outputs/RobotLab/ros2/src/vacuum_hardware/vacuum_hardware/serial_link.py | `e3c38e4d5d44444e4462` | [read](text/e3c38e4d5d44444e4462--serial_link.py.md) · [raw](objects/sha256/8e/8e279328cf4eb8e5ebdf91640038fd68f346358a5edba70a55ddb19e989a23e7.py) |

## Historical simulation and verification evidence

| Source | ID | Snapshot |
|---|---|---|
| ros-resumed:outputs/RobotLab/reports/history/backup-verification.json | `deb1429b2c334832af0d` | [read](text/deb1429b2c334832af0d--backup-verification.json.md) · [raw](objects/sha256/c0/c05a7d34368d371a3fbda44edd65fa2b4c87d55a9b5b47d77d482c1f1e66c9ed.json) |
| ros-resumed:outputs/RobotLab/reports/history/direct-drive-validation.json | `ae71c4e412da81cea68a` | [read](text/ae71c4e412da81cea68a--direct-drive-validation.json.md) · [raw](objects/sha256/c3/c339f3b99783fefbc84f35b1c453ee694dc36e750878a401f54e3b7840358250.json) |
| ros-resumed:outputs/RobotLab/reports/history/directional-guard-validation.json | `0423efe48afec47457c7` | [read](text/0423efe48afec47457c7--directional-guard-validation.json.md) · [raw](objects/sha256/28/284cc78fdd1db2c6f78c07821627c93da6adc442df12accb27b9b79910f2fdc9.json) |
| ros-resumed:outputs/RobotLab/reports/history/executable-verification.json | `62c79ec78f999eb685df` | [read](text/62c79ec78f999eb685df--executable-verification.json.md) · [raw](objects/sha256/21/21ac8af49122cbfea18ef0ba1da07e11fb9aeab1cc9e45cd4e1c0e8a92d631fd.json) |
| ros-resumed:outputs/RobotLab/reports/history/lab-validation.json | `c2495f14b4f2fd9d24be` | [read](text/c2495f14b4f2fd9d24be--lab-validation.json.md) · [raw](objects/sha256/0c/0c40432e5038fd1c8051554de071e34fe826db9ca812a98ba2284bfec00c7aa8.json) |
| ros-resumed:outputs/RobotLab/reports/history/modern-drive-validation.json | `3a714038d6dc4214a66c` | [read](text/3a714038d6dc4214a66c--modern-drive-validation.json.md) · [raw](objects/sha256/c3/c339f3b99783fefbc84f35b1c453ee694dc36e750878a401f54e3b7840358250.json) |
| ros-resumed:outputs/RobotLab/reports/history/navigation-check.json | `4f887eeea33c02912bfb` | [read](text/4f887eeea33c02912bfb--navigation-check.json.md) · [raw](objects/sha256/27/27ab57ecc1824ea60ae8ee02f194f5846c39b057a2147536c74656d463b7e511.json) |
| ros-resumed:outputs/RobotLab/reports/history/performance-check.json | `3cc0fda0f8d358b07498` | [read](text/3cc0fda0f8d358b07498--performance-check.json.md) · [raw](objects/sha256/1d/1d6af7f8de36e3f00e080dffbf218372ebea84cd30373d8315ef46d018ea6362.json) |
| ros-resumed:outputs/RobotLab/reports/history/shutdown-verification.json | `b11fe0d624a0e5d0b490` | [read](text/b11fe0d624a0e5d0b490--shutdown-verification.json.md) · [raw](objects/sha256/c1/c17d954b91e934308a43b8eb039a35bbeee734652b128caf459af93cbed189e9.json) |
| ros-resumed:outputs/RobotLab/reports/history/simulation-check.json | `8c4b721c198dc8a92919` | [read](text/8c4b721c198dc8a92919--simulation-check.json.md) · [raw](objects/sha256/54/54418e0b07ade3c16ceeb7895065309cb6b1ad1d8caf2679be1f2273d5496ee1.json) |
| ros-resumed:outputs/RobotLab/reports/history/tuned-simulation-check.json | `a5c2e78414d4e20f3c60` | [read](text/a5c2e78414d4e20f3c60--tuned-simulation-check.json.md) · [raw](objects/sha256/52/52f8030bf44238add20791089f6de81ac273c13d026f1fcc3d5d3ec1a30b96a5.json) |
| ros-resumed:outputs/RobotLab/reports/README.md | `bee8d33387d734fbda1e` | [read](text/bee8d33387d734fbda1e--README.md.md) · [raw](objects/sha256/6a/6ab80697485c50aa8341ed15fe13ace3ef1b3f1b8c6814689020fa26b772b7f2.md) |

## Wheel shaft CAD, variants and fit notes

| Source | ID | Snapshot |
|---|---|---|
| wheel-shaft:outputs/direct_hex_40mm_13mm_base_assembly_notes.txt | `ecb4bd76aea45977a157` | [read](text/ecb4bd76aea45977a157--direct_hex_40mm_13mm_base_assembly_notes.txt.md) · [raw](objects/sha256/3a/3aca79dc8022413bb1ffdeba0c874827fdf4e62c16bba874d1f6fa13d6d9e92b.txt) |
| wheel-shaft:outputs/direct_hex_40mm_assembly_notes.txt | `3385f838aa3ede07decd` | [read](text/3385f838aa3ede07decd--direct_hex_40mm_assembly_notes.txt.md) · [raw](objects/sha256/e1/e1c225baf141a7a3b17ecf9202f0a3819fc2bf4dd207db885113055e50261f46.txt) |
| wheel-shaft:outputs/direct_hex_40mm_reinforced_assembly_notes.txt | `1a410a7e58eeacea393a` | [read](text/1a410a7e58eeacea393a--direct_hex_40mm_reinforced_assembly_notes.txt.md) · [raw](objects/sha256/58/58a71434df5f699dbb1329650d34dad18ec57ad223212138c8412c416e557f35.txt) |
| wheel-shaft:outputs/direct_hex_40mm_uniform13_assembly_notes.txt | `325fa0266be574c17071` | [read](text/325fa0266be574c17071--direct_hex_40mm_uniform13_assembly_notes.txt.md) · [raw](objects/sha256/f6/f6bde03b1595844cd478f00015c8e381eeb87f74e211bb4a610b7a18bcb51bc8.txt) |
| wheel-shaft:outputs/direct_hex_assembly_notes.txt | `f1355f8aef28c0faff4a` | [read](text/f1355f8aef28c0faff4a--direct_hex_assembly_notes.txt.md) · [raw](objects/sha256/bf/bf06b7d27947615215468e0be49872c2695a21e8b8475b4c482071792b2bd3a5.txt) |
| wheel-shaft:outputs/shaft_pair_5mm_D.step | `26732d6a4fdb90b7b65d` | [read](objects/sha256/b1/b10e5a8d55aebb4ea5b8782b5af113afab601e735b235a5e62c1768d86c2fd01.step) · [raw](objects/sha256/b1/b10e5a8d55aebb4ea5b8782b5af113afab601e735b235a5e62c1768d86c2fd01.step) |
| wheel-shaft:outputs/shaft_pair_5mm_D.stl | `b6e06dcb54d1e032753b` | [read](objects/sha256/d0/d0f8611aecaeb012dd90814b707636ab722345c5b5af38724e0932d1681e3b1c.stl) · [raw](objects/sha256/d0/d0f8611aecaeb012dd90814b707636ab722345c5b5af38724e0932d1681e3b1c.stl) |
| wheel-shaft:outputs/shaft_pair_direct_hex_M3.step | `48c643c7dd0a14085991` | [read](objects/sha256/71/71725b727331308130c7bd45d4838a0657cefc945c8145113ccdf0610b239f3d.step) · [raw](objects/sha256/71/71725b727331308130c7bd45d4838a0657cefc945c8145113ccdf0610b239f3d.step) |
| wheel-shaft:outputs/shaft_pair_direct_hex_M3.stl | `ca7f7be022c2dbba7912` | [read](objects/sha256/d2/d2077afd9d9cb96da727f13e1b43a863a771161386c5b584502fea05ed2c5416.stl) · [raw](objects/sha256/d2/d2077afd9d9cb96da727f13e1b43a863a771161386c5b584502fea05ed2c5416.stl) |
| wheel-shaft:outputs/shaft_pair_direct_hex_M3_40mm.step | `7b23614744ac34119344` | [read](objects/sha256/6c/6ce31edcfa47afeef2e4bf5d90b2e1665b0312cfb3185c144101dfdaa81b3423.step) · [raw](objects/sha256/6c/6ce31edcfa47afeef2e4bf5d90b2e1665b0312cfb3185c144101dfdaa81b3423.step) |
| wheel-shaft:outputs/shaft_pair_direct_hex_M3_40mm.stl | `58898c7bbb6b5a9879b6` | [read](objects/sha256/45/458aa73edd82180e5db6629c2f4a1edb29abb611e8098983bd2ed62656fb75eb.stl) · [raw](objects/sha256/45/458aa73edd82180e5db6629c2f4a1edb29abb611e8098983bd2ed62656fb75eb.stl) |
| wheel-shaft:outputs/shaft_pair_direct_hex_M3_40mm_13mm_base.step | `34535d9a9b235af87c27` | [read](objects/sha256/b0/b0c6506e5820972e253b95b77db0296a09b2aab8ba6e99c61d886d6cbc224c56.step) · [raw](objects/sha256/b0/b0c6506e5820972e253b95b77db0296a09b2aab8ba6e99c61d886d6cbc224c56.step) |
| wheel-shaft:outputs/shaft_pair_direct_hex_M3_40mm_13mm_base.stl | `dcbcf006acf11963c0b6` | [read](objects/sha256/ef/ef9c1c058f0234379d329d9a852d34c908d34521d1c55e3e7a2ce235b157eaa2.stl) · [raw](objects/sha256/ef/ef9c1c058f0234379d329d9a852d34c908d34521d1c55e3e7a2ce235b157eaa2.stl) |
| wheel-shaft:outputs/shaft_pair_direct_hex_M3_40mm_reinforced.step | `044865393e6322297e8b` | [read](objects/sha256/32/3278d6d462c5a9d3637d2bedfd658e038862bd0c8cc87c2eabee02f48f4ba6c3.step) · [raw](objects/sha256/32/3278d6d462c5a9d3637d2bedfd658e038862bd0c8cc87c2eabee02f48f4ba6c3.step) |
| wheel-shaft:outputs/shaft_pair_direct_hex_M3_40mm_reinforced.stl | `b070528524ce9a7d9259` | [read](objects/sha256/b3/b335663098361b5cb597f44b43ed49c3c27ee9593f539cf87eb5308344e7787b.stl) · [raw](objects/sha256/b3/b335663098361b5cb597f44b43ed49c3c27ee9593f539cf87eb5308344e7787b.stl) |
| wheel-shaft:outputs/shaft_pair_direct_hex_M3_40mm_uniform13.step | `b133a9515c3cfa91a397` | [read](objects/sha256/4c/4c3c18b9231fa195e7702c519951262d90cbeb51e8b5047d3bf4940a6f729c2d.step) · [raw](objects/sha256/4c/4c3c18b9231fa195e7702c519951262d90cbeb51e8b5047d3bf4940a6f729c2d.step) |
| wheel-shaft:outputs/shaft_pair_direct_hex_M3_40mm_uniform13.stl | `7d5829052d72afa7a145` | [read](objects/sha256/37/37e8718acad4e2f563af654944524821ff58ce7892f6e693d5dcc1b204efa0b2.stl) · [raw](objects/sha256/37/37e8718acad4e2f563af654944524821ff58ce7892f6e693d5dcc1b204efa0b2.stl) |
| wheel-shaft:outputs/shaft_pair_shorter_reinforced.step | `d8efe83969f3d62160f4` | [read](objects/sha256/c3/c30f07e7a644b2f903f79105f2d89c0b461b3cb6dbe70454444e727d85b50606.step) · [raw](objects/sha256/c3/c30f07e7a644b2f903f79105f2d89c0b461b3cb6dbe70454444e727d85b50606.step) |
| wheel-shaft:outputs/shaft_pair_shorter_reinforced.stl | `95777ff45313b5800214` | [read](objects/sha256/78/784f96584afcf38336e7853df1c574c362a9cb88d16c2b6dc2c051848b214727.stl) · [raw](objects/sha256/78/784f96584afcf38336e7853df1c574c362a9cb88d16c2b6dc2c051848b214727.stl) |

## A4988 bench diagnostics

| Source | ID | Snapshot |
|---|---|---|
| a4988-bench:outputs/left_wheel_diagnostic/left_wheel_diagnostic.ino | `36350cd1133b07a4ed66` | [read](text/36350cd1133b07a4ed66--left_wheel_diagnostic.ino.md) · [raw](objects/sha256/59/59e3c4e502d9494609d5609cea5add509564bd162faec5a090f0da8e53e4ec32.ino) |
| a4988-bench:outputs/WIRING_STATUS.md | `0a7d338063f0650b815d` | [read](text/0a7d338063f0650b815d--WIRING_STATUS.md.md) · [raw](objects/sha256/e2/e2f7b02923d5823235df764c59ecbc589870d38d797f68d78cac4c13eae78133.md) |

## Connected chat exports

| Source | ID | Snapshot |
|---|---|---|
| connector-intake:chats/01a0f23d-427b-7882-b4e2-567c8015c061/conversation.md | `39a18c9611bc4d2022e6` | [read](text/39a18c9611bc4d2022e6--conversation.md.md) · [raw](objects/sha256/e3/e3f5907daf43fb66701ea2a9a2b53995b7f16791f870d1b07c18da3e86d5f5f1.md) |
| connector-intake:chats/01a100ed-8242-7cb2-84fa-d15b49a1ce9b/conversation.md | `0ccea399e660d6b4221e` | [read](text/0ccea399e660d6b4221e--conversation.md.md) · [raw](objects/sha256/b2/b25b342b58b6b6d5210219ddc97bf647b2ce76136990be9232bd83e7ab03e925.md) |
| connector-intake:chats/01a10c3d-0091-7df2-8a3b-01c24d3edb83/conversation.md | `a67e6567414fd102db4a` | [read](text/a67e6567414fd102db4a--conversation.md.md) · [raw](objects/sha256/c5/c54992b0c505a32a3ceb90b8eba3a001d802108090739b0088f075f7e0b3be6f.md) |
| connector-intake:chats/01a116f2-d5d7-7190-860d-2f8b7d7c7d0f/conversation.md | `2dda853c7eb12414d740` | [read](text/2dda853c7eb12414d740--conversation.md.md) · [raw](objects/sha256/e9/e9b12f6ea06e11bc937594c4d7d528420e60eb35ea73f590939430efd794c92b.md) |
| connector-intake:chats/6ab52933-9c18-83ee-9b6a-9de48ba6eaa9/conversation.md | `5ae1be285d5a7773953c` | [read](text/5ae1be285d5a7773953c--conversation.md.md) · [raw](objects/sha256/03/03bfb17d2c942d7765a85547b9a09026f8326b0a92ef400e038f3ec699b49937.md) |
| connector-intake:chats/6ab5e2f1-a8ec-83e8-a9e6-a57dac34bb00/conversation.md | `1f68beb4fd47998232dd` | [read](text/1f68beb4fd47998232dd--conversation.md.md) · [raw](objects/sha256/45/45cf8bfc122ca931a42d08924b6ac623d32fc7b2181f9c5f4f6bc002d39ec9e9.md) |
| connector-intake:chats/6aca197c-2f7c-83ee-aa5a-e7b606718202/conversation.md | `5ff50638ee53f122f835` | [read](text/5ff50638ee53f122f835--conversation.md.md) · [raw](objects/sha256/3a/3a50ee12661dba384dc2167228d74f8103d6406702690e20eea6b3753d1effcb.md) |

## Project email and purchase evidence

| Source | ID | Snapshot |
|---|---|---|
| connector-intake:connectors/email-19e69b57fdfdc2d1.md | `86af76160d91358bf924` | [read](text/86af76160d91358bf924--email-19e69b57fdfdc2d1.md.md) · [raw](objects/sha256/63/63137fe6ec0bb7ef8a3f1f0baeeec24c62e0f9e658a0dc954bd1e740595896f6.md) |
| connector-intake:connectors/email-19e6c086d56fbc3e.md | `15e9ab6d677fb3fdbc0c` | [read](text/15e9ab6d677fb3fdbc0c--email-19e6c086d56fbc3e.md.md) · [raw](objects/sha256/04/0478f3d778467e072b3fdea58885fb2b2897d3332f7f5d62e2ec60e8b9806aae.md) |
| connector-intake:connectors/email-19e8d13b4298a034.md | `dbdc918fbfc638a81b7e` | [read](text/dbdc918fbfc638a81b7e--email-19e8d13b4298a034.md.md) · [raw](objects/sha256/1d/1de576647f8be5ae87d372ea75ac4f8a51169431746c601ffac7d6677a76b0e7.md) |
| connector-intake:connectors/email-19f173f236e6c4ad.md | `86ceb792c54e35f24818` | [read](text/86ceb792c54e35f24818--email-19f173f236e6c4ad.md.md) · [raw](objects/sha256/70/7007ba295782fd20b2490ac66b9b8a1de0ba271cc0dc1a3d3c2a4b5ecb1c1085.md) |
| connector-intake:connectors/email-19e799d456189f4e.md | `13143d65f7bcbc0199bc` | [read](text/13143d65f7bcbc0199bc--email-19e799d456189f4e.md.md) · [raw](objects/sha256/58/58adfaf9302d0f19df57fb0687be64ec3db85a60943af1134d2176c4992833c4.md) |
| connector-intake:connectors/email-19e82db2335b2ba2.md | `fad157ace93a115fb7b5` | [read](text/fad157ace93a115fb7b5--email-19e82db2335b2ba2.md.md) · [raw](objects/sha256/1f/1fa992afded148a20d2d14074a6574b04ee331fd88d7ef0d264356b6a9232f18.md) |
| connector-intake:connectors/email-19e8b6ff298aea83.md | `400bf5418d048aaa03ac` | [read](text/400bf5418d048aaa03ac--email-19e8b6ff298aea83.md.md) · [raw](objects/sha256/52/52f41f0239ae75dd78e2da9cd4a35af5c630b2f0a8a4b19ea4cf5411d749943c.md) |
| connector-intake:connectors/email-19ea0258a3bcf6c1.md | `10ad64bb4a44ce84170a` | [read](text/10ad64bb4a44ce84170a--email-19ea0258a3bcf6c1.md.md) · [raw](objects/sha256/0a/0aafe28f84a715c6a38c243354f1371731b69858c0690228b4e9a4e0db7ce7eb.md) |

## Google Drive originals: concepts, presentations and budget

| Source | ID | Snapshot |
|---|---|---|
| FRC \| Science Fair \| Vacuum Robot | `95855215860e00691ab4` | [read](text/95855215860e00691ab4--FRC%20_%20Science%20Fair%20_%20Vacuum%20Robot.pptx.md) · [raw](objects/sha256/07/0795ea4a2b9a979a66823431ac17297ff7824b240550d85603b3dd05274b162e.pptx) |
| Vacuum Robot | `5ae3ff536e70db678760` | [read](text/5ae3ff536e70db678760--Vacuum%20Robot.pptx.md) · [raw](objects/sha256/84/84db0e2d24d0fdb046dd36d505412ded6dfee69682c525b51bc8af9d8cebe7a0.pptx) |
| FRC _ Science Fair _ Vacuum Robot.pptx | `b2979acc3613c2896281` | [read](text/b2979acc3613c2896281--FRC%20_%20Science%20Fair%20_%20Vacuum%20Robot.pptx.md) · [raw](objects/sha256/16/160ede0f209d2df3ee1e00c17e5824da354801543ce05dfa5e211f0a65bc3b2b.pptx) |
| FRC___Science_Fair___Vacuum_Robot | `4b14cc1606a41cf44530` | [read](text/4b14cc1606a41cf44530--FRC___Science_Fair___Vacuum_Robot.pptx.md) · [raw](objects/sha256/c8/c8b2d87e5d55c2e637d63c0c8c8b03faf773681ac0fe5b4e1d1d37b9011608ac.pptx) |
| Arduino Vacuum Cleaner | `f64638aac74c5700efce` | [read](text/f64638aac74c5700efce--Arduino%20Vacuum%20Cleaner.pptx.md) · [raw](objects/sha256/5c/5cc25445f4e8d4b2966a78d0824414252c8f8e9c74cfcb4f43dfbc373ab1e5e1.pptx) |
| ROBOT_MASTER | `6be05a3ff60d379c1829` | [read](text/6be05a3ff60d379c1829--ROBOT_MASTER.docx.md) · [raw](objects/sha256/b9/b908fe2fd69b14e15d3de9f84d8d6478e8d4cd5b86e98a3b57b93d191be06b13.docx) |
| Untitled document | `99c11c4cb8d8bd55338b` | [read](text/99c11c4cb8d8bd55338b--Untitled%20document.docx.md) · [raw](objects/sha256/9d/9dc6963e84f9c54e6ab2c9424254a5ec4879967f17b24838c06f6bd3155ceb31.docx) |
| Untitled document | `7cd6ee941d4e4c49c2ff` | [read](text/7cd6ee941d4e4c49c2ff--Untitled%20document.docx.md) · [raw](objects/sha256/ee/eedf8fb6b8b4162cb889b6edcd9d852895507bb3158aba0d7ba7edbbfba9ad67.docx) |
| 機器人材料費 | `614ace17f37c6b03b295` | [read](text/614ace17f37c6b03b295--%E6%A9%9F%E5%99%A8%E4%BA%BA%E6%9D%90%E6%96%99%E8%B2%BB.docx.md) · [raw](objects/sha256/e0/e0c14f794729066d0345f926d8a6cb4d0d3b6ab21d93a0be57e94afffb34c150.docx) |
| Untitled presentation | `eb56792ba9abb48d9699` | [read](text/eb56792ba9abb48d9699--Untitled%20presentation.pptx.md) · [raw](objects/sha256/92/92869e79bd16946fe15ea17b5b3b766dbaa60313cf2f56aded35a3dc00665bbb.pptx) |
| AIVac | `5b6e242015394129e1b1` | [read](text/5b6e242015394129e1b1--AIVac.pptx.md) · [raw](objects/sha256/8f/8f694776130eb4601fbd954040cdb450a3b00e490322b51c7c46c52fe2dffd59.pptx) |

## Git history

| Source | ID | Snapshot |
|---|---|---|
| connector-intake:git/Argus_Vac_Dashboard.bundle | `798218ee4217231bdc08` | [read](objects/sha256/5a/5af38a0a50ad61bbb044ea9a781012d65c9cd22b1a85abfd31de9d0eb4d9b502.bundle) · [raw](objects/sha256/5a/5af38a0a50ad61bbb044ea9a781012d65c9cd22b1a85abfd31de9d0eb4d9b502.bundle) |

## Additional BOMs, wiring, CAD and exported reports

| Source | ID | Snapshot |
|---|---|---|
| local-extra-001:Argus Vactextfile.pdf | `2c6f3f8f6ce8f3abf076` | [read](text/2c6f3f8f6ce8f3abf076--Argus%20Vactextfile.pdf.md) · [raw](objects/sha256/61/61f3b085b76f01eeec8f6b1ee8eaf068696a8c00160fb7e17646f872d1c83469.pdf) |
| local-extra-004:FRC _ Science Fair _ Vacuum Robot (1).pdf | `76f81cd2f706be538034` | [read](text/76f81cd2f706be538034--FRC%20_%20Science%20Fair%20_%20Vacuum%20Robot%20_1_.pdf.md) · [raw](objects/sha256/5c/5cd098e6fce5dde3e78c49a120006dcf9226e5f6084f2bbf081de40bac7ccf92.pdf) |
| local-extra-006:FRC _ Science Fair _ Vacuum Robot (2).pdf | `d8f9ef4fd818dd6f0aab` | [read](text/d8f9ef4fd818dd6f0aab--FRC%20_%20Science%20Fair%20_%20Vacuum%20Robot%20_2_.pdf.md) · [raw](objects/sha256/79/792e84ecbc06074d6ff63188ec2dfd28e60333833bcb2f1d9140a26204cf5362.pdf) |
| local-extra-007:FRC _ Science Fair _ Vacuum Robot.pdf | `06fcfbaa2d5e45d542df` | [read](text/06fcfbaa2d5e45d542df--FRC%20_%20Science%20Fair%20_%20Vacuum%20Robot.pdf.md) · [raw](objects/sha256/a2/a2fd874ffe825775fc2c1a43139132f6b04d0b3490b22782d92459a4696bebaf.pdf) |
| local-extra-187:Vacuum Robot.csv | `9d8980cc66ced1eef7f1` | [read](text/9d8980cc66ced1eef7f1--Vacuum%20Robot.csv.md) · [raw](objects/sha256/9e/9ed0d6916c054177a6e5f5ec02dea7a6e9fed9e4c6e887b8b2bb35fe48371bad.csv) |
| local-extra-190:Argus Vac.fz | `f4d088b886096cd7aab4` | [read](text/f4d088b886096cd7aab4--Argus%20Vac.fz.md) · [raw](objects/sha256/ca/ca022004930c6eba7dfa32d09d96ab2e81b57f6b092d2640046b59d0d84fc271.fz) |
| local-extra-191:Argus Vac.fzz | `cad8ec6481825ae7b036` | [read](text/cad8ec6481825ae7b036--Argus%20Vac.fzz.md) · [raw](objects/sha256/86/86719e283660bc0054cc67da7a5ec095355bde3f40e73c92d266a0b0eee24370.fzz) |
| local-extra-192:Argus Vac1.fzz | `0c3b8998f36b9eda5fdd` | [read](text/0c3b8998f36b9eda5fdd--Argus%20Vac1.fzz.md) · [raw](objects/sha256/86/86719e283660bc0054cc67da7a5ec095355bde3f40e73c92d266a0b0eee24370.fzz) |
| local-extra-194:Argus Vac_Bill Of Materials_csv.csv | `7300408f6dfe9cc64666` | [read](text/7300408f6dfe9cc64666--Argus%20Vac_Bill%20Of%20Materials_csv.csv.md) · [raw](objects/sha256/09/0949350d18ae34ccf6bbbe3fbf3a3fab4380984d25ea8cbc1615a8119b2d21a2.csv) |
| local-extra-195:Argus Vac_bom_csv.csv | `1bed6d79ed4cb0a10406` | [read](text/1bed6d79ed4cb0a10406--Argus%20Vac_bom_csv.csv.md) · [raw](objects/sha256/2d/2d4ac136ebc82b829927077a6d075df77d4b18f32f30d8a3a2a986a24371938a.csv) |
| local-extra-201:Vacuum Robot.csv | `1f6e130124783eddbd7c` | [read](text/1f6e130124783eddbd7c--Vacuum%20Robot.csv.md) · [raw](objects/sha256/9e/9ed0d6916c054177a6e5f5ec02dea7a6e9fed9e4c6e887b8b2bb35fe48371bad.csv) |
| local-extra-204:A4988-Stepper-Driver-WithPins.stp | `f995b5813ed82fe430ee` | [read](objects/sha256/e7/e71818427e73cd5bfebfe040488cae04f85c4359cd29184955742a7a0703a5e5.stp) · [raw](objects/sha256/e7/e71818427e73cd5bfebfe040488cae04f85c4359cd29184955742a7a0703a5e5.stp) |
| local-extra-205:A4988.fzz | `7d190171a1c19fd7173e` | [read](text/7d190171a1c19fd7173e--A4988.fzz.md) · [raw](objects/sha256/1f/1f64e51c0f88469f3981f83e4e3ea651b5110934bcceb2ab741e7b34454e8899.fzz) |
| local-extra-220:planetary-gearbox-+slim.shapr | `c056b792b74b22f27be3` | [read](objects/sha256/74/74b86aee45519f1b4ef4d55a3692af11350fee1568489bd8792539f7d43fa494.shapr) · [raw](objects/sha256/74/74b86aee45519f1b4ef4d55a3692af11350fee1568489bd8792539f7d43fa494.shapr) |
| local-extra-221:planetary-gearbox-+slim.step | `bb79ceaec8c4e316e330` | [read](objects/sha256/a1/a1eadbf5357596f890a06951b73e44b2ece56177b62e6b0c7c7ad78e01a7de68.step) · [raw](objects/sha256/a1/a1eadbf5357596f890a06951b73e44b2ece56177b62e6b0c7c7ad78e01a7de68.step) |

## Recovered local Codex visible messages

| Source | ID | Snapshot |
|---|---|---|
| connector-intake:local-codex/01a038d4-e7c4-7730-be8d-d45ea5e75e99/conversation.md | `c14af90914aca067cabc` | [read](text/c14af90914aca067cabc--conversation.md.md) · [raw](objects/sha256/0f/0f89987fbf5eb8a38b33e3f859276493fa251dd37a1144af01cb3769d97a3ba7.md) |
| connector-intake:local-codex/01a038dc-064e-7681-bb85-6e15aaa8bdfe/conversation.md | `1cf3388a680c44cc51ab` | [read](text/1cf3388a680c44cc51ab--conversation.md.md) · [raw](objects/sha256/c4/c4630adf9f9608716710a4c0d0fe619bdb972719591054212e29ca62cce92e3c.md) |
| connector-intake:local-codex/01a0f23d-427b-7882-b4e2-567c8015c061/conversation.md | `7577322351703b098efd` | [read](text/7577322351703b098efd--conversation.md.md) · [raw](objects/sha256/f1/f12f5f0b8c79210a0392bfef4ec119a3f4abf882f90ba25e69fad7db7be5f8cd.md) |
| connector-intake:local-codex/01a100ed-8242-7cb2-84fa-d15b49a1ce9b/conversation.md | `a95497cf05084ae93d4a` | [read](text/a95497cf05084ae93d4a--conversation.md.md) · [raw](objects/sha256/e9/e938007f3ffe18352fa0e77f0bb5773467314ff56386390a11c1343c183fbc65.md) |
| connector-intake:local-codex/01a10c3d-0091-7df2-8a3b-01c24d3edb83/conversation.md | `e16cf5067ce2833ea55f` | [read](text/e16cf5067ce2833ea55f--conversation.md.md) · [raw](objects/sha256/cf/cf48d4610b3e999d0464a20d05a93915eda303d10fc1b1d660153d72d1f3d729.md) |
| connector-intake:local-codex/01a116f2-d5d7-7190-860d-2f8b7d7c7d0f/conversation.md | `af9e52d7bff4a43525fd` | [read](text/af9e52d7bff4a43525fd--conversation.md.md) · [raw](objects/sha256/8e/8e351d2eb5de382fbc6d9b82de9447d38b958c3ede1efe1fcdbf81a6a5f89c6f.md) |
