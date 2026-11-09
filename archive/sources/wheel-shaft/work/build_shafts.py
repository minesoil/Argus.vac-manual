import sys,pathlib,json,math
root=pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0,str(root/'work/cadlibs'))
import cadquery as cq
import trimesh
import numpy as np
out=root/'outputs'; out.mkdir(exist_ok=True)
original=cq.importers.importStep(str(root/'work/original_output.step')).solids().val()
# The STEP source's Torx starts at the top of the 8 mm journal.
z_join=11.166664
collar_height=1.5
shaft_length=24.0
shaft_radius=2.5
flat_depth=0.5
flat_length=15.0
z_shaft=z_join+collar_height
z_tip=z_shaft+shaft_length
# Retain the complete original mechanism below the Torx interface.
lower_half=cq.Solid.makeBox(100,100,z_join+50,cq.Vector(-50,-50,-50))
base=original.intersect(lower_half).clean()
# Cap the existing 5.4 mm underside bore at its original depth. The
# replacement 5 mm output cannot join the original annular journal alone.
collar=cq.Solid.makeCylinder(3.999996,collar_height,cq.Vector(0,0,z_join))
rod=cq.Solid.makeCylinder(shaft_radius,shaft_length,cq.Vector(0,0,z_shaft))
# A small lead-in at the tip helps a nominal 5 mm coupler slide on.
rod=cq.Workplane('XY').newObject([rod]).edges('>Z').chamfer(0.25).val()
flat=cq.Solid.makeBox(20,10,flat_length+1,cq.Vector(-10,shaft_radius-flat_depth,z_tip-flat_length))
rod=rod.cut(flat).clean()
part=base.fuse(collar,rod).clean()
assert part.isValid() and len(part.Solids())==1
removed_below=base.cut(part).Volume()
added_below=part.intersect(lower_half).cut(base).Volume()
assert abs(removed_below)<1e-6 and abs(added_below)<1e-6
# Keep original gearbox mounting features exact; place both bottoms on Z=0.
bottom=part.BoundingBox().zmin
one=part.translate(cq.Vector(0,0,-bottom))
pitch=40.0
two=one.translate(cq.Vector(pitch,0,0))
pair=cq.Compound.makeCompound([one,two])
assert pair.isValid() and len(pair.Solids())==2
step=out/'shaft_pair_5mm_D.step'
stl=out/'shaft_pair_5mm_D.stl'
cq.exporters.export(pair,str(step))
cq.exporters.export(pair,str(stl),tolerance=0.01,angularTolerance=0.04)
reloaded=cq.importers.importStep(str(step)).solids().vals()
assert len(reloaded)==2 and all(s.isValid() for s in reloaded)
mesh=trimesh.load_mesh(str(stl))
pieces=mesh.split(only_watertight=False)
assert mesh.is_watertight and len(pieces)==2
assert all(p.is_volume for p in pieces)
assert abs(pieces[0].volume-pieces[1].volume)<0.01
report={
 'source':'planetary-gearbox-+slim.step / output (regular fit)',
 'shaft_diameter_mm':5.0,'shaft_length_from_collar_mm':shaft_length,
 'flat_depth_mm':flat_depth,'flat_length_from_tip_mm':flat_length,
 'tip_chamfer_mm':0.25,'replacement_collar_diameter_mm':7.999992,
 'replacement_collar_height_mm':collar_height,
 'copy_center_spacing_mm':pitch,'copy_gap_mm':pitch-one.BoundingBox().xlen,
 'quantity':2,'units':'mm','part_height_mm':one.BoundingBox().zlen,
 'cad_valid':True,'step_reimport_solids':len(reloaded),'stl_watertight':mesh.is_watertight,
 'stl_disconnected_parts':len(pieces),'original_lower_geometry_preserved':True,
 'physical_fit_tested':False,
}
(root/'work/validation.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
# A faithful mesh rendering of the final exported deliverable.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
fig=plt.figure(figsize=(12,7.5),facecolor='#f4f6f8')
ax=fig.add_subplot(111,projection='3d',computed_zorder=False)
ax.set_facecolor('#f4f6f8')
for p in pieces:
 normals=p.face_normals
 light=np.array([-0.4,-0.6,0.75]); light/=np.linalg.norm(light)
 intensity=0.42+0.58*np.maximum(0,normals@light)
 colors=np.column_stack([0.19*intensity+0.12,0.52*intensity+0.12,0.69*intensity+0.12,np.ones(len(intensity))])
 coll=Poly3DCollection(p.triangles,facecolors=colors,edgecolors='none',linewidths=0,zsort='average')
 ax.add_collection3d(coll)
lo,hi=mesh.bounds
ax.set_xlim(lo[0]-3,hi[0]+3); ax.set_ylim(lo[1]-3,hi[1]+3); ax.set_zlim(0,hi[2]+3)
ax.set_box_aspect((hi[0]-lo[0]+6,hi[1]-lo[1]+6,hi[2]+3))
ax.view_init(elev=25,azim=65)
ax.set_axis_off()
fig.suptitle('Two output shafts · 5 mm D-shaft ends',fontsize=20,color='#172f3c',y=0.94)
fig.text(0.5,0.055,'24 mm shaft length  •  0.5 mm-deep flat over final 15 mm  •  10 mm gap between parts',ha='center',fontsize=11,color='#405563')
fig.subplots_adjust(left=0,right=1,bottom=.07,top=.9)
fig.savefig(out/'shaft_pair_preview.png',dpi=170,facecolor=fig.get_facecolor())
