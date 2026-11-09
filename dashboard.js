'use strict';
// Dependency-free static viewer. GitHub is the source; this page cannot drive Argus.
const REPO = 'minesoil/Argus.vac-manual';
const BRANCH = 'main';
const API = `https://api.github.com/repos/${REPO}`;
const DEFAULT_FILE = 'robot_control/PROJECT-STATUS.md';
const CACHE_KEY = `argus-tree-v1:${REPO}:${BRANCH}`;
const MAX_TEXT = 1024 * 1024;
const $ = id => document.getElementById(id);
const state = { files: [], ref: BRANCH, selected: '', text: '', filter: 'all', source: false, request: 0, ready: false };
const codeExtensions = new Set(['py','js','ts','cpp','c','h','ino','json','yaml','yml','cfg','conf','xml','html','css','ps1','sh','toml','example']);
const imageExtensions = new Set(['png','jpg','jpeg','gif','webp','svg','avif']);
function ext(path) { return path.split('/').pop().split('.').pop().toLowerCase(); }
function fileKind(path) {
  if (/(^|\/)(tests?|stubs)(\/|$)/i.test(path) || /(?:^|\/)(test_|.*_check\.)/.test(path)) return 'tests';
  if (['md','txt','rst'].includes(ext(path))) return 'docs';
  return codeExtensions.has(ext(path)) || path.endsWith('/argus') ? 'code' : 'other';
}
function encodedPath(path) { return path.split('/').map(encodeURIComponent).join('/'); }
function rawURL(path) { return `https://raw.githubusercontent.com/${REPO}/${state.ref}/${encodedPath(path)}`; }
function githubURL(path) { return `https://github.com/${REPO}/blob/${state.ref}/${encodedPath(path)}`; }
function el(tag, text, className) { const node = document.createElement(tag); if (text !== undefined) node.textContent = text; if (className) node.className = className; return node; }
function setNotice(message) { $('notice').textContent = message; $('notice').hidden = !message; }
function safeURL(value, path) {
  try {
    if (/^[a-z][a-z\d+.-]*:/i.test(value) && !/^https?:/i.test(value)) return null;
    if (value.startsWith('#')) return null;
    const base = rawURL(path.slice(0, path.lastIndexOf('/') + 1));
    const url = new URL(value, base);
    return ['https:', 'http:'].includes(url.protocol) ? url : null;
  } catch { return null; }
}
// Build markdown with DOM nodes; embedded HTML is displayed as text, never executed.
function inline(parent, text, path) {
  const pattern = /(`[^`]+`|\*\*[^*]+\*\*|!?\[[^\]]*\]\([^\s)]+\))/g;
  let start = 0;
  for (const match of text.matchAll(pattern)) {
    parent.append(document.createTextNode(text.slice(start, match.index)));
    const token = match[0];
    if (token.startsWith('`')) parent.append(el('code', token.slice(1,-1)));
    else if (token.startsWith('**')) parent.append(el('strong', token.slice(2,-2)));
    else {
      const parts = token.match(/^(!?)\[([^\]]*)\]\(([^)]+)\)$/);
      const url = safeURL(parts[3], path);
      if (!url) parent.append(document.createTextNode(token));
      else if (parts[1]) { const img = el('img'); img.src = url.href; img.alt = parts[2]; img.loading = 'lazy'; parent.append(img); }
      else {
        const a = el('a', parts[2]);
        const rawPrefix = `https://raw.githubusercontent.com/${REPO}/${state.ref}/`;
        if (url.href.startsWith(rawPrefix)) {
          const target = decodeURIComponent(url.href.slice(rawPrefix.length));
          a.href = state.files.some(f => f.path === target) ? '#file=' + encodeURIComponent(target) : url.href;
        } else a.href = url.href;
        if (!a.getAttribute('href').startsWith('#')) { a.target = '_blank'; a.rel = 'noopener noreferrer'; }
        parent.append(a);
      }
    }
    start = match.index + token.length;
  }
  parent.append(document.createTextNode(text.slice(start)));
}
function markdown(text, path) {
  const root = document.createDocumentFragment(), lines = text.replace(/\r/g,'').split('\n');
  let i = 0;
  while (i < lines.length) {
    const line = lines[i];
    if (!line.trim()) { i++; continue; }
    if (/^\s*```/.test(line)) {
      const code = []; i++;
      while (i < lines.length && !/^\s*```/.test(lines[i])) code.push(lines[i++]);
      i++; const pre = el('pre'); pre.append(el('code',code.join('\n'))); root.append(pre); continue;
    }
    const heading = line.match(/^(#{1,6})\s+(.+?)\s*#*$/);
    if (heading) { const h = el('h'+heading[1].length); inline(h,heading[2],path); root.append(h); i++; continue; }
    if (/^\s*([-*_])(?:\s*\1){2,}\s*$/.test(line)) { root.append(el('hr')); i++; continue; }
    if (line.includes('|') && i+1 < lines.length && /^\s*\|?\s*:?-{3,}/.test(lines[i+1])) {
      const table=el('table'), header=el('thead'), body=el('tbody');
      const row=(value,tag)=>{const tr=el('tr');value.trim().replace(/^\||\|$/g,'').split('|').forEach(v=>{const cell=el(tag);inline(cell,v.trim(),path);tr.append(cell);});return tr;};
      header.append(row(line,'th')); i+=2;
      while(i<lines.length && lines[i].includes('|') && lines[i].trim()) body.append(row(lines[i++],'td'));
      table.append(header,body);root.append(table);continue;
    }
    if (/^\s*(?:[-*+] |\d+\. )/.test(line)) {
      const ordered=/^\s*\d+\./.test(line), list=el(ordered?'ol':'ul');
      while(i<lines.length && (ordered ? /^\s*\d+\. / : /^\s*[-*+] /).test(lines[i])) {const li=el('li');inline(li,lines[i++].replace(/^\s*(?:[-*+]|\d+\.)\s+/,''),path);list.append(li);}
      root.append(list);continue;
    }
    if (/^>\s?/.test(line)) { const quote=el('blockquote');inline(quote,line.replace(/^>\s?/,''),path);root.append(quote);i++;continue; }
    const p=el('p');inline(p,line,path);root.append(p);i++;
  }
  return root;
}
function codeView(text, highlight) {
  const pre=el('pre',undefined,'source-code'), code=el('code');
  const tokens=/(\/\/.*$|#.*$|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|\b(?:def|class|import|from|return|if|else|elif|for|while|try|except|const|let|function|async|await|true|false|True|False|None|void|bool|int|include|struct|public)\b)/g;
  text.replace(/\r/g,'').split('\n').forEach(line=>{
    const node=el('span',undefined,'source-line');let start=0;
    if(highlight) for(const match of line.matchAll(tokens)) {node.append(document.createTextNode(line.slice(start,match.index)));node.append(el('span',match[0],match[0].startsWith('#')||match[0].startsWith('//')?'syntax-comment':/^['"]/.test(match[0])?'syntax-string':'syntax-keyword'));start=match.index+match[0].length;}
    node.append(document.createTextNode(line.slice(start)||'\u200b'));code.append(node);
  });pre.append(code);return pre;
}
const explanations = {
  'PROJECT-STATUS.md': 'The current progress report: physical results, incomplete deployment steps and the next camera milestone. Start here to distinguish tested behavior from planned work.',
  'PHONE-START-DESIGN.md': 'How a phone request reaches the Pi follower, how Stop invalidates it, and which installation and hardware checks still need to happen.',
  'PI-ESP32-WIRING.md': 'The GPIO serial connection between the Pi and ESP32. This keeps control on the robot while USB supplies power. Follow the documented pin numbers and power-off steps.',
  'START-HERE.md': 'The beginner entry point for using the Orange Pi project. It explains the terminal commands and separates simulated checks from physical robot use.',
  'follow.py': 'The camera tape-following controller. It uses fresh camera frames to choose wheel speeds, requests an explicit drive session, and stops its own session when the tape or camera becomes unreliable.',
  'usb_bridge.py': 'The Pi service that owns the ESP32 serial connection. It exposes a local control interface and claims phone Start requests before launching a bounded follower process.',
  'serial_control.py': 'The serial protocol client. It frames requests and matches replies so the Pi can send state, arm, drive and stop operations through one shared link.',
  'line_preview.py': 'Camera freshness checks and tape interpretation. A healthy video frame and a usable tape path are separate requirements; a missing or ambiguous path must not become a forward command.',
  'core.py': 'The range-based obstacle controller, separate from the tape demo. Its decisions depend on fresh, adequate scan coverage. Passing its software tests does not prove that the broken LiDAR is working.',
  'simulate.py': 'A lightweight simulated world for exercising controller behavior without installing a full robot simulator. These results describe the model, not physical clearance on Argus.',
  'esp32_wifi_controlcam_auto.ino': 'ESP32 firmware: phone control page, manual and automatic drive ownership, UART communication and watchdogs. Real Wi-Fi settings belong in a private config.h. Flashing requires the hardware commissioning steps.',
  'PhoneStart.h': 'One-use phone Start requests. Epochs and random request tokens prevent an old, duplicated or delayed Start from bypassing Stop or taking over a newer session.',
  'DriveControl.h': 'Drive ownership and command expiry. This is where manual/automatic sessions, bounds and the command lease are enforced.',
  'ControlPacketParser.h': 'Packet validation for the control link. Malformed or incomplete input must not turn into a wheel command.',
  'config.h.example': 'A public template for local Wi-Fi settings. Copy it to config.h privately; never commit real passwords or compiled images containing them.'
};
function explain(path) {
  const name=path.split('/').pop();
  if(explanations[name]) return [explanations[name], 'Project-maintained explanation.'];
  if(fileKind(path)==='tests') return ['A software test or test fixture. It checks behavior without proving physical robot performance. Read the cases and assertions to see exactly what is covered.', 'Explanation inferred from the file’s test directory or name.'];
  if(path.includes('/reports/')) return ['A dated verification report or recorded test output. Check its date and environment before treating the result as current physical evidence.', 'Explanation inferred from the reports directory.'];
  if(/\.(yaml|yml|cfg|conf|json|toml)$/.test(path)) return ['Configuration or structured data consumed by the project. Inspect the values and their matching code before changing hardware behavior.', 'Explanation inferred from the file type.'];
  if(fileKind(path)==='docs') return ['Project documentation. The rendered view makes the text easier to read; the source view shows the exact committed file. Its date and stated scope determine whether it describes plans or verified results.', 'General explanation for a new documentation file; add a specific entry in dashboard.js when needed.'];
  return ['A repository file available in its original form. Its folder and source provide context. This dashboard has no reviewed, file-specific explanation for it yet.', 'New files appear automatically; this fallback avoids inventing their purpose.'];
}
function renderFiles() {
  const query=$('search').value.toLowerCase().trim();
  const files=state.files.filter(f=>(state.filter==='all'||fileKind(f.path)===state.filter)&&f.path.toLowerCase().includes(query));
  $('file-count').textContent=`${files.length} / ${state.files.length}`;
  const tree=$('file-tree');tree.replaceChildren();
  const groups=new Map([['',tree]]);
  files.forEach(file=>{
    const parts=file.path.split('/');let prefix='';
    for(let i=0;i<parts.length-1;i++) {const parent=prefix;prefix+=(prefix?'/':'')+parts[i];if(!groups.has(prefix)){const d=el('details');d.open=Boolean(query)||state.selected.startsWith(prefix+'/')||parts.length<3;d.append(el('summary',parts[i]));groups.get(parent).append(d);groups.set(prefix,d);}}
    const link=el('a',undefined,'file-link'+(file.path===state.selected?' selected':''));link.href='#file='+encodeURIComponent(file.path);link.title=file.path;if(file.path===state.selected)link.setAttribute('aria-current','page');link.append(el('span',fileKind(file.path)==='docs'?'▤':'◇','file-icon'),el('span',parts.at(-1)));groups.get(prefix).append(link);
  });
  if(!files.length)tree.append(el('p','No files match this search.','empty'));
}
function renderContent() {
  const area=$('file-content');area.replaceChildren();
  const type=ext(state.selected);
  if(imageExtensions.has(type) && !state.source){const img=el('img');img.src=rawURL(state.selected);img.alt=state.selected;img.onerror=()=>setNotice('Image could not be loaded. Open the raw file to inspect it.');area.append(img);}
  else if(imageExtensions.has(type))area.append(el('p','Image source is available through Raw file.','empty'));
  else if(type==='md'&&!state.source)area.append(markdown(state.text,state.selected));
  else area.append(codeView(state.text,!state.source&&fileKind(state.selected)==='code'));
}
async function openFile(path) {
  const request=++state.request;
  state.selected=path;state.text='';state.ready=false;renderFiles();
  $('file-name').textContent=path.split('/').pop();$('breadcrumb').textContent=path.includes('/')?path.slice(0,path.lastIndexOf('/')):'REPOSITORY ROOT';$('file-meta').textContent='Loading…';
  $('github-file').href=githubURL(path);$('download').href=rawURL(path);$('copy').disabled=true;
  const [explanation,origin]=explain(path);$('file-explanation').textContent=explanation;$('explanation-origin').textContent=origin;
  const area=$('file-content');area.setAttribute('aria-busy','true');area.replaceChildren(el('p','Loading file…','empty'));setNotice('');
  try {
    const file=state.files.find(f=>f.path===path);if(!file)throw Error('This path is not in the current repository. Choose a file from the browser.');
    if(imageExtensions.has(ext(path))){state.ready=true;$('file-meta').textContent=`Image · ${Math.ceil((file.size||0)/1024)} KB`;renderContent();return;}
    if(file.size>MAX_TEXT)throw Error('This file is larger than the 1 MB preview limit. Open it in GitHub or use Raw file.');
    const response=await fetch(rawURL(path));if(!response.ok)throw Error(`GitHub returned ${response.status}. Try Refresh or open the file in GitHub.`);
    const text=await response.text();if(request!==state.request)return;
    if(text.length>MAX_TEXT||text.includes('\u0000'))throw Error('This format is available as a raw download. Text preview is unavailable.');
    state.text=text;state.ready=true;$('copy').disabled=false;
    $('file-meta').textContent=`${ext(path).toUpperCase()} · ${text.split('\n').length} lines · ${Math.max(1,Math.ceil((file.size||text.length)/1024))} KB · ${state.ref===BRANCH?'main':state.ref.slice(0,7)}`;
    renderContent();
  }catch(error){if(request===state.request){setNotice(error.message);area.replaceChildren(el('p','Preview unavailable. The original file is still accessible using the links above.','empty'));$('file-meta').textContent='Preview unavailable';}}
  finally{if(request===state.request)area.setAttribute('aria-busy','false');}
}
function route() {let path;try{path=new URLSearchParams(location.hash.slice(1)).get('file')||DEFAULT_FILE;}catch{path=DEFAULT_FILE;}openFile(path);}
async function jsonFetch(url) {const controller=new AbortController(),timeout=setTimeout(()=>controller.abort(),12000);try{const r=await fetch(url,{signal:controller.signal});if(!r.ok)throw Error(`GitHub ${r.status}`);return await r.json();}finally{clearTimeout(timeout);}}
async function loadRepository() {
  $('refresh').disabled=true;$('sync-label').textContent='Checking latest commit…';
  let source='GitHub';
  try {
    const branch=await jsonFetch(`${API}/branches/${BRANCH}`);
    const tree=await jsonFetch(`${API}/git/trees/${branch.commit.sha}?recursive=1`);
    if(tree.truncated)throw Error('Repository exceeds the recursive listing limit');
    const data={ref:branch.commit.sha,files:tree.tree.filter(f=>f.type==='blob').map(({path,size})=>({path,size})),savedAt:Date.now()};
    state.files=data.files;state.ref=data.ref;
    try{localStorage.setItem(CACHE_KEY,JSON.stringify(data));}catch{/* Storage can be disabled. */}
  } catch(error) {
    let data;try{data=JSON.parse(localStorage.getItem(CACHE_KEY));}catch{/* No cache. */}
    if(data&&Array.isArray(data.files)&&typeof data.ref==='string'){source='Cached listing';state.files=data.files;state.ref=data.ref;}
    else {try{const snapshot=await jsonFetch('catalog.json');state.files=snapshot.files;state.ref=snapshot.ref;source='Bundled snapshot';}catch{state.files=[];}}
    if(!state.files.length){$('sync-label').textContent='GitHub unavailable';$('file-tree').replaceChildren(el('p','Cannot load files. Try Refresh or open GitHub.','empty'));$('file-content').replaceChildren(el('p','Repository unavailable. Check your connection and try Refresh.','empty'));$('file-content').setAttribute('aria-busy','false');$('refresh').disabled=false;return;}
  }
  state.files.sort((a,b)=>a.path.localeCompare(b.path));
  $('sync-label').textContent=`${source} · ${state.ref.slice(0,7)}`;
  $('refresh').disabled=false;route();
  if(source!=='GitHub')setNotice('GitHub is unavailable or rate limited. Showing an older file listing; use Refresh to retry.');
}
function init() {
  $('search').addEventListener('input',renderFiles);
  document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{state.filter=button.dataset.filter;document.querySelectorAll('[data-filter]').forEach(b=>{b.classList.toggle('active',b===button);b.setAttribute('aria-pressed',String(b===button));});renderFiles();}));
  [$('preview-tab'),$('source-tab')].forEach((button,i)=>button.addEventListener('click',()=>{state.source=Boolean(i);$('preview-tab').classList.toggle('active',!i);$('source-tab').classList.toggle('active',Boolean(i));$('preview-tab').setAttribute('aria-pressed',String(!i));$('source-tab').setAttribute('aria-pressed',String(Boolean(i)));if(state.ready)renderContent();}));
  $('copy').addEventListener('click',async()=>{try{await navigator.clipboard.writeText(state.text);$('copy').textContent='Copied';setTimeout(()=>$('copy').textContent='Copy',1500);}catch{setNotice('Copy is unavailable in this browser. Use Source or Raw file.');}});
  $('refresh').addEventListener('click',loadRepository);
  addEventListener('hashchange',()=>{if(state.files.length)route();});
  addEventListener('keydown',event=>{if(event.key==='/'&&!/INPUT|TEXTAREA/.test(document.activeElement.tagName)){event.preventDefault();$('search').focus();}});
  loadRepository();
}
if(typeof document!=='undefined')init();
