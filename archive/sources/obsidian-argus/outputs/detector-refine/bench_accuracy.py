"""
bench_accuracy.py - Does feeding native 640x480 (v9) lose accuracy vs the v8
1280x720 upscale path? Runs BOTH preprocessing variants through the SAME model
on real photos and compares classes, scores, box overlap (IoU) and latency.
"""
import time

import cv2
import numpy as np

from mediapipe.tasks.python import BaseOptions
from mediapipe.tasks.python import vision

MODEL_PATH = "efficientdet_lite2.tflite"
CONF = 0.50
IMAGES = ["person_street.jpg", "dog.jpg", "chair_room.jpg", "cat_laptop.jpg"]


def make_detector():
    opts = vision.ObjectDetectorOptions(
        base_options=BaseOptions(model_asset_path=MODEL_PATH),
        score_threshold=CONF, max_results=5,
        running_mode=vision.RunningMode.IMAGE)
    return vision.ObjectDetector.create_from_options(opts)


def detect(det, bgr):
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    img = __import__("mediapipe").Image(image_format=__import__("mediapipe").ImageFormat.SRGB, data=rgb)
    return det.detect(img)


def to_records(res, scale_x=1.0, scale_y=1.0):
    out = []
    if not res or not res.detections:
        return out
    for d in res.detections:
        bb = d.bounding_box
        c = d.categories[0]
        out.append({
            "name": c.category_name or "?",
            "score": c.score,
            "box": [bb.origin_x * scale_x, bb.origin_y * scale_y,
                    bb.width * scale_x, bb.height * scale_y],
        })
    return out


def iou(a, b):
    ax1, ay1, aw, ah = a; bx1, by1, bw, bh = b
    ax2, ay2, bx2, by2 = ax1 + aw, ay1 + ah, bx1 + bw, by1 + bh
    ix1, iy1 = max(ax1, bx1), max(ay1, by1)
    ix2, iy2 = min(ax2, bx2), min(ay2, by2)
    iw, ih = max(0, ix2 - ix1), max(0, iy2 - iy1)
    inter = iw * ih
    union = aw * ah + bw * bh - inter
    return inter / union if union > 0 else 0.0


def compare(recs_a, recs_b):
    """Greedy match A->B by class+IoU. Returns list of rows."""
    rows = []
    used_b = set()
    for ra in recs_a:
        best, bi = 0.0, -1
        for j, rb in enumerate(recs_b):
            if j in used_b or rb["name"] != ra["name"]:
                continue
            v = iou(ra["box"], rb["box"])
            if v > best:
                best, bi = v, j
        if bi >= 0 and best > 0.3:
            used_b.add(bi)
            rows.append((ra["name"], ra["score"], recs_b[bi]["score"], best))
        else:
            rows.append((ra["name"], ra["score"], None, None))
    for j, rb in enumerate(recs_b):
        if j not in used_b:
            rows.append((rb["name"], None, rb["score"], None))
    return rows


def main():
    import mediapipe as mp
    det_a = make_detector()   # v8 path: upscale to 1280x720
    det_b = make_detector()   # v9 path: native 640x480

    # Empirically confirm the model's internal input tensor size if runtime allows
    try:
        from ai_edge_litert.interpreter import Interpreter
        itp = Interpreter(model_path=MODEL_PATH, num_threads=1)
        itp.allocate_tensors()
        inp = itp.get_input_details()[0]["shape"]
        print(f"[model] input tensor shape: {inp}")
    except Exception as e:
        print(f"[model] (could not introspect input size: {e})")

    ta_total = tb_total = 0.0
    for name in IMAGES:
        img = cv2.imread(name)
        if img is None:
            print(f"!! could not read {name}")
            continue
        cam_frame = cv2.resize(img, (640, 480))  # simulated camera frame

        t0 = time.perf_counter()
        up = cv2.resize(cam_frame, (1280, 720))              # v8 distortion 4:3 -> 16:9
        ra = to_records(detect(det_a, up), 640 / 1280, 480 / 720)
        ta = time.perf_counter() - t0
        ta_total += ta

        t0 = time.perf_counter()
        rb = to_records(detect(det_b, cam_frame))            # v9 native aspect
        tb = time.perf_counter() - t0
        tb_total += tb

        print(f"\n--- {name} ---")
        print(f"{'class':<14} {'v8-upscale':>10} {'v9-native':>10} {'IoU':>6}")
        for cls, sa, sb, ov in sorted(compare(ra, rb)):
            sa_s = f"{sa*100:5.0f}%" if sa is not None else "   --"
            sb_s = f"{sb*100:5.0f}%" if sb is not None else "   --"
            ov_s = f"{ov:.2f}" if ov is not None else "  --"
            print(f"{cls:<14} {sa_s:>10} {sb_s:>10} {ov_s:>6}")
        print(f"latency: v8={ta*1000:6.1f} ms   v9={tb*1000:6.1f} ms")

    n = len(IMAGES)
    print(f"\n[AVERAGE] v8 upscale path: {ta_total/n*1000:.1f} ms | v9 native path: {tb_total/n*1000:.1f} ms")


if __name__ == "__main__":
    main()
