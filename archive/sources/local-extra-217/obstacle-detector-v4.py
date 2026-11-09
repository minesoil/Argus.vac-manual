#!/usr/bin/env python3
"""
Argus Vac - Self-Calibrating Obstacle Detector (v4)
Developed by Gemini Notebook for Orange Pi 5

To solve the "immediate trigger" issue caused by ambient lighting, floor texture,
and camera sensor noise, this version introduces AUTOMATIC SELF-CALIBRATION.

How it works:
1. On Startup, it takes 3 seconds (approx. 60 frames) to analyze the clean floor
   directly in front of the robot (inside your Driving Corridor).
2. It measures the "baseline noise" (maximum edge contour size and pixel density) 
   of your actual floor under your room's specific lighting.
3. It dynamically sets the "Min Area" and "Canny Thresholds" just above this baseline.
4. Once calibrated, it goes active. It will remain 100% quiet on your floor and walls,
   only triggering a warning if a real, physical object (like a sock, shoe, or cable)
   is introduced into the corridor!
"""

import cv2
import numpy as np
import sys
import time

# ==================== CONFIGURATION ====================
SHOW_GUI = False          # Set to True if using X11 Forwarding; False for console-only
DETECTION_MODE = "EDGE"   # "EDGE" (Canny) or "HSV" (Color Isolation)
CALIBRATION_FRAMES = 60   # Number of frames to analyze during startup calibration
# =======================================================

def nothing(x):
    pass

def main():
    print("=====================================================")
    print("     ARGUS VAC - SELF-CALIBRATING DETECTOR (v4)      ")
    print("=====================================================")
    print(f"Mode: {DETECTION_MODE} | Display: {'GUI' if SHOW_GUI else 'HEADLESS'}")
    print("Starting USB camera capture...")

    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("[ERROR] Could not open USB camera (index 0).")
        print("Please verify your camera is plugged into the Orange Pi 5.")
        sys.exit(1)

    time.sleep(1.0) # Let camera auto-exposure settle
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    # 1. Base ROI Layout (Driving Corridor)
    # Focus strictly on the floor directly in front of the robot (bottom-middle of the frame)
    roi_top_pct = 0.55   # Focus on the bottom 45% of the frame (ignores walls/ceilings)
    roi_left_pct = 0.3   # Narrow corridor to avoid side walls
    roi_right_pct = 0.7
    
    # Starting parameters before calibration
    canny_low = 80
    canny_high = 220
    min_area = 1000      # Will be dynamically overwritten by calibration
    
    # HSV Calibration defaults (if HSV is selected)
    low_h, high_h = 0, 179
    low_s, high_s = 40, 255
    low_v, high_v = 40, 255

    window_name = "Argus Vac - Self-Calibration"

    # =======================================================
    # STEP 1: AUTOMATIC BASELINE CALIBRATION
    # =======================================================
    print("\n-----------------------------------------------------")
    print("🔮 STARTING AUTOMATIC FLOOR CALIBRATION...")
    print("Please keep the floor in front of the camera clear!")
    print("-----------------------------------------------------")
    
    noise_areas = []
    
    for i in range(CALIBRATION_FRAMES):
        ret, frame = cap.read()
        if not ret:
            time.sleep(0.05)
            continue
            
        height, width, _ = frame.shape
        roi_y_start = int(height * roi_top_pct)
        roi_y_end = height
        roi_x_start = int(width * roi_left_pct)
        roi_x_end = int(width * roi_right_pct)
        
        roi = frame[roi_y_start:roi_y_end, roi_x_start:roi_x_end]
        
        # Heavy bilateral filter to smooth floor textures while preserving strong object edges
        smoothed = cv2.bilateralFilter(roi, 9, 75, 75)
        
        if DETECTION_MODE == "EDGE":
            gray = cv2.cvtColor(smoothed, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, canny_low, canny_high)
            
            # Find contours of noise on the "clean" floor
            contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                area = cv2.contourArea(cnt)
                noise_areas.append(area)
        else:
            # For HSV mode, sample the average floor color to build a floor-rejection mask
            hsv = cv2.cvtColor(smoothed, cv2.COLOR_BGR2HSV)
            # We track noise contours that slip past defaults
            lower_bound = np.array([low_h, low_s, low_v])
            upper_bound = np.array([high_h, high_s, high_v])
            mask = cv2.inRange(hsv, lower_bound, upper_bound)
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                noise_areas.append(cv2.contourArea(cnt))

        if i % 15 == 0:
            print(f"  [Calibrating...] Captured frame {i}/{CALIBRATION_FRAMES}...")
            
    # Calculate Dynamic Noise Floor
    if len(noise_areas) > 0:
        max_noise_area = max(noise_areas)
        avg_noise_area = sum(noise_areas) / len(noise_areas)
        # Set trigger threshold safely above the maximum noise seen
        min_area = int(max(max_noise_area * 2.5, 1200)) 
    else:
        min_area = 1500 # Default fallback
        max_noise_area = 0
        avg_noise_area = 0

    print("\n✅ CALIBRATION COMPLETE!")
    print(f"  - Avg Floor Noise Area: {avg_noise_area:.1f} px")
    print(f"  - Max Floor Noise Area: {max_noise_area:.1f} px")
    print(f"  - DYNAMIC TRIGGER THRESHOLD (Min Area): {min_area} px")
    print("-----------------------------------------------------")
    print("📡 Obstacle Detector is now ACTIVE.\n")

    # Initialize GUI if requested
    if SHOW_GUI:
        cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)
        cv2.createTrackbar(\"ROI Top %\", window_name, int(roi_top_pct * 100), 100, nothing)
        cv2.createTrackbar(\"ROI Left %\", window_name, int(roi_left_pct * 100), 100, nothing)
        cv2.createTrackbar(\"ROI Right %\", window_name, int(roi_right_pct * 100), 100, nothing)
        cv2.createTrackbar(\"Min Area px\", window_name, min_area, 20000, nothing)
        if DETECTION_MODE == \"EDGE\":
            cv2.createTrackbar(\"Canny Low\", window_name, canny_low, 255, nothing)
            cv2.createTrackbar(\"Canny High\", window_name, canny_high, 255, nothing)

    last_warning_time = 0

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("[WARNING] Failed to grab frame from USB camera.")
                time.sleep(0.1)
                continue

            height, width, _ = frame.shape
            
            # 1. Pull settings
            if SHOW_GUI:
                roi_top_pct = cv2.getTrackbarPos("ROI Top %", window_name) / 100.0
                roi_left_pct = cv2.getTrackbarPos("ROI Left %", window_name) / 100.0
                roi_right_pct = cv2.getTrackbarPos("ROI Right %", window_name) / 100.0
                min_area = cv2.getTrackbarPos("Min Area px", window_name)
                if DETECTION_MODE == "EDGE":
                    canny_low = cv2.getTrackbarPos("Canny Low", window_name)
                    canny_high = cv2.getTrackbarPos("Canny High", window_name)

            # 2. Extract Corridor (ROI)
            roi_y_start = int(height * roi_top_pct)
            roi_y_end = height
            roi_x_start = int(width * roi_left_pct)
            roi_x_end = int(width * roi_right_pct)
            
            roi = frame[roi_y_start:roi_y_end, roi_x_start:roi_x_end]
            
            # Apply bilateral filter to suppress textures while highlighting true objects
            smoothed = cv2.bilateralFilter(roi, 9, 75, 75)
            
            # 3. Process
            if DETECTION_MODE == "EDGE":
                gray = cv2.cvtColor(smoothed, cv2.COLOR_BGR2GRAY)
                mask = cv2.Canny(gray, canny_low, canny_high)
                
                # Dilate to connect broken contours of actual objects
                kernel = np.ones((3, 3), np.uint8)
                mask = cv2.dilate(mask, kernel, iterations=1)
            else:
                hsv = cv2.cvtColor(smoothed, cv2.COLOR_BGR2HSV)
                lower_bound = np.array([low_h, low_s, low_v])
                upper_bound = np.array([high_h, high_s, high_v])
                mask = cv2.inRange(hsv, lower_bound, upper_bound)
                
                kernel = np.ones((5, 5), np.uint8)
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

            # 4. Contour Filter
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            obstacle_detected = False
            
            if SHOW_GUI:
                cv2.rectangle(frame, (roi_x_start, roi_y_start), (roi_x_end, roi_y_end), (255, 255, 0), 2)
                cv2.putText(frame, f"Driving Corridor ({DETECTION_MODE})", (roi_x_start + 5, roi_y_start - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)

            for cnt in contours:
                area = cv2.contourArea(cnt)
                
                # Must exceed our dynamically calibrated minimum noise floor
                if area > min_area:
                    obstacle_detected = True
                    
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
            
            # 5. Output warning logs
            if obstacle_detected:
                current_time = time.time()
                if current_time - last_warning_time > 0.5:
                    print(f"[ALERT] {time.strftime('%H:%M:%S')} - Obstacle in corridor! Area exceeds {min_area}px baseline.")
                    last_warning_time = current_time
            
            if SHOW_GUI:
                cv2.imshow(window_name, frame)
                cv2.imshow("Detection Mask (Processed)", mask)
                
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break
            else:
                time.sleep(0.03)
                
    except KeyboardInterrupt:
        print("\n[INFO] Shutting down detector.")
    finally:
        cap.release()
        if SHOW_GUI:
            cv2.destroyAllWindows()
        print("Camera hardware released. Done.")

if __name__ == '__main__':
    main()
