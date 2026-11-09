#!/usr/bin/env python3
"""Launch one local simulation and clean up its own processes on exit."""
import fcntl
import os
from pathlib import Path
import signal
import subprocess
import sys

workspace = Path(__file__).resolve().parents[1]
lock = (workspace / '.simulator.lock').open('a')
try:
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
except BlockingIOError:
    raise SystemExit('This workspace already has a simulator running. Stop its terminal first.')

def interrupted(signum, frame):
    raise KeyboardInterrupt

signal.signal(signal.SIGTERM, interrupted)
process = subprocess.Popen(['/bin/bash', '-lc', 'source env.sh; exec "$@"', 'vacuum-launch',
                            'ros2', 'launch', 'vacuum_sim', 'sim.launch.py', *sys.argv[1:]],
                           cwd=workspace, start_new_session=True)
result = 0
try:
    result = process.wait()
except KeyboardInterrupt:
    result = 130
finally:
    try:
        os.killpg(process.pid, signal.SIGINT)
        process.wait(timeout=8)
    except subprocess.TimeoutExpired:
        pass
    except ProcessLookupError:
        pass
    try:
        os.killpg(process.pid, signal.SIGTERM)
        process.wait(timeout=3)
    except (ProcessLookupError, subprocess.TimeoutExpired):
        pass
    lock.close()
sys.exit(result)
