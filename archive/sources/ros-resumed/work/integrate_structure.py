"""One-time migration into the separated source tree; original files stay archived."""
from pathlib import Path
import re

repo = Path(__file__).resolve().parents[1] / 'outputs/RobotLab'
tools = repo / 'simulation/tools'
for path in tools.glob('*.py'):
    if path.name == 'workspace_paths.py': continue
    text = path.read_text(encoding='utf-8-sig')
    used = False
    replacements = {
        "Path('/home/robot/vacuum_ws')": 'workspace()',
        "Path('/home/robot/vacuum_ws/src/vacuum_sim')": "workspace() / 'src/vacuum_sim'",
        "Path('/home/robot/vacuum_ws/.lab/manual-mode')": "workspace() / '.lab/manual-mode'",
        "Path('/home/robot/vacuum_ws/.lab')": "workspace() / '.lab'",
        "Path('/home/robot/vacuum_ws/.lab/manual-input.lock')": "workspace() / '.lab/manual-input.lock'",
    }
    for old, new in replacements.items():
        if old in text: text = text.replace(old, new); used = True
    if used:
        lines = text.splitlines()
        index = next((i for i, line in enumerate(lines) if line.startswith('import ') or line.startswith('from ')), 0)
        lines.insert(index, 'from workspace_paths import workspace, load_profile, profile_path')
        text = '\n'.join(lines) + '\n'
    if "PROFILE = json.loads((Path(__file__).parent / 'robot-profile.json').read_text())['drive']" in text:
        text = text.replace("PROFILE = json.loads((Path(__file__).parent / 'robot-profile.json').read_text())['drive']", "PROFILE = load_profile()['drive']")
    if path.name == 'apply_robot_profile.py': text = text.replace("source = WS / 'tools/robot-profile.json'", 'source = profile_path()')
    if path.name == 'prepare_lab.py':
        start = text.index('def prepare():')
        text = text[:start] + '''def prepare():
    """Prepare camera settings; preserve a design selected by the assembly editor."""
    prepare_driving_views()
    if not (WS / '.lab/custom-design.json').exists():
        from apply_robot_profile import apply_profile
        apply_profile()


if __name__ == '__main__':
    prepare()
'''
    if path.name == 'lab_controller.py':
        text = text.replace("guard['FootprintApproach']['points'] = str(circle(.17))", "if not (RUN / 'custom-design.json').exists():\n        guard['FootprintApproach']['points'] = str(circle(.17))")
    path.write_text(text, encoding='utf-8')

launch = repo / 'ros2/src/vacuum_sim/launch/sim.launch.py'
text = launch.read_text().replace("str(package / 'urdf/vacuum.urdf.xacro')", "LaunchConfiguration('description_file')")
text = text.replace("DeclareLaunchArgument('camera_width'", "DeclareLaunchArgument('description_file', default_value=str(package / ('urdf/designed.urdf' if (package / 'urdf/designed.urdf').exists() else 'urdf/vacuum.urdf.xacro'))),\n        DeclareLaunchArgument('camera_width'")
launch.write_text(text)
cmake = repo / 'ros2/src/vacuum_sim/CMakeLists.txt'
text = cmake.read_text().replace('install(DIRECTORY urdf config launch worlds', 'install(DIRECTORY urdf config launch worlds meshes')
cmake.write_text(text)
(repo / 'ros2/src/vacuum_sim/meshes').mkdir(exist_ok=True)

desktop = repo / 'desktop'
theme = desktop / 'Modern-Theme.ps1'
text = theme.read_text(encoding='utf-8-sig').replace("Join-Path $PSScriptRoot 'Vacuum-Lab.ico'", "Join-Path (Split-Path $PSScriptRoot) 'assets\\Vacuum-Lab.ico'")
theme.write_text(text, encoding='utf-8-sig')
panel = desktop / 'Controller-Panel.ps1'
text = panel.read_text(encoding='utf-8-sig').replace("Join-Path $profileRoot 'robot-profile.json'", "Join-Path $profileRoot 'config\\simulation.json'")
panel.write_text(text, encoding='utf-8-sig')
files = desktop / 'Files-Panel.ps1'
text = files.read_text(encoding='utf-8-sig').replace("Join-Path $appRoot 'file_catalog.py'", "Join-Path $appRoot 'simulation\\tools\\file_catalog.py'")
insert = '''        [pscustomobject]@{ Name='Robot designs and 3D editor'; Path=(ConvertTo-LabLinuxPath (Join-Path $appRoot 'designer')); Windows=$true }
        [pscustomobject]@{ Name='Arduino motor firmware'; Path=(ConvertTo-LabLinuxPath (Join-Path $appRoot 'firmware')); Windows=$true }
        [pscustomobject]@{ Name='Orange Pi ROS packages'; Path=(ConvertTo-LabLinuxPath (Join-Path $appRoot 'ros2\\src\\vacuum_hardware')); Windows=$true }
        [pscustomobject]@{ Name='Setup and deployment guides'; Path=(ConvertTo-LabLinuxPath (Join-Path $appRoot 'docs')); Windows=$true }
        [pscustomobject]@{ Name='Saved editable designs'; Path=(ConvertTo-LabLinuxPath (Join-Path $env:LOCALAPPDATA 'VacuumLab\\designs')); Windows=$true }
'''
text = text.replace("    @(\n", "    @(\n" + insert, 1)
files.write_text(text, encoding='utf-8-sig')

launcher = desktop / 'Vacuum-Lab.ps1'
text = launcher.read_text(encoding='utf-8-sig').replace('[switch]$Files,', '[switch]$Files, [switch]$Designer,')
text = text.replace('$script:root = $PSScriptRoot', '$script:root = Split-Path $PSScriptRoot')
for file in ('Modern-Theme.ps1', 'Controller-Panel.ps1', 'Files-Panel.ps1'):
    text = text.replace("Join-Path $script:root '" + file + "'", "Join-Path $PSScriptRoot '" + file + "'")
text = text.replace("'Furnished-room-preview.png'", "'assets\\Furnished-room-preview.png'")
text = text.replace("'Vacuum-Lab-Quickstart.md'", "'README.md'").replace("'Hardware-Profile.md'", "'docs\\hardware.md'")
text = text.replace("foreach ($name in @('lab_controller.py','run_sim.py','prepare_lab.py','controller_bridge.py','command_gate.py','check_lab.py','wait_ready.py','activate_guard.py','apply_robot_profile.py','robot-profile.json'))", "foreach ($name in @('lab_controller.py','run_sim.py','prepare_lab.py','controller_bridge.py','command_gate.py','check_lab.py','wait_ready.py','activate_guard.py','apply_robot_profile.py','workspace_paths.py','robot-profile.json'))")
text = text.replace("$files[$name] = [Convert]::ToBase64String([IO.File]::ReadAllBytes((Join-Path $script:root $name)))", "$sourcePath=if ($name -eq 'robot-profile.json') { Join-Path $script:root 'config\\simulation.json' } else { Join-Path $script:root ('simulation\\tools\\'+$name) }; $files[$name] = [Convert]::ToBase64String([IO.File]::ReadAllBytes($sourcePath))")
# Avoid replacing the profile after the designer has changed wheel geometry.
text = text.replace("for name, data in decoded.items():\n    p = tools / name", "for name, data in decoded.items():\n    if name == 'robot-profile.json' and (tools.parent / '.lab/custom-design.json').exists():\n        continue\n    p = tools / name")
text = text.replace("'Build. Drive. Explore.'", "'Design. Test. Drive.'").replace("'Your hardware. A bigger room. Direct control.'", "'Edit your robot and test it in the simulator.'")
text = text.replace("Add-LabButton 'Robot profile' 24 478 { Start-Process (Join-Path $script:root 'docs\\hardware.md') }", "Add-LabButton 'Design robot' 24 478 { & (Join-Path $PSScriptRoot 'Start-Designer.ps1') -RepoRoot $script:root }")
text = text.replace("if ($Files) { Show-LabFiles $wsl $script:root $code }", "if ($Files) { Show-LabFiles $wsl $script:root $code }; if ($Designer) { & (Join-Path $PSScriptRoot 'Start-Designer.ps1') -RepoRoot $script:root }")
launcher.write_text(text, encoding='utf-8-sig')
# Redirect the executable to the organized source root; full ZIP still supports standalone use.
cs = desktop / 'build/Launcher.cs'
text = cs.read_text().replace('AssemblyVersion("2.0.0.0")', 'AssemblyVersion("3.0.0.0")')
text = text.replace('string script = Path.Combine(app, "Vacuum-Lab.ps1");', '''string sibling = Path.Combine(Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location), "RobotLab");
            if (File.Exists(Path.Combine(sibling, "desktop", "Vacuum-Lab.ps1"))) app = sibling;
            string script = Path.Combine(app, "desktop", "Vacuum-Lab.ps1");''')
text = text.replace('Array.IndexOf(args, "--files") >= 0 ? " -Files" : ""', 'Array.IndexOf(args, "--files") >= 0 ? " -Files" : Array.IndexOf(args, "--designer") >= 0 ? " -Designer" : ""')
cs.write_text(text)
print('Structured paths and editable-model startup integrated.')
