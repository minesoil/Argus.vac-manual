// Run the actual embedded script with DOM/HTTP stand-ins. No device requests.
const assert = require('assert');
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const sketch = fs.readFileSync(path.join(__dirname, '../esp32_wifi_controlcam_auto.ino'), 'utf8');
const source = sketch.match(/<script>([\s\S]*?)<\/script>/)[1];
const states = [];
const lidars = [];
const posts = [];
const drawnArcs = [];
const elements = new Map();
const response = (value, status = 200) => ({ok: status < 400, json: async () => value});
function deferred() {
  let resolve;
  const promise = new Promise(accept => {resolve = accept;});
  return {promise, resolve};
}
function element(id) {
  if (!elements.has(id)) elements.set(id, {
    style: {}, textContent: '', className: '', hidden: false,
    value: id === 'mapRange' ? '200' : '', events: {},
    addEventListener(name, fn) {this.events[name] = fn;},
    setPointerCapture() {},
    getBoundingClientRect() {return {left: 0, top: 0, width: 160, height: 160};},
    getContext() {
      const draw = () => {};
      return {setTransform: draw, fillRect: draw, beginPath: draw,
        arc(x, y, radius) {drawnArcs.push({x, y, radius});},
        stroke: draw, fillText: draw, moveTo: draw, lineTo: draw, fill: draw};
    }
  });
  return elements.get(id);
}
const context = vm.createContext({
  document: {getElementById: element, addEventListener() {}, hidden: false},
  window: {addEventListener() {}},
  URLSearchParams, Math, Date, console,
  setInterval() {}, setTimeout() {}, clearTimeout() {},
  fetch(url, options) {
    const pending = deferred();
    if (url === '/lidar') {
      lidars.push(pending);
    } else if (!options || options.method !== 'POST') {
      states.push(pending);
    } else {
      posts.push({url, body: new URLSearchParams(options.body), ...pending});
    }
    return pending.promise;
  }
});
const evaluate = code => vm.runInContext(code, context);
const settle = () => new Promise(resolve => setImmediate(resolve));

async function selectManual(epoch, token) {
  const selection = evaluate('selectManual(intent)');
  states.at(-1).resolve(response({mode: 'stopped', epoch, reason: 'stopped'}));
  await settle();
  const arm = posts.at(-1);
  assert.equal(arm.url, '/manual/arm');
  assert.equal(arm.body.get('epoch'), String(epoch));
  arm.resolve(response({mode: 'manual', epoch: epoch + 1, session: token}));
  assert.equal(await selection, true);
}

async function main() {
  evaluate(source);
  const oldestPoll = states[0];
  await selectManual(100, '1111111111111111');
  oldestPoll.resolve(response({mode: 'stopped', epoch: 100, reason: 'old poll'}));
  await settle();
  assert.equal(evaluate('manualSession'), '1111111111111111');

  const first = evaluate('refreshState()');
  const earlier = states.at(-1);
  const second = evaluate('refreshState()');
  states.at(-1).resolve(response({mode: 'auto', epoch: 102, reason: 'auto selected'}));
  await second;
  earlier.resolve(response({mode: 'manual', epoch: 101, reason: 'older state'}));
  await first;
  assert.equal(evaluate('mode'), 'auto');
  assert.equal(evaluate('manualSession'), '');
  const beforeIdle = posts.length;
  await evaluate('sendDrive()');
  assert.equal(posts.length, beforeIdle);

  await selectManual(102, '2222222222222222');
  const pendingDrive = evaluate('leftSpeed = 50; rightSpeed = 50; sendDrive()');
  const drive = posts.at(-1);
  assert.equal(drive.url, '/drive');
  assert.equal(evaluate('sending'), true);
  const stop = evaluate('operatorStop()');
  assert.equal(posts.at(-1).url, '/stop');
  posts.at(-1).resolve(response({mode: 'stopped', epoch: 104}));
  await settle();
  states.at(-1).resolve(response({mode: 'stopped', epoch: 104, reason: 'Operator stop'}));
  await stop;
  drive.resolve(response(null, 204));
  await pendingDrive;
  assert.equal(evaluate('manualSession'), '');
  assert.equal(evaluate('mode'), 'stopped');
  const afterStop = posts.length;
  await evaluate('sendDrive()');
  assert.equal(posts.length, afterStop);

  // A joystick gesture checks the ESP32's current mode even when the displayed
  // status is still stopped from before automatic mode was selected.
  const gesture = elements.get('stick').events.pointerdown({pointerId: 1, clientX: 80, clientY: 40});
  states.at(-1).resolve(response({mode: 'auto', epoch: 105, reason: 'Automatic selected'}));
  await settle();
  states.at(-1).resolve(response({mode: 'auto', epoch: 105, reason: 'Automatic selected'}));
  await settle();
  assert.equal(posts.at(-1).url, '/assist/arm');
  posts.at(-1).resolve(response({mode: 'manual', epoch: 106, session: '3333333333333333'}));
  await gesture;
  assert.equal(evaluate('mode'), 'manual');
  assert.equal(posts.at(-1).url, '/drive');
  assert.ok(Number(posts.at(-1).body.get('l')) >= 0 && Number(posts.at(-1).body.get('l')) <= 35);
  assert.ok(Number(posts.at(-1).body.get('r')) >= 0 && Number(posts.at(-1).body.get('r')) <= 35);
  posts.at(-1).resolve(response(null, 204));
  await settle();

  // A Stop that wins while Start is in flight must not be undone by its reply.
  const start = elements.get('follow').onclick();
  states.at(-1).resolve(response({mode: 'stopped', epoch: 110, reason: 'stopped'}));
  await settle();
  const startPost = posts.at(-1);
  assert.equal(startPost.url, '/follow/start');
  const concurrentStop = evaluate('operatorStop()');
  const stopPost = posts.at(-1);
  assert.equal(stopPost.url, '/stop');
  stopPost.resolve(response({mode: 'stopped', epoch: 111}));
  await settle();
  states.at(-1).resolve(response({mode: 'stopped', epoch: 111, reason: 'Operator stop'}));
  await concurrentStop;
  const countAfterStop = posts.length;
  startPost.resolve(response({follow_token: '4444444444444444'}));
  await start;
  assert.equal(evaluate('followToken'), '');
  assert.equal(posts.length, countAfterStop);

  const roamStart = elements.get('roam').onclick();
  states.at(-1).resolve(response({mode: 'stopped', epoch: 111, reason: 'stopped'}));
  await settle();
  assert.equal(posts.at(-1).url, '/roam/start');
  posts.at(-1).resolve(response({follow_token: '5555555555555555'}));
  await roamStart;
  assert.equal(evaluate('followToken'), '5555555555555555');
  assert.equal(evaluate('modeLabel.textContent'), 'Lidar roaming requested');
  const showMap = evaluate('refreshLidar()');
  assert.equal(lidars.length, 1);
  const bins = '14' + '00'.repeat(17) + '0A' + '00'.repeat(53);
  lidars[0].resolve(response({fresh: true, age_ms: 120, bins, sensor_forward_cm: 8}));
  await showMap;
  assert.ok(elements.get('mapStatus').textContent.startsWith('LIVE'));
  assert.equal(elements.get('mapCard').className, 'map-card');
  // At a 2 m view and 240 px canvas, a 1 m forward return starts at
  // the C1 marker 8 cm ahead of the robot midpoint.
  assert.ok(drawnArcs.some(a => Math.abs(a.x - 120) < .1 &&
    Math.abs(a.y - (120 - 108 * .528)) < .1 && a.radius === 1.8));
  elements.get('viewCamera').onclick();
  assert.equal(elements.get('lidarPanel').hidden, true);
  assert.equal(elements.get('cameraPanel').hidden, false);
  elements.get('viewLidar').onclick();
  assert.equal(elements.get('lidarPanel').hidden, false);
  const staleMap = lidars.at(-1);
  staleMap.resolve(response({fresh: false, age_ms: 1700, bins, sensor_forward_cm: 8}));
  await settle();
  assert.ok(elements.get('mapStatus').textContent.toLowerCase().includes('stale'));
  assert.ok(elements.get('mapCard').className.includes('stale'));
  console.log('PASS embedded UI: stale poll, manual takeover, Stop races and separate lidar roaming Start');
}
main().catch(error => {console.error(error); process.exitCode = 1;});
