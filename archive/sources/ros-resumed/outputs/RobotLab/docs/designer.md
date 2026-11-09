# Edit the robot

Choose **Design robot** in the launcher. The editor runs locally and loads its graphics library from this project; it needs no account or internet connection. The supplied assembly has 17 separately editable parts, including both chassis plates, standoffs, wheels, motors, drivers, boards, lidar and camera.

Click a part in the list or 3D view. Drag the coloured arrows to move it. **Move** and **Rotate** switch the handle; `W` and `E` do the same. Right-drag to orbit, middle-drag to pan and scroll to zoom. **Top**, **Front** and **Fit** change the view. Snap defaults to 5 mm, with 5-degree rotation steps; set snap to zero for free placement.

The properties panel accepts exact position in millimetres and rotation in degrees. X points forward, Y left and Z up from the floor reference. JSON stores metres and radians. Size and mass are editable. Wheel size is diameter × diameter × width; supplied wheel assemblies have a built-in 90-degree cylinder rotation, so their part rotation starts at zero.

## Add and remove parts

Choose a library part and press **Add part**. The library includes your electronics, a battery, chassis plates, a wheel housing and custom boxes, cylinders and spheres. New parts are fixed attachments. **Duplicate** copies a selected part as another fixed attachment. **Remove** removes it from the design. Undo/redo keeps the last 30 edits; keyboard shortcuts are Ctrl+Z and Ctrl+Y.

**Import STL** accepts a local STL up to 8 MB. Choose the file's units, then set its position and mass. Imported meshes keep their authored origin. Their dimensions define an approximate collision box; they do not calculate a measured centre of mass. A flat or invalid mesh is rejected. Use a solid mesh with thickness for a physical part.

## Save, export and simulate

**Save** writes the file name shown at the top. Enter a new name to save another design. Names accept letters, numbers, hyphens and underscores. Existing files keep timestamped copies in `history/`. Two editors cannot silently overwrite each other's changes: a conflicting save asks you to reload or choose another name. Unsaved changes produce a close/reload prompt.

**Export robot** downloads a ZIP containing `design.json`, a simulation URDF, a hardware URDF and imported meshes. **Import JSON** opens one of these design files. Exports preserve layouts that are unsuitable for differential drive, so you can keep working on them.

**Check layout** verifies wheel geometry. **Apply to simulator** saves the design, stops the owned simulator, creates a backup, updates the model/controller/obstacle footprint, rebuilds and restarts. Close the driving panel first. The update runs in the background and reports its stage. If rebuilding or startup fails, source changes roll back and the simulator stays stopped; inspect the reported error before restarting.

The simulator needs the supplied left wheel, right wheel and lidar. Both wheels must have equal diameter/width, a shared X position, parallel Y axles, and centre Z at half their diameter. Left wheel Y must exceed right wheel Y. Boards, motors, chassis and sensors can move independently. The editor checks drive geometry, not mechanical mounting strength, wiring clearance, torque or collision-free assembly.

For the Orange Pi, copy the saved JSON into this project's `designs/`, then run `python3 tools/deploy/export-hardware.py designs/your-design.json` and rebuild. This updates the physical model and wheel geometry while keeping its speed limits and disabling motion for recalibration.
