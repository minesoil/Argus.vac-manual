import sys,pathlib,json
sys.path.insert(0,str(pathlib.Path(__file__).parent/'cadlibs'))
import cadquery as cq
src=r'[REDACTED_HOME_PATH]
model=cq.importers.importStep(src)
solids=model.solids().vals()
def bounds(s):
 b=s.BoundingBox(); return [round(v,4) for v in (b.xmin,b.xmax,b.ymin,b.ymax,b.zmin,b.zmax)]
for i,s in enumerate(solids):
 print(i,'bounds',bounds(s),'volume',s.Volume(),'faces',len(s.Faces()))
 if abs(s.Center().x)<1 and abs(s.Center().y)<1 and s.BoundingBox().zmax>14 and s.BoundingBox().zmax<15:
  print('OUTPUT CANDIDATE',i)
  for j,f in enumerate(s.Faces()):
   print('face',j,f.geomType(),'area',round(f.Area(),3),'bounds',bounds(f))
  cq.exporters.export(s,'work/original_output.step')
  cq.exporters.export(s,'work/original_output.stl',tolerance=0.02,angularTolerance=0.05)
