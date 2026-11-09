from pathlib import Path
import shutil

repo=Path(__file__).resolve().parents[1]/'outputs/RobotLab'
p=repo/'simulation/tools/prepare_lab.py';t=p.read_text();start=t.index('def prepare():')
t=t[:start]+'''def prepare():
    """Update view settings without changing the saved robot assembly."""
    prepare_driving_views()


if __name__ == '__main__':
    prepare()
''';p.write_text(t)
p=repo/'desktop/Vacuum-Lab.ps1';t=p.read_text(encoding='utf-8-sig')
t=t.replace("'activate_guard.py','apply_robot_profile.py','workspace_paths.py'","'activate_guard.py','workspace_paths.py'")
p.write_text(t,encoding='utf-8-sig')
p=repo/'ros2/src/vacuum_sim/launch/sim.launch.py'
t=p.read_text();t='\n'.join(line for line in t.splitlines() if not line.strip().startswith('gz_launch ='))+'\n';p.write_text(t)
# Obsolete generators/duplicate launches remain available in the historical area.
for name in ('apply_robot_profile.py','navigation.launch.py'):
    p=repo/'simulation/tools'/name
    if p.exists():
        target=repo/'archive/legacy-tools'/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.move(p,target)
p=repo/'desktop/build/Build-Executable.ps1'
if p.exists():shutil.move(p,repo/'archive/legacy-tools/Build-Executable.ps1')
print('Obsolete model rewriting and duplicate build entry points archived.')
