#!/usr/bin/env python3
"""
Argus Vac - AI Object Detector (v8) For Orange Pi 5
Debugged and rewritten by Claude (Anthropic), working through the following issues with Justin over several sessions on 2026-08-24.

### ================================================================================ CHANGELOG / DEBUGGING HISTORY
1. The original script tried: from mediapipe.tasks.vision import ObjectDetectorOptions, ObjectDetector
   That module path doesn't exist in the installed package. Confirmed by inspecting the actual package layout on this machine - the vision classes live one level deeper: from mediapipe.tasks.python import vision, BaseOptions
   The wrong import silently raised ImportError, which is what caused the script to always fall through to its "legacy fallback" path below.

2. Current PyPI builds of mediapipe (0.10.x+, including the 1.0.1 build used here) no longer ship mediapipe.solutions at all.
   Confirmed: >>> import mediapipe.solutions
   ModuleNotFoundError: No module named 'mediapipe.solutions'
   So the original script's "hybrid" design (modern API with legacy fallback) had nothing to actually fall back TO. This version drops the legacy branch entirely and fixes the modern import instead.

3. lsusb showed the camera (10bb:2b08, "TM Technology USB CAMERA"), and dmesg/journalctl showed the kernel registering it as a UVC 1.00 device - but only its *input* interface (the shutter button), never a video interface.
   journalctl also showed repeated USB disconnect/reconnect cycles for the same device. This pattern is a classic symptom of insufficient USB power on SBCs: the control interface enumerates fine (low current draw), but the camera browns out negotiating the higher-current video streaming interface.
   FIX: Plugging the camera into a USB 3.0 port instead of USB 2.0 resolved it immediately - the 3.0 port supplies more current.

4. Since Justin works over VS Code Remote-SSH (no display attached to the Pi session), SHOW_GUI is now False by default. Instead this script runs a small built-in HTTP server (stdlib http.server, no Flask needed) that serves the annotated feed as an MJPEG stream. View it by forwarding STREAM_PORT in VS Code's "Ports" tab and opening http://localhost:8000/, or directly via http://<orange-pi-ip>:8000/ since the Pi and laptop are on the same Ethernet link.

5. Original loop did capture -> inference -> encode -> stream all serially in one thread, so the entire pipeline (including the VIDEO ITSELF) was capped at whatever speed inference ran. Fixes applied, in order of impact:
    *  Split into three independent threads: capture / inference / render. The render thread (what you actually see) now runs at a steady target FPS completely decoupled from how fast inference is - it just draws whatever the latest detection result is onto whatever the latest camera frame is. Detection boxes update whenever a new result is ready and simply "hold" between updates, instead of the whole video freezing while inference runs.
    *  Capture resolution dropped from 1280x720 to 640x480 (faster capture, encode, and network transfer).
    *  Camera forced to its own MJPG capture format (cv2.CAP_PROP_FOURCC) instead of raw YUYV, cutting USB bandwidth and CPU decode cost.
    *  cv2.CAP_PROP_BUFFERSIZE set to 1 so OpenCV always hands us the newest frame instead of a queued, stale one.
    *  Switched MediaPipe from RunningMode.IMAGE to RunningMode.VIDEO, which is built for continuous frame streams instead of re-initializing internal state on every single call.
    *  Removed artificial time.sleep() calls that were adding pure latency for no benefit once the pipeline was already CPU-bound.

6. Justin explicitly chose to stay CPU-only rather than set up RK3588 NPU acceleration (RKNN), which would have been the real "more accurate AND faster" lever. Within that constraint:
    *  Kept efficientdet_lite2 (the largest model Google officially hosts for the MediaPipe Tasks API - there's no lite3/lite4 in that bucket).
    *  Because inference is now decoupled from the visible video (see #5), it became "free" to feed the detector a larger 1280x720 upscaled copy of each frame for better accuracy on small/distant objects, while capture/display stay at 640x480. Detection box coordinates are scaled back down so they still line up on the smaller display frame.
    *  Suggested next steps if more accuracy is still needed: lower CONFIDENCE_THRESHOLD to catch lower-confidence true positives (trades against false positives), or fine-tune a custom model via MediaPipe Model Maker on Argus Vac's actual environment - COCO-pretrained lite2 isn't tuned for the specific obstacles a vacuum robot needs to avoid.

7. This script only detects and visualizes - it does not yet send anything to the Arduino Mega 2560 to actually control turning/motors. Justin wants obstacle proximity (closer = about to turn) to eventually drive motor behavior; that logic (serial link to the Arduino, translating box size/position into a turn command) hasn't been built yet.
================================================================================
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
    print("\n" + "="*70)
    print("  [FATAL ERROR] FAILED TO IMPORT OPENCV OR NUMPY")
    print("="*70)
    print(f"Details: {e}")
    print("\nThis is usually an ABI conflict between NumPy and OpenCV.")
    print("Fix:")
    print('  pip3 install "numpy<2" --break-system-packages')
    print("="*70 + "\n")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# --- IMPORT SAFETY NET FOR MEDIAPIPE ---
try:
    import mediapipe as mp
    from mediapipe.tasks.python import BaseOptions
    from mediapipe.tasks.python import vision
except ImportError as e:
    print("\n" + "="*70)
    print("  [FATAL ERROR] MEDIAPIPE TASKS API NOT AVAILABLE")
    print("="*70)
    print(f"Details: {e}")
    print("\nPlease (re)install mediapipe:")
    print("  pip3 install --force-reinstall mediapipe --break-system-packages")
    print("="*70 + "\n")
    sys.exit(1)

# --- CONFIGURATION ---
SHOW_GUI = False          # cv2.imshow needs a local display - not available over SSH.
STREAM_HTTP = True        # Serve the annotated feed as MJPEG over HTTP instead.
STREAM_PORT = 8000
CONFIDENCE_THRESHOLD = 0.50
MAX_RESULTS = 5

### Now safe to use the more accurate model - the threaded pipeline below means
### inference speed no longer caps the visible video framerate.
MODEL_FILENAME = "efficientdet_lite2.tflite"
MODEL_URL = "https://storage.googleapis.com/mediapipe-models/object_detector/efficientdet_lite2/float16/1/efficientdet_lite2.tflite"

CAPTURE_WIDTH = 640
CAPTURE_HEIGHT = 480

### Inference no longer blocks the video, so it's now free to feed the detector
### higher-resolution frames for better accuracy (especially on smaller/farther
### objects) without hurting perceived smoothness - it just costs a bit more
### time PER detection cycle, not per displayed frame. Try 1280x720 first.
INFERENCE_WIDTH = 1280
INFERENCE_HEIGHT = 720

JPEG_QUALITY = 60         # Lower = smaller frames over the network, less lag.
TARGET_STREAM_FPS = 30    # Caps the render/stream loop; independent of inference speed.

# --- SHARED STATE BETWEEN THREADS ---
# Guarded by their own locks since capture, inference, and render/stream all
# run concurrently and each only cares about the MOST RECENT value.
_frame_lock = threading.Lock()
_latest_raw_frame = None            # newest frame straight from the camera

_result_lock = threading.Lock()
_latest_detections = []             # newest detection result (list of detections)

_stream_lock = threading.Lock()
_latest_jpeg_bytes = None           # newest encoded+annotated frame for the HTTP server
_stop_event = threading.Event()

class _MJPEGHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # silence default HTTP request logging

    def do_GET(self):
        global _latest_jpeg_bytes
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'multipart/x-mixed-replace; boundary=frame')
            self.end_headers()
            try:
                while not _stop_event.is_set():
                    with _stream_lock:
                        jpeg_bytes = _latest_jpeg_bytes
                    if jpeg_bytes is None:
                        time.sleep(0.01)
                        continue
                    self.wfile.write(b'--frame\r\n')
                    self.send_header('Content-type', 'image/jpeg')
                    self.send_header('Content-length', str(len(jpeg_bytes)))
                    self.end_headers()
                    self.wfile.write(jpeg_bytes)
                    self.wfile.write(b'\r\n')
                    time.sleep(1.0 / TARGET_STREAM_FPS)
            except (ConnectionResetError, BrokenPipeError):
                pass
        else:
            self.send_error(404)

def start_stream_server():
    server = ThreadingHTTPServer(('0.0.0.0', STREAM_PORT), _MJPEGHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    print(f"[STREAM] MJPEG feed live at http://<orange-pi-ip>:{STREAM_PORT}/")
    print(f"[STREAM] Forward port {STREAM_PORT} in VS Code (Ports tab) then open "
          f"http://localhost:{STREAM_PORT}/ on your laptop.")
    return server

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

def _draw_detections(frame, detections, last_log_time_box):
    """Draws detection overlays on frame in-place. last_log_time_box is a single-element list used as a mutable float so callers can track console log throttling across calls."""
    scale_x = CAPTURE_WIDTH / INFERENCE_WIDTH
    scale_y = CAPTURE_HEIGHT / INFERENCE_HEIGHT
    
    for detection in detections:
        bbox = detection.bounding_box
        category = detection.categories[0]
        category_name = category.category_name
        score = category.score
        
        # Scale bounding box coordinates back down to CAPTURE_WIDTH x CAPTURE_HEIGHT (640x480)
        xmin = int(bbox.origin_x * scale_x)
        ymin = int(bbox.origin_y * scale_y)
        w = int(bbox.width * scale_x)
        h = int(bbox.height * scale_y)
        
        cx = int(xmin + w / 2)
        cy = int(ymin + h / 2)
        radius = int(max(w, h) / 4)
        radius = max(radius, 25)
        
        # Draw a circle on the object center (retaining Argus Vac styling)
        cv2.circle(frame, (cx, cy), radius, (0, 255, 0), 3)
        cv2.circle(frame, (cx, cy), 6, (0, 255, 0), -1)
        
        label_text = f"{category_name.upper()} ({score * 100:.0f}%)"
        text_size = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)[0]
        text_w, text_h = text_size[0], text_size[1]
        cv2.rectangle(frame, (cx - text_w // 2 - 5, cy - radius - 25), (cx + text_w // 2 + 5, cy - radius), (0, 0, 0), -1)
        cv2.putText(frame, label_text, (cx - text_w // 2, cy - radius - 8),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
        current_time = time.time()
        if current_time - last_log_time_box[0] > 1.0:
            print(f"[AI ALERT] {category_name} | Confidence: {score*100:.1f}% | Coordinates: ({cx}, {cy})")
            last_log_time_box[0] = current_time

def _capture_thread_fn(cap):
    """Continuously reads frames from the camera as fast as it can and publishes only the newest one. Never blocked by inference or streaming."""
    global _latest_raw_frame
    while not _stop_event.is_set():
        ret, frame = cap.read()
        if not ret:
            time.sleep(0.05)
            continue
        with _frame_lock:
            _latest_raw_frame = frame

def _inference_thread_fn(detector):
    """Continuously runs detection on whatever the newest frame is, back to back, with no artificial delay. Publishes results as they complete. Naturally self-paces to however fast the model actually runs - never queues up stale work."""
    global _latest_raw_frame, _latest_detections
    last_timestamp_ms = 0
    while not _stop_event.is_set():
        # Get newest frame straight from camera
        with _frame_lock:
            frame = _latest_raw_frame.copy() if _latest_raw_frame is not None else None
        
        if frame is None:
            time.sleep(0.01)
            continue
            
        # Inference uses 1280x720 upscaled frame for better accuracy on small/distant objects
        inference_frame = cv2.resize(frame, (INFERENCE_WIDTH, INFERENCE_HEIGHT))
        rgb_frame = cv2.cvtColor(inference_frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        
        # We need a monotonically increasing timestamp in milliseconds for VIDEO mode
        current_timestamp_ms = int(time.time() * 1000)
        if current_timestamp_ms <= last_timestamp_ms:
            current_timestamp_ms = last_timestamp_ms + 1
        last_timestamp_ms = current_timestamp_ms
        
        # Switched MediaPipe from RunningMode.IMAGE to RunningMode.VIDEO
        # In VIDEO mode, detect_for_video takes the mp_image and timestamp
        detection_result = detector.detect_for_video(mp_image, current_timestamp_ms)
        
        if detection_result and detection_result.detections:
            with _result_lock:
                _latest_detections = detection_result.detections

def _render_thread_fn(stream_server_active):
    """Draws the latest detections onto the latest frame and republishes it at a steady target rate for display/streaming. This is what determines perceived smoothness - decoupled entirely from inference speed."""
    global _latest_raw_frame, _latest_detections, _latest_jpeg_bytes
    last_log_time_box = [0.0]
    frame_interval = 1.0 / TARGET_STREAM_FPS
    
    while not _stop_event.is_set():
        start_time = time.time()
        
        with _frame_lock:
            frame = _latest_raw_frame.copy() if _latest_raw_frame is not None else None
            
        if frame is not None:
            with _result_lock:
                detections = list(_latest_detections)
                
            # Draw detections onto the frame (which is 640x480)
            _draw_detections(frame, detections, last_log_time_box)
            
            # Show GUI locally if configured
            if SHOW_GUI:
                cv2.imshow("Argus Vac - Google MediaPipe Object Detection (v8)", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    _stop_event.set()
                    break
                    
            # Encode frame to JPEG for HTTP stream
            if STREAM_HTTP and stream_server_active:
                ret, jpeg_buffer = cv2.imencode('.jpg', frame, [int(cv2.IMWRITE_JPEG_QUALITY), JPEG_QUALITY])
                if ret:
                    with _stream_lock:
                        _latest_jpeg_bytes = jpeg_buffer.tobytes()
                        
        elapsed = time.time() - start_time
        sleep_time = max(0.0, frame_interval - elapsed)
        time.sleep(sleep_time)

def run_detector():
    print("[AI Mode] Initializing MediaPipe Tasks API (EfficientDet-Lite2)...")
    
    # Configure base options
    base_options = BaseOptions(model_asset_path=MODEL_FILENAME)
    
    # Switched MediaPipe from RunningMode.IMAGE to RunningMode.VIDEO
    options = vision.ObjectDetectorOptions(
        base_options=base_options,
        score_threshold=CONFIDENCE_THRESHOLD,
        running_mode=vision.RunningMode.VIDEO,
        max_results=MAX_RESULTS
    )
    
    detector = vision.ObjectDetector.create_from_options(options)
    print("[AI Mode] Neural Network successfully loaded!")
    
    # Initialize camera capture
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Could not open USB camera.")
        detector.close()
        sys.exit(1)
        
    time.sleep(1.0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAPTURE_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAPTURE_HEIGHT)
    
    # Camera forced to MJPG capture format
    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
    # cv2.CAP_PROP_BUFFERSIZE set to 1 so OpenCV always hands us the newest frame
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    
    stream_server = None
    if STREAM_HTTP:
        stream_server = start_stream_server()
        
    # Start threads
    capture_thread = threading.Thread(target=_capture_thread_fn, args=(cap,), daemon=True)
    inference_thread = threading.Thread(target=_inference_thread_fn, args=(detector,), daemon=True)
    render_thread = threading.Thread(target=_render_thread_fn, args=(STREAM_HTTP,), daemon=True)
    
    capture_thread.start()
    inference_thread.start()
    render_thread.start()
    
    print("\n[INFO] AI pipeline is fully running across 3 independent threads!")
    print("[INFO] Perceived framerate is decoupled from inference speed.")
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
        capture_thread.join(timeout=1.0)
        inference_thread.join(timeout=1.0)
        render_thread.join(timeout=1.0)
        cap.release()
        detector.close()
        if stream_server:
            stream_server.shutdown()
        if SHOW_GUI:
            cv2.destroyAllWindows()
        print("[INFO] Shutdown complete. System in safe state.")

def main():
    print("=====================================================")
    print("   ARGUS VAC - OBJECT DETECTOR (v8)                  ")
    print("=====================================================")
    check_and_download_model()
    run_detector()

if __name__ == "__main__":
    main()
