import json,subprocess,time,rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
rclpy.init(); node=Node('diagnose_manual'); latest={}
for topic in ['/vacuum/manual_cmd_vel','/vacuum/selected_cmd_vel','/cmd_vel']:
    node.create_subscription(Twist,topic,lambda m,t=topic: latest.update({t:m.linear.x}),10)
node.create_subscription(Odometry,'/odom',lambda m:latest.update({'odom':m.twist.twist.linear.x}),10)
p=subprocess.Popen(['python3','tools/controller_bridge.py'],stdin=subprocess.PIPE,text=True)
started=time.monotonic(); next_print=0
try:
    while time.monotonic()-started<9:
        elapsed=time.monotonic()-started
        p.stdin.write(json.dumps({'v':.1,'w':0.,'held':3<elapsed<7})+'\n');p.stdin.flush()
        rclpy.spin_once(node,timeout_sec=.05);time.sleep(.02)
        if elapsed>=next_print:
            print(round(elapsed,2),latest,flush=True);next_print=elapsed+1
finally:
    p.stdin.close();p.wait(timeout=5);node.destroy_node();rclpy.shutdown()
