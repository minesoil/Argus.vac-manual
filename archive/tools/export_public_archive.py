"""Inventory and prepare a sanitized documentation export; never change originals."""
import argparse, collections, hashlib, html, io, json, posixpath, re, shutil, zipfile
from urllib.parse import quote
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOC = {'.md','.txt','.rst','.pdf','.docx','.pptx','.xlsx','.csv','.tsv','.canvas','.canvas-llm','.fzz','.fz','.step','.stp','.stl','.shapr','.kcl','.svg','.png','.jpg','.jpeg','.webp','.gif','.mp3','.wav','.m4a','.ogg','.ino','.py','.cpp','.h','.hpp','.c','.yaml','.yml','.json','.xml','.sdf','.urdf','.xacro','.log','.html','.css','.js','.ps1','.sh','.ipynb'}

def records():
    return [json.loads(x) for x in (ROOT/'knowledge/catalog.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]

def audit():
    rs=records()
    unique={r['object_path']:r for r in rs}
    by_ext=collections.Counter()
    for r in unique.values(): by_ext[Path(r['object_path']).suffix.lower()]+=1
    print(json.dumps({'records':len(rs),'unique_objects':len(unique),'extensions':by_ext,'largest':[{'name':r['title'],'source':r['source_label'],'bytes':r['size_bytes']} for r in sorted(unique.values(),key=lambda r:r['size_bytes'],reverse=True)[:15]],'gemini_named':[{'name':r['title'],'source':r['source_label']} for r in rs if 'gemini' in (r['title']+' '+r['relative_path']).lower()],'obsidian':[{'name':r['relative_path'],'bytes':r['size_bytes']} for r in rs if r['source_label']=='obsidian-argus']},indent=2))

TEXT = {'.md','.txt','.rst','.csv','.tsv','.canvas','.canvas-llm','.kcl','.svg','.ino','.py','.cpp','.h','.hpp','.c','.yaml','.yml','.json','.xml','.sdf','.urdf','.xacro','.log','.html','.css','.js','.ts','.ps1','.sh','.toml','.cfg','.conf','.rviz','.rules','.fzp','.cs','.cmd','.bat','.cjs','.mjs','.example','.inc','.rc','.vcxproj','.filters','.sln'}
MEDIA = {'.png','.jpg','.jpeg','.webp','.gif','.bmp','.ico','.mp3','.wav','.m4a','.ogg','.step','.stp','.stl','.shapr','.iam','.ipt','.dae','.pgm','.tflite'}
OFFICE = {'.docx','.pptx','.xlsx','.fzz','.fzpz','.fz'}
RULES = [
 ('api-key',r'(?i)\b(?:AIza[\w-]{25,}|sk-(?:proj-|or-v1-)?[\w-]{20,}|gh[pousr]_[\w]{20,}|github_pat_[\w]{20,})\b'),
 ('private-key',r'-----BEGIN [^-]*PRIVATE KEY-----[\s\S]*?-----END [^-]*PRIVATE KEY-----'),
 ('email',r'(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'),
 ('home-path',r'(?i)[A-Z]:[\\/](?:Users|home)[\\/][^\s`"<>\r\n]+'),
 ('phone',r'(?<!\d)(?:\+886[- ]?|0)9\d{2}[- ]?\d{3}[- ]?\d{3}(?!\d)'),
 ('secret-assignment',r'''(?im)(?:["']?(?:password|passwd|api[_-]?key|access[_-]?token|auth[_-]?token|AP_PASS)["']?\s*[:=]\s*["'])([^"'\r\n]+)(?:["'])'''),
 ('credential-url',r'(?i)https?://[^\s<>"\]]*[?&](?:token|key|auth|signature|code|access_token)=[^\s<>"\]]+'),
 ('bearer-token',r'(?i)Bearer\s+[A-Za-z0-9._~+/=-]{16,}'),
 ('inline-password',r'''(?im)(?:root\s+password|password\s+(?:is|was)|sshpass\s+-p)\s*[:=]?\s*["']?[^\s"'`,;<>]{3,}'''),
]

def sanitize(text):
    counts=collections.Counter()
    for label,pattern in RULES:
        def replace(m):
            counts[label]+=1
            return '[REDACTED_'+label.upper().replace('-','_')+']'
        text=re.sub(pattern,replace,text)
    # Personal delivery fields in saved order notifications are not project evidence.
    text,n=re.subn(r'(?im)^(?:shipping address|delivery address|billing address|收件地址|收貨地址)\s*[:：].*$', '[REDACTED_DELIVERY_ADDRESS]',text)
    if n: counts['delivery-address']+=n
    return text,dict(counts)

def safe_path(value):
    return '/'.join(re.sub(r'[<>:"|?*\x00-\x1f]','_',p).rstrip('. ') or '_' for p in value.replace('\\','/').split('/') if p not in ('','.','..'))

def hidden_reason(r):
    rel=r['relative_path'].replace('\\','/').lower()
    if any(x in rel.split('/') for x in ('.opencode','.command-center','agent-memory','.git','.obsidian','.smart-env','.copilot')): return 'agent runtime or configuration'
    if Path(rel).name in ('config.h','.env','credentials.json','auth.json','token.json','package-lock.json','pnpm-lock.yaml','yarn.lock','skills-lock.json'): return 'local configuration or dependency lock'
    if '/fzp_cache/' in rel: return 'generated component cache'
    return None

def export(destination):
    dest=Path(destination).resolve()
    if dest.exists(): raise SystemExit('Export requires a new destination')
    dest.mkdir(parents=True)
    manifest=[]; emitted={}; totals=collections.Counter(); redactions=collections.Counter()
    for r in records():
        src=ROOT/r['object_path']; suffix=src.suffix.lower(); reason=hidden_reason(r)
        item={'id':r['id'],'title':r['title'],'source':r['source_label'],'original_name':r['relative_path'],'date':r.get('source_modified_utc'),'status':r['status'],'sha256':r['sha256']}
        if not src.is_file(): item['omitted']='source object unavailable';manifest.append(item);continue
        if reason: item['omitted']=reason;manifest.append(item);continue
        # Keep each immutable object once; alias records retain provenance.
        if r['sha256'] in emitted:
            item.update(emitted[r['sha256']]);item['duplicate']=True;manifest.append(item);continue
        relative=safe_path(r['relative_path'])
        if not Path(relative).suffix and suffix: relative+=suffix
        target='sources/'+safe_path(r['source_label'])+'/'+relative
        if any(x.get('path')==target for x in manifest): target='sources/'+safe_path(r['source_label'])+'/'+r['id']+'-'+Path(relative).name
        output=dest/target; output.parent.mkdir(parents=True,exist_ok=True)
        if suffix in TEXT:
            value,changes=sanitize(src.read_text(encoding='utf-8',errors='replace'))
            output.write_text(value,encoding='utf-8');item['path']='archive/'+target;item['redactions']=changes;redactions.update(changes)
        elif suffix in MEDIA:
            shutil.copyfile(src,output);item['path']='archive/'+target
        elif suffix in OFFICE:
            # Sanitize XML text/metadata while retaining embedded images and layout.
            if zipfile.is_zipfile(src):
                changes=collections.Counter()
                with zipfile.ZipFile(src) as zin, zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as zout:
                    for member in zin.infolist():
                        data=zin.read(member.filename)
                        if member.filename.lower().endswith(('.xml','.rels','.svg','.txt')):
                            text,found=sanitize(data.decode('utf-8',errors='replace'));changes.update(found);data=text.encode('utf-8')
                        zout.writestr(member,data)
                item['path']='archive/'+target;item['redactions']=dict(changes);redactions.update(changes)
            else: item['omitted']='opaque document container; readable extraction provided where available'
        elif suffix=='.pdf':
            # PDF byte edits corrupt offsets; publish only if the extracted body has no sensitive matches.
            extracted=ROOT/r['text_path'] if r.get('text_path') else None
            body=extracted.read_text(encoding='utf-8',errors='replace').split('\n---\n',1)[-1] if extracted and extracted.exists() else ''
            _,hits=sanitize(body)
            if body and not hits: shutil.copyfile(src,output);item['path']='archive/'+target
            else: item['omitted']='PDF needs manual privacy review; sanitized text provided'
        else: item['omitted']='executable, package, dependency, or opaque binary; not published'
        if r.get('text_path') and suffix not in TEXT:
            extracted=ROOT/r['text_path']
            if extracted.is_file():
                text=extracted.read_text(encoding='utf-8',errors='replace').split('\n---\n',1)[-1]
                text,changes=sanitize(text);redactions.update(changes)
                readpath='readable/'+r['id']+'-'+safe_path(r['title']).replace('/','_')+'.md'
                readable=dest/readpath;readable.parent.mkdir(parents=True,exist_ok=True)
                readable.write_text('# '+r['title']+'\n\nHistorical source: '+r['source_label']+'\n\n'+text,encoding='utf-8')
                item['readable']='archive/'+readpath
        emitted[r['sha256']]={k:v for k,v in item.items() if k in ('path','readable','omitted','redactions')}
        manifest.append(item)
    # Saved Gemini chats are identified from the model inside the original export.
    gemini=[]
    for item in manifest:
        if item.get('path','').endswith('.md'):
            p=dest/Path(item['path']).relative_to('archive')
            if p.is_file() and re.search(r'modelKey:\s*[^\n]*gemini',p.read_text(encoding='utf-8')): gemini.append(item['path'])
    result={'date':'2026-11-09','records':manifest,'gemini_chats':sorted(set(gemini)),'redaction_counts':redactions}
    (dest/'manifest.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    included=sum(bool(x.get('path') or x.get('readable')) for x in manifest)
    summary={'source_records':len(manifest),'represented_records':included,'exported_files':sum(1 for p in dest.rglob('*') if p.is_file()),'bytes':sum(p.stat().st_size for p in dest.rglob('*') if p.is_file()),'gemini_chats':len(set(gemini)),'redactions':redactions,'omission_reasons':collections.Counter(x['omitted'] for x in manifest if x.get('omitted'))}
    (dest/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    print(json.dumps(summary,indent=2))

def contact_sheet(destination):
    from PIL import Image,ImageOps,ImageDraw
    imgs={r['sha256']:r for r in records() if Path(r['object_path']).suffix.lower() in {'.png','.jpg','.jpeg','.webp','.bmp'}}
    dest=Path(destination);dest.mkdir(parents=True,exist_ok=True)
    for batch in range(0,len(imgs),20):
        subset=list(imgs.values())[batch:batch+20];sheet=Image.new('RGB',(1200,1050),'#eee');draw=ImageDraw.Draw(sheet)
        for i,r in enumerate(subset):
            image=Image.open(ROOT/r['object_path']).convert('RGB');image.thumbnail((290,170))
            x=(i%4)*300;y=(i//4)*210;sheet.paste(image,(x,y));draw.text((x+3,y+174),str(batch+i)+' '+r['title'][:38],fill='black')
        sheet.save(dest/f'contact-{batch//20+1}.jpg')
    print(json.dumps([{'index':i,'name':r['title'],'source':r['source_label'],'object':r['object_path']} for i,r in enumerate(imgs.values())],indent=2))

def finish(destination):
    """Add current notes, readable source indexes, and a complete accounting."""
    dest=Path(destination).resolve(); data=json.loads((dest/'manifest.json').read_text(encoding='utf-8'));rs=[r for r in data['records'] if r['source']!='project-notes'];data['records']=rs
    candidates=list((ROOT/'knowledge').glob('*.md'))+list((ROOT/'knowledge/updates').glob('*.md'))+list((ROOT/'knowledge/plans').glob('*.md'))+list((ROOT/'workspace').rglob('*.md'))
    for src in candidates:
        rel=src.relative_to(ROOT).as_posix()
        if rel.startswith(('workspace/github/','workspace/dashboard/')): continue
        target='notes/'+rel;out=dest/target;out.parent.mkdir(parents=True,exist_ok=True)
        value,changes=sanitize(src.read_text(encoding='utf-8',errors='replace'));out.write_text(value,encoding='utf-8')
        rs.append({'id':hashlib.sha256(rel.encode()).hexdigest()[:20],'title':src.name,'source':'project-notes','original_name':rel,'date':'2026-11-09','status':'dated project notes; inspect individual evidence dates','path':'archive/'+target,'redactions':changes})
    # Re-scan generated text so the final sanitizer rules apply to all copies.
    for p in dest.rglob('*'):
        if p.is_file() and p.suffix.lower() in TEXT and p.name not in ('manifest.json','summary.json'):
            value=p.read_text(encoding='utf-8',errors='replace');clean,changes=sanitize(value)
            if p.name.startswith('email-') or p.name.startswith('gmail-'):
                clean=re.sub(r'https?://[^\s<>"\)]+','[REDACTED_EMAIL_LINK]',clean)
                clean=re.sub(r'(?im)^.*(?:order number|order id|訂單編號|tracking number|運單號).*$','[REDACTED_ORDER_REFERENCE]',clean)
            if clean!=value: p.write_text(clean,encoding='utf-8')
            data['redaction_counts'].update({key:data['redaction_counts'].get(key,0)+count for key,count in changes.items()})
    # Convert saved Obsidian links where a unique/same-source target is available.
    names=collections.defaultdict(list)
    for r in rs:
        if r.get('path'): names[Path(r['original_name']).stem.lower()].append(r)
    for r in rs:
        if not r.get('path','').endswith('.md'): continue
        p=dest/Path(r['path']).relative_to('archive')
        text=p.read_text(encoding='utf-8')
        def wiki(match):
            target=match[2].split('|')[0].split('#')[0];label=match[2].split('|')[-1]
            found=names.get(Path(target).stem.lower(),[]);same=[x for x in found if x['source']==r['source']]
            found=same or found
            if not found: return match[0]
            paths={x['path'] for x in found}
            if len(paths)!=1:return match[0]
            link=posixpath.relpath(found[0]['path'],posixpath.dirname(r['path']))
            return ('!' if match[1] else '')+'['+label.replace(']','')+']('+quote(link,safe='/')+')'
        text=re.sub(r'(!?)\[\[([^\]]+)\]\]',wiki,text);p.write_text(text,encoding='utf-8')
    groups=collections.defaultdict(list)
    for r in rs: groups[r['source']].append(r)
    for source,items in groups.items():
        path=dest/'indexes'/f'{safe_path(source)}.md';path.parent.mkdir(parents=True,exist_ok=True)
        lines=['# '+source,'','Historical source collection. Older instructions are reference material, not current wiring guidance.','','| Record | Date | Available copy |','| --- | --- | --- |']
        for r in items:
            links=[]
            for label,key in [('File','path'),('Readable text','readable')]:
                if r.get(key): links.append('['+label+'](../../'+quote(r[key],safe='/')+')')
            lines.append('| '+r['title'].replace('|',' / ').replace('\n',' ')+' | '+str(r.get('date') or 'Unknown')[:10]+' | '+(' · '.join(links) or r.get('omitted','Not available'))+' |')
        path.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    overview=['# Argus archive','','Project notes, saved conversations, images and design files collected from the local Argus archive. Newer robot code remains under robot_control/.','','## Saved Gemini chats','', 'These are conversations saved by Obsidian Copilot with a Gemini model label. This is not a complete export from the Gemini app.','']
    for path in data['gemini_chats']: overview.append('- ['+Path(path).name+'](../'+quote(path,safe='/')+')')
    overview+=['','## Obsidian and other sources','','| Collection | Source records |','| --- | --- |']
    for source,items in sorted(groups.items()): overview.append('| ['+source+'](indexes/'+safe_path(source)+'.md) | '+str(len(items))+' |')
    overview+=['','## Images and diagrams','']
    seen=set()
    for r in rs:
        path=r.get('path','')
        if path and path not in seen and Path(path).suffix.lower() in {'.jpg','.jpeg','.png','.webp','.svg','.bmp'}:
            seen.add(path);overview+=['### '+r['title'],'','!['+r['title']+'](../'+quote(path,safe='/')+')','',r['source']+' · '+str(r.get('date') or 'Unknown date')[:10],'']
    overview+=['## Scope and limits','','All 1,449 original source records are accounted for in manifest.json, including aliases, redactions and omissions. The index adds current local project notes. Local immutable originals are preserved. Public copies have contact details, home paths and detected credentials removed; extracted text supplements office formats and opaque documents. Installers, downloaded packages, runtime/auth state and caches are listed as omissions rather than published. The original Gemini-only diagnostic workspace and a complete Gemini-app history were not available.','', 'Archived AI replies, A4988 guides and simulator reports are historical evidence. They do not establish the present wiring or physical test results.','', '[Export summary](summary.json) · [Complete provenance manifest](manifest.json)','']
    (dest/'README.md').write_text('\n'.join(overview),encoding='utf-8')
    (dest/'manifest.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    summary={'date':'2026-11-09','original_source_records':1449,'total_records':len(rs),'represented_records':sum(bool(r.get('path') or r.get('readable')) for r in rs),'unique_files':sum(p.is_file() for p in dest.rglob('*')),'gemini_chats':len(data['gemini_chats']),'images':len(seen),'bytes':sum(p.stat().st_size for p in dest.rglob('*') if p.is_file()),'omissions':dict(collections.Counter(r['omitted'] for r in rs if r.get('omitted'))),'redactions':data['redaction_counts']}
    (dest/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8');print(json.dumps(summary,indent=2))

def validate(destination):
    import xml.etree.ElementTree as ET
    dest=Path(destination).resolve();data=json.loads((dest/'manifest.json').read_text(encoding='utf-8'));errors=[];office=0
    for r in data['records']:
        for key in ('path','readable'):
            if r.get(key) and not (dest/Path(r[key]).relative_to('archive')).is_file(): errors.append(r['id']+': missing '+key)
    for p in dest.rglob('*'):
        if not p.is_file():continue
        if p.suffix.lower() in OFFICE and zipfile.is_zipfile(p):
            office+=1
            with zipfile.ZipFile(p) as z:
                if z.testzip():errors.append(p.name+': ZIP checksum error')
                for name in z.namelist():
                    if name.endswith(('.xml','.rels')):
                        try:ET.fromstring(z.read(name))
                        except ET.ParseError:errors.append(p.name+': malformed XML '+name)
        if p.suffix.lower() in TEXT and p.name not in ('manifest.json','summary.json'):
            text=p.read_text(encoding='utf-8',errors='replace')
            for label,pattern in RULES:
                if label in ('api-key','private-key','bearer-token','credential-url') and re.search(pattern,text): errors.append(p.name+': '+label)
    print(json.dumps({'manifest_records':len(data['records']),'office_containers_checked':office,'errors':errors},indent=2))
    if errors:raise SystemExit(1)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--export');p.add_argument('--contact-sheet');p.add_argument('--finish');p.add_argument('--validate');a=p.parse_args()
    if a.export: export(a.export)
    elif a.contact_sheet: contact_sheet(a.contact_sheet)
    elif a.finish: finish(a.finish)
    elif a.validate: validate(a.validate)
    else: audit()
