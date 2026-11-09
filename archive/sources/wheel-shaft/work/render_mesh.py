import json,pathlib,numpy as np
from PIL import Image,ImageDraw,ImageFont
root=pathlib.Path(__file__).resolve().parent.parent
def render(source,target,title,subtitle,camera=(.35,1,.65),dimension=None):
 m=json.loads((root/source).read_text()); v=np.asarray(m['vertices']).reshape(-1,3); f=np.asarray(m['triangles']).reshape(-1,3)
 # Camera faces the set-screw flat on the positive-Y side.
 cam=np.array(camera,dtype=float); cam/=np.linalg.norm(cam)
 right=np.cross(cam,[0,0,1]);right/=np.linalg.norm(right)
 up=np.cross(right,cam)
 xy=np.column_stack([v@right,-v@up]); depth=v@cam
 lo=xy.min(axis=0); hi=xy.max(axis=0)
 size=(1600,1100); scale=min(1380/(hi-lo)[0],820/(hi-lo)[1])
 xy=(xy-(lo+hi)/2)*scale+np.array([800,590])
 pixels=np.full((size[1],size[0],3),(244,246,248),dtype=np.uint8)
 zbuffer=np.full((size[1],size[0]),-np.inf)
 light=np.array([.3,.5,1]);light/=np.linalg.norm(light)
 for tri in f[np.argsort(depth[f].mean(axis=1))]:
  pts=v[tri]; normal=np.cross(pts[1]-pts[0],pts[2]-pts[0]); n=np.linalg.norm(normal)
  if n<1e-12:continue
  normal/=n
  shade=.50+.50*max(0,float(normal@light))
  color=tuple(int(c*shade) for c in (81,166,193))
  p=xy[tri]; z=depth[tri]
  xmin=max(0,int(np.floor(p[:,0].min())));xmax=min(size[0]-1,int(np.ceil(p[:,0].max())))
  ymin=max(0,int(np.floor(p[:,1].min())));ymax=min(size[1]-1,int(np.ceil(p[:,1].max())))
  if xmax<xmin or ymax<ymin:continue
  xx,yy=np.meshgrid(np.arange(xmin,xmax+1)+.5,np.arange(ymin,ymax+1)+.5)
  den=(p[1,1]-p[2,1])*(p[0,0]-p[2,0])+(p[2,0]-p[1,0])*(p[0,1]-p[2,1])
  if abs(den)<1e-9:continue
  a=((p[1,1]-p[2,1])*(xx-p[2,0])+(p[2,0]-p[1,0])*(yy-p[2,1]))/den
  b=((p[2,1]-p[0,1])*(xx-p[2,0])+(p[0,0]-p[2,0])*(yy-p[2,1]))/den
  c=1-a-b; zz=a*z[0]+b*z[1]+c*z[2]
  subz=zbuffer[ymin:ymax+1,xmin:xmax+1]
  mask=(a>=-1e-7)&(b>=-1e-7)&(c>=-1e-7)&(zz>subz)
  subz[mask]=zz[mask];pixels[ymin:ymax+1,xmin:xmax+1][mask]=color
 img=Image.fromarray(pixels);draw=ImageDraw.Draw(img)
 fontpath='C:/Windows/Fonts/segoeui.ttf'
 font=ImageFont.truetype(fontpath,43);small=ImageFont.truetype(fontpath,25)
 draw.text((800,62),title,fill='#18323f',font=font,anchor='mm')
 draw.text((800,1037),subtitle,fill='#405563',font=small,anchor='mm')
 if dimension:
  bottom,top,label=dimension
  endpoints=np.asarray([bottom,top],dtype=float)
  projected=np.column_stack([endpoints@right,-endpoints@up])
  projected=(projected-(lo+hi)/2)*scale+np.array([800,590])
  dx=float(min(projected[:,0])-185)
  y1,y2=float(projected[0,1]),float(projected[1,1])
  for p in projected:draw.line([(dx-12,float(p[1])),(float(p[0])-12,float(p[1]))],fill='#b07824',width=2)
  draw.line([(dx,y1),(dx,y2)],fill='#b07824',width=3)
  draw.polygon([(dx,y1),(dx-7,y1-14),(dx+7,y1-14)],fill='#b07824')
  draw.polygon([(dx,y2),(dx-7,y2+14),(dx+7,y2+14)],fill='#b07824')
  draw.text((dx-12,(y1+y2)/2),label,fill='#8f5f18',font=small,anchor='rm')
 img.save(root/target)
if __name__=='__main__':
 import sys
 if '--hex40uniform' in sys.argv:
  render('work/pair_mesh_hex_40mm_uniform13.json','outputs/shaft_pair_direct_hex_M3_40mm_uniform13.png','40 mm wheel shafts with uniform 13 mm bodies','13 mm body diameter  |  Smooth root and flange blends  |  Captive M3 nut',camera=(.45,1,.65),dimension=([0,0,2.7],[0,0,42.7],'40 mm'))
 elif '--hex40widebase' in sys.argv:
  render('work/pair_mesh_hex_40mm_13mm_base.json','outputs/shaft_pair_direct_hex_M3_40mm_13mm_base.png','40 mm wheel shafts with 13 mm lower sections','Lower section: 13 mm diameter x 10 mm height  |  5.6 mm bottom bore',camera=(.45,1,.65),dimension=([0,0,2.7],[0,0,42.7],'40 mm'))
 elif '--hex40reinforced' in sys.argv:
  render('work/pair_mesh_hex_40mm_reinforced.json','outputs/shaft_pair_direct_hex_M3_40mm_reinforced.png','40 mm wheel shafts with thicker bodies','12 mm exposed body  |  Smooth transitions  |  Original bearing seat retained',camera=(.45,1,.65),dimension=([0,0,2.7],[0,0,42.7],'40 mm'))
 elif '--hex40' in sys.argv:
  render('work/pair_mesh_hex_40mm.json','outputs/shaft_pair_direct_hex_M3_40mm.png','40 mm direct-hex wheel shafts','40 mm from mounting base top to hex tip  |  Captive M3 nut  |  Two copies',camera=(.45,1,.65),dimension=([0,0,2.7],[0,0,42.7],'40 mm'))
 elif '--hex' in sys.argv:
  render('work/pair_mesh_hex.json','outputs/shaft_pair_direct_hex_M3.png','Direct wheel mount with captive M3 nuts','11.8 mm hex  |  5.8 mm engagement length  |  5.6 mm bottom bore',camera=(.6,1,.8))
  render('work/detail_mesh_hex.json','work/hex_detail.png','Slide an M3 nut into the side pocket','Insert the nut first, seat the wheel on the hex, then install the retaining screw',camera=(1,.5,.85))
 elif '--v2' in sys.argv:
  render('work/pair_mesh_v2.json','outputs/shaft_pair_shorter_reinforced.png','Shorter shafts with reinforced roots','19.5 mm shaft  |  18 mm adapter clearance  |  5.6 mm bottom bore')
  render('work/underside_mesh_v2.json','work/underside_preview_v2.png','Wider bottom bore','5.6 mm diameter  |  Original bore depth and mounting holes retained')
 else:
  render('work/original_mesh.json','work/original_preview.png','Original output shaft','Original Torx end and gearbox mounting base')
  if (root/'work/pair_mesh.json').exists():
   render('work/pair_mesh.json','outputs/shaft_pair_preview.png','Two output shafts with 5 mm D-shaped ends','24 mm shaft length  |  15 mm set-screw flat  |  10 mm gap')
