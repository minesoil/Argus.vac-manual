"""Logic checks using installed ROS types; does not move the robot."""
import math
from pathlib import Path
import tempfile
import threading
import time
from types import SimpleNamespace
import unittest
from geometry_msgs.msg import Twist
import command_gate
import controller_bridge
from prepare_lab import circle


class Publisher:
    def __init__(self):
        self.messages = []

    def publish(self, message):
        self.messages.append(message)


class SafetyTests(unittest.TestCase):
    def test_decode(self):
        self.assertEqual(controller_bridge.decode('{"v":100,"w":100,"held":true}'), (.50, 1.2))
        self.assertEqual(controller_bridge.decode('{"v":-100,"w":-100,"held":true}'), (-.30, -1.2))
        self.assertEqual(controller_bridge.decode('{"v":0.1,"w":0.2,"held":false}'), (0., 0.))
        with self.assertRaises(ValueError):
            controller_bridge.decode('{"v":"NaN","w":0,"held":true}')

    def test_manual_watchdog_and_interlock(self):
        from unittest.mock import patch
        fake = SimpleNamespace(pub=Publisher(), lock=threading.Lock(), latest=(.15, .5),
                               received=time.monotonic(), closed=False,
                               states={'collision_monitor': (3, time.monotonic())},
                               scan_at=time.monotonic(), motion_since=0.,
                               report=lambda *args: None)
        with patch.object(controller_bridge, 'MODE') as mode:
            mode.exists.return_value = True
            controller_bridge.Bridge.tick(fake)
            self.assertEqual(fake.pub.messages[-1].linear.x, .15)
            mode.exists.return_value = False
            controller_bridge.Bridge.tick(fake)
            self.assertEqual(fake.pub.messages[-1].linear.x, 0.)
            mode.exists.return_value = True
            fake.received = time.monotonic() - .5
            controller_bridge.Bridge.tick(fake)
            self.assertEqual(fake.pub.messages[-1].linear.x, 0.)
            fake.received = time.monotonic()
            fake.states['collision_monitor'] = (3, time.monotonic() - 2.)
            controller_bridge.Bridge.tick(fake)
            self.assertEqual(fake.pub.messages[-1].linear.x, 0.)
            fake.states['collision_monitor'] = (3, time.monotonic())
            fake.scan_at = time.monotonic() - .6
            controller_bridge.Bridge.tick(fake)
            self.assertEqual(fake.pub.messages[-1].linear.x, 0.)

    def test_gate_mode_and_timeout(self):
        root = Path('/home/robot/vacuum_ws/.lab')
        root.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=root) as folder:
            previous = command_gate.MODE
            command_gate.MODE = Path(folder) / 'manual'
            fake = SimpleNamespace(pub=Publisher(), mode='auto', inputs={'auto': (0.,0.,0.), 'manual': (0.,0.,0.)},
                                   last_status=None, get_logger=lambda: SimpleNamespace(info=lambda msg: None))
            try:
                auto = Twist(); auto.linear.x = .2
                command_gate.Gate.receive(fake, 'auto', auto)
                command_gate.Gate.tick(fake)
                self.assertEqual(fake.pub.messages[-1].linear.x, .2)
                command_gate.MODE.touch()
                command_gate.Gate.tick(fake)
                self.assertEqual(fake.pub.messages[-1].linear.x, 0.)
                command_gate.Gate.receive(fake, 'auto', auto)
                command_gate.Gate.tick(fake)
                self.assertEqual(fake.pub.messages[-1].linear.x, 0.)
                manual = Twist(); manual.linear.x = .1
                command_gate.Gate.receive(fake, 'manual', manual)
                command_gate.Gate.tick(fake)
                self.assertEqual(fake.pub.messages[-1].linear.x, .1)
                fake.inputs['manual'] = (.1, 0., time.monotonic() - .5)
                command_gate.Gate.tick(fake)
                self.assertEqual(fake.pub.messages[-1].linear.x, 0.)
            finally:
                command_gate.MODE = previous

    def test_health_check_recovers_from_lost_response(self):
        from concurrent.futures import Future
        lost, replacement = Future(), Future()
        removed = []
        client = SimpleNamespace(service_is_ready=lambda: True,
                                 remove_pending_request=removed.append,
                                 call_async=lambda request: replacement)
        fake = SimpleNamespace(state_clients={'collision_monitor': client},
                               pending={'collision_monitor': (lost, time.monotonic()-1)},
                               record=lambda *args: None)
        controller_bridge.Bridge.check_states(fake)
        self.assertTrue(lost.cancelled())
        self.assertEqual(removed, [lost])
        self.assertIs(fake.pending['collision_monitor'][0], replacement)

    def test_circular_footprint_and_wheel_envelope(self):
        points = circle(.15)
        for a, b in zip(points, points[1:] + points[:1]):
            ax, ay = a[0]+.03, a[1]
            bx, by = b[0]+.03, b[1]
            distance = abs(ax*by-ay*bx) / math.hypot(bx-ax, by-ay)
            self.assertGreaterEqual(distance, .15 - 1e-6)
        self.assertLess(math.hypot(.03+.05, .22/2+.025/2), .15)


if __name__ == '__main__':
    unittest.main()
