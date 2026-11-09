"""Inspect floor tape and print steering decisions while the robot is stationary."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import ipaddress
import math
from pathlib import Path
import time
import urllib.error
import urllib.parse
import urllib.request

try:
    import cv2
    import numpy as np
except ModuleNotFoundError:
    cv2 = None
    np = None

FLOOR_START = 0.76


@dataclass(frozen=True)
class TapeDecision:
    state: str
    reason: str
    error: float | None = None
    center_x: float | None = None
    confidence: float = 0.0


def stop(reason):
    return TapeDecision("STOP", reason)


def decide_tape(frame, tape="black"):
    """Evaluate a BGR camera frame using a lower-frame floor region.

    Error is horizontal displacement from image center divided by half the
    image width. Negative values mean left. This estimates line alignment,
    without estimating obstacle clearance or distance travelled.
    """
    if cv2 is None or np is None:
        raise RuntimeError("Camera preview requires OpenCV and NumPy on the Pi")
    if tape not in ("black", "white", "blue"):
        raise ValueError("Tape must be black, white or blue")
    if not isinstance(frame, np.ndarray) or frame.dtype != np.uint8:
        return stop("Camera frame is missing or has an unsupported pixel format")
    if frame.ndim != 3 or frame.shape[2] != 3:
        return stop("Expected a colour camera frame")
    height, width = frame.shape[:2]
    if height < 120 or width < 160:
        return stop("Camera frame is too small for the floor preview")

    # The mounted camera's usable floor starts below the chassis/background.
    floor = frame[int(height * FLOOR_START):height, :]
    floor_height = floor.shape[0]
    gray = cv2.cvtColor(floor, cv2.COLOR_BGR2GRAY)
    contrast = float(np.percentile(gray, 99) - np.percentile(gray, 1))
    if tape == "blue":
        hsv = cv2.cvtColor(floor, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (90, 90, 45), (130, 255, 255))
        contrast_score = 1.0
    else:
        if contrast < 40:
            return stop("Floor and tape have too little contrast")
        threshold_mode = cv2.THRESH_BINARY_INV if tape == "black" else cv2.THRESH_BINARY
        _, mask = cv2.threshold(gray, 0, 255, threshold_mode | cv2.THRESH_OTSU)
        contrast_score = min(1.0, contrast / 100.0)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    fraction = float(np.count_nonzero(mask)) / mask.size
    if fraction < 0.005:
        return stop("No continuous tape found in the floor view")
    if fraction > 0.35:
        return stop("Too much of the floor matches the tape colour")

    count, labels, statistics, _ = cv2.connectedComponentsWithStats(mask, connectivity=8)
    candidates = []
    for label in range(1, count):
        x, y, component_width, component_height, area = statistics[label]
        if component_height < floor_height * 0.60 or y + component_height < floor_height * 0.90:
            continue
        if area < mask.size * 0.005:
            continue
        component = labels == label
        row_widths = component.sum(axis=1)
        visible = row_widths > 0
        coverage = float(visible.mean())
        if coverage < 0.70:
            continue
        median_width = float(np.median(row_widths[visible]))
        if not width * 0.01 <= median_width <= width * 0.20:
            continue
        if component_width > width * 0.45:
            continue
        # Separate segments across the same row indicate a fork or crossing.
        starts = component[:, :1].astype(np.int16).sum(axis=1)
        starts += (np.diff(component.astype(np.int16), axis=1) == 1).sum(axis=1)
        branched = float((starts > 1).mean()) > 0.10
        broad = float((row_widths > width * 0.30).mean()) > 0.05
        candidates.append((component, coverage, branched or broad))

    if not candidates:
        return stop("Tape must extend continuously through the lower floor view")
    if len(candidates) != 1 or candidates[0][2]:
        return stop("Multiple paths or a crossing are ambiguous")
    component, coverage, _ = candidates[0]
    centers = []
    for start, end in ((0.20, 0.40), (0.65, 0.90)):
        rows, columns = np.nonzero(component[int(floor_height * start):int(floor_height * end)])
        if not len(columns):
            return stop("Tape is missing from a steering band")
        centers.append(float(np.mean(columns)))
    center_x = centers[0] * 0.30 + centers[1] * 0.70
    error = max(-1.0, min(1.0, (center_x - width / 2) / (width / 2)))
    confidence = coverage * contrast_score
    if confidence < 0.60:
        return stop("Tape alignment is uncertain")
    state = "LEFT" if error < -0.10 else "RIGHT" if error > 0.10 else "FORWARD"
    return TapeDecision(state, "One continuous tape path", error, center_x, confidence)


def print_decision(decision):
    error = "unknown" if decision.error is None else f"{decision.error:+.2f}"
    print(f"{decision.state:7}  offset {error:7}  confidence {decision.confidence:.2f}  {decision.reason}", flush=True)


def save_overlay(frame, decision, destination):
    overlay = frame.copy()
    height, width = overlay.shape[:2]
    cv2.line(overlay, (width // 2, int(height * FLOOR_START)), (width // 2, height - 1), (0, 180, 255), 2)
    if decision.center_x is not None:
        x = round(decision.center_x)
        cv2.line(overlay, (x, int(height * FLOOR_START)), (x, height - 1), (0, 220, 0), 2)
    cv2.putText(overlay, decision.state, (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 180, 255), 2)
    destination.parent.mkdir(parents=True, exist_ok=True)
    if not cv2.imwrite(str(destination), overlay):
        raise OSError(f"Could not save overlay to {destination}")


def positive_seconds(value):
    number = float(value)
    if not 0 < number <= 300:
        raise argparse.ArgumentTypeError("Choose a duration above zero and at most 300 seconds")
    return number


def check_snapshot_headers(headers, now_raw, previous_grab=None, max_age_s=0.25):
    """Validate uStreamer capture metadata against the same host's RAW clock.

    Return the accepted grab timestamp. Callers retain it only after the whole
    reading succeeds. A cached or repeated frame cannot advance this timestamp.
    """
    if not math.isfinite(now_raw) or not math.isfinite(max_age_s) or max_age_s <= 0:
        raise ValueError("Invalid camera freshness clock or limit")
    values = {key.lower(): value for key, value in headers.items()}
    if str(values.get("x-ustreamer-online", "")).strip().lower() != "true":
        raise ValueError("Camera reports offline or lacks online metadata")
    try:
        grab = float(values["x-ustreamer-grab-timestamp"])
        sent = float(values["x-ustreamer-send-timestamp"])
    except (KeyError, TypeError, ValueError) as error:
        raise ValueError("Camera capture timestamps are missing or invalid") from error
    if not math.isfinite(grab) or not math.isfinite(sent):
        raise ValueError("Camera capture timestamps must be finite")
    if sent < grab or sent - grab > max_age_s:
        raise ValueError("Camera snapshot was stale when sent")
    if now_raw - grab > max_age_s or now_raw - grab < -0.02 or sent - now_raw > 0.02:
        raise ValueError("Camera capture is expired or uses a different clock")
    if previous_grab is not None and (not math.isfinite(previous_grab) or grab <= previous_grab):
        raise ValueError("Camera repeated a cached snapshot")
    return grab


def raw_clock():
    """uStreamer 4.9 uses CLOCK_MONOTONIC_RAW for capture timestamps."""
    try:
        return time.clock_gettime(time.CLOCK_MONOTONIC_RAW)
    except AttributeError as error:
        raise RuntimeError("Live freshness checks need the Pi's Linux RAW clock") from error


class SnapshotReader:
    """Read fresh uStreamer frames on the same Pi, without retaining old images."""

    def __init__(self, url="http://127.0.0.1:8080/snapshot", max_age_s=0.25):
        address = urllib.parse.urlsplit(url)
        try:
            loopback = address.hostname == "localhost" or ipaddress.ip_address(address.hostname).is_loopback
        except (TypeError, ValueError):
            loopback = False
        if address.scheme not in ("http", "https") or not loopback or address.username or address.password:
            raise ValueError("Live preview needs the Pi's loopback uStreamer address")
        if not math.isfinite(max_age_s) or max_age_s <= 0:
            raise ValueError("Camera maximum age must be positive and finite")
        self.url = url
        self.max_age_s = max_age_s
        self.last_grab = None
        self.capture_ok = False

    def read(self, timeout=2.0):
        self.capture_ok = False
        if cv2 is None or np is None:
            raise RuntimeError("Camera preview requires OpenCV and NumPy on the Pi")
        request = urllib.request.Request(self.url, headers={"Cache-Control": "no-cache"})
        with urllib.request.urlopen(request, timeout=timeout) as response:
            headers = response.headers
            jpeg = response.read(4 * 1024 * 1024 + 1)
        if len(jpeg) > 4 * 1024 * 1024:
            raise ValueError("Camera response exceeds the image size limit")
        frame = cv2.imdecode(np.frombuffer(jpeg, dtype=np.uint8), cv2.IMREAD_COLOR)
        if frame is None:
            raise ValueError("Camera response is not a decodable image")
        grab = check_snapshot_headers(headers, raw_clock(), self.last_grab, self.max_age_s)
        self.last_grab = grab
        self.capture_ok = True
        return frame

    def age_s(self):
        return None if self.last_grab is None else raw_clock() - self.last_grab

    def is_fresh(self):
        age = self.age_s()
        return self.capture_ok and age is not None and -0.02 <= age <= self.max_age_s


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tape", choices=("black", "white", "blue"), default="black")
    parser.add_argument("--seconds", type=positive_seconds, default=10.0)
    parser.add_argument("--url", default="http://127.0.0.1:8080/snapshot", help="Existing camera snapshot address")
    parser.add_argument("--image", type=Path, help="Inspect one saved camera frame instead of the live camera")
    parser.add_argument("--save-overlay", type=Path, help="Save the latest evaluated frame with alignment marks")
    args = parser.parse_args(argv)
    if cv2 is None or np is None:
        parser.exit(2, "OpenCV and NumPy are needed for this command. Check the Pi's existing Python environment.\n")
    if args.image:
        frame = cv2.imread(str(args.image))
        decision = decide_tape(frame, args.tape)
        print_decision(decision)
        if args.save_overlay and frame is not None:
            save_overlay(frame, decision, args.save_overlay)
        return 0 if decision.state != "STOP" else 1

    try:
        reader = SnapshotReader(args.url)
    except ValueError as error:
        parser.error(str(error))
    deadline = time.monotonic() + args.seconds
    decoded_frames = 0
    failed_frames = 0
    latest_capture_ok = False
    last_camera_error = "No fresh camera reading received"
    print(f"Stationary camera preview for {args.seconds:g} seconds. Tape colour {args.tape}.", flush=True)
    try:
        while time.monotonic() < deadline:
            started = time.monotonic()
            try:
                frame = reader.read(timeout=min(2.0, deadline - started))
                decision = decide_tape(frame, args.tape)
                if not reader.is_fresh():
                    raise ValueError("Camera frame expired during processing")
                decoded_frames += 1
                latest_capture_ok = True
                print_decision(decision)
                if args.save_overlay and frame is not None:
                    save_overlay(frame, decision, args.save_overlay)
            except (OSError, ValueError, RuntimeError, urllib.error.URLError, cv2.error) as error:
                latest_capture_ok = False
                failed_frames += 1
                last_camera_error = str(error)
                print_decision(stop(f"Camera reading failed: {last_camera_error}"))
            remaining = min(0.20 - (time.monotonic() - started), deadline - time.monotonic())
            if remaining > 0:
                time.sleep(remaining)
    except KeyboardInterrupt:
        print_decision(stop("Preview ended by operator"))
    else:
        if latest_capture_ok and reader.is_fresh():
            print_decision(stop(f"Preview finished; {decoded_frames} fresh frames, {failed_frames} failed readings"))
        else:
            reason = last_camera_error if not latest_capture_ok else "Last camera frame expired"
            print_decision(stop(f"Preview ended with camera fault: {reason}"))
    return 0 if latest_capture_ok and reader.is_fresh() else 1


if __name__ == "__main__":
    raise SystemExit(main())
