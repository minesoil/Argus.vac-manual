import pathlib,struct,collections,json,numpy as np,sys
root=pathlib.Path(__file__).resolve().parent.parent
filename=sys.argv[1] if len(sys.argv)>1 else 'shaft_pair_5mm_D.stl'
b=(root/'outputs'/filename).read_bytes(); n=struct.unpack_from('<I',b,80)[0]
assert len(b)==84+50*n
data=np.frombuffer(b,offset=84,count=n,dtype=np.dtype([('normal','<f4',3),('v','<f4',(3,3)),('attr','<u2')]))
tri=data['v'].astype(float)
verts,idx=np.unique(np.round(tri.reshape(-1,3),5),axis=0,return_inverse=True); faces=idx.reshape(-1,3)
edges=collections.Counter(); directions=collections.Counter();parent=list(range(len(verts)))
def find(v):
 while parent[v]!=v:
  parent[v]=parent[parent[v]];v=parent[v]
 return v
for t in faces:
 for a,b in zip(t,np.roll(t,-1)):
  a,b=int(a),int(b); key=tuple(sorted((a,b))); edges[key]+=1; directions[key]+=1 if a<b else -1
  parent[find(a)]=find(b)
assert all(count==2 for count in edges.values()),collections.Counter(edges.values())
assert all(d==0 for d in directions.values())
components=collections.defaultdict(list)
for i,t in enumerate(faces):components[find(int(t[0]))].append(i)
assert len(components)==2,len(components)
volumes=[]
for ids in components.values():
 t=tri[ids]; vol=np.einsum('ij,ij->i',t[:,0],np.cross(t[:,1],t[:,2])).sum()/6
 assert vol>0
 volumes.append(float(vol))
assert abs(volumes[0]-volumes[1])<.01
report={'triangles':n,'watertight':True,'consistent_orientation':True,'separate_parts':2,'mesh_volumes_mm3':volumes}
(root/'work'/('stl_validation_'+pathlib.Path(filename).stem+'.json')).write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
