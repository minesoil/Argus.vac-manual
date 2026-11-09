#!/usr/bin/env python3
"""User-owned, simulator-only launcher. No sudo, hardware, or global process killing."""
from workspace_paths import workspace
import argparse
import datetime
import fcntl
import json
import os
from pathlib import Path
import signal
import subprocess
import time
import yaml

WS = workspace()
RUN = WS / ".lab"
STATE = RUN / "processes.json"
SESSION = RUN / "session.json"
CAMERA_RATE = 60


def say(message):
    print(message, flush=True)


def identity(pid):
    try:
        path = Path(f"/proc/{pid}")
        # comm may contain spaces, so split after its closing parenthesis.
        fields = (path / "stat").read_text().rsplit(")", 1)[1].split()
        if fields[0] == "Z" or path.stat().st_uid != os.getuid():
            return None
        return fields[19]  # /proc stat field 22: start time
    except (FileNotFoundError, ProcessLookupError, PermissionError):
        return None


def read_state():
    return json.loads(STATE.read_text()) if STATE.exists() else {}


def save(state):
    tmp = STATE.with_suffix(".tmp")
    tmp.write_text(json.dumps(state))
    tmp.replace(STATE)


def alive(record):
    return identity(record["pid"]) == record["start"]


def member_alive(pid, stamp, group):
    try:
        return (
            identity(int(pid)) == stamp
            and os.getpgid(int(pid)) == group
            and os.getsid(int(pid)) == group
        )
    except ProcessLookupError:
        return False


def group_members(record):
    result = {}
    if not alive(record):
        return {
            pid: stamp
            for pid, stamp in record.get("members", {}).items()
            if member_alive(pid, stamp, record["pid"])
        }
    for path in Path("/proc").iterdir():
        if not path.name.isdigit():
            continue
        try:
            fields = (path / "stat").read_text().rsplit(")", 1)[1].split()
            if int(fields[2]) == record["pid"] and int(fields[3]) == record["pid"]:
                stamp = identity(int(path.name))
                if stamp is not None:
                    result[path.name] = stamp
        except (FileNotFoundError, ProcessLookupError, PermissionError):
            pass
    return result


def stop(state):
    # Reverse startup order. Never signal a recycled PID or another user's process.
    for name, record in reversed(list(state.items())):
        members = group_members(record)
        if not members:
            continue
        record["members"] = members
        save(state)

        def still_running():
            return any(
                member_alive(pid, stamp, record["pid"])
                for pid, stamp in members.items()
            )

        say(f"Stopping {name}…")
        for sig, delay in ((signal.SIGTERM, 14), (signal.SIGKILL, 2)):
            if not still_running():
                break
            try:
                os.killpg(record["pid"], sig)
            except ProcessLookupError:
                break
            end = time.monotonic() + delay
            while still_running() and time.monotonic() < end:
                time.sleep(0.2)
    remaining = {name: rec for name, rec in state.items() if group_members(rec)}
    save(remaining)
    (RUN / "manual-mode").unlink(missing_ok=True)
    SESSION.unlink(missing_ok=True)
    if remaining:
        raise RuntimeError("Some lab processes did not stop. See .lab logs.")


def command(argv, timeout=20):
    return subprocess.run(
        ["/bin/bash", "-lc", 'source env.sh; exec "$@"', "vacuum-lab", *argv],
        cwd=WS,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=timeout,
    )


def launch(state, name, argv):
    with (RUN / f"{name}.log").open("w") as log:
        proc = subprocess.Popen(
            ["/bin/bash", "-lc", 'source env.sh; exec "$@"', "vacuum-lab", *argv],
            cwd=WS,
            stdin=subprocess.DEVNULL,
            stdout=log,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
    state[name] = {"pid": proc.pid, "start": identity(proc.pid)}
    if state[name]["start"] is None:
        raise RuntimeError(f"{name} exited during startup. See .lab/{name}.log.")
    save(state)


def ready(state, target, seconds=60):
    result = command(
        ["python3", "tools/wait_ready.py", target, "--timeout", str(seconds)],
        seconds + 10,
    )
    if any(not alive(rec) for rec in state.values()):
        raise RuntimeError("A lab component exited. See .lab logs.")
    if result.returncode or "READY" not in result.stdout:
        raise RuntimeError(
            f"{target} startup timed out. See .lab logs. " + result.stdout
        )


def start(state, gazebo):
    settings = json.loads(SESSION.read_text()) if SESSION.exists() else {}
    if (
        set(state) == {"simulation", "command gate", "mapping", "navigation"}
        and all(alive(rec) for rec in state.values())
        and settings.get("camera_rate") == CAMERA_RATE
        and not (RUN / "manual-mode").exists()
    ):
        say(
            "Lab is already running. Stop and restart to leave manual mode or change the views."
        )
        return
    if state:
        stop(state)
        state.clear()
    required = [
        WS / "env.sh",
        WS / "tools/run_sim.py",
        WS / "src/vacuum_sim/config/vacuum_nav2.yaml",
        WS / "src/vacuum_sim/config/vacuum_navigate.xml",
    ]
    if any(not path.is_file() for path in required):
        raise RuntimeError(
            "The simulator or conservative navigation profile is missing."
        )
    # Refuse to combine this session with an existing manually started ROS workload.
    nodes = command(["ros2", "node", "list", "--no-daemon", "--spin-time", "2"]).stdout
    if any(
        name in nodes
        for name in ("/slam_toolbox", "/controller_server", "/robot_state_publisher")
    ):
        raise RuntimeError("A manual lab session is running. Stop its terminals first.")
    from prepare_lab import prepare

    checked = command(["python3", "tools/check_lab.py"], 30)
    if checked.returncode:
        raise RuntimeError("Controller safety logic checks failed: " + checked.stdout)
    prepare()
    try:
        say("Starting simulator and RViz…")
        launch(
            state,
            "simulation",
            [
                "python3",
                "tools/run_sim.py",
                f"gui:={str(gazebo).lower()}",
                "rviz:=true",
                f"camera_rate:={CAMERA_RATE}",
                "rviz_config:=" + str(WS / "src/vacuum_sim/config/view.rviz"),
            ],
        )
        ready(state, "scan")
        launch(state, "command gate", ["python3", "tools/command_gate.py"])
        say("Starting mapping…")
        launch(state, "mapping", ["ros2", "launch", "vacuum_sim", "mapping.launch.py"])
        ready(state, "map")
        say("Starting obstacle-aware navigation…")
        launch(
            state,
            "navigation",
            [
                "ros2",
                "launch",
                "vacuum_sim",
                "navigation.launch.py",
                "params_file:=" + str(required[2]),
            ],
        )
        ready(state, "navigation")
        SESSION.write_text(
            json.dumps({"mode": "navigation", "camera_rate": CAMERA_RATE})
        )
        say(
            "Ready. In RViz set Fixed Frame to map, then use Nav2 Goal to choose a destination."
        )
        say(
            "This is mapping and destination navigation. Automatic room cleaning is not implemented."
        )
    except BaseException:
        say("Startup failed; stopping this launcher’s processes…")
        stop(state)
        raise


def drive(state, gazebo):
    settings = json.loads(SESSION.read_text()) if SESSION.exists() else {}
    if (
        set(state) == {"simulation", "command gate", "collision guard", "camera view"}
        and all(alive(rec) for rec in state.values())
        and settings.get("camera_rate") == CAMERA_RATE
    ):
        ready(state, "collision_monitor", 15)
        say(
            "Ready to drive. Open the controller panel; push forward, pull back to reverse."
        )
        return
    if state:
        stop(state)
        state.clear()
    nodes = command(["ros2", "node", "list", "--no-daemon", "--spin-time", "2"]).stdout
    if any(
        name in nodes
        for name in (
            "/slam_toolbox",
            "/controller_server",
            "/robot_state_publisher",
            "/collision_monitor",
        )
    ):
        raise RuntimeError("A manual lab session is running. Stop its terminals first.")
    from prepare_lab import prepare, circle

    prepare()
    checked = command(["python3", "tools/check_lab.py"], 30)
    if checked.returncode:
        raise RuntimeError("Controller safety checks failed: " + checked.stdout)
    config = yaml.safe_load((WS / "src/vacuum_sim/config/vacuum_nav2.yaml").read_text())
    guard = config["collision_monitor"]["ros__parameters"]
    # Static approach footprint preserves predictive braking without a costmap.
    if not (RUN / "custom-design.json").exists():
        guard["FootprintApproach"]["points"] = str(circle(0.17))
    guard["cmd_vel_in_topic"] = "/vacuum/selected_cmd_vel"
    guard_path = RUN / "drive-guard.yaml"
    guard_path.write_text(
        yaml.safe_dump(
            {"collision_monitor": {"ros__parameters": guard}}, sort_keys=False
        )
    )
    (RUN / "manual-mode").write_text("Direct manual driving selected.\n")
    try:
        say("Starting 60 FPS camera and driving view…")
        launch(
            state,
            "simulation",
            [
                "python3",
                "tools/run_sim.py",
                f"gui:={str(gazebo).lower()}",
                "rviz:=false",
                f"camera_rate:={CAMERA_RATE}",
                "rviz_config:=" + str(WS / "src/vacuum_sim/config/drive.rviz"),
            ],
        )
        ready(state, "scan")
        launch(state, "command gate", ["python3", "tools/command_gate.py"])
        launch(
            state,
            "collision guard",
            [
                "/opt/ros/jazzy/lib/nav2_collision_monitor/collision_monitor",
                "--ros-args",
                "--params-file",
                str(guard_path),
            ],
        )
        activated = command(["python3", "tools/activate_guard.py"], 65)
        if activated.returncode:
            raise RuntimeError(activated.stdout)
        launch(
            state,
            "camera view",
            [
                "python3",
                "/opt/ros/jazzy/lib/rqt_image_view/rqt_image_view",
                "/camera/image_raw",
            ],
        )
        ready(state, "collision_monitor", 15)
        SESSION.write_text(json.dumps({"mode": "drive", "camera_rate": CAMERA_RATE}))
        say(
            "Ready to drive. Push forward, pull back to reverse. Camera target: 60 FPS."
        )
    except BaseException:
        say("Driving startup failed; stopping this launcher’s processes…")
        stop(state)
        raise


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action", choices=["start", "drive", "stop", "status", "save-map", "manual"]
    )
    parser.add_argument("--gazebo", action="store_true")
    args = parser.parse_args()
    if not WS.is_dir():
        raise RuntimeError("Ubuntu vacuum workspace was not found.")
    RUN.mkdir(exist_ok=True)
    with (RUN / "controller.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        state = read_state()
        if args.action == "start":
            start(state, args.gazebo)
        elif args.action == "drive":
            drive(state, args.gazebo)
        elif args.action == "stop":
            stop(state)
            say("Lab stopped.")
        elif args.action == "status":
            say(
                "\n".join(
                    f'{name}: {"running" if alive(rec) else "stopped"}'
                    for name, rec in state.items()
                )
                or "Lab is stopped."
            )
        elif args.action == "manual":
            if set(state) == {
                "simulation",
                "command gate",
                "collision guard",
                "camera view",
            } and all(alive(rec) for rec in state.values()):
                ready(state, "collision_monitor", 15)
                say("Manual mode ready. Direct driving guard is active.")
                return
            if set(state) != {
                "simulation",
                "command gate",
                "mapping",
                "navigation",
            } or any(not alive(rec) for rec in state.values()):
                raise RuntimeError("Start the lab before enabling manual drive.")
            # Switch the gate first: autonomous output cannot reach the robot,
            # even while cancellation is pending. Keep Nav2's managed nodes alive
            # so its bond manager does not tear down Collision Monitor.
            (RUN / "manual-mode").write_text(
                "Manual command source selected; restart to resume goals.\n"
            )
            result = command(
                [
                    "ros2",
                    "service",
                    "call",
                    "/navigate_to_pose/_action/cancel_goal",
                    "action_msgs/srv/CancelGoal",
                    "{}",
                ],
                30,
            )
            if result.returncode:
                raise RuntimeError(
                    "Could not cancel navigation; the gate remains stopped in manual mode. "
                    + result.stdout
                )
            ready(state, "collision_monitor", 20)
            say("Manual mode ready. Navigation is paused until Stop lab → Start lab.")
        else:
            if not state.get("mapping") or not alive(state["mapping"]):
                raise RuntimeError("Start the lab before saving a map.")
            maps = WS / "maps"
            maps.mkdir(exist_ok=True)
            prefix = maps / datetime.datetime.now().strftime("room-%Y%m%d-%H%M%S-%f")
            result = command(
                [
                    "ros2",
                    "run",
                    "nav2_map_server",
                    "map_saver_cli",
                    "-f",
                    str(prefix),
                    "--ros-args",
                    "-p",
                    "use_sim_time:=true",
                    "-p",
                    "save_map_timeout:=10.0",
                    "-p",
                    "map_subscribe_transient_local:=true",
                ],
                40,
            )
            if result.returncode or not prefix.with_suffix(".yaml").is_file():
                raise RuntimeError("Map save failed: " + result.stdout)
            say(
                f"Map saved: {prefix}.yaml\nSaved-map localization is a separate future workflow."
            )


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        say(f"Error: {exc}")
        raise SystemExit(1)
