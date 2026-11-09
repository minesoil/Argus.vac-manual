import os
from pathlib import Path
import signal

proc = Path('/proc/9065')
if proc.exists():
    args=(proc/'cmdline').read_bytes()
    assert proc.stat().st_uid == os.getuid() and b'/outputs/RobotLab/designer/server.py' in args
    os.kill(9065,signal.SIGTERM)
