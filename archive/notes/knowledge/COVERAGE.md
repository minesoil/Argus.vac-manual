# Collection coverage and limits

As of 2026-10-10, Asia/Taipei. The collection was project-specific and read-only
for originals outside this repository.

## Collected

- `[REDACTED_HOME_PATH]`: project manuals, raw notes,
  logs, current/archived software, wiring, detector model and fixtures, saved
  Copilot conversations, voice notes/audio, project agent-memory notes and canvases.
- Older general Obsidian vault at `OneDrive\Documents\Obsidian Vault`: filename
  and note-content searches found no additional matches for the project, lidar,
  Orange Pi, NEMA 17 or A4988 terms. The dedicated Argus vault above was recovered.
- Local OneDrive/Documents/Desktop/Downloads searches: project-named files,
  BOMs, Fritzing diagrams/netlists/parts, older detector versions, diagrams,
  PDFs and slides, AIVac/Zoo CAD projects, planetary gearbox and shaft files,
  lidar SDK and fan CAD references.
- September/October Codex work folders for the simulator setup, resumed RobotLab
  work, A4988 diagnostics and shaft CAD. Project source and reports were retained.
- Live `VacuumRobot-24.04` WSL workspace `/home/robot/vacuum_ws`: source, launchers,
  project configuration, maps, validation artifacts and historical model backups.
- Eleven related Drive files: seven presentation originals/exports and four Docs,
  including ROBOT_MASTER, early AIVac specification, budget and portfolio notes.
  Native files were exported as DOCX/PPTX; a stored PPTX was downloaded unchanged.
- Eight matching email messages: ArgusVac model-training evidence and four
  notifications for a component order. Original MIME data and readable copies
  are retained. Archived order links were not used to enter a shop account.
- Seven connected chat exports and six local Codex visible-message exports,
  with four overlapping chats: nine distinct chat IDs, plus conversations
  already saved inside Obsidian. Seven exposed image attachments were preserved.
- `Argus_Vac_Dashboard` local files and a verified Git bundle containing its
  initial commit and refs. Connected GitHub repository searches found no matches.
- Project and global Codex memory lookup instructions, a source-backed summary,
  structured facts, decision chronology, open questions and a topic map.

## Exclusions and gaps

Generic agent skills, plugin/application state, authentication files, embedding
caches, bytecode, downloaded runtime installers and rebuildable dependency/build
trees were omitted. `discovery/exclusions.json` records the selections. A password
setup script was excluded; embedded API keys in three archived agent setup files
were replaced with `REDACTED_API_KEY`. External originals were not changed.

No files were accessed directly from the physical Orange Pi or an unavailable
Gemini workspace. The vault's mention of an original Gemini-only diagnostic
sketch does not establish that it was collected. Saved local conversations and
downloaded Arduino sketches were preserved where found.

Connected chat exports are limited to content exposed by the read tool. Some tool
outputs are truncated. Recent TB6600 assistant answers were returned as reference
placeholders; user statements and the attachment were recoverable. The tool's
`hasMore=false` is not a guarantee that all historical ChatGPT messages exist in
the export. Local Codex extraction preserves visible user/assistant messages;
internal prompts, hidden reasoning and tool records were excluded there.

There was no custom saved-design directory at the documented
`%LOCALAPPDATA%\VacuumLab\designs` location during collection. Default designs,
WSL applied designs and model backups were collected. RobotLab's referenced
`reports/quality-review.json` was not present. Historical reports are not fresh
proof of physical behavior or completion of the last audit.

Binary media and CAD originals are preserved even when searchable text is
unavailable. PDF text extraction does not OCR image-only pages, and document
extraction is for retrieval, not an assertion of visual-layout verification.
ZIP/tar text retrieval is bounded per member; complete container files remain
preserved. Native Drive exports preserve an editable offline snapshot, not
Google revision history or comment threads. Older cloud revisions were not
requested or enumerated.

## Persistence boundary

`AGENTS.md` gives Codex a persistent instruction to retrieve the archive. This
is a file-based knowledge system rather than a promise of perfect model memory.
Global lookup works while its pointer and this folder are available; update the
pointer if the archive moves. The archive can be attached/copied elsewhere, but
ordinary ChatGPT conversations do not automatically receive local Codex files.
The implementation follows OpenAI's [AGENTS.md guidance](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

No scheduled refresh or automatic cloud synchronization was configured. New
facts should be recorded by future project work. The final count, storage totals
and integrity result are in `stats.json` and `verification.json`.
