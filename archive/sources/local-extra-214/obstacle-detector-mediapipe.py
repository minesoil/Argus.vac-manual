#!/usr/bin/env python3
"""
Argus Vac - AI Object Detection Sandbox with Google MediaPipe (v1)
Developed by Gemini Notebook for Orange Pi 5

This script uses Google's MediaPipe Object Detector (Deep Learning/AI model)
to automatically recognize real-world objects (such as cups, shoes, books, backpacks,
or bottles) on your floor. It opens up the camera GUI, processes frames through the
neural network, and draws a green circle around the center of any detected objects.

NO MANUAL CALIBRATION OF SLIDERS OR HSV VALUES REQUIRED!

Prerequisites:
  pip3 install mediapipe opencv-python numpy
"""

import cv2
import numpy as np
import sys
import time
import os
import urllib.request

# --- CONFIGURATION ---
SHOW_GUI = True         # True: Opens the camera desktop GUI. False: Console-only logging.
CONFIDENCE_THRESHOLD = 0.40  # Detect objects with at least 40% confidence
MODEL_FILENAME = "efficientdet_lite0.tflite"
MODEL_URL = "https://storage.googleapis.com/mediapipe-models/object_detector/efficientdet_lite0/float16/1/efficientdet_lite0.tflite"

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
    print("      ARGUS VAC - MEDIAPIPE OBJECT DETECTOR (v1)     ")
    print("=====================================================")
    
    # 1. Download model if needed
    check_and_download_model()

    # 2. Check and import MediaPipe
    try:
        import mediapipe as mp
        from mediapipe.tasks import python
        from mediapipe.tasks.vision import ObjectDetectorOptions, ObjectDetector
        from mediapipe.tasks.vision import RunningMode as VisionRunningMode
    except ImportError:
        print("\n[ERROR] Google MediaPipe is not installed!")
        print("Please install the required libraries on your Orange Pi 5 using:")
        print("  pip3 install mediapipe opencv-python numpy\n")
        sys.exit(1)

    # 3. Initialize MediaPipe Object Detector
    print("[AI] Initializing Neural Network...")
    try:
        base_options = python.BaseOptions(model_asset_path=MODEL_FILENAME)
        options = ObjectDetectorOptions(
            base_options=base_options,
            score_threshold=CONFIDENCE_THRESHOLD,
            running_mode=VisionRunningMode.IMAGE, # Processes frame-by-frame
            max_results=5                         # Maximum objects to track at once
        )
        detector = ObjectDetector.create_from_options(options)
        print("[AI] Neural Network successfully loaded!")
    except Exception as e:
        print(f"[ERROR] Failed to initialize MediaPipe Object Detector: {e}")
        sys.exit(1)

    # 4. Initialize Video Capture
    print("[CAMERA] Opening USB camera feed (index 0)...")
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Could not open USB camera.")
        print("Please verify it is plugged in and check '/dev/video*'.")
        detector.close()
        sys.exit(1)

    # Warm-up camera
    time.sleep(1.0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

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

            # Flip frame horizontally for natural mirror view if desired (optional)
            # frame = cv2.flip(frame, 1)

            # Convert BGR frame to RGB (MediaPipe requires RGB color space)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Load numpy array into MediaPipe Image object
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
            
            # Perform Object Detection
            detection_result = detector.detect(mp_image)
            
            obstacle_detected = False
            
            # Draw detections
            if detection_result.detections:
                for detection in detection_result.detections:
                    bbox = detection.bounding_box
                    category = detection.categories[0]
                    category_name = category.category_name
                    score = category.score
                    
                    obstacle_detected = True
                    
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
