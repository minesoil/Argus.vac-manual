"""Short, read-only bench commands. The demo uses the tested controller."""

from pathlib import Path
import argparse
import math
import platform
import socket
import time


def status():
    print(f"Computer     {socket.gethostname()} ({platform.machine()})")
    print(f"Linux        {platform.freedesktop_os_release()['PRETTY_NAME']}")
    print(f"Python       {platform.python_version()}")
    distros = sorted(path.parent.name for path in Path("/opt/ros").glob("*/setup.bash"))
    print("ROS          " + (", ".join(distros) if distros else "no installation found in /opt/ros"))
    ports = sorted(str(p) for pattern in ("ttyUSB*", "ttyACM*") for p in Path("/dev").glob(pattern))
    print("Serial       " + (", ".join(ports) if ports else "no USB serial device node"))
    print("Project      " + str(Path(__file__).resolve().parents[1]))


def demo():
    from .simulate import run_scenario, scenarios

    print("Simulated wall approach. Times below are simulated seconds.", flush=True)
    result = run_scenario(next(scene for scene in scenarios() if scene.name == "wall"))
    for event in result["transitions"]:
        print(f"{event['time_s']:5.1f} s  {event['state']:8} {event['reason']}")
    print(f"Closest body clearance: {result['minimum_physical_clearance_m'] * 100:.1f} cm")
    print(f"Modeled contacts: {result['contact_substeps']}")
    return 0 if result["passed"] else 1


def scan():
    import rclpy
    from rclpy.qos import qos_profile_sensor_data
    from sensor_msgs.msg import LaserScan

    rclpy.init()
    node = rclpy.create_node("argus_scan_listener")
    count = 0

    def show_reading(msg):
        nonlocal count
        valid = [r for r in msg.ranges if math.isfinite(r) and msg.range_min <= r <= msg.range_max]
        nearest = f"{min(valid):.2f} m" if valid else "unknown"
        print(f"Frame {msg.header.frame_id} | valid rays {len(valid)}/{len(msg.ranges)} | closest return {nearest}", flush=True)
        count += 1

    node.create_subscription(LaserScan, "/scan", show_reading, qos_profile_sensor_data)
    deadline = time.monotonic() + 10
    try:
        print("Listening for /scan for up to 10 seconds.", flush=True)
        while rclpy.ok() and count < 3 and time.monotonic() < deadline:
            rclpy.spin_once(node, timeout_sec=0.2)
        if not count:
            print("No scan received. Check that the identified lidar driver is running on this ROS network.")
            return 1
        return 0
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("status", "demo", "scan"))
    raise SystemExit({"status": status, "demo": demo, "scan": scan}[parser.parse_args().command]() or 0)
