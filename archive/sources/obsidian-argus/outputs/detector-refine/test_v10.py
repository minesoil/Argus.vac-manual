"""
test_v10.py - Validates obstacle-detector-mediapipe-v10.6.py

Part A: unit tests of the unknown-obstacle layer's pure functions.
Part B: integrated two-phase run of v10's REAL threads against a fake camera:
        phase A = clean floor (must stay quiet), phase B = debris appears
        (must be flagged as OBSTACLE?). Also measures anomaly-layer cost.
"""
import importlib.util
import sys
import threading
import time

import cv2
import numpy as np

V10_PATH = r"[REDACTED_HOME_PATH]"
MODEL = "efficientdet_lite2.tflite"

spec = importlib.util.spec_from_file_location("v10", V10_PATH)
v10 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v10)

FAILURES = []


def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    print(f"  [{status}] {name}" + (f"  ({detail})" if detail else ""))
    if not cond:
        FAILURES.append(name)


# ============================================================================
print("\nPART A - unit tests")
print("=" * 60)

# --- chromaticity block features: uniform grey -> flat chroma, zero texture ---
small = np.full((120, 160, 3), (90, 90, 90), np.uint8)
c1, c2, tex = v10.block_features(small)
gh, gw = 12, 16
check("feature shapes", c1.shape == (gh, gw) and tex.shape == (gh, gw))
check("uniform grey -> equal channel shares (~85), texture ~0",
      abs(float(np.mean(c1)) - 85.0) < 3.0 and abs(float(np.mean(c2)) - 85.0) < 3.0
      and float(np.max(tex)) < 3.0,
      f"c1={float(np.mean(c1)):.1f} c2={float(np.mean(c2)):.1f} maxTex={float(np.max(tex)):.2f}")

# shadow invariance: dimming every channel must NOT move chromaticity
dim = (small.astype(np.int16) // 2).astype(np.uint8)
c1d, c2d, _ = v10.block_features(dim)
check("shadow (uniform dimming) leaves chromaticity unchanged",
      abs(float(np.mean(c1)) - float(np.mean(c1d))) < 1.5
      and abs(float(np.mean(c2)) - float(np.mean(c2d))) < 1.5)

# --- floor model fit + flagging on synthetic feature fields ---
rng = np.random.default_rng(7)
frames_H, frames_S, frames_T = [], [], []
roi_mask = np.zeros((gh, gw), bool)
roi_mask[int(gh * v10.ANOMALY_ROI_TOP_FRAC):, :] = True
last_full = None
for _ in range(25):
    noisy = np.full((120, 160, 3), (90, 88, 92), np.uint8)
    noisy = np.clip(noisy.astype(np.int16) + rng.normal(0, 6, noisy.shape), 0, 255).astype(np.uint8)
    h_, s_, t_ = v10.block_features(noisy)
    frames_H.append(h_[roi_mask]); frames_S.append(s_[roi_mask]); frames_T.append(t_[roi_mask])
    last_full = (h_, s_, t_)
model = v10.fit_floor_model(frames_H, frames_S, frames_T)

clean_h, clean_s, clean_t = last_full

flags_clean = v10.flag_blocks(clean_h, clean_s, clean_t, model, roi_mask)
check("clean floor: near-zero false flags",
      int(np.count_nonzero(flags_clean)) <= 2,
      f"{int(np.count_nonzero(flags_clean))}/{int(np.count_nonzero(roi_mask))} blocks flagged")

# plant a real colored outlier (red cloth patch on grey floor)
frame_full = np.full((480, 640, 3), (95, 93, 97), np.uint8)
frame_full[340:420, 280:380] = (60, 60, 190)
small_full = cv2.resize(frame_full, (160, 120), interpolation=cv2.INTER_AREA)
fc1, fc2, ftex = v10.block_features(small_full)
flags_hit = v10.flag_blocks(fc1, fc2, ftex, model, roi_mask)
check("planted colored patch IS flagged", int(np.count_nonzero(flags_hit)) >= 2,
      f"{int(np.count_nonzero(flags_hit))} blocks")

# --- mask -> boxes scaling ---
mask = np.zeros((gh, gw), bool)
mask[8:10, 7:10] = True   # 2x3 blocks
merged = v10.mask_to_boxes(mask)
check("blob merged into one box", len(merged) == 1, f"{len(merged)} boxes")
box0, wb_, hb_ = merged[0]
check("block dims reported", (wb_, hb_) == (3, 2))
bx, by, bw, bh = box0
check("box scaled to full frame coords",
      bx > 100 and bw > 80, f"box={[round(v) for v in box0]}")
check("tiny blobs filtered (min_blocks)", len(v10.mask_to_boxes(
    np.pad(np.ones((1, 1), bool), ((0, 11), (0, 15)))) ) == 0)

# --- risk scoring ---
big_low = [240.0, 340.0, 160.0, 120.0]     # large, bottom-center
small_top = [300.0, 150.0, 40.0, 40.0]     # tiny, far away
stringy = [50.0, 400.0, 400.0, 12.0]       # cable-like ribbon
r_big, r_small, r_str = v10.box_risk(big_low), v10.box_risk(small_top), v10.box_risk(stringy)
check("bigger+near box riskier than small far box", r_big > r_small + 0.3,
      f"{r_big:.2f} vs {r_small:.2f}")
check("stringy shape gets tangle bonus", r_str >= 0.45, f"{r_str:.2f}")
check("risk clamped to 1.0", v10.box_risk([0.0, 300.0, 640.0, 180.0]) <= 1.0)

# --- dedup: AI-known box beats overlapping unknown box ---
known = [{"name": "person", "score": 0.9, "box": [100, 100, 100, 100], "kind": "known"}]
anoms = [
    {"name": "OBSTACLE?", "score": 0.5, "box": [110, 110, 80, 80], "kind": "unknown"},
    {"name": "OBSTACLE?", "score": 0.6, "box": [400, 300, 80, 80], "kind": "unknown"},
]
kept = v10.dedup_anomalies(known, anoms)
check("overlapping unknown removed, far unknown kept",
      len(kept) == 1 and kept[0]["box"][0] == 400.0)

# --- top threat selection ---
snap = [
    {"name": "OBSTACLE?", "score": 0.4, "box": [0, 0, 40, 40]},
    {"name": "person", "score": 0.9, "box": [200, 200, 60, 60]},
]
check("top threat = highest score", v10.pick_top_threat(snap)["score"] == 0.9)
check("top threat None-safe", v10.pick_top_threat([]) is None)

# --- 10.1 serial decision logic ---
st0 = {"name": None, "risk": None, "cx": None, "cy": None, "last_any": 0.0, "last_halt": 0.0}
threat_lo = {"name": "OBSTACLE?", "score": 0.5, "box": [300, 340, 80, 80]}
lines, st1 = v10.serial_decide(st0, threat_lo, now=100.0)
check("first threat sends exactly one R packet",
      len(lines) == 1 and lines[0].startswith("R OBSTACLE?") and " 50 " in lines[0],
      f"{lines}")
lines2, st2 = v10.serial_decide(st1, threat_lo, now=100.5)
check("unchanged threat inside 1s gap sends nothing", len(lines2) == 0)
lines3, st3 = v10.serial_decide(st1, threat_lo, now=101.5)
check("unchanged threat after gap still sends nothing (no change)", len(lines3) == 0)

threat_hi = {"name": "OBSTACLE?", "score": 0.92, "box": [300, 340, 80, 80]}
lines4, st4 = v10.serial_decide(st1, threat_hi, now=102.0)
check("risk jump >=0.1 triggers R AND auto-H at >=85%",
      any(l.startswith("R ") for l in lines4) and "H" in lines4, f"{lines4}")
lines5, st5 = v10.serial_decide(st4, threat_hi, now=103.0)
check("H not re-sent inside 3s window", "H" not in lines5)
lines6, st6 = v10.serial_decide(st4, threat_hi, now=106.0)
check("H re-asserted after 3s while threat persists", "H" in lines6)
lines7, _ = v10.serial_decide(st0, None, now=200.0)
check("no summary -> no packets", len(lines7) == 0)
try:
    v10._serial_send("R test 50 1 1")   # SERIAL_ENABLED=False -> silent no-op
    check("_serial_send is a safe no-op while disabled", True)
except Exception as e:
    check("_serial_send is a safe no-op while disabled", False, str(e))


# ============================================================================
print("\nPART B - integrated two-phase run (fake camera + real threads)")
print("=" * 60)

from mediapipe.tasks.python import BaseOptions
from mediapipe.tasks.python import vision

opts = vision.ObjectDetectorOptions(
    base_options=BaseOptions(model_asset_path=MODEL),
    score_threshold=v10.CONFIDENCE_THRESHOLD,
    running_mode=vision.RunningMode.VIDEO,
    max_results=v10.MAX_RESULTS)
det = vision.ObjectDetector.create_from_options(opts)


class DebrisCam:
    """640x480 @30fps. Phase A: clean carpet-like floor. Phase B: sock + cable."""
    def __init__(self):
        self.debris = False
        self.n = 0
        self.t0 = time.perf_counter()
        rng = np.random.default_rng(3)
        base = np.full((480, 640, 3), (95, 93, 97), np.uint8)
        stripes = ((np.arange(480) % 8 < 4)[..., None, None] * 6).astype(np.int16)  # subtle floor texture
        self.base = np.clip(base.astype(np.int16) + stripes - 3, 0, 255).astype(np.uint8)
        self.noise_sigma = 5

    def isOpened(self):
        return True

    def read(self):
        self.n += 1
        rng = np.random.default_rng(self.n)
        f = self.base.copy()
        f = np.clip(f.astype(np.int16) + rng.normal(0, self.noise_sigma, f.shape),
                    0, 255).astype(np.uint8)
        if self.debris:
            # grey wool sock: slightly darker + heavy speckle texture + soft outline
            x, y, w, h = 210, 300, 110, 85
            patch = f[y:y+h, x:x+w].copy()
            patch = np.clip(patch.astype(np.int16) - 22
                            + rng.normal(0, 26, patch.shape), 0, 255).astype(np.uint8)
            cv2.rectangle(patch, (0, 0), (w - 1, h - 1), (70, 68, 66), 2)
            f[y:y+h, x:x+w] = patch
            # phone-charger cable: thin dark line low in frame
            cv2.line(f, (40, 428), (610, 436), (55, 52, 50), 4)
        target = self.n / 30.0
        behind = target - (time.perf_counter() - self.t0)
        if behind > 0:
            time.sleep(min(behind, 0.05))
        return True, f

    def release(self):
        pass


cam = DebrisCam()
stop = v10._stop_event
threads = [
    threading.Thread(target=v10._capture_thread_fn, args=(cam,), daemon=True),
    threading.Thread(target=v10._inference_thread_fn, args=(det,), daemon=True),
    threading.Thread(target=v10._render_thread_fn, args=(False,), daemon=True),
]
for th in threads:
    th.start()

samples = []  # (phase, had_obstacle_track)


def sampler():
    while not stop.is_set():
        with v10._result_lock:
            names = [t["name"] for t in v10._latest_tracks]
        samples.append(("A" if not cam.debris else "B", "OBSTACLE?" in names))
        time.sleep(0.2)


samp_th = threading.Thread(target=sampler, daemon=True)
samp_th.start()

print("[run] Phase A: clean floor, 9s (boot + quiet period)...")
time.sleep(9)

with v10._result_lock:
    booted_ok = True  # engine state lives inside inference thread; infer via behavior
print("[run] Phase B: dropping sock + cable onto floor, 12s...")
cam.debris = True
time.sleep(12)

stop.set()
for th in threads:
    th.join(timeout=2.0)
det.close()

a_tail = [had for ph, had in samples if ph == "A"][-25:]
b_tail = [had for ph, had in samples if ph == "B"][-40:]
fp_rate = sum(a_tail) / max(1, len(a_tail))
hit_rate = sum(b_tail) / max(1, len(b_tail))

with v10._stats_lock:
    st = dict(v10._stats)
anom_avg = st["anom_ms_sum"] / st["anom_n"] if st["anom_n"] else 0.0

print(f"\n  false-alarm rate on clean floor : {fp_rate*100:5.1f}% of samples")
print(f"  debris detection rate           : {hit_rate*100:5.1f}% of samples")
print(f"  anomaly layer avg cost          : {anom_avg:5.2f} ms/cycle")
print(f"  inference cycles                : {st['inf_cycles']}")

check(f"quiet on clean floor (<=8% false alarms, got {fp_rate*100:.0f}%)", fp_rate <= 0.08)
check(f"debris flagged reliably (>=50% of samples, got {hit_rate*100:.0f}%)", hit_rate >= 0.5)
check(f"anomaly layer cheap ({anom_avg:.2f} ms << 50 ms budget)", anom_avg < 15.0)
check("inference cycles ran throughout", st["inf_cycles"] > 80)
check("no camera recoveries needed", st["recoveries"] == 0)

print("\n" + "=" * 60)
if FAILURES:
    print(f"RESULT: {len(FAILURES)} FAILURE(S): {FAILURES}")
    sys.exit(1)
print("RESULT: ALL TESTS PASSED")
