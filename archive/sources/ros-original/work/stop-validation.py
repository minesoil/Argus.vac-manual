#!/usr/bin/env python3
import os
import signal
import time
from pathlib import Path
folder = Path('/home/robot/vacuum_ws/validation')
for name in ('navigation', 'mapping', 'sim'):
    file = folder / (name+'.pid')
    if not file.exists():
        continue
    pid = int(file.read_text())
    proc = Path(f'/proc/{pid}/cmdline')
    if not proc.exists():
        continue
    command = proc.read_bytes().replace(b'\0', b' ')
    if b'ros2 launch vacuum_sim ' + (name+'.launch.py').encode() not in command:
        raise RuntimeError(f'Refuse to signal PID {pid}: command no longer matches validation process')
    os.kill(pid, signal.SIGINT)
    end = time.monotonic()+15
    while proc.exists() and time.monotonic()<end:
        time.sleep(0.2)
    print(f'Stopped {name} launcher {pid}')
