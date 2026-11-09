# CAD reconstruction — request, evidence and editable drafts

## 2026-10-13 — current physical robot

Source: Justin's direct message in this project's Codex chat, dated using
Asia/Taipei client time:

> i want you to make the cad of my robot as close to the one i have rn irl. i can show u as many pics of my robot from any angle as much as you need, just ask me.

Confirmed objective: match the present physical Argus Vac robot in CAD, and
provide a separate proposed completed layout. Justin subsequently supplied seven
Library photographs, now archived with readable view captions in the
[photo evidence catalog](../workspace/exports/cad-reference/photo-evidence.json).

The original default assembly was an older estimate, preserved as
[legacy-layout-estimate.json](../workspace/designs/legacy-layout-estimate.json)
and in Workshop revision history. It is historical reference data.

Available evidence includes overview, chassis and detached-lid overhead views,
side views and front-camera detail. The [current build update](CURRENT_BUILD_STATE.md)
records the stated 300 × 300 mm bounds, circular photo-observed outline and three
60–70 mm spacers. The [latest correction](updates/2026-10-13-plate-thickness-correction.md)
sets acrylic thickness to **3 mm**, superseding the earlier 10 mm statement.

## 2026-10-13 — saved draft delivery

- [Current robot CAD draft](../workspace/designs/argus-as-built-v1.json): photo-informed
  reconstruction with the detached lidar lid. This is now the Workshop default.
- [Completed-layout proposal](../workspace/designs/argus-complete-layout-v1.json):
  editable placement, retention and spatial harness proposals, including reserves
  for the uninstalled components.
- [Export notes](../workspace/exports/cad-reconstruction-v1/README.md): layout-only
  URDF/STL exports, route manifests and software validation reports.

Both are editable CAD drafts. Component positions, unmatched model envelopes,
masses and the 65 mm spacer choice are estimates. Exact underside geometry,
mounting dimensions, adapter mating fit and wire endpoints still need evidence.
Software checks and exports do not establish physical fit, measured balance or
terminal-by-terminal electrical continuity. No hardware was powered or moved.
