"""Manual simulator control via stdin; steady-time watchdog and Nav2 interlock."""
import json
import math
from pathlib import Path
import sys
import threading
import time
import rclpy
from geometry_msgs.msg import Twist
from lifecycle_msgs.srv import GetState
from nav2_msgs.msg import CollisionMonitorState
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from rclpy.qos import qos_profile_sensor_data
from rclpy.node import Node

MODE = Path('/home/robot/vacuum_ws/.lab/manual-mode')


def decode(line):
    data = json.loads(line)
    v, w = float(data['v']), float(data['w'])
    if not math.isfinite(v) or not math.isfinite(w):
        raise ValueError('Non-finite control input')
    if data.get('held') is not True:
        return 0., 0.
    return max(-.30, min(.50, v)), max(-1.2, min(1.2, w))


class Bridge(Node):
    def __init__(self):
        super().__init__('vacuum_manual_controller')
        self.pub = self.create_publisher(Twist, '/vacuum/manual_cmd_vel', 1)
        self.lock = threading.Lock()
        self.latest = (0., 0.)
        self.received = 0.
        self.closed = False
        self.states = {'collision_monitor': (0, 0.)}
        self.state_clients = {name: self.create_client(GetState, f'/{name}/get_state') for name in self.states}
        self.pending = {}
        self.last_status = None
        self.report_at = 0.
        self.guard_action = (0, '')
        self.output = (0., 0., 0.)
        self.scan_at = 0.
        self.odom = (0., 0., 0.)
        self.motion_since = 0.
        self.create_subscription(CollisionMonitorState, '/collision_monitor_state', self.guard_state, 10)
        self.create_subscription(Twist, '/cmd_vel', self.guard_output, 1)
        self.create_subscription(LaserScan, '/scan', self.scan_received, qos_profile_sensor_data)
        self.create_subscription(Odometry, '/odom', self.odom_received, qos_profile_sensor_data)
        self.create_timer(.05, self.tick)
        self.create_timer(.25, self.check_states)
        threading.Thread(target=self.read_input, daemon=True).start()

    def read_input(self):
        try:
            for line in sys.stdin:
                try:
                    command = decode(line)
                except (ValueError, KeyError, TypeError):
                    command = (0., 0.)
                with self.lock:
                    self.latest = command
                    self.received = time.monotonic()
        finally:
            with self.lock:
                self.latest = (0., 0.)
                self.closed = True

    def check_states(self):
        now = time.monotonic()
        for name, client in self.state_clients.items():
            previous = self.pending.get(name)
            if previous and not previous[0].done():
                if now - previous[1] < .75:
                    continue
                # A lost service response must not leave a permanently pending
                # future that prevents all subsequent health checks.
                self.pending.pop(name)
                client.remove_pending_request(previous[0])
                previous[0].cancel()
            if not client.service_is_ready():
                continue
            future = client.call_async(GetState.Request())
            self.pending[name] = (future, now)
            future.add_done_callback(lambda result, name=name: self.record(name, result))

    def record(self, name, future):
        if self.pending.get(name, (None,))[0] is not future:
            return
        try:
            self.states[name] = (future.result().current_state.id, time.monotonic())
        except Exception:
            self.states[name] = (0, 0.)

    def guard_state(self, message):
        self.guard_action = (message.action_type, message.polygon_name)

    def guard_output(self, message):
        self.output = (message.linear.x, message.angular.z, time.monotonic())

    def scan_received(self, message):
        self.scan_at = time.monotonic()

    def odom_received(self, message):
        self.odom = (message.twist.twist.linear.x, message.twist.twist.angular.z, time.monotonic())

    def report(self, now, safe, v, w):
        if now < self.report_at:
            return
        self.report_at = now + .25
        out_v, out_w, stamp = self.output
        actual_v, actual_w, odom_stamp = self.odom
        action, polygon = self.guard_action
        reason = 'Ready'
        if not MODE.exists():
            reason = 'Manual mode is not selected'
        elif now - self.scan_at > .5:
            reason = 'Lidar data missing or stale; guard stops motion'
        elif not safe:
            reason = 'Waiting for collision guard health; commands stopped'
        elif abs(v) + abs(w) > .001:
            if now - stamp > .5:
                reason = 'No fresh guard output; commands stopped'
            elif abs(out_v) + abs(out_w) < .001:
                if action and polygon:
                    escape = 'try reverse' if v > .001 else ('try forward' if v < -.001 else 'move away before turning')
                    reason = 'Obstacle blocks this direction; ' + escape
                else:
                    reason = 'Guard stopped motion; check lidar/TF in Ubuntu logs'
            elif abs(out_v) < abs(v) - .01 or abs(out_w) < abs(w) - .01:
                reason = 'Slowing near an obstacle'
            else:
                reason = 'Driving'
                if now - odom_stamp > 1.:
                    reason = 'Odometry missing; check simulator/controller'
                elif self.motion_since and now - self.motion_since > 1.5 and abs(actual_v) < .015 and abs(actual_w) < .04:
                    reason = 'No actual movement; STOP and check simulator/controller'
        print(json.dumps({'ready': safe, 'reason': reason, 'polygon': polygon,
                          'requested_v': v, 'output_v': out_v, 'output_w': out_w,
                          'actual_v': actual_v, 'actual_w': actual_w}), flush=True)

    def tick(self):
        now = time.monotonic()
        safe = MODE.exists() and now - self.scan_at < .5 and all(state == 3 and now - stamp < 1.
                                     for state, stamp in self.states.values())
        with self.lock:
            v, w = self.latest if safe and now - self.received < .3 else (0., 0.)
            closed = self.closed
        message = Twist()
        message.linear.x, message.angular.z = v, w
        if abs(v) + abs(w) > .03:
            if not self.motion_since:
                self.motion_since = now
        else:
            self.motion_since = 0.
        self.pub.publish(message)
        self.report(now, safe, v, w)
        if closed:
            raise KeyboardInterrupt


def main():
    # The launcher lock, separate from the simulator lock, serializes manual sources.
    import fcntl
    path = Path('/home/robot/vacuum_ws/.lab/manual-input.lock')
    with path.open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        rclpy.init()
        node = Bridge()
        try:
            rclpy.spin(node)
        except KeyboardInterrupt:
            pass
        finally:
            node.pub.publish(Twist())
            node.destroy_node()
            if rclpy.ok():
                rclpy.shutdown()


if __name__ == '__main__':
    main()
