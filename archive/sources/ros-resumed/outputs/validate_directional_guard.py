"""Exercise the exact drive guard in an isolated namespace, with no motor output."""
import copy
import json
import math
from pathlib import Path
import subprocess
import time
import yaml
import rclpy
from rclpy.node import Node
from rclpy.parameter import Parameter
from rclpy.qos import qos_profile_sensor_data
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from lifecycle_msgs.srv import ChangeState

WS=Path('/home/robot/vacuum_ws')
OUT=WS/'validation/furnished-20261007'
OUT.mkdir(parents=True,exist_ok=True)
p=copy.deepcopy(yaml.safe_load((WS/'.lab/drive-guard.yaml').read_text())['collision_monitor']['ros__parameters'])
p.update(cmd_vel_in_topic='/furnished_guard_test/input',cmd_vel_out_topic='/furnished_guard_test/output',state_topic='/furnished_guard_test/state')
p['scan']['topic']='/furnished_guard_test/scan'
for key in ('StopZone','SlowZone'):p[key]['polygon_pub_topic']='/furnished_guard_test/'+key
config=OUT/'isolated-guard.yaml'
config.write_text(yaml.safe_dump({'/furnished_guard_test/collision_monitor':{'ros__parameters':p}}))
rclpy.init()
node=Node('furnished_guard_validation',parameter_overrides=[Parameter('use_sim_time',value=True)])
outputs=[]
node.create_subscription(Twist,'/furnished_guard_test/output',outputs.append,10)
pub=node.create_publisher(Twist,'/furnished_guard_test/input',10)
scans=node.create_publisher(LaserScan,'/furnished_guard_test/scan',qos_profile_sensor_data)
service=node.create_client(ChangeState,'/furnished_guard_test/collision_monitor/change_state')
log=(OUT/'isolated-guard.log').open('w')
proc=subprocess.Popen(['/opt/ros/jazzy/lib/nav2_collision_monitor/collision_monitor','--ros-args','-r','__ns:=/furnished_guard_test','-r','tf:=/tf','-r','tf_static:=/tf_static','--params-file',str(config)],stdout=log,stderr=subprocess.STDOUT)
report={'scope':'isolated test topics; no robot command output','tests':{}}


def wait(predicate,seconds):
    end=time.monotonic()+seconds
    while not predicate() and time.monotonic()<end:rclpy.spin_once(node,timeout_sec=.03)
    assert predicate(),'Timed out'


def exercise(label,speed,distance,angle=0):
    first=len(outputs);start=node.get_clock().now().nanoseconds
    end=time.monotonic()+5
    while time.monotonic()<end:
        cmd=Twist();cmd.linear.x=speed;pub.publish(cmd)
        if distance is not None:
            scan=LaserScan();scan.header.frame_id='base_footprint';scan.header.stamp=node.get_clock().now().to_msg()
            scan.angle_min=angle-.005;scan.angle_max=angle+.005;scan.angle_increment=.005
            scan.range_min=.03;scan.range_max=12.;scan.ranges=[distance]*3;scans.publish(scan)
        next_pub=time.monotonic()+.05
        while time.monotonic()<next_pub:rclpy.spin_once(node,timeout_sec=.01)
        if node.get_clock().now().nanoseconds-start>1_300_000_000 and len(outputs)>first:break
    assert len(outputs)>first,'No guard output'
    value=outputs[-1].linear.x
    report['tests'][label]=value
    print(label,value,flush=True)
    return value


try:
    assert service.wait_for_service(timeout_sec=15),'Guard lifecycle unavailable'
    for id in (1,3):
        req=ChangeState.Request();req.transition.id=id
        future=service.call_async(req);wait(future.done,10)
        assert future.result().success,'Lifecycle transition failed'
    wait(lambda: node.get_clock().now().nanoseconds>0,5)
    assert abs(exercise('clear_fast_forward',1.5,float('inf'))-1.5)<.01
    assert abs(exercise('forward_slow_front',1.5,1.25)-.60)<.01
    assert abs(exercise('forward_stop_front',1.5,.50))<.001
    assert abs(exercise('reverse_away_from_front',-.9,.50)+.90)<.01
    assert abs(exercise('reverse_stop_rear',-.9,.50,math.pi))<.001
    assert abs(exercise('forward_away_from_rear',1.5,.50,math.pi)-1.50)<.01
    # Side point inside the padded body must block motion even when a directional
    # strip would miss it: the predictive footprint remains active.
    assert abs(exercise('padded_body_contact_stop',1.5,.14,math.pi/2))<.001
    exercise('clear_before_timeout',1.5,float('inf'))
    assert abs(exercise('stale_lidar_stop',1.5,None))<.001
    report['passed']=True
finally:
    proc.terminate()
    try:proc.wait(timeout=8)
    except subprocess.TimeoutExpired:proc.kill();proc.wait(timeout=2)
    log.close();node.destroy_node();rclpy.shutdown()
    (OUT/'directional-guard.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2),flush=True)
