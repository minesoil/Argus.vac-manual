"""Wait for live ROS messages/services, without the ros2 CLI graph cache."""
import argparse
import os
import time
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, DurabilityPolicy, ReliabilityPolicy, qos_profile_sensor_data
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import OccupancyGrid
from lifecycle_msgs.srv import GetState


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('target', choices=['scan', 'map', 'navigation', 'collision_monitor'])
    parser.add_argument('--timeout', type=float, default=60)
    args = parser.parse_args()
    rclpy.init()
    node = Node(f'vacuum_lab_readiness_{os.getpid()}')
    received = []
    clients = {}
    pending = {}
    active = set()
    if args.target == 'scan':
        node.create_subscription(LaserScan, '/scan', received.append, qos_profile_sensor_data)
    elif args.target == 'map':
        node.create_subscription(OccupancyGrid, '/map', received.append,
                                 QoSProfile(depth=1, durability=DurabilityPolicy.TRANSIENT_LOCAL,
                                            reliability=ReliabilityPolicy.RELIABLE))
    else:
        names = ['controller_server', 'planner_server', 'collision_monitor', 'bt_navigator'] if args.target == 'navigation' else ['collision_monitor']
        clients = {name: node.create_client(GetState, f'/{name}/get_state') for name in names}
    deadline = time.monotonic() + args.timeout
    next_call = 0.
    try:
        while time.monotonic() < deadline:
            rclpy.spin_once(node, timeout_sec=.05)
            if received or (clients and len(active) == len(clients)):
                print('READY', flush=True)
                return 0
            if time.monotonic() >= next_call:
                for name, client in clients.items():
                    request = pending.get(name)
                    future = request[0] if request else None
                    if future and not future.done():
                        if time.monotonic() - request[1] < 2.:
                            continue
                        client.remove_pending_request(future)
                        future.cancel()
                        pending.pop(name)
                        active.discard(name)
                        future = None
                    if future:
                        try:
                            if future.result().current_state.id == 3:
                                active.add(name)
                            else:
                                active.discard(name)
                        except Exception:
                            active.discard(name)
                    if client.service_is_ready():
                        pending[name] = (client.call_async(GetState.Request()), time.monotonic())
                next_call = time.monotonic() + .5
        missing = sorted(set(clients)-active)
        print(f'Not ready: {args.target}' + (f'; waiting for {", ".join(missing)}' if missing else ''), flush=True)
        return 1
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    raise SystemExit(main())
