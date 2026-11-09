#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path
name = sys.argv[1]
assert name in ('sim', 'mapping', 'navigation')
folder = Path('/home/robot/vacuum_ws/validation')
folder.mkdir(exist_ok=True)
with (folder / (name+'.log')).open('w') as log:
    process = subprocess.Popen(['/bin/bash', '-lc', f'cd /home/robot/vacuum_ws; source env.sh; exec ros2 launch vacuum_sim {name}.launch.py'],
                               stdin=subprocess.DEVNULL, stdout=log, stderr=subprocess.STDOUT, start_new_session=True)
(folder / (name+'.pid')).write_text(str(process.pid))
print(name, process.pid)
