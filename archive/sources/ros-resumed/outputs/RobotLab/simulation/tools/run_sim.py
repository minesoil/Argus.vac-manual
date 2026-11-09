#!/usr/bin/env python3
"""Run one simulator, retaining its lock until all owned child processes stop."""
import fcntl
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

workspace = Path(__file__).resolve().parents[1]
lock = (workspace / ".simulator.lock").open("a")
try:
    fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
except BlockingIOError:
    raise SystemExit(
        "This workspace already has a simulator running. Stop its terminal first."
    )


def identity(pid, group):
    try:
        path = Path(f"/proc/{pid}")
        fields = (path / "stat").read_text().rsplit(")", 1)[1].split()
        if fields[0] == "Z" or path.stat().st_uid != os.getuid():
            return None
        if int(fields[2]) != group or int(fields[3]) != group:
            return None
        return fields[19]
    except (FileNotFoundError, ProcessLookupError, PermissionError):
        return None


def members(group):
    result = {}
    for path in Path("/proc").iterdir():
        if path.name.isdigit():
            stamp = identity(path.name, group)
            if stamp is not None:
                result[int(path.name)] = stamp
    return result


def interrupted(signum, frame):
    raise KeyboardInterrupt


signal.signal(signal.SIGTERM, interrupted)
process = subprocess.Popen(
    [
        "/bin/bash",
        "-lc",
        'source env.sh; exec "$@"',
        "vacuum-launch",
        "ros2",
        "launch",
        "vacuum_sim",
        "sim.launch.py",
        *sys.argv[1:],
    ],
    cwd=workspace,
    start_new_session=True,
)
owned = members(process.pid)
result = 0
try:
    while process.poll() is None:
        owned.update(members(process.pid))
        try:
            process.wait(timeout=0.2)
        except subprocess.TimeoutExpired:
            pass
    result = process.returncode
except KeyboardInterrupt:
    result = 130
finally:
    # Ignore repeat terminal signals while performing bounded cleanup.
    signal.signal(signal.SIGTERM, signal.SIG_IGN)
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    if process.poll() is None:
        owned.update(members(process.pid))

    def active():
        return {
            pid: stamp
            for pid, stamp in owned.items()
            if identity(pid, process.pid) == stamp
        }

    for sig, seconds in ((signal.SIGINT, 5), (signal.SIGTERM, 4), (signal.SIGKILL, 2)):
        if not active():
            break
        try:
            os.killpg(process.pid, sig)
        except ProcessLookupError:
            break
        deadline = time.monotonic() + seconds
        while active() and time.monotonic() < deadline:
            # Collect children while the original session leader is still alive.
            if process.poll() is None:
                owned.update(members(process.pid))
            time.sleep(0.1)
    try:
        process.wait(timeout=1)
    except subprocess.TimeoutExpired:
        pass
    remaining = active()
    if remaining:
        print(
            "Simulator cleanup incomplete; remaining owned PIDs: "
            + str(list(remaining)),
            file=sys.stderr,
        )
        result = 1
    lock.close()
sys.exit(result)
