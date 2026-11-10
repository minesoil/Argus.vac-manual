"""Offline adapter checks with ROS stand-ins; these are not ROS integration tests.

The production adapter is imported unchanged. Only its ROS dependencies and
message/service transports are replaced; the controller and adapter methods run.
"""

import importlib.util
import json
import math
from pathlib import Path
import sys
import types
import unittest
from unittest import mock

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE_ROOT))
from argus_avoidance.core import AvoidanceController, Config


class Twist:
    def __init__(self):
        self.linear = types.SimpleNamespace(x=0.0, y=0.0, z=0.0)
        self.angular = types.SimpleNamespace(x=0.0, y=0.0, z=0.0)


class Time:
    @staticmethod
    def from_msg(stamp):
        return types.SimpleNamespace(nanoseconds=stamp.nanoseconds)


class TransformException(Exception):
    pass


def load_adapter():
    def module(**attributes):
        result = types.ModuleType("offline_ros_standin")
        result.__dict__.update(attributes)
        return result

    stubs = {
        "rclpy": module(),
        "rclpy.node": module(Node=object),
        "rclpy.duration": module(Duration=lambda **kwargs: None),
        "rclpy.qos": module(qos_profile_sensor_data=object()),
        "rclpy.time": module(Time=Time),
        "geometry_msgs": module(),
        "geometry_msgs.msg": module(Twist=Twist),
        "lifecycle_msgs": module(),
        "lifecycle_msgs.msg": module(State=types.SimpleNamespace(PRIMARY_STATE_ACTIVE=3)),
        "lifecycle_msgs.srv": module(GetState=types.SimpleNamespace(Request=object)),
        "sensor_msgs": module(),
        "sensor_msgs.msg": module(LaserScan=object),
        "std_msgs": module(),
        "std_msgs.msg": module(String=types.SimpleNamespace),
        "std_srvs": module(),
        "std_srvs.srv": module(SetBool=object),
        "tf2_ros": module(Buffer=object, TransformException=TransformException,
                          TransformListener=object),
    }
    spec = importlib.util.spec_from_file_location(
        "argus_avoidance._offline_adapter", PACKAGE_ROOT / "argus_avoidance/node.py"
    )
    adapter = importlib.util.module_from_spec(spec)
    with mock.patch.dict(sys.modules, stubs):
        spec.loader.exec_module(adapter)
    return adapter


adapter = load_adapter()


def sensor_pose(roll=0.0):
    return types.SimpleNamespace(
        rotation=types.SimpleNamespace(x=math.sin(roll/2), y=0.0, z=0.0,
                                       w=math.cos(roll/2)),
        translation=types.SimpleNamespace(x=0.1, y=-0.02, z=0.2),
    )


class AdapterTests(unittest.TestCase):
    def node(self, ros_now=1_000_000_000):
        node = object.__new__(adapter.AvoidanceNode)
        node.config = Config()
        node.controller = AvoidanceController(node.config)
        node.mode = "auto"
        node.fault_latched = False
        node.adapter_fault = ""
        node.manual_at = None
        node.manual_command = (0.0, 0.0)
        node.last_scan_stamp_ns = None
        node.last_scan_frame = None
        node.last_ros_clock_ns = None
        node.future_tolerance = 0.05
        node.stamp_timeout = 0.5
        node.tf_timeout = 0.02
        node.tilt_limit = 0.05
        node.base_frame = "base_link"
        node.guard_timeout = 0.75
        node.guard_active = True
        node.guard_at = 10.0
        node.guard_future = None
        node.guard_requested_at = None
        node.guard_client = mock.Mock()
        node.guard_client.service_is_ready.return_value = True
        node.get_logger = mock.Mock()
        node.publish_velocity = mock.Mock()
        node.clock_ns = ros_now
        node.get_clock = lambda: types.SimpleNamespace(
            now=lambda: types.SimpleNamespace(nanoseconds=node.clock_ns)
        )
        node.tf_buffer = mock.Mock()
        node.tf_buffer.lookup_transform.return_value = types.SimpleNamespace(
            transform=sensor_pose()
        )
        return node

    def scan(self, stamp=1_000_000_000):
        return types.SimpleNamespace(
            header=types.SimpleNamespace(frame_id="lidar_link",
                                         stamp=types.SimpleNamespace(nanoseconds=stamp)),
            ranges=[4.0]*720, angle_min=-math.pi,
            angle_increment=math.tau/720, range_min=0.05, range_max=12.0,
        )

    def test_delayed_scan_keeps_source_expiry(self):
        node = self.node(ros_now=1_490_000_000)
        with mock.patch.object(adapter.time, "monotonic", return_value=10.0):
            node.on_scan(self.scan())
        self.assertEqual(node.adapter_fault, "")
        self.assertTrue(node.controller.health(10.0)[0])
        self.assertFalse(node.controller.health(10.02)[0])

    def test_scan_duplicate_latches_and_stops(self):
        node = self.node()
        with mock.patch.object(adapter.time, "monotonic", return_value=10.0):
            node.on_scan(self.scan())
            node.on_scan(self.scan())
        self.assertTrue(node.fault_latched)
        self.assertIn("Repeated", node.adapter_fault)
        node.publish_velocity.assert_called_with(0.0, 0.0)

    def test_backward_clock_requires_reselection_after_fresh_scan(self):
        node = self.node()
        with mock.patch.object(adapter.time, "monotonic", return_value=10.0):
            node.on_scan(self.scan())
            node.clock_ns = 100_000_000
            node.on_scan(self.scan(100_000_000))
            self.assertIn("clock moved backward", node.adapter_fault)
            node.clock_ns = 200_000_000
            node.on_scan(self.scan(200_000_000))
        self.assertEqual(node.adapter_fault, "")
        self.assertTrue(node.fault_latched)

    def test_stale_or_future_scan_rejected(self):
        for stamp in (400_000_000, 1_100_000_000):
            with self.subTest(stamp=stamp):
                node = self.node()
                with mock.patch.object(adapter.time, "monotonic", return_value=10.0):
                    node.on_scan(self.scan(stamp))
                self.assertTrue(node.fault_latched)
                self.assertIn("stale or in the future", node.adapter_fault)

    def test_tilted_scan_rejected(self):
        node = self.node()
        node.tf_buffer.lookup_transform.return_value.transform = sensor_pose(roll=0.2)
        with mock.patch.object(adapter.time, "monotonic", return_value=10.0):
            node.on_scan(self.scan())
        self.assertTrue(node.fault_latched)
        self.assertIn("tilted", node.adapter_fault)

    def test_late_active_guard_reply_cannot_refresh_health(self):
        node = self.node()
        node.guard_requested_at = 9.0
        node.guard_future = mock.Mock()
        node.guard_future.done.return_value = True
        node.guard_future.result.return_value = types.SimpleNamespace(
            current_state=types.SimpleNamespace(id=3)
        )
        old_future = node.guard_future
        with mock.patch.object(adapter.time, "monotonic", return_value=10.0):
            node.poll_guard()
        self.assertFalse(node.guard_active)
        old_future.result.assert_not_called()
        self.assertEqual(node.guard_at, 10.0)

    def test_guard_reply_age_anchored_to_request(self):
        node = self.node()
        node.guard_requested_at = 9.5
        node.guard_future = mock.Mock()
        node.guard_future.done.return_value = True
        node.guard_future.result.return_value = types.SimpleNamespace(
            current_state=types.SimpleNamespace(id=3)
        )
        with mock.patch.object(adapter.time, "monotonic", return_value=10.0):
            node.poll_guard()
        self.assertTrue(node.guard_active)
        self.assertEqual(node.guard_at, 9.5)

    def test_guard_query_send_failure_stops(self):
        node = self.node()
        node.guard_client.call_async.side_effect = RuntimeError("Service lost")
        with mock.patch.object(adapter.time, "monotonic", return_value=10.0):
            node.poll_guard()
        self.assertFalse(node.guard_active)
        self.assertTrue(node.fault_latched)
        node.publish_velocity.assert_called_with(0.0, 0.0)

    def test_manual_bounds_and_nonfinite_stop(self):
        node = self.node()
        message = Twist()
        message.linear.x, message.angular.z = 10.0, 10.0
        node.on_manual(message)
        self.assertEqual(node.manual_command, (0.05, 0.3))
        message.linear.x = -10.0
        node.on_manual(message)
        self.assertEqual(node.manual_command, (-0.05, 0.3))
        message.angular.z = float("nan")
        node.on_manual(message)
        self.assertEqual(node.manual_command, (0.0, 0.0))
        self.assertTrue(node.fault_latched)

    def test_resolved_output_and_manual_loop_rejected(self):
        mappings = [
            {"/avoidance/preview_cmd_vel": "/cmd_vel"},
            {"/cmd_vel_raw": "/cmd_vel"},
            {"/avoidance/manual_cmd_vel": "/avoidance/preview_cmd_vel"},
        ]
        for mapping in mappings:
            with self.subTest(mapping=mapping), self.assertRaises(ValueError):
                output = "/cmd_vel_raw" if "/cmd_vel_raw" in mapping else "/avoidance/preview_cmd_vel"
                adapter.resolved_command_topics(
                    output, "/avoidance/manual_cmd_vel",
                    lambda name: mapping.get(name, name),
                )

    def test_status_nonfinite_values_become_json_null(self):
        data = adapter.finite_json({"front": float("inf"), "nested": {"bad": float("nan")}})
        self.assertEqual(json.loads(json.dumps(data, allow_nan=False)),
                         {"front": None, "nested": {"bad": None}})


if __name__ == "__main__":
    unittest.main()
