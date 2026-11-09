import re,pathlib
t=pathlib.Path(r'[REDACTED_HOME_PATH]
es={int(i):s for i,s in re.findall(r'#(\d+)\s*=\s*(.*?);',t,re.S)}
for f in [int(v) for v in re.findall(r'#(\d+)',es[48134])]:
 refs=[int(v) for v in re.findall(r'#(\d+)',es[f])]
 seen=set(); todo=refs[:-1]; ps=[]
 while todo:
  k=todo.pop()
  if k in seen: continue
  seen.add(k); e=es[k]
  if e.startswith('CARTESIAN_POINT'):
   try: ps.append([float(v) for v in re.search(r'\(\s*[^,]*,\s*\((.*?)\)',e,re.S).group(1).split(',')])
   except: pass
  todo.extend(int(v) for v in re.findall(r'#(\d+)',e))
 ps=[p for p in ps if len(p)==3]
 print(f,es[refs[-1]][:70],[[round(min(p[a] for p in ps),3),round(max(p[a] for p in ps),3)] for a in range(3)])
