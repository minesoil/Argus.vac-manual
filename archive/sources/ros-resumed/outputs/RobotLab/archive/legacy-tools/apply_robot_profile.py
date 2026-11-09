"""Apply the user's simulator geometry and response profile with rollback."""
from workspace_paths import workspace, profile_path
from datetime import datetime
import hashlib
import json
import re
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET
import yaml

WS = workspace()
PACKAGE = WS / 'src/vacuum_sim'
XACRO = 'http://www.ros.org/wiki/xacro'
ET.register_namespace('xacro', XACRO)


def apply_profile():
    source = profile_path()
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
