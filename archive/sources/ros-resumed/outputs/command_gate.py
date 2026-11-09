"""Select exactly one launcher command source before Collision Monitor."""
import math
from pathlib import Path
import json
import time
import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node

MODE = Path('/home/robot/vacuum_ws/.lab/manual-mode')
PROFILE = json.loads((Path(__file__).parent / 'robot-profile.json').read_text())['drive']


class Gate(Node):
    def __init__(self):
        super().__init__('vacuum_command_gate')
        self.pub = self.create_publisher(Twist, '/vacuum/selected_cmd_vel', 1)
        self.inputs = {'manual': (0., 0., 0.), 'auto': (0., 0., 0.)}
        self.mode = 'manual' if MODE.exists() else 'auto'
        self.last_status = None
        self.create_subscription(Twist, '/cmd_vel_smoothed', lambda msg: self.receive('auto', msg), 1)
        self.create_subscription(Twist, '/vacuum/manual_cmd_vel', lambda msg: self.receive('manual', msg), 1)
        self.create_timer(PROFILE['input_period_s'], self.tick)

    def receive(self, source, msg):
        v, w = msg.linear.x, msg.angular.z
        if not math.isfinite(v) or not math.isfinite(w):
            v, w = 0., 0.
        self.inputs[source] = (max(-PROFILE['reverse_m_s'], min(PROFILE['forward_m_s'], v)), max(-PROFILE['turn_rad_s'], min(PROFILE['turn_rad_s'], w)), time.monotonic())

    def tick(self):
        mode = 'manual' if MODE.exists() else 'auto'
        if mode != self.mode:
            self.mode = mode
            # Require fresh input after every mode transition.
            self.inputs = {'manual': (0., 0., 0.), 'auto': (0., 0., 0.)}
        v, w, stamp = self.inputs[mode]
        message = Twist()
        if time.monotonic() - stamp < .3:
            message.linear.x, message.angular.z = v, w
        status = (mode, abs(message.linear.x) > .001 or abs(message.angular.z) > .001)
        if status != self.last_status:
            self.get_logger().info(f'Selected {mode}: speed={message.linear.x:.3f}, turn={message.angular.z:.3f}')
            self.last_status = status
        self.pub.publish(message)


def main():
    rclpy.init()
    node = Gate()
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
