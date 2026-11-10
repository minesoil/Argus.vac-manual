"""ROS 2 adapter for the pure avoidance controller.

This node never opens a serial port or arms the motor bridge. Its selected
velocity must pass through a separate, active Collision Monitor. Launch defaults
publish zero to a preview topic; candidate commands remain visible in status.
"""

from dataclasses import fields
import json
import math
import time

import rclpy
from geometry_msgs.msg import Twist
from lifecycle_msgs.msg import State
from lifecycle_msgs.srv import GetState
from rclpy.duration import Duration
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from rclpy.time import Time
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String
from std_srvs.srv import SetBool
from tf2_ros import Buffer, TransformException, TransformListener

from .core import AvoidanceController, Config, Scan


UPSTREAM_TOPICS = frozenset(
    {"/avoidance/preview_cmd_vel", "/avoidance/guard_input",
     "/cmd_vel_raw", "/vacuum/selected_cmd_vel"}
)


def resolved_command_topics(output_topic, manual_topic, resolve):
    """Validate final ROS remapping before creating the command publisher."""
    selected = resolve(output_topic)
    manual = resolve(manual_topic)
    if selected not in UPSTREAM_TOPICS:
        raise ValueError(
            "Resolved output must be a known upstream Collision Monitor input "
            "or preview topic; final /cmd_vel is forbidden, including remappings"
        )
    if selected == manual:
        raise ValueError("Resolved manual input and selected output must differ")
    return selected, manual


def finite_json(value):
    """Keep unobserved/infinite clearances valid in strict JSON viewers."""
    if isinstance(value, float) and not math.isfinite(value):
        return None
    if isinstance(value, dict):
        return {key: finite_json(item) for key, item in value.items()}
    return value


def planar_pose(transform, tilt_limit):
    """Return measured planar sensor pose; reject tilted or malformed frames."""
    q = transform.rotation
    values = (q.x, q.y, q.z, q.w, transform.translation.x,
              transform.translation.y, transform.translation.z)
    if not all(math.isfinite(value) for value in values):
        raise ValueError("Nonfinite sensor transform")
    norm = math.sqrt(q.x*q.x + q.y*q.y + q.z*q.z + q.w*q.w)
    if abs(norm - 1.0) > 0.01:
        raise ValueError("Sensor transform quaternion is not normalized")
    x, y, z, w = q.x/norm, q.y/norm, q.z/norm, q.w/norm
    roll = math.atan2(2.0*(w*x+y*z), 1.0-2.0*(x*x+y*y))
    pitch = math.asin(max(-1.0, min(1.0, 2.0*(w*y-z*x))))
    if abs(roll) > tilt_limit or abs(pitch) > tilt_limit:
        raise ValueError("Lidar scan plane is tilted relative to the robot")
    yaw = math.atan2(2.0*(w*z+x*y), 1.0-2.0*(y*y+z*z))
    return transform.translation.x, transform.translation.y, yaw


class AvoidanceNode(Node):
    def __init__(self):
        super().__init__("argus_avoidance")
        defaults = Config()
        settings = {
            field.name: self.declare_parameter(
                field.name, getattr(defaults, field.name)
            ).value for field in fields(Config)
        }
        self.config = Config(**settings)
        self.controller = AvoidanceController(self.config)
        self.enable_output = self.declare_parameter("enable_output", False).value
        self.output_topic = self.declare_parameter(
            "output_topic", "/avoidance/preview_cmd_vel"
        ).value
        if self.output_topic not in UPSTREAM_TOPICS:
            raise ValueError(
                "output_topic must be a known upstream Collision Monitor input "
                "or /avoidance/preview_cmd_vel; final /cmd_vel is forbidden"
            )
        self.scan_topic = self.declare_parameter("scan_topic", "/scan").value
        self.base_frame = self.declare_parameter("base_frame", "base_link").value
        self.manual_topic = self.declare_parameter(
            "manual_topic", "/avoidance/manual_cmd_vel"
        ).value
        self.guard_service = self.declare_parameter(
            "guard_service", "/collision_monitor/get_state"
        ).value
        self.manual_timeout = self._positive("manual_timeout_s", 0.25)
        self.guard_timeout = self._positive("guard_timeout_s", 0.75)
        self.stamp_timeout = self._positive("scan_stamp_timeout_s", 0.5)
        self.future_tolerance = self._positive("future_stamp_tolerance_s", 0.05)
        self.tilt_limit = self._positive("scan_tilt_limit_rad", 0.05)
        self.tf_timeout = self._positive("transform_timeout_s", 0.02)
        self.resolved_output_topic, self.resolved_manual_topic = resolved_command_topics(
            self.output_topic, self.manual_topic, self.resolve_topic_name
        )

        self.mode = "disarmed"
        self.fault_latched = False
        self.adapter_fault = "Waiting for a valid scan and sensor transform"
        self.manual_command = (0.0, 0.0)
        self.manual_at = None
        self.guard_active = False
        self.guard_at = None
        self.guard_future = None
        self.guard_requested_at = None
        self.last_scan_stamp_ns = None
        self.last_scan_frame = None
        self.last_ros_clock_ns = None
        self.last_status_at = -math.inf
        self.tf_buffer = Buffer(cache_time=Duration(seconds=5.0))
        self.tf_listener = TransformListener(self.tf_buffer, self)
        self.velocity = self.create_publisher(Twist, self.output_topic, 1)
        self.status = self.create_publisher(String, "/avoidance/status", 10)
        self.create_subscription(
            LaserScan, self.scan_topic, self.on_scan, qos_profile_sensor_data
        )
        self.create_subscription(Twist, self.manual_topic, self.on_manual, 1)
        self.create_service(SetBool, "/avoidance/set_auto", self.on_set_auto)
        self.guard_client = self.create_client(GetState, self.guard_service)
        self.create_timer(0.25, self.poll_guard)
        self.create_timer(0.05, self.tick)
        self.get_logger().info(
            f"Selected output: {self.resolved_output_topic}; enable_output={self.enable_output}. "
            "Automatic and manual selection start disarmed. No motor arming performed."
        )

    def _positive(self, name, default):
        value = self.declare_parameter(name, default).value
        if isinstance(value, bool) or not isinstance(value, (int, float)) \
                or not math.isfinite(value) or value <= 0:
            raise ValueError(f"{name} must be positive and finite")
        return float(value)

    def poll_guard(self):
        now = time.monotonic()
        if self.guard_future is not None:
            if now-self.guard_requested_at > self.guard_timeout:
                # A delayed ACTIVE reply cannot renew the guard's freshness.
                self.guard_active = False
                if not self.guard_future.done():
                    self.guard_future.cancel()
                self.guard_future = None
                return
            if not self.guard_future.done():
                return
            try:
                response = self.guard_future.result()
                self.guard_active = (
                    response is not None
                    and response.current_state.id == State.PRIMARY_STATE_ACTIVE
                )
                self.guard_at = self.guard_requested_at
            except Exception as exc:
                self.guard_active = False
                self.get_logger().warning(f"Collision Monitor state query failed: {exc}")
            self.guard_future = None
        if not self.guard_client.service_is_ready():
            self.guard_active = False
            return
        self.guard_requested_at = now
        try:
            self.guard_future = self.guard_client.call_async(GetState.Request())
        except Exception as exc:
            self.guard_active = False
            self.guard_future = None
            self.latch_fault("Collision Monitor state query could not be sent")
            self.get_logger().warning(f"Collision Monitor query unavailable: {exc}")

    def on_scan(self, message):
        received_at = time.monotonic()
        try:
            if not message.header.frame_id:
                raise ValueError("Lidar scan has no frame_id")
            stamp = Time.from_msg(message.header.stamp)
            if stamp.nanoseconds <= 0:
                raise ValueError("Lidar scan has no positive timestamp")
            ros_now_ns = self.get_clock().now().nanoseconds
            if self.last_ros_clock_ns is not None \
                    and ros_now_ns < self.last_ros_clock_ns-self.future_tolerance*1e9:
                self.last_scan_stamp_ns = None
                self.last_scan_frame = None
                self.last_ros_clock_ns = ros_now_ns
                raise ValueError("ROS clock moved backward; fresh scans and re-selection required")
            self.last_ros_clock_ns = ros_now_ns
            if self.last_scan_frame == message.header.frame_id \
                    and self.last_scan_stamp_ns is not None \
                    and stamp.nanoseconds <= self.last_scan_stamp_ns:
                raise ValueError("Repeated or out-of-order lidar timestamp")
            age = (ros_now_ns-stamp.nanoseconds)*1e-9
            if age < -self.future_tolerance or age > self.stamp_timeout:
                raise ValueError("Lidar timestamp is stale or in the future")
            transform = self.tf_buffer.lookup_transform(
                self.base_frame, message.header.frame_id, stamp,
                timeout=Duration(seconds=self.tf_timeout),
            )
            x, y, yaw = planar_pose(transform.transform, self.tilt_limit)
            self.controller.observe(Scan(
                ranges=tuple(message.ranges),
                angle_min=float(message.angle_min),
                angle_increment=float(message.angle_increment),
                range_min=float(message.range_min),
                range_max=float(message.range_max),
                # Anchor expiry to source acquisition, not arrival at this node.
                received_at=received_at-max(age, 0.0),
                sensor_x=x, sensor_y=y, sensor_yaw=yaw,
            ))
            self.last_scan_stamp_ns = stamp.nanoseconds
            self.last_scan_frame = message.header.frame_id
            self.adapter_fault = ""
        except (ValueError, TypeError, TransformException) as exc:
            self.adapter_fault = str(exc)
            self.latch_fault(self.adapter_fault)

    def on_manual(self, message):
        values = (message.linear.x, message.linear.y, message.linear.z,
                  message.angular.x, message.angular.y, message.angular.z)
        if not all(math.isfinite(value) for value in values):
            self.latch_fault("Nonfinite manual velocity")
            return
        if any(abs(value) > 1e-8 for value in (
            message.linear.y, message.linear.z, message.angular.x, message.angular.y
        )):
            self.latch_fault("Unsupported manual velocity axis")
            return
        self.manual_command = (
            max(-self.config.forward_m_s,
                min(self.config.forward_m_s, message.linear.x)),
            max(-self.config.turn_rad_s,
                min(self.config.turn_rad_s, message.angular.z)),
        )
        self.manual_at = time.monotonic()

    def safety_health(self, now):
        if self.adapter_fault:
            return False, self.adapter_fault
        if not self.guard_active or self.guard_at is None \
                or now-self.guard_at > self.guard_timeout:
            return False, "Collision Monitor is inactive or its state is stale"
        return self.controller.health(now)

    def latch_fault(self, reason):
        self.controller.disarm(reason)
        self.manual_command = (0.0, 0.0)
        self.manual_at = None
        if self.mode != "disarmed":
            self.fault_latched = True
        self.publish_velocity(0.0, 0.0)

    def on_set_auto(self, request, response):
        now = time.monotonic()
        self.controller.disarm("Mode selection changed")
        self.manual_command = (0.0, 0.0)
        self.manual_at = None
        self.publish_velocity(0.0, 0.0)
        healthy, reason = self.safety_health(now)
        if not healthy:
            self.mode = "disarmed"
            self.fault_latched = True
            response.success = not request.data
            response.message = f"Automatic mode disabled; selection remains disarmed: {reason}"
            return response
        self.fault_latched = False
        if request.data:
            success, reason = self.controller.arm(now)
            self.mode = "auto" if success else "disarmed"
            response.success = success
            response.message = reason
        else:
            self.mode = "manual"
            response.success = True
            response.message = "Manual selected; waiting for a new manual command"
        if not self.enable_output:
            response.message += "; output disabled, candidate commands only in status"
        return response

    def publish_velocity(self, linear, angular):
        message = Twist()
        if self.enable_output:
            message.linear.x = float(linear)
            message.angular.z = float(angular)
        self.velocity.publish(message)

    def tick(self):
        now = time.monotonic()
        healthy, reason = self.safety_health(now)
        if not healthy and self.mode != "disarmed":
            self.latch_fault(reason)
        decision = self.controller.step(now)
        linear, angular = 0.0, 0.0
        state, selected_reason = decision.state, decision.reason
        if self.fault_latched:
            state, selected_reason = "FAULT", reason if not healthy else "Re-select mode to clear fault"
        elif self.mode == "auto" and healthy:
            linear, angular = decision.linear, decision.angular
        elif self.mode == "manual" and healthy:
            state = "MANUAL"
            if self.manual_at is not None and now-self.manual_at <= self.manual_timeout:
                linear, angular = self.manual_command
                selected_reason = "Fresh manual command; final Collision Monitor still applies"
            else:
                selected_reason = "Manual command missing or expired"
        elif self.mode == "disarmed":
            state, selected_reason = "DISARMED", reason if not healthy else "Select manual or automatic mode"
        self.publish_velocity(linear, angular)
        if now-self.last_status_at >= 0.2:
            self.last_status_at = now
            message = String()
            message.data = json.dumps(finite_json({
                "state": state, "reason": selected_reason, "mode": self.mode,
                "output_enabled": self.enable_output,
                "output_topic": self.resolved_output_topic,
                "candidate_linear_m_s": linear, "candidate_angular_rad_s": angular,
                "front_clearance_m": decision.front_clearance,
                "left_clearance_m": decision.left_clearance,
                "right_clearance_m": decision.right_clearance,
                "guard_active": healthy and self.guard_active,
                "fault_latched": self.fault_latched,
            }), allow_nan=False)
            self.status.publish(message)


def main(args=None):
    rclpy.init(args=args)
    node = None
    try:
        node = AvoidanceNode()
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if node is not None:
            node.controller.disarm("Controller shutting down")
            if rclpy.ok():
                node.publish_velocity(0.0, 0.0)
            node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()
