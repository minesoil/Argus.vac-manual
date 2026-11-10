# Keep the explanation beside the code

The public repository is `minesoil/Argus.vac-manual`. Its `robot_control/`
folder is maintained source; `handbook/code/` is a dated teaching/recovery
snapshot. The dashboard discovers newly committed files automatically.
It shows repository content, not the current physical state of Argus.

## After a meaningful change

1. Edit maintained source, not just the snapshot.
2. Run checks appropriate to the changed behavior.
3. Record the actual result and any unfinished physical check in
   `robot_control/PROJECT-STATUS.md` or a dated report.
4. Refresh the snapshot and its inventory with the included exporter. This
   copies reviewed files and excludes private runtime/build material.
5. Review `git diff` and `git status` before committing and pushing.

Do not commit actual hotspot/SSH passwords, `.state/`, real firmware
`config.h`, firmware binaries or tool caches. The dummy config in test stubs
and `config.h.example` are meant to be shared. Git history already preserves
earlier versions; do not call an older report the current state.

## Snapshot exporter

From the local Argus workspace, the exporter uses these roots by default:

```powershell
py -3.12 workspace/argus-handbook/tools/export_snapshot.py --workspace . --handbook workspace/argus-handbook
```

The exporter also supports a public clone with maintained `robot_control/`
and `dashboard/` folders:

```bash
python handbook/tools/export_snapshot.py --workspace . --handbook handbook
```

The Mega references are retained from this reviewed recovery snapshot; the
exporter only refreshes them if the known original local sources exist.
It fails if an unexpected file would be discarded. Resolve that difference
deliberately instead of deleting files automatically. The inventory includes
hashes and the origin of every copied source file.

## Explain a piece of the project in your own words

Choose one feature: for example, the camera-assisted stop. Draw its path from
image to Pi status to UART to the ESP32 latch to Mega zero output. Then explain
why a clear frame does not resume the wheels. Finally, show the matching test
and state what has not yet been checked on the real robot.

A useful description is: “I integrated the Pi's vision with my ESP32/Mega
drive system, with AI assistance for implementation and debugging. I tested
the hardware in stages, and these are the results and remaining limits.”
You do not need to claim you personally typed every recovered command.

## Small learning sessions

Read one source file and its tests at a time. Start with the command wrapper,
then follow one phone request, then read `ManualGuard.h`. Learn ROS after the
physical path makes sense: a topic is easier to understand when you already
know what information must move between two programs.
