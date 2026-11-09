"""ROS state-machine tests using a fake link; no USB device is opened."""

from pathlib import Path
import sys
import time
import unittest
from unittest.mock import patch

repo = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo / "ros2/src/vacuum_hardware"))
try:
    import rclpy
    from std_srvs.srv import SetBool
    from geometry_msgs.msg import Twist
    from vacuum_hardware.motor_bridge import MotorBridge
    from vacuum_hardware.protocol import Status

    HAS_ROS = True
except ImportError:
    HAS_ROS = False


class FakeLink:
    def __init__(self, *_):
        self.state = Status(1, False, 0, 0, 0)
        self.last = None

    def snapshot(self):
        return True, self.state, time.monotonic(), ""

    def update(self, *args):
        self.last = args

    def close(self):
        pass


@unittest.skipUnless(
    HAS_ROS, "Source ROS 2 Jazzy to run hardware state-machine checks."
)
class HardwareTests(unittest.TestCase):
    def setUp(self):
        rclpy.init(args=[])
        self.patch = patch("vacuum_hardware.motor_bridge.SerialLink", FakeLink)
        self.patch.start()
        self.node = MotorBridge()
        now = time.monotonic()
        self.node.scan_at = self.node.guard_at = now
        self.node.guard_active = True

    def tearDown(self):
        self.node.destroy_node()
        self.patch.stop()
        rclpy.try_shutdown()

    def arm(self):
        return self.node.on_arm(SetBool.Request(data=True), SetBool.Response())

    def test_default_disarmed(self):
        self.assertFalse(self.arm().success)
        self.assertFalse(self.node.armed)

    def test_neutral_handshake_and_timeout(self):
        self.node.settings["motion_enabled"] = True
        self.assertTrue(self.arm().success)
        self.node.tick()
        self.assertEqual(self.node.link.last, (True, 0, 0))
        self.node.link.state = Status(2, True, 0, 0, 0)
        self.node.tick()
        self.assertTrue(self.node.handshake)
        self.node.command_at = time.monotonic() - 1
        self.node.tick()
        self.assertFalse(self.node.armed)

    def test_nonfinite_and_guard_loss(self):
        self.node.settings["motion_enabled"] = True
        self.assertTrue(self.arm().success)
        command = Twist()
        command.linear.x = float("nan")
        self.node.on_command(command)
        self.assertFalse(self.node.armed)
        self.assertTrue(self.arm().success)
        self.node.guard_active = False
        self.node.tick()
        self.assertFalse(self.node.armed)

    def test_moving_command_cannot_arm(self):
        self.node.settings["motion_enabled"] = True
        command = Twist()
        command.linear.x = 0.1
        self.node.on_command(command)
        self.assertFalse(self.arm().success)


if __name__ == "__main__":
    unittest.main()
