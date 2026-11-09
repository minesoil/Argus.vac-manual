# CAD wiring evidence — 2026-10-13

Current state comes from Justin's current statement and current photos. San Ace suction motors, N12 12V brush motors, their drivers and Orange Pi5 are not installed. RPLIDAR C1 sits on the detached lid. The red object is the adapter for his M12 3Ah battery. Battery capacity/adapter arrival are now newer evidence than September's pending-battery notes. None of this establishes electrical continuity, powered operation or final protection settings.

`component-evidence.json` records verified manufacturer reference sizes, mass and the candidate route graph. Unknown board envelopes remain unknown. The nominal Mega37g, OPi46g and C1 110g exclude mounts/cables. M12B3 181g is a conditional compact-battery reference, not a measured mass of Justin's battery/adapter.

## Archive evidence and obsolete Fritzing

- `06eae1cb21dfcba8d63f`: Argus Vac Final.fzz, modified 2026-08-29. Its raw internal FZ was read directly, without running its included sketch. It still models two A4988s, a 5000mAh 3S LiPo, an LM2596, L298N, Wago blocks and a fan-driver substitute named drv-1012. OrangePi is represented by a Raspberry Pi4B image. Camera/lidar USB paths are not represented as connected nets.
- `c78dfd96fd1275c2e95a`: XML netlist dated 2026-08-23, modified August25. It is older than Final.fzz. This XML merges positive and negative actuator buses in net1 and leaves left VMOT with only its capacitor. The later Final.fzz separates those buses and connects both VMOTs to positive. Do not attribute the old XML rail fault to Final.fzz or the physical robot.
- Final.fzz drawn drive pins: left STEP D4/DIR D3; right STEP D6/DIR D5. Brush IN1 D52, IN2 D50, IN3 D46, IN4 D48; ENA D13, ENB D12. Fan substitute control pins4/8 go to D9/D8. These differ from the historical manual/firmware pin maps, and are obsolete for the present TB6600 interface.
- Final.fzz still draws LM2596 regulated 5V to Mega VIN. Official Mega VIN recommendation is7–12V; retain USB power in the proposed computing architecture instead of copying this connection.
- Final.fzz draws LiPo positive → switch → fuse → positive distribution. New candidate CAD places the fuse close to adapter positive. Historical DaKoang switch only has recovered AC markings250VAC10A/125VAC15A; its suitability as a DC motor cutoff is unverified.
- `e84583dda7f9bde230e9`: electrical manual, revised September27. It explicitly says Fritzing drv-1012 is a substitute for an actual IBT-2, and historically assigns L298N to the two N20 brushes. It records separate motor battery and USB computing-power-bank architecture, 10A blade fuses, 12AWG inline holders, 14AWG adapter leads, LM2596 and Wago distributions. The manual's old A4988 and fan pin assignments cannot establish present wiring; its fan allocation reuses historically dead D2.
- `87b42cf22476245ab36c`: raw ROBOT_MASTER September27 update. Both NEMAs moved below chassis; one NEMA was wired then, camera/lidar mounted, adapter awaited. Today's user state supersedes installation/arrival assumptions. Older N20 label is retained as history alongside current N12 label.
- `2dda853c7eb12414d740`: October robotics chat. User confirms two NEMA17s, two TB6600s, 70mm wheel diameter. Simulator16×12m/1.5m/s values are not physical validation.
- `5ff50638ee53f122f835`: October10 TB6600 chat. User confirms barebones TB6600 with blue current potentiometer and1.7A NEMA17. Exact terminal labels and input circuit were not recovered. Do not use boxed common-anode TB6600 dimensions or optocoupler wiring as proof.
- `8d2072f762edb271d396`: RobotLab hardware guide October8. Proposed allocation left/right STEP D22/D23, DIR D24/D25, optional ENA D26; stop D27; common-anode module assumption; Pi→Mega USB and Pi→C1 USB adapter. These are software proposals, not actual flashing/physical wiring evidence.
- `1f68beb4fd47998232dd`: battery chat September25. User says total setup should be≤7.5A, without measured maximum; user explicitly had NOT bought XH-M609 then. No evidence establishes purchase/current rating/configuration. Model a generic planned protection envelope rather than claiming an installed XH-M609 or a selected threshold.
- Workshop chat `workspace/codex/01a12b5e-e226-7622-84a5-7a5572795600.md` already records an assistant correction for treating September's adapter-pending note as current. This explains some mixed stage reporting.

## Routing and layout implications

Use separate as-built observed routes and proposed completed routes. Photographs showing wire presence cannot establish which obscured terminal it reaches. Mark uncertain endpoints explicitly.

For the completed layout, reserve one short protected battery-power route and fixed positive/return Wago carriers. Place each drive driver near its own motor exit; route each four-wire coil harness as a bundle away from wheels. Make control/USB routes accessible separately from motor bundles. Preserve USB plug and bend envelopes, terminal screwdriver access, driver cooling, fuse access, battery insertion/removal and a protected removable-lid harness. A third/triangle spacer limits possible trays and route crossings; do not route through its mechanical envelope.

Use screw-mounted board trays/standoffs, clips and a restrained battery-adapter mount to address sliding. A peripheral harness channel can clear the centre for suction/dust path. Heavy actual motor/battery/plate masses need measurement/model identification before a centre-of-mass claim; PCB catalogue masses alone cannot establish robot balance.

Retain the historical split computing/actuator sources in the proposal, pending actual power-bank rating. Nonisolated driver controls require a shared signal reference; optical TB6600 isolation must be confirmed before deciding its reference wiring. USB does not guarantee absence of ground loops. Do not join separate positive supplies or retain obsolete buck5V→MegaVIN. Proposed full cables are spatial planning, not a ready-to-energize terminal schedule.

Remaining exact identifiers: TB6600 terminal/current circuit; San Ace model/quantity/voltage/control wires; N12 versus N20 model/stall rating; actual L298N/IBT-2 variant and jumpers; M12 compact/XC SKU and adapter envelope; protection/switch DC ratings; camera, computing power bank, USB adapter/hub and actual deployed Mega firmware.

## October11 photo-label audit

Five closeups from the recent chat titled **Stepper Wiring Safety Check** were inspected: IMG_5421–IMG_5425. The temporary preview originals were readable. Current IMG_5457/IMG_5460 were inspected for comparison.

Source chat ID: `6acb3fd5-4978-83ee-8bd4-582ad636a1d7`; photo date2026-10-11. Original-name copies and SHA-256 records are preserved in `workspace/exports/cad-reference/recent-wiring-photos/observations.json` alongside all five JPEGs.

Both drive boards are bare green PCBs with large finned aluminium heatsinks. Each has a six-position screw block for the motor/supply side and a four-position block opposite for controls; a blue trimmer; M1/M2/M3 labels by selector pads/header; and a white socket labelled **半流开关** (half-current switch). GND is readable at the six-position block; the remaining small control/power/coil labels are too faint or obscured for dependable transcription. Exact PCB/chip identity and whether the inputs are isolated remain open. The observed geometry does not match the boxed six-terminal PUL±/DIR±/ENA± driver assumed by RobotLab. Current photos show the same visible board architecture, with changed placements; no serial identity or continuity is claimed.

IMG_5421 clearly shows a physically present blue relay/display board with **VIN** and **VOUT** two-pole blocks, three-digit LED display, two buttons, gold toroid and four corner holes. Its relay reads **HeFeng SRA-S-105DM**, **20A14VDC**, **10A250VAC**. These are relay markings, not verification of whole-board continuous rating or selected cutoff settings. Exact PCB model is not legible; retain “blue voltage-cutoff module, model pending” instead of asserting XH-M609. Current IMG_5457 shows the same visible cutoff-board architecture. This supersedes treating September's not-bought statement as present absence.
