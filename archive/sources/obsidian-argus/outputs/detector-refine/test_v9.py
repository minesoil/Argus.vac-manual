"""
test_v9.py - Validates obstacle-detector-mediapipe-v9.py

Part A: unit tests of the pure pipeline logic (IoU matching, EMA smoothing,
        hold-TTL expiry, coordinate scaling, drawing).
Part B: integrated smoke test running v9's REAL capture/inference/render threads
        against a fake camera + the REAL EfficientDet-Lite2 model.
"""
import importlib.util
import sys
import threading
import time

import cv2
import numpy as np

V9_PATH = r"[REDACTED_HOME_PATH]"
MODEL = "efficientdet_lite2.tflite"

spec = importlib.util.spec_from_file_location("v9", V9_PATH)
v9 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v9)

FAILURES = []


def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    print(f"  [{status}] {name}" + (f"  ({detail})" if detail else ""))
    if not cond:
        FAILURES.append(name)


# ============================================================================
print("\nPART A - unit tests of pipeline logic")
print("=" * 60)

# --- iou sanity ---
check("iou identical boxes = 1.0", abs(v9.iou([0, 0, 10, 10], [0, 0, 10, 10]) - 1.0) < 1e-9)
check("iou disjoint boxes = 0.0", v9.iou([0, 0, 10, 10], [100, 100, 10, 10]) == 0.0)
check("iou half overlap ~ 1/3",
      abs(v9.iou([0, 0, 10, 10], [5, 0, 10, 10]) - (50 / 150)) < 1e-9)

# --- detections_to_records scaling ---
class _BB:
    def __init__(s, x, y, w, h):
        s.origin_x, s.origin_y, s.width, s.height = x, y, w, h

class _Cat:
    def __init__(s):
        s.category_name, s.score = "person", 0.75

class _Det:
    def __init__(s):
        s.bounding_box = _BB(200, 150, 100, 80)
        s.categories = [_Cat()]

recs = v9.detections_to_records([_Det()], scale_x=640 / 1280, scale_y=480 / 720)
check("record scaled x0.5/y(2/3)",
      abs(recs[0]["box"][0] - 100) < 1e-6 and abs(recs[0]["box"][1] - 100) < 1e-6
      and abs(recs[0]["box"][2] - 50) < 1e-6 and abs(recs[0]["box"][3] - (80 * 480 / 720)) < 1e-6,
      f"box={recs[0]['box']}")
check("record name/score kept", recs[0]["name"] == "person" and recs[0]["score"] == 0.75)
check("None-safe on empty input", v9.detections_to_records(None) == [])

# --- update_tracks: match + smooth ---
tracks = []
t_ms = 1000.0
snap = v9.update_tracks(tracks, [{"name": "dog", "score": 0.8, "box": [10, 10, 40, 40]}], t_ms)
check("new record becomes track", len(snap) == 1 and snap[0]["name"] == "dog")
# same object moved slightly -> should MATCH and smooth halfway (alpha=0.5)
snap = v9.update_tracks(tracks, [{"name": "dog", "score": 0.6, "box": [20, 20, 40, 40]}], t_ms + 30)
b = snap[0]["box"]
check("matched track smoothed halfway", abs(b[0] - 15) < 1e-6 and abs(b[1] - 15) < 1e-6,
      f"box={b}")
check("score EMA averaged", abs(snap[0]["score"] - 0.7) < 1e-6, f"score={snap[0]['score']:.3f}")

# different class far away -> separate track
snap = v9.update_tracks(tracks, [{"name": "chair", "score": 0.9, "box": [400, 300, 80, 120]}],
                        t_ms + 60)
check("unmatched record adds second track", len(snap) == 2)
check("snapshot is a copy (mutating it is safe)", snap[0] is not tracks[0])

# --- hold-TTL expiry (ghost-box fix) ---
snap_more = v9.update_tracks(tracks, [], t_ms + 60 + 100)          # 160ms since last seen
check("track still held within DETECTION_HOLD_MS", len(snap_more) == 2,
      f"{len(snap_more)} tracks @ +160ms")
snap_gone = v9.update_tracks(tracks, [], t_ms + 60 + v9.DETECTION_HOLD_MS + 50)
check("tracks expired after DETECTION_HOLD_MS (ghost fix)", len(snap_gone) == 0,
      f"{len(snap_gone)} tracks @ +{v9.DETECTION_HOLD_MS + 50}ms")

# --- drawing smoke test incl. top-edge label clamp ---
frame = np.zeros((480, 640, 3), np.uint8)
v9.draw_tracks(frame, [
    {"name": "person", "score": 0.83, "box": [5, 2, 120, 90]},     # label must flip below
    {"name": "cat", "score": 0.51, "box": [600, 400, 80, 70]},     # near right/bottom edge
])
check("draw_tracks renders without exception", frame.sum() > 0)

# ============================================================================
print("\nPART B - integrated run of v9's real threads (fake camera + real model)")
print("=" * 60)

from mediapipe.tasks.python import BaseOptions
from mediapipe.tasks.python import vision

opts = vision.ObjectDetectorOptions(
    base_options=BaseOptions(model_asset_path=MODEL),
    score_threshold=v9.CONFIDENCE_THRESHOLD,
    running_mode=vision.RunningMode.VIDEO,
    max_results=v9.MAX_RESULTS)
det = vision.ObjectDetector.create_from_options(opts)


class FakeCap:
    """Stands in for cv2.VideoCapture: moving-shapes 640x480 @30fps."""
    def __init__(self):
        self.seq = 0
        self.base = np.full((480, 640, 3), 45, np.uint8)
        self.t0 = time.perf_counter()
        self.n = 0

    def isOpened(self):
        return True

    def read(self):
        self.n += 1
        f = self.base.copy()
        x = int((self.seq * 7) % 500)
        cv2.rectangle(f, (x, 200), (x + 110, 340), (0, 180, 255), -1)
        self.seq += 1
        target = self.n / 30.0
        behind = target - (time.perf_counter() - self.t0)
        if behind > 0:
            time.sleep(min(behind, 0.05))
        return True, f

    def release(self):
        pass


fake = FakeCap()
stop = v9._stop_event
threads = [
    threading.Thread(target=v9._capture_thread_fn, args=(fake,), daemon=True),
    threading.Thread(target=v9._inference_thread_fn, args=(det,), daemon=True),
    threading.Thread(target=v9._render_thread_fn, args=(True,), daemon=True),
]
for th in threads:
    th.start()

# Seed a fake track so we can watch it get EXPIRED by real (empty) inference cycles.
with v9._result_lock:
    v9._latest_tracks.append({"name": "ghost", "score": 0.99,
                              "box": [300, 240, 60, 60], "last_seen_ms": 0.0})

RUN_S = 10
print(f"[run] {RUN_S}s ...")
time.sleep(RUN_S)
stop.set()
for th in threads:
    th.join(timeout=2.0)
det.close()

with v9._stats_lock:
    st = dict(v9._stats)
dur = RUN_S
cam_fps = st["cam_frames"] / dur
enc_fps = st["enc_frames"] / dur
inf_hz = st["inf_cycles"] / dur
e2e = sorted(v9._e2e_samples)
e2e_avg = sum(e2e) / len(e2e) if e2e else 0

print(f"\n  cam={cam_fps:.1f}fps  encode={enc_fps:.1f}fps  infer={inf_hz:.1f}Hz  "
       f"e2e avg={e2e_avg:.1f}ms")

check(f"capture alive ({st['cam_frames']} frames)", cam_fps > 10)
check(f"encode tracks new frames only ({st['enc_frames']} encoded vs {st['cam_frames']} captured)",
      0.5 * cam_fps <= enc_fps <= cam_fps * 1.05)
check("e2e latency actually measured", len(v9._e2e_samples) > 50)
check("inference cycles ran", inf_hz > 1)
check("seeded ghost track EXPIRED via real empty results",
      all(t["name"] != "ghost" for t in v9._latest_tracks))
check("no camera recoveries needed", st["recoveries"] == 0)
check("stats line formats cleanly", "cam=" in v9._format_stats_line())

print("\n" + "=" * 60)
if FAILURES:
    print(f"RESULT: {len(FAILURES)} FAILURE(S): {FAILURES}")
    sys.exit(1)
print("RESULT: ALL TESTS PASSED")
