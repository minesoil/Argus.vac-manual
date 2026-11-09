"""Clean the single Gazebo process left by our just-stopped old launcher."""
import os
from pathlib import Path
import signal
import time
pid=4160
path=Path(f'/proc/{pid}')
if not path.exists():raise SystemExit('Known orphan has already exited.')
args=(path/'cmdline').read_bytes().replace(b'\0',b' ').decode()
expected='/home/robot/vacuum_ws/install/vacuum_sim/share/vacuum_sim/worlds/room.sdf'
if expected not in args or path.stat().st_uid!=os.getuid() or os.getpgid(pid)!=4121:
    raise SystemExit('Known orphan identity no longer matches; no process was signalled.')
stamp=(path/'stat').read_text().rsplit(')',1)[1].split()[19]
def alive():
    try:
        fields=(path/'stat').read_text().rsplit(')',1)[1].split()
        return fields[0]!='Z' and fields[19]==stamp
    except FileNotFoundError:return False
os.kill(pid,signal.SIGTERM)
deadline=time.monotonic()+5
while alive() and time.monotonic()<deadline:time.sleep(.1)
if alive():os.kill(pid,signal.SIGKILL)
print('Cleaned the verified leftover Gazebo process.')
