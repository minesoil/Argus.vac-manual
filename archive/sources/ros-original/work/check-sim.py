#!/usr/bin/env python3
"""Measure actual simulated ROS sensors, odometry, motion and command expiry."""
import json
import math
import time
from pathlib import Path
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan, Image, CameraInfo

rclpy.init()
node = Node('vacuum_setup_validation', parameter_overrides=[rclpy.parameter.Parameter('use_sim_time', value=True)])
latest = {}
counts = {}
def receive(key):
    def callback(message):
        latest[key] = message
        counts[key] = counts.get(key, 0) + 1
    return callback
subs = [node.create_subscription(kind, topic, receive(key), qos_profile_sensor_data)
        for kind, topic, key in [(Odometry, '/odom', 'odom'), (LaserScan, '/scan', 'scan'),
                                 (Image, '/camera/image_raw', 'image'), (CameraInfo, '/camera/camera_info', 'camera_info')]]
publisher = node.create_publisher(Twist, '/cmd_vel', 10)
def spin(seconds, command=None):
    end = time.monotonic() + seconds
    next_pub = 0
    while time.monotonic() < end:
        if command is not None and time.monotonic() >= next_pub:
            publisher.publish(command)
            next_pub = time.monotonic() + 0.1
        rclpy.spin_once(node, timeout_sec=0.05)
spin(12)
assert all(key in latest for key in ('odom', 'scan', 'image', 'camera_info')), counts
origin = latest['odom'].pose.pose.position
start = (origin.x, origin.y)
command = Twist()
command.linear.x = 0.15
spin(4, command)
position = latest['odom'].pose.pose.position
distance = math.hypot(position.x-start[0], position.y-start[1])
# Stop publishing; verify controller's timeout independently from a zero command.
spin(3)
velocity = latest['odom'].twist.twist
scan = latest['scan']
result = dict(counts=counts, distance_m=distance, stopped_linear_m_s=velocity.linear.x,
              stopped_yaw_rad_s=velocity.angular.z, scan_samples=len(scan.ranges),
              finite_scan_samples=sum(math.isfinite(x) for x in scan.ranges),
              scan_frame=scan.header.frame_id, image_frame=latest['image'].header.frame_id,
              image_size=[latest['image'].width, latest['image'].height],
              camera_info_frame=latest['camera_info'].header.frame_id)
publisher.publish(Twist())
Path('/home/robot/vacuum_ws/simulation-check.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
assert distance > 0.2, 'Robot did not move as expected'
assert abs(velocity.linear.x) < 0.02 and abs(velocity.angular.z) < 0.02, 'Command expiry failed'
assert scan.header.frame_id == 'lidar_link' and len(scan.ranges) == 360
assert latest['image'].header.frame_id == 'camera_optical_frame'
assert latest['camera_info'].header.frame_id == 'camera_optical_frame'
node.destroy_node()
rclpy.shutdown()
