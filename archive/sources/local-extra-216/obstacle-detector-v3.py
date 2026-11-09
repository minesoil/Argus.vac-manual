#!/usr/bin/env python3
"""
Argus Vac - Camera Obstacle Detection Sandbox (v3)
Developed by Gemini Notebook for Orange Pi 5

This script implements an advanced, highly precise computer vision sandbox using OpenCV.
To solve the "auto-trigger" issue where shadows, walls, and floors cause false positives, 
this version introduces dual detection modes:

1. EDGE MODE (Highly Recommended for general obstacles):
   Uses Canny Edge Detection to locate physical boundaries. A flat floor or wall has 
   zero edges, so it is completely ignored. Objects (like socks, cables, or slippers) 
   have sharp contrast edges and trigger the warning instantly.

2. HSV COLOR MODE (Highly Precise for targeting specific objects):
   Calibrates the camera to look ONLY for a specific color signature (e.g. a bright red sock,
   blue toy, etc.) by narrowing Hue, Saturation, and Value ranges to block out shadows.
"""

import cv2
import numpy as np
import sys
import time

# ==================== CONFIGURATION ====================
SHOW_GUI = False      # Set to True if using X11 Forwarding; False for console-only
DETECTION_MODE = "EDGE"  # Choose "EDGE" (Canny Edge) or "HSV" (Color Isolation)
# =======================================================

def nothing(x):
    pass

def main():
    print("=====================================================")
    print("      ARGUS VAC - OBSTACLE DETECTION SANDBOX (v3)    ")
    print("=====================================================")
    print(f"Mode: {DETECTION_MODE} | Display: {'GUI' if SHOW_GUI else 'HEADLESS'}")
    print("Starting USB camera capture...")

    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("[ERROR] Could not open USB camera (index 0).")
        print("Please verify your camera is plugged into the Orange Pi 5 and run 'ls /dev/video*'.")
        sys.exit(1)

    time.sleep(1.0) # Warm up
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    window_name = "Argus Vac - Obstacle Calibration"
    
    # Precise starting parameters
    # ROI: driving corridor boundaries (percentages of screen)
    roi_top_pct = 0.5   # Ignore the top 50% of the screen (horizon/walls)
    roi_left_pct = 0.25  # Focus on the middle path
    roi_right_pct = 0.75
    min_area = 1500      # Obstacles must be at least 1500 pixels to trigger

    # HSV Parameters (Targeted for a colorful test object to avoid shadow triggers)
    # By default, we target high saturation/brightness colors (like bright red, orange, or green)
    low_h, high_h = 0, 20      # Red/Orange Hue
    low_s, high_s = 100, 255   # Bright/Vivid colors only (ignores grey/white floor and dark shadows)
    low_v, high_v = 100, 255   # Lit objects only (ignores dark rooms and shadows)

    # Edge Parameters
    canny_low = 50
    canny_high = 150

    if SHOW_GUI:
        cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
        cv2.createTrackbar("ROI Top %", window_name, int(roi_top_pct * 100), 100, nothing)
        cv2.createTrackbar("ROI Left %", window_name, int(roi_left_pct * 100), 100, nothing)
        cv2.createTrackbar("ROI Right %", window_name, int(roi_right_pct * 100), 100, nothing)
        cv2.createTrackbar("Min Area px", window_name, min_area, 20000, nothing)

        if DETECTION_MODE == "HSV":
            cv2.createTrackbar("Low H", window_name, low_h, 179, nothing)
            cv2.createTrackbar("High H", window_name, high_h, 179, nothing)
            cv2.createTrackbar("Low S", window_name, low_s, 255, nothing)
            cv2.createTrackbar("High S", window_name, high_s, 255, nothing)
            cv2.createTrackbar("Low V", window_name, low_v, 255, nothing)
            cv2.createTrackbar("High V", window_name, high_v, 255, nothing)
        else: # EDGE Mode
            cv2.createTrackbar("Canny Low", window_name, canny_low, 255, nothing)
            cv2.createTrackbar("Canny High", window_name, canny_high, 255, nothing)

        print("\n[INFO] Calibration UI initialized.")
        print("  - Drag sliders to fine-tune boundaries.")
        print("  - Press 'q' in any video window to exit.\n")
    else:
        print("\n[INFO] Running in headless mode.")
        print("  - Output alerts will print directly below.")
        print("  - Press Ctrl+C in your terminal to exit.\n")

    last_warning_time = 0

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("[WARNING] Failed to grab frame from USB camera.")
                time.sleep(0.1)
                continue

            height, width, _ = frame.shape
            
            # 1. Read parameters (sliders or defaults)
            if SHOW_GUI:
                roi_top_pct = cv2.getTrackbarPos("ROI Top %", window_name) / 100.0
                roi_left_pct = cv2.getTrackbarPos("ROI Left %", window_name) / 100.0
                roi_right_pct = cv2.getTrackbarPos("ROI Right %", window_name) / 100.0
                min_area = cv2.getTrackbarPos("Min Area px", window_name)
                
                if DETECTION_MODE == "HSV":
                    low_h = cv2.getTrackbarPos("Low H", window_name)
                    high_h = cv2.getTrackbarPos("High H", window_name)
                    low_s = cv2.getTrackbarPos("Low S", window_name)
                    high_s = cv2.getTrackbarPos("High S", window_name)
                    low_v = cv2.getTrackbarPos("Low V", window_name)
                    high_v = cv2.getTrackbarPos("High V", window_name)
                else:
                    canny_low = cv2.getTrackbarPos("Canny Low", window_name)
                    canny_high = cv2.getTrackbarPos("Canny High", window_name)

            # 2. Define and Crop Region of Interest (ROI) - Driving Corridor
            roi_y_start = int(height * roi_top_pct)
            roi_y_end = height
            roi_x_start = int(width * roi_left_pct)
            roi_x_end = int(width * roi_right_pct)
            
            roi = frame[roi_y_start:roi_y_end, roi_x_start:roi_x_end]
            blurred = cv2.GaussianBlur(roi, (5, 5), 0)
            
            # 3. Process according to Selected Mode
            if DETECTION_MODE == "HSV":
                hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
                lower_bound = np.array([low_h, low_s, low_v])
                upper_bound = np.array([high_h, high_s, high_v])
                mask = cv2.inRange(hsv, lower_bound, upper_bound)
                
                kernel = np.ones((5, 5), np.uint8)
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            
            else: # EDGE Detection Mode
                # Convert to grayscale first
                gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
                # Compute Canny Edges
                mask = cv2.Canny(gray, canny_low, canny_high)
                # Dilate edges slightly to close gaps and make them solid shapes
                kernel = np.ones((3, 3), np.uint8)
                mask = cv2.dilate(mask, kernel, iterations=1)

            # 4. Find Contours
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            obstacle_detected_in_corridor = False
            
            if SHOW_GUI:
                # Draw corridor on the main image
                cv2.rectangle(frame, (roi_x_start, roi_y_start), (roi_x_end, roi_y_end), (255, 255, 0), 2)
                cv2.putText(frame, f"Driving Corridor ({DETECTION_MODE})", (roi_x_start + 5, roi_y_start - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)

            for cnt in contours:
                area = cv2.contourArea(cnt)
                
                if area > min_area:
                    obstacle_detected_in_corridor = True
                    
                    if SHOW_GUI:
                        x, y, w, h_box = cv2.boundingRect(cnt)
                        global_x = roi_x_start + x
                        global_y = roi_y_start + y
                        
                        cx = global_x + (w // 2)
                        cy = global_y + (h_box // 2)
                        
                        proximity_ratio = (global_y + h_box - roi_y_start) / (height - roi_y_start)
                        severity = "CRITICAL" if proximity_ratio > 0.7 else "WARNING"
                        color = (0, 0, 255) if severity == "CRITICAL" else (0, 165, 255)
                        
                        cv2.rectangle(frame, (global_x, global_y), (global_x + w, global_y + h_box), color, 3)
                        cv2.circle(frame, (cx, cy), 5, (0, 255, 255), -1)
                        
                        label = f"{severity}: Obj ({int(area)}px)"
                        cv2.putText(frame, label, (global_x, global_y - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            
            # 5. Output warnings to terminal (throttled to 500ms)
            if obstacle_detected_in_corridor:
                current_time = time.time()
                if current_time - last_warning_time > 0.5:
                    print(f"[ALERT] {time.strftime('%H:%M:%S')} - Obstacle detected! (Mode: {DETECTION_MODE})")
                    last_warning_time = current_time
            
            if SHOW_GUI:
                cv2.imshow(window_name, frame)
                cv2.imshow("Detection Mask (Processed)", mask)
                
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    print("\n[INFO] Shutting down camera sandbox.")
                    break
            else:
                time.sleep(0.03) # Prevent CPU pinning
                
    except KeyboardInterrupt:
        print("\n[INFO] Interrupt detected. Shutting down.")
        
    finally:
        cap.release()
        if SHOW_GUI:
            cv2.destroyAllWindows()
        print("Camera hardware released. Done.")

if __name__ == '__main__':
    main()
