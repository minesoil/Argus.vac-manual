# Argus dashboard

Static GitHub Pages dashboard for `minesoil/Argus.vac-manual`. Replaces the old
Onshape guide at the site root. No framework, build service, API key or robot
connection is required. Git history retains the old website.

## Updating it

Publish `index.html`, `dashboard.css` and `dashboard.js` to the repository root.
The dashboard reads the latest main commit through GitHub's public API, then
uses that exact commit for both the file list and content. New files and folders
appear automatically, including files outside robot_control/. Two API requests
are used per refresh; file content is fetched from raw.githubusercontent.com.

GitHub's unauthenticated API can be rate limited. A cached listing in the browser
and the committed `catalog.json` provide older snapshots as fallbacks. The page
labels fallback data; Refresh retries GitHub. Snapshot file content still needs
network access. Never put a GitHub token into the browser code.

`catalog.json` contains a commit SHA and `files: [{path, size}]`. Regenerate it
from the repository tree when publishing a dashboard release. It is only a
fallback; normal operation discovers files automatically.

Update the dated progress note in index.html and PROJECT-STATUS.md when physical
validation changes. It is recorded progress, never live robot telemetry.
Add reviewed descriptions to `explanations` in dashboard.js for important new
files. New files without one receive a clearly labeled general explanation.

## Rendering and security

Markdown supports headings, paragraphs, lists, fenced code, links, images,
tables and blockquotes. Raw HTML is treated as text. Code uses line numbers and
basic syntax colors; Source shows the exact text. HTML and scripts are never
executed as file previews. Images use normal image loading; other formats and
files larger than 1 MB link to their originals. No code editing or motor control.

Use GitHub for private settings and uploads only after reviewing them; the
dashboard shows public repository contents. Credentials, compiled firmware
containing them, raw private chats and caches must stay out of the repository.

## Local preview

Serve this folder with a static HTTP server, e.g. `python -m http.server 8080`.
Open http://localhost:8080. Do not open index.html via file:// because browser
fetch rules differ. Test desktop and narrow screens, search/filter, direct file
links, markdown/code/source switching, copy, missing files, API failure fallback,
and unsafe HTML/URL input before publishing changes.
