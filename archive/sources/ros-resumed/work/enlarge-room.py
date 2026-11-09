from pathlib import Path
out=Path(__file__).resolve().parents[1]/'outputs'
path=out/'build_furnished_room.py';text=path.read_text(encoding='utf-8-sig')
text=text.replace("((q[0]+4)/8,(q[1]+3.5)/7)", "((q[0]+8)/16,(q[1]+6)/12)")
text=text.replace("'7 -9 8 0 .60 2.2'", "'13 -16 13 0 .62 2.2'")
text=text.replace("    def save(self):\n        # One shared", '''    def save(self):
        if self.name == 'architecture':
            # Enlarge only architecture, preserving human-scale furniture.
            for material, faces in self.mesh.faces.items():
                self.mesh.faces[material] = [([(p[0]*2, p[1]*12/7, p[2]) for p in points], normals, uvs)
                                            for points,normals,uvs in faces]
            self.collisions = [(kind,(c[0]*2,c[1]*12/7,c[2]),
                                (s[0]*2,s[1]*12/7,s[2]) if kind=='box' else s,yaw)
                               for kind,c,s,yaw in self.collisions]
        # One shared''')
poses={
    "(-.65,2.72,0,0)":"(-2.8,4.95,0,0)",
    "(-.65,1.1,0,0)":"(-2.8,3.45,0,0)",
    "(-.65,1.32,0,0)":"(-2.8,3.65,0,0)",
    "(3.65,.70,0,0)":"(7.55,3.3,0,0)",
    "(-3.7,1.55,0,0)":"(-7.65,3.4,0,0)",
    "(-2.4,-1.55,0,0)":"(-4.2,-2.0,0,0)",
    "('north',-2.4,-.78,math.pi),('south',-2.4,-2.33,0),('west',-3.47,-1.55,-math.pi/2)":"('north',-4.2,-1.23,math.pi),('south',-4.2,-2.78,0),('west',-5.27,-2.0,-math.pi/2),('east',-3.13,-2.0,math.pi/2)",
    "(2.20,-2.95,0,0)":"(5.7,-5.55,0,0)",
    "(2.2,-2.10,0,math.pi)":"(5.7,-4.65,0,math.pi)",
    "(1.30,2.72,0,0)":"(-.9,4.95,0,0)",
    "(2.90,2.82,0,0)":"(5.8,5.3,0,0)",
    "(-3.45,-2.87,0,0)":"(-7.0,-5.25,0,0)"
}
for before,after in poses.items():text=text.replace(before,after)
text=text.replace("art=Item('framed_wall_art')", "art=Item('framed_wall_art',(1.3,-2.5,0,0))")
extra='''# Kitchen cabinetry and island keep the new floor plan furnished, with wide
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

'''
text=text.replace("path=room_mesh.save('living_room')",extra+"path=room_mesh.save('living_room')")
text=text.replace('Furnished 8 x 7 m room:', 'Furnished 16 x 12 m room:')
path.write_text(text,encoding='utf-8')
path=out/'capture_room_preview.py';text=path.read_text(encoding='utf-8-sig')
text=text.replace('-2.8 -2.6 5.5 0 0.92 0.748','-7.0 -6.0 12.5 0 0.96 0.708')
text=text.replace('<far>30</far>','<far>45</far>')
path.write_text(text,encoding='utf-8')
print('16 x 12 m open-plan furnished world prepared.')
