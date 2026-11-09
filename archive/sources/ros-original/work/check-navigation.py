#!/usr/bin/env python3
import json
import time
from pathlib import Path
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from rclpy.qos import QoSProfile, DurabilityPolicy, ReliabilityPolicy
from nav_msgs.msg import OccupancyGrid
from nav2_msgs.action import NavigateToPose

rclpy.init()
node = Node('vacuum_navigation_validation', parameter_overrides=[rclpy.parameter.Parameter('use_sim_time', value=True)])
maps = []
sub = node.create_subscription(OccupancyGrid, '/map', maps.append,
    QoSProfile(depth=1, durability=DurabilityPolicy.TRANSIENT_LOCAL, reliability=ReliabilityPolicy.RELIABLE))
client = ActionClient(node, NavigateToPose, '/navigate_to_pose')
end = time.monotonic()+30
while not maps and time.monotonic()<end:
    rclpy.spin_once(node, timeout_sec=0.1)
assert maps, 'SLAM did not publish a map'
message = maps[-1]
summary = dict(map_width=message.info.width, map_height=message.info.height,
               known_cells=sum(x>=0 for x in message.data), occupied_cells=sum(x>50 for x in message.data))
assert summary['known_cells'] > 100 and summary['occupied_cells'] > 20, summary
assert client.wait_for_server(timeout_sec=30), 'Nav2 action server unavailable'
goal = NavigateToPose.Goal()
goal.pose.header.frame_id = 'map'
goal.pose.header.stamp = node.get_clock().now().to_msg()
goal.pose.pose.position.x = 1.0
goal.pose.pose.position.y = 0.0
goal.pose.pose.orientation.w = 1.0
future = client.send_goal_async(goal)
rclpy.spin_until_future_complete(node, future, timeout_sec=10)
handle = future.result()
assert handle is not None and handle.accepted, 'Nav2 rejected goal'
result_future = handle.get_result_async()
end = time.monotonic()+120
while not result_future.done() and time.monotonic()<end:
    rclpy.spin_once(node, timeout_sec=0.1)
if not result_future.done():
    cancel = handle.cancel_goal_async()
    rclpy.spin_until_future_complete(node, cancel, timeout_sec=5)
    raise RuntimeError('Navigation validation timed out; goal cancelled')
result = result_future.result()
summary.update(goal=[1.0, 0.0], status=result.status, error_code=result.result.error_code)
Path('/home/robot/vacuum_ws/navigation-check.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
assert result.status == 4 and result.result.error_code == 0, 'Navigation failed'
node.destroy_node()
rclpy.shutdown()
