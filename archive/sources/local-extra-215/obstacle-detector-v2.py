#!/usr/bin/env python3
"""
Argus Vac - Camera Obstacle Detection Sandbox (v2)
Developed by Gemini Notebook for Orange Pi 5

This script implements a high-performance computer vision sandbox using OpenCV.
It captures video from a USB camera, isolates a driving corridor (Region of Interest),
detects obstacles (like socks, cables, or toys) using HSV thresholding or contour detection,
and issues movement warnings.

It supports both:
1. Headless Mode (SHOW_GUI = False): Outputs alerts purely to the console, perfect for quick testing.
2. GUI Mode (SHOW_GUI = True): Displays live video feed, masks, and adjustment sliders (requires X11 forwarding).
"""

import cv2
import numpy as np
import sys
import time

# --- CONFIGURATION TOGGLE ---
SHOW_GUI = False  # Set to False to run purely in the console without X11 forwarding display errors!
# ----------------------------

def nothing(x):
    pass

def main():
    print("=====================================================")
    print("      ARGUS VAC - OBSTACLE DETECTION SANDBOX (v2)    ")
    print("=====================================================")
    print(f"Starting USB camera capture in {'GUI' if SHOW_GUI else 'HEADLESS'} mode...")

    # Initialize video capture (0 is default USB webcam on Orange Pi / Linux)
    cap = cv2.VideoCapture(0)
    
    # Check if camera opened successfully
    if not cap.isOpened():
        print("[ERROR] Could not open USB camera (index 0).")
        print("Please verify your camera is plugged into the Orange Pi 5 and run 'ls /dev/video*'.")
        sys.exit(1)

    # Allow camera to warm up
    time.sleep(1.0)
    
    # Configure video dimensions
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    window_name = "Argus Vac - Obstacle Detector Calibration"
    
    # Default parameters for detection (used in Headless mode or as starting slider points)
    # Optimized to detect dark/colored obstacles (like socks/cables) on light-colored floors.
    low_h, high_h = 0, 179
    low_s, high_s = 0, 255
    low_v, high_v = 0, 150
    roi_top_pct = 0.4   # Focus on the bottom 60% of the frame
    roi_left_pct = 0.2  # Clip the leftmost 20%
    roi_right_pct = 0.8 # Clip the rightmost 20%
    min_area = 800      # Minimum size in pixels to count as an obstacle

    if SHOW_GUI:
        # Create an OpenCV GUI window for tuning parameters
        cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
        
        # Create Trackbars for on-the-fly HSV threshold tuning
        cv2.createTrackbar("Low H", window_name, low_h, 179, nothing)
        cv2.createTrackbar("High H", window_name, high_h, 179, nothing)
        cv2.createTrackbar("Low S", window_name, low_s, 255, nothing)
        cv2.createTrackbar("High S", window_name, high_s, 255, nothing)
        cv2.createTrackbar("Low V", window_name, low_v, 255, nothing)
        cv2.createTrackbar("High V", window_name, high_v, 255, nothing)
        
        # Trackbars for Region of Interest (ROI) driving corridor boundaries
        cv2.createTrackbar("ROI Top %", window_name, int(roi_top_pct * 100), 100, nothing)
        cv2.createTrackbar("ROI Left %", window_name, int(roi_left_pct * 100), 100, nothing)
        cv2.createTrackbar("ROI Right %", window_name, int(roi_right_pct * 100), 100, nothing)
        
        # Minimum contour area to trigger a warning
        cv2.createTrackbar("Min Area px", window_name, min_area, 20000, nothing)

        print("\n[INFO] Calibration UI initialized.")
        print("  - Drag sliders to isolate the obstacle's color signature in the 'Mask' window.")
        print("  - Press 'q' in any video window to exit.")
        print("  - Check your terminal for real-time status and obstacle warnings.\n")
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
            
            # 1. Read parameters (either from sliders or preconfigured defaults)
            if SHOW_GUI:
                low_h = cv2.getTrackbarPos("Low H", window_name)
                high_h = cv2.getTrackbarPos("High H", window_name)
                low_s = cv2.getTrackbarPos("Low S", window_name)
                high_s = cv2.getTrackbarPos("High S", window_name)
                low_v = cv2.getTrackbarPos("Low V", window_name)
                high_v = cv2.getTrackbarPos("High V", window_name)
                
                roi_top_pct = cv2.getTrackbarPos("ROI Top %", window_name) / 100.0
                roi_left_pct = cv2.getTrackbarPos("ROI Left %", window_name) / 100.0
                roi_right_pct = cv2.getTrackbarPos("ROI Right %", window_name) / 100.0
                min_area = cv2.getTrackbarPos("Min Area px", window_name)

            # 2. Define and draw the Region of Interest (ROI) - the "Driving Corridor"
            roi_y_start = int(height * roi_top_pct)
            roi_y_end = height
            roi_x_start = int(width * roi_left_pct)
            roi_x_end = int(width * roi_right_pct)
            
            # Crop to the ROI
            roi = frame[roi_y_start:roi_y_end, roi_x_start:roi_x_end]
            
            # 3. Process the ROI for detection
            blurred = cv2.GaussianBlur(roi, (5, 5), 0)
            hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
            
            # Create a binary mask using the bounds
            lower_bound = np.array([low_h, low_s, low_v])
            upper_bound = np.array([high_h, high_s, high_v])
            mask = cv2.inRange(hsv, lower_bound, upper_bound)
            
            # Clean up isolated noise pixels
            kernel = np.ones((5, 5), np.uint8)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
            mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
            
            # 4. Find Contours in the binary mask
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            obstacle_detected_in_corridor = False
            
            # Draw static corridor borders on display frame if GUI is active
            if SHOW_GUI:
                cv2.rectangle(frame, (roi_x_start, roi_y_start), (roi_x_end, roi_y_end), (255, 255, 0), 2)
                cv2.putText(frame, "Driving Corridor (ROI)", (roi_x_start + 5, roi_y_start - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)

            for cnt in contours:
                area = cv2.contourArea(cnt)
                
                # Check if the detected object is large enough
                if area > min_area:
                    obstacle_detected_in_corridor = True
                    
                    if SHOW_GUI:
                        # Compute bounding box coordinates relative to the original frame
                        x, y, w, h_box = cv2.boundingRect(cnt)
                        global_x = roi_x_start + x
                        global_y = roi_y_start + y
                        
                        cx = global_x + (w // 2)
                        cy = global_y + (h_box // 2)
                        
                        # Estimate proximity hazard severity (closer objects are lower in the frame)
                        proximity_ratio = (global_y + h_box - roi_y_start) / (height - roi_y_start)
                        severity = "CRITICAL" if proximity_ratio > 0.7 else "WARNING"
                        color = (0, 0, 255) if severity == "CRITICAL" else (0, 165, 255) # Red vs Orange
                        
                        # Draw visual feedback
                        cv2.rectangle(frame, (global_x, global_y), (global_x + w, global_y + h_box), color, 3)
                        cv2.circle(frame, (cx, cy), 5, (0, 255, 255), -1)
                        
                        label = f"{severity}: Obj (Area:{int(area)})"
                        cv2.putText(frame, label, (global_x, global_y - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            
            # 5. Output warning logs to terminal at a throttled rate (every 500ms)
            if obstacle_detected_in_corridor:
                current_time = time.time()
                if current_time - last_warning_time > 0.5:
                    print(f"[ALERT] {time.strftime('%H:%M:%S')} - Obstacle detected in driving corridor! Sending HALT signal.")
                    last_warning_time = current_time
            
            # Show visual frames if GUI mode is active
            if SHOW_GUI:
                cv2.imshow(window_name, frame)
                cv2.imshow("Detection Mask (Thresholded)", mask)
                
                # Monitor keypresses. Exit if 'q' is pressed.
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    print("\n[INFO] Gracefully shutting down camera sandbox.")
                    break
            else:
                # Slight sleep in headless mode to prevent CPU pinning
                time.sleep(0.03)
                
    except KeyboardInterrupt:
        print("\n[INFO] Interrupt detected. Shutting down.")
        
    finally:
        cap.release()
        if SHOW_GUI:
            cv2.destroyAllWindows()
        print("Camera hardware released. Done.")

if __name__ == '__main__':
    main()
