// Run with Node and Playwright installed. No robot connection or GitHub writes.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const { chromium } = require(process.env.PLAYWRIGHT_PATH || 'playwright');
const files = [
  {path:'robot_control/PROJECT-STATUS.md',size:3200},
  {path:'robot_control/follow.py',size:80},
  {path:'new-folder/new-note.md',size:100},
  {path:'tests/test_example.py',size:90},
  {path:'README.md',size:60}
];
const contents = {
  'robot_control/PROJECT-STATUS.md':'# Project status\n\n**Tested** results.\n\n| Check | State |\n| --- | --- |\n| Stop | Passed |\n\n```python\nprint("hello")\n```\n\n<script>window.compromised=true</script>\n[Unsafe](javascript:alert(1))\n[Note](../new-folder/new-note.md)',
  'robot_control/follow.py':'# A comment\ndef follow():\n    return True\n',
  'new-folder/new-note.md':'# A new note\nAutomatically discovered.',
  'tests/test_example.py':'assert True',
  'README.md':'# Readme'
};
const server = http.createServer((req,res)=>{
  if(req.url==='/catalog.json'){res.setHeader('Content-Type','application/json');res.end(JSON.stringify({ref:'abc1234',files}));return;}
  const name=req.url==='/'?'index.html':req.url.slice(1).split('?')[0];
  if(!['index.html','dashboard.js','dashboard.css'].includes(name)){res.writeHead(404);res.end();return;}
  res.setHeader('Content-Type',name.endsWith('.js')?'application/javascript':name.endsWith('.css')?'text/css':'text/html');res.end(fs.readFileSync(path.join(__dirname,name)));
});
(async()=>{
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  const browser=await chromium.launch({headless:true,...(process.env.PLAYWRIGHT_CHANNEL?{channel:process.env.PLAYWRIGHT_CHANNEL}:{})});
  try {
    const page=await browser.newPage({viewport:{width:1440,height:1100}}),errors=[];
    page.on('pageerror',e=>errors.push(e.message));
    await page.route('https://fonts.googleapis.com/**',r=>r.abort());
    await page.route('https://api.github.com/**',r=>r.fulfill({json:r.request().url().includes('/branches/')?{commit:{sha:'abc1234'}}:{tree:files.map(f=>({...f,type:'blob'})),truncated:false}}));
    await page.route('https://raw.githubusercontent.com/**',r=>{
      const url=r.request().url(),file=decodeURIComponent(url.split('/abc1234/')[1]||'');
      return r.fulfill({body:contents[file]||'',contentType:'text/plain'});
    });
    const url=`http://127.0.0.1:${server.address().port}`;
    await page.goto(url);
    await page.waitForSelector('#file-content h1');
    assert.equal(await page.locator('#file-name').innerText(),'PROJECT-STATUS.md');
    assert.equal(await page.locator('#file-content table').count(),1);
    assert.equal(await page.evaluate(()=>Boolean(window.compromised)),false);
    assert.equal(await page.locator('#file-content a[href^="javascript:"]').count(),0);
    await page.locator('#source-tab').click();
    assert.match(await page.locator('#file-content').innerText(),/<script>/);
    await page.locator('#search').fill('new-note');
    assert.equal(await page.locator('.file-link').count(),1);
    await page.locator('.file-link').click();
    await page.waitForFunction(()=>document.getElementById('file-name').textContent==='new-note.md');
    await page.waitForFunction(()=>document.getElementById('file-meta').textContent.includes('lines'));
    assert.match(await page.locator('#file-explanation').innerText(),/Project documentation/);
    await page.locator('#search').fill('');
    await page.locator('[data-filter="tests"]').click();
    assert.equal(await page.locator('.file-link').count(),1);
    await page.locator('[data-filter="all"]').click();
    await page.goto(url+'/#file=robot_control%2Ffollow.py');
    await page.waitForFunction(()=>document.getElementById('file-meta').textContent.includes('lines'));
    assert.match(await page.locator('#file-content').innerText(),/def follow/);
    await page.screenshot({path:path.join(__dirname,'../../.tmp/argus-dashboard-desktop.png'),fullPage:true});
    await page.setViewportSize({width:390,height:844});
    assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);
    await page.screenshot({path:path.join(__dirname,'../../.tmp/argus-dashboard-mobile.png'),fullPage:true});
    await page.unroute('https://api.github.com/**');
    await page.route('https://api.github.com/**',r=>r.fulfill({status:403,body:'rate limited'}));
    await page.reload();
    await page.waitForFunction(()=>document.getElementById('sync-label').textContent.includes('Cached'));
    await page.waitForFunction(()=>document.getElementById('file-meta').textContent.includes('lines'));
    await page.evaluate(()=>localStorage.clear());
    await page.reload();
    await page.waitForFunction(()=>document.getElementById('sync-label').textContent.includes('Bundled'));
    await page.goto(url+'/#file=missing.md');
    await page.waitForFunction(()=>document.getElementById('file-meta').textContent==='Preview unavailable');
    assert.equal(errors.length,0,errors.join('\n'));
    console.log('PASS: markdown, safe rendering, source, discovery, search, filters, deep links, mobile width, cached and bundled fallbacks, missing files.');
  }finally{await browser.close();server.close();}
})().catch(error=>{console.error(error);server.close();process.exitCode=1;});
