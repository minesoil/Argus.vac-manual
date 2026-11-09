"""
bench_synth.py - Synthetic-camera benchmark for Argus Vac obstacle-detector pipelines.

Runs the REAL threaded pipeline (real MediaPipe EfficientDet-Lite2 inference) against
a deterministic synthetic 640x480 @30fps camera source, and measures where time goes.

Variants:
  v8 = current design: capture -> [resize 640x480 -> 1280x720 upscale] -> RGB -> detect,
       render thread re-encodes JPEG every tick regardless of frame freshness.
  v9 = candidate:      capture -> detect on NATIVE 640x480 (no upscale, no distortion),
       render re-encodes only when a NEW frame arrived, results published even when empty.

Usage:
  python bench_synth.py --variant v8 --seconds 15
  python bench_synth.py --variant v9 --seconds 15
"""
import argparse
import threading
import time

import cv2
import numpy as np

import mediapipe as mp
from mediapipe.tasks.python import BaseOptions
from mediapipe.tasks.python import vision

MODEL_PATH = "efficientdet_lite2.tflite"
CONF = 0.50
MAX_RESULTS = 5
JPEG_QUALITY = 60
TARGET_STREAM_FPS = 30
CAM_W, CAM_H, CAM_FPS = 640, 480, 30


# ----------------------------------------------------------------------------
# Synthetic camera: deterministic moving-shapes scene at CAM_FPS
# ----------------------------------------------------------------------------
class FakeCamera(threading.Thread):
    def __init__(self, stop_event):
        super().__init__(daemon=True)
        self.stop_event = stop_event
        self.lock = threading.Lock()
        self.frame = None
        self.seq = 0
        self.t_capture = 0.0
        self.read_ms_sum = 0.0
        self.n = 0
        self.base = np.zeros((CAM_H, CAM_W, 3), np.uint8)
        # static background texture (so JPEG has realistic content)
        cv2.rectangle(self.base, (0, 0), (CAM_W, CAM_H), (40, 40, 40), -1)
        for y in range(0, CAM_H, 40):
            cv2.line(self.base, (0, y), (CAM_W, y), (60, 60, 60), 1)

    def _compose(self, seq):
        f = self.base.copy()
        x = int((seq * 7) % (CAM_W - 120))
        y = int(CAM_H / 2 + 80 * np.sin(seq / 25.0))
        cv2.rectangle(f, (x, y), (x + 100, y + 160), (0, 180, 255), -1)
        x2 = CAM_W - int((seq * 11) % (CAM_W - 80))
        cv2.circle(f, (x2, 90), 35, (255, 120, 40), -1)
        return f

    def read(self):
        """Emulate cap.read(): frame produced at CAM_FPS, returns (ret, frame, seq, t)."""
        t0 = time.perf_counter()
        self.n += 1
        seq = self.seq + 1
        frame = self._compose(seq)
        self.seq = seq
        t = time.perf_counter()
        self.read_ms_sum += (time.perf_counter() - t0) * 1000.0
        # pace to CAM_FPS like a real UVC camera would
        target = self.n / CAM_FPS
        behind = target - (time.perf_counter() - self.t_start)
        if behind > 0:
            time.sleep(min(behind, 0.05))
        return True, frame, seq, t

    def run(self):
        self.t_start = time.perf_counter()
        while not self.stop_event.is_set():
            ret, frame, seq, t = self.read()
            if not ret:
                continue
            with self.lock:
                self.frame = frame
                self.t_capture = t
                self.seq_pub = seq


# ----------------------------------------------------------------------------
# Shared state (mirrors production layout)
# ----------------------------------------------------------------------------
class Shared:
    def __init__(self):
        self.frame_lock = threading.Lock()
        self.frame = None
        self.seq = 0
        self.t_capture = 0.0
        self.result_lock = threading.Lock()
        self.dets = []
        self.jpeg_lock = threading.Lock()
        self.jpeg = None
        self.jpeg_seq = -1
        self.e2e_samples = []


# ----------------------------------------------------------------------------
# Pipelines
# ----------------------------------------------------------------------------
def inference_loop(sh, cam, stop, variant, stats):
    last_ts = 0
    while not stop.is_set():
        with cam.lock:
            frame = None if cam.frame is None else cam.frame.copy()
            seq = getattr(cam, "seq_pub", 0)
        if frame is None:
            time.sleep(0.005)
            continue
        p0 = time.perf_counter()
        if variant == "v8":
            inf = cv2.resize(frame, (1280, 720))
        else:
            inf = frame  # v9: feed native resolution, no distortion, no wasted upscale
        rgb = cv2.cvtColor(inf, cv2.COLOR_BGR2RGB)
        p1 = time.perf_counter()
        img = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        ts = int(time.monotonic() * 1000)
        if ts <= last_ts:
            ts = last_ts + 1
        last_ts = ts
        res = DETECTOR.detect_for_video(img, ts)
        p2 = time.perf_counter()
        dets = res.detections if res else []
        with sh.result_lock:
            sh.dets = dets
        stats["pre_ms"].append((p1 - p0) * 1000.0)
        stats["infer_ms"].append((p2 - p1) * 1000.0)
        stats["n"] += 1


def render_loop(sh, cam, stop, variant, stats):
    interval = 1.0 / TARGET_STREAM_FPS
    last_encoded_seq = -1
    while not stop.is_set():
        t0 = time.perf_counter()
        with cam.lock:
            frame = None if cam.frame is None else cam.frame.copy()
            seq = getattr(cam, "seq_pub", 0)
            t_cap = cam.t_capture
        if frame is not None:
            with sh.result_lock:
                dets = list(sh.dets)
            _draw(frame, dets)
            do_encode = True if variant == "v8" else (seq != last_encoded_seq)
            if do_encode:
                ok, buf = cv2.imencode(".jpg", frame,
                                       [int(cv2.IMWRITE_JPEG_QUALITY), JPEG_QUALITY])
                e0 = time.perf_counter()
                if ok:
                    with sh.jpeg_lock:
                        sh.jpeg = buf.tobytes()
                        sh.jpeg_seq = seq
                last_encoded_seq = seq
                stats["enc_ms"].append((e0 - t0) * 1000.0 if False else (time.perf_counter() - t0) * 1000.0)
                stats["encoded"] += 1
                if t_cap > 0:
                    sh.e2e_samples.append((t0 - t_cap) * 1000.0)
            stats["ticks"] += 1
        dt = time.perf_counter() - t0
        time.sleep(max(0.0, interval - dt))


def _draw(frame, detections):
    h, w = frame.shape[:2]
    for d in detections:
        bb = d.bounding_box
        cat = d.categories[0]
        x1, y1 = int(bb.origin_x), int(bb.origin_y)
        cw, ch = int(bb.width), int(bb.height)
        cv2.rectangle(frame, (x1, y1), (x1 + cw, y1 + ch), (0, 255, 0), 2)
        name = cat.category_name or "?"
        cv2.putText(frame, f"{name} {cat.score*100:.0f}%", (max(2, x1), max(14, y1 - 6)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 1)


def capture_loop(sh, cam, stop, stats):
    while not stop.is_set():
        ret, frame, seq, t = cam.read()
        if not ret:
            continue
        with sh.frame_lock:
            sh.frame = frame
            sh.seq = seq
            sh.t_capture = t
        stats["captured"] += 1


def pct(vals, p):
    if not vals:
        return float("nan")
    s = sorted(vals)
    return s[min(len(s) - 1, int(len(s) * p))]


def main():
    global DETECTOR
    ap = argparse.ArgumentParser()
    ap.add_argument("--variant", choices=["v8", "v9"], required=True)
    ap.add_argument("--seconds", type=float, default=15.0)
    args = ap.parse_args()

    base = BaseOptions(model_asset_path=MODEL_PATH)
    opts = vision.ObjectDetectorOptions(
        base_options=base, score_threshold=CONF,
        running_mode=vision.RunningMode.VIDEO, max_results=MAX_RESULTS)
    t0 = time.perf_counter()
    DETECTOR = vision.ObjectDetector.create_from_options(opts)
    print(f"[init] detector loaded in {(time.perf_counter()-t0)*1000:.0f} ms")

    stop = threading.Event()
    cam = FakeCamera(stop)
    cam.start()
    time.sleep(0.3)

    sh = Shared()
    istats = {"pre_ms": [], "infer_ms": [], "n": 0}
    rstats = {"enc_ms": [], "encoded": 0, "ticks": 0}
    cstats = {"captured": 0}

    ths = [
        threading.Thread(target=capture_loop, args=(sh, cam, stop, cstats), daemon=True),
        threading.Thread(target=inference_loop, args=(sh, cam, stop, args.variant, istats), daemon=True),
        threading.Thread(target=render_loop, args=(sh, cam, stop, args.variant, rstats), daemon=True),
    ]
    for t in ths:
        t.start()

    print(f"[run] variant={args.variant} for {args.seconds}s ...")
    time.sleep(args.seconds)
    stop.set()
    for t in ths:
        t.join(timeout=2.0)
    DETECTOR.close()

    dur = args.seconds
    n_inf = max(1, istats["n"])
    print("\n================ RESULTS ================")
    print(f"[capture] {cstats['captured']/dur:6.1f} fps  ({cstats['captured']} frames)")
    print(f"[infer ] {istats['n']/dur:6.1f} Hz   preprocess avg={sum(istats['pre_ms'])/len(istats['pre_ms']) if istats['pre_ms'] else 0:5.2f} ms"
          f"  detect avg={sum(istats['infer_ms'])/len(istats['infer_ms']) if istats['infer_ms'] else 0:6.2f} ms"
          f"  p95={pct(istats['infer_ms'], 0.95):6.2f} ms  max={max(istats['infer_ms']) if istats['infer_ms'] else 0:6.2f} ms")
    enc = rstats["enc_ms"]
    print(f"[render] ticks={rstats['ticks']/dur:6.1f} Hz  encoded={rstats['encoded']/dur:6.1f} fps"
          f"  encode avg={sum(enc)/len(enc) if enc else 0:5.2f} ms")
    e = sh.e2e_samples
    if e:
        print(f"[e2e   ] capture->jpeg avg={sum(e)/len(e):5.1f} ms  p95={pct(e,0.95):6.1f} ms")
    print(f"[cam   ] compose avg={cam.read_ms_sum/max(1,cam.n):5.2f} ms/frame")


if __name__ == "__main__":
    main()
