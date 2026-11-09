import os
import signal
import time
from pathlib import Path
# Groups returned by ps during this turn; each belongs to our two test launches.
for group in (393, 902):
    members = []
    for proc in Path('/proc').iterdir():
        if not proc.name.isdecimal():
            continue
        try:
            if os.getpgid(int(proc.name)) == group:
                cmd = (proc/'cmdline').read_bytes().replace(b'\0',b' ')
                if cmd:
                    members.append((int(proc.name),cmd))
        except (ProcessLookupError,FileNotFoundError,PermissionError):
            pass
    assert all(any(token in cmd for token in (b'gz sim ',b'gz_tools_vendor',b'ros2 launch vacuum_sim',
               b'robot_state_publisher',b'parameter_bridge',b'twist_adapter.py',b'/rviz2',b'spawner'))
               for pid,cmd in members), members
    if members:
        os.killpg(group,signal.SIGINT)
        time.sleep(3)
        try:
            os.killpg(group,signal.SIGTERM)
        except ProcessLookupError:
            pass
        print('Stopped verified test process group',group)
