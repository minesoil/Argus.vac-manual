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
            uv = [((q[0]+4)/8,(q[1]+3.5)/7) for q in p] if floor_uv else None
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
camera=ET.SubElement(gui,'camera',name='user_camera');element(camera,'pose','7 -9 8 0 .60 2.2')


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
        # One shared visual mesh gives the renderer one draw batch per material,
        # rather than repeating material/draw setup for each piece of furniture.
        x,y,z,yaw=self.pose
        for material,faces in self.mesh.faces.items():
            for points,normals,uvs in faces:
                transformed=[]
                for point in points:
                    q=rotate(point,yaw);transformed.append((q[0]+x,q[1]+y,q[2]+z))
                room_mesh.faces[material].append((transformed,[rotate(n,yaw) for n in normals],uvs))
        if not self.collisions:
            return
        model=ET.SubElement(world,'model',name=self.name);element(model,'static','true')
        element(model,'pose',f'{x} {y} {z} 0 0 {yaw}')
        link=ET.SubElement(model,'link',name='body')
        for i,(kind,center,size,yaw) in enumerate(self.collisions):
            collision=ET.SubElement(link,'collision',name='proxy'+str(i));element(collision,'pose',' '.join(map(str,center))+f' 0 0 {yaw}')
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

sofa=Item('three_seat_sofa',(-.65,2.72,0,0))
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

carpet=Item('woven_living_room_rug',(-.65,1.1,0,0))
# A flush decorative rug is deliberately not a raised lidar-invisible obstacle.
carpet.mesh.quad('rug',[(-1.6,-1.15,.002),(1.6,-1.15,.002),(1.6,1.15,.002),(-1.6,1.15,.002)],[(0,0),(1,0),(1,1),(0,1)])
carpet.save()

coffee=Item('rounded_coffee_table',(-.65,1.32,0,0))
coffee.box((0,0,.40),(1.25,.63,.07),'oak',collision=True,rounded=.018)
for x in (-.47,.47):
    for y in (-.21,.21):coffee.cylinder((x,y,.20),.035,.40,'charcoal',collision=True)
coffee.box((-.20,0,.45),(.28,.20,.025),'burgundy')
coffee.box((-.18,.01,.47),(.25,.18,.022),'white')
coffee.mesh.lathe((.29,.02,.44),[(.045,0),(.048,.08),(.046,.085)],'ceramic')
coffee.save()

console=Item('oak_media_console',(3.65,.70,0,0))
console.box((0,0,.35),(.45,2.05,.51),'oak',collision=True,rounded=.012)
for y in (-.67,0,.67):
    console.box((-.235,y,.35),(.02,.64,.42),'oak')
    console.box((-.251,y,.50),(.016,.16,.009),'brass')
for y in (-.82,.82):console.cylinder((0,y,.075),.035,.15,'charcoal',collision=True)
console.box((.05,0,1.37),(.04,1.65,.96),'charcoal')
console.mesh.quad('art',[(.025,.79,.93),(.025,-.79,.93),(.025,-.79,1.81),(.025,.79,1.81)],[(0,0),(1,0),(1,1),(0,1)])
for y in (-.88,.88):console.cylinder((0,y,.70),.045,.20,'charcoal')
console.save()

bookshelf=Item('bookcase',(-3.7,1.55,0,0))
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

dining=Item('dining_table',(-2.4,-1.55,0,0))
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
for n,x,y,yaw in [('north',-2.4,-.78,math.pi),('south',-2.4,-2.33,0),('west',-3.47,-1.55,-math.pi/2)]:
    chair('dining_chair_'+n,(x,y,0,yaw))

desk=Item('home_office_desk',(2.20,-2.95,0,0))
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
chair('office_chair',(2.2,-2.10,0,math.pi))

lamp=Item('floor_lamp',(1.30,2.72,0,0))
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
plant('window_plant',(2.90,2.82,0,0),1.20)
plant('entry_plant',(-3.45,-2.87,0,0),.72)

art=Item('framed_wall_art')
for x in (-.75,.40):
    art.box((x,-3.42,1.70),(.78,.04,1.04),'oak')
    art.mesh.quad('art',[(x+.35,-3.39,1.22),(x-.35,-3.39,1.22),(x-.35,-3.39,2.18),(x+.35,-3.39,2.18)],[(0,0),(1,0),(1,1),(0,1)])
art.save()

path=room_mesh.save('living_room')
model=ET.SubElement(world,'model',name='furnished_room_visuals');element(model,'static','true')
link=ET.SubElement(model,'link',name='room')
visual=ET.SubElement(link,'visual',name='furnished_room');geometry=ET.SubElement(visual,'geometry')
element(ET.SubElement(geometry,'mesh'),'uri',str(path));element(visual,'cast_shadows','false')

ET.indent(root,space='  ')
ET.ElementTree(root).write(PACKAGE/'worlds/room.sdf',encoding='utf-8',xml_declaration=True)
print(f'Furnished 8 x 7 m room: {len(world.findall("model"))} batched models, original meshes and textures.')
