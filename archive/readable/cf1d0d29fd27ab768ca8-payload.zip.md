# payload.zip

Historical source: ros-resumed


## activate_guard.py

"""Activate the standalone simulator collision guard for direct driving."""
import os
import time
import rclpy
from rclpy.node import Node
from lifecycle_msgs.srv import GetState, ChangeState


def main():
    rclpy.init()
    node = Node(f'vacuum_guard_start_{os.getpid()}')
    get = node.create_client(GetState, '/collision_monitor/get_state')
    change = node.create_client(ChangeState, '/collision_monitor/change_state')

    def result(future):
        deadline = time.monotonic() + 15
        while not future.done() and time.monotonic() < deadline:
            rclpy.spin_once(node, timeout_sec=.05)
        if not future.done():
            raise RuntimeError('Collision guard lifecycle request timed out.')
        return future.result()

    try:
        if not get.wait_for_service(timeout_sec=20) or not change.wait_for_service(timeout_sec=20):
            raise RuntimeError('Collision guard is not available.')
        state = result(get.call_async(GetState.Request())).current_state.id
        for expected, transition in ((1, 1), (2, 3)):
            if state == expected:
                request = ChangeState.Request()
                request.transition.id = transition
                if not result(change.call_async(request)).success:
                    raise RuntimeError('Collision guard could not be activated.')
                state = result(get.call_async(GetState.Request())).current_state.id
        if state != 3:
            raise RuntimeError(f'Collision guard is in state {state}, not active.')
        print('Collision guard active.', flush=True)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()


## apply_robot_profile.py

"""Apply the user's simulator geometry and response profile with rollback."""
from datetime import datetime
import hashlib
import json
import re
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET
import yaml

WS = Path('/home/robot/vacuum_ws')
PACKAGE = WS / 'src/vacuum_sim'
XACRO = 'http://www.ros.org/wiki/xacro'
ET.register_namespace('xacro', XACRO)


def apply_profile():
    source = WS / 'tools/robot-profile.json'
    profile = json.loads(source.read_text())
    fingerprint = hashlib.sha256(source.read_bytes()+Path(__file__).read_bytes()).hexdigest()
    marker = WS / '.lab/hardware-profile-v2'
    if marker.exists() and marker.read_text().splitlines()[0] == fingerprint:
        return
    hardware, drive = profile['hardware'], profile['drive']
    radius = hardware['wheel_diameter_m'] / 2
    model = PACKAGE / 'urdf/vacuum.urdf.xacro'
    root = ET.fromstring(model.read_text())
    properties = {item.get('name'): item for item in root.findall(f'{{{XACRO}}}property')}
    for name, value in {'wheel_radius': radius, 'wheel_separation': hardware['wheel_separation_m'],
                        'body_z': .08, 'body_mass': 3.0}.items():
        properties[name].set('value', str(value))
    root.find("joint[@name='base_joint']/origin").set('xyz', '-0.03 0 0.116')
    wheel_macro = root.find(f'{{{XACRO}}}macro[@name="wheel"]')
    wheel_macro.find('joint/origin').set('xyz', '0.03 ${sign*wheel_separation/2} ${wheel_radius-0.116}')
    wheel_macro.find('joint/limit').set('velocity', '70.0')
    root.find("joint[@name='caster_joint']/origin").set('xyz', '-0.105 0 -0.096')
    body = root.find("link[@name='base_link']")
    for visual in list(body.findall('visual')):
        body.remove(visual)
    for name, rgba in {'acrylic': '.17 .70 .77 .55', 'rubber': '.055 .065 .075 1',
                       'sensor': '.08 .10 .14 1', 'aluminium': '.62 .68 .75 1',
                       'pcb': '.06 .42 .25 1', 'pcb_blue': '.06 .25 .52 1',
                       'copper': '.95 .58 .18 1', 'terminal': '.15 .61 .29 1'}.items():
        material = root.find(f"material[@name='{name}']")
        if material is None:
            material = ET.SubElement(root, 'material', name=name)
            ET.SubElement(material, 'color')
        material.find('color').set('rgba', rgba)

    def visual(link, name, position, shape, dimensions, material, rpy=None):
        item = ET.SubElement(link, 'visual', name=name)
        origin = ET.SubElement(item, 'origin', xyz=' '.join(map(str, position)))
        if rpy:
            origin.set('rpy', rpy)
        geometry = ET.SubElement(item, 'geometry')
        if shape == 'box':
            ET.SubElement(geometry, 'box', size=' '.join(map(str, dimensions)))
        else:
            ET.SubElement(geometry, 'cylinder', radius=str(dimensions[0]), length=str(dimensions[1]))
        ET.SubElement(item, 'material', name=material)

    for name, height in [('lower_acrylic_chassis', -.038), ('upper_acrylic_chassis', .038)]:
        visual(body, name, (0, 0, height), 'cylinder', (.15, .004), 'acrylic')
    for x in (-.08, .08):
        for y in (-.075, .075):
            visual(body, f'standoff_{x}_{y}', (x, y, 0), 'cylinder', (.004, .072), 'aluminium')

    # Fixed components remain explicit ROS links; main chassis envelope provides
    # collision volume for the electronics. Mass and module details are estimates.
    names = ('left_nema17', 'right_nema17', 'left_tb6600', 'right_tb6600', 'arduino_mega', 'orange_pi5')
    for child in list(root):
        if child.tag in ('joint', 'link') and child.get('name', '').replace('_mount', '') in names:
            root.remove(child)

    def component(name, position, dimensions, material, mass):
        joint = ET.SubElement(root, 'joint', name=name+'_mount', type='fixed')
        ET.SubElement(joint, 'parent', link='base_link'); ET.SubElement(joint, 'child', link=name)
        ET.SubElement(joint, 'origin', xyz=' '.join(map(str, position)))
        link = ET.SubElement(root, 'link', name=name)
        inertial = ET.SubElement(link, 'inertial'); ET.SubElement(inertial, 'mass', value=str(mass))
        x,y,z = dimensions
        ET.SubElement(inertial, 'inertia', ixx=str(mass*(y*y+z*z)/12),
                      iyy=str(mass*(x*x+z*z)/12), izz=str(mass*(x*x+y*y)/12), ixy='0', ixz='0', iyz='0')
        visual(link, name+'_body', (0,0,0), 'box', dimensions, material)
        return link

    for side, sign in [('left', 1), ('right', -1)]:
        motor = component(side+'_nema17', (.03, sign*.071, -.081), (.0423,.040,.0423), 'sensor', .25)
        for y in (-.016,.016):
            visual(motor, 'endplate_'+str(y), (0,y,0), 'box', (.0423,.008,.0423), 'aluminium')
        visual(motor, 'shaft_and_hub', (0,sign*.031,0), 'cylinder', (.004,.023), 'aluminium', '${pi/2} 0 0')
        visual(motor, 'under_chassis_mount', (0,0,.030), 'box', (.043,.042,.018), 'aluminium')
        driver = component(side+'_tb6600', (.078,sign*.044,-.021), (.077,.038,.026), 'sensor', .10)
        for x in (-.025,-.015,-.005,.005,.015,.025):
            visual(driver,'cooling_fin_'+str(x),(x,0,.016),'box',(.003,.038,.009),'aluminium')
        visual(driver, 'screw_terminals', (0,-sign*.022,0), 'box', (.065,.010,.018), 'terminal')
    mega = component('arduino_mega', (-.044,.056,-.027), (.10152,.0533,.003), 'pcb_blue', .037)
    visual(mega,'mega_processor',(-.009,0,.004),'box',(.014,.014,.005),'sensor')
    for y in (-.023,.023): visual(mega,'mega_pin_headers_'+str(y),(0,y,.005),'box',(.079,.004,.007),'sensor')
    visual(mega,'mega_usb',(-.046,0,.007),'box',(.015,.013,.012),'aluminium')
    orange = component('orange_pi5',(-.044,-.054,-.027),(.100,.062,.003),'pcb',.046)
    visual(orange,'rk3588s_heatsink',(0,0,.009),'box',(.025,.025,.016),'aluminium')
    for x in (-.01,-.005,0,.005,.01): visual(orange,'heatsink_fin_'+str(x),(x,0,.019),'box',(.002,.025,.006),'sensor')
    visual(orange,'ethernet_port',(-.04,0,.007),'box',(.019,.016,.014),'aluminium')
    visual(orange,'gpio_header',(.009,.026,.006),'box',(.05,.005,.009),'sensor')
    lidar = root.find("link[@name='lidar_link']")
    for item in list(lidar.findall('visual')): lidar.remove(item)
    visual(lidar,'rplidar_mount_standoff',(0,0,-.030),'cylinder',(.010,.032),'aluminium')
    visual(lidar,'rplidar_c1_base',(0,0,-.009),'box',(.054,.054,.012),'sensor')
    visual(lidar,'rplidar_c1_scanner',(0,0,.005),'cylinder',(.027,.025),'sensor')
    visual(lidar,'rplidar_c1_accent',(0,0,.015),'cylinder',(.025,.004),'copper')
    sensor = root.find("gazebo[@reference='lidar_link']/sensor")
    sensor.find('update_rate').text=str(profile['lidar']['scan_hz'])
    sensor.find('lidar/scan/horizontal/samples').text=str(profile['lidar']['samples'])
    sensor.find('lidar/range/min').text=str(profile['lidar']['min_range_m'])
    sensor.find('lidar/range/max').text=str(profile['lidar']['max_range_m'])
    sensor.find('lidar/noise/stddev').text='0.015'
    ET.indent(root, space='  ')
    updates = {model: ET.tostring(root, encoding='unicode')+'\n',
               PACKAGE/'config/robot-profile.json': json.dumps(profile,indent=2)+'\n'}
    controller = PACKAGE/'config/controllers.yaml'
    data=yaml.safe_load(controller.read_text()); p=data['diff_drive_controller']['ros__parameters']
    p.update(wheel_radius=radius, wheel_separation=hardware['wheel_separation_m'],
             publish_rate=60.0, cmd_vel_timeout=.25, velocity_rolling_window_size=drive['odometry_window_samples'])
    data['controller_manager']['ros__parameters']['update_rate']=60
    p.update({'linear.x.max_velocity':drive['forward_m_s'], 'linear.x.min_velocity':-drive['reverse_m_s'],
              'linear.x.max_acceleration':drive['acceleration_m_s2'], 'linear.x.min_acceleration':-drive['acceleration_m_s2'],
              'linear.x.has_jerk_limits':False, 'angular.z.max_velocity':drive['turn_rad_s'],
              'angular.z.min_velocity':-drive['turn_rad_s'], 'angular.z.max_acceleration':drive['angular_acceleration_rad_s2'],
              'angular.z.min_acceleration':-drive['angular_acceleration_rad_s2'], 'angular.z.has_jerk_limits':False})
    updates[controller]=yaml.safe_dump(data,sort_keys=False)
    adapter=PACKAGE/'scripts/twist_adapter.py'
    adapter_text=adapter.read_text().replace('enforces its 0.5 s timeout','enforces its 0.25 s timeout')
    adapter_text=re.sub(r'outgoing.twist.linear.x = .+',
                        f"outgoing.twist.linear.x = max(-{drive['reverse_m_s']}, min({drive['forward_m_s']}, message.linear.x))",adapter_text)
    adapter_text=re.sub(r'outgoing.twist.angular.z = .+',
                        f"outgoing.twist.angular.z = max(-{drive['turn_rad_s']}, min({drive['turn_rad_s']}, message.angular.z))",adapter_text)
    adapter_text=adapter_text.replace("'/diff_drive_controller/cmd_vel', 10", "'/diff_drive_controller/cmd_vel', 1")
    adapter_text=adapter_text.replace("'/cmd_vel', self.on_twist, 10", "'/cmd_vel', self.on_twist, 1")
    updates[adapter]=adapter_text
    for name in ('nav2.yaml','vacuum_nav2.yaml'):
        path=PACKAGE/'config'/name; data=yaml.safe_load(path.read_text()); guard=data['collision_monitor']['ros__parameters']
        for zone,front,rear,width in [('StopZone',.62,-.60,.20),('SlowZone',1.7,-1.2,.25)]:
            if zone not in guard:
                continue
            p=guard[zone]
            p['forward']['points']=str([[-.03,width],[-.03,-width],[front,-width],[front,width]])
            p['reverse']['points']=str([[rear,width],[rear,-width],[-.03,-width],[-.03,width]])
            for polygon in p['velocity_polygons']:
                item=p[polygon]
                item['linear_max']=2.0 if polygon!='reverse' else -.001
                item['linear_min']=-2.0 if polygon!='forward' else .001
                item['theta_min']=-3.;item['theta_max']=3.
        if 'FootprintApproach' in guard:
            guard['FootprintApproach']['time_before_collision']=.55
            guard['FootprintApproach']['simulation_time_step']=.02
        updates[path]=yaml.safe_dump(data,sort_keys=False)
    backup=WS/'model-backups'/datetime.now().strftime('hardware-v2-%Y%m%d-%H%M%S-%f')
    backup.mkdir(parents=True)
    originals={path:path.read_bytes() if path.exists() else None for path in updates}
    for path,content in originals.items():
        if content is not None:
            saved=backup/path.relative_to(PACKAGE);saved.parent.mkdir(parents=True,exist_ok=True);saved.write_bytes(content)
    try:
        for path,value in updates.items(): path.write_text(value)
        result=subprocess.run(['/bin/bash','-lc','source env.sh; colcon build --symlink-install --packages-select vacuum_sim'],cwd=WS,text=True,capture_output=True,timeout=180)
        if result.returncode: raise RuntimeError(result.stdout+result.stderr)
        marker.write_text(fingerprint+'\n'+str(backup)+'\n')
    except BaseException:
        for path,value in originals.items():
            if value is None:path.unlink(missing_ok=True)
            else:path.write_bytes(value)
        raise
    print('Hardware profile applied: 70 mm wheels, under-chassis NEMA 17s, 1.5 m/s simulator drive.',flush=True)


if __name__ == '__main__': apply_profile()


## backup-verification.json

{

  "Completed": true,

  "Path": "F:\\VacuumRobotBackups\\VacuumRobot-24.04-verified-20260930-222815.tar",

  "Bytes": 7263426560,

  "SHA256": "8c815e22403a6d8838acebe70ae7041076b0c1e5b994ac890060c74052758e8b",

  "ArchiveStructureVerified": true,

  "RestoreBootTested": false,

  "Finished": "2026-09-30T22:32:12.1319441+08:00"

}



## build_furnished_room.py

"""Build original, local room assets. Standard library only; no model downloads.



Meshes are batched by furniture item/material; physics uses simple proxies.

All dimensions are metres. Generated assets live inside the simulator package.

"""

from collections import defaultdict

import math

from pathlib import Path

import random

import struct

import xml.etree.ElementTree as ET

import zlib



PACKAGE = Path('/home/robot/vacuum_ws/src/vacuum_sim')

ASSETS = PACKAGE / 'worlds/furnished'

ASSETS.mkdir(parents=True, exist_ok=True)

DAE = 'http://www.collada.org/2005/11/COLLADASchema'





def png(name, size, pixel):

    width, height = size

    raw = bytearray()

    for y in range(height):

        raw.append(0)

        for x in range(width):

            raw.extend(max(0, min(255, int(v))) for v in pixel(x, y))

    def chunk(kind, data):

        return struct.pack('>I', len(data)) + kind + data + struct.pack('>I', zlib.crc32(kind + data))

    (ASSETS / name).write_bytes(b'\x89PNG\r\n\x1a\n' +

        chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)) +

        chunk(b'IDAT', zlib.compress(bytes(raw), 7)) + chunk(b'IEND', b''))





def oak(x, y):

    plank = y // 48

    seam = y % 48 == 0 or (x + (plank % 3)*128) % 384 == 0

    if seam:

        return (132, 101, 68)

    grain = 5*math.sin(y*.65 + math.sin(x*.004)*4) + 2*math.sin(y*2+x*.015)

    shade = ((plank*17) % 13)-6 + grain + 2*math.sin(x*.03)

    return (181+shade, 139+shade, 94+shade*.7)





def fabric(x, y):

    grain = (x % 3 == 0)*7 - (y % 3 == 0)*5 + 2*math.sin(x*1.7+y*.8)

    return (184+grain, 169+grain, 145+grain)





def rug(x, y):

    edge = min(x, y, 511-x, 511-y)

    grain = ((x*7+y*13) % 11)-5

    stripe = edge < 12 or (22 < edge < 26) or (abs(x-256)+abs(y-256)) % 96 < 3

    return tuple(v+grain for v in ((65, 83, 86) if stripe else (201, 187, 157)))





def artwork(x, y):

    # An original abstract landscape, also used on the TV display.

    if (x-368)**2+(y-94)**2 < 37**2:

        return (239, 172, 102)

    if y > 194 + 31*math.sin(x*.009):

        return (42, 78, 83)

    if y > 150 + 38*math.sin(x*.011+1.4):

        return (71, 107, 112)

    return (174-y*.12, 199-y*.09, 204-y*.06)





def garden(x,y):

    if y > 275 + 22*math.sin(x*.009):return (102,126,73)

    if y > 244 + 18*math.sin(x*.014+.8):return (129,151,104)

    for cx,cy,r in ((80,212,90),(230,190,75),(710,200,110),(948,190,100)):

        if (x-cx)**2+(y-cy)**2<r*r:return (74+y*.09,112+y*.08,76+y*.05)

    cloud=math.exp(-((x-450)/180)**2-((y-86)/30)**2)+math.exp(-((x-750)/130)**2-((y-66)/22)**2)

    return (163+cloud*45+y*.06,196+cloud*25+y*.04,213+cloud*15)





png('oak.png', (2048, 2048), oak)

png('linen.png', (256, 256), fabric)

png('woven-rug.png', (512, 512), rug)

png('landscape.png', (512, 256), artwork)

png('garden.png', (1024,384), garden)



MATERIALS = {
    'aluminium': ((.62,.68,.75), None),
    'oak': ((.62, .43, .25), 'oak.png'),

    'linen': ((.73, .66, .55), 'linen.png'),

    'rug': ((.76, .71, .61), 'woven-rug.png'),

    'art': ((.5, .65, .7), 'landscape.png'),

    'garden': ((.7,.8,.7), 'garden.png'),

    'plaster': ((.86, .85, .80), None),

    'sage': ((.30, .42, .36), None),

    'white': ((.92, .90, .85), None),

    'teal': ((.16, .32, .34), None),

    'terra': ((.62, .27, .15), None),

    'brass': ((.63, .48, .24), None),

    'charcoal': ((.035, .045, .05), None),

    'ceramic': ((.77, .81, .77), None),

    'leaf': ((.10, .29, .11), None),

    'leaf_light': ((.22, .40, .16), None),

    'blue': ((.22, .35, .48), None),

    'burgundy': ((.40, .13, .17), None),

}





def rotate(point, yaw):

    x, y, z = point

    return (x*math.cos(yaw)-y*math.sin(yaw), x*math.sin(yaw)+y*math.cos(yaw), z)





class Mesh:

    def __init__(self):

        self.faces = defaultdict(list)



    def triangle(self, material, points, uvs=None, normals=None):

        if uvs is None:

            uvs = [(p[0]*2, p[1]*2+p[2]*2) for p in points]

        a, b, c = points

        u = tuple(b[i]-a[i] for i in range(3)); v = tuple(c[i]-a[i] for i in range(3))

        n = (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0])

        length = math.sqrt(sum(t*t for t in n))

        if length < 1e-10:

            return

        normal = tuple(t/length for t in n)

        self.faces[material].append((points, normals or [normal]*3, uvs))



    def quad(self, material, points, uvs=None, normals=None):

        if uvs is None:

            uvs = [(p[0]*2, p[1]*2+p[2]*2) for p in points]

        for indices in ((0, 1, 2), (0, 2, 3)):

            self.triangle(material, [points[i] for i in indices], [uvs[i] for i in indices],

                          [normals[i] for i in indices] if normals else None)



    def box(self, center, size, material, yaw=0, floor_uv=False):

        points = []

        for x, y, z in ((-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),

                        (-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)):

            q = rotate((x*size[0]/2, y*size[1]/2, z*size[2]/2), yaw)

            points.append(tuple(q[i]+center[i] for i in range(3)))

        for face in ((0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)):

            p = [points[i] for i in face]

            uv = [((q[0]+8)/16,(q[1]+6)/12) for q in p] if floor_uv else None

            self.quad(material, p, uv)



    def rounded(self, center, size, radius, material, yaw=0):

        """Bevelled upholstered/wood parts: four rounded corners, curved edges."""

        sx, sy, sz = size

        radius = min(radius, sx/3, sy/3, sz/3)

        rings = []; normal_rings=[]

        for zsign, tilt in ((-1,-math.pi/2),(-1,-math.pi/3),(-1,-math.pi/6),(-1,0),

                            (1,0),(1,math.pi/6),(1,math.pi/3),(1,math.pi/2)):

            z=zsign*(sz/2-radius)+radius*math.sin(tilt)

            ring = []; normal_ring=[]

            for cx, cy, start in ((1,1,0),(-1,1,90),(-1,-1,180),(1,-1,270)):

                for j in range(5):

                    angle = math.radians(start+j*90/4)

                    r = max(.0001, radius*math.cos(tilt))

                    q = rotate((cx*(sx/2-radius)+r*math.cos(angle),

                                cy*(sy/2-radius)+r*math.sin(angle), z), yaw)

                    ring.append(tuple(q[i]+center[i] for i in range(3)))

                    normal_ring.append(rotate((math.cos(angle)*math.cos(tilt),math.sin(angle)*math.cos(tilt),math.sin(tilt)),yaw))

            rings.append(ring)

            normal_rings.append(normal_ring)

        count = len(rings[0])

        for layer,(lower, upper) in enumerate(zip(rings, rings[1:])):

            for j in range(count):

                k = (j+1) % count

                self.quad(material, [lower[j],lower[k],upper[k],upper[j]],

                          normals=[normal_rings[layer][j],normal_rings[layer][k],normal_rings[layer+1][k],normal_rings[layer+1][j]])

        for j in range(1,count-1):

            self.triangle(material, [rings[0][0],rings[0][j+1],rings[0][j]])

            self.triangle(material, [rings[-1][0],rings[-1][j],rings[-1][j+1]])



    def lathe(self, center, profile, material, segments=24):

        rings = [[(center[0]+r*math.cos(i*2*math.pi/segments),

                   center[1]+r*math.sin(i*2*math.pi/segments),center[2]+z)

                  for i in range(segments)] for r,z in profile]

        for lower,upper in zip(rings,rings[1:]):

            for i in range(segments):

                j=(i+1)%segments

                self.quad(material,[lower[i],lower[j],upper[j],upper[i]])

        for ring,reverse in ((rings[0],True),(rings[-1],False)):

            for i in range(1,segments-1):

                self.triangle(material,[ring[0],ring[i+1],ring[i]] if reverse else [ring[0],ring[i],ring[i+1]])



    def cylinder(self, center, radius, height, material):

        self.lathe(center,[(radius,-height/2),(radius,height/2)],material)



    def leaf(self, center, length, width, yaw, material):

        coords=[(0,0,0),(-width,length*.35,length*.22),(0,length*.5,length*.45),

                (width,length*.35,length*.22),(0,length*.85,length*.45)]

        p=[tuple(rotate(q,yaw)[i]+center[i] for i in range(3)) for q in coords]

        for face in ((0,1,2),(0,2,3),(1,4,2),(2,4,3)):

            self.triangle(material,[p[i] for i in face])

            self.triangle(material,[p[i] for i in reversed(face)])



    def save(self, name):

        root=ET.Element('COLLADA', xmlns=DAE, version='1.4.1')

        asset=ET.SubElement(root,'asset')

        ET.SubElement(asset,'unit',name='meter',meter='1')

        ET.SubElement(asset,'up_axis').text='Z_UP'

        images=ET.SubElement(root,'library_images'); effects=ET.SubElement(root,'library_effects')

        mats=ET.SubElement(root,'library_materials'); geometries=ET.SubElement(root,'library_geometries')

        scenes=ET.SubElement(root,'library_visual_scenes'); scene=ET.SubElement(scenes,'visual_scene',id='Scene',name='Scene')

        for mat,faces in self.faces.items():

            color,texture=MATERIALS[mat]

            effect=ET.SubElement(effects,'effect',id=mat+'fx'); profile=ET.SubElement(effect,'profile_COMMON')

            if texture:

                im=ET.SubElement(images,'image',id=mat+'image');ET.SubElement(im,'init_from').text=texture

                par=ET.SubElement(profile,'newparam',sid=mat+'surface'); surf=ET.SubElement(par,'surface',type='2D');ET.SubElement(surf,'init_from').text=mat+'image'

                par=ET.SubElement(profile,'newparam',sid=mat+'sampler');sample=ET.SubElement(par,'sampler2D');ET.SubElement(sample,'source').text=mat+'surface'

            phong=ET.SubElement(ET.SubElement(profile,'technique',sid='common'),'phong')

            ET.SubElement(ET.SubElement(phong,'ambient'),'color').text=' '.join(str(v*.7) for v in color)+' 1'

            diffuse=ET.SubElement(phong,'diffuse')

            if texture:ET.SubElement(diffuse,'texture',texture=mat+'sampler',texcoord='UVSET0')

            else:ET.SubElement(diffuse,'color').text=' '.join(map(str,color))+' 1'

            spec=.22 if mat=='brass' else .03

            ET.SubElement(ET.SubElement(phong,'specular'),'color').text=f'{spec} {spec} {spec} 1'

            ET.SubElement(ET.SubElement(phong,'shininess'),'float').text='20'

            material=ET.SubElement(mats,'material',id=mat,name=mat);ET.SubElement(material,'instance_effect',url='#'+mat+'fx')

            mesh=ET.SubElement(ET.SubElement(geometries,'geometry',id=mat+'mesh',name=mat),'mesh')

            positions=[];normals=[];uv=[]

            for points,ns,tex in faces:

                for p,t,n in zip(points,tex,ns): positions.extend(p);normals.extend(n);uv.extend(t)

            def source(sid,values,stride,params):

                src=ET.SubElement(mesh,'source',id=sid)

                ET.SubElement(src,'float_array',id=sid+'array',count=str(len(values))).text=' '.join(f'{v:.6f}' for v in values)

                accessor=ET.SubElement(ET.SubElement(src,'technique_common'),'accessor',source='#'+sid+'array',count=str(len(values)//stride),stride=str(stride))

                for param in params:ET.SubElement(accessor,'param',name=param,type='float')

            source(mat+'pos',positions,3,('X','Y','Z'));source(mat+'norm',normals,3,('X','Y','Z'));source(mat+'uv',uv,2,('S','T'))

            vertices=ET.SubElement(mesh,'vertices',id=mat+'verts');ET.SubElement(vertices,'input',semantic='POSITION',source='#'+mat+'pos')

            triangles=ET.SubElement(mesh,'triangles',material=mat,count=str(len(faces)))

            for semantic,src,offset in [('VERTEX',mat+'verts',0),('NORMAL',mat+'norm',1),('TEXCOORD',mat+'uv',2)]:

                ET.SubElement(triangles,'input',semantic=semantic,source='#'+src,offset=str(offset),**({'set':'0'} if offset==2 else {}))

            ET.SubElement(triangles,'p').text=' '.join(f'{i} {i} {i}' for i in range(len(positions)//3))

            node=ET.SubElement(scene,'node',id=mat+'node',name=mat,type='NODE')

            inst=ET.SubElement(node,'instance_geometry',url='#'+mat+'mesh')

            bind=ET.SubElement(ET.SubElement(inst,'bind_material'),'technique_common')

            im=ET.SubElement(bind,'instance_material',symbol=mat,target='#'+mat)

            ET.SubElement(im,'bind_vertex_input',semantic='UVSET0',input_semantic='TEXCOORD',input_set='0')

        ET.SubElement(ET.SubElement(root,'scene'),'instance_visual_scene',url='#Scene')

        path=ASSETS/(name+'.dae'); ET.ElementTree(root).write(path,encoding='utf-8',xml_declaration=True)

        return path





room_mesh = Mesh()

root=ET.Element('sdf',version='1.9');world=ET.SubElement(root,'world',name='vacuum_room')

def element(parent,tag,value):ET.SubElement(parent,tag).text=str(value)

physics=ET.SubElement(world,'physics',name='physics',type='ignored')

element(physics,'max_step_size','0.005555555555555556');element(physics,'real_time_factor',1.)

element(world,'gravity','0 0 -9.81')

for filename,classname in [('physics','Physics'),('user-commands','UserCommands'),('scene-broadcaster','SceneBroadcaster'),('sensors','Sensors')]:

    plugin=ET.SubElement(world,'plugin',filename='gz-sim-'+filename+'-system',name='gz::sim::systems::'+classname)

    if classname=='Sensors':element(plugin,'render_engine','ogre2')

scene=ET.SubElement(world,'scene');element(scene,'ambient','.7 .7 .7 1');element(scene,'background','.69 .79 .85 1');element(scene,'shadows','false')

light=ET.SubElement(world,'light',name='afternoon_daylight',type='directional')

element(light,'pose','0 0 6 0 0 0');element(light,'diffuse','.75 .72 .65 1');element(light,'specular','.15 .15 .15 1');element(light,'direction','-.5 -.4 -1');element(light,'cast_shadows','false')

light=ET.SubElement(world,'light',name='soft_window_fill',type='directional')

element(light,'pose','0 0 6 0 0 0');element(light,'diffuse','.25 .28 .3 1');element(light,'specular','0 0 0 1');element(light,'direction','.4 .4 -1');element(light,'cast_shadows','false')

gui=ET.SubElement(world,'gui',fullscreen='false')

# Main Gazebo window opens with a useful architectural view.

camera=ET.SubElement(gui,'camera',name='user_camera');element(camera,'pose','13 -16 13 0 .62 2.2')

room_model=ET.SubElement(world,'model',name='furnished_living_room');element(room_model,'static','true')

element(room_model,'self_collide','false')

room_link=ET.SubElement(room_model,'link',name='room')





class Item:

    def __init__(self,name,pose=(0,0,0,0)):

        self.name=name;self.mesh=Mesh();self.collisions=[];self.pose=pose

    def box(self,center,size,material,yaw=0,collision=False,rounded=0):

        if rounded:self.mesh.rounded(center,size,rounded,material,yaw)

        else:self.mesh.box(center,size,material,yaw)

        if collision:self.collisions.append(('box',center,size,yaw))

    def cylinder(self,center,radius,height,material,collision=False):

        self.mesh.cylinder(center,radius,height,material)

        if collision:self.collisions.append(('cylinder',center,(radius,height),0))

    def save(self):

        if self.name == 'architecture':

            # Enlarge only architecture, preserving human-scale furniture.

            for material, faces in self.mesh.faces.items():

                self.mesh.faces[material] = [([(p[0]*2, p[1]*12/7, p[2]) for p in points], normals, uvs)

                                            for points,normals,uvs in faces]

            self.collisions = [(kind,(c[0]*2,c[1]*12/7,c[2]),

                                (s[0]*2,s[1]*12/7,s[2]) if kind=='box' else s,yaw)

                               for kind,c,s,yaw in self.collisions]

        # One shared visual mesh gives the renderer one draw batch per material,

        # rather than repeating material/draw setup for each piece of furniture.

        x,y,z,yaw=self.pose

        for material,faces in self.mesh.faces.items():

            for points,normals,uvs in faces:

                transformed=[]

                for point in points:

                    q=rotate(point,yaw);transformed.append((q[0]+x,q[1]+y,q[2]+z))

                room_mesh.faces[material].append((transformed,[rotate(n,yaw) for n in normals],uvs))

        # All fixed furnishings are shapes of one immobile body. This prevents

        # expensive contact checks between the floor and static furniture.

        for i,(kind,center,size,local_yaw) in enumerate(self.collisions):

            q=rotate(center,yaw);center=(q[0]+x,q[1]+y,q[2]+z)

            collision=ET.SubElement(room_link,'collision',name=self.name+'_proxy'+str(i));element(collision,'pose',' '.join(map(str,center))+f' 0 0 {yaw+local_yaw}')

            shape=ET.SubElement(ET.SubElement(collision,'geometry'),kind)

            if kind=='box':element(shape,'size',' '.join(map(str,size)))

            else:element(shape,'radius',size[0]);element(shape,'length',size[1])





house=Item('architecture')

house.mesh.box((0,0,-.04),(8.2,7.2,.08),'oak',floor_uv=True)

house.collisions.append(('box',(0,0,-.04),(8.2,7.2,.08),0))

# North wall has a real window opening. Collision proxies match the wall pieces.

for center,size in [((0,-3.5,1.4),(8.2,.12,2.8)),((-4,0,1.4),(.12,7,2.8)),((4,0,1.4),(.12,7,2.8)),

                    ((0,3.5,.45),(8.2,.12,.9)),((0,3.5,2.65),(8.2,.12,.3)),

                    ((-3.15,3.5,1.7),(1.9,.12,1.6)),((3.15,3.5,1.7),(1.9,.12,1.6))]:

    house.box(center,size,'sage' if center[0]==4 else 'plaster',collision=True)

for x in (-4,4):house.box((x*.985,0,.055),(.035,6.95,.11),'white')

for y in (-3.5,3.5):house.box((0,y*.985,.055),(7.95,.035,.11),'white')

for x in (-2.19,0,2.19):house.box((x,3.48,1.7),(.055,.15,1.6),'white')

for z in (.9,1.7,2.5):house.box((0,3.48,z),(4.45,.16,.055),'white')

house.box((0,3.35,.88),(4.65,.40,.055),'oak')

house.mesh.quad('garden',[(-2.20,3.62,.90),(2.20,3.62,.90),(2.20,3.62,2.50),(-2.20,3.62,2.50)],[(0,0),(1,0),(1,1),(0,1)])

# Curtains, hung above floor clearance, with visible folds.

for side in (-1,1):

    for i in range(12):house.cylinder((side*2.25+(i-5.5)*.025,3.28,1.6),.029,2.05,'linen')

house.box((-2.5,-3.425,1.04),(.94,.035,2.05),'oak')

house.box((-2.5,-3.395,1.04),(1.02,.025,2.13),'white')

house.box((-2.5,-3.36,1.04),(.90,.025,2.01),'oak')

house.cylinder((-2.18,-3.32,1.03),.025,.05,'brass')

house.save()



sofa=Item('three_seat_sofa',(-2.8,4.95,0,0))

sofa.box((0,0,.28),(2.55,.90,.30),'teal',collision=True,rounded=.06)

sofa.box((0,.36,.65),(2.55,.21,.75),'teal',collision=True,rounded=.045)

for x in (-1.21,1.21):sofa.box((x,-.03,.53),(.18,.87,.56),'teal',collision=True,rounded=.035)

for x in (-.77,0,.77):

    sofa.box((x,-.08,.49),(.72,.65,.18),'linen',rounded=.05)

    sofa.box((x,.24,.74),(.70,.15,.44),'teal',rounded=.04)

for x,y in ((-1.08,-.30),(1.08,-.30),(-1.08,.30),(1.08,.30)):

    sofa.cylinder((x,y,.09),.035,.18,'oak',collision=True)

for x,mat,yaw in ((-.94,'terra',.18),(.88,'linen',-.2)):

    sofa.box((x,.10,.72),(.38,.22,.38),mat,yaw=yaw,rounded=.06)

sofa.save()



carpet=Item('woven_living_room_rug',(-2.8,3.45,0,0))

# A flush decorative rug is deliberately not a raised lidar-invisible obstacle.

carpet.mesh.quad('rug',[(-1.6,-1.15,.002),(1.6,-1.15,.002),(1.6,1.15,.002),(-1.6,1.15,.002)],[(0,0),(1,0),(1,1),(0,1)])

carpet.save()



coffee=Item('rounded_coffee_table',(-2.8,3.65,0,0))

coffee.box((0,0,.40),(1.25,.63,.07),'oak',collision=True,rounded=.018)

for x in (-.47,.47):

    for y in (-.21,.21):coffee.cylinder((x,y,.20),.035,.40,'charcoal',collision=True)

coffee.box((-.20,0,.45),(.28,.20,.025),'burgundy')

coffee.box((-.18,.01,.47),(.25,.18,.022),'white')

coffee.mesh.lathe((.29,.02,.44),[(.045,0),(.048,.08),(.046,.085)],'ceramic')

coffee.save()



console=Item('oak_media_console',(7.55,3.3,0,0))

console.box((0,0,.35),(.45,2.05,.51),'oak',collision=True,rounded=.012)

for y in (-.67,0,.67):

    console.box((-.235,y,.35),(.02,.64,.42),'oak')

    console.box((-.251,y,.50),(.016,.16,.009),'brass')

for y in (-.82,.82):console.cylinder((0,y,.075),.035,.15,'charcoal',collision=True)

console.box((.05,0,1.37),(.04,1.65,.96),'charcoal')

console.mesh.quad('art',[(.025,.79,.93),(.025,-.79,.93),(.025,-.79,1.81),(.025,.79,1.81)],[(0,0),(1,0),(1,1),(0,1)])

for y in (-.88,.88):console.cylinder((0,y,.70),.045,.20,'charcoal')

console.save()



bookshelf=Item('bookcase',(-7.65,3.4,0,0))

bookshelf.box((.08,0,.105),(.42,1.20,.21),'oak',collision=True)

bookshelf.box((-.05,0,1.05),(.12,1.20,2.1),'oak',collision=True)

for y in (-.57,.57):bookshelf.box((.08,y,1.05),(.42,.045,2.1),'oak',collision=True)

for z in (.06,.50,.96,1.42,1.88,2.12):bookshelf.box((.08,0,z),(.42,1.2,.035),'oak',collision=True)

rng=random.Random(17)

for row,z in enumerate((.50,.96,1.42)):

    for i in range(12):

        y=-.48+i*.073; h=rng.uniform(.22,.34)

        bookshelf.box((.13,y,z+.018+h/2),(.22,.055,h),rng.choice(['terra','blue','burgundy','white','teal']))

bookshelf.mesh.lathe((.10,-.22,1.90),[(.065,0),(.08,.09),(.045,.23),(.035,.25)],'ceramic')

bookshelf.box((.15,.32,1.96),(.18,.25,.08),'linen')

bookshelf.save()



dining=Item('dining_table',(-4.2,-2.0,0,0))

dining.box((0,0,.76),(1.45,.88,.065),'oak',collision=True,rounded=.02)

for x in (-.58,.58):

    for y in (-.30,.30):dining.cylinder((x,y,.37),.045,.74,'oak',collision=True)

for x in (-.35,.35):

    dining.cylinder((x,0,.804),.14,.014,'ceramic')

dining.mesh.lathe((0,0,.80),[(.05,0),(.09,.07),(.055,.21)],'terra')

dining.save()



def chair(name,pose):

    item=Item(name,pose)

    item.box((0,0,.45),(.45,.45,.065),'linen',collision=True,rounded=.02)

    item.box((0,.195,.72),(.46,.065,.50),'oak',collision=True,rounded=.015)

    for x in (-.16,.16):

        for y in (-.16,.16):item.cylinder((x,y,.225),.025,.45,'oak',collision=True)

    item.save()

for n,x,y,yaw in [('north',-4.2,-1.23,math.pi),('south',-4.2,-2.78,0),('west',-5.27,-2.0,-math.pi/2),('east',-3.13,-2.0,math.pi/2)]:

    chair('dining_chair_'+n,(x,y,0,yaw))



desk=Item('home_office_desk',(5.7,-5.55,0,0))

desk.box((0,0,.76),(1.65,.65,.055),'oak',collision=True,rounded=.015)

for x in (-.70,.70):

    for y in (-.23,.23):desk.box((x,y,.37),(.045,.045,.74),'charcoal',collision=True)

desk.box((.0,-.17,1.10),(.67,.035,.40),'charcoal')

desk.mesh.quad('art',[(.30,-.149,.925),(-.30,-.149,.925),(-.30,-.149,1.275),(.30,-.149,1.275)],[(0,0),(1,0),(1,1),(0,1)])

desk.box((0,-.17,.90),(.04,.05,.24),'charcoal')

desk.box((0,-.10,.805),(.25,.20,.025),'charcoal')

desk.box((0,.09,.805),(.43,.14,.016),'charcoal')

for y in (-.04,.0,.04):

    for x in range(14):desk.box((-.19+x*.028,y+.08,.816),(.021,.022,.004),'white')

desk.box((.58,.04,.812),(.14,.18,.024),'blue',rounded=.007)

desk.save()

chair('office_chair',(5.7,-4.65,0,math.pi))



lamp=Item('floor_lamp',(-.9,4.95,0,0))

lamp.cylinder((0,0,.105),.20,.21,'charcoal',collision=True)

lamp.cylinder((0,0,.77),.018,1.5,'brass',collision=True)

lamp.mesh.lathe((0,0,1.40),[(.28,0),(.21,.36)],'linen')

lamp.save()



def plant(name,pose,height):

    item=Item(name,pose)

    item.mesh.lathe((0,0,0),[(.16,0),(.21,.32),(.22,.34),(.20,.36)],'terra')

    item.collisions.append(('cylinder',(0,0,.18),(.22,.36),0))

    item.cylinder((0,0,.34+height*.35),.012,height*.7,'oak')

    for i in range(22):

        angle=i*2.399; radius=.03+(i%4)*.035

        z=.33+(i%7)*height/9

        item.mesh.leaf((radius*math.cos(angle),radius*math.sin(angle),z),height*.43,.09,angle,'leaf' if i%2 else 'leaf_light')

    item.save()

plant('window_plant',(5.8,5.3,0,0),1.20)

plant('entry_plant',(-7.0,-5.25,0,0),.72)



art=Item('framed_wall_art',(1.3,-2.5,0,0))

for x in (-.75,.40):

    art.box((x,-3.42,1.70),(.78,.04,1.04),'oak')

    art.mesh.quad('art',[(x+.35,-3.39,1.22),(x-.35,-3.39,1.22),(x-.35,-3.39,2.18),(x+.35,-3.39,2.18)],[(0,0),(1,0),(1,1),(0,1)])

art.save()



# Kitchen cabinetry and island keep the new floor plan furnished, with wide

# central aisles for high-speed simulator tests.

kitchen=Item('kitchen_wall',(0,-5.65,0,0))

for x in (-2.0,-1.0,0,1.0,2.0):

    kitchen.box((x,0,.46),(.98,.60,.92),'white',collision=True)

    kitchen.box((x,.313,.46),(.91,.025,.78),'oak')

    kitchen.box((x,.335,.75),(.22,.012,.015),'brass')

kitchen.box((0,0,.95),(5.1,.65,.055),'charcoal',collision=True)

kitchen.box((1.1,0,.989),(.63,.46,.020),'aluminium')

for x in (-1.4,-1.0):

    for y in (-.12,.12):kitchen.cylinder((x,y,.99),.082,.015,'charcoal')

kitchen.save()

island=Item('kitchen_island',(1.3,-2.7,0,0))

island.box((0,0,.45),(1.9,.75,.90),'oak',collision=True)

island.box((0,0,.93),(2.1,.95,.055),'white',collision=True,rounded=.014)

island.mesh.lathe((.55,0,.965),[(.10,0),(.16,.07),(.13,.09)],'terra')

island.save()

chair('island_stool_left',(.75,-1.75,0,math.pi))

chair('island_stool_right',(1.9,-1.75,0,math.pi))

reading=Item('reading_lounge',(4.6,2.8,0,-.35))

reading.box((0,0,.26),(1.10,.87,.33),'teal',collision=True,rounded=.06)

reading.box((0,.32,.65),(1.10,.20,.62),'teal',collision=True,rounded=.04)

for x in (-.49,.49):reading.box((x,0,.5),(.14,.80,.40),'teal',collision=True,rounded=.03)

for x in (-.42,.42):

    for y in (-.3,.3):reading.cylinder((x,y,.065),.027,.13,'oak',collision=True)

reading.save()

sidetable=Item('reading_side_table',(5.6,2.6,0,0))

sidetable.cylinder((0,0,.49),.30,.055,'oak',collision=True)

sidetable.cylinder((0,0,.23),.045,.46,'charcoal',collision=True)

sidetable.mesh.lathe((0,0,.52),[(.055,0),(.065,.12),(.04,.21)],'ceramic')

sidetable.save()

plant('reading_plant',(6.7,1.55,0,0),1.0)

bench=Item('entry_bench',(-4.3,-5.6,0,0))

bench.box((0,0,.42),(1.4,.45,.14),'linen',collision=True,rounded=.025)

for x in (-.56,.56):bench.box((x,0,.19),(.045,.37,.38),'oak',collision=True)

bench.save()



path=room_mesh.save('living_room')

visual=ET.SubElement(room_link,'visual',name='furnished_room');geometry=ET.SubElement(visual,'geometry')

element(ET.SubElement(geometry,'mesh'),'uri',str(path));element(visual,'cast_shadows','false')



ET.indent(root,space='  ')

ET.ElementTree(root).write(PACKAGE/'worlds/room.sdf',encoding='utf-8',xml_declaration=True)

print(f'Furnished 16 x 12 m room: one fixed body, {len(room_link.findall("collision"))} collision shapes, batched materials.')



## capture_robot_preview.py

"""Temporarily add a camera to the running simulator and save a room overview."""

from pathlib import Path

import struct

import subprocess

import time

import zlib

import rclpy

from rclpy.node import Node

from rclpy.qos import qos_profile_sensor_data

from sensor_msgs.msg import Image



WS=Path('/home/robot/vacuum_ws')

out=WS/'validation/furnished-20261007';out.mkdir(parents=True,exist_ok=True)

sdf=out/'preview-camera.sdf'

sdf.write_text('''<sdf version="1.9"><model name="robot_preview"><static>true</static>

<pose>.4 -.42 .19 0 .17 2.332</pose><link name="camera">

<sensor name="overview" type="camera"><topic>/robot_preview</topic><always_on>true</always_on><update_rate>1</update_rate>

<camera><horizontal_fov>1.0</horizontal_fov><image><width>1400</width><height>850</height><format>R8G8B8</format></image>

<clip><near>0.05</near><far>45</far></clip></camera></sensor></link></model></sdf>''')

rclpy.init();node=Node('furnished_robot_preview_capture');images=[]

node.create_subscription(Image,'/robot_preview',images.append,qos_profile_sensor_data)

bridge=None

created=False

try:

    reset=subprocess.run(['gz','service','-s','/world/vacuum_room/set_pose',

                         '--reqtype','gz.msgs.Pose','--reptype','gz.msgs.Boolean','--timeout','5000',

                         '--req','name: "vacuum", position: {x: 0 y: 0 z: 0.015}, orientation: {w: 1}'],

                         capture_output=True,text=True,timeout=8)

    assert reset.returncode==0 and 'true' in reset.stdout,reset.stdout+reset.stderr

    time.sleep(1)

    result=subprocess.run(['/opt/ros/jazzy/lib/ros_gz_sim/create','-world','vacuum_room','-file',str(sdf),'-name','robot_preview',

                           '-x','.4','-y','-.42','-z','.19','-R','0','-P','.17','-Y','2.332'],capture_output=True,text=True,timeout=20)
    assert result.returncode==0,result.stdout+result.stderr

    created=True

    log=(out/'preview-bridge.log').open('w')

    bridge=subprocess.Popen(['/opt/ros/jazzy/lib/ros_gz_bridge/parameter_bridge','/robot_preview@sensor_msgs/msg/Image[gz.msgs.Image'],stdout=log,stderr=subprocess.STDOUT)

    end=time.monotonic()+25

    while not images and time.monotonic()<end:rclpy.spin_once(node,timeout_sec=.1)

    assert images,'Preview camera did not publish'

    m=images[-1];assert m.encoding=='rgb8',m.encoding

    data=bytes(m.data);raw=b''.join(b'\0'+data[y*m.step:y*m.step+m.width*3] for y in range(m.height))

    def chunk(kind,data):return struct.pack('>I',len(data))+kind+data+struct.pack('>I',zlib.crc32(kind+data))

    png=b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',m.width,m.height,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(raw))+chunk(b'IEND',b'')

    path=out/'robot-hardware.png';path.write_bytes(png);print(path,flush=True)

finally:

    if bridge:

        bridge.terminate()

        try:bridge.wait(timeout=5)

        except subprocess.TimeoutExpired:bridge.kill();bridge.wait(timeout=2)

        log.close()

    if created:

        result=subprocess.run(['gz','service','-s','/world/vacuum_room/remove','--reqtype','gz.msgs.Entity','--reptype','gz.msgs.Boolean','--timeout','5000','--req','name: "robot_preview", type: MODEL'],capture_output=True,text=True,timeout=8)

        print('Preview camera removal:',result.stdout.strip(),result.stderr.strip(),flush=True)

    node.destroy_node();rclpy.shutdown()



## capture_room_preview.py

"""Temporarily add a camera to the running simulator and save a room overview."""

from pathlib import Path

import struct

import subprocess

import time

import zlib

import rclpy

from rclpy.node import Node

from rclpy.qos import qos_profile_sensor_data

from sensor_msgs.msg import Image



WS=Path('/home/robot/vacuum_ws')

out=WS/'validation/furnished-20261007';out.mkdir(parents=True,exist_ok=True)

sdf=out/'preview-camera.sdf'

sdf.write_text('''<sdf version="1.9"><model name="room_preview"><static>true</static>

<pose>-12.0 -10.0 20.0 0 0.91 0.695</pose><link name="camera">
<sensor name="overview" type="camera"><topic>/room_preview</topic><always_on>true</always_on><update_rate>1</update_rate>

<camera><horizontal_fov>1.1</horizontal_fov><image><width>1200</width><height>900</height><format>R8G8B8</format></image>
<clip><near>0.05</near><far>45</far></clip></camera></sensor></link></model></sdf>''')

rclpy.init();node=Node('furnished_room_preview_capture');images=[]

node.create_subscription(Image,'/room_preview',images.append,qos_profile_sensor_data)

bridge=None

created=False

try:

    result=subprocess.run(['/opt/ros/jazzy/lib/ros_gz_sim/create','-world','vacuum_room','-file',str(sdf),'-name','room_preview',

                           '-x','-12','-y','-10','-z','20','-R','0','-P','.91','-Y','.695'],capture_output=True,text=True,timeout=20)
    assert result.returncode==0,result.stdout+result.stderr

    created=True

    log=(out/'preview-bridge.log').open('w')

    bridge=subprocess.Popen(['/opt/ros/jazzy/lib/ros_gz_bridge/parameter_bridge','/room_preview@sensor_msgs/msg/Image[gz.msgs.Image'],stdout=log,stderr=subprocess.STDOUT)

    end=time.monotonic()+25

    while not images and time.monotonic()<end:rclpy.spin_once(node,timeout_sec=.1)

    assert images,'Preview camera did not publish'

    m=images[-1];assert m.encoding=='rgb8',m.encoding

    data=bytes(m.data);raw=b''.join(b'\0'+data[y*m.step:y*m.step+m.width*3] for y in range(m.height))

    def chunk(kind,data):return struct.pack('>I',len(data))+kind+data+struct.pack('>I',zlib.crc32(kind+data))

    png=b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',m.width,m.height,8,2,0,0,0))+chunk(b'IDAT',zlib.compress(raw))+chunk(b'IEND',b'')

    path=out/'room-overview.png';path.write_bytes(png);print(path,flush=True)

finally:

    if bridge:

        bridge.terminate()

        try:bridge.wait(timeout=5)

        except subprocess.TimeoutExpired:bridge.kill();bridge.wait(timeout=2)

        log.close()

    if created:

        result=subprocess.run(['gz','service','-s','/world/vacuum_room/remove','--reqtype','gz.msgs.Entity','--reptype','gz.msgs.Boolean','--timeout','5000','--req','name: "room_preview", type: MODEL'],capture_output=True,text=True,timeout=8)

        print('Preview camera removal:',result.stdout.strip(),result.stderr.strip(),flush=True)

    node.destroy_node();rclpy.shutdown()



## check_lab.py

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

        self.assertEqual(controller_bridge.decode('{"v":100,"w":100,"held":true}'), (1.50, 2.4))

        self.assertEqual(controller_bridge.decode('{"v":-100,"w":-100,"held":true}'), (-.90, -2.4))

        self.assertEqual(controller_bridge.decode('{"v":0.1,"w":0.2,"held":false}'), (0., 0.))

        with self.assertRaises(ValueError):

            controller_bridge.decode('{"v":"NaN","w":0,"held":true}')



    def test_armed_input_without_hold_button(self):

        self.assertEqual(controller_bridge.decode('{"v":1.5,"w":2.4,"enabled":true}'), (1.5, 2.4))

        self.assertEqual(controller_bridge.decode('{"v":1.5,"w":0,"enabled":false}'), (0., 0.))

        self.assertEqual(controller_bridge.decode('{"v":1.5,"w":0}'), (0., 0.))



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



## Check-Lab.ps1

$ErrorActionPreference = 'Stop'

$taskProblems = @()

Add-Type -AssemblyName System.Windows.Forms

Add-Type -AssemblyName System.Drawing

foreach ($name in @('Vacuum-Lab.ps1', 'Controller-Panel.ps1', 'Files-Panel.ps1', 'Modern-Theme.ps1', 'Check-Lab.ps1')) {

    $taskTokens=$null; $taskErrors=$null

    [void][Management.Automation.Language.Parser]::ParseFile((Join-Path $PSScriptRoot $name),[ref]$taskTokens,[ref]$taskErrors)

    $taskProblems += $taskErrors

}

if ($taskProblems.Count) { $taskProblems | Format-List; throw 'PowerShell parsing failed.' }

. (Join-Path $PSScriptRoot 'Modern-Theme.ps1')

. (Join-Path $PSScriptRoot 'Controller-Panel.ps1')

if ([Runtime.InteropServices.Marshal]::SizeOf([type][VacuumJoystick+Caps]) -ne 728) { throw 'Unexpected joystick capability layout.' }

if ([Runtime.InteropServices.Marshal]::SizeOf([type][VacuumJoystick+Pos]) -ne 52) { throw 'Unexpected joystick position layout.' }

'PowerShell parsed; joystick interop compiled. Connected devices:'

[VacuumJoystick]::Devices() | ForEach-Object { $_.ToString() }

Show-ControllerPanel '' $PSScriptRoot -CheckOnly | Format-List

'No robot motion or Ubuntu changes were performed by this check.'



## command_gate.py

"""Select exactly one launcher command source before Collision Monitor."""

import math

from pathlib import Path

import json

import time

import rclpy

from geometry_msgs.msg import Twist

from rclpy.node import Node



MODE = Path('/home/robot/vacuum_ws/.lab/manual-mode')

PROFILE = json.loads((Path(__file__).parent / 'robot-profile.json').read_text())['drive']





class Gate(Node):

    def __init__(self):

        super().__init__('vacuum_command_gate')

        self.pub = self.create_publisher(Twist, '/vacuum/selected_cmd_vel', 1)

        self.inputs = {'manual': (0., 0., 0.), 'auto': (0., 0., 0.)}

        self.mode = 'manual' if MODE.exists() else 'auto'

        self.last_status = None

        self.create_subscription(Twist, '/cmd_vel_smoothed', lambda msg: self.receive('auto', msg), 1)

        self.create_subscription(Twist, '/vacuum/manual_cmd_vel', lambda msg: self.receive('manual', msg), 1)

        self.create_timer(PROFILE['input_period_s'], self.tick)



    def receive(self, source, msg):

        v, w = msg.linear.x, msg.angular.z

        if not math.isfinite(v) or not math.isfinite(w):

            v, w = 0., 0.

        self.inputs[source] = (max(-PROFILE['reverse_m_s'], min(PROFILE['forward_m_s'], v)), max(-PROFILE['turn_rad_s'], min(PROFILE['turn_rad_s'], w)), time.monotonic())



    def tick(self):

        mode = 'manual' if MODE.exists() else 'auto'

        if mode != self.mode:

            self.mode = mode

            # Require fresh input after every mode transition.

            self.inputs = {'manual': (0., 0., 0.), 'auto': (0., 0., 0.)}

        v, w, stamp = self.inputs[mode]

        message = Twist()

        if time.monotonic() - stamp < .3:

            message.linear.x, message.angular.z = v, w

        status = (mode, abs(message.linear.x) > .001 or abs(message.angular.z) > .001)

        if status != self.last_status:

            self.get_logger().info(f'Selected {mode}: speed={message.linear.x:.3f}, turn={message.angular.z:.3f}')

            self.last_status = status

        self.pub.publish(message)





def main():

    rclpy.init()

    node = Gate()

    try:

        rclpy.spin(node)

    except KeyboardInterrupt:

        pass

    finally:

        node.pub.publish(Twist())

        node.destroy_node()

        if rclpy.ok():

            rclpy.shutdown()





if __name__ == '__main__':

    main()



## controller_bridge.py

"""Manual simulator control via stdin; steady-time watchdog and Nav2 interlock."""

import json

import math

from pathlib import Path

import sys

import threading

import time

import rclpy

from geometry_msgs.msg import Twist

from lifecycle_msgs.srv import GetState

from nav2_msgs.msg import CollisionMonitorState

from nav_msgs.msg import Odometry

from sensor_msgs.msg import LaserScan

from rclpy.qos import qos_profile_sensor_data

from rclpy.node import Node



MODE = Path('/home/robot/vacuum_ws/.lab/manual-mode')

PROFILE = json.loads((Path(__file__).parent / 'robot-profile.json').read_text())['drive']





def decode(line):

    data = json.loads(line)

    v, w = float(data['v']), float(data['w'])

    if not math.isfinite(v) or not math.isfinite(w):

        raise ValueError('Non-finite control input')

    if data.get('enabled', data.get('held', False)) is not True:

        return 0., 0.

    return max(-PROFILE['reverse_m_s'], min(PROFILE['forward_m_s'], v)), max(-PROFILE['turn_rad_s'], min(PROFILE['turn_rad_s'], w))





class Bridge(Node):

    def __init__(self):

        super().__init__('vacuum_manual_controller')

        self.pub = self.create_publisher(Twist, '/vacuum/manual_cmd_vel', 1)

        self.lock = threading.Lock()

        self.latest = (0., 0.)

        self.received = 0.

        self.closed = False

        self.states = {'collision_monitor': (0, 0.)}

        self.state_clients = {name: self.create_client(GetState, f'/{name}/get_state') for name in self.states}

        self.pending = {}

        self.last_status = None

        self.report_at = 0.

        self.guard_action = (0, '')

        self.output = (0., 0., 0.)

        self.scan_at = 0.

        self.odom = (0., 0., 0.)

        self.motion_since = 0.

        self.create_subscription(CollisionMonitorState, '/collision_monitor_state', self.guard_state, 10)

        self.create_subscription(Twist, '/cmd_vel', self.guard_output, 1)

        self.create_subscription(LaserScan, '/scan', self.scan_received, qos_profile_sensor_data)

        self.create_subscription(Odometry, '/odom', self.odom_received, qos_profile_sensor_data)

        self.create_timer(PROFILE['input_period_s'], self.tick)

        self.create_timer(.25, self.check_states)

        threading.Thread(target=self.read_input, daemon=True).start()



    def read_input(self):

        try:

            for line in sys.stdin:

                try:

                    command = decode(line)

                except (ValueError, KeyError, TypeError):

                    command = (0., 0.)

                with self.lock:

                    self.latest = command

                    self.received = time.monotonic()

        finally:

            with self.lock:

                self.latest = (0., 0.)

                self.closed = True



    def check_states(self):

        now = time.monotonic()

        for name, client in self.state_clients.items():

            previous = self.pending.get(name)

            if previous and not previous[0].done():

                if now - previous[1] < .75:

                    continue

                # A lost service response must not leave a permanently pending

                # future that prevents all subsequent health checks.

                self.pending.pop(name)

                client.remove_pending_request(previous[0])

                previous[0].cancel()

            if not client.service_is_ready():

                continue

            future = client.call_async(GetState.Request())

            self.pending[name] = (future, now)

            future.add_done_callback(lambda result, name=name: self.record(name, result))



    def record(self, name, future):

        if self.pending.get(name, (None,))[0] is not future:

            return

        try:

            self.states[name] = (future.result().current_state.id, time.monotonic())

        except Exception:

            self.states[name] = (0, 0.)



    def guard_state(self, message):

        self.guard_action = (message.action_type, message.polygon_name)



    def guard_output(self, message):

        self.output = (message.linear.x, message.angular.z, time.monotonic())



    def scan_received(self, message):

        self.scan_at = time.monotonic()



    def odom_received(self, message):

        self.odom = (message.twist.twist.linear.x, message.twist.twist.angular.z, time.monotonic())



    def report(self, now, safe, v, w):

        if now < self.report_at:

            return

        self.report_at = now + .25

        out_v, out_w, stamp = self.output

        actual_v, actual_w, odom_stamp = self.odom

        action, polygon = self.guard_action

        reason = 'Ready'

        if not MODE.exists():

            reason = 'Manual mode is not selected'

        elif now - self.scan_at > .5:

            reason = 'Lidar data missing or stale; guard stops motion'

        elif not safe:

            reason = 'Waiting for collision guard health; commands stopped'

        elif abs(v) + abs(w) > .001:

            if now - stamp > .5:

                reason = 'No fresh guard output; commands stopped'

            elif abs(out_v) + abs(out_w) < .001:

                if action and polygon:

                    escape = 'try reverse' if v > .001 else ('try forward' if v < -.001 else 'move away before turning')

                    reason = 'Obstacle blocks this direction; ' + escape

                else:

                    reason = 'Guard stopped motion; check lidar/TF in Ubuntu logs'

            elif abs(out_v) < abs(v) - .01 or abs(out_w) < abs(w) - .01:

                reason = 'Slowing near an obstacle'

            else:

                reason = 'Driving'

                if now - odom_stamp > 1.:

                    reason = 'Odometry missing; check simulator/controller'

                elif self.motion_since and now - self.motion_since > 1.5 and abs(actual_v) < .015 and abs(actual_w) < .04:

                    reason = 'No actual movement; STOP and check simulator/controller'

        print(json.dumps({'ready': safe, 'reason': reason, 'polygon': polygon,

                          'requested_v': v, 'output_v': out_v, 'output_w': out_w,

                          'actual_v': actual_v, 'actual_w': actual_w}), flush=True)



    def tick(self):

        now = time.monotonic()

        safe = MODE.exists() and now - self.scan_at < .5 and all(state == 3 and now - stamp < 1.

                                     for state, stamp in self.states.values())

        with self.lock:

            v, w = self.latest if safe and now - self.received < .3 else (0., 0.)

            closed = self.closed

        message = Twist()

        message.linear.x, message.angular.z = v, w

        if abs(v) + abs(w) > .03:

            if not self.motion_since:

                self.motion_since = now

        else:

            self.motion_since = 0.

        self.pub.publish(message)

        self.report(now, safe, v, w)

        if closed:

            raise KeyboardInterrupt





def main():

    # The launcher lock, separate from the simulator lock, serializes manual sources.

    import fcntl

    path = Path('/home/robot/vacuum_ws/.lab/manual-input.lock')

    with path.open('a') as lock:

        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)

        rclpy.init()

        node = Bridge()

        try:

            rclpy.spin(node)

        except KeyboardInterrupt:

            pass

        finally:

            node.pub.publish(Twist())

            node.destroy_node()

            if rclpy.ok():

                rclpy.shutdown()





if __name__ == '__main__':

    main()



## Controller-Panel.ps1

# Built-in Windows joystick reader: no USB forwarding, drivers, or Python install.

Add-Type -TypeDefinition @'

using System;

using System.Collections.Generic;

using System.Runtime.InteropServices;

public static class VacuumJoystick {

    [StructLayout(LayoutKind.Sequential, CharSet=CharSet.Unicode)]

    public struct Caps {

        public ushort Mid, Pid;

        [MarshalAs(UnmanagedType.ByValTStr, SizeConst=32)] public string Name;

        public uint Xmin,Xmax,Ymin,Ymax,Zmin,Zmax,Buttons,PeriodMin,PeriodMax;

        public uint Rmin,Rmax,Umin,Umax,Vmin,Vmax,Flags,MaxAxes,Axes,MaxButtons;

        [MarshalAs(UnmanagedType.ByValTStr, SizeConst=32)] public string RegKey;

        [MarshalAs(UnmanagedType.ByValTStr, SizeConst=260)] public string Oem;

    }

    [StructLayout(LayoutKind.Sequential)]

    public struct Pos {

        public uint Size,Flags,X,Y,Z,R,U,V,Buttons,ButtonNumber,Pov,Reserved1,Reserved2;

    }

    public class Device {

        public uint Id; public Caps Info; public string DisplayName;

        public override string ToString() { return DisplayName + " (" + Info.Axes + " axes, " + Info.Buttons + " buttons)"; }

    }

    [DllImport("winmm.dll", EntryPoint="joyGetDevCapsW", CharSet=CharSet.Unicode)]

    static extern uint GetCaps(UIntPtr id, out Caps caps, uint size);

    [DllImport("winmm.dll", EntryPoint="joyGetPosEx")]

    static extern uint GetPos(uint id, ref Pos pos);

    public static Device[] Devices() {

        var result = new List<Device>();

        for(uint id=0;id<16;id++) {

            Caps caps; Pos pos = new Pos {Size=52,Flags=255};

            if(GetCaps(new UIntPtr(id),out caps,(uint)Marshal.SizeOf(typeof(Caps)))==0 && GetPos(id,ref pos)==0) {

                string name=caps.Name;

                string key="System\\CurrentControlSet\\Control\\MediaProperties\\PrivateProperties\\Joystick\\OEM\\VID_"+

                           caps.Mid.ToString("X4")+"&PID_"+caps.Pid.ToString("X4");

                foreach(var hive in new[] {Microsoft.Win32.Registry.CurrentUser,Microsoft.Win32.Registry.LocalMachine}) {

                    using(var entry=hive.OpenSubKey(key)) {

                        var friendly=entry==null ? null : entry.GetValue("OEMName") as string;

                        if(!String.IsNullOrEmpty(friendly)) { name=friendly; break; }

                    }

                }

                result.Add(new Device {Id=id,Info=caps,DisplayName=name});

            }

        }

        return result.ToArray();

    }

    public static double[] Read(Device device, out uint buttons) {

        Caps caps; Pos pos = new Pos {Size=52,Flags=255};

        if(GetCaps(new UIntPtr(device.Id),out caps,(uint)Marshal.SizeOf(typeof(Caps)))!=0 ||

           caps.Mid!=device.Info.Mid || caps.Pid!=device.Info.Pid || caps.Name!=device.Info.Name ||

           GetPos(device.Id,ref pos)!=0) throw new Exception("Controller disconnected or changed.");

        uint[] raw={pos.X,pos.Y,pos.Z,pos.R,pos.U,pos.V};

        uint[] min={caps.Xmin,caps.Ymin,caps.Zmin,caps.Rmin,caps.Umin,caps.Vmin};

        uint[] max={caps.Xmax,caps.Ymax,caps.Zmax,caps.Rmax,caps.Umax,caps.Vmax};

        var axes=new double[6];

        for(int i=0;i<6;i++) axes[i]=max[i]>min[i] ? Math.Max(-1,Math.Min(1,2.0*(raw[i]- (double)min[i])/(max[i]-min[i])-1)) : 0;

        buttons=pos.Buttons; return axes;

    }

    public static bool Supports(Device device, int axis) {

        return axis>=0 && axis<6 && (axis<2 || (device.Info.Flags & (1u << (axis-2)))!=0);

    }

    // Read Ubuntu status off the UI thread; a delayed read cannot freeze input.

    public class OutputPump {

        private readonly object gate = new object();

        private string latest = "", log = "";

        private DateTime received = DateTime.MinValue;

        public System.Threading.Tasks.Task Completion;

        public OutputPump(System.IO.StreamReader reader) {

            Completion = System.Threading.Tasks.Task.Run(() => {

                string line;

                while ((line = reader.ReadLine()) != null) {

                    lock (gate) {

                        if (line.StartsWith("{")) { latest = line; received = DateTime.UtcNow; }

                        log += line + "\n";

                        if (log.Length > 8192) log = log.Substring(log.Length - 8192);

                    }

                }

            });

        }

        public string Latest { get { lock (gate) return latest; } }

        public bool Fresh { get { lock (gate) return (DateTime.UtcNow - received).TotalSeconds < 1; } }

        public string Log { get { lock (gate) return log; } }

    }

}

'@



function Show-ControllerPanel([string]$wslPath, [string]$profileRoot, [switch]$CheckOnly, [string]$PreviewPath) {

    $driveProfile=(Get-Content -LiteralPath (Join-Path $profileRoot 'robot-profile.json') -Raw | ConvertFrom-Json).drive

    $panel = New-Object Windows.Forms.Form

    $panel.Text = 'Vacuum Lab / Direct drive'

    $area = [Windows.Forms.Screen]::PrimaryScreen.WorkingArea

    $panel.Size = New-Object Drawing.Size([Math]::Min(650,$area.Width-24), [Math]::Min(820,$area.Height-24))
    $panel.AutoScroll=$true

    $panel.AutoScrollMinSize=New-Object Drawing.Size(630,752)

    $panel.StartPosition = 'CenterParent'

    $panel.FormBorderStyle = 'FixedDialog'

    $panel.MaximizeBox = $false

    $panel.Font = New-Object Drawing.Font('Segoe UI', 10)

    $state = @{ Armed=$false; Process=$null; Pump=$null; Centers=@(0.,0.,0.,0.,0.,0.); Axes=$null; Buttons=[uint32]0; Device=$null }



    function Label-At($text,$y) {

        $label = New-Object Windows.Forms.Label

        $label.Text=$text; $label.SetBounds(20,$y,595,30); $panel.Controls.Add($label)

        return $label

    }

    $null = Label-At 'Push forward. Pull back to reverse. Turn the yoke to steer.' 16

    $device = New-Object Windows.Forms.ComboBox

    $device.DropDownStyle='DropDownList'; $device.SetBounds(20,50,590,30)

    $panel.Controls.Add($device)

    foreach ($item in [VacuumJoystick]::Devices()) { [void]$device.Items.Add($item) }

    if ($device.Items.Count) { $device.SelectedIndex=0 }

    for ($i=0;$i -lt $device.Items.Count;$i++) {

        if ($device.Items[$i].DisplayName -match 'Honeycomb|Alpha') { $device.SelectedIndex=$i; break }

    }

    $live = Label-At 'Connect a controller before opening this panel.' 94

    $live.Height=52

    $null = Label-At 'Speed axis                     Steering axis                      Dead zone (%)' 156

    $speed = New-Object Windows.Forms.ComboBox

    $steer = New-Object Windows.Forms.ComboBox

    foreach ($box in @($speed,$steer)) {

        $box.DropDownStyle='DropDownList'; $box.Items.AddRange(@('X','Y','Z','R','U','V')); $panel.Controls.Add($box)

    }

    $speed.SetBounds(20,186,170,30); $speed.SelectedIndex=1

    $steer.SetBounds(220,186,170,30); $steer.SelectedIndex=0

    $dead = New-Object Windows.Forms.NumericUpDown

    $dead.Minimum=2; $dead.Maximum=40; $dead.Value=5; $dead.SetBounds(420,186,160,30)

    $panel.Controls.Add($dead)

    $invertSpeed = New-Object Windows.Forms.CheckBox

    $invertSpeed.Text='Invert speed'; $invertSpeed.Checked=$true; $invertSpeed.SetBounds(20,224,170,30)

    $invertSteer = New-Object Windows.Forms.CheckBox

    $invertSteer.Text='Invert steering'; $invertSteer.Checked=$true; $invertSteer.SetBounds(220,224,190,30)

    $panel.Controls.AddRange(@($invertSpeed,$invertSteer))

    $null = Label-At 'Optional hold button          Stop button (latched)' 268

    $hold = New-Object Windows.Forms.NumericUpDown

    $stop = New-Object Windows.Forms.NumericUpDown

    foreach ($box in @($hold,$stop)) { $box.Minimum=1; $box.Maximum=32; $panel.Controls.Add($box) }

    $hold.SetBounds(20,298,170,30); $hold.Value=1

    $stop.SetBounds(220,298,170,30); $stop.Value=3

    $requireHold=New-Object Windows.Forms.CheckBox

    $requireHold.Text='Require drive button'

    $requireHold.Checked=$driveProfile.require_hold_button; $requireHold.SetBounds(420,270,195,28)
    $hold.Enabled=$requireHold.Checked; $panel.Controls.Add($requireHold)
    $requireHold.Add_CheckedChanged({ Disarm-Drive; $hold.Enabled=$requireHold.Checked; $message.Text='Drive mode changed. Center the yoke and re-arm.' })

    $message = Label-At 'Center the yoke and arm once. Move the yoke to drive; center to stop.' 344

    $message.Height=48

    $arm = New-Object Windows.Forms.Button

    $arm.Text='Arm drive'; $arm.SetBounds(20,405,175,42)

    $disarm = New-Object Windows.Forms.Button

    $disarm.Text='STOP / disarm'; $disarm.SetBounds(220,405,175,42)

    $center = New-Object Windows.Forms.Button

    $center.Text='Set neutral center'; $center.SetBounds(420,405,190,42)

    $panel.Controls.AddRange(@($arm,$disarm,$center))

    $save = New-Object Windows.Forms.Button

    $save.Text='Save custom profile'; $save.SetBounds(20,465,175,42)

    $load = New-Object Windows.Forms.Button

    $load.Text='Load custom profile'; $load.SetBounds(220,465,175,42)

    $preset = New-Object Windows.Forms.Button

    $preset.Text='Honeycomb Alpha'; $preset.SetBounds(420,465,190,42)

    $panel.Controls.AddRange(@($save,$load,$preset))

    $pull = New-Object Windows.Forms.Button

    $pull.Text='Set pull = reverse'; $pull.SetBounds(20,520,175,36)

    $panel.Controls.Add($pull)

    $pullHint = Label-At 'Pull the yoke fully back, then click Set pull = reverse.' 523

    $pullHint.Text='Pull fully back, then set reverse.'
    $pullHint.SetBounds(220,523,190,42)
    $fileButton=New-Object Windows.Forms.Button
    $fileButton.Text='All project files'; $fileButton.SetBounds(420,520,190,36)
    $panel.Controls.Add($fileButton)
    $fileButton.Add_Click({
        Disarm-Drive; $message.Text='Stopped for file browsing. Center and re-arm when finished.'
        Show-LabFiles $wslPath $profileRoot '[REDACTED_HOME_PATH] VS Code\bin\code.cmd'
    })
    $null = Label-At 'Preview: push must produce + speed; pulling must produce − speed.' 569

    $background = New-Object Windows.Forms.CheckBox

    $background.Text='Keep drive armed when switching windows'

    $background.Checked=$true; $background.SetBounds(20,606,595,30)

    $panel.Controls.Add($background)

    $guardStatus = Label-At 'Ubuntu guard: connecting...' 643

    $guardStatus.Height=48

    $footer = Label-At 'Center the yoke to stop. STOP disarms. Input loss also stops drive.' 697

    $footer.Height=55

    $footer.Text += "`r`nSpeed: +1.50 / -0.90 m/s. Responsive steering: 2.4 rad/s."



    function Send-Drive($v,$w,$enabled) {

        if ($state.Process -and -not $state.Process.HasExited) {

            $packet = @{v=[double]$v;w=[double]$w;enabled=[bool]$enabled} | ConvertTo-Json -Compress

            try {

                $state.Process.StandardInput.WriteLine($packet)

                $state.Process.StandardInput.Flush()

            } catch {

                $state.Armed=$false

                $message.Text='Stopped: Ubuntu input connection was lost.'

            }

        }

    }

    function Disarm-Drive {

        $state.Armed=$false

        Send-Drive 0 0 $false

        $arm.Text='Arm drive'

    }

    function Axis-Value($index,$invert) {

        $value = [Math]::Max(-1,[Math]::Min(1,$state.Axes[$index]-$state.Centers[$index]))

        $zone = [double]$dead.Value / 100

        if ([Math]::Abs($value) -le $zone) { return 0. }

        $value = [Math]::Sign($value) * ([Math]::Abs($value)-$zone)/(1-$zone)

        if ($invert) { $value = -$value }

        return $value

    }

    $device.Add_SelectedIndexChanged({ Disarm-Drive; $state.Centers=@(0.,0.,0.,0.,0.,0.) })

    foreach ($box in @($speed,$steer)) { $box.Add_SelectedIndexChanged({ Disarm-Drive }) }

    foreach ($box in @($hold,$stop,$dead)) { $box.Add_ValueChanged({ Disarm-Drive }) }

    foreach ($box in @($invertSpeed,$invertSteer)) { $box.Add_CheckedChanged({ Disarm-Drive }) }

    $disarm.Add_Click({ Disarm-Drive; $message.Text='Stopped. Center the yoke and release buttons before arming again.' })

    $center.Add_Click({

        Disarm-Drive

        if ($state.Axes) { $state.Centers = @($state.Axes); $message.Text='Neutral center saved for this session. Check your preview values.' }

    })

    $arm.Add_Click({

        if (-not $state.Axes -or -not $state.Process -or $state.Process.HasExited) { $message.Text='Controller or Ubuntu input bridge unavailable.'; return }

        if (($requireHold.Checked -and $hold.Value -eq $stop.Value) -or $speed.SelectedIndex -eq $steer.SelectedIndex) { $message.Text='Choose distinct axes; optional hold and stop must be different.'; return }

        if (-not [VacuumJoystick]::Supports($device.SelectedItem,$speed.SelectedIndex) -or -not [VacuumJoystick]::Supports($device.SelectedItem,$steer.SelectedIndex)) { $message.Text='Choose axes supported by this controller.'; return }

        if (($requireHold.Checked -and $hold.Value -gt $device.SelectedItem.Info.Buttons) -or $stop.Value -gt $device.SelectedItem.Info.Buttons) { $message.Text='Choose buttons that exist on this controller.'; return }

        $driveMask = ([uint64]1 -shl ([int]$stop.Value-1))

        if ($requireHold.Checked) { $driveMask = $driveMask -bor ([uint64]1 -shl ([int]$hold.Value-1)) }

        if ((Axis-Value $speed.SelectedIndex $false) -ne 0 -or (Axis-Value $steer.SelectedIndex $false) -ne 0 -or ([uint64]$state.Buttons -band $driveMask) -ne 0) {

            $message.Text='Center the selected axes and release STOP before arming.'; return

        }

        $state.Armed=$true; $arm.Text='Drive armed'

        $message.Text='Armed. Move the yoke to drive; center the yoke to stop.'

    })

    $preset.Add_Click({

        Disarm-Drive; $speed.SelectedIndex=1; $steer.SelectedIndex=0

        $invertSpeed.Checked=$true; $invertSteer.Checked=$true; $hold.Value=1; $stop.Value=3; $dead.Value=5; $requireHold.Checked=$false

        $state.Centers=@(0.,0.,0.,0.,0.,0.)

        $message.Text='Alpha starting profile loaded. Verify live axes/buttons; actual numbering may vary.'

    })

    $pull.Add_Click({

        Disarm-Drive

        if (-not $state.Axes) { $message.Text='Connect a controller first.'; return }

        $raw = $state.Axes[$speed.SelectedIndex] - $state.Centers[$speed.SelectedIndex]

        if ([Math]::Abs($raw) -lt .3) { $message.Text='Pull the yoke further back, then click Set pull = reverse.'; return }

        $invertSpeed.Checked = $raw -gt 0

        $message.Text='Pulling is now reverse. Return to neutral before arming.'

    })

    $save.Add_Click({

        Disarm-Drive

        if (-not $device.SelectedItem) { return }

        $dialog = New-Object Windows.Forms.SaveFileDialog

        $dialog.Filter='Controller profile (*.json)|*.json'; $dialog.InitialDirectory=$profileRoot; $dialog.FileName='my-controller.json'

        if ($dialog.ShowDialog() -eq 'OK') {

            @{ version=2; requireHold=$requireHold.Checked; device=$device.SelectedItem.DisplayName; speed=$speed.SelectedIndex; steering=$steer.SelectedIndex;

               invertSpeed=$invertSpeed.Checked; invertSteering=$invertSteer.Checked; hold=[int]$hold.Value;

               stop=[int]$stop.Value; deadZone=[int]$dead.Value; centers=@($state.Centers) } |

                ConvertTo-Json | Set-Content -LiteralPath $dialog.FileName -Encoding UTF8

            $message.Text='Custom bindings saved.'

        }

        $dialog.Dispose()

    })

    $load.Add_Click({

        Disarm-Drive

        $dialog=New-Object Windows.Forms.OpenFileDialog

        $dialog.Filter='Controller profile (*.json)|*.json'; $dialog.InitialDirectory=$profileRoot

        if ($dialog.ShowDialog() -eq 'OK') {

            try {

                $p = Get-Content -LiteralPath $dialog.FileName -Raw | ConvertFrom-Json

                if ($p.version -notin @(1,2) -or $p.speed -notin 0..5 -or $p.steering -notin 0..5 -or

                    $p.hold -notin 1..32 -or $p.stop -notin 1..32 -or $p.deadZone -notin 2..40 -or

                    $p.centers.Count -ne 6 -or $p.invertSpeed -isnot [bool] -or $p.invertSteering -isnot [bool]) { throw 'Invalid profile values.' }

                foreach ($value in $p.centers) { if ($value -isnot [ValueType] -or [double]::IsNaN($value) -or [Math]::Abs($value) -gt 1) { throw 'Invalid center.' } }

                $speed.SelectedIndex=$p.speed; $steer.SelectedIndex=$p.steering; $hold.Value=$p.hold; $stop.Value=$p.stop

                $dead.Value=$p.deadZone; $invertSpeed.Checked=$p.invertSpeed; $invertSteer.Checked=$p.invertSteering

                $requireHold.Checked=($p.version -eq 2 -and $p.requireHold -eq $true)

                $state.Centers=@($p.centers)

                $message.Text="Loaded bindings for $($p.device). Verify them on the selected controller."

            } catch { $message.Text="Could not load profile: $_" }

        }

        $dialog.Dispose()

    })

    $background.Add_CheckedChanged({ Disarm-Drive; $message.Text='Focus behavior changed. Center and re-arm to drive.' })

    $panel.Add_Deactivate({

        if (-not $background.Checked) {

            Disarm-Drive; $message.Text='Disarmed: panel lost focus. Re-arm or enable switching windows.'

        }

    })

    $timer = New-Object Windows.Forms.Timer

    $timer.Interval=20

    $timer.Add_Tick({

        try {

            if (-not $device.SelectedItem) { Send-Drive 0 0 $false; return }

            [uint32]$bits=0

            $state.Axes=[VacuumJoystick]::Read($device.SelectedItem,[ref]$bits)

            $state.Buttons=$bits

            $axesText = for ($i=0;$i -lt 6;$i++) { '{0}: {1:F2}' -f @('X','Y','Z','R','U','V')[$i],$state.Axes[$i] }

            $pressed = for ($i=0;$i -lt 32;$i++) { if (([uint64]$bits -band ([uint64]1 -shl $i)) -ne 0) { $i+1 } }

            $live.Text = ($axesText -join '   ') + "`r`nPressed buttons: " + ($pressed -join ', ')

            $preview = Axis-Value $speed.SelectedIndex $invertSpeed.Checked

            $previewSpeed = $preview * $(if ($preview -ge 0) { $driveProfile.forward_m_s } else { $driveProfile.reverse_m_s })

            $live.Text += ('   Speed: {0:+0.000;-0.000;0.000} m/s' -f $previewSpeed)

            if (-not $background.Checked -and -not $panel.ContainsFocus) { Disarm-Drive }

            if (([uint64]$bits -band ([uint64]1 -shl ([int]$stop.Value-1))) -ne 0) {

                Disarm-Drive; $message.Text='STOP button is pressed. Release it, center the yoke, then re-arm.'

            }

            $held = $state.Armed -and (-not $requireHold.Checked -or (([uint64]$bits -band ([uint64]1 -shl ([int]$hold.Value-1))) -ne 0))

            $v=0.; $w=0.

            if ($held) {

                $a=Axis-Value $speed.SelectedIndex $invertSpeed.Checked

                $v=$a * $(if ($a -ge 0) { $driveProfile.forward_m_s } else { $driveProfile.reverse_m_s })

                $w=(Axis-Value $steer.SelectedIndex $invertSteer.Checked) * $driveProfile.turn_rad_s

            }

            Send-Drive $v $w $held

            if ($state.Armed) {

                if (-not $held) { $message.Text="Armed. Hold button $($hold.Value) to drive (see live pressed buttons above)." }

                elseif ([Math]::Abs($v) + [Math]::Abs($w) -lt .001) { $message.Text='Armed at neutral. Move the yoke to drive.' }

                else { $message.Text='Driving. Center the yoke to stop, or press STOP to disarm.' }

            }

            if ($state.Pump -and $state.Pump.Latest) {

                $health = $state.Pump.Latest | ConvertFrom-Json

                if ($state.Armed) { $message.Text += "`r`n" + $health.reason }

                $guardStatus.Text = 'Ubuntu guard: ' + $health.reason + "`r`n" +

                    ('Guard: {0:+0.00;-0.00;0.00} m/s / robot: {1:+0.00;-0.00;0.00} m/s, turn {2:0.00}' -f $health.output_v,$health.actual_v,$health.output_w)

                $guardStatus.ForeColor = $(if (-not $health.ready -or $health.reason -match 'stop|blocks|missing|stale') { [Drawing.Color]::Firebrick } else { [Drawing.Color]::DarkGreen })

                if (-not $state.Pump.Fresh) {

                    Disarm-Drive

                    $message.Text='Disarmed: Ubuntu bridge status is stale. Wait and re-arm.'

                    $guardStatus.Text='Ubuntu bridge status is stale. Commands stopped; wait and re-arm.'

                    $guardStatus.ForeColor=[Drawing.Color]::Firebrick

                }

            }

            if ($state.Process.HasExited) { throw 'Ubuntu controller bridge stopped; close this panel and check lab logs.' }

        } catch {

            $state.Armed=$false; $arm.Text='Arm drive'; $message.Text="Stopped: $_"

            try { Send-Drive 0 0 $false } catch { }

        }

    })

    Set-LabTheme $panel

    if ($CheckOnly) {

        if ($PreviewPath) {

            $panel.Show(); $panel.Refresh()

            $bitmap=New-Object Drawing.Bitmap($panel.Width,$panel.Height)

            try { $panel.DrawToBitmap($bitmap,(New-Object Drawing.Rectangle(0,0,$panel.Width,$panel.Height))); $bitmap.Save($PreviewPath) }

            finally { $bitmap.Dispose(); $panel.Hide() }

        }

        $state.Axes=@(0.,1.,0.,0.,0.,0.)

        $pullSpeed=(Axis-Value $speed.SelectedIndex $invertSpeed.Checked) * $driveProfile.reverse_m_s

        $state.Axes=@(0.,-1.,0.,0.,0.,0.)

        $pushSpeed=(Axis-Value $speed.SelectedIndex $invertSpeed.Checked) * $driveProfile.forward_m_s

        if ($pullSpeed -ge 0 -or $pushSpeed -le 0) { throw 'Alpha profile does not map both speed directions.' }

        [pscustomobject]@{ Controls=$panel.Controls.Count; SelectedDevice=[string]$device.SelectedItem;

            SpeedAxis=$speed.SelectedItem; SteeringAxis=$steer.SelectedItem; Armed=$state.Armed; RequireHold=$requireHold.Checked; InputPeriodMs=$timer.Interval;

            PullSpeed=$pullSpeed; PushSpeed=$pushSpeed }

        $timer.Dispose(); $panel.Dispose()

        return

    }

    try {

        $psi=New-Object Diagnostics.ProcessStartInfo

        $psi.FileName=$wslPath

        $psi.Arguments='-d VacuumRobot-24.04 -u robot --cd /home/robot/vacuum_ws --exec /bin/bash -lc "source env.sh; exec python3 tools/controller_bridge.py"'

        $psi.UseShellExecute=$false; $psi.CreateNoWindow=$true; $psi.RedirectStandardInput=$true

        $psi.RedirectStandardOutput=$true; $psi.RedirectStandardError=$true

        $state.Process=New-Object Diagnostics.Process

        $state.Process.StartInfo=$psi

        [void]$state.Process.Start()

        $state.Pump=New-Object VacuumJoystick+OutputPump($state.Process.StandardOutput)

        $bridgeErr=$state.Process.StandardError.ReadToEndAsync()

        $timer.Start()

        [void]$panel.ShowDialog()

    } finally {

        $timer.Stop(); $timer.Dispose()

        if ($state.Process) {

            try { Disarm-Drive; $state.Process.StandardInput.Close(); [void]$state.Process.WaitForExit(3000) } catch { }

            if ($state.Process.HasExited) {

                [void]$state.Pump.Completion.Wait(500)

                ($state.Pump.Log + $bridgeErr.Result) | Set-Content (Join-Path $profileRoot 'controller-bridge-last.log')

            }

            # Never terminate WSL service or unrelated Linux jobs. EOF ends the bridge;

            # if it stalls, its monotonic input watchdog emits zero within 300 ms.

            $state.Process.Dispose()

        }

        $panel.Dispose()

    }

}



## direct-drive-validation.json

{
  "date": "2026-10-07",
  "scope": "simulator only",
  "tests": {
    "camera": {
      "target_fps": 60,
      "simulation_fps": 62.56311305242787,
      "wall_fps": 60.779299121060774,
      "frames": 180
    },
    "forward": {
      "signed_displacement_m": 2.4259256627277037,
      "peak_odometry_m_s": 1.7333333325829166,
      "first_10_percent_wall_s": 0.1339447560003464,
      "time_to_90_percent_wall_s": 0.33980555700009063,
      "neutral_stop_wall_s": 0.3714044120001745
    },
    "reverse": {
      "signed_displacement_m": -2.321481239286263,
      "peak_odometry_m_s": -1.0399999992263087,
      "first_10_percent_wall_s": 0.14133213600007366,
      "time_to_90_percent_wall_s": 0.256096781999986,
      "neutral_stop_wall_s": 0.2586458340001627
    },
    "neutral_stop_without_hold_button": true,
    "disarmed_stop": true,
    "steering": {
      "peak_rad_s": 2.6666666636267404,
      "time_to_90_percent_wall_s": 0.41659782800024914
    },
    "input_timeout_stop": true
  },
  "passed": true
}


## directional-guard-validation.json

{
  "scope": "isolated test topics; no robot command output",
  "tests": {
    "clear_fast_forward": 1.5,
    "forward_slow_front": 0.6000000000000001,
    "forward_stop_front": 0.0,
    "reverse_away_from_front": -0.9,
    "reverse_stop_rear": 0.0,
    "forward_away_from_rear": 1.5,
    "padded_body_contact_stop": 0.0,
    "clear_before_timeout": 1.5,
    "stale_lidar_stop": 0.0
  },
  "passed": true
}


## Drive robot.cmd

@echo off
powershell.exe -NoProfile -STA -File "%~dp0Vacuum-Lab.ps1" -DriveNow
if errorlevel 1 pause


## Executable-Guide.md

# Vacuum Lab executable

Double-click **Vacuum Lab.exe**. The launcher has the driving, mapping, navigation, map-saving and stop controls. Click **All project files** to browse and search the project.

The file area includes the live Ubuntu workspace, models/worlds/configuration, tools, maps, session logs, validation results, rollback backups, ROS packages, the original Windows project, Ubuntu disk/image files, and the full Ubuntu backups. Hidden files are included. Double-click folders to browse. Search matches file and folder names recursively from the current folder; clear the search and refresh to return to normal browsing. Directory links are listed but recursive search does not follow them.

Use **Open** to open Windows files in their associated app and Linux files in VS Code. **Show in Explorer** reveals the file or opens the current folder. **Copy path** copies its Windows-accessible path. Permission errors are shown in the status area. Searches stop after 45 seconds and report partial results if needed; choose the workspace or a specific folder for project searches.

The EXE contains the launcher scripts, guides, previews, validation reports, executable build source, and **vacuum-workspace-source.tar.gz**, a snapshot of source, tools, maps and validation results. Only the EXE is needed to launch the app; it extracts its bundled files automatically into `%LOCALAPPDATA%\VacuumLab\app`. Find that folder through the first file-browser location. Keep editable custom profiles there or save them to a folder you choose.

The app uses your existing **VacuumRobot-24.04** WSL installation for ROS 2 and Gazebo. Ubuntu, ROS and Gazebo remain on their existing drives. Moving the EXE to another Windows PC also requires that Ubuntu installation; the EXE is not a replacement for the multi-gigabyte Ubuntu backup.

Optional command-line modes: `--drive` opens the drive workflow, `--files` opens the file area, and `--check --report <path>` checks the bundled launcher without starting simulation or motion. Normal startup opens the menu and leaves the controller disarmed.


## Executable-source/Build-Executable.ps1

param([string]$OutputRoot=(Split-Path $PSScriptRoot), [string]$BuildRoot)
$ErrorActionPreference='Stop'
if (-not $BuildRoot) { $BuildRoot=Join-Path (Split-Path $OutputRoot) 'work\executable-build' }
[void][IO.Directory]::CreateDirectory($BuildRoot)
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem
$bundlePath=Join-Path $BuildRoot 'payload.zip'
$stream=[IO.File]::Open($bundlePath,[IO.FileMode]::Create)
$zip=New-Object IO.Compression.ZipArchive($stream,[IO.Compression.ZipArchiveMode]::Create)
try {
    foreach ($file in (Get-ChildItem -LiteralPath $OutputRoot -File -Recurse -Force | Sort-Object FullName)) {
        if ($file.Extension -eq '.exe' -or $file.FullName -match '\\__pycache__\\' -or $file.Name -eq 'executable-verification.json' -or $file.Name -eq 'controller-bridge-last.log') { continue }
        $relative=$file.FullName.Substring($OutputRoot.TrimEnd('\').Length+1).Replace('\','/')
        [void][IO.Compression.ZipFileExtensions]::CreateEntryFromFile($zip,$file.FullName,$relative,[IO.Compression.CompressionLevel]::Optimal)
    }
} finally { $zip.Dispose(); $stream.Dispose() }
$compiler=Join-Path $env:WINDIR 'Microsoft.NET\Framework64\v4.0.30319\csc.exe'
$binary=Join-Path $OutputRoot 'Vacuum Lab.exe'
& $compiler /nologo /target:winexe /platform:x64 /optimize+ "/out:$binary" "/win32icon:$(Join-Path $OutputRoot 'Vacuum-Lab.ico')" /reference:System.Windows.Forms.dll /reference:System.IO.Compression.dll /reference:System.IO.Compression.FileSystem.dll "/resource:$bundlePath,VacuumLab.Payload" (Join-Path $PSScriptRoot 'Launcher.cs')
if ($LASTEXITCODE -ne 0) { throw 'Executable compilation failed.' }
Get-Item -LiteralPath $binary | Select-Object FullName,Length
Get-FileHash -LiteralPath $binary -Algorithm SHA256


## Executable-source/Launcher.cs

## Executable-source/Make-Icon.py

"""Code-native app icon: vacuum outline in the launcher's dark/cyan palette."""
from pathlib import Path
import math
import struct
import zlib

def chunk(name,data):
    return struct.pack('>I',len(data))+name+data+struct.pack('>I',zlib.crc32(name+data))

size=256
raw=bytearray()
for y in range(size):
    raw.append(0)
    for x in range(size):
        values=[]
        for ox,oy in ((.25,.25),(.75,.25),(.25,.75),(.75,.75)):
            px,py=x+ox,y+oy;r=math.hypot(px-128,py-131)
            if 70<r<88:color=(53,222,196,255)
            elif 112<px<144 and 55<py<105:color=(234,241,250,255)
            elif 80<px<176 and 190<py<196:color=(53,222,196,255)
            else:color=(11,18,32,255)
            values.append(color)
        raw.extend(round(sum(v[c] for v in values)/4) for c in range(4))
png=b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',size,size,8,6,0,0,0))+chunk(b'IDAT',zlib.compress(bytes(raw)))+chunk(b'IEND',b'')
header=struct.pack('<HHH',0,1,1)+struct.pack('<BBBBHHII',0,0,0,0,1,32,len(png),22)
(Path(__file__).resolve().parents[1]/'Vacuum-Lab.ico').write_bytes(header+png)


## file_catalog.py

"""Read-only file listings for the Windows launcher; paths arrive as JSON stdin."""
import json
import os
from pathlib import Path
import sys
import time


def catalog(request):
    root = Path(request['path'])
    query = request.get('query', '').casefold().strip()
    entries, errors = [], []

    def entry(path):
        try:
            stat = path.lstat()
            entries.append({'name': path.name, 'path': str(path),
                            'folder': path.is_dir(), 'link': path.is_symlink(),
                            'size': stat.st_size, 'modified': stat.st_mtime})
        except OSError as exc:
            errors.append(f'{path}: {exc.strerror}')

    if not root.is_dir():
        raise ValueError(f'Folder unavailable: {root}')
    if query:
        deadline = time.monotonic() + 45
        def problem(exc):
            errors.append(f'{exc.filename}: {exc.strerror}')
        for folder, dirs, files in os.walk(root, onerror=problem, followlinks=False):
            if time.monotonic() > deadline:
                errors.append('Search stopped after 45 seconds; results are partial. Choose a smaller folder.')
                break
            for name in dirs + files:
                if query in name.casefold():
                    entry(Path(folder) / name)
    else:
        for path in root.iterdir():
            entry(path)
    entries.sort(key=lambda item: (not item['folder'], item['name'].casefold(), item['path']))
    return {'entries': entries, 'errors': errors, 'path': str(root), 'query': query}


if __name__ == '__main__':
    try:
        print(json.dumps(catalog(json.load(sys.stdin))))
    except Exception as exc:
        print(json.dumps({'entries': [], 'errors': [str(exc)]}))
        sys.exit(1)


## Files-Panel.ps1

function ConvertTo-LabLinuxPath([string]$path) {

    $full = [IO.Path]::GetFullPath($path)

    if ($full -notmatch '^([A-Za-z]):\\(.*)$') { throw 'Expected a Windows drive path.' }

    '/mnt/' + $Matches[1].ToLowerInvariant() + '/' + $Matches[2].Replace('\','/')

}



function Get-LabLocations([string]$appRoot) {

    @(

        [pscustomobject]@{ Name='Launcher, guides and bundled files'; Path=(ConvertTo-LabLinuxPath $appRoot); Windows=$true }
        [pscustomobject]@{ Name='Saved launcher versions, profiles and logs'; Path=(ConvertTo-LabLinuxPath (Join-Path $env:LOCALAPPDATA 'VacuumLab')); Windows=$true }
        [pscustomobject]@{ Name='Live robot workspace - every file'; Path='/home/robot/vacuum_ws'; Windows=$false }

        [pscustomobject]@{ Name='Robot models, worlds and configuration'; Path='/home/robot/vacuum_ws/src'; Windows=$false }

        [pscustomobject]@{ Name='Robot tools and control scripts'; Path='/home/robot/vacuum_ws/tools'; Windows=$false }

        [pscustomobject]@{ Name='Saved maps'; Path='/home/robot/vacuum_ws/maps'; Windows=$false }

        [pscustomobject]@{ Name='Session logs and process state'; Path='/home/robot/vacuum_ws/.lab'; Windows=$false }

        [pscustomobject]@{ Name='Validation results and images'; Path='/home/robot/vacuum_ws/validation'; Windows=$false }

        [pscustomobject]@{ Name='Model rollback backups'; Path='/home/robot/vacuum_ws/model-backups'; Windows=$false }

        [pscustomobject]@{ Name='ROS 2 installed packages'; Path='/opt/ros/jazzy'; Windows=$false }

        [pscustomobject]@{ Name='Ubuntu filesystem'; Path='/'; Windows=$false }

        [pscustomobject]@{ Name='This project - Windows files'; Path='/mnt/c/Users/justi/Documents/Codex/2026-10-07/re'; Windows=$true }

        [pscustomobject]@{ Name='Original project and installation files'; Path='/mnt/c/Users/justi/Documents/Codex/2026-09-30/pl'; Windows=$true }

        [pscustomobject]@{ Name='Ubuntu disk and installation image'; Path='/mnt/e/WSL/VacuumRobot'; Windows=$true }

        [pscustomobject]@{ Name='Full Ubuntu backups'; Path='/mnt/f/VacuumRobotBackups'; Windows=$true }

    )

}



function Get-LabWindowsPath([string]$path, [bool]$windows) {

    if ($windows -and $path -match '^/mnt/([a-z])(?:/(.*))?$') {

        return $Matches[1].ToUpperInvariant() + ':\' + $Matches[2].Replace('/','\')

    }

    '\\wsl.localhost\VacuumRobot-24.04' + $path.Replace('/','\')

}



function Start-LabFileListing([string]$wslPath, [string]$appRoot, [string]$path, [string]$query) {

    $payload = [Convert]::ToBase64String([IO.File]::ReadAllBytes((Join-Path $appRoot 'file_catalog.py')))

    $request = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes((@{path=$path;query=$query} | ConvertTo-Json -Compress)))

    Start-Job -ArgumentList $wslPath,$payload,$request -ScriptBlock {

        param($wsl,$source,$request)

        $psi = New-Object Diagnostics.ProcessStartInfo

        $psi.FileName=$wsl; $psi.Arguments='-d VacuumRobot-24.04 -u robot --exec python3 -'

        $psi.UseShellExecute=$false; $psi.CreateNoWindow=$true

        $psi.RedirectStandardInput=$true; $psi.RedirectStandardOutput=$true; $psi.RedirectStandardError=$true

        $psi.StandardOutputEncoding=[Text.Encoding]::UTF8; $psi.StandardErrorEncoding=[Text.Encoding]::UTF8

        $proc=New-Object Diagnostics.Process; $proc.StartInfo=$psi

        try {

            [void]$proc.Start()

            $stdout=$proc.StandardOutput.ReadToEndAsync(); $stderr=$proc.StandardError.ReadToEndAsync()

            $proc.StandardInput.WriteLine("import base64, io, sys; sys.stdin=io.StringIO(base64.b64decode('$request').decode()); exec(compile(base64.b64decode('$source'), 'file_catalog.py', 'exec'))")

            $proc.StandardInput.Close()

            if (-not $proc.WaitForExit(60000)) { $proc.Kill(); throw 'File search timed out; choose a smaller folder.' }

            if (-not $stdout.Result.Trim()) { throw $stderr.Result }

            $stdout.Result

        } finally { $proc.Dispose() }

    }

}



function Show-LabFiles([string]$wslPath, [string]$appRoot, [string]$codePath, [switch]$CheckOnly, [string]$PreviewPath) {

    $filesForm=New-Object Windows.Forms.Form

    $filesForm.Text='Vacuum Lab - All project files'

    $filesForm.Size=New-Object Drawing.Size(1120,720)

    $filesForm.MinimumSize=New-Object Drawing.Size(1080,580)

    $filesForm.StartPosition='CenterParent'

    $filesForm.Font=New-Object Drawing.Font('Segoe UI',10)

    $layout=New-Object Windows.Forms.TableLayoutPanel

    $layout.Dock='Fill'; $layout.ColumnCount=1; $layout.RowCount=5; $layout.Padding=New-Object Windows.Forms.Padding(12)

    foreach ($height in @(44,44,44)) { [void]$layout.RowStyles.Add((New-Object Windows.Forms.RowStyle('Absolute',$height))) }

    [void]$layout.RowStyles.Add((New-Object Windows.Forms.RowStyle('Percent',100)))

    [void]$layout.RowStyles.Add((New-Object Windows.Forms.RowStyle('Absolute',54)))

    $filesForm.Controls.Add($layout)

    $location=New-Object Windows.Forms.ComboBox; $location.Dock='Fill'; $location.DropDownStyle='DropDownList'; $location.DisplayMember='Name'

    foreach ($root in (Get-LabLocations $appRoot)) { [void]$location.Items.Add($root) }

    $layout.Controls.Add($location,0,0)

    $pathBox=New-Object Windows.Forms.TextBox; $pathBox.Dock='Fill'; $pathBox.ReadOnly=$true

    $layout.Controls.Add($pathBox,0,1)

    $toolbar=New-Object Windows.Forms.FlowLayoutPanel; $toolbar.Dock='Fill'; $toolbar.WrapContents=$false

    $queryBox=New-Object Windows.Forms.TextBox; $queryBox.Width=245

    $toolbar.Controls.Add($queryBox)

    $buttons=@{}

    foreach ($label in @('Search','Up','Refresh','Open','Show in Explorer','Copy path')) {

        $button=New-Object Windows.Forms.Button; $button.Text=$label; $button.AutoSize=$true

        $toolbar.Controls.Add($button); $buttons[$label]=$button

    }

    $layout.Controls.Add($toolbar,0,2)

    $listing=New-Object Windows.Forms.ListView

    $listing.Dock='Fill'; $listing.View='Details'; $listing.FullRowSelect=$true; $listing.MultiSelect=$false; $listing.HideSelection=$false

    [void]$listing.Columns.Add('Name',280); [void]$listing.Columns.Add('Type',85); [void]$listing.Columns.Add('Size',85); [void]$listing.Columns.Add('Path',550)

    $layout.Controls.Add($listing,0,3)

    $help=New-Object Windows.Forms.Label; $help.Dock='Fill'

    $help.Text='Choose a location. Search matches names throughout the current folder. Hidden files are included.'

    $layout.Controls.Add($help,0,4)

    $browseState=@{Job=$null; Path=''; Root=''; Windows=$false; Query=''; Pending=$null}

    $loadFolder={ param([string]$nextPath,[string]$search)

        if ($browseState.Job) { $browseState.Pending=@($nextPath,$search); $help.Text='Waiting for current listing...'; return }

        $browseState.Path=$nextPath; $browseState.Query=$search; $location.Enabled=$false

        $pathBox.Text=Get-LabWindowsPath $nextPath $browseState.Windows

        $listing.Items.Clear(); $help.Text='Loading files from Ubuntu...'

        $browseState.Job=Start-LabFileListing $wslPath $appRoot $nextPath $search

    }

    $navigate={

        if ($listing.SelectedItems.Count) {

            $item=$listing.SelectedItems[0].Tag

            if ($item.folder) { $queryBox.Clear(); & $loadFolder $item.path '' }

            else {

                try {

                    $visiblePath=Get-LabWindowsPath $item.path $browseState.Windows

                    if (-not $browseState.Windows -and (Test-Path -LiteralPath $codePath)) {

                        Start-Process -FilePath $codePath -ArgumentList ('--remote wsl+VacuumRobot-24.04 "'+$item.path+'"') -WindowStyle Hidden

                    } else { Start-Process -FilePath $visiblePath }

                } catch { [void][Windows.Forms.MessageBox]::Show($_.Exception.Message,'Could not open file') }

            }

        }

    }

    $location.Add_SelectedIndexChanged({

        $selected=$location.SelectedItem

        $browseState.Windows=$selected.Windows; $browseState.Root=$selected.Path

        $queryBox.Clear(); & $loadFolder $selected.Path ''

    })

    $buttons['Search'].Add_Click({ & $loadFolder $browseState.Path $queryBox.Text })

    $queryBox.Add_KeyDown({ if ($_.KeyCode -eq 'Enter') { $_.SuppressKeyPress=$true; & $loadFolder $browseState.Path $queryBox.Text } })

    $buttons['Refresh'].Add_Click({ & $loadFolder $browseState.Path $browseState.Query })

    $buttons['Up'].Add_Click({

        if ($browseState.Path -ne $browseState.Root) {

            $parent=$browseState.Path.TrimEnd('/') -replace '/[^/]+$',''

            if (-not $parent) { $parent='/' }

            $queryBox.Clear(); & $loadFolder $parent ''

        }

    })

    $listing.Add_DoubleClick($navigate); $buttons['Open'].Add_Click($navigate)

    $buttons['Copy path'].Add_Click({

        $selectedPath=if ($listing.SelectedItems.Count) { Get-LabWindowsPath $listing.SelectedItems[0].Tag.path $browseState.Windows } else { $pathBox.Text }

        if ($selectedPath) { [Windows.Forms.Clipboard]::SetText($selectedPath) }

    })

    $buttons['Show in Explorer'].Add_Click({

        try {

            if ($listing.SelectedItems.Count) {

                $selectedPath=Get-LabWindowsPath $listing.SelectedItems[0].Tag.path $browseState.Windows

                Start-Process explorer.exe -ArgumentList ('/select,"'+$selectedPath+'"')

            } elseif ($pathBox.Text) { Start-Process explorer.exe -ArgumentList ('"'+$pathBox.Text+'"') }

        } catch { [void][Windows.Forms.MessageBox]::Show($_.Exception.Message,'Explorer unavailable') }

    })

    $fileTimer=New-Object Windows.Forms.Timer; $fileTimer.Interval=250

    $fileTimer.Add_Tick({

        if (-not $browseState.Job -or $browseState.Job.State -notin @('Completed','Failed','Stopped')) { return }

        try {

            $received=Receive-Job $browseState.Job -ErrorAction Stop

            $data=($received -join '') | ConvertFrom-Json

            $listing.BeginUpdate()

            foreach ($entry in $data.entries) {

                $row=New-Object Windows.Forms.ListViewItem($entry.name)

                [void]$row.SubItems.Add($(if ($entry.folder) {'Folder'} elseif ($entry.link) {'Link'} else {'File'}))

                [void]$row.SubItems.Add($(if ($entry.folder) {''} else {$entry.size.ToString('N0')}))

                [void]$row.SubItems.Add((Get-LabWindowsPath $entry.path $browseState.Windows)); $row.Tag=$entry

                [void]$listing.Items.Add($row)

            }

            $help.Text="$($listing.Items.Count) items. Double-click a folder to browse or a file to open."

            if ($data.errors.Count) { $help.Text += " $($data.errors.Count) unavailable items: " + ($data.errors -join '; ') }

        } catch { $help.Text='Listing failed: '+$_.Exception.Message }

        finally {

            $listing.EndUpdate(); Remove-Job $browseState.Job -Force; $browseState.Job=$null; $location.Enabled=$true

            if ($browseState.Pending) { $next=$browseState.Pending; $browseState.Pending=$null; & $loadFolder $next[0] $next[1] }

        }

        if ($PreviewPath) {

            $bitmap=New-Object Drawing.Bitmap($filesForm.Width,$filesForm.Height)

            try {

                $filesForm.DrawToBitmap($bitmap,(New-Object Drawing.Rectangle(0,0,$filesForm.Width,$filesForm.Height)))

                $bitmap.Save($PreviewPath,[Drawing.Imaging.ImageFormat]::Png)

            } finally { $bitmap.Dispose() }

            $filesForm.Close()

        }

    })

    Set-LabTheme $filesForm

    if ($CheckOnly) {

        $filesForm.CreateControl(); $layout.PerformLayout()

        [pscustomobject]@{ Title=$filesForm.Text; Locations=$location.Items.Count; Columns=$listing.Columns.Count; Buttons=$buttons.Count }

        $fileTimer.Dispose(); $filesForm.Dispose(); return

    }

    $filesForm.Add_Shown({ $location.SelectedIndex=0 })

    $fileTimer.Start()

    try { [void]$filesForm.ShowDialog() }

    finally {

        $fileTimer.Stop(); $fileTimer.Dispose()

        if ($browseState.Job) { Stop-Job $browseState.Job; Remove-Job $browseState.Job -Force }

        $filesForm.Dispose()

    }

}



## Furnished-room-preview.png

## Hardware-Profile.md

# Your vacuum robot

The Gazebo model now represents two NEMA 17 motors mounted below two acrylic chassis plates, one 7 cm diameter wheel on each motor, two TB6600 modules, an Arduino Mega 2560, an Orange Pi 5, an RPLIDAR C1, and the existing front camera. The wheel radius is 0.035 m in both the robot geometry and differential-drive controller. The lower chassis plate sits above the wheels and motor bodies; brackets connect the motors beneath it.

The 30 cm chassis diameter and 22 cm wheel separation are retained from the previous model. Motor body length, driver enclosure size, brackets, mass, and electronics positions are provisional because the exact NEMA 17 and TB6600 variants and your mechanical measurements were not supplied. These visual components do not implement physical stepper electronics or measure torque, missed steps, battery sag, or real motor temperature.

The simulated control path is yoke → Windows controller panel → ROS command gate → Collision Monitor → Gazebo differential-drive controller. Your intended physical architecture is Orange Pi 5 running ROS 2, Arduino Mega producing step/direction signals, and one TB6600 driving each NEMA 17. No firmware or physical motor commands are sent by this launcher.

Manual simulator limits are **1.5 m/s forward**, **0.9 m/s reverse**, and **2.4 rad/s turning**. Input and command forwarding run at 50 Hz. The dead zone starts at 5%, acceleration is 6 m/s², and odometry averaging uses three samples at 60 Hz. Arm once to drive with the yoke; center it to stop. **Require drive button** is an optional setting that starts off. STOP, disconnect, stale commands, and lidar/obstacle protection remain active. Autonomous navigation retains its existing 0.20 m/s planner limit.

At 1.5 m/s, direct-drive 70 mm wheels turn at approximately 409 RPM. This is a simulator setting, not a verified loaded speed for your particular NEMA 17/TB6600 setup.

The C1 sensor approximation uses 10 Hz scans, 500 samples per revolution, and a 0.05–12 m range. Its hardware profile records the 460800-baud UART interface. These values follow [SLAMTEC's C1 specifications](https://www.slamtec.com/en/c1/spec); Gazebo approximates its returns and does not reproduce reflectivity-dependent limits. The Arduino board outline uses the published dimensions in [Arduino's Mega 2560 product information](https://store-usa.arduino.cc/products/arduino-mega-2560-rev3).

The room is now **16 × 12 m**, with living, dining, kitchen, reading and home-office areas. The world uses a shared static body with batched materials to retain camera performance. Changes have a rollback archive in `~/vacuum_ws/model-backups/modern-hardware-20261007/before.tar.gz`.

The editable profile is `robot-profile.json`; the live ROS model is `src/vacuum_sim/urdf/vacuum.urdf.xacro`, its wheel/speed configuration is `config/controllers.yaml`, and the room generator is `tools/build_furnished_room.py`. Find these through **All project files**. Scene or robot changes need a simulation restart.

See **Robot-model-preview.png** for the assembled model and **Furnished-room-preview.png** for the room. Current drive, obstacle, navigation/map-save and executable reports are included beside this guide. Simulator shutdown now waits for its owned Gazebo child processes before releasing the single-simulator lock; startup checks use fresh ROS discovery.


## lab_controller.py

#!/usr/bin/env python3
"""User-owned, simulator-only launcher. No sudo, hardware, or global process killing."""
import argparse
import datetime
import fcntl
import json
import os
from pathlib import Path
import signal
import subprocess
import time
import yaml

WS = Path('/home/robot/vacuum_ws')
RUN = WS / '.lab'
STATE = RUN / 'processes.json'
SESSION = RUN / 'session.json'
CAMERA_RATE = 60


def say(message):
    print(message, flush=True)


def identity(pid):
    try:
        path = Path(f'/proc/{pid}')
        # comm may contain spaces, so split after its closing parenthesis.
        fields = (path / 'stat').read_text().rsplit(')', 1)[1].split()
        if fields[0] == 'Z' or path.stat().st_uid != os.getuid():
            return None
        return fields[19]  # /proc stat field 22: start time
    except (FileNotFoundError, ProcessLookupError, PermissionError):
        return None


def read_state():
    return json.loads(STATE.read_text()) if STATE.exists() else {}


def save(state):
    tmp = STATE.with_suffix('.tmp')
    tmp.write_text(json.dumps(state))
    tmp.replace(STATE)


def alive(record):
    return identity(record['pid']) == record['start']


def member_alive(pid, stamp, group):
    try:
        return identity(int(pid)) == stamp and os.getpgid(int(pid)) == group and os.getsid(int(pid)) == group
    except ProcessLookupError:
        return False


def group_members(record):
    result = {}
    if not alive(record):
        return {pid: stamp for pid, stamp in record.get('members', {}).items()
                if member_alive(pid, stamp, record['pid'])}
    for path in Path('/proc').iterdir():
        if not path.name.isdigit():
            continue
        try:
            fields = (path / 'stat').read_text().rsplit(')', 1)[1].split()
            if int(fields[2]) == record['pid'] and int(fields[3]) == record['pid']:
                stamp = identity(int(path.name))
                if stamp is not None:
                    result[path.name] = stamp
        except (FileNotFoundError, ProcessLookupError, PermissionError):
            pass
    return result


def stop(state):
    # Reverse startup order. Never signal a recycled PID or another user's process.
    for name, record in reversed(list(state.items())):
        members = group_members(record)
        if not members:
            continue
        record['members'] = members
        save(state)
        def still_running():
            return any(member_alive(pid, stamp, record['pid'])
                       for pid, stamp in members.items())
        say(f'Stopping {name}…')
        for sig, delay in ((signal.SIGTERM, 14), (signal.SIGKILL, 2)):
            if not still_running():
                break
            try:
                os.killpg(record['pid'], sig)
            except ProcessLookupError:
                break
            end = time.monotonic() + delay
            while still_running() and time.monotonic() < end:
                time.sleep(.2)
    remaining = {name: rec for name, rec in state.items() if group_members(rec)}
    save(remaining)
    (RUN / 'manual-mode').unlink(missing_ok=True)
    SESSION.unlink(missing_ok=True)
    if remaining:
        raise RuntimeError('Some lab processes did not stop. See .lab logs.')


def command(argv, timeout=20):
    return subprocess.run(['/bin/bash', '-lc', 'source env.sh; exec "$@"',
                           'vacuum-lab', *argv], cwd=WS, text=True,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                          timeout=timeout)


def launch(state, name, argv):
    with (RUN / f'{name}.log').open('w') as log:
        proc = subprocess.Popen(['/bin/bash', '-lc', 'source env.sh; exec "$@"',
                                 'vacuum-lab', *argv], cwd=WS, stdin=subprocess.DEVNULL,
                                stdout=log, stderr=subprocess.STDOUT,
                                start_new_session=True)
    state[name] = {'pid': proc.pid, 'start': identity(proc.pid)}
    if state[name]['start'] is None:
        raise RuntimeError(f'{name} exited during startup. See .lab/{name}.log.')
    save(state)


def ready(state, target, seconds=60):
    result = command(['python3', 'tools/wait_ready.py', target, '--timeout', str(seconds)], seconds + 10)
    if any(not alive(rec) for rec in state.values()):
        raise RuntimeError('A lab component exited. See .lab logs.')
    if result.returncode or 'READY' not in result.stdout:
        raise RuntimeError(f'{target} startup timed out. See .lab logs. ' + result.stdout)


def start(state, gazebo):
    settings = json.loads(SESSION.read_text()) if SESSION.exists() else {}
    if set(state) == {'simulation', 'command gate', 'mapping', 'navigation'} and all(alive(rec) for rec in state.values()) and settings.get('camera_rate') == CAMERA_RATE and not (RUN / 'manual-mode').exists():
        say('Lab is already running. Stop and restart to leave manual mode or change the views.')
        return
    if state:
        stop(state)
        state.clear()
    required = [WS / 'env.sh', WS / 'tools/run_sim.py',
                WS / 'src/vacuum_sim/config/vacuum_nav2.yaml',
                WS / 'src/vacuum_sim/config/vacuum_navigate.xml']
    if any(not path.is_file() for path in required):
        raise RuntimeError('The simulator or conservative navigation profile is missing.')
    # Refuse to combine this session with an existing manually started ROS workload.
    nodes = command(['ros2', 'node', 'list', '--no-daemon', '--spin-time', '2']).stdout
    if any(name in nodes for name in ('/slam_toolbox', '/controller_server', '/robot_state_publisher')):
        raise RuntimeError('A manual lab session is running. Stop its terminals first.')
    from prepare_lab import prepare
    checked = command(['python3', 'tools/check_lab.py'], 30)
    if checked.returncode:
        raise RuntimeError('Controller safety logic checks failed: ' + checked.stdout)
    prepare()
    try:
        say('Starting simulator and RViz…')
        launch(state, 'simulation', ['python3', 'tools/run_sim.py',
                                    f'gui:={str(gazebo).lower()}', 'rviz:=true',
                                    f'camera_rate:={CAMERA_RATE}',
                                    'rviz_config:=' + str(WS / 'src/vacuum_sim/config/view.rviz')])
        ready(state, 'scan')
        launch(state, 'command gate', ['python3', 'tools/command_gate.py'])
        say('Starting mapping…')
        launch(state, 'mapping', ['ros2', 'launch', 'vacuum_sim', 'mapping.launch.py'])
        ready(state, 'map')
        say('Starting obstacle-aware navigation…')
        launch(state, 'navigation', ['ros2', 'launch', 'vacuum_sim', 'navigation.launch.py',
                                    'params_file:=' + str(required[2])])
        ready(state, 'navigation')
        SESSION.write_text(json.dumps({'mode': 'navigation', 'camera_rate': CAMERA_RATE}))
        say('Ready. In RViz set Fixed Frame to map, then use Nav2 Goal to choose a destination.')
        say('This is mapping and destination navigation. Automatic room cleaning is not implemented.')
    except BaseException:
        say('Startup failed; stopping this launcher’s processes…')
        stop(state)
        raise


def drive(state, gazebo):
    settings = json.loads(SESSION.read_text()) if SESSION.exists() else {}
    if set(state) == {'simulation', 'command gate', 'collision guard', 'camera view'} and all(alive(rec) for rec in state.values()) and settings.get('camera_rate') == CAMERA_RATE:
        ready(state, 'collision_monitor', 15)
        say('Ready to drive. Open the controller panel; push forward, pull back to reverse.')
        return
    if state:
        stop(state)
        state.clear()
    nodes = command(['ros2', 'node', 'list', '--no-daemon', '--spin-time', '2']).stdout
    if any(name in nodes for name in ('/slam_toolbox', '/controller_server', '/robot_state_publisher', '/collision_monitor')):
        raise RuntimeError('A manual lab session is running. Stop its terminals first.')
    from prepare_lab import prepare, circle
    prepare()
    checked = command(['python3', 'tools/check_lab.py'], 30)
    if checked.returncode:
        raise RuntimeError('Controller safety checks failed: ' + checked.stdout)
    config = yaml.safe_load((WS / 'src/vacuum_sim/config/vacuum_nav2.yaml').read_text())
    guard = config['collision_monitor']['ros__parameters']
    # Static approach footprint preserves predictive braking without a costmap.
    guard['FootprintApproach']['points'] = str(circle(.17))
    guard['cmd_vel_in_topic'] = '/vacuum/selected_cmd_vel'
    guard_path = RUN / 'drive-guard.yaml'
    guard_path.write_text(yaml.safe_dump({'collision_monitor': {'ros__parameters': guard}}, sort_keys=False))
    (RUN / 'manual-mode').write_text('Direct manual driving selected.\n')
    try:
        say('Starting 60 FPS camera and driving view…')
        launch(state, 'simulation', ['python3', 'tools/run_sim.py',
                                    f'gui:={str(gazebo).lower()}', 'rviz:=false',
                                    f'camera_rate:={CAMERA_RATE}',
                                    'rviz_config:=' + str(WS / 'src/vacuum_sim/config/drive.rviz')])
        ready(state, 'scan')
        launch(state, 'command gate', ['python3', 'tools/command_gate.py'])
        launch(state, 'collision guard', ['/opt/ros/jazzy/lib/nav2_collision_monitor/collision_monitor',
                                         '--ros-args', '--params-file', str(guard_path)])
        activated = command(['python3', 'tools/activate_guard.py'], 65)
        if activated.returncode:
            raise RuntimeError(activated.stdout)
        launch(state, 'camera view', ['python3', '/opt/ros/jazzy/lib/rqt_image_view/rqt_image_view', '/camera/image_raw'])
        ready(state, 'collision_monitor', 15)
        SESSION.write_text(json.dumps({'mode': 'drive', 'camera_rate': CAMERA_RATE}))
        say('Ready to drive. Push forward, pull back to reverse. Camera target: 60 FPS.')
    except BaseException:
        say('Driving startup failed; stopping this launcher’s processes…')
        stop(state)
        raise


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['start', 'drive', 'stop', 'status', 'save-map', 'manual'])
    parser.add_argument('--gazebo', action='store_true')
    args = parser.parse_args()
    if not WS.is_dir():
        raise RuntimeError('Ubuntu vacuum workspace was not found.')
    RUN.mkdir(exist_ok=True)
    with (RUN / 'controller.lock').open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        state = read_state()
        if args.action == 'start':
            start(state, args.gazebo)
        elif args.action == 'drive':
            drive(state, args.gazebo)
        elif args.action == 'stop':
            stop(state)
            say('Lab stopped.')
        elif args.action == 'status':
            say('\n'.join(f'{name}: {"running" if alive(rec) else "stopped"}'
                          for name, rec in state.items()) or 'Lab is stopped.')
        elif args.action == 'manual':
            if set(state) == {'simulation', 'command gate', 'collision guard', 'camera view'} and all(alive(rec) for rec in state.values()):
                ready(state, 'collision_monitor', 15)
                say('Manual mode ready. Direct driving guard is active.')
                return
            if set(state) != {'simulation', 'command gate', 'mapping', 'navigation'} or any(not alive(rec) for rec in state.values()):
                raise RuntimeError('Start the lab before enabling manual drive.')
            # Switch the gate first: autonomous output cannot reach the robot,
            # even while cancellation is pending. Keep Nav2's managed nodes alive
            # so its bond manager does not tear down Collision Monitor.
            (RUN / 'manual-mode').write_text('Manual command source selected; restart to resume goals.\n')
            result = command(['ros2', 'service', 'call', '/navigate_to_pose/_action/cancel_goal',
                              'action_msgs/srv/CancelGoal', '{}'], 30)
            if result.returncode:
                raise RuntimeError('Could not cancel navigation; the gate remains stopped in manual mode. ' + result.stdout)
            ready(state, 'collision_monitor', 20)
            say('Manual mode ready. Navigation is paused until Stop lab → Start lab.')
        else:
            if not state.get('mapping') or not alive(state['mapping']):
                raise RuntimeError('Start the lab before saving a map.')
            maps = WS / 'maps'
            maps.mkdir(exist_ok=True)
            prefix = maps / datetime.datetime.now().strftime('room-%Y%m%d-%H%M%S-%f')
            result = command(['ros2', 'run', 'nav2_map_server', 'map_saver_cli',
                              '-f', str(prefix), '--ros-args', '-p', 'use_sim_time:=true',
                              '-p', 'save_map_timeout:=10.0',
                              '-p', 'map_subscribe_transient_local:=true'], 40)
            if result.returncode or not prefix.with_suffix('.yaml').is_file():
                raise RuntimeError('Map save failed: ' + result.stdout)
            say(f'Map saved: {prefix}.yaml\nSaved-map localization is a separate future workflow.')


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        say(f'Error: {exc}')
        raise SystemExit(1)


## lab-validation.json

{
  "date": "2026-10-07",
  "scope": "simulator only",
  "tests": {
    "circular_robot_goal": {
      "status": 4,
      "error_code": 0
    },
    "map_save": true,
    "manual_hold_and_release": {
      "movement_m": 0.18666664767127053,
      "released_speed_m_s": -2.105212574635046e-14
    },
    "input_timeout_stop": true,
    "bridge_eof_cleanup": true
  },
  "passed": true
}


## modern-drive-validation.json

{
  "date": "2026-10-07",
  "scope": "simulator only",
  "tests": {
    "camera": {
      "target_fps": 60,
      "simulation_fps": 62.56311305242787,
      "wall_fps": 60.779299121060774,
      "frames": 180
    },
    "forward": {
      "signed_displacement_m": 2.4259256627277037,
      "peak_odometry_m_s": 1.7333333325829166,
      "first_10_percent_wall_s": 0.1339447560003464,
      "time_to_90_percent_wall_s": 0.33980555700009063,
      "neutral_stop_wall_s": 0.3714044120001745
    },
    "reverse": {
      "signed_displacement_m": -2.321481239286263,
      "peak_odometry_m_s": -1.0399999992263087,
      "first_10_percent_wall_s": 0.14133213600007366,
      "time_to_90_percent_wall_s": 0.256096781999986,
      "neutral_stop_wall_s": 0.2586458340001627
    },
    "neutral_stop_without_hold_button": true,
    "disarmed_stop": true,
    "steering": {
      "peak_rad_s": 2.6666666636267404,
      "time_to_90_percent_wall_s": 0.41659782800024914
    },
    "input_timeout_stop": true
  },
  "passed": true
}


## Modern-Theme.ps1

$script:LabIconPath=Join-Path $PSScriptRoot 'Vacuum-Lab.ico'
function Set-LabTheme([Windows.Forms.Control]$control) {
    $background=[Drawing.ColorTranslator]::FromHtml('#0B1220')
    $surface=[Drawing.ColorTranslator]::FromHtml('#162338')
    $text=[Drawing.ColorTranslator]::FromHtml('#EAF1FA')
    $muted=[Drawing.ColorTranslator]::FromHtml('#A1B2CC')
    $control.BackColor=$background; $control.ForeColor=$text
    if ($control -is [Windows.Forms.Form]) {
        $control.Font=New-Object Drawing.Font('Segoe UI',10)
        if (Test-Path -LiteralPath $script:LabIconPath) { $control.Icon=New-Object Drawing.Icon($script:LabIconPath) }
    }
    foreach ($child in $control.Controls) { Set-LabTheme $child }
    if ($control -is [Windows.Forms.Button]) {
        $control.FlatStyle='Flat'; $control.FlatAppearance.BorderSize=0
        $control.BackColor=$surface; $control.ForeColor=$text
        $control.Cursor=[Windows.Forms.Cursors]::Hand
        $control.Font=New-Object Drawing.Font('Segoe UI Semibold',10)
        if ($control.Tag -eq 'primary' -or $control.Text -in @('Drive now','Arm drive')) {
            $control.BackColor=[Drawing.ColorTranslator]::FromHtml('#35DEC4'); $control.ForeColor=$background
        } elseif ($control.Tag -eq 'danger' -or $control.Text -match 'STOP|Stop lab') {
            $control.BackColor=[Drawing.ColorTranslator]::FromHtml('#482636'); $control.ForeColor=[Drawing.ColorTranslator]::FromHtml('#FFAFBE')
        }
        $control.FlatAppearance.MouseOverBackColor=[Drawing.ColorTranslator]::FromHtml('#31506A')
        $control.Add_SizeChanged({ Set-LabRoundedRegion $this })
        Set-LabRoundedRegion $control
    } elseif ($control -is [Windows.Forms.TextBox] -or $control -is [Windows.Forms.ComboBox] -or $control -is [Windows.Forms.NumericUpDown]) {
        $control.BackColor=$surface; $control.ForeColor=$text
        if ($control -is [Windows.Forms.TextBox]) { $control.BorderStyle='FixedSingle' }
        if ($control -is [Windows.Forms.ComboBox]) {
            $control.FlatStyle='Flat'; $control.DrawMode='OwnerDrawFixed'; $control.ItemHeight=24
            $control.Add_DrawItem({
                $shade=[Drawing.ColorTranslator]::FromHtml('#162338')
                if (($_.State -band [Windows.Forms.DrawItemState]::Selected) -ne 0) { $shade=[Drawing.ColorTranslator]::FromHtml('#29445C') }
                $brush=New-Object Drawing.SolidBrush($shade)
                try { $_.Graphics.FillRectangle($brush,$_.Bounds) } finally { $brush.Dispose() }
                $caption=$this.Text
                if ($_.Index -ge 0) {
                    $item=$this.Items[$_.Index]
                    $caption=if ($this.DisplayMember) { [string]$item.($this.DisplayMember) } else { $item.ToString() }
                }
                [Windows.Forms.TextRenderer]::DrawText($_.Graphics,$caption,$this.Font,$_.Bounds,[Drawing.ColorTranslator]::FromHtml('#EAF1FA'),([Windows.Forms.TextFormatFlags]::Left -bor [Windows.Forms.TextFormatFlags]::VerticalCenter))
                $_.DrawFocusRectangle()
            })
        }
    } elseif ($control -is [Windows.Forms.ListView]) {
        $control.BackColor=[Drawing.ColorTranslator]::FromHtml('#111C2E'); $control.ForeColor=$text
        $control.BorderStyle='None'; $control.OwnerDraw=$true
        $control.Add_DrawColumnHeader({
            $brush=New-Object Drawing.SolidBrush([Drawing.ColorTranslator]::FromHtml('#23344E'))
            try { $_.Graphics.FillRectangle($brush,$_.Bounds) } finally { $brush.Dispose() }
            [Windows.Forms.TextRenderer]::DrawText($_.Graphics,$_.Header.Text,$this.Font,$_.Bounds,[Drawing.ColorTranslator]::FromHtml('#BFD0E9'),[Windows.Forms.TextFormatFlags]::Left)
        })
        $control.Add_DrawItem({ $_.DrawDefault=$true })
        $control.Add_DrawSubItem({ $_.DrawDefault=$true })
    } elseif ($control -is [Windows.Forms.Label]) {
        if ($control.Tag -eq 'muted') { $control.ForeColor=$muted }
        if ($control.Tag -eq 'accent') { $control.ForeColor=[Drawing.ColorTranslator]::FromHtml('#35DEC4') }
    }
}

function Set-LabRoundedRegion([Windows.Forms.Control]$control) {
    if ($control.Width -lt 20 -or $control.Height -lt 20) { return }
    $path=New-Object Drawing.Drawing2D.GraphicsPath
    $diameter=16; $right=$control.Width-1; $bottom=$control.Height-1
    $path.AddArc(0,0,$diameter,$diameter,180,90)
    $path.AddArc($right-$diameter,0,$diameter,$diameter,270,90)
    $path.AddArc($right-$diameter,$bottom-$diameter,$diameter,$diameter,0,90)
    $path.AddArc(0,$bottom-$diameter,$diameter,$diameter,90,90); $path.CloseFigure()
    $previous=$control.Region; $control.Region=New-Object Drawing.Region($path)
    if ($previous) { $previous.Dispose() }; $path.Dispose()
}


## navigation.launch.py

"""Local destination navigation, with only the servers used by this robot's BT."""
from pathlib import Path
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, TimerAction
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    package = Path(get_package_share_directory('vacuum_sim'))
    params = LaunchConfiguration('params_file')
    servers = [
        ('nav2_controller', 'controller_server', [('cmd_vel', 'cmd_vel_nav')]),
        ('nav2_planner', 'planner_server', []),
        ('nav2_behaviors', 'behavior_server', [('cmd_vel', 'cmd_vel_nav')]),
        ('nav2_velocity_smoother', 'velocity_smoother', [('cmd_vel', 'cmd_vel_nav')]),
        ('nav2_collision_monitor', 'collision_monitor', []),
        ('nav2_bt_navigator', 'bt_navigator', []),
    ]
    actions = [DeclareLaunchArgument('params_file', default_value=str(package / 'config/vacuum_nav2.yaml'))]
    for pkg, name, remap in servers:
        actions.append(Node(package=pkg, executable=name, name=name,
                            parameters=[params, {'use_sim_time': True}],
                            remappings=[('/tf','tf'),('/tf_static','tf_static')] + remap,
                            output='screen'))
    # Allow process/plugin startup and local discovery before lifecycle requests.
    # All commands still pass through the gate and Collision Monitor.
    actions.append(TimerAction(period=4., actions=[Node(
        package='nav2_lifecycle_manager', executable='lifecycle_manager',
        name='lifecycle_manager_navigation', output='screen',
        parameters=[{'use_sim_time': True, 'autostart': True,
                     'node_names': [name for _, name, _ in servers],
                     'bond_timeout': 4.0}])]))
    return LaunchDescription(actions)


## navigation-check.json

{
  "map_width": 119,
  "map_height": 119,
  "known_cells": 1504,
  "occupied_cells": 36,
  "goal": [
    1.0,
    0.0
  ],
  "status": 4,
  "error_code": 0
}


## Open-Robot-Code.ps1

$ErrorActionPreference = 'Stop'
& '[REDACTED_HOME_PATH] VS Code\bin\code.cmd' --remote wsl+VacuumRobot-24.04 /home/robot/vacuum_ws


## performance-check.json

{
  "baseline_real_time_factor": 0.7747647821972173,
  "tuned_real_time_factor": 0.9058861310192173
}


## prepare_lab.py

"""Apply the 30 cm chassis to the existing Ubuntu simulator, with rollback."""

from datetime import datetime

import math

from pathlib import Path

import subprocess

import xml.etree.ElementTree as ET

import yaml



WS = Path('/home/robot/vacuum_ws')

PACKAGE = WS / 'src/vacuum_sim'

XACRO = 'http://www.ros.org/wiki/xacro'

ET.register_namespace('xacro', XACRO)





def circle(radius, count=32):

    # Circumscribed polygon: never underestimate the circular shell.

    outer = radius / math.cos(math.pi / count)

    return [[round(-.03 + outer * math.cos(2 * math.pi * i / count), 6),

             round(outer * math.sin(2 * math.pi * i / count), 6)] for i in range(count)]





def prepare_driving_views():

    launch = PACKAGE / 'launch/sim.launch.py'

    text = launch.read_text()

    text = text.replace("DeclareLaunchArgument('camera_rate', default_value='5')",

                        "DeclareLaunchArgument('camera_rate', default_value='60')")

    if "DeclareLaunchArgument('rviz_config'" not in text:

        text = text.replace("DeclareLaunchArgument('rviz', default_value='true'),",

                            "DeclareLaunchArgument('rviz', default_value='true'),\n"

                            "        DeclareLaunchArgument('rviz_config', default_value=str(package / 'config/view.rviz')),")

        text = text.replace("arguments=['-d', str(package / 'config/view.rviz')]",

                            "arguments=['-d', LaunchConfiguration('rviz_config')]")

    compile(text, str(launch), 'exec')

    model = PACKAGE / 'urdf/vacuum.urdf.xacro'

    root = ET.fromstring(model.read_text())

    rate = root.find(f'{{{XACRO}}}arg[@name="camera_rate"]')

    if rate is None:

        raise RuntimeError('The camera rate argument is missing.')

    rate.set('default', '60')

    view = PACKAGE / 'config/view.rviz'

    data = yaml.safe_load(view.read_text())

    data['Visualization Manager']['Global Options']['Frame Rate'] = 60

    drive_data = yaml.safe_load(yaml.safe_dump(data))

    drive_data['Visualization Manager']['Global Options']['Fixed Frame'] = 'odom'

    drive_data['Visualization Manager']['Displays'] = [item for item in drive_data['Visualization Manager']['Displays']

                                                       if item.get('Class') != 'rviz_default_plugins/Map']

    updates = {launch: text, model: ET.tostring(root, encoding='unicode') + '\n',

               view: yaml.safe_dump(data, sort_keys=False),

               PACKAGE / 'config/drive.rviz': yaml.safe_dump(drive_data, sort_keys=False)}

    world = PACKAGE / 'worlds/room.sdf'

    scene = ET.fromstring(world.read_text())

    # 180 Hz physics divides into 60 Hz camera/control, 30 Hz odometry, 10 Hz lidar.

    # At the 1.5 m/s limit a physics step covers about 8.3 mm.

    scene.find('world/physics/max_step_size').text = '0.005555555555555556'

    updates[world] = ET.tostring(scene, encoding='unicode') + '\n'

    changed = {path: value for path, value in updates.items() if not path.exists() or path.read_text() != value}

    if not changed:

        return

    backup = WS / 'model-backups' / datetime.now().strftime('camera60-%Y%m%d-%H%M%S-%f')

    backup.mkdir(parents=True)

    originals = {path: path.read_bytes() if path.exists() else None for path in changed}

    for path, content in originals.items():

        if content is not None:

            saved = backup / path.relative_to(PACKAGE)

            saved.parent.mkdir(parents=True, exist_ok=True)

            saved.write_bytes(content)

    try:

        for path, value in changed.items():

            path.write_text(value)

        built = subprocess.run(['/bin/bash', '-lc',

                                'source env.sh; colcon build --symlink-install --packages-select vacuum_sim'],

                               cwd=WS, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)

        if built.returncode:

            raise RuntimeError('Camera configuration build failed: ' + built.stdout[-4000:])

    except BaseException:

        for path, content in originals.items():

            if content is None:

                path.unlink(missing_ok=True)

            else:

                path.write_bytes(content)

        raise

    print('Camera target set to 60 FPS; direct driving view prepared.', flush=True)





def prepare():

    model = PACKAGE / 'urdf/vacuum.urdf.xacro'

    marker = WS / '.lab/circular-model-v1'

    prepare_driving_views()

    from apply_robot_profile import apply_profile

    apply_profile()

    if marker.exists():

        return

    root = ET.fromstring(model.read_text())

    props = {p.get('name'): p for p in root.findall(f'{{{XACRO}}}property')}

    for key in ('body_x', 'body_y', 'body_z', 'body_mass', 'wheel_separation'):

        if key not in props:

            raise RuntimeError(f'Unexpected robot model: missing {key}; no geometry changes applied.')

    props['wheel_separation'].set('value', '0.22')

    body = root.find("link[@name='base_link']")

    if body is None:

        raise RuntimeError('Expected chassis link was not found.')

    root.find("joint[@name='base_joint']/origin").set('xyz', '-0.03 0 0.08')

    inertia = body.find('inertial/inertia')

    inertia.set('ixx', '${body_mass*(3*0.15**2+body_z**2)/12}')

    inertia.set('iyy', '${body_mass*(3*0.15**2+body_z**2)/12}')

    inertia.set('izz', '${body_mass*0.15**2/2}')

    geom = body.find('collision/geometry')

    geom.clear()

    ET.SubElement(geom, 'cylinder', radius='0.15', length='${body_z}')

    plates = 0

    for visual in body.findall('visual'):

        geom = visual.find('geometry')

        box = geom.find('box')

        if box is not None and 'body_x' in box.get('size', ''):

            geom.clear()

            ET.SubElement(geom, 'cylinder', radius='0.15', length='0.004')

            plates += 1

        elif geom.find('cylinder') is not None:

            plate = geom.find('cylinder')

            if plate.get('radius') == '0.15' and plate.get('length') == '0.004':

                plates += 1

    if plates != 2:

        raise RuntimeError('Expected two acrylic plates; no geometry changes applied.')

    wheel = root.find(f'{{{XACRO}}}macro[@name="wheel"]/joint/origin')

    wheel.set('xyz', '0.03 ${sign*wheel_separation/2} ${wheel_radius-0.08}')

    root.find("joint[@name='caster_joint']/origin").set('xyz', '-0.105 0 -0.06')

    root.find("joint[@name='camera_joint']/origin").set('xyz', '0.1325 0 0.025')

    updates = {model: ET.tostring(root, encoding='unicode') + '\n'}

    controllers = PACKAGE / 'config/controllers.yaml'

    data = yaml.safe_load(controllers.read_text())

    data['diff_drive_controller']['ros__parameters']['wheel_separation'] = .22

    updates[controllers] = yaml.safe_dump(data, sort_keys=False)

    for name in ('nav2.yaml', 'vacuum_nav2.yaml'):

        path = PACKAGE / 'config' / name

        data = yaml.safe_load(path.read_text())

        for costmap in ('local_costmap', 'global_costmap'):

            params = data[costmap][costmap]['ros__parameters']

            params.pop('robot_radius', None)

            params['footprint'] = str(circle(.15))

            params['footprint_padding'] = .02

        params = data['collision_monitor']['ros__parameters']

        if name == 'vacuum_nav2.yaml':

            params['cmd_vel_in_topic'] = '/vacuum/selected_cmd_vel'

        for zone, radius in (('StopZone', .23), ('SlowZone', .35)):

            if zone in params:

                params[zone]['points'] = str(circle(radius))

        updates[path] = yaml.safe_dump(data, sort_keys=False)

    view = PACKAGE / 'config/view.rviz'

    data = yaml.safe_load(view.read_text())

    data['Visualization Manager']['Global Options']['Fixed Frame'] = 'map'

    updates[view] = yaml.safe_dump(data, sort_keys=False)

    backup = WS / 'model-backups' / datetime.now().strftime('%Y%m%d-%H%M%S-%f')

    backup.mkdir(parents=True)

    originals = {path: path.read_bytes() for path in updates}

    for path, content in originals.items():

        saved = backup / path.relative_to(PACKAGE)

        saved.parent.mkdir(parents=True, exist_ok=True)

        saved.write_bytes(content)

    try:

        for path, text in updates.items():

            path.write_text(text)

        built = subprocess.run(['/bin/bash', '-lc',

                                'source env.sh; colcon build --symlink-install --packages-select vacuum_sim'],

                               cwd=WS, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=180)

        if built.returncode:

            raise RuntimeError('Model build failed: ' + built.stdout[-5000:])

        marker.parent.mkdir(exist_ok=True)

        marker.write_text('30 cm circular body; axle offset 3 cm; wheel separation 22 cm.\n'

                          f'Previous source files: {backup}\n'

                          'Previous navigation validation used the old body; rerun for this geometry.\n')

    except BaseException:

        for path, content in originals.items():

            path.write_bytes(content)

        raise

    print(f'30 cm circular chassis prepared. Previous source saved in {backup}', flush=True)





if __name__ == '__main__':

    prepare()



## Resume-status.md

# Vacuum Lab / updated

The launcher, controller and file browser use the new dark interface. The model includes two under-chassis NEMA 17 motors, two TB6600 modules, Arduino Mega 2560, Orange Pi 5, RPLIDAR C1 and 7 cm diameter wheels.

Arm once and drive with the yoke; return to neutral to stop. A held button is optional and disabled by default. Manual simulator speed is 1.5 m/s forward, 0.9 m/s reverse and 2.4 rad/s turning. The room is 16 x 12 m with living, dining, kitchen, reading and office areas.

Current tests passed for motion, neutral/disarmed/stale-input stopping, directional obstacle escape and braking, navigation and map saving. Drive validation measured about 61 camera frames per second and 0.34 seconds to reach 90% of requested forward speed. Simulator shutdown and restart were checked after fixing orphaned Gazebo processes. See the JSON reports beside this document.

Open Vacuum Lab.exe. All project files is available in the launcher and controller. See Vacuum-Lab-Quickstart.md and Hardware-Profile.md for controls, model dimensions and provisional hardware assumptions. This launcher controls the simulator and uses the existing VacuumRobot-24.04 WSL installation.

## Robot Code.cmd

@echo off
call "[REDACTED_HOME_PATH] VS Code\bin\code.cmd" --remote wsl+VacuumRobot-24.04 /home/robot/vacuum_ws


## Robot-camera-preview.png

## Robot-Guide.md

# Robot workspace



Open **Vacuum Lab.exe** and follow **Vacuum-Lab-Quickstart.md**. Click **Drive now**, center the yoke and arm once. You can drive without holding a button; center the yoke to stop.



The model has two under-chassis NEMA 17 motors, two TB6600 modules, 7 cm wheels, Arduino Mega 2560, Orange Pi 5 and RPLIDAR C1. Read **Hardware-Profile.md** for specifications and provisional geometry. Manual simulator limits are 1.5 m/s forward, 0.9 m/s reverse and 2.4 rad/s turning. The furnished world is 16 × 12 m.



**All project files** finds source, models/world/configuration, maps, logs and backups. The Linux workspace is `/home/robot/vacuum_ws` in WSL distro `VacuumRobot-24.04`. **Open robot code** connects VS Code to it. Use the launcher for driving, mapping/navigation, map saving and shutdown. Legacy keyboard teleop publishes directly and should not run alongside the launcher's controller.



Historical setup reports are retained with their dates. **modern-drive-validation.json** covers current motion and response; **directional-guard-validation.json** covers the guard; **executable-verification.json** covers the packaged launcher and file browser.



## Robot-model-preview.png

## robot-profile.json

{
  "version": 2,
  "scope": "simulation",
  "hardware": {
    "drive_motors": "2 x NEMA 17, mounted beneath the chassis",
    "stepper_drivers": "2 x TB6600 modules",
    "microcontroller": "Arduino Mega 2560",
    "computer": "Orange Pi 5",
    "lidar": "RPLIDAR C1",
    "wheel_diameter_m": 0.07,
    "wheel_separation_m": 0.22,
    "chassis_diameter_m": 0.30,
    "motor_body_m": [0.0423, 0.040, 0.0423],
    "estimated_geometry": "Motor length, driver enclosure, mount height, mass and chassis layout are provisional; exact motor/driver variants were not supplied."
  },
  "drive": {
    "forward_m_s": 1.5,
    "reverse_m_s": 0.9,
    "turn_rad_s": 2.4,
    "acceleration_m_s2": 6.0,
    "angular_acceleration_rad_s2": 14.0,
    "input_period_s": 0.02,
    "odometry_window_samples": 3,
    "require_hold_button": false
  },
  "room": {"width_m": 16.0, "depth_m": 12.0},
  "lidar": {"min_range_m": 0.05, "max_range_m": 12.0, "scan_hz": 10.0, "samples": 500, "serial_baud": 460800}
}


## run_sim.py

#!/usr/bin/env python3
"""Run one simulator, retaining its lock until all owned child processes stop."""
import fcntl
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

workspace=Path(__file__).resolve().parents[1]
lock=(workspace/'.simulator.lock').open('a')
try:
    fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
except BlockingIOError:
    raise SystemExit('This workspace already has a simulator running. Stop its terminal first.')


def identity(pid,group):
    try:
        path=Path(f'/proc/{pid}')
        fields=(path/'stat').read_text().rsplit(')',1)[1].split()
        if fields[0]=='Z' or path.stat().st_uid!=os.getuid():return None
        if int(fields[2])!=group or int(fields[3])!=group:return None
        return fields[19]
    except (FileNotFoundError,ProcessLookupError,PermissionError):return None


def members(group):
    result={}
    for path in Path('/proc').iterdir():
        if path.name.isdigit():
            stamp=identity(path.name,group)
            if stamp is not None:result[int(path.name)]=stamp
    return result


def interrupted(signum,frame):raise KeyboardInterrupt
signal.signal(signal.SIGTERM,interrupted)
process=subprocess.Popen(['/bin/bash','-lc','source env.sh; exec "$@"','vacuum-launch',
                          'ros2','launch','vacuum_sim','sim.launch.py',*sys.argv[1:]],
                         cwd=workspace,start_new_session=True)
owned=members(process.pid)
result=0
try:
    while process.poll() is None:
        owned.update(members(process.pid))
        try:process.wait(timeout=.2)
        except subprocess.TimeoutExpired:pass
    result=process.returncode
except KeyboardInterrupt:result=130
finally:
    # Ignore repeat terminal signals while performing bounded cleanup.
    signal.signal(signal.SIGTERM,signal.SIG_IGN)
    signal.signal(signal.SIGINT,signal.SIG_IGN)
    if process.poll() is None:owned.update(members(process.pid))
    def active():
        return {pid:stamp for pid,stamp in owned.items() if identity(pid,process.pid)==stamp}
    for sig,seconds in ((signal.SIGINT,5),(signal.SIGTERM,4),(signal.SIGKILL,2)):
        if not active():break
        try:os.killpg(process.pid,sig)
        except ProcessLookupError:break
        deadline=time.monotonic()+seconds
        while active() and time.monotonic()<deadline:
            # Collect children while the original session leader is still alive.
            if process.poll() is None:owned.update(members(process.pid))
            time.sleep(.1)
    try:process.wait(timeout=1)
    except subprocess.TimeoutExpired:pass
    remaining=active()
    if remaining:
        print('Simulator cleanup incomplete; remaining owned PIDs: '+str(list(remaining)),file=sys.stderr)
        result=1
    lock.close()
sys.exit(result)


## Setup-status.md

# Robot development environment installed

Completed on 2026-09-30 on this Windows PC.

| Component | Installed / location |
|---|---|
| Windows Subsystem for Linux | 3.0.1.0, WSL 2 with WSLg |
| Ubuntu | 24.04.5 LTS, distribution `VacuumRobot-24.04` |
| Linux storage | `E:\WSL\VacuumRobot\Ubuntu-24.04` |
| Linux account | `robot`, regular sudo user with privately set password |
| ROS 2 | Jazzy desktop and development tools |
| Gazebo | Harmonic / Gazebo Sim 8.15.0, ROS bridge and ros2_control integration |
| Navigation / mapping | Nav2 1.3.13 and SLAM Toolbox 2.8.5 |
| Graphical tools | Gazebo, RViz, VS Code WSL extension |
| Graphics | Verified D3D12 hardware acceleration on RTX 3060 laptop GPU |
| Workspace | `/home/robot/vacuum_ws` |
| Backup | New tar export under `F:\VacuumRobotBackups`; see `backup-verification.json` |

## Verification

- Ubuntu boots with systemd and WSLg; package database audit is clean.
- `colcon build --symlink-install` succeeds; URDF parses and Gazebo world validates.
- Both joint-state and differential-drive controllers become active.
- Simulated movement measured **0.468 m**; velocity falls effectively to zero after command expiry.
- Lidar publishes **360 finite samples** in `lidar_link`; RGB images and camera info publish in `camera_optical_frame` at **640 × 480**.
- SLAM publishes a **119 × 119** map; Nav2 reaches **(1.0, 0.0)** with success status and zero error code.
- Map saving succeeds; ROS dependency checks report all system dependencies satisfied.
- Gazebo and RViz graphical windows open; VS Code opens `vacuum_ws [WSL: VacuumRobot-24.04]`.
- The full Ubuntu export was created and its tar structure and SHA-256 verified. See `backup-verification.json`; the archive is approximately 6.8 GiB. A separate restoration/boot test was not run.

Visual inspection of the graphical windows was not completed because its permission prompt timed out. The simulation, sensor and navigation checks above exercised the running programs through ROS interfaces. These are startup and functional checks, not extended stress tests or validation of your physical robot.

## Windows changes

WSL and Virtual Machine Platform were installed/enabled. Two existing Microsoft devices that were disabled were enabled: Virtual Drive Enumerator and Hyper-V Virtualization Infrastructure Driver. Those targeted repairs allowed WSL to start. No unrelated disk/virtual-drive devices were changed.

The new account-level `.wslconfig` caps WSL at 10 GB RAM, six processors and 2 GB swap, with a 40 GB maximum Ubuntu virtual disk, NAT networking, GUI support and the WSL firewall enabled. These settings also apply to future WSL 2 distributions under this Windows account.

Windows remains installed. No partitioning, Windows replacement, firewall exceptions, firmware flashing, robot USB attachment, passwordless sudo or physical motor commands were performed.

Start with **[Robot-Guide.md](Robot-Guide.md)** and the three `.cmd` launchers in this folder. Geometry, masses, motor behavior and sensors are explicitly provisional.


## shutdown-verification.json

{

  "Checks": [

    "Stop removes Gazebo and camera viewer processes",

    "Fresh ROS discovery is empty after shutdown",

    "Restart uses the single-simulator lock"

  ],

  "Scope": "Launcher-owned simulation",

  "Cleanup": "Tracked child process identities with bounded signal escalation",

  "Passed": true

}



## simulation-check.json

{
  "counts": {
    "scan": 127,
    "camera_info": 127,
    "odom": 378,
    "image": 54
  },
  "distance_m": 0.46804799993045726,
  "stopped_linear_m_s": 7.367153764537104e-17,
  "stopped_yaw_rad_s": 0.0,
  "scan_samples": 360,
  "finite_scan_samples": 360,
  "scan_frame": "lidar_link",
  "image_frame": "camera_optical_frame",
  "image_size": [
    640,
    480
  ],
  "camera_info_frame": "camera_optical_frame"
}


## Start-Ubuntu.ps1

$ErrorActionPreference = 'Stop'
& 'C:\Program Files\WSL\wsl.exe' -d VacuumRobot-24.04 -u robot --cd /home/robot/vacuum_ws


## Start-Vacuum-Simulation.ps1

$ErrorActionPreference = 'Stop'
& 'C:\Program Files\WSL\wsl.exe' -d VacuumRobot-24.04 -u robot --cd /home/robot/vacuum_ws --exec python3 tools/run_sim.py


## tuned-simulation-check.json

{
  "counts": {
    "scan": 183,
    "odom": 549,
    "camera_info": 92,
    "image": 91
  },
  "distance_m": 0.5430839999207747,
  "stopped_linear_m_s": 3.764349908134548e-17,
  "stopped_yaw_rad_s": 1.9721522630525296e-32,
  "scan_samples": 360,
  "finite_scan_samples": 360,
  "scan_frame": "lidar_link",
  "image_frame": "camera_optical_frame",
  "image_size": [
    320,
    240
  ],
  "camera_info_frame": "camera_optical_frame"
}


## Ubuntu Terminal.cmd

@echo off
"C:\Program Files\WSL\wsl.exe" -d VacuumRobot-24.04 -u robot --cd /home/robot/vacuum_ws


## Vacuum Lab.cmd

@echo off
powershell.exe -NoProfile -STA -File "%~dp0Vacuum-Lab.ps1"
if errorlevel 1 pause


## Vacuum Simulator - RViz only.cmd

@echo off
"C:\Program Files\WSL\wsl.exe" -d VacuumRobot-24.04 -u robot --cd /home/robot/vacuum_ws --exec python3 tools/run_sim.py gui:=false
pause


## Vacuum Simulator.cmd

@echo off
"C:\Program Files\WSL\wsl.exe" -d VacuumRobot-24.04 -u robot --cd /home/robot/vacuum_ws --exec python3 tools/run_sim.py
pause


## Vacuum-Lab.ico

## Vacuum-Lab.ps1

param([switch]$DriveNow, [switch]$Files, [switch]$CheckOnly, [string]$PreviewPath)

$ErrorActionPreference = 'Stop'

Add-Type -AssemblyName System.Windows.Forms

Add-Type -AssemblyName System.Drawing

[System.Windows.Forms.Application]::EnableVisualStyles()

$script:job = $null

$script:started = $null

$script:root = $PSScriptRoot

$wsl = 'C:\Program Files\WSL\wsl.exe'

$code = '[REDACTED_HOME_PATH] VS Code\bin\code.cmd'

$linuxRoot = '\\wsl.localhost\VacuumRobot-24.04\home\robot\vacuum_ws'

. (Join-Path $script:root 'Modern-Theme.ps1')

. (Join-Path $script:root 'Controller-Panel.ps1')

. (Join-Path $script:root 'Files-Panel.ps1')



$form = New-Object Windows.Forms.Form

$form.Text = 'Vacuum Lab'

$form.ClientSize = New-Object Drawing.Size(1060,790)

$form.FormBorderStyle='FixedSingle'; $form.MaximizeBox=$false

$form.StartPosition='CenterScreen'

$script:actionButtons=@()

function Add-LabLabel($text,$x,$y,$width,$height,$size=10,$tag='') {

    $label=New-Object Windows.Forms.Label

    $label.Text=$text; $label.SetBounds($x,$y,$width,$height); $label.Tag=$tag

    $label.Font=New-Object Drawing.Font('Segoe UI',$size)

    $form.Controls.Add($label); return $label

}

function Add-LabButton($text,$x,$y,$handler,$managed=$false,$width=166,$height=44,$tag='') {

    $button=New-Object Windows.Forms.Button

    $button.Text=$text; $button.SetBounds($x,$y,$width,$height); $button.Tag=$tag

    $button.Add_Click($handler); $form.Controls.Add($button)

    if ($managed) { $script:actionButtons += $button }

}

$null=Add-LabLabel 'VACUUM' 24 28 180 35 20 'accent'

$null=Add-LabLabel 'LAB / 02' 26 72 164 30 12 'muted'

$null=Add-LabLabel 'WORKSPACE' 26 148 166 24 9 'muted'

$null=Add-LabLabel 'ROS 2 JAZZY' 26 626 170 25 9 'accent'

$null=Add-LabLabel 'GAZEBO HARMONIC' 26 653 175 25 9 'muted'

$null=Add-LabLabel 'SIMULATION STUDIO' 244 30 450 24 10 'accent'

$null=Add-LabLabel 'Build. Drive. Explore.' 242 65 780 58 30

$null=Add-LabLabel 'Your hardware. A bigger room. Direct control.' 244 128 720 30 12 'muted'

$null=Add-LabLabel 'TAKE CONTROL' 244 174 330 26 9 'muted'

$gazebo=New-Object Windows.Forms.CheckBox

$gazebo.Text='Open the Gazebo 3D view as well'

$gazebo.SetBounds(244,400,350,30); $form.Controls.Add($gazebo)

$preview=New-Object Windows.Forms.PictureBox

$preview.SetBounds(618,174,406,256); $preview.SizeMode='Zoom'

$imagePath=Join-Path $script:root 'Furnished-room-preview.png'

if (Test-Path -LiteralPath $imagePath) { $preview.Image=[Drawing.Image]::FromFile($imagePath) }

$form.Controls.Add($preview)

$null=Add-LabLabel '16 x 12 m / FURNISHED TEST WORLD' 618 438 406 27 9 'muted'

foreach ($metric in @(@('1.5 m/s','FORWARD SPEED',244),@('70 mm','WHEEL DIAMETER',506),@('50 Hz','DIRECT INPUT',768))) {

    $null=Add-LabLabel $metric[0] $metric[2] 478 230 43 24 'accent'

    $null=Add-LabLabel $metric[1] $metric[2] 524 230 24 9 'muted'

}

$null=Add-LabLabel 'YOUR ROBOT' 244 564 760 24 9 'muted'

$null=Add-LabLabel 'NEMA 17 x2  /  TB6600 x2  /  Arduino Mega 2560' 244 592 780 27 12

$null=Add-LabLabel 'Orange Pi 5  /  RPLIDAR C1  /  Motors below the acrylic chassis' 244 620 790 26 10 'muted'

$status=Add-LabLabel 'Ready. Choose a workflow to begin.' 244 656 780 27 10 'accent'

$output=New-Object Windows.Forms.TextBox

$output.Multiline=$true; $output.ReadOnly=$true; $output.ScrollBars='Vertical'

$output.SetBounds(244,688,780,76)

$output.Text='Arm once, then drive with the yoke. Center it to stop.'

$form.Controls.Add($output)

function Start-LabAction([string]$action) {

    if ($script:job) { return }

    $files = @{}

    foreach ($name in @('lab_controller.py','run_sim.py','prepare_lab.py','controller_bridge.py','command_gate.py','check_lab.py','wait_ready.py','activate_guard.py','apply_robot_profile.py','robot-profile.json')) {
        $files[$name] = [Convert]::ToBase64String([IO.File]::ReadAllBytes((Join-Path $script:root $name)))

    }

    $source = $files | ConvertTo-Json -Compress

    $script:operation = $action

    $script:started = Get-Date

    $status.Text = "Working: $action ..."

    $output.Text = 'Ubuntu is preparing the requested action. Startup may take a few minutes.'

    foreach ($button in $script:actionButtons) { $button.Enabled = $false }

    $gazebo.Enabled = $false

    $script:job = Start-Job -ArgumentList $wsl,$source,$action,$gazebo.Checked -ScriptBlock {

        param($wslPath,$payload,$operation,$showGazebo)

        $bootstrap = @"

import base64, json, pathlib, runpy, sys

tools = pathlib.Path('/home/robot/vacuum_ws/tools')

if not tools.is_dir():

    raise SystemExit('Ubuntu vacuum workspace is missing.')

decoded = {name: base64.b64decode(value) for name, value in json.loads('$payload').items()}

for name, data in decoded.items():

    if name.endswith('.py'):

        compile(data, name, 'exec')

for name, data in decoded.items():

    p = tools / name

    if not p.exists() or p.read_bytes() != data:

        p.write_bytes(data)

p = tools / 'lab_controller.py'

sys.path.insert(0, str(tools))

sys.argv = [str(p), '$operation'] + (['--gazebo'] if '$showGazebo' == 'True' else [])

runpy.run_path(str(p), run_name='__main__')

"@

        $psi = New-Object System.Diagnostics.ProcessStartInfo

        $psi.FileName = $wslPath

        $psi.Arguments = '-d VacuumRobot-24.04 -u robot --exec python3 -'

        $psi.UseShellExecute = $false

        $psi.CreateNoWindow = $true

        $psi.RedirectStandardInput = $true

        $psi.RedirectStandardOutput = $true

        $psi.RedirectStandardError = $true

        $psi.StandardOutputEncoding = [Text.Encoding]::UTF8

        $psi.StandardErrorEncoding = [Text.Encoding]::UTF8

        $proc = New-Object System.Diagnostics.Process

        $proc.StartInfo = $psi

        try {

            [void]$proc.Start()

            $stdout = $proc.StandardOutput.ReadToEndAsync()

            $stderr = $proc.StandardError.ReadToEndAsync()

            $proc.StandardInput.Write($bootstrap)

            $proc.StandardInput.Close()

            $proc.WaitForExit()

            [pscustomobject]@{ Code = $proc.ExitCode; Text = $stdout.Result + $stderr.Result }

        } finally { $proc.Dispose() }

    }

}



Add-LabButton 'Drive now' 244 206 { Start-LabAction 'drive' } $true 350 52 'primary'

Add-LabButton 'Mapping + navigation' 244 270 { Start-LabAction 'start' } $true 350 52

Add-LabButton 'All project files' 244 334 { Show-LabFiles $wsl $script:root $code } $false 350 52

Add-LabButton 'Open robot code' 24 184 {

    if (Test-Path $code) { Start-Process -FilePath $code -ArgumentList '--remote wsl+VacuumRobot-24.04 /home/robot/vacuum_ws' -WindowStyle Hidden }

}

Add-LabButton 'Ubuntu terminal' 24 238 {

    Start-Process -FilePath $wsl -ArgumentList '-d VacuumRobot-24.04 -u robot --cd /home/robot/vacuum_ws'

}

Add-LabButton 'Save current map' 24 292 { Start-LabAction 'save-map' } $true

Add-LabButton 'Check lab status' 24 346 { Start-LabAction 'status' } $true

Add-LabButton 'Quick guide' 24 400 {

    Start-Process notepad.exe -ArgumentList ('"'+(Join-Path $script:root 'Vacuum-Lab-Quickstart.md')+'"')

}

Add-LabButton 'Robot profile' 24 454 {

    Start-Process notepad.exe -ArgumentList ('"'+(Join-Path $script:root 'Hardware-Profile.md')+'"')

}

Add-LabButton 'Stop lab' 24 710 { Start-LabAction 'stop' } $true 166 52 'danger'



$timer = New-Object System.Windows.Forms.Timer

$timer.Interval = 1000

$timer.Add_Tick({

    if (-not $script:job) { return }

    if ($script:job.State -in @('Completed', 'Failed', 'Stopped')) {

        $result = Receive-Job $script:job -ErrorAction SilentlyContinue

        $failure = $script:job.ChildJobs[0].JobStateInfo.Reason

        if ($result) {

            $output.Text = ($result.Text -replace "`r?`n", "`r`n")

            $status.Text = if ($result.Code -eq 0) { 'Done. See the details below.' } else { 'Action failed. See the details below.' }

        } else {

            $output.Text = "The action could not complete. $failure"

            $status.Text = 'Action failed.'

        }

        $openController = $script:operation -in @('manual','drive') -and $result -and $result.Code -eq 0

        Remove-Job $script:job

        $script:job = $null

        foreach ($button in $script:actionButtons) { $button.Enabled = $true }

        $gazebo.Enabled = $true

        if ($openController) { Show-ControllerPanel $wsl $script:root }

    } else {

        $elapsed = [int]((Get-Date) - $script:started).TotalSeconds

        $status.Text = "Working in Ubuntu ... ${elapsed}s"

    }

})

$form.Add_FormClosing({

    param($sender, $event)

    if ($script:job) {

        $event.Cancel = $true

        [void][Windows.Forms.MessageBox]::Show('Wait for this action to finish before closing the launcher.')

    }

})

$form.Add_Shown({ if ($DriveNow) { Start-LabAction 'drive' }; if ($Files) { Show-LabFiles $wsl $script:root $code } })

Set-LabTheme $form

if ($CheckOnly) {

    if ($PreviewPath) {

        $form.Show(); $form.Refresh()

        $bitmap=New-Object Drawing.Bitmap($form.Width,$form.Height)

        try { $form.DrawToBitmap($bitmap,(New-Object Drawing.Rectangle(0,0,$form.Width,$form.Height))); $bitmap.Save($PreviewPath) }

        finally { $bitmap.Dispose(); $form.Hide() }

    }

    [pscustomobject]@{ Title=$form.Text; Controls=$form.Controls.Count; FileBrowser=$true; Armed=$false } | ConvertTo-Json -Compress

    $timer.Dispose(); if ($preview.Image) { $preview.Image.Dispose() }; $form.Dispose()

    exit 0

}

$timer.Start()

try { [void]$form.ShowDialog() } finally { $timer.Stop(); $timer.Dispose(); if ($preview.Image) { $preview.Image.Dispose() }; $form.Dispose() }



## Vacuum-Lab-Quickstart.md

# Vacuum Lab



Open **Vacuum Lab.exe**. The dark launcher includes driving, mapping/navigation, the project file browser, a room preview and your hardware profile. **Drive now** opens the simulator, camera viewer and Alpha controller panel.



## Drive with the yoke



1. Center the yoke and release STOP.

2. Click **Arm drive** once.

3. Push forward, pull back to reverse, and rotate to steer.

4. Center the yoke to stop. **STOP / disarm** or the configured STOP button stops drive and requires arming again.



You do **not** have to hold a drive button. **Require drive button** is optional and starts unchecked. Disconnect, panel closure, lost commands and stale lidar stop input. The obstacle guard remains active. It allows reversing away from a front obstacle or moving forward away from a rear obstacle when that direction is clear.



The Alpha profile uses Y for speed, X for steering and button 3 for STOP. The dead zone is 5%. If pulling gives positive preview speed, pull back and click **Set pull = reverse**, then return to neutral. **Set neutral center** recalibrates axes. Save/load profiles preserve the optional button requirement; older profiles load without requiring a button.



**Keep drive armed when switching windows** starts enabled so you can select the camera or Gazebo while driving. Disable it to require panel focus. Changing bindings or focus behavior disarms drive. Status compares requested, guarded and actual speed and explains blocked movement.



Manual limits are **1.5 m/s forward**, **0.9 m/s reverse** and **2.4 rad/s turning**. Windows input and ROS command forwarding run at 50 Hz. Acceleration is 6 m/s²; odometry uses three samples at 60 Hz. Camera target remains 60 FPS at 320 × 240. Current performance and response measurements are in **modern-drive-validation.json**.



## Your robot and world



The model uses **two NEMA 17 motors beneath the chassis**, **two TB6600 drivers**, **Arduino Mega 2560**, **Orange Pi 5**, **RPLIDAR C1** and **7 cm diameter wheels**. Chassis diameter remains 30 cm; wheel separation is 22 cm. The model has acrylic decks, motor brackets, electronics, scanner and front camera. **Robot profile** opens **Hardware-Profile.md**, which identifies provisional dimensions and hardware limits.



The **16 × 12 m room** includes living, dining, kitchen, reading and home-office areas. Its furniture collision shapes belong to a shared static body with batched visual materials. Enable **Open the Gazebo 3D view as well** before startup for the separate world view; stop/restart to change this.



**All project files** browses/searches the live Ubuntu workspace and hidden files, source, maps, logs, validation, rollback backups, installed ROS packages, original Windows files, Ubuntu disk/image and full backups. The first location contains files extracted from the EXE. Open files, reveal them in Explorer or copy their paths.



## Mapping and shutdown



**Mapping + navigation** starts SLAM/Nav2 and RViz. Use **Nav2 Goal** in RViz to choose a destination. Autonomous navigation retains its 0.20 m/s planner limit. **Save current map** writes a unique map in `~/vacuum_ws/maps` while mapping runs. Switching workflows restarts the simulator and resets the current pose and live map; save first if needed.



**Stop lab** shuts down the launcher-owned simulation. Closing the main menu leaves the simulator running; closing the controller stops its commands. **Open robot code** connects VS Code to the workspace; **Ubuntu terminal** opens a shell.



The existing WSL distro is `VacuumRobot-24.04`, user `robot`, workspace `/home/robot/vacuum_ws`. The executable bundles the launcher and source snapshot and uses the installed Ubuntu/ROS/Gazebo environment. It controls the simulator. Actual motor/driver variants and mechanical measurements remain unverified. Physical firmware/control, cleaning coverage and docking are not implemented; 1.5 m/s is not a verified real-robot speed.



## vacuum-workspace-source.tar.gz

## validate_directional_guard.py

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



## validate_drive.py

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



## validate_lab.py

"""Test an already-running launcher lab. Commands only the simulated robot."""
import json
import math
from pathlib import Path
import subprocess
import time
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from nav2_msgs.action import NavigateToPose

WS = Path('/home/robot/vacuum_ws')
report = {'date': '2026-10-07', 'scope': 'simulator only', 'tests': {}}
rclpy.init()
node = Node('vacuum_lab_validation', parameter_overrides=[rclpy.parameter.Parameter('use_sim_time', value=True)])
odom = []
commands = []
node.create_subscription(Odometry, '/odom', odom.append, qos_profile_sensor_data)
node.create_subscription(Twist, '/vacuum/selected_cmd_vel', commands.append, 10)
client = ActionClient(node, NavigateToPose, '/navigate_to_pose')
bridge = None


def wait(predicate, seconds):
    end = time.monotonic() + seconds
    while time.monotonic() < end:
        rclpy.spin_once(node, timeout_sec=.05)
        if predicate():
            return True
    return bool(predicate())


def run(action):
    result = subprocess.run(['python3', 'tools/lab_controller.py', action], cwd=WS,
                            text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=100)
    print(result.stdout, flush=True)
    if result.returncode:
        raise RuntimeError(result.stdout)


try:
    assert wait(lambda: bool(odom) and bool(commands), 20), 'No odometry / command gate'
    assert client.wait_for_server(timeout_sec=10)
    goal = NavigateToPose.Goal()
    goal.pose.header.frame_id = 'map'
    goal.pose.header.stamp = node.get_clock().now().to_msg()
    goal.pose.pose.position.x = .6
    goal.pose.pose.orientation.w = 1.
    future = client.send_goal_async(goal)
    assert wait(future.done, 10)
    handle = future.result()
    assert handle.accepted, 'Navigation goal rejected'
    outcome = handle.get_result_async()
    if not wait(outcome.done, 100):
        cancellation = handle.cancel_goal_async()
        wait(cancellation.done, 5)
        raise RuntimeError('Navigation timed out; goal cancelled')
    result = outcome.result()
    assert result.status == 4 and result.result.error_code == 0, str(result)
    report['tests']['circular_robot_goal'] = {'status': result.status, 'error_code': result.result.error_code}
    print('Circular robot navigation goal passed.', flush=True)
    run('save-map')
    report['tests']['map_save'] = True
    run('manual')
    logfile = (WS / '.lab/bridge-validation.log').open('w')
    bridge = subprocess.Popen(['python3', 'tools/controller_bridge.py'], cwd=WS,
                              stdin=subprocess.PIPE, stdout=logfile, stderr=subprocess.STDOUT, text=True)

    def exercise(held, seconds):
        end = time.monotonic() + seconds
        while time.monotonic() < end:
            assert bridge.poll() is None, 'Manual bridge exited'
            bridge.stdin.write(json.dumps({'v': .10, 'w': 0., 'held': held}) + '\n')
            bridge.stdin.flush()
            rclpy.spin_once(node, timeout_sec=.05)
            time.sleep(.02)

    # Allow DDS services and subscriptions to connect while sending zero input.
    exercise(False, 5)
    assert abs(odom[-1].twist.twist.linear.x) < .02, 'Robot moved while disarmed'
    start = odom[-1].pose.pose.position
    before = (start.x, start.y)
    exercise(True, 3)
    end = odom[-1].pose.pose.position
    movement = math.hypot(end.x-before[0], end.y-before[1])
    assert movement > .08, f'Manual drive did not move: {movement}'
    exercise(False, 2)
    assert abs(commands[-1].linear.x) < .001 and abs(odom[-1].twist.twist.linear.x) < .02
    report['tests']['manual_hold_and_release'] = {'movement_m': movement, 'released_speed_m_s': odom[-1].twist.twist.linear.x}
    exercise(True, 1)
    # Keep the bridge alive, but stop supplying packets. Steady-time watchdog must stop.
    assert wait(lambda: abs(commands[-1].linear.x) < .001 and abs(odom[-1].twist.twist.linear.x) < .02, 4)
    report['tests']['input_timeout_stop'] = True
    bridge.stdin.close()
    bridge.wait(timeout=5)
    assert bridge.returncode == 0
    report['tests']['bridge_eof_cleanup'] = True
    report['passed'] = True
except Exception as exc:
    report['passed'] = False
    report['error'] = str(exc)
    raise
finally:
    if bridge and bridge.poll() is None:
        try:
            bridge.stdin.close()
            bridge.wait(timeout=5)
        except Exception:
            bridge.terminate()
    target = WS / 'validation/lab-20261007'
    target.mkdir(parents=True, exist_ok=True)
    (target / 'results.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2), flush=True)
    node.destroy_node()
    rclpy.shutdown()


## wait_ready.py

"""Wait for live ROS messages/services, without the ros2 CLI graph cache."""
import argparse
import os
import time
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, DurabilityPolicy, ReliabilityPolicy, qos_profile_sensor_data
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import OccupancyGrid
from lifecycle_msgs.srv import GetState


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('target', choices=['scan', 'map', 'navigation', 'collision_monitor'])
    parser.add_argument('--timeout', type=float, default=60)
    args = parser.parse_args()
    rclpy.init()
    node = Node(f'vacuum_lab_readiness_{os.getpid()}')
    received = []
    clients = {}
    pending = {}
    active = set()
    if args.target == 'scan':
        node.create_subscription(LaserScan, '/scan', received.append, qos_profile_sensor_data)
    elif args.target == 'map':
        node.create_subscription(OccupancyGrid, '/map', received.append,
                                 QoSProfile(depth=1, durability=DurabilityPolicy.TRANSIENT_LOCAL,
                                            reliability=ReliabilityPolicy.RELIABLE))
    else:
        names = ['controller_server', 'planner_server', 'collision_monitor', 'bt_navigator'] if args.target == 'navigation' else ['collision_monitor']
        clients = {name: node.create_client(GetState, f'/{name}/get_state') for name in names}
    deadline = time.monotonic() + args.timeout
    next_call = 0.
    try:
        while time.monotonic() < deadline:
            rclpy.spin_once(node, timeout_sec=.05)
            if received or (clients and len(active) == len(clients)):
                print('READY', flush=True)
                return 0
            if time.monotonic() >= next_call:
                for name, client in clients.items():
                    request = pending.get(name)
                    future = request[0] if request else None
                    if future and not future.done():
                        if time.monotonic() - request[1] < 2.:
                            continue
                        client.remove_pending_request(future)
                        future.cancel()
                        pending.pop(name)
                        active.discard(name)
                        future = None
                    if future:
                        try:
                            if future.result().current_state.id == 3:
                                active.add(name)
                            else:
                                active.discard(name)
                        except Exception:
                            active.discard(name)
                    if client.service_is_ready():
                        pending[name] = (client.call_async(GetState.Request()), time.monotonic())
                next_call = time.monotonic() + .5
        missing = sorted(set(clients)-active)
        print(f'Not ready: {args.target}' + (f'; waiting for {", ".join(missing)}' if missing else ''), flush=True)
        return 1
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    raise SystemExit(main())
