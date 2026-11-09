from pathlib import Path
import shutil

repo=Path(__file__).resolve().parents[1]/'outputs/RobotLab'
(repo/'simulation/tools/prepare_lab.py').write_text('''"""Check simulator assets before startup without rewriting saved source."""
import math
from workspace_paths import workspace


def circle(radius, count=32):
    """Circumscribed legacy body footprint in base_link coordinates."""
    outer = radius / math.cos(math.pi / count)
    return [[round(-.03 + outer * math.cos(2 * math.pi * i/count), 6),
             round(outer * math.sin(2 * math.pi * i/count), 6)] for i in range(count)]


def prepare():
    package = workspace() / 'src/vacuum_sim'
    for relative in ('launch/sim.launch.py', 'worlds/room.sdf', 'config/controllers.yaml', 'config/drive.rviz'):
        if not (package / relative).is_file():
            raise RuntimeError(f'Missing simulator asset: {relative}. Run tools/install-simulation.py.')


if __name__ == '__main__':
    prepare()
''')
for filename,old in [('validate_drive.py','validation/modern-drive-20261007'),('validate_lab.py','validation/lab-20261007'),('validate_directional_guard.py','validation/furnished-20261007')]:
    p=repo/'simulation/tools'/filename;t=p.read_text();t='from datetime import datetime\n'+t if not t.startswith('#!') else t.replace('\n','\nfrom datetime import datetime\n',1)
    t=t.replace('"date": "2026-10-07"','"date": datetime.now().strftime("%Y-%m-%d")')
    t=t.replace('"'+old+'"','"validation/review-" + datetime.now().strftime("%Y%m%d")')
    # Parentheses keep Path division applied to the complete relative path.
    t=t.replace('WS / "validation/review-" + datetime.now().strftime("%Y%m%d")','WS / ("validation/review-" + datetime.now().strftime("%Y%m%d"))')
    p.write_text(t)
# Controller profiles/logs persist independently of installed/extracted source.
p=repo/'desktop/Controller-Panel.ps1';t=p.read_text(encoding='utf-8-sig')
t=t.replace("    $driveProfile=", "    $userProfileRoot=Join-Path $env:LOCALAPPDATA 'VacuumLab\\controller-profiles'\n    [void][IO.Directory]::CreateDirectory($userProfileRoot)\n    $driveProfile=",1)
t=t.replace('$dialog.InitialDirectory=$profileRoot','$dialog.InitialDirectory=$userProfileRoot').replace("Join-Path $profileRoot 'controller-bridge-last.log'","Join-Path $userProfileRoot 'controller-bridge-last.log'")
p.write_text(t,encoding='utf-8-sig')
history=repo/'reports/history';history.mkdir(exist_ok=True)
for p in (repo/'reports').glob('*.json'):shutil.move(p,history/p.name)
for p in [repo/'designs/reference.urdf', repo/'ros2/src/vacuum_sim/config/robot-profile.json', repo/'ros2/src/vacuum_sim/launch/navigation.launch.py.before-autonomy-20261006']:
    if p.exists():
        target=repo/'archive/legacy-tools'/p.name;shutil.move(p,target)
print('Runtime source checks, dated validation and persistent controller profiles ready.')
