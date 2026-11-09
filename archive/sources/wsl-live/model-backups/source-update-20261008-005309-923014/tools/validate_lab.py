"""Test an already-running launcher lab. Commands only the simulated robot."""

from workspace_paths import workspace
import json
import math
import subprocess
import time
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from nav2_msgs.action import NavigateToPose

WS = workspace()
report = {"date": "2026-10-07", "scope": "simulator only", "tests": {}}
rclpy.init()
node = Node(
    "vacuum_lab_validation",
    parameter_overrides=[rclpy.parameter.Parameter("use_sim_time", value=True)],
)
odom = []
commands = []
node.create_subscription(Odometry, "/odom", odom.append, qos_profile_sensor_data)
node.create_subscription(Twist, "/vacuum/selected_cmd_vel", commands.append, 10)
client = ActionClient(node, NavigateToPose, "/navigate_to_pose")
bridge = None


def wait(predicate, seconds):
    end = time.monotonic() + seconds
    while time.monotonic() < end:
        rclpy.spin_once(node, timeout_sec=0.05)
        if predicate():
            return True
    return bool(predicate())


def run(action):
    result = subprocess.run(
        ["python3", "tools/lab_controller.py", action],
        cwd=WS,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=100,
    )
    print(result.stdout, flush=True)
    if result.returncode:
        raise RuntimeError(result.stdout)


try:
    assert wait(lambda: bool(odom) and bool(commands), 20), "No odometry / command gate"
    assert client.wait_for_server(timeout_sec=10)
    goal = NavigateToPose.Goal()
    goal.pose.header.frame_id = "map"
    goal.pose.header.stamp = node.get_clock().now().to_msg()
    goal.pose.pose.position.x = 0.6
    goal.pose.pose.orientation.w = 1.0
    future = client.send_goal_async(goal)
    assert wait(future.done, 10)
    handle = future.result()
    assert handle.accepted, "Navigation goal rejected"
    outcome = handle.get_result_async()
    if not wait(outcome.done, 100):
        cancellation = handle.cancel_goal_async()
        wait(cancellation.done, 5)
        raise RuntimeError("Navigation timed out; goal cancelled")
    result = outcome.result()
    assert result.status == 4 and result.result.error_code == 0, str(result)
    report["tests"]["circular_robot_goal"] = {
        "status": result.status,
        "error_code": result.result.error_code,
    }
    print("Circular robot navigation goal passed.", flush=True)
    run("save-map")
    report["tests"]["map_save"] = True
    run("manual")
    logfile = (WS / ".lab/bridge-validation.log").open("w")
    bridge = subprocess.Popen(
        ["python3", "tools/controller_bridge.py"],
        cwd=WS,
        stdin=subprocess.PIPE,
        stdout=logfile,
        stderr=subprocess.STDOUT,
        text=True,
    )

    def exercise(held, seconds):
        end = time.monotonic() + seconds
        while time.monotonic() < end:
            assert bridge.poll() is None, "Manual bridge exited"
            bridge.stdin.write(json.dumps({"v": 0.10, "w": 0.0, "held": held}) + "\n")
            bridge.stdin.flush()
            rclpy.spin_once(node, timeout_sec=0.05)
            time.sleep(0.02)

    # Allow DDS services and subscriptions to connect while sending zero input.
    exercise(False, 5)
    assert abs(odom[-1].twist.twist.linear.x) < 0.02, "Robot moved while disarmed"
    start = odom[-1].pose.pose.position
    before = (start.x, start.y)
    exercise(True, 3)
    end = odom[-1].pose.pose.position
    movement = math.hypot(end.x - before[0], end.y - before[1])
    assert movement > 0.08, f"Manual drive did not move: {movement}"
    exercise(False, 2)
    assert (
        abs(commands[-1].linear.x) < 0.001 and abs(odom[-1].twist.twist.linear.x) < 0.02
    )
    report["tests"]["manual_hold_and_release"] = {
        "movement_m": movement,
        "released_speed_m_s": odom[-1].twist.twist.linear.x,
    }
    exercise(True, 1)
    # Keep the bridge alive, but stop supplying packets. Steady-time watchdog must stop.
    assert wait(
        lambda: abs(commands[-1].linear.x) < 0.001
        and abs(odom[-1].twist.twist.linear.x) < 0.02,
        4,
    )
    report["tests"]["input_timeout_stop"] = True
    bridge.stdin.close()
    bridge.wait(timeout=5)
    assert bridge.returncode == 0
    report["tests"]["bridge_eof_cleanup"] = True
    report["passed"] = True
except Exception as exc:
    report["passed"] = False
    report["error"] = str(exc)
    raise
finally:
    if bridge and bridge.poll() is None:
        try:
            bridge.stdin.close()
            bridge.wait(timeout=5)
        except Exception:
            bridge.terminate()
    target = WS / "validation/lab-20261007"
    target.mkdir(parents=True, exist_ok=True)
    (target / "results.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2), flush=True)
    node.destroy_node()
    rclpy.shutdown()
