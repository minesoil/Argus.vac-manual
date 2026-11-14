
#include <WiFi.h>
#include <WebServer.h>
#include <errno.h>
#include <stdlib.h>
#include "DriveControl.h"
#include "ControlPacketParser.h"
#include "PhoneStart.h"
#include "ManualGuard.h"
#include "LidarMap.h"

// Argus Vac camera relay and joystick
// Board: NodeMCU-32 / ESP32-WROOM-32

#include "config.h"

// ESP32 -> Arduino Mega Serial1
const int MEGA_RX_PIN = 16;   // ESP32 RX2
const int MEGA_TX_PIN = 17;   // ESP32 TX2 -> Mega D19

const int MEGA_BAUD = 9600;

// Orange Pi GPIO UART: Pi TX -> GPIO25 RX; Pi RX <- GPIO26 TX; shared GND.
const int PI_RX_PIN = 25;
const int PI_TX_PIN = 26;
const int PI_BAUD = 115200;
ControlPacketParser gpioControl;

// Orange Pi -> ESP32 programming USB
const int CAMERA_BAUD = 115200;
const size_t MAX_JPEG = 24000;

// Motor command timing
const unsigned long SEND_INTERVAL = 100;

WebServer server(80);

// CAMERA FRAME BUFFERS

// Two buffers: receiving + completed frame
uint8_t jpegBuffers[2][MAX_JPEG];

uint8_t activeFrame = 0;
size_t activeLength = 0;
bool frameReady = false;
unsigned long frameTime = 0;

// USB preview packet: "AVF1" + uint32 length (little endian) + JPEG.
// USB map packet: "AVL1" + uint32 length (little endian, 72) + 72 range bins.

enum CameraState {
  WAIT_MAGIC,
  READ_LENGTH,
  READ_JPEG
};

CameraState cameraState = WAIT_MAGIC;

const uint8_t MAGIC[4] = {'A','V','F','1'};
const uint8_t MAP_MAGIC[4] = {'A','V','L','1'};
bool controlPacket = false;
bool mapPacket = false;
const uint8_t CONTROL_MAGIC[4] = {0xA5, 0xDA, 0xC3, 0xBC};
const size_t MAX_CONTROL = 160;
char controlBuffer[MAX_CONTROL + 1];
uint8_t mapBuffer[LidarMap::BinCount];
void processControlPacket(char* payload, bool viaGPIO = false);

uint8_t magicPos = 0;
uint8_t lengthPos = 0;
uint32_t expectedLength = 0;
size_t receivedLength = 0;

unsigned long lastCameraByte = 0;

// CONTROL OWNERSHIP AND MEGA OUTPUT

DriveControl control;
ManualGuard manualGuard;
PhoneStart phoneStart;
LidarMap lidarMap;
bool phoneSessionActive = false;
uint32_t phoneLastHeartbeat = 0;
unsigned long lastMotorSend = 0;

void sendImmediateStop() {
  // End any partial packet before the Mega's single-character stop command.
  Serial2.print("\nS\n");
}

void sendToMega(int left, int right) {
  Serial2.print("M:");
  Serial2.print(left);
  Serial2.print(",");
  Serial2.println(right);
}

void updateMotors() {
  unsigned long now = millis();
  bool expired = manualGuard.tick(control, now);
  expired = control.expire(now) || expired;
  bool phoneOwnsState = phoneSessionActive &&
      ((control.mode == DriveMode::Stopped && control.epoch == phoneStart.epoch) ||
       (control.mode == DriveMode::Automatic && control.epoch == uint32_t(phoneStart.epoch + 1)));
  if (phoneSessionActive && !phoneOwnsState) phoneSessionActive = false;
  if (phoneOwnsState && uint32_t(now - phoneLastHeartbeat) >= 1000) {
    phoneSessionActive = false;
    phoneStart.pending = false;
    control.stop("Phone connection lost; select control again");
    expired = true;
  }
  if (expired) {
    sendImmediateStop();
    lastMotorSend = now;
  }
  if (now - lastMotorSend < SEND_INTERVAL) return;
  lastMotorSend = now;
  if (control.mode == DriveMode::Stopped) {
    sendImmediateStop();
  } else {
    sendToMega(control.left, control.right);
  }
}

// CAMERA SERIAL RECEIVER

void resetCameraParser() {
  cameraState = WAIT_MAGIC;
  magicPos = 0;
  lengthPos = 0;
  expectedLength = 0;
  receivedLength = 0;
  controlPacket = false;
  mapPacket = false;
}

void processCameraByte(uint8_t b) {

  lastCameraByte = millis();

  if (cameraState == WAIT_MAGIC) {

    if (magicPos == 0) {
      controlPacket = b == CONTROL_MAGIC[0];
      mapPacket = false;
    }
    if (!controlPacket && magicPos == 2 && b == MAP_MAGIC[2]) mapPacket = true;
    const uint8_t* expectedMagic = controlPacket ? CONTROL_MAGIC : (mapPacket ? MAP_MAGIC : MAGIC);
    if (b == expectedMagic[magicPos]) {
      magicPos++;
    } else {
      magicPos = (b == MAGIC[0] || b == CONTROL_MAGIC[0]) ? 1 : 0;
      controlPacket = b == CONTROL_MAGIC[0];
      mapPacket = false;
    }

    if (magicPos == 4) {
      cameraState = READ_LENGTH;
      magicPos = 0;
      lengthPos = 0;
      expectedLength = 0;
    }

    return;
  }

  if (cameraState == READ_LENGTH) {
    if (controlPacket && b < 0x80) {
      resetCameraParser();
      return;
    }
    expectedLength |= controlPacket
        ? ((uint32_t)(b & 0x7f) << (7 * lengthPos))
        : ((uint32_t)b << (8 * lengthPos));

    lengthPos++;

    if (lengthPos == (controlPacket ? 2 : 4)) {

      if ((mapPacket && expectedLength != LidarMap::BinCount) ||
          (!mapPacket && (expectedLength < (controlPacket ? 1u : 4u) ||
                          expectedLength > (controlPacket ? MAX_CONTROL : MAX_JPEG)))) {
        resetCameraParser();
        return;
      }

      receivedLength = 0;
      cameraState = READ_JPEG;
    }

    return;
  }

  if (cameraState == READ_JPEG) {

    if (mapPacket) {
      mapBuffer[receivedLength++] = b;
      if (receivedLength == expectedLength) {
        lidarMap.updateBins(mapBuffer, receivedLength, millis());
        resetCameraParser();
      }
      return;
    }

    if (controlPacket) {
      if (b < 0x80) {
        resetCameraParser();
        return;
      }
      controlBuffer[receivedLength++] = (char)(b & 0x7f);
      if (receivedLength == expectedLength) {
        controlBuffer[receivedLength] = '\0';
        // Embedded NUL bytes cannot truncate a validated command.
        if (strlen(controlBuffer) == expectedLength) processControlPacket(controlBuffer);
        resetCameraParser();
      }
      return;
    }

    uint8_t receivingBuffer = 1 - activeFrame;

    jpegBuffers[receivingBuffer][receivedLength++] = b;

    if (receivedLength == expectedLength) {

      uint8_t* image = jpegBuffers[receivingBuffer];

      bool validJPEG =
        image[0] == 0xFF &&
        image[1] == 0xD8 &&
        image[expectedLength - 2] == 0xFF &&
        image[expectedLength - 1] == 0xD9;

      if (validJPEG) {
        activeFrame = receivingBuffer;
        activeLength = expectedLength;
        frameReady = true;
        frameTime = millis();
      }

      resetCameraParser();
    }
  }
}

void receiveCamera() {

  if (cameraState != WAIT_MAGIC &&
      millis() - lastCameraByte > 1500) {
    resetCameraParser();
  }

  // Limit serial processing each pass,
  // so Wi-Fi and motor handling still run.
  int budget = 4096;

  while (Serial.available() > 0 && budget-- > 0) {
    int value = Serial.read();

    if (value >= 0) {
      processCameraByte((uint8_t)value);
    }
  }
}

void receiveGpioControl() {
  gpioControl.expire(millis());
  int budget = 256;
  while (Serial1.available() > 0 && budget-- > 0) {
    int value = Serial1.read();
    if (value >= 0 && gpioControl.feed((uint8_t)value, millis())) {
      processControlPacket(gpioControl.payload, true);
    }
  }
}

// WEBPAGE

const char PAGE_HTML[] PROGMEM = R"ARGUS(
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport"
 content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">

<title>Argus Vac</title>

<style>
* { box-sizing: border-box; }

body {
  margin: 0;
  background: #0b1118;
  color: #dce7ec;
  font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
  text-align: center;
}

main {
  max-width: 680px;
  margin: auto;
  padding: 14px;
}

h2 {
  margin: 7px 0 14px;
  font-size: 19px;
  font-weight: 600;
  letter-spacing: 3px;
}

.view-tabs {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin-bottom: 10px;
}
.view-tabs button {
  margin: 0;
  padding: 10px;
  background: #16212b;
  color: #a4b7bf;
  font: 12px ui-monospace, SFMono-Regular, Consolas, monospace;
  letter-spacing: .5px;
}
.view-tabs button.selected {
  background: #17323a;
  color: #bce9e5;
  box-shadow: inset 0 -2px #4ca8a4;
}
.sensor-panel[hidden] { display: none; }
.map-card {
  padding: 9px;
  border: 1px solid #34505a;
  border-radius: 4px;
  background: #111d26;
}
.map-heading {
  display: flex;
  justify-content: space-between;
  padding: 2px 3px 9px;
  color: #a9c8ce;
  font-size: 11px;
  letter-spacing: 1px;
}
#lidarCanvas {
  display: block;
  width: 100%;
  aspect-ratio: 1;
  border: 1px solid #29424b;
  background: #0b171e;
}
.map-card.stale #lidarCanvas { opacity: .6; }
.map-details {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 10px;
  margin-top: 8px;
  text-align: left;
}
.map-details .status { margin: 0; }
.map-details select {
  flex: none;
  border: 1px solid #45606a;
  border-radius: 3px;
  padding: 6px;
  background: #13232c;
  color: #dce7ec;
  font: 11px ui-monospace, SFMono-Regular, Consolas, monospace;
}

.camera {
  width: 100%;
  aspect-ratio: 4/3;
  background: #050505;
  border: 1px solid #34444e;
  border-radius: 12px;
  object-fit: contain;
}

.status {
  font-size: 12px;
  color: #aab8c4;
  margin: 8px;
}
.warning { color: #ff9b88; font-weight: bold; }

#stick {
  position: relative;
  margin: 20px auto;
  width: 210px;
  height: 210px;
  border-radius: 50%;
  background: #263743;
  border: 2px solid #647887;
  touch-action: none;
  user-select: none;
}

#knob {
  position: absolute;
  width: 66px;
  height: 66px;
  border-radius: 50%;
  background: #70b9d3;
  border: 3px solid #b9e8f8;
  left: 50%;
  top: 50%;
  transform: translate(-50%,-50%);
  pointer-events: none;
}

.readout {
  display: flex;
  justify-content: space-around;
  padding: 9px;
  background: #1b2b35;
  border-radius: 9px;
}

button {
  padding: 13px 30px;
  border: 0;
  border-radius: 9px;
  background: #d94b4b;
  color: white;
  font-weight: bold;
  font-size: 16px;
  margin-top: 14px;
}
#stop {
  position: sticky;
  bottom: 10px;
  z-index: 2;
  width: 100%;
  box-shadow: 0 4px 18px #0009;
}
</style>
</head>

<body>
<main>
<h2>ARGUS VAC</h2>

<div class="view-tabs">
  <button id="viewLidar" class="selected" type="button">LiDAR map</button>
  <button id="viewCamera" type="button">Camera · later</button>
</div>
<section id="lidarPanel" class="sensor-panel" aria-label="Live LiDAR map">
  <div id="mapCard" class="map-card stale">
    <div class="map-heading"><span>C1 / POLAR SCAN</span><span>72 × 5° · ROBOT FRAME</span></div>
    <canvas id="lidarCanvas" aria-label="Robot centered range map; forward is up"></canvas>
    <div class="map-details">
      <div id="mapStatus" class="status">Waiting for LiDAR scan...</div>
      <select id="mapRange" aria-label="Map distance">
        <option value="100">1 m view</option>
        <option value="200" selected>2 m view</option>
        <option value="400">4 m view</option>
        <option value="800">8 m view</option>
      </select>
    </div>
  </div>
  <p class="status">FORWARD ↑ · RETURNS AT SCANNER HEIGHT · BLANK SECTORS = UNKNOWN</p>
</section>
<section id="cameraPanel" class="sensor-panel" hidden>
  <img id="camera" class="camera" alt="Optional camera preview">
  <div id="cameraStatus" class="status">Camera preview is available when enabled on the Pi.</div>
</section>

<div id="stick">
  <div id="knob"></div>
</div>

<div class="readout">
  <span>LEFT: <b id="left">0%</b></span>
  <span>RIGHT: <b id="right">0%</b></span>
</div>

<div id="driveMode" class="status">Stopped</div>
<div id="guardStatus" class="status">Camera assistance unavailable</div>
<button id="assist">ENABLE CAMERA-ASSISTED DRIVE</button>
<button id="manual">UNASSISTED MANUAL (NO CAMERA STOP)</button>
<button id="follow">START LINE FOLLOWING</button>
<button id="roam">START LIDAR ROAMING</button>
<p class="status">LiDAR roaming requires a clear route. Keep STOP within reach. Scan or connection loss ends the run.</p>
<button id="stop">STOP</button>
<p class="status">Camera-assisted drive: forward only, 35% limit. Release joystick to stop. Tape following and unassisted manual have no obstacle stop.</p>
</main>

<script>
// Joystick

const stick = document.getElementById("stick");
const knob = document.getElementById("knob");

let leftSpeed = 0;
let rightSpeed = 0;
let dragging = false;

function updateReadout() {
  document.getElementById("left").textContent =
    leftSpeed + "%";

  document.getElementById("right").textContent =
    rightSpeed + "%";
}

function moveStick(e) {
  const rect = stick.getBoundingClientRect();

  const cx = rect.left + rect.width / 2;
  const cy = rect.top + rect.height / 2;

  const radius = 70;

  let dx = e.clientX - cx;
  let dy = e.clientY - cy;

  const distance = Math.hypot(dx, dy);

  if (distance > radius) {
    dx = dx * radius / distance;
    dy = dy * radius / distance;
  }

  knob.style.left =
    `calc(50% + ${dx}px)`;

  knob.style.top =
    `calc(50% + ${dy}px)`;

  const steering = dx / radius;
  const throttle = -dy / radius;

  // Mix throttle and steering, keeping both outputs within 100%.
  let l = throttle + steering;
  let r = throttle - steering;

  const scale = Math.max(1, Math.abs(l), Math.abs(r));

  leftSpeed = Math.round(l / scale * 100);
  rightSpeed = Math.round(r / scale * 100);
  if (manualAssist) {
    leftSpeed = Math.max(0, Math.round(leftSpeed * .35));
    rightSpeed = Math.max(0, Math.round(rightSpeed * .35));
  }

  updateReadout();
}

let manualSession = "";
let manualAssist = false;
let followToken = "";
let manualEpoch = "";
let sequence = 0;
let mode = "stopped";
let intent = 0;
let sending = false;
let stateGeneration = 0;
let stateRequest = 0;
let latestStateApplied = 0;
const modeLabel = document.getElementById("driveMode");

function centerStick() {
  dragging = false;
  knob.style.left = "50%";
  knob.style.top = "50%";
  leftSpeed = 0;
  rightSpeed = 0;
  updateReadout();
}

async function post(path, fields = {}) {
  return fetch(path, {
    method: "POST",
    body: new URLSearchParams(fields),
    cache: "no-store"
  });
}

async function refreshState() {
  const observedGeneration = stateGeneration;
  const request = ++stateRequest;
  const reply = await fetch("/state", {cache: "no-store"});
  const state = await reply.json();
  if (observedGeneration !== stateGeneration || request < latestStateApplied) return state;
  latestStateApplied = request;
  mode = state.mode;
  modeLabel.textContent = state.mode + " — " + state.reason;
  document.getElementById("guardStatus").textContent = state.assist
      ? (state.guard === "clear" ? (state.guard_latched ? "View clear — re-enable assisted drive to resume" : "Camera assistance active — watched front region only")
         : (state.guard === "blocked" ? "OBSTACLE WARNING — assisted drive stopped" : "CAMERA UNAVAILABLE — assisted drive stopped"))
      : "Camera: " + (state.guard || "unavailable") + " — unassisted mode has no obstacle stop";
  document.getElementById("guardStatus").className = "status" + (state.assist && (state.guard !== "clear" || state.guard_latched) ? " warning" : "");
  if (manualSession && String(state.epoch) !== manualEpoch) {
    manualSession = "";
    centerStick();
  }
  return state;
}

async function selectManual(expectedIntent, assisted = false) {
  followToken = "";
  const state = await refreshState();
  if (expectedIntent !== intent) return false;
  const reply = await post(assisted ? "/assist/arm" : "/manual/arm", {epoch: String(state.epoch)});
  if (!reply.ok) {
    await refreshState();
    if (assisted) modeLabel.textContent = "Camera view not ready — assisted drive remains stopped";
    return false;
  }
  const selected = await reply.json();
  if (expectedIntent !== intent) return false;
  ++stateGeneration;
  manualSession = selected.session;
  manualAssist = assisted;
  manualEpoch = String(selected.epoch);
  sequence = 0;
  mode = "manual";
  modeLabel.textContent = "manual — ready";
  return true;
}

async function operatorStop() {
  ++intent;
  ++stateGeneration;
  manualSession = "";
  followToken = "";
  centerStick();
  mode = "stopped";
  modeLabel.textContent = "stopped — stop requested";
  // This has its own request and never waits for a drive request to finish.
  try {
    await post("/stop");
    await refreshState();
  } catch (error) {
    modeLabel.textContent = "Connection lost — reconnect and select control again";
  }
}

async function sendDrive() {
  if (!manualSession || mode !== "manual" || sending || document.hidden) return;
  const sentIntent = intent;
  const sentSession = manualSession;
  sending = true;
  try {
    const reply = await post("/drive", {
      session: sentSession,
      seq: String(++sequence),
      l: String(leftSpeed),
      r: String(rightSpeed)
    });
    if (!reply.ok && sentIntent === intent && sentSession === manualSession) {
      manualSession = "";
      centerStick();
      await refreshState();
    }
  } catch (error) {
    if (sentIntent === intent) {
      manualSession = "";
      centerStick();
      modeLabel.textContent = "Connection lost — select control again";
    }
  } finally {
    sending = false;
  }
}

function releaseStick() {
  ++intent;
  centerStick();
  sendDrive();
}

stick.addEventListener("pointerdown", async event => {
  const thisIntent = ++intent;
  stick.setPointerCapture(event.pointerId);
  try {
    const current = await refreshState();
    if (thisIntent !== intent) return;
    if (current.mode === "stopped") {
      modeLabel.textContent = "Choose assisted or unassisted manual control first";
      return;
    }
    dragging = true;
    // A deliberate joystick gesture takes over automatic control.
    if (!manualSession && !await selectManual(thisIntent, true)) return;
    if (thisIntent !== intent || !dragging) return;
    moveStick(event);
    sendDrive();
  } catch (error) {
    manualSession = "";
    centerStick();
  }
});

stick.addEventListener("pointermove", event => {
  if (dragging && manualSession) moveStick(event);
});
stick.addEventListener("pointerup", releaseStick);
stick.addEventListener("pointercancel", releaseStick);

document.getElementById("manual").onclick = async () => {
  centerStick();
  const thisIntent = ++intent;
  try {
    if (await selectManual(thisIntent)) sendDrive();
  } catch (error) {
    modeLabel.textContent = "Connection lost — select control again";
  }
};
document.getElementById("stop").onclick = operatorStop;
document.getElementById("assist").onclick = async () => {
  centerStick();
  const thisIntent = ++intent;
  try { if (await selectManual(thisIntent, true)) sendDrive(); }
  catch (error) { modeLabel.textContent = "Camera assistance unavailable — check the Pi"; }
};
async function startAutomatic(roaming) {
  const thisIntent = ++intent;
  centerStick();
  try {
    const state = await refreshState();
    if (thisIntent !== intent) return;
    const reply = await post(roaming ? "/roam/start" : "/follow/start", {epoch: String(state.epoch)});
    if (!reply.ok) { modeLabel.textContent = "Press STOP, then try again"; return; }
    const started = await reply.json();
    if (thisIntent !== intent) return;
    if (document.hidden) { await operatorStop(); return; }
    followToken = started.follow_token;
    modeLabel.textContent = roaming ? "Lidar roaming requested" : "Line following requested";
    setTimeout(async () => {
      if (thisIntent !== intent) return;
      try {
        const current = await refreshState();
        if (thisIntent === intent && current.mode === "stopped")
          modeLabel.textContent = "Run stopped or unavailable — check the Pi and sensor, then press STOP to retry";
      } catch (error) { /* The heartbeat watchdog handles connection loss. */ }
    }, 3000);
  } catch (error) {
    modeLabel.textContent = "Connection lost — reconnect and select control again";
  }
}
document.getElementById("follow").onclick = () => startAutomatic(false);
document.getElementById("roam").onclick = () => startAutomatic(true);
window.addEventListener("blur", () => {if (manualSession || followToken) operatorStop();});
window.addEventListener("pagehide", () => {if (manualSession || followToken) operatorStop();});
document.addEventListener("visibilitychange", () => {
  if (document.hidden && (manualSession || followToken)) operatorStop();
});

setInterval(async () => {
  if (!followToken || document.hidden) return;
  const sentToken = followToken;
  try {
    const reply = await post("/follow/heartbeat", {session: sentToken});
    if (!reply.ok && followToken === sentToken) followToken = "";
  } catch (error) { if (followToken === sentToken) followToken = ""; }
}, 400);

// A manual page refreshes only its own valid manual session.
setInterval(sendDrive, 100);
setInterval(() => refreshState().catch(() => {}), 500);
refreshState().catch(() => {});

// Read-only sensor views. Range data never drives the robot from this page.
const mapCanvas = document.getElementById("lidarCanvas");
const mapStatus = document.getElementById("mapStatus");
const mapCard = document.getElementById("mapCard");
const mapRange = document.getElementById("mapRange");
const camera = document.getElementById("camera");
const cameraStatus = document.getElementById("cameraStatus");
let selectedView = "lidar";
let latestScan = null;
let lidarPending = false;
let cameraTimer;

function drawLidar(scan) {
  const context = mapCanvas.getContext("2d");
  if (!context) return;
  const size = Math.max(240, Math.round(mapCanvas.getBoundingClientRect().width || 300));
  const ratio = Math.min(2, window.devicePixelRatio || 1);
  mapCanvas.width = Math.round(size * ratio);
  mapCanvas.height = Math.round(size * ratio);
  context.setTransform(ratio, 0, 0, ratio, 0, 0);
  const middle = size / 2;
  const rangeCm = Number(mapRange.value) || 200;
  const scale = size * .44 / rangeCm;
  const sensorY = middle - (scan.sensor_forward_cm || 8) * scale;

  context.fillStyle = "#0b171e";
  context.fillRect(0, 0, size, size);
  context.strokeStyle = "#25414a";
  context.lineWidth = 1;
  context.font = "10px monospace";
  context.fillStyle = "#8aa9b0";
  for (let ring = 1; ring <= 4; ring++) {
    const radius = size * .44 * ring / 4;
    context.beginPath();
    context.arc(middle, middle, radius, 0, Math.PI * 2);
    context.stroke();
    context.fillText((rangeCm * ring / 400).toFixed(1) + " m", middle + 5, middle - radius - 4);
  }
  context.beginPath();
  context.moveTo(middle, 8);
  context.lineTo(middle, size - 8);
  context.moveTo(8, middle);
  context.lineTo(size - 8, middle);
  context.stroke();

  const points = [];
  for (let i = 0; i < 72; i++) {
    const steps = parseInt(scan.bins.slice(i * 2, i * 2 + 2), 16);
    if (!steps) { points.push(null); continue; }
    const cm = steps * 5;
    const angle = i * Math.PI / 36;
    const x = middle + Math.sin(angle) * cm * scale;
    const y = sensorY - Math.cos(angle) * cm * scale;
    points.push(x >= 2 && x <= size - 2 && y >= 2 && y <= size - 2 ? {x, y, cm} : null);
  }
  if (scan.fresh) {
    context.lineWidth = 1.3;
    context.strokeStyle = "#478d91";
    for (let i = 0; i < 72; i++) {
      const a = points[i], b = points[(i + 1) % 72];
      if (!a || !b || Math.abs(a.cm - b.cm) > 25 + Math.min(a.cm, b.cm) * .15) continue;
      context.beginPath();
      context.moveTo(a.x, a.y);
      context.lineTo(b.x, b.y);
      context.stroke();
    }
  }
  for (const point of points) {
    if (!point) continue;
    context.beginPath();
    context.arc(point.x, point.y, point.cm < 40 ? 2.7 : 1.8, 0, Math.PI * 2);
    context.fillStyle = point.cm < 40 ? "#f0a46c" : "#8bd4d0";
    context.fill();
  }

  // Chassis and scanner share one robot-centered coordinate frame.
  context.beginPath();
  context.arc(middle, middle, 15 * scale, 0, Math.PI * 2);
  context.strokeStyle = "#d7e1df";
  context.lineWidth = 1.5;
  context.stroke();
  context.beginPath();
  context.moveTo(middle, middle - 16 * scale);
  context.lineTo(middle - 6 * scale, middle + 3 * scale);
  context.lineTo(middle + 6 * scale, middle + 3 * scale);
  context.stroke();
  context.beginPath();
  context.arc(middle, sensorY, 3, 0, Math.PI * 2);
  context.fillStyle = "#d7e1df";
  context.fill();
  context.fillStyle = "#a9c8ce";
  context.fillText("FWD 000°", middle - 24, 17);
}

async function refreshLidar() {
  if (lidarPending || selectedView !== "lidar" || document.hidden) return;
  lidarPending = true;
  try {
    const reply = await fetch("/lidar", {cache: "no-store"});
    if (!reply.ok) throw new Error("LiDAR unavailable");
    const scan = await reply.json();
    if (typeof scan.bins !== "string" || !/^[0-9A-F]{144}$/.test(scan.bins))
      throw new Error("Invalid LiDAR data");
    latestScan = scan;
    drawLidar(scan);
    mapCard.className = "map-card" + (scan.fresh ? "" : " stale");
    const hasReturns = /[1-9A-F]/.test(scan.bins);
    const returns = (scan.bins.match(/.{2}/g) || []).filter(value => value !== "00").length;
    mapStatus.textContent = scan.fresh
      ? (hasReturns ? "LIVE / " + scan.age_ms + " ms / " + returns + " returns"
                    : "SCAN ACTIVE / NO RETURNS")
      : (hasReturns ? "STALE / CHECK PI + C1" : "WAITING FOR C1 SCAN");
  } catch (error) {
    mapCard.className = "map-card stale";
    mapStatus.textContent = "DISCONNECTED / CHECK PI LINK";
  } finally {
    lidarPending = false;
  }
}

function requestFrame() {
  if (selectedView === "camera" && !document.hidden)
    camera.src = "/frame?t=" + Date.now();
}
camera.onload = () => {
  cameraStatus.textContent = "Camera connected";
  cameraTimer = setTimeout(requestFrame, 450);
};
camera.onerror = () => {
  cameraStatus.textContent = "Camera preview is not enabled on the Pi";
  cameraTimer = setTimeout(requestFrame, 1200);
};
function selectView(view) {
  selectedView = view;
  document.getElementById("lidarPanel").hidden = view !== "lidar";
  document.getElementById("cameraPanel").hidden = view !== "camera";
  document.getElementById("viewLidar").className = view === "lidar" ? "selected" : "";
  document.getElementById("viewCamera").className = view === "camera" ? "selected" : "";
  clearTimeout(cameraTimer);
  if (view === "camera") requestFrame();
  else refreshLidar().catch(() => {});
}
document.getElementById("viewLidar").onclick = () => selectView("lidar");
document.getElementById("viewCamera").onclick = () => selectView("camera");
mapRange.onchange = () => { if (latestScan) drawLidar(latestScan); };
setInterval(() => refreshLidar().catch(() => {}), 250);
setTimeout(() => refreshLidar().catch(() => {}), 0);

</script>
</body>
</html>
)ARGUS";

// HTTP HANDLERS

void handleHome() {
  server.send_P(200, "text/html", PAGE_HTML);
}

const char* modeName() {
  if (control.mode == DriveMode::Manual) return "manual";
  if (control.mode == DriveMode::Automatic) return "auto";
  return "stopped";
}

void formatState(char* response, size_t capacity, bool includeSession = false,
                 uint32_t requestId = 0, int status = 200) {
  phoneStart.expire(millis(), control.epoch, control.mode == DriveMode::Stopped);
  char token[17];
  char followToken[17];
  snprintf(token, sizeof(token), "%08lx%08lx",
           (unsigned long)(control.session >> 32), (unsigned long)(control.session & 0xffffffff));
  snprintf(followToken, sizeof(followToken), "%08lx%08lx",
           (unsigned long)(phoneStart.requestToken >> 32), (unsigned long)(phoneStart.requestToken & 0xffffffff));
  snprintf(response, capacity,
           "{\"mode\":\"%s\",\"epoch\":%lu,\"reason\":\"%s\","
           "\"lease_ms\":%lu,\"max_auto_percent\":%d,\"left\":%d,\"right\":%d,"
           "\"request_id\":%lu,\"status\":%d,\"follow_pending\":%s,\"follow_token\":\"%s\","
           "\"follow_kind\":\"%s\",\"assist\":%s,\"guard\":\"%s\",\"guard_latched\":%s%s%s%s}",
           modeName(), (unsigned long)control.epoch, control.reason,
           (unsigned long)DriveControl::TimeoutMs, DriveControl::AutoLimit,
           control.left, control.right, (unsigned long)requestId, status,
           phoneStart.pending ? "true" : "false", phoneStart.pending ? followToken : "",
           phoneStart.roaming ? "roam" : "tape",
           manualGuard.selected ? "true" : "false", manualGuard.state(millis()), manualGuard.latched ? "true" : "false",
           includeSession ? ",\"session\":\"" : "",
           includeSession ? token : "", includeSession ? "\"" : "");
}

void sendState(bool includeSession = false) {
  char response[768];
  formatState(response, sizeof(response), includeSession);
  server.sendHeader("Cache-Control", "no-store");
  server.send(200, "application/json", response);
}

bool parseUnsigned(const String& value, uint32_t& result) {
  if (!value.length() || value.length() > 10) return false;
  for (size_t i = 0; i < value.length(); ++i) {
    if (value[i] < '0' || value[i] > '9') return false;
  }
  errno = 0;
  char* end = nullptr;
  unsigned long long number = strtoull(value.c_str(), &end, 10);
  if (errno || *end || number > UINT32_MAX) return false;
  result = (uint32_t)number;
  return true;
}

bool readUnsigned(const char* key, uint32_t& result) {
  return server.hasArg(key) && parseUnsigned(server.arg(key), result);
}

bool parseToken(const String& value, uint64_t& result) {
  if (value.length() != 16) return false;
  for (size_t i = 0; i < value.length(); ++i) {
    char c = value[i];
    if (!((c >= '0' && c <= '9') || (c >= 'a' && c <= 'f') || (c >= 'A' && c <= 'F'))) return false;
  }
  errno = 0;
  char* end = nullptr;
  result = strtoull(value.c_str(), &end, 16);
  return !errno && !*end && result != 0;
}

bool readToken(uint64_t& result) {
  return server.hasArg("session") && parseToken(server.arg("session"), result);
}

bool parsePercent(const String& value, int limit, int& result) {
  if (!value.length() || value.length() > 4) return false;
  size_t digit = value[0] == '-' ? 1 : 0;
  if (digit == value.length()) return false;
  for (; digit < value.length(); ++digit) {
    if (value[digit] < '0' || value[digit] > '9') return false;
  }
  char* end = nullptr;
  long number = strtol(value.c_str(), &end, 10);
  if (*end || number < -limit || number > limit) return false;
  result = (int)number;
  return true;
}

bool readPercent(const char* key, int limit, int& result) {
  return server.hasArg(key) && parsePercent(server.arg(key), limit, result);
}

void writeControlBytes(const uint8_t* bytes, size_t count, bool viaGPIO) {
  if (viaGPIO) Serial1.write(bytes, count);
  else Serial.write(bytes, count);
}

void processControlPacket(char* payload, bool viaGPIO) {
  char* parts[7];
  size_t count = 0;
  char* position = payload;
  do {
    if (count == 7) return;
    parts[count++] = position;
    char* comma = strchr(position, ',');
    if (!comma) break;
    *comma = '\0';
    position = comma + 1;
  } while (true);

  uint32_t requestId = 0, epoch = 0, sequence = 0;
  uint64_t token = 0;
  int left = 0, right = 0, status = 400;
  bool includeSession = false;
  bool includeGuardToken = false;
  updateMotors();
  if (count >= 2 && parseUnsigned(String(parts[0]), requestId)) {
    if (strcmp(parts[1], "state") == 0 && count == 2) {
      status = 200;
    } else if (viaGPIO && strcmp(parts[1], "garm") == 0 && count == 3 &&
               parseUnsigned(String(parts[2]), epoch)) {
      if (epoch != control.epoch) status = 409;
      else {
        token = ((uint64_t)esp_random() << 32) | esp_random();
        manualGuard.connect(token ? token : 1);
        if (manualGuard.tick(control, millis())) sendImmediateStop();
        status = 200; includeGuardToken = true;
      }
    } else if (viaGPIO && strcmp(parts[1], "gupdate") == 0 && count == 5 &&
               parseToken(String(parts[2]), token) && parseUnsigned(String(parts[3]), sequence) &&
               parsePercent(String(parts[4]), 2, left) && left >= 0) {
      status = manualGuard.report(token, sequence, left, millis()) ? 200 : 409;
      if (manualGuard.tick(control, millis())) sendImmediateStop();
    } else if (strcmp(parts[1], "claim") == 0 && count == 4 &&
               parseUnsigned(String(parts[2]), epoch) && parseToken(String(parts[3]), token)) {
      status = phoneStart.claim(epoch, token, control.epoch,
                                control.mode == DriveMode::Stopped, millis()) ? 200 : 409;
    } else if (strcmp(parts[1], "arm") == 0 && count == 3 &&
               parseUnsigned(String(parts[2]), epoch)) {
      token = ((uint64_t)esp_random() << 32) | esp_random();
      if (!token) token = 1;
      if (control.arm(DriveMode::Automatic, epoch, token, millis())) {
        manualGuard.selected = false;
        sendImmediateStop();
        lastMotorSend = millis();
        status = 200;
        includeSession = true;
      } else {
        status = 409;
      }
    } else if (strcmp(parts[1], "drive") == 0 && count == 6 &&
               parseToken(String(parts[2]), token) &&
               parseUnsigned(String(parts[3]), sequence) &&
               parsePercent(String(parts[4]), DriveControl::AutoLimit, left) &&
               parsePercent(String(parts[5]), DriveControl::AutoLimit, right)) {
      status = control.command(DriveMode::Automatic, token, sequence, left, right, millis())
                   ? 204 : 409;
    } else if (strcmp(parts[1], "stop") == 0 && count == 3 &&
               parseToken(String(parts[2]), token)) {
      if (control.stopAutomatic(token, millis())) {
        sendImmediateStop();
        lastMotorSend = millis();
        status = 200;
      } else {
        status = 409;
      }
    }
  }
  char response[768];
  formatState(response, sizeof(response), includeSession, requestId, status);
  if (includeGuardToken) {
    size_t length = strlen(response);
    snprintf(response + length - 1, sizeof(response) - length + 1,
             ",\"guard_token\":\"%08lx%08lx\"}",
             (unsigned long)(manualGuard.token >> 32), (unsigned long)(manualGuard.token & 0xffffffff));
  }
  const uint8_t marker[] = {'A', 'V', 'R', '1'};
  uint32_t length = strlen(response);
  uint8_t lengthBytes[4];
  for (int i = 0; i < 4; ++i) lengthBytes[i] = (length >> (8 * i)) & 0xff;
  writeControlBytes(marker, sizeof(marker), viaGPIO);
  writeControlBytes(lengthBytes, sizeof(lengthBytes), viaGPIO);
  writeControlBytes((const uint8_t*)response, length, viaGPIO);
}

void handleState() {
  updateMotors();
  sendState();
}

void handleLidar() {
  char encoded[LidarMap::BinCount * 2 + 1];
  lidarMap.encodeHex(encoded);
  uint32_t now = millis();
  char response[256];
  snprintf(response, sizeof(response),
           "{\"fresh\":%s,\"age_ms\":%lu,\"step_deg\":5,\"unit_cm\":5,\"sensor_forward_cm\":8,\"bins\":\"%s\"}",
           lidarMap.fresh(now) ? "true" : "false",
           (unsigned long)lidarMap.age(now), encoded);
  server.sendHeader("Cache-Control", "no-store");
  server.send(200, "application/json", response);
}

void handleFollowStart(bool roaming = false) {
  updateMotors();
  uint32_t expectedEpoch;
  if (!readUnsigned("epoch", expectedEpoch)) {
    server.send(400, "text/plain", "Current epoch required");
    return;
  }
  uint64_t token = ((uint64_t)esp_random() << 32) | esp_random();
  if (!token) token = 1;
  if (!phoneStart.request(expectedEpoch, control.epoch, control.mode == DriveMode::Stopped,
                          millis(), token, roaming)) {
    server.send(409, "text/plain", "Press Stop and select control again");
    return;
  }
  phoneSessionActive = true;
  phoneLastHeartbeat = millis();
  sendState();
}

void handleFollowHeartbeat() {
  updateMotors();
  uint64_t token;
  if (!readToken(token) || !phoneSessionActive || token != phoneStart.requestToken) {
    server.send(409, "text/plain", "Phone session ended");
    return;
  }
  phoneLastHeartbeat = millis();
  server.send(204, "text/plain", "");
}

void handleArm(DriveMode mode, bool assisted = false) {
  updateMotors();
  uint32_t expectedEpoch;
  if (!readUnsigned("epoch", expectedEpoch)) {
    server.send(400, "text/plain", "Current epoch required");
    return;
  }
  if (assisted && !manualGuard.clear(millis())) {
    if (expectedEpoch == control.epoch) {
      manualGuard.selected = true;
      manualGuard.latched = true;
      control.stop(manualGuard.code == 1 ? "Camera obstacle; assisted drive stopped"
                                        : "Camera unavailable; assisted drive stopped");
      sendImmediateStop();
    }
    server.send(409, "text/plain", "Camera guard must report a fresh clear view");
    return;
  }
  uint64_t token = ((uint64_t)esp_random() << 32) | esp_random();
  if (!token) token = 1;
  if (!control.arm(mode, expectedEpoch, token, millis())) {
    server.send(409, "text/plain", "State changed; select control again");
    return;
  }
  manualGuard.selected = assisted;
  if (assisted) manualGuard.latched = false;
  sendImmediateStop();
  lastMotorSend = millis();
  sendState(true);
}

void handleCommand(DriveMode mode) {
  updateMotors();
  uint32_t sequence;
  uint64_t token;
  int left, right;
  int limit = mode == DriveMode::Automatic ? DriveControl::AutoLimit : 100;
  if (!readToken(token) || !readUnsigned("seq", sequence) ||
      !readPercent("l", limit, left) || !readPercent("r", limit, right)) {
    server.send(400, "text/plain", "Valid session, sequence and wheel percentages required");
    return;
  }
  if (mode == DriveMode::Manual && manualGuard.selected && !manualGuard.permits(left, right, millis())) {
    if (control.mode == mode && control.session == token) {
      manualGuard.latched = true;
      control.stop("Assisted drive requires clear view and forward 0-35 commands");
      sendImmediateStop();
    }
    server.send(409, "text/plain", "Assisted drive blocked");
    return;
  }
  if (!control.command(mode, token, sequence, left, right, millis())) {
    server.send(409, "text/plain", "Control session expired, superseded or sequence already used");
    return;
  }
  server.send(204, "text/plain", "");
}

void handleStop() {
  control.stop("Operator stop; select control again");
  sendImmediateStop();
  lastMotorSend = millis();
  sendState();
}

void handleAutoStop() {
  updateMotors();
  uint64_t token;
  if (!readToken(token)) {
    server.send(400, "text/plain", "Valid automatic session required");
    return;
  }
  if (!control.stopAutomatic(token, millis())) {
    server.send(409, "text/plain", "Automatic session is no longer current");
    return;
  }
  sendImmediateStop();
  lastMotorSend = millis();
  sendState();
}

void handleFrame() {

  if (!frameReady ||
      millis() - frameTime > 3000) {
    server.send(503, "text/plain", "No fresh frame");
    return;
  }

  server.sendHeader("Cache-Control", "no-store");
  server.setContentLength(activeLength);
  server.send(200, "image/jpeg", "");

  WiFiClient client = server.client();

  size_t sent = 0;
  unsigned long start = millis();

  // Send image in chunks to avoid large writes
  while (sent < activeLength &&
         millis() - start < 80) {

    size_t chunk = activeLength - sent;
    if (chunk > 1024) chunk = 1024;

    updateMotors();
    size_t n = client.write(
      jpegBuffers[activeFrame] + sent,
      chunk
    );

    if (n == 0) break;
    sent += n;
  }
}

// SETUP

void setup() {

  // USB serial: Orange Pi JPEG data
  // Must enlarge buffer BEFORE begin()
  Serial.setRxBufferSize(32768);
  Serial.begin(CAMERA_BAUD);
  Serial1.setRxBufferSize(512);
  Serial1.begin(PI_BAUD, SERIAL_8N1, PI_RX_PIN, PI_TX_PIN);

  // Motor commands use UART2.
  Serial2.begin(
    MEGA_BAUD,
    SERIAL_8N1,
    MEGA_RX_PIN,
    MEGA_TX_PIN
  );

  WiFi.mode(WIFI_AP);
  WiFi.softAP(AP_SSID, AP_PASS);

  server.on("/", HTTP_GET, handleHome);
  server.on("/drive", HTTP_GET, []() { handleCommand(DriveMode::Manual); });
  server.on("/drive", HTTP_POST, []() { handleCommand(DriveMode::Manual); });
  server.on("/state", HTTP_GET, handleState);
  server.on("/lidar", HTTP_GET, handleLidar);
  server.on("/follow/start", HTTP_POST, []() { handleFollowStart(false); });
  server.on("/roam/start", HTTP_POST, []() { handleFollowStart(true); });
  server.on("/follow/heartbeat", HTTP_POST, handleFollowHeartbeat);
  server.on("/manual/arm", HTTP_POST, []() { handleArm(DriveMode::Manual); });
  server.on("/assist/arm", HTTP_POST, []() { handleArm(DriveMode::Manual, true); });
  server.on("/auto/arm", HTTP_POST, []() { handleArm(DriveMode::Automatic); });
  server.on("/auto/drive", HTTP_POST, []() { handleCommand(DriveMode::Automatic); });
  server.on("/auto/stop", HTTP_POST, handleAutoStop);
  server.on("/stop", HTTP_POST, handleStop);
  server.on("/frame", HTTP_GET, handleFrame);

  server.begin();

  control.reset(esp_random());
  lastMotorSend = millis();

  // Start stopped
  sendImmediateStop();
}

// MAIN LOOP

void loop() {

  // Send motor commands before and after camera/HTTP work.
  updateMotors();

  // Read incoming JPEG bytes
  receiveCamera();
  receiveGpioControl();

  // Handle browser requests
  server.handleClient();

  updateMotors();

  delay(1);
}
