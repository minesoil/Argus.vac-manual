#!/usr/bin/env python3
"""
Argus Vac - Dual-Compatible AI Object Detector (v6 - Hybrid)
Developed by Gemini Notebook for Orange Pi 5

This script is engineered to be 100% robust against older/custom MediaPipe versions 
often found on ARM64 Single Board Computers like the Orange Pi 5.

It features an automatic HYBRID FALLBACK:
  - Mode 1 (Modern): Attempts to use the modern Google Tasks API (mediapipe.tasks.vision)
    with the high-accuracy EfficientDet-Lite2 model.
  - Mode 2 (Legacy Fallback): If Tasks is not found (MediaPipe < 0.10.0), it seamlessly
    falls back to the classic, highly optimized MediaPipe Solutions API (which runs
    beautifully on older ARM64 installs).
"""

import sys
import os
import time
import urllib.request

# --- IMPORT SAFETY NET FOR OPENCV / NUMPY ---
try:
    import cv2
    import numpy as np
except ImportError as e:
    print("\n" + "="*70)
    print("  [FATAL ERROR] FAILED TO IMPORT OPENCV OR NUMPY")
    print("="*70)
    print(f"Details: {e}")
    print("\nThis is usually caused by an ABI compatibility conflict between NumPy and OpenCV.")
    print("Specifically, on the Orange Pi 5, pre-compiled wheels for OpenCV may have been")
    print("compiled against NumPy 1.x, while your environment is running NumPy 2.x.")
    print("\nRecommended Fix:")
    print("  pip3 install \"numpy<2\" --break-system-packages")
    print("="*70 + "\n")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# --- CONFIGURATION ---
SHOW_GUI = True         # True: Opens the camera desktop GUI. False: Console-only logging.
CONFIDENCE_THRESHOLD = 0.50  # Detect objects with at least 50% confidence
MAX_RESULTS = 5              # Max simultaneous detections to track

# EfficientDet-Lite2 trades some speed for meaningfully better accuracy than Lite0
MODEL_FILENAME = "efficientdet_lite2.tflite"
MODEL_URL = "https://storage.googleapis.com/mediapipe-models/object_detector/efficientdet_lite2/float16/1/efficientdet_lite2.tflite"

CAPTURE_WIDTH = 1280
CAPTURE_HEIGHT = 720

def check_and_download_model():
    """Checks if the MediaPipe model exists locally. If not, attempts to download it."""
    if not os.path.exists(MODEL_FILENAME):
        print(f"[MODEL] MediaPipe Object Detection model '{MODEL_FILENAME}' not found locally.")
        print(f"[MODEL] Attempting to download from Google APIs...")
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
            print("And save it in the same directory as this script.")
            sys.exit(1)
    else:
        print(f"[MODEL] Found local model '{MODEL_FILENAME}'. Ready to load.")

def run_modern_tasks_detector():
    """Runs the modern MediaPipe Tasks Object Detector API (v0.10.0+)"""
    import mediapipe as mp
    from mediapipe.tasks import python
    from mediapipe.tasks.vision import ObjectDetectorOptions, ObjectDetector
    from mediapipe.tasks.vision import RunningMode as VisionRunningMode

    print("[AI Mode] Initializing Modern Tasks API (EfficientDet-Lite2)...")
    base_options = python.BaseOptions(model_asset_path=MODEL_FILENAME)
    options = ObjectDetectorOptions(
        base_options=base_options,
        score_threshold=CONFIDENCE_THRESHOLD,
        running_mode=VisionRunningMode.IMAGE,
        max_results=MAX_RESULTS
    )
    detector = ObjectDetector.create_from_options(options)
    print("[AI Mode] Neural Network successfully loaded!")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Could not open USB camera.")
        detector.close()
        sys.exit(1)

    time.sleep(1.0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAPTURE_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAPTURE_HEIGHT)

    window_name = "Argus Vac - Google MediaPipe Object Detection (Modern)"
    if SHOW_GUI:
        cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
        print("\n[INFO] Starting live video stream! Press 'q' to exit.\n")
    else:
        print("\n[INFO] Headless Mode Active. Logging to console. Press Ctrl+C to stop.\n")

    last_log_time = 0

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                time.sleep(0.1)
                continue

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
            detection_result = detector.detect(mp_image)

            if detection_result.detections:
                for detection in detection_result.detections:
                    bbox = detection.bounding_box
                    category = detection.categories[0]
                    category_name = category.category_name
                    score = category.score

                    cx = int(bbox.origin_x + bbox.width / 2)
                    cy = int(bbox.origin_y + bbox.height / 2)
                    radius = int(max(bbox.width, bbox.height) / 4)
                    radius = max(radius, 25)

                    cv2.circle(frame, (cx, cy), radius, (0, 255, 0), 3)
                    cv2.circle(frame, (cx, cy), 6, (0, 255, 0), -1)

                    label_text = f"{category_name.upper()} ({score * 100:.0f}%)"
                    text_size = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)[0]
                    text_w, text_h = text_size[0], text_size[1]
                    cv2.rectangle(frame, (cx - text_w // 2 - 5, cy - radius - 25), (cx + text_w // 2 + 5, cy - radius), (0, 0, 0), -1)
                    cv2.putText(frame, label_text, (cx - text_w // 2, cy - radius - 8),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                    current_time = time.time()
                    if current_time - last_log_time > 1.0:
                        print(f"[AI ALERT] {category_name} | Confidence: {score*100:.1f}% | Coordinates: ({cx}, {cy})")
                        last_log_time = current_time

            if SHOW_GUI:
                cv2.imshow(window_name, frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                time.sleep(0.03)

    except KeyboardInterrupt:
        print("\n[INFO] Shutting down gracefully.")
    finally:
        cap.release()
        detector.close()
        if SHOW_GUI:
            cv2.destroyAllWindows()


def run_legacy_solutions_detector():
    """Runs the classic MediaPipe Solutions Object Detector API (< v0.10.0)"""
    import mediapipe as mp
    
    print("[AI Mode] Initializing Classic Solutions API (Fall-back)...")
    mp_object_detection = mp.solutions.object_detection
    mp_drawing = mp.solutions.drawing_utils

    # model_selection=0 is optimized for short-range objects (within 2 meters)
    detector = mp_object_detection.ObjectDetection(
        model_selection=0, 
        min_detection_confidence=CONFIDENCE_THRESHOLD
    )
    print("[AI Mode] Classic Solution model loaded successfully!")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Could not open USB camera.")
        sys.exit(1)

    time.sleep(1.0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Use 640x480 for classic model speed
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    window_name = "Argus Vac - Google MediaPipe Object Detection (Legacy)"
    if SHOW_GUI:
        cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
        print("\n[INFO] Starting live video stream! Press 'q' to exit.\n")
    else:
        print("\n[INFO] Headless Mode Active. Logging to console. Press Ctrl+C to stop.\n")

    last_log_time = 0

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                time.sleep(0.1)
                continue

            height, width, _ = frame.shape
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = detector.process(rgb_frame)

            if results.detections:
                for detection in results.detections:
                    # Legacy structure uses relative coordinate offsets (0.0 to 1.0)
                    bbox = detection.location_data.relative_bounding_box
                    category_name = "object"
                    score = detection.score[0] if detection.score else CONFIDENCE_THRESHOLD
                    
                    if detection.label_id:
                        # Map index to common categories if label string not populated
                        category_name = f"Class {detection.label_id[0]}"

                    # Convert relative float coordinates back to absolute pixel positions
                    xmin = int(bbox.xmin * width)
                    ymin = int(bbox.ymin * height)
                    w = int(bbox.width * width)
                    h = int(bbox.height * height)
                    
                    cx = int(xmin + w / 2)
                    cy = int(ymin + h / 2)
                    radius = int(max(w, h) / 4)
                    radius = max(radius, 25)

                    # Draw green bounding markers
                    cv2.circle(frame, (cx, cy), radius, (0, 255, 0), 3)
                    cv2.circle(frame, (cx, cy), 6, (0, 255, 0), -1)

                    label_text = f"{category_name.upper()} ({score * 100:.0f}%)"
                    text_size = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)[0]
                    text_w, text_h = text_size[0], text_size[1]
                    cv2.rectangle(frame, (xmin, ymin - 25), (xmin + text_w + 10, ymin), (0, 0, 0), -1)
                    cv2.putText(frame, label_text, (xmin + 5, ymin - 8),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                    current_time = time.time()
                    if current_time - last_log_time > 1.0:
                        print(f"[AI ALERT] {category_name} | Confidence: {score*100:.1f}% | Coordinates: ({cx}, {cy})")
                        last_log_time = current_time

            if SHOW_GUI:
                cv2.imshow(window_name, frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                time.sleep(0.03)

    except KeyboardInterrupt:
        print("\n[INFO] Shutting down gracefully.")
    finally:
        cap.release()
        detector.close()
        if SHOW_GUI:
            cv2.destroyAllWindows()


def main():
    print("=====================================================")
    print("   ARGUS VAC - HYBRID OBJECT DETECTOR (v6 - Hybrid)  ")
    print("=====================================================")

    # Attempt to import modern Tasks vision API
    use_modern_api = False
    try:
        import mediapipe as mp
        from mediapipe.tasks import python
        from mediapipe.tasks.vision import ObjectDetector
        # If imports succeeded, we can run modern detector
        use_modern_api = True
    except ImportError:
        print("[AI] Modern MediaPipe Tasks API not found. Checking classic Solutions API fallback...")

    if use_modern_api:
        # Download lite2 model if using modern tasks
        check_and_download_model()
        run_modern_tasks_detector()
    else:
        # Fall back to legacy solutions API
        try:
            import mediapipe as mp
            import mediapipe.solutions.object_detection
        except ImportError as e:
            print("\n" + "="*70)
            print("  [FATAL ERROR] BOTH MEDIAPIPE APIs FAILED TO LOAD")
            print("="*70)
            print(f"Details: {e}")
            print("\nYour MediaPipe installation is completely missing or broken.")
            print("\nPlease execute these commands on the Orange Pi 5 to repair:")
            print("  1. pip3 install \"numpy<2\" --break-system-packages")
            print("  2. pip3 install --force-reinstall mediapipe --break-system-packages")
            print("="*70 + "\n")
            sys.exit(1)
            
        run_legacy_solutions_detector()


if __name__ == "__main__":
    main()
