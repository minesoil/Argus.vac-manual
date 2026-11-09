"""Generate a fallback listing pinned to a committed public repository snapshot."""
import argparse,json,subprocess
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('repository');p.add_argument('output');a=p.parse_args()
ref=subprocess.check_output(['git','-C',a.repository,'rev-parse','HEAD'],text=True).strip()
raw=subprocess.check_output(['git','-C',a.repository,'ls-tree','-rlz','HEAD'])
files=[]
for item in raw.split(b'\0'):
    if not item:continue
    info,name=item.split(b'\t',1);parts=info.split()
    if parts[1]==b'blob':files.append({'path':name.decode('utf-8'),'size':int(parts[3])})
Path(a.output).write_text(json.dumps({'ref':ref,'files':files},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'ref':ref,'files':len(files)}))
