"""Convert the checked ROS model into an editable assembly without losing detail."""
import json
from pathlib import Path
import shutil
import xml.etree.ElementTree as ET

repo = Path(__file__).resolve().parents[1] / 'outputs/RobotLab'
templates = repo / 'designer/templates'
templates.mkdir(parents=True, exist_ok=True)
source = repo / 'designs/reference.urdf'
shutil.copy2(source, templates / 'reference.urdf')
root = ET.parse(source).getroot()
materials = {e.get('name'): e.find('color').get('rgba') for e in root.findall('material') if e.find('color') is not None}
base = [-.03, 0, .116]

def numbers(text):
    return [float(x) for x in text.split()]

def visual(element):
    geom = element.find('geometry')[0]
    if geom.tag == 'box':
        size = numbers(geom.get('size'))
    elif geom.tag == 'cylinder':
        size = [float(geom.get('radius')) * 2] * 2 + [float(geom.get('length'))]
    elif geom.tag == 'sphere':
        size = [float(geom.get('radius')) * 2] * 3
    else:
        raise ValueError(geom.tag)
    origin = element.find('origin')
    material = element.find('material')
    color = material.find('color') if material is not None else None
    rgba = color.get('rgba') if color is not None else materials.get(material.get('name'), '.4 .5 .6 1') if material is not None else '.4 .5 .6 1'
    return {'shape': geom.tag, 'size_m': size,
            'xyz_m': numbers(origin.get('xyz', '0 0 0')) if origin is not None else [0, 0, 0],
            'rpy_rad': numbers(origin.get('rpy', '0 0 0')) if origin is not None else [0, 0, 0], 'rgba': numbers(rgba)}

labels = {'left_nema17': 'Left NEMA 17', 'right_nema17': 'Right NEMA 17', 'left_tb6600': 'Left TB6600',
          'right_tb6600': 'Right TB6600', 'arduino_mega': 'Arduino Mega 2560', 'orange_pi5': 'Orange Pi 5',
          'lidar_link': 'RPLIDAR C1', 'camera_link': 'Front camera', 'caster': 'Caster',
          'left_wheel': 'Left drive wheel', 'right_wheel': 'Right drive wheel'}
parts = []
for link in root.findall('link'):
    name = link.get('name')
    visuals = link.findall('visual')
    if not visuals:
        continue
    if name == 'base_link':
        for index, item in enumerate(visuals):
            v = visual(item)
            id_ = item.get('name') or f'chassis_{index}'
            id_ = id_.replace('-', 'neg').replace('.', '_')
            parts.append({'id': id_, 'label': item.get('name', id_).replace('_', ' ').title(), 'kind': 'chassis' if 'chassis' in id_ else 'standoff',
                          'role': 'fixed', 'shape': v['shape'], 'size_m': v['size_m'],
                          'xyz_m': [base[i] + v['xyz_m'][i] for i in range(3)], 'rpy_rad': v['rpy_rad'],
                          'rgba': v['rgba'], 'mass_kg': .15 if 'chassis' in id_ else .01, 'collision': 'chassis' in id_,
                          'target': {'link': name, 'visual': item.get('name')}, 'visuals': []})
        continue
    joint = next(e for e in root.findall('joint') if e.find('child').get('link') == name)
    origin = joint.find('origin')
    xyz = numbers(origin.get('xyz', '0 0 0'))
    p = {'id': name, 'label': labels.get(name, name.replace('_', ' ').title()), 'kind': name,
         'role': {'left_wheel': 'left_wheel', 'right_wheel': 'right_wheel', 'lidar_link': 'lidar', 'camera_link': 'camera'}.get(name, 'fixed'),
         'shape': 'assembly', 'xyz_m': [base[i] + xyz[i] for i in range(3)],
         'rpy_rad': numbers(origin.get('rpy', '0 0 0')), 'rgba': visual(visuals[0])['rgba'],
         'size_m': visual(visuals[0])['size_m'], 'mass_kg': float(link.find('inertial/mass').get('value')),
         'collision': link.find('collision') is not None, 'target': {'link': name}, 'visuals': [visual(v) for v in visuals]}
    parts.append(p)
design = {'schema_version': 1, 'name': 'Your vacuum robot', 'parts': parts, 'notes': 'Dimensions and masses are editable estimates. Coordinates: X forward, Y left, Z up; metres and radians in JSON.'}
(repo / 'designs/default.json').write_text(json.dumps(design, indent=2) + '\n')
print(f'Created editable assembly with {len(parts)} parts.')
