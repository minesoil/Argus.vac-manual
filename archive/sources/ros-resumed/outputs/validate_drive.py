"""Check camera delivery and forward/reverse movement in a running drive session."""
import json
import math
from pathlib import Path
import subprocess
import struct
import time
import zlib
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Image
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

WS = Path('/home/robot/vacuum_ws')
rclpy.init()
node = Node('vacuum_direct_drive_validation')
images = []
odom = []
timed_odom = []
commands = []
def receive_odom(message):
    odom.append(message); timed_odom.append((time.monotonic(), message))
node.create_subscription(Odometry, '/odom', receive_odom, qos_profile_sensor_data)
node.create_subscription(Twist, '/vacuum/selected_cmd_vel', commands.append, 10)
report = {'date': '2026-10-07', 'scope': 'simulator only', 'tests': {}}
bridge = None
latest_image = None


def remember_image(message):
    global latest_image
    latest_image = message
    images.append((time.monotonic(), message.header.stamp.sec + message.header.stamp.nanosec * 1e-9))


node.create_subscription(Image, '/camera/image_raw', remember_image, qos_profile_sensor_data)


def spin(seconds):
    end = time.monotonic() + seconds
    while time.monotonic() < end:
        rclpy.spin_once(node, timeout_sec=.03)


try:
    reset=subprocess.run(['gz','service','-s','/world/vacuum_room/set_pose',
                          '--reqtype','gz.msgs.Pose','--reptype','gz.msgs.Boolean','--timeout','5000',
                          '--req','name: "vacuum", position: {x: 0 y: 0 z: 0.015}, orientation: {w: 1}'],
                         capture_output=True,text=True,timeout=8)
    assert reset.returncode==0 and 'true' in reset.stdout, 'Could not reset the test pose: '+reset.stdout+reset.stderr
    # Let the renderer and WSLg viewer settle after cold-start shader creation.
    spin(12)
    assert len(images) > 100 and odom, 'Camera or odometry unavailable'
    capture = images[-180:]
    fps_sim = (len(capture)-1) / (capture[-1][1]-capture[0][1])
    fps_wall = (len(capture)-1) / (capture[-1][0]-capture[0][0])
    report['tests']['camera'] = {'target_fps': 60, 'simulation_fps': fps_sim, 'wall_fps': fps_wall, 'frames': len(capture)}
    assert 57 <= fps_sim <= 63, f'Camera simulation frequency was {fps_sim}'
    assert fps_wall >= 55, f'Camera delivery too slow: {fps_wall}'
    log = (WS / '.lab/drive-validation-bridge.log').open('w')
    bridge = subprocess.Popen(['python3', 'tools/controller_bridge.py'], cwd=WS, text=True,
                              stdin=subprocess.PIPE, stdout=log, stderr=subprocess.STDOUT)

    def exercise(speed, held, seconds):
        end = time.monotonic() + seconds
        while time.monotonic() < end:
            assert bridge.poll() is None, 'Input bridge exited'
            bridge.stdin.write(json.dumps({'v': speed, 'w': 0., 'enabled': held}) + '\n')
            bridge.stdin.flush()
            # Drain camera/odom/command callbacks faster than their combined
            # arrival rate so test-side queues do not inflate response times.
            for _ in range(10):
                rclpy.spin_once(node, timeout_sec=0.)
            time.sleep(.01)

    exercise(0., False, 4)
    for label, speed, seconds in (('forward', 1.50, 2), ('reverse', -.90, 3)):
        before = odom[-1].pose.pose
        q = before.orientation
        yaw = math.atan2(2*(q.w*q.z + q.x*q.y), 1-2*(q.y*q.y+q.z*q.z))
        first = len(odom)
        issued=time.monotonic()
        exercise(speed, True, seconds)
        after = odom[-1].pose.pose.position
        displacement = (after.x-before.position.x)*math.cos(yaw) + (after.y-before.position.y)*math.sin(yaw)
        assert displacement * (1 if speed > 0 else -1) > .06, f'{label} did not move as expected: {displacement}'
        velocities = [m.twist.twist.linear.x for m in odom[first:]]
        actual_speed = max(velocities) if speed > 0 else min(velocities)
        assert abs(actual_speed) >= abs(speed)*.85, f'{label} speed clipped: {actual_speed}'
        after_command=[(t,m) for t,m in timed_odom if t>=issued]
        reaction=next(t-issued for t,m in after_command if abs(m.twist.twist.linear.x)>=abs(speed)*.10)
        rise=next(t-issued for t,m in after_command if abs(m.twist.twist.linear.x)>=abs(speed)*.90)
        assert reaction < .25, f'{label} response delayed: {reaction}'
        assert rise < .50, f'{label} rise too slow: {rise}'
        report['tests'][label] = {'signed_displacement_m': displacement, 'peak_odometry_m_s': actual_speed,
                                  'first_10_percent_wall_s':reaction,'time_to_90_percent_wall_s':rise}
        neutral_at=time.monotonic()
        exercise(0., True, 1)
        stopping=next(t-neutral_at for t,m in timed_odom if t>=neutral_at and abs(m.twist.twist.linear.x)<.02)
        assert stopping < .5, f'Neutral stop too slow: {stopping}'
        report['tests'][label]['neutral_stop_wall_s']=stopping
        assert abs(commands[-1].linear.x) < .001 and abs(odom[-1].twist.twist.linear.x) < .02
    report['tests']['neutral_stop_without_hold_button'] = True
    report['tests']['disarmed_stop'] = True
    exercise(0., False, .5)
    # A pure turn tests the smaller wheels and higher yaw command without a
    # translational goal or a held-button input.
    turn_start=time.monotonic()
    while time.monotonic()-turn_start<1.0:
        bridge.stdin.write(json.dumps({'v':0.,'w':2.4,'enabled':True})+'\n');bridge.stdin.flush()
        for _ in range(10):rclpy.spin_once(node,timeout_sec=0.)
        time.sleep(.01)
    turn_records=[(t,m) for t,m in timed_odom if t>=turn_start]
    peak=max(abs(m.twist.twist.angular.z) for t,m in turn_records)
    assert peak>2.0, f'Turn speed clipped: {peak}'
    turn_rise=next(t-turn_start for t,m in turn_records if abs(m.twist.twist.angular.z)>=2.16)
    assert turn_rise<.5, f'Turn rise too slow: {turn_rise}'
    report['tests']['steering']={'peak_rad_s':peak,'time_to_90_percent_wall_s':turn_rise}
    exercise(0.,False,1)
    exercise(.2, True, 1)
    spin(2)
    assert abs(commands[-1].linear.x) < .001 and abs(odom[-1].twist.twist.linear.x) < .02
    report['tests']['input_timeout_stop'] = True
    message = latest_image
    assert message.encoding in ('rgb8','bgr8'), message.encoding
    rows = []
    data = bytes(message.data)
    for y in range(message.height):
        row = data[y*message.step:y*message.step+message.width*3]
        if message.encoding == 'bgr8':
            row = bytes(v for i in range(0,len(row),3) for v in (row[i+2],row[i+1],row[i]))
        rows.append(b'\0'+row)
    def chunk(kind, content):
        return struct.pack('>I',len(content))+kind+content+struct.pack('>I',zlib.crc32(kind+content))
    png = b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',message.width,message.height,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(b''.join(rows)))+chunk(b'IEND',b'')
    (WS/'validation/furnished-robot-camera.png').write_bytes(png)
    report['passed'] = True
except Exception as exc:
    report['passed'] = False
    report['error'] = str(exc)
    raise
finally:
    if bridge:
        try:
            bridge.stdin.close()
            bridge.wait(timeout=5)
        except Exception:
            bridge.terminate()
    path = WS / 'validation/modern-drive-20261007'
    path.mkdir(parents=True, exist_ok=True)
    (path / 'results.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2), flush=True)
    node.destroy_node()
    rclpy.shutdown()
