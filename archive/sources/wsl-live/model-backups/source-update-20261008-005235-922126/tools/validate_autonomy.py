#!/usr/bin/env python3
"""Simulator-only integration checks; isolated guard output cannot command motors."""
import copy
import json
import math
import os
from pathlib import Path
import signal
import subprocess
import time
import yaml
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from rclpy.qos import QoSProfile, DurabilityPolicy, ReliabilityPolicy, qos_profile_sensor_data
from geometry_msgs.msg import Twist
from lifecycle_msgs.srv import ChangeState, GetState
from nav_msgs.msg import OccupancyGrid, Odometry
from nav2_msgs.action import NavigateToPose
from sensor_msgs.msg import LaserScan

ws=Path('/home/robot/vacuum_ws')
logs=ws/'validation/autonomy-20261006'
logs.mkdir(parents=True,exist_ok=True)
processes=[]
handles=[]
def start(name,args):
    log=(logs/(name+'.log')).open('w')
    handles.append(log)
    p=subprocess.Popen(args,cwd=ws,stdout=log,stderr=subprocess.STDOUT,
                       stdin=subprocess.DEVNULL,start_new_session=True)
    processes.append(p)
    return p

def cleanup():
    for p in reversed(processes):
        try:
            os.killpg(p.pid,signal.SIGINT)
            p.wait(timeout=8)
        except (ProcessLookupError,subprocess.TimeoutExpired):
            pass
        try:
            os.killpg(p.pid,signal.SIGTERM)
            p.wait(timeout=2)
        except (ProcessLookupError,subprocess.TimeoutExpired):
            pass
    for log in handles:
        log.close()

rclpy.init()
node=Node('vacuum_autonomy_validation',parameter_overrides=[rclpy.parameter.Parameter('use_sim_time',value=True)])
maps=[]
odom=[]
subscriptions=[
    node.create_subscription(OccupancyGrid,'/map',maps.append,QoSProfile(depth=1,durability=DurabilityPolicy.TRANSIENT_LOCAL,reliability=ReliabilityPolicy.RELIABLE)),
    node.create_subscription(Odometry,'/odom',odom.append,qos_profile_sensor_data)]
client=ActionClient(node,NavigateToPose,'/navigate_to_pose')
result={'date':'2026-10-06','scope':'Ubuntu vacuum simulator only','tests':{}}
def wait(predicate,seconds):
    end=time.monotonic()+seconds
    while not predicate() and time.monotonic()<end:
        rclpy.spin_once(node,timeout_sec=0.05)
    return predicate()
def goal(x,y,timeout=90):
    request=NavigateToPose.Goal()
    request.pose.header.frame_id='map'
    request.pose.header.stamp=node.get_clock().now().to_msg()
    request.pose.pose.position.x=x
    request.pose.pose.position.y=y
    request.pose.pose.orientation.w=1.0
    future=client.send_goal_async(request)
    assert wait(future.done,10),'Goal submission timed out'
    handle=future.result()
    assert handle and handle.accepted,'Goal rejected'
    future=handle.get_result_async()
    if not wait(future.done,timeout):
        cancellation=handle.cancel_goal_async()
        wait(cancellation.done,5)
        raise RuntimeError('Goal timed out and was cancelled')
    return future.result()

try:
    start('sim',['python3','tools/run_sim.py','gui:=false','rviz:=false'])
    assert wait(lambda: bool(odom),40),'Simulator odometry unavailable'
    start('mapping',['ros2','launch','vacuum_sim','mapping.launch.py'])
    assert wait(lambda: bool(maps),30),'SLAM map unavailable'
    start('navigation',['ros2','launch','vacuum_sim','navigation.launch.py',
          'params_file:='+str(ws/'src/vacuum_sim/config/vacuum_nav2.yaml')])
    assert client.wait_for_server(timeout_sec=40),'Nav2 action endpoint unavailable'
    for name in ('bt_navigator','controller_server','planner_server','collision_monitor'):
        service=node.create_client(GetState,'/'+name+'/get_state')
        assert service.wait_for_service(timeout_sec=20),name+' lifecycle unavailable'
        deadline=time.monotonic()+40
        active=False
        while time.monotonic()<deadline:
            state=service.call_async(GetState.Request())
            if wait(state.done,3) and state.result().current_state.id==3:
                active=True
                break
            end=time.monotonic()+.3
            while time.monotonic()<end:
                rclpy.spin_once(node,timeout_sec=.05)
        assert active,name+' never activated'
    outcome=goal(1.0,0.0)
    assert outcome.status==4 and outcome.result.error_code==0, str(outcome)
    result['tests']['free_space_goal']={'status':outcome.status,'error_code':outcome.result.error_code}
    before=copy.deepcopy(odom[-1].pose.pose.position)
    outcome=goal(3.15,0.0,40)
    assert outcome.status==6,'Goal beyond room wall should abort'
    end=time.monotonic()+2
    while time.monotonic()<end:
        rclpy.spin_once(node,timeout_sec=.05)
    after=odom[-1].pose.pose.position
    movement=math.hypot(after.x-before.x,after.y-before.y)
    assert movement<.10 and abs(odom[-1].twist.twist.linear.x)<.02,'Robot moved toward blocked wall goal'
    result['tests']['goal_beyond_wall']={'status':outcome.status,'movement_m':movement}

    # An isolated copy of the exact configured collision guard. Its output has no
    # connection to the robot's /cmd_vel adapter; only synthetic scans are injected.
    p=copy.deepcopy(yaml.safe_load((ws/'src/vacuum_sim/config/vacuum_nav2.yaml').read_text())['collision_monitor']['ros__parameters'])
    p.update(cmd_vel_in_topic='/autonomy_guard_test/input',cmd_vel_out_topic='/autonomy_guard_test/output',
             state_topic='/autonomy_guard_test/state',polygons=['StopZone','SlowZone'])
    p['scan']['topic']='/autonomy_guard_test/scan'
    p['StopZone']['polygon_pub_topic']='/autonomy_guard_test/stop_polygon'
    p['SlowZone']['polygon_pub_topic']='/autonomy_guard_test/slow_polygon'
    guardfile=logs/'isolated_guard.yaml'
    guardfile.write_text(yaml.safe_dump({'/autonomy_guard_test/collision_monitor':{'ros__parameters':p}}))
    start('isolated_guard',['/opt/ros/jazzy/lib/nav2_collision_monitor/collision_monitor','--ros-args',
                           '-r','__ns:=/autonomy_guard_test','--params-file',str(guardfile)])
    service=node.create_client(ChangeState,'/autonomy_guard_test/collision_monitor/change_state')
    assert service.wait_for_service(timeout_sec=15),'Guard service unavailable'
    for transition in (1,3):
        request=ChangeState.Request()
        request.transition.id=transition
        future=service.call_async(request)
        assert wait(future.done,10) and future.result().success,'Guard lifecycle transition failed'
    outputs=[]
    subscriptions.append(node.create_subscription(Twist,'/autonomy_guard_test/output',outputs.append,10))
    command=node.create_publisher(Twist,'/autonomy_guard_test/input',10)
    scans=node.create_publisher(LaserScan,'/autonomy_guard_test/scan',qos_profile_sensor_data)
    def exercise(distance,seconds=1.5):
        start_count=len(outputs)
        started=time.monotonic()
        start_sim=node.get_clock().now().nanoseconds
        end=started+(15 if distance is None else seconds)
        next_pub=0
        while time.monotonic()<end:
            if distance is None and node.get_clock().now().nanoseconds-start_sim>1_500_000_000:
                break
            if time.monotonic()>=next_pub:
                twist=Twist(); twist.linear.x=.20
                command.publish(twist)
                if distance is not None:
                    scan=LaserScan()
                    scan.header.frame_id='base_footprint'
                    scan.header.stamp=node.get_clock().now().to_msg()
                    scan.angle_min=-.01; scan.angle_max=.01; scan.angle_increment=.01
                    scan.range_min=.08; scan.range_max=12.; scan.ranges=[distance]*3
                    scans.publish(scan)
                next_pub=time.monotonic()+.05
            rclpy.spin_once(node,timeout_sec=.02)
        assert len(outputs)>start_count,'Guard published no output'
        elapsed_sim=(node.get_clock().now().nanoseconds-start_sim)*1e-9
        print('guard phase',distance,'simulation seconds',elapsed_sim,'output',outputs[-1].linear.x,flush=True)
        if distance is None:
            assert elapsed_sim>1.0,'Simulator clock did not advance enough for source-timeout test'
        return outputs[-1].linear.x
    clear=exercise(float('inf'))
    slow=exercise(.30)
    stop=exercise(.18)
    # Make the preceding valid scan clear so stopping below proves data timeout.
    exercise(float('inf'))
    stale=exercise(None,2)
    assert abs(clear-.20)<.01 and abs(slow-.08)<.01 and abs(stop)<.001 and abs(stale)<.001,(clear,slow,stop,stale)
    result['tests']['isolated_guard']={'clear_m_s':clear,'slow_m_s':slow,'stop_m_s':stop,'scan_timeout_m_s':stale}
    result['passed']=True
    print(json.dumps(result,indent=2),flush=True)
except Exception as error:
    result['passed']=False
    result['error']=str(error)
    print(json.dumps(result,indent=2),flush=True)
    raise
finally:
    (logs/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    cleanup()
    node.destroy_node()
    rclpy.shutdown()
