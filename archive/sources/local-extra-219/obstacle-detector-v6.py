#!/usr/bin/env python3
"""
Argus Vac - Calibrated Obstacle Detector (v6)
Target: Orange Pi 5 (8GB) -> USB camera -> Arduino Mega 2560 actuator bridge

This version replaces the v5 runtime auto-calibration with FIXED thresholds
derived directly from a physical lighting/HSV/edge diagnostic pass, since
that data is now known:

    - Avg floor luminance:   185.47  (bright, low-contrast floor)
    - Exposure std dev:       8.046  (auto-exposure hunting -> lock it)
    - Mean floor saturation: 13.55   (near-grayscale floor)
    - Mean floor value:      187.44  (bright floor)
    - Canny density @(100,200): 1.080%  (very clean floor texture)

Engineering changes vs v5:
    1. Explicit auto-exposure lock attempt on startup (V4L2-style controls),
       to stop the ~8px exposure oscillation from creating phantom edges.
    2. Bilateral filter on the ROI before any edge/color processing.
    3. EDGE mode fixed at Canny(80, 200), min contour area 2500px.
    4. HSV mode fixed with S >= 60, V >= 60 to reject the near-grayscale floor.
    5. Single file, SHOW_GUI toggle preserved for headless SSH or local X11.
"""

import cv2
import numpy as np
import sys
import time

# ==================== CONFIGURATION ====================
SHOW_GUI = False          # True for X11-forwarded windows, False for headless/SSH
DETECTION_MODE = "EDGE"   # "EDGE" (Canny, primary) or "HSV" (color isolation, secondary)

# --- Calibrated Edge Mode (primary) ---
CANNY_LOW = 80
CANNY_HIGH = 200
MIN_AREA_EDGE = 2500       # px, filters remaining sensor speckle above the 1.08% floor noise

# --- Calibrated HSV Mode (secondary) ---
# Floor mean S=13.55, V=187.44 -> reject anything the floor could plausibly produce
HSV_LOW = (0, 60, 60)
HSV_HIGH = (179, 255, 255)
MIN_AREA_HSV = 1500

# --- Driving corridor ROI (bottom-middle of frame) ---
ROI_TOP_PCT = 0.55
ROI_LEFT_PCT = 0.3
ROI_RIGHT_PCT = 0.7

WARNING_COOLDOWN_S = 0.5
# =======================================================


def lock_auto_exposure(cap):
    """
    Attempt to disable/lock camera auto-exposure to remove the ~8px luminance
    oscillation seen in diagnostics. Behavior is driver-dependent (V4L2 on
    Linux/Orange Pi), so we try the common values and verify what stuck.
    """
    print("[INIT] Attempting to lock auto-exposure (V4L2)...")

    # For most UVC/V4L2 webcams: 1 = manual mode, 3 = aperture-priority (auto)
    attempts = [1, 0.25]
    locked = False
    for val in attempts:
        ok = cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, val)
        current = cap.get(cv2.CAP_PROP_AUTO_EXPOSURE)
        if ok:
            print(f"  -> Set CAP_PROP_AUTO_EXPOSURE={val}, camera reports {current}")
            locked = True
            break

    # Optionally pin exposure to a fixed value once manual mode is engaged.
    # This value is a reasonable starting point for a bright ~185 luminance floor;
    # tune with `v4l2-ctl --list-ctrls` / `--set-ctrl=exposure_absolute=N` if needed.
    cap.set(cv2.CAP_PROP_EXPOSURE, 150)

    if not locked:
        print("  [WARN] Camera driver did not confirm manual exposure mode.")
        print("         Falling back to per-frame intensity normalization instead.")

    return locked


def normalize_intensity(gray):
    """
    Fallback for cameras whose driver ignores CAP_PROP_AUTO_EXPOSURE.
    CLAHE evens out residual exposure drift without washing out real edges.
    """
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    return clahe.apply(gray)


def get_roi(frame):
    height, width = frame.shape[:2]
    y0 = int(height * ROI_TOP_PCT)
    y1 = height
    x0 = int(width * ROI_LEFT_PCT)
    x1 = int(width * ROI_RIGHT_PCT)
    return frame[y0:y1, x0:x1], (x0, y0, x1, y1)


def process_edge(roi):
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray = normalize_intensity(gray)
    edges = cv2.Canny(gray, CANNY_LOW, CANNY_HIGH)
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.dilate(edges, kernel, iterations=1)
    return mask, MIN_AREA_EDGE


def process_hsv(roi):
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    lower = np.array(HSV_LOW)
    upper = np.array(HSV_HIGH)
    mask = cv2.inRange(hsv, lower, upper)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    return mask, MIN_AREA_HSV


def main():
    print("=====================================================")
    print("      ARGUS VAC - CALIBRATED OBSTACLE DETECTOR (v6)   ")
    print("=====================================================")
    print(f"Mode: {DETECTION_MODE} | Display: {'GUI' if SHOW_GUI else 'HEADLESS'}")
    print("Starting USB camera capture...")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[ERROR] Could not open USB camera (index 0).")
        print("Please verify your camera is plugged into the Orange Pi 5.")
        sys.exit(1)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    lock_auto_exposure(cap)
    time.sleep(1.0)  # let exposure settings actually take effect

    print("\n-----------------------------------------------------")
    print("Using fixed, diagnostic-calibrated thresholds:")
    print(f"  EDGE mode: Canny({CANNY_LOW}, {CANNY_HIGH}), min area {MIN_AREA_EDGE}px")
    print(f"  HSV mode:  S>={HSV_LOW[1]}, V>={HSV_LOW[2]}, min area {MIN_AREA_HSV}px")
    print("-----------------------------------------------------")
    print("Obstacle Detector is ACTIVE.\n")

    window_name = "Argus Vac - Calibrated Detector"
    if SHOW_GUI:
        cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

    last_warning_time = 0

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("[WARNING] Failed to grab frame from USB camera.")
                time.sleep(0.1)
                continue

            roi, (x0, y0, x1, y1) = get_roi(frame)
            smoothed = cv2.bilateralFilter(roi, 9, 75, 75)

            if DETECTION_MODE == "EDGE":
                mask, min_area = process_edge(smoothed)
            else:
                mask, min_area = process_hsv(smoothed)

            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            obstacle_detected = False

            if SHOW_GUI:
                cv2.rectangle(frame, (x0, y0), (x1, y1), (255, 255, 0), 2)
                cv2.putText(frame, f"Driving Corridor ({DETECTION_MODE})", (x0 + 5, y0 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 1)

            for cnt in contours:
                area = cv2.contourArea(cnt)
                if area > min_area:
                    obstacle_detected = True
                    if SHOW_GUI:
                        bx, by, bw, bh = cv2.boundingRect(cnt)
                        gx, gy = x0 + bx, y0 + by
                        proximity = (gy + bh - y0) / (frame.shape[0] - y0)
                        severity = "CRITICAL" if proximity > 0.7 else "WARNING"
                        color = (0, 0, 255) if severity == "CRITICAL" else (0, 165, 255)
                        cv2.rectangle(frame, (gx, gy), (gx + bw, gy + bh), color, 3)
                        cv2.putText(frame, f"{severity}: Obj ({int(area)}px)", (gx, gy - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

            if obstacle_detected:
                now = time.time()
                if now - last_warning_time > WARNING_COOLDOWN_S:
                    print(f"[ALERT] {time.strftime('%H:%M:%S')} - Obstacle in corridor "
                          f"(area > {min_area}px threshold).")
                    last_warning_time = now

            if SHOW_GUI:
                cv2.imshow(window_name, frame)
                cv2.imshow("Detection Mask", mask)
                if cv2.waitKey(1) & 0xFF == ord('q'):
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
