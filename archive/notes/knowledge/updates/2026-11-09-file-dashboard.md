# File dashboard — 2026-11-09

Justin explicitly requests replacing the old Onshape website with a dashboard
for formatted repository files and explanations, designed for future additions.
This supersedes the earlier instruction to preserve the old website in place.
Its content remains recoverable through Git history.

Implemented in workspace/dashboard; published to minesoil/Argus.vac-manual main:
https://github.com/minesoil/Argus.vac-manual/commit/19637658bc0318a98e04bc75c876d4a948e5cf5b

Includes searchable nested file browser, Docs/Code/Tests filters, Markdown
renderer, line-numbered source with basic highlighting, copy/raw/GitHub links,
images, per-file explanations and mobile layout. Unknown files use an honest
general explanation. Latest-main GitHub tree discovery includes future folders;
cached listing and bundled snapshot are labeled when GitHub is unavailable.
No authentication tokens, robot telemetry or driving controls are included.

Milestones are explicitly dated November 9: short tape run verified; phone
Start installation pending; camera obstacle stop planned. These require manual
status updates when physical evidence changes. New files appear automatically.

Playwright headless Chromium checks passed: formatting, source, safe handling
of raw scripts/unsafe links, discovery, search/filter, direct links, mobile width,
cached and bundled fallback, and missing-file handling. Desktop/mobile screenshots
were generated locally. Initial Pages request after commit still served the old
cached build; deployment propagation is checked separately before final handoff.

Final deployment verified: GitHub Pages serves title "Argus / Project dashboard".
A real headless browser loaded the public site, discovered 63/63 files from
commit 1963765, and rendered PROJECT-STATUS.md. Live screenshot:
.tmp/argus-dashboard-live.png (local-only verification artifact).
