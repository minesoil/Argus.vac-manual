#!/usr/bin/env python3
"""
Argus Vac - AI Object Detector (v9) For Orange Pi 5
Refined from v8 after actually running the pipeline under a controlled benchmark
(synthetic 30fps camera + real EfficientDet-Lite2 inference + real photo tests).
Harness and raw numbers: outputs/detector-refine/ (bench_synth.py, bench_accuracy.py).

=================================================================================
 WHAT CHANGED VS V8 - AND THE MEASUREMENTS THAT JUSTIFY EACH CHANGE
=================================================================================
1. INFERENCE NOW RUNS AT NATIVE 640x480. v8 upscaled every frame to 1280x720
   believing it improved small-object accuracy. Measured on real photos with the
   SAME model: detection sets are IDENTICAL (IoU 0.97-0.99 per box, scores within
   a couple of points; one image scored BETTER native). The model internally
   resizes to its own fixed input size anyway, so the upscale adds no information
   - it only burned CPU (2.2ms resize + a 4x bigger RGB copy every cycle) and
   stretched the camera's native 4:3 onto 16:9, distorting object shapes before
   detection (the "dog" test case lost ~7 points of confidence because of it).
   Benchmark: detect avg 140ms -> 107ms (+31% detection throughput), preprocess
   2.2ms -> 0.24ms, p95 tail 187ms -> 121ms.

2. STALE-BOX BUG FIXED. v8 only published results when detections were NON-empty,
   so once an object left the scene its box stayed on screen forever. Results are
   now published every cycle, including empty ones.

3. FLICKER-FREE TRACKING (new). Raw detector output jitters frame to frame.
   v9 adds cheap temporal smoothing: boxes are matched by class+IoU across cycles
   and EMA-smoothed; a missed detection holds the last box for DETECTION_HOLD_MS
   before it disappears. Steadier geometry = better input for the future Arduino
   proximity/turn logic. Cost is microseconds for <=MAX_RESULTS boxes.

4. NO WASTED ENCODES. The render thread re-encoded JPEG even when the camera
   hadn't delivered a new frame (e.g., low light drops UVC cameras to ~15fps while
   the stream still burns 30 encodes/s). Frames now carry a sequence number and
   JPEG encoding happens only when that number advances.

5. CAMERA CONFIG IS VERIFIED AND SELF-HEALING. After setup the script reads back
   what the driver ACTUALLY applied (resolution/FPS/PixelFormat) and warns loudly
   if the camera silently fell back (e.g., YUYV instead of MJPG caps USB cameras at
   ~15fps at this resolution and eats USB/CPU budget). Repeated read failures
   trigger an automatic camera re-open instead of spinning on a dead handle.

6. CPU HEADROOM ON THE PI. Back-to-back inference saturates cores that capture,
   JPEG encode and the stream server also need. INFERENCE_MAX_HZ (default 10)
   caps the detection cycle rate - far above what motor control needs, but stops
   inference from monopolizing the SoC when frames arrive faster than useful.
   Set to None to restore unlimited back-to-back behavior.

7. MONOTONIC TIMESTAMPS for MediaPipe VIDEO mode (wall-clock jumps from NTP could
   break detect_for_video's strictly-increasing requirement), plus periodic one-line
   STATS (cam/infer/render fps, latencies) printed every few seconds and served at
   http://<pi>:8000/stats so bottlenecks are visible over SSH without a debugger.
=================================================================================
"""

import sys
import os
import time
import threading
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

# --- IMPORT SAFETY NET FOR OPENCV / NUMPY ---
try:
    import cv2
    import numpy as np
except ImportError as e:
    print("\n" + "=" * 70)
    print("  [FATAL ERROR] FAILED TO IMPORT OPENCV OR NUMPY")
    print("=" * 70)
    print(f"Details: {e}")
    print("\nThis is usually an ABI conflict between NumPy and OpenCV.")
    print("Fix:")
    print('  pip3 install "numpy<2" --break-system-packages')
    print("=" * 70 + "\n")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# --- IMPORT SAFETY NET FOR MEDIAPIPE ---
try:
    import mediapipe as mp
    from mediapipe.tasks.python import BaseOptions
    from mediapipe.tasks.python import vision
except ImportError as e:
    print("\n" + "=" * 70)
    print("  [FATAL ERROR] MEDIAPIPE TASKS API NOT AVAILABLE")
    print("=" * 70)
    print(f"Details: {e}")
    print("\nPlease (re)install mediapipe:")
    print("  pip3 install --force-reinstall mediapipe --break-system-packages")
    print("=" * 70 + "\n")
    sys.exit(1)

# --- CONFIGURATION ---
SHOW_GUI = False            # cv2.imshow needs a local display - not available over SSH.
STREAM_HTTP = True          # Serve the annotated feed as MJPEG over HTTP instead.
STREAM_PORT = 8000

CAMERA_INDEX = 0
CAPTURE_WIDTH = 640         # Camera capture size. Also the INFERENCE size (see header #1):
CAPTURE_HEIGHT = 480        # native-aspect input measured just as accurate as upscaling.

CONFIDENCE_THRESHOLD = 0.50
MAX_RESULTS = 5
MODEL_FILENAME = "efficientdet_lite2.tflite"
MODEL_URL = ("https://storage.googleapis.com/mediapipe-models/object_detector/"
             "efficientdet_lite2/float16/1/efficientdet_lite2.tflite")

JPEG_QUALITY = 60           # Lower = smaller frames over the network, less lag.
TARGET_STREAM_FPS = 30      # Caps the render/stream loop; independent of inference speed.

INFERENCE_MAX_HZ = 10       # Cap detection cycles/second to leave CPU headroom on the Pi
                            # (header #6). None = unlimited back-to-back inference.

SMOOTH_ALPHA = 0.5          # EMA weight of each new measurement (higher = snappier boxes).
TRACK_MATCH_IOU = 0.20      # Min IoU for two boxes (same class) to count as the same object.
DETECTION_HOLD_MS = 300     # Keep showing a briefly-missed object this long before clearing.

STATS_INTERVAL_S = 5.0      # How often the one-line pipeline stats are printed/served.
RECOVER_AFTER_FAILS = 30    # Consecutive failed cap.read() calls before reopening the camera.


# --- SHARED STATE BETWEEN THREADS ---
_frame_lock = threading.Lock()
_latest_raw_frame = None        # newest frame straight from the camera
_latest_frame_seq = 0           # increments on every NEW camera frame
_latest_frame_time = 0.0        # perf_counter timestamp of that frame

_result_lock = threading.Lock()
_latest_tracks = []             # smoothed detection records in CAPTURE/display space:
                                # [{"name": str, "score": float, "box": [x, y, w, h]}]

_stream_lock = threading.Lock()
_latest_jpeg_bytes = None
_stop_event = threading.Event()

# --- LIGHTWEIGHT STATS COUNTERS (for the status line / /stats endpoint) ---
_stats_lock = threading.Lock()
_stats = {
    "cam_frames": 0, "inf_cycles": 0, "enc_frames": 0, "render_ticks": 0,
    "inf_ms_sum": 0.0, "inf_ms_max": 0.0, "pre_ms_sum": 0.0,
    "e2e_sum": 0.0, "e2e_n": 0, "recoveries": 0,
}
_stats_window_start = time.perf_counter()
_e2e_samples = []               # small ring buffer for percentile-ish reporting


def _stat(**deltas):
    with _stats_lock:
        for k, v in deltas.items():
            if k == "inf_ms":
                _stats["inf_cycles"] += 1
                _stats["inf_ms_sum"] += v
                _stats["inf_ms_max"] = max(_stats["inf_ms_max"], v)
            elif k == "pre_ms":
                _stats["pre_ms_sum"] += v
            elif k == "e2e_ms":
                _stats["e2e_sum"] += v
                _stats["e2e_n"] += 1
                _e2e_samples.append(v)
                if len(_e2e_samples) > 100:
                    _e2e_samples.pop(0)
            else:
                _stats[k] = _stats.get(k, 0) + v


def _format_stats_line():
    """Snapshot counters into a one-line rate summary."""
    global _stats_window_start
    now = time.perf_counter()
    with _stats_lock:
        dur = max(1e-6, now - _stats_window_start)
        s = dict(_stats)
        e2e = sorted(_e2e_samples)
        _stats.update({"cam_frames": 0, "render_ticks": 0, "enc_frames": 0})
        _stats_window_start = now
    cam_fps = s["cam_frames"] / dur
    inf_hz = s["inf_cycles"] / dur
    inf_avg = s["inf_ms_sum"] / s["inf_cycles"] if s["inf_cycles"] else 0.0
    enc_fps = s["enc_frames"] / dur
    render_hz = s["render_ticks"] / dur
    e2e_avg = sum(e2e) / len(e2e) if e2e else 0.0
    e2e_p95 = e2e[int(len(e2e) * 0.95)] if e2e else 0.0
    return (f"[stats] cam={cam_fps:5.1f}fps  infer={inf_hz:4.1f}Hz(avg {inf_avg:6.1f} ms,"
            f" max {s['inf_ms_max']:6.1f} ms)  render={render_hz:5.1f}Hz  encode={enc_fps:5.1f}fps"
            f"  e2e avg={e2e_avg:5.1f}/p95={e2e_p95:5.1f} ms  recoveries={s['recoveries']}")


# ============================================================================
# DETECTION RECORD HELPERS (pure functions - unit-testable without hardware)
# ============================================================================

def iou(a, b):
    """Intersection-over-union of [x, y, w, h] boxes."""
    ax1, ay1, aw, ah = a
    bx1, by1, bw, bh = b
    ix1, iy1 = max(ax1, bx1), max(ay1, by1)
    ix2, iy2 = min(ax1 + aw, bx1 + bw), min(ay1 + ah, by1 + bh)
    iw, ih = max(0.0, ix2 - ix1), max(0.0, iy2 - iy1)
    inter = iw * ih
    union = aw * ah + bw * bh - inter
    return inter / union if union > 0 else 0.0


def detections_to_records(detections, scale_x=1.0, scale_y=1.0):
    """Convert MediaPipe detections to plain records scaled into display space."""
    records = []
    for d in detections or []:
        cats = getattr(d, "categories", None)
        if not cats:
            continue
        bb = d.bounding_box
        records.append({
            "name": cats[0].category_name or "object",
            "score": float(cats[0].score),
            "box": [bb.origin_x * scale_x, bb.origin_y * scale_y,
                    bb.width * scale_x, bb.height * scale_y],
        })
    return records


def update_tracks(tracks, new_records, now_ms):
    """
    Match new raw records against existing tracks (class + IoU), EMA-smooth the
    matched ones, add unmatched as new tracks, expire stale ones after
    DETECTION_HOLD_MS. Mutates `tracks` in place; returns a deep-enough snapshot
    for rendering.
    """
    matched = set()
    for rec in new_records:
        best_i, best_v = -1, TRACK_MATCH_IOU
        for i, t in enumerate(tracks):
            if i in matched or t["name"] != rec["name"]:
                continue
            v = iou(t["box"], rec["box"])
            if v > best_v:
                best_v, best_i = v, i
        if best_i >= 0:
            t = tracks[best_i]
            matched.add(best_i)
            a = SMOOTH_ALPHA
            t["box"] = [a * n + (1 - a) * o for n, o in zip(rec["box"], t["box"])]
            t["score"] = a * rec["score"] + (1 - a) * t["score"]
            t["last_seen_ms"] = now_ms
        else:
            tracks.append({**rec, "last_seen_ms": now_ms})

    alive = [t for t in tracks if now_ms - t["last_seen_ms"] <= DETECTION_HOLD_MS]
    tracks[:] = alive
    return [{**t} for t in alive]


def draw_tracks(frame, tracks):
    """Draw smoothed tracks on a BGR frame in-place (capture-resolution space)."""
    fh, fw = frame.shape[:2]
    for t in tracks:
        x, y, w, h = (int(v) for v in t["box"])
        x, y = max(0, x), max(0, y)
        x2, y2 = min(fw - 1, x + w), min(fh - 1, y + h)
        cx, cy = (x + x2) // 2, (y + y2) // 2

        cv2.rectangle(frame, (x, y), (x2, y2), (0, 255, 0), 2)
        cv2.circle(frame, (cx, cy), 6, (0, 255, 0), -1)

        label = f"{t['name'].upper()} ({t['score'] * 100:.0f}%)"
        ts = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)[0]
        lx = max(2, min(cx - ts[0] // 2, fw - ts[0] - 4))       # clamp inside frame
        ly = y - 8
        if ly - ts[1] < 2:                                      # label would clip top
            ly = y2 + ts[1] + 8                                  # flip below the box
        ly = min(ly, fh - 4)
        cv2.rectangle(frame, (lx - 4, ly - ts[1] - 6), (lx + ts[0] + 4, ly + 2), (0, 0, 0), -1)
        cv2.putText(frame, label, (lx, ly), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


# ============================================================================
# HTTP STREAM SERVER (MJPEG feed + /stats endpoint)
# ============================================================================

class _MJPEGHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # silence default HTTP request logging

    def do_GET(self):
        if self.path == "/stats":
            body = (_format_stats_line() + "\n").encode("utf-8")
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.send_header("Content-length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "multipart/x-mixed-replace; boundary=frame")
            self.end_headers()
            try:
                while not _stop_event.is_set():
                    with _stream_lock:
                        jpeg_bytes = _latest_jpeg_bytes
                    if jpeg_bytes is None:
                        time.sleep(0.01)
                        continue
                    self.wfile.write(b"--frame\r\n")
                    self.send_header("Content-type", "image/jpeg")
                    self.send_header("Content-length", str(len(jpeg_bytes)))
                    self.end_headers()
                    self.wfile.write(jpeg_bytes)
                    self.wfile.write(b"\r\n")
                    time.sleep(1.0 / TARGET_STREAM_FPS)
            except (ConnectionResetError, BrokenPipeError):
                pass
        else:
            self.send_error(404)


def start_stream_server():
    server = ThreadingHTTPServer(("0.0.0.0", STREAM_PORT), _MJPEGHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    print(f"[STREAM] MJPEG feed live at http://<orange-pi-ip>:{STREAM_PORT}/")
    print(f"[STREAM] Pipeline stats at http://<orange-pi-ip>:{STREAM_PORT}/stats")
    print(f"[STREAM] Forward port {STREAM_PORT} in VS Code (Ports tab) then open "
          f"http://localhost:{STREAM_PORT}/ on your laptop.")
    return server


# ============================================================================
# MODEL + CAMERA SETUP
# ============================================================================

def check_and_download_model():
    if not os.path.exists(MODEL_FILENAME):
        print(f"[MODEL] '{MODEL_FILENAME}' not found locally. Downloading...")
        try:
            def progress(count, block_size, total_size):
                percent = int(count * block_size * 100 / total_size)
                sys.stdout.write(f"\rDownloading model: {percent}% complete")
                sys.stdout.flush()
            urllib.request.urlretrieve(MODEL_URL, MODEL_FILENAME, progress)
            print(f"\n[MODEL] Download complete! Saved as '{MODEL_FILENAME}'")
        except Exception as e:
            print(f"\n[ERROR] Failed to download model automatically: {e}")
            print(f"Please manually download the model file from:\n  {MODEL_URL}")
            sys.exit(1)
    else:
        print(f"[MODEL] Found local model '{MODEL_FILENAME}'. Ready to load.")


def _fourcc_to_str(value):
    return "".join(chr((int(value) >> (8 * i)) & 0xFF) for i in range(4))


def open_camera():
    """Opens CAMERA_INDEX, applies settings, VERIFIES what the driver chose."""
    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        return None

    time.sleep(0.5)  # let the UVC driver settle before configuring
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAPTURE_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAPTURE_HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, TARGET_STREAM_FPS)
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # always hand us the newest frame
    time.sleep(0.3)

    # Verify what the driver ACTUALLY applied - UVC cameras silently fall back.
    aw = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    ah = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    afps = cap.get(cv2.CAP_PROP_FPS)
    afmt = _fourcc_to_str(cap.get(cv2.CAP_PROP_FOURCC))
    print(f"[CAM ] Driver reports: {aw}x{ah} @ {afps:.0f}fps format={afmt!r}")
    if (aw, ah) != (CAPTURE_WIDTH, CAPTURE_HEIGHT):
        print(f"[CAM ] WARNING: requested {CAPTURE_WIDTH}x{CAPTURE_HEIGHT} but got {aw}x{ah}.")
    if "MJPG" not in afmt.upper():
        print("[CAM ] WARNING: not MJPG - likely YUYV fallback. That caps USB bandwidth")
        print("[CAM ] and can halve framerate. Try a different port/cable (USB 3.0).")
    return cap


# ============================================================================
# PIPELINE THREADS
# ============================================================================

def _capture_thread_fn(cap):
    """Reads frames as fast as the camera delivers them and publishes only the newest.
    Self-heals by reopening the camera after repeated failures."""
    fails = 0
    while not _stop_event.is_set():
        try:
            ret, frame = cap.read()
        except cv2.error:
            ret, frame = False, None
        if not ret:
            fails += 1
            if fails == RECOVER_AFTER_FAILS:
                print(f"[CAM ] {RECOVER_AFTER_FAILS} consecutive read failures - reopening camera...")
            if fails >= RECOVER_AFTER_FAILS:
                try:
                    cap.release()
                except Exception:
                    pass
                time.sleep(1.0)
                new_cap = open_camera()
                if new_cap is not None and new_cap.isOpened():
                    cap = new_cap
                    fails = 0
                    with _stats_lock:
                        _stats["recoveries"] += 1
                    print("[CAM ] Camera recovered.")
                continue
            time.sleep(0.01)
            continue
        fails = 0
        now = time.perf_counter()
        with _frame_lock:
            global _latest_raw_frame, _latest_frame_seq, _latest_frame_time
            _latest_raw_frame = frame
            _latest_frame_seq += 1
            _latest_frame_time = now
        _stat(cam_frames=1)


def _inference_thread_fn(detector):
    """Runs detection on whatever the newest frame is. Publishes EVERY cycle's result
    (including 'nothing found') so the display never shows ghost boxes."""
    global _latest_tracks
    last_timestamp_ms = 0
    alerted = {}  # class name -> last alert print time (throttle)

    while not _stop_event.is_set():
        cycle_start = time.perf_counter()

        with _frame_lock:
            frame = None if _latest_raw_frame is None else _latest_raw_frame.copy()

        if frame is None:
            time.sleep(0.01)
            continue

        # Native-resolution inference (header #1): no upscale, no distortion.
        p0 = time.perf_counter()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

        # Monotonic timestamps keep VIDEO mode happy even if wall clock jumps (NTP).
        current_timestamp_ms = int(time.monotonic() * 1000)
        if current_timestamp_ms <= last_timestamp_ms:
            current_timestamp_ms = last_timestamp_ms + 1
        last_timestamp_ms = current_timestamp_ms

        result = detector.detect_for_video(mp_image, current_timestamp_ms)
        infer_ms = (time.perf_counter() - p0) * 1000.0
        pre_ms = (p0 - cycle_start) * 1000.0

        # Convert to plain records in display space (scale is 1:1 at native res,
        # but kept generic so INFERENCE_* != CAPTURE_* still works if ever needed).
        scale_x = CAPTURE_WIDTH / float(CAPTURE_WIDTH)
        scale_y = CAPTURE_HEIGHT / float(CAPTURE_HEIGHT)
        records = detections_to_records(result.detections, scale_x, scale_y)

        now_ms = time.monotonic() * 1000.0
        with _result_lock:
            snapshot = update_tracks(_latest_tracks, records, now_ms)

        # Throttled per-class alerts (replaces v8's log-inside-render-loop).
        for rec in records:
            prev = alerted.get(rec["name"], 0.0)
            if time.monotonic() - prev > 1.0:
                x, y, w, h = rec["box"]
                print(f"[AI ALERT] {rec['name']} | Confidence: {rec['score']*100:.1f}% | "
                      f"Center: ({int(x + w/2)}, {int(y + h/2)}) | Size: {int(w)}x{int(h)}")
                alerted[rec["name"]] = time.monotonic()

        _stat(pre_ms=pre_ms, inf_ms=infer_ms)

        # Optional pacing so inference leaves CPU for capture/encode/stream (header #6).
        if INFERENCE_MAX_HZ:
            budget = 1.0 / INFERENCE_MAX_HZ
            spent = time.perf_counter() - cycle_start
            if spent < budget:
                time.sleep(budget - spent)


def _render_thread_fn(stream_server_active):
    """Draws latest tracks onto latest frame at a steady target FPS. Encodes JPEG only
    when a NEW camera frame arrived - no wasted CPU re-encoding stale pixels."""
    global _latest_jpeg_bytes
    last_encoded_seq = -1
    frame_interval = 1.0 / TARGET_STREAM_FPS

    while not _stop_event.is_set():
        tick_start = time.perf_counter()

        with _frame_lock:
            frame = None if _latest_raw_frame is None else _latest_raw_frame.copy()
            seq = _latest_frame_seq
            t_capture = _latest_frame_time

        if frame is not None:
            with _result_lock:
                tracks = [{**t} for t in _latest_tracks]

            draw_tracks(frame, tracks)

            if SHOW_GUI:
                cv2.imshow("Argus Vac - Object Detection (v9)", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    _stop_event.set()
                    break

            if STREAM_HTTP and stream_server_active and seq != last_encoded_seq:
                ok, buf = cv2.imencode(".jpg", frame,
                                       [int(cv2.IMWRITE_JPEG_QUALITY), JPEG_QUALITY])
                if ok:
                    with _stream_lock:
                        _latest_jpeg_bytes = buf.tobytes()
                    if t_capture > 0:
                        _stat(e2e_ms=(tick_start - t_capture) * 1000.0)
                last_encoded_seq = seq
                _stat(enc_frames=1)

        _stat(render_ticks=1)
        elapsed = time.perf_counter() - tick_start
        time.sleep(max(0.0, frame_interval - elapsed))


def _stats_thread_fn():
    """Prints one compact line every STATS_INTERVAL_S so SSH users see pipeline health."""
    while not _stop_event.is_set():
        time.sleep(STATS_INTERVAL_S)
        if _stop_event.is_set():
            break
        print(_format_stats_line())


# ============================================================================
# MAIN
# ============================================================================

def run_detector():
    print("[AI Mode] Initializing MediaPipe Tasks API (EfficientDet-Lite2)...")

    base_options = BaseOptions(model_asset_path=MODEL_FILENAME)
    options = vision.ObjectDetectorOptions(
        base_options=base_options,
        score_threshold=CONFIDENCE_THRESHOLD,
        running_mode=vision.RunningMode.VIDEO,
        max_results=MAX_RESULTS
    )

    detector = vision.ObjectDetector.create_from_options(options)
    print("[AI Mode] Neural Network successfully loaded!")

    cap = open_camera()
    if cap is None:
        print("[ERROR] Could not open USB camera.")
        detector.close()
        sys.exit(1)

    stream_server = None
    if STREAM_HTTP:
        stream_server = start_stream_server()

    threads = [
        threading.Thread(target=_capture_thread_fn, args=(cap,), daemon=True),
        threading.Thread(target=_inference_thread_fn, args=(detector,), daemon=True),
        threading.Thread(target=_render_thread_fn, args=(STREAM_HTTP,), daemon=True),
        threading.Thread(target=_stats_thread_fn, daemon=True),
    ]
    for t in threads:
        t.start()

    print("\n[INFO] v9 pipeline running: capture / inference / render / stats threads.")
    print(f"[INFO] Inference at native {CAPTURE_WIDTH}x{CAPTURE_HEIGHT}, capped at "
          f"{INFERENCE_MAX_HZ or 'unlimited'} Hz.")
    if STREAM_HTTP:
        print(f"[INFO] View stream at http://localhost:{STREAM_PORT}/ via VS Code Port Forwarding.")
    else:
        print("[INFO] Showing local desktop GUI. Press 'q' to exit.")

    try:
        while not _stop_event.is_set():
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n[INFO] KeyboardInterrupt received. Shutting down gracefully...")
    finally:
        _stop_event.set()
        for t in threads:
            t.join(timeout=1.0)
        cap.release()
        detector.close()
        if stream_server:
            stream_server.shutdown()
        if SHOW_GUI:
            cv2.destroyAllWindows()
        print("[INFO] Shutdown complete. System in safe state.")


def main():
    print("=====================================================")
    print("   ARGUS VAC - OBJECT DETECTOR (v9)                  ")
    print("=====================================================")
    check_and_download_model()
    run_detector()


if __name__ == "__main__":
    main()
