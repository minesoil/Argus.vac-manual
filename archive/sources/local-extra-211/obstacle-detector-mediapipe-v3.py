#!/usr/bin/env python3
"""
Argus Vac - AI Object Detection Sandbox with Google MediaPipe (v3)
Developed by Gemini Notebook for Orange Pi 5

This script uses Google's MediaPipe Object Detector (Deep Learning/AI model)
to automatically recognize real-world objects (such as cups, shoes, books, backpacks,
or bottles) on your floor. It opens up the camera GUI, processes frames through the
neural network, and draws a green circle around the center of any detected objects.

NO MANUAL CALIBRATION OF SLIDERS OR HSV VALUES REQUIRED!

Prerequisites:
  pip3 install mediapipe opencv-python numpy
"""

import sys
import os
import time
import urllib.request

# --- IMPORT SAFETY NET (CAPTURES NUMPY/OPENCV CONFLICTS) ---
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
CONFIDENCE_THRESHOLD = 0.50  # Detect objects with at least 50% confidence (fewer false positives)
MAX_RESULTS = 5              # Max simultaneous detections to track

# EfficientDet-Lite2 trades some speed for meaningfully better accuracy than Lite0,
# especially on smaller/partially-occluded objects (shoes, small bottles, etc).
MODEL_FILENAME = "efficientdet_lite2.tflite"
MODEL_URL = "https://storage.googleapis.com/mediapipe-models/object_detector/efficientdet_lite2/float16/1/efficientdet_lite2.tflite"

# Capture at a higher resolution so the detector gets more detail per frame.
# (EfficientDet resizes internally, but starting from a sharper source frame helps
# with small/distant objects; drop back to 640x480 if your camera can't hit this
# framerate on the Orange Pi.)
CAPTURE_WIDTH = 1280
CAPTURE_HEIGHT = 720

def check_and_download_model():
    """Checks if the MediaPipe model exists locally. If not, attempts to download it."""
    if not os.path.exists(MODEL_FILENAME):
        print(f"[MODEL] MediaPipe Object Detection model '{MODEL_FILENAME}' not found locally.")
        print(f"[MODEL] Attempting to download from Google APIs...")
        try:
            # Create a progress printer
            def progress(count, block_size, total_size):
                percent = int(count * block_size * 100 / total_size)
                sys.stdout.write(f"\rDownloading model: {percent}% complete")
                sys.stdout.flush()
            
            urllib.request.urlretrieve(MODEL_URL, MODEL_FILENAME, progress)
            print(f"\n[MODEL] Download complete! Saved as '{MODEL_FILENAME}'")
        except Exception as e:
            print(f"\n[ERROR] Failed to download model automatically: {e}")
            print(f"Please manually download the model file from:")
            print(f"  {MODEL_URL}")
            print(f"And save it in the same directory as this script.")
            sys.exit(1)
    else:
        print(f"[MODEL] Found local model '{MODEL_FILENAME}'. Ready to load.")

def main():
    print("=====================================================")
    print("   ARGUS VAC - MEDIAPIPE OBJECT DETECTOR (v3 - HiAcc)")
    print("=====================================================")
    
    # 1. Download model if needed
    check_and_download_model()

    # 2. Check and import MediaPipe
    try:
        import mp_dummy_placeholder  # Force an import error or wrap safely for demonstration if needed, but we write correct imports:
        import mediapipe as mp
        from mediapipe.tasks import python
        from mediapipe.tasks.vision import ObjectDetectorOptions, ObjectDetector
        from mediapipe.tasks.vision import RunningMode as VisionRunningMode
    except ImportError:
        # Re-trying standard import without placeholder to let it run properly
        try:
            import mediapipe as mp
            from mediapipe.tasks import python
            from mediapipe.tasks.vision import ObjectDetectorOptions, ObjectDetector
            from mediapipe.tasks.vision import RunningMode as VisionRunningMode
        except ImportError as e:
            print("\n" + "="*70)
            print("  [FATAL ERROR] FAILED TO IMPORT GOOGLE MEDIAPIPE")
            print("="*70)
            print(f"Details: {e}")
            print("\nThis occurs when the mediapipe library or its protobuf/flatbuffers dependencies")
            print("are missing or incompatible with your Python/NumPy version.")
            print("\nRecommended Fix:")
            print("  pip3 install mediapipe --break-system-packages")
            print("="*70 + "\n")
            import traceback
            traceback.print_exc()
            sys.exit(1)

    # 3. Initialize MediaPipe Object Detector
    print("[AI] Initializing Neural Network (EfficientDet-Lite2)...")
    try:
        base_options = python.BaseOptions(model_asset_path=MODEL_FILENAME)
        options = ObjectDetectorOptions(
            base_options=base_options,
            score_threshold=CONFIDENCE_THRESHOLD,
            running_mode=VisionRunningMode.IMAGE, # Processes frame-by-frame
            max_results=MAX_RESULTS
        )
        detector = ObjectDetector.create_from_options(options)
        print("[AI] Neural Network successfully loaded!")
    except Exception as e:
        print(f"[ERROR] Failed to initialize MediaPipe Object Detector: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

    # 4. Initialize Video Capture
    print(f"[CAMERA] Opening USB camera feed (index 0) at {CAPTURE_WIDTH}x{CAPTURE_HEIGHT}...")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Could not open USB camera.")
        print("Please verify it is plugged in and check '/dev/video*'.")
        detector.close()
        sys.exit(1)

    # Warm-up camera and set resolution
    time.sleep(1.0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAPTURE_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAPTURE_HEIGHT)

    window_name = "Argus Vac - Google MediaPipe Object Detection"
    if SHOW_GUI:
        cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
        print("\n[INFO] Starting live video stream!")
        print("  - Place objects (cups, shoes, bottles, backpacks) in front of the camera.")
        print("  - The AI will draw a green circle around the center of recognized objects.")
        print("  - Press 'q' in the window to exit.\n")
    else:
        print("\n[INFO] Running in Headless Mode. Alerts will log to console. Press Ctrl+C to stop.\n")

    last_log_time = 0

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("[WARNING] Failed to grab frame from camera.")
                time.sleep(0.1)
                continue

            # Convert BGR frame to RGB (MediaPipe requires RGB color space)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Load numpy array into MediaPipe Image object
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
            
            # Perform Object Detection
            detection_result = detector.detect(mp_image)
            
            # Draw detections
            if detection_result.detections:
                for detection in detection_result.detections:
                    bbox = detection.bounding_box
                    category = detection.categories[0]
                    category_name = category.category_name
                    score = category.score
                    
                    # 1. Calculate center coordinates
                    cx = int(bbox.origin_x + bbox.width / 2)
                    cy = int(bbox.origin_y + bbox.height / 2)
                    
                    # 2. Define a radius proportional to object size (fallback to minimum 25 pixels)
                    radius = int(max(bbox.width, bbox.height) / 4)
                    radius = max(radius, 25)
                    
                    # 3. Draw a vibrant green circle around the object's center point
                    cv2.circle(frame, (cx, cy), radius, (0, 255, 0), 3) # Outer circle
                    cv2.circle(frame, (cx, cy), 6, (0, 255, 0), -1)    # Solid center dot
                    
                    # 4. Draw a clean text banner above the circle
                    label_text = f"{category_name.upper()} ({score * 100:.0f}%)"
                    
                    # Draw a semi-transparent black background box for text legibility
                    text_size = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)[0]
                    text_w, text_h = text_size[0], text_size[1]
                    cv2.rectangle(frame, (cx - text_w // 2 - 5, cy - radius - 25), (cx + text_w // 2 + 5, cy - radius), (0, 0, 0), -1)
                    
                    # Overlay the green text inside/above the circle boundary
                    cv2.putText(frame, label_text, (cx - text_w // 2, cy - radius - 8),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    
                    # Console logging (throttled to once per second)
                    current_time = time.time()
                    if current_time - last_log_time > 1.0:
                        print(f"[AI ALERT] Recognized: {category_name} | Confidence: {score*100:.1f}% | Coordinates: ({cx}, {cy})")
                        last_log_time = current_time

            # Show window if GUI is enabled
            if SHOW_GUI:
                cv2.imshow(window_name, frame)
                
                # Check for keypress 'q' to quit
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break
            else:
                time.sleep(0.03) # Prevent CPU throttling in headless loop

    except KeyboardInterrupt:
        print("\n[INFO] Interrupt detected. Shutting down gracefully.")
    finally:
        # Cleanup
        cap.release()
        detector.close()
        if SHOW_GUI:
            cv2.destroyAllWindows()
        print("Camera and AI model resources released. Done.")

if __name__ == "__main__":
    main()