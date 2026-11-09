import re, pathlib, json
t=pathlib.Path(r'[REDACTED_HOME_PATH]
entities={int(i):s for i,s in re.findall(r'#(\d+)\s*=\s*(.*?);',t,re.S)}
for i,s in entities.items():
    if not s.startswith('MANIFOLD_SOLID_BREP'): continue
    seen=set(); pending=[i]; points=[]
    while pending:
        k=pending.pop()
        if k in seen: continue
        seen.add(k); e=entities[k]
        if e.startswith('CARTESIAN_POINT'):
            m=re.search(r'\(\s*[^,]*,\s*\((.*?)\)',e,re.S)
            if m:
                try: points.append([float(v) for v in m.group(1).split(',')])
                except ValueError: pass
        pending.extend(int(v) for v in re.findall(r'#(\d+)',e))
    p=[p for p in points if len(p)==3]
    print(i,s,'bounds',[[round(min(x[a] for x in p),4),round(max(x[a] for x in p),4)] for a in range(3)])
    if 'output' in s:
        print('z levels',sorted(set(round(x[2],4) for x in p)))
