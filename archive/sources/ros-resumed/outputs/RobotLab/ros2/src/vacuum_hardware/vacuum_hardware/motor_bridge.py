"""ROS velocity -> Mega pulses. Arms explicitly and publishes issued-step odometry.

No encoder feedback exists in the specified hardware. /odom and joint_states are
therefore estimates; slipping wheels/missed steps cannot be observed here.
"""

import json
import math
import time
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from geometry_msgs.msg import Twist, TransformStamped
from nav_msgs.msg import Odometry
from sensor_msgs.msg import JointState, LaserScan
from std_msgs.msg import String
from std_srvs.srv import SetBool
from lifecycle_msgs.srv import GetState
from tf2_ros import TransformBroadcaster
from .protocol import wheel_rates, count_delta
from .serial_link import SerialLink


class MotorBridge(Node):
    def __init__(self):
        super().__init__("motor_bridge")
        defaults = {
            "serial_port": "/dev/robot_mega",
            "serial_baud": 115200,
            "motion_enabled": False,
            "wheel_radius_m": 0.035,
            "wheel_separation_m": 0.22,
            "steps_per_revolution": 1600,
            "forward_m_s": 0.15,
            "reverse_m_s": 0.08,
            "turn_rad_s": 0.8,
            "command_timeout_s": 0.25,
            "scan_timeout_s": 0.5,
            "acceleration_m_s2": 0.4,
            "angular_acceleration_rad_s2": 1.5,
        }
        self.settings = {
            k: self.declare_parameter(k, v).value for k, v in defaults.items()
        }
        for key in defaults:
            if key not in ("serial_port", "motion_enabled") and (
                not math.isfinite(self.settings[key]) or self.settings[key] <= 0
            ):
                raise ValueError(f"{key} must be positive and finite.")
        self.link = SerialLink(
            self.settings["serial_port"], self.settings["serial_baud"]
        )
        self.armed = False
        self.handshake = False
        self.reason = "Disarmed"
        self.velocity = [0.0, 0.0]
        self.command = [0.0, 0.0]
        self.command_at = 0.0
        self.scan_at = 0.0
        self.guard_active = False
        self.guard_at = 0.0
        self.guard_future = None
        self.guard_sent = 0.0
        self.pose = [0.0, 0.0, 0.0]
        self.previous_steps = None
        self.odom_at = 0.0
        self.last_report = 0.0
        self.received_sequence = None
        self.create_subscription(Twist, "/cmd_vel", self.on_command, 1)
        self.create_subscription(
            LaserScan, "/scan", self.on_scan, qos_profile_sensor_data
        )
        self.create_service(SetBool, "/drive/arm", self.on_arm)
        self.guard_client = self.create_client(GetState, "/collision_monitor/get_state")
        self.odom = self.create_publisher(Odometry, "/odom", 10)
        self.joints = self.create_publisher(JointState, "/joint_states", 10)
        self.health = self.create_publisher(String, "/drive/status", 10)
        self.tf = TransformBroadcaster(self)
        self.last_tick = time.monotonic()
        self.timer = self.create_timer(0.02, self.tick)

    def disarm(self, reason):
        self.armed = False
        self.handshake = False
        self.velocity = [0.0, 0.0]
        self.reason = reason
        self.link.update(False, 0, 0)

    def on_command(self, msg):
        if not math.isfinite(msg.linear.x) or not math.isfinite(msg.angular.z):
            self.disarm("Nonfinite velocity")
            return
        p = self.settings
        self.command = [
            max(-p["reverse_m_s"], min(p["forward_m_s"], msg.linear.x)),
            max(-p["turn_rad_s"], min(p["turn_rad_s"], msg.angular.z)),
        ]
        self.command_at = time.monotonic()

    def on_scan(self, msg):
        # Empty/invalid scans cannot keep the motor guard alive.
        if msg.ranges and any(
            math.isfinite(x) and msg.range_min <= x <= msg.range_max for x in msg.ranges
        ):
            self.scan_at = time.monotonic()

    def ready(self, now, status, received):
        return (
            status is not None
            and now - received < 0.25
            and status.fault == 0
            and now - self.scan_at < self.settings["scan_timeout_s"]
            and self.guard_active
            and now - self.guard_at < 1.5
        )

    def on_arm(self, request, response):
        if not request.data:
            self.disarm("Disarmed by user")
            response.success = True
            response.message = self.reason
            return response
        now = time.monotonic()
        connected, status, received, error = self.link.snapshot()
        if not self.settings["motion_enabled"]:
            response.message = "Set motion_enabled after wiring and wheel calibration."
        elif not connected or not self.ready(now, status, received):
            response.message = "Mega, lidar or collision guard is not ready. " + error
        elif now - self.command_at < self.settings["command_timeout_s"] and any(
            abs(x) > 0.001 for x in self.command
        ):
            response.message = "Centre the drive command before arming."
        else:
            self.armed = True
            self.handshake = False
            self.reason = "Armed at zero"
            response.success = True
            response.message = self.reason
        return response

    def tick(self):
        now = time.monotonic()
        dt = min(0.05, now - self.last_tick)
        self.last_tick = now
        if self.guard_future:
            if self.guard_future.done():
                try:
                    self.guard_active = self.guard_future.result().current_state.id == 3
                    self.guard_at = now
                except Exception:
                    self.guard_active = False
                self.guard_future = None
            elif now - self.guard_sent > 0.75:
                self.guard_client.remove_pending_request(self.guard_future)
                self.guard_future = None
                self.guard_active = False
        elif now - self.guard_sent > 0.5 and self.guard_client.service_is_ready():
            self.guard_sent = now
            self.guard_future = self.guard_client.call_async(GetState.Request())
        connected, status, received, error = self.link.snapshot()
        if self.armed:
            if not connected or not self.ready(now, status, received):
                self.disarm("Hardware/guard health lost: " + error)
            elif (
                now - self.command_at > self.settings["command_timeout_s"]
                and self.handshake
            ):
                self.disarm("Drive input expired")
        if self.armed:
            if not self.handshake:
                self.link.update(True, 0, 0)
                if status.armed:
                    self.handshake = True
                    self.command_at = now
            else:
                for i, acceleration in enumerate(
                    (
                        self.settings["acceleration_m_s2"],
                        self.settings["angular_acceleration_rad_s2"],
                    )
                ):
                    self.velocity[i] += max(
                        -acceleration * dt,
                        min(acceleration * dt, self.command[i] - self.velocity[i]),
                    )
                left, right = wheel_rates(
                    *self.velocity,
                    self.settings["wheel_radius_m"],
                    self.settings["wheel_separation_m"],
                    self.settings["steps_per_revolution"],
                )
                self.link.update(True, left, right)
        else:
            self.link.update(False, 0, 0)
        if status and received != self.last_report:
            self.publish_odometry(status, received)
            self.last_report = received
        if int(now * 5) != int((now - dt) * 5):
            self.health.publish(
                String(
                    data=json.dumps(
                        {
                            "armed": self.armed,
                            "ready": self.ready(now, status, received),
                            "reason": self.reason,
                            "serial_error": error,
                            "firmware_fault": status.fault if status else None,
                            "odometry": "issued steps; no encoders",
                        }
                    )
                )
            )

    def publish_odometry(self, status, received):
        counts = [status.left_steps, status.right_steps]
        if self.previous_steps is None or received - self.odom_at > 0.5:
            self.previous_steps = counts
            self.odom_at = received
            return
        delta = [count_delta(counts[i], self.previous_steps[i]) for i in range(2)]
        self.previous_steps = counts
        dt = max(0.001, received - self.odom_at)
        self.odom_at = received
        metres = (
            2
            * math.pi
            * self.settings["wheel_radius_m"]
            / self.settings["steps_per_revolution"]
        )
        dl, dr = [x * metres for x in delta]
        distance = (dl + dr) / 2
        angle = (dr - dl) / self.settings["wheel_separation_m"]
        # Reject counter resets/jumps rather than teleporting odometry on USB reset.
        if abs(dl) > dt * 0.5 + 0.03 or abs(dr) > dt * 0.5 + 0.03:
            self.disarm("Unexpected step counter reset")
            return
        self.pose[0] += distance * math.cos(self.pose[2] + angle / 2)
        self.pose[1] += distance * math.sin(self.pose[2] + angle / 2)
        self.pose[2] += angle
        stamp = self.get_clock().now().to_msg()
        odom = Odometry()
        odom.header.stamp = stamp
        odom.header.frame_id = "odom"
        odom.child_frame_id = "base_footprint"
        odom.pose.pose.position.x, odom.pose.pose.position.y = self.pose[:2]
        odom.pose.pose.orientation.z = math.sin(self.pose[2] / 2)
        odom.pose.pose.orientation.w = math.cos(self.pose[2] / 2)
        odom.twist.twist.linear.x = distance / dt
        odom.twist.twist.angular.z = angle / dt
        for i in (0, 7):
            odom.pose.covariance[i] = 0.05
            odom.twist.covariance[i] = 0.05
        odom.pose.covariance[35] = 0.1
        odom.twist.covariance[35] = 0.1
        self.odom.publish(odom)
        tf = TransformStamped()
        tf.header = odom.header
        tf.child_frame_id = odom.child_frame_id
        tf.transform.translation.x, tf.transform.translation.y = self.pose[:2]
        tf.transform.rotation = odom.pose.pose.orientation
        self.tf.sendTransform(tf)
        joints = JointState()
        joints.header.stamp = stamp
        joints.name = ["left_wheel_joint", "right_wheel_joint"]
        joints.position = [
            x * 2 * math.pi / self.settings["steps_per_revolution"] for x in counts
        ]
        self.joints.publish(joints)

    def destroy_node(self):
        self.disarm("Bridge shutdown")
        self.link.close()
        super().destroy_node()


def main():
    rclpy.init()
    node = MotorBridge()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()
