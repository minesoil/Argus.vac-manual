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
    # 300 Hz physics divides evenly into 60 Hz camera, 50 Hz drive, and 10 Hz lidar.
    # It also lowers CPU load compared with the previous 500 Hz simulation.
    scene.find('world/physics/max_step_size').text = '0.0033333333333333335'
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
