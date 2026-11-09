from pathlib import Path
import shutil
import ast

root = Path('/home/robot/vacuum_ws/src/vacuum_sim')
backup = Path('/home/robot/vacuum_ws/performance-originals')
backup.mkdir(exist_ok=True)
changes = {
    'config/view.rviz': [('Frame Rate: 30', 'Frame Rate: 15')],
    'worlds/room.sdf': [('<shadows>true</shadows>', '<shadows>false</shadows>'),
                        ('<cast_shadows>true</cast_shadows>', '<cast_shadows>false</cast_shadows>')],
    'urdf/vacuum.urdf.xacro': [
        ('  <xacro:property name="wheel_radius"',
         '  <xacro:arg name="camera_width" default="320"/>\n  <xacro:arg name="camera_height" default="240"/>\n  <xacro:arg name="camera_rate" default="5"/>\n  <xacro:property name="wheel_radius"'),
        ('<update_rate>10</update_rate><always_on>true</always_on>\n      <camera>',
         '<update_rate>$(arg camera_rate)</update_rate><always_on>true</always_on>\n      <camera>'),
        ('<width>640</width><height>480</height>', '<width>$(arg camera_width)</width><height>$(arg camera_height)</height>')],
    'launch/sim.launch.py': [
        ("Command(['xacro ', str(package / 'urdf/vacuum.urdf.xacro')])",
         "Command(['xacro ', str(package / 'urdf/vacuum.urdf.xacro'), ' camera_width:=', LaunchConfiguration('camera_width'), ' camera_height:=', LaunchConfiguration('camera_height'), ' camera_rate:=', LaunchConfiguration('camera_rate')])"),
        ("        DeclareLaunchArgument('gui', default_value='true'),",
         "        DeclareLaunchArgument('camera_width', default_value='320'),\n        DeclareLaunchArgument('camera_height', default_value='240'),\n        DeclareLaunchArgument('camera_rate', default_value='5'),\n        DeclareLaunchArgument('gui', default_value='true'),")]
}
prepared = {}
for relative, replacements in changes.items():
    path = root / relative
    content = path.read_text()
    for before, after in replacements:
        if content.count(before) != 1:
            raise RuntimeError(f'Expected exactly one matching configuration in {relative}: {before}')
        content = content.replace(before, after, 1)
    if path.suffix == '.py':
        ast.parse(content)
    prepared[path] = content
for path, content in prepared.items():
    destination = backup / path.relative_to(root)
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        raise RuntimeError('Original configuration backup already exists; preserve it.')
    shutil.copy2(path, destination)
    path.write_text(content)
print('Saved original settings; reduced camera payload, RViz refresh and shadows. Physics and lidar unchanged.')
