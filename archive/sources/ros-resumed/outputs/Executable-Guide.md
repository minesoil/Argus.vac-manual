# Vacuum Lab executable

Double-click **Vacuum Lab.exe**. The launcher has the driving, mapping, navigation, map-saving and stop controls. Click **All project files** to browse and search the project.

The file area includes the live Ubuntu workspace, models/worlds/configuration, tools, maps, session logs, validation results, rollback backups, ROS packages, the original Windows project, Ubuntu disk/image files, and the full Ubuntu backups. Hidden files are included. Double-click folders to browse. Search matches file and folder names recursively from the current folder; clear the search and refresh to return to normal browsing. Directory links are listed but recursive search does not follow them.

Use **Open** to open Windows files in their associated app and Linux files in VS Code. **Show in Explorer** reveals the file or opens the current folder. **Copy path** copies its Windows-accessible path. Permission errors are shown in the status area. Searches stop after 45 seconds and report partial results if needed; choose the workspace or a specific folder for project searches.

The EXE contains the launcher scripts, guides, previews, validation reports, executable build source, and **vacuum-workspace-source.tar.gz**, a snapshot of source, tools, maps and validation results. Only the EXE is needed to launch the app; it extracts its bundled files automatically into `%LOCALAPPDATA%\VacuumLab\app`. Find that folder through the first file-browser location. Keep editable custom profiles there or save them to a folder you choose.

The app uses your existing **VacuumRobot-24.04** WSL installation for ROS 2 and Gazebo. Ubuntu, ROS and Gazebo remain on their existing drives. Moving the EXE to another Windows PC also requires that Ubuntu installation; the EXE is not a replacement for the multi-gigabyte Ubuntu backup.

Optional command-line modes: `--drive` opens the drive workflow, `--files` opens the file area, and `--check --report <path>` checks the bundled launcher without starting simulation or motion. Normal startup opens the menu and leaves the controller disarmed.
