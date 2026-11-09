# Argus Vac CAD drafts — 2026-10-13

Open the Design corner and choose `argus-as-built-v1` or `argus-complete-layout-v1`.

The current version includes the detached C1 lid, exposed driver boards/heatsinks,
Mega terminal shield, empty red M12 adapter, front cable coils, camera and caster.
Orange Pi and cleaning hardware are absent from this version.

The completed layout adds trays, battery restraints, cable carriers, shelves/posts
and 33 proposed spatial harness groups. Horizontal M12 and stacked Mega / USB
power bank / Orange Pi reserves fit below the proposed assembled lid. Distinct
board bodies do not intersect in the visible-geometry envelope check. Battery
and adapter mating intentionally overlaps and still requires actual fit checks.
Driver pin labels, coil colors, exact San Ace/N12 models, electrical protection,
USB supply ratings and most mounting dimensions remain unresolved. These routes
cover the planned connection groups; they are not terminal-by-terminal verified
wiring instructions. No hardware was powered or moved.

Both use confirmed3mm circular acrylic plates;300mm stated bounds and65mm estimated
spacer length. Estimated base underside73mm clears70mm wheel tops by3mm; this is
not a measured ride height. Under-plate geometry and component placement still need underside
photos and measurements. All displayed masses are reference estimates, including
unidentified board/adapter weights; measured balance is not established.

Each design has a millimetre STL reference assembly, a fixed-link layout URDF,
route-manifest.json and validation.json in its namesake export folder. The URDF
contains only saved layout geometry, without old simulator solids or plugins.
STL solids are component references, not fabrication-ready mounts. Real connector
exits, cable bend radii, base/lid penetrations and service slack require detail.
Candidate cleaning driver/motor reserves must be resized to actual selected parts;
fan and duct geometry remains unresolved.
