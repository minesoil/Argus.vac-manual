#!/usr/bin/env python3
"""
Argus Vac - Lidar Watchdog (v1.0) For Orange Pi 5
Watches the RPLidar C1 and stops the robot when anything solid gets too close
in front of it. Covers what the camera cannot see: glass furniture legs, dark
objects on dark floors, anything outside the camera's frame.

Protocol reuse (deliberate - no firmware change needed):
    Sends standard "R <name> <risk> <x> <y>" packets where risk is derived from
    the nearest distance inside the forward cone:
        dist <= HALT_MM          -> risk 95+  -> Mega AUTO-HALTs itself
        HALT_MM < dist < WARN_MM -> scaled warning risk
        dist >= WARN_MM          -> silent (nothing sent)
    Never sends G. Releasing a halt stays human-only (same rule as the detector).

Two drivers:
    --mock   synthetic turntable scan (fully testable anywhere, no hardware)
    --real   rplidar-compatible driver on the Pi (pip3 install rplidar)
             Tested with the RPLidar C1 over /dev/ttyUSB0. If your C1 uses the
             newer SLAMTEC protocol, install Slamtec's sllidar python demo and
             point LidarDriver.open() at it - the interface is one method.

Usage on the Pi:
    python3 lidar-watch.py --real --serial /dev/ttyACM0
Bench test anywhere (no lidar, no Mega needed if SERIAL_ENABLED stays False):
    python3 lidar-watch.py --mock
"""

import argparse
import math
import time

# --- shared serial helpers straight from the detector (one implementation) ---
import importlib.util
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_V10_CANDIDATES = [
    os.path.join(_HERE, "obstacle-detector-mediapipe-v10.6.py"),
    "/home/orangepi/argus_vac/obstacle-detector-mediapipe-v10.6.py",
]
_v10 = None
for _p in _V10_CANDIDATES:
    if os.path.exists(_p):
        _spec = importlib.util.spec_from_file_location("v10mod", _p)
        _v10 = importlib.util.module_from_spec(_spec)
        _spec.loader.exec_module(_v10)
        break
if _v10 is None:
    raise SystemExit("Could not find obstacle-detector-mediapipe-v10.6.py next to me "
                     "- keep both files in the same folder on the Pi.")

SERIAL_ENABLED = False       # flip True after the Mega passes bench testing
SERIAL_PORT = "/dev/ttyACM0"
SERIAL_BAUD = 115200

# --- watchdog tuning ---
FORWARD_CENTER_DEG = 0.0     # lidar angle that points straight ahead (set after mounting)
HALF_CONE_DEG = 40.0         # only care about things roughly in front
HALT_MM = 300                # at/below this: auto-halt territory (risk 95+)
WARN_MM = 700                # above this: ignore
MIN_VALID_MM = 120           # C1 near-field junk below this distance is discarded
SEND_MIN_GAP_S = 0.8         # throttle between R packets
ALERT_PRINT_GAP_S = 2.0


def nearest_in_cone(points, center_deg, half_cone_deg):
    """
    points: iterable of (angle_deg, dist_mm).
    Returns nearest valid distance within half_cone_deg of center (wrap-safe),
    else None.
    """
    best = None
    for ang, dist in points:
        if dist is None or dist < MIN_VALID_MM:
            continue
        d = (float(ang) - center_deg + 180.0) % 360.0 - 180.0
        if abs(d) <= half_cone_deg:
            if best is None or dist < best:
                best = float(dist)
    return best


def distance_to_risk(dist_mm):
    """Map distance to the Mega's risk scale. None-safe."""
    if dist_mm is None:
        return None
    if dist_mm <= HALT_MM:
        return 95 + int(min(4, (HALT_MM - dist_mm) / 50))
    if dist_mm >= WARN_MM:
        return None
    frac = (WARN_MM - dist_mm) / float(WARN_MM - HALT_MM)   # 0..1
    return int(30 + frac * 60)                               # warn zone: 30..90


class MockDriver:
    """Deterministic turntable: wall ring at 2000mm + optional obstacle."""

    def __init__(self):
        self.obstacle_dist = None   # set externally to simulate objects
        self.obstacle_ang = 0.0

    def open(self):
        pass

    def iter_scans(self):
        while True:
            pts = []
            for deg in range(0, 360, 2):
                jitter = ((deg * 7919) % 13) - 6           # stable pseudo-noise
                pts.append((float(deg), 2000.0 + jitter))
            if self.obstacle_dist is not None:
                for ddeg in range(-6, 7, 2):
                    ang = (self.obstacle_ang + ddeg) % 360.0
                    pts.append((ang, float(self.obstacle_dist)))
            yield pts
            time.sleep(0.1)

    def close(self):
        pass


class RealDriver:
    """Thin adapter around the community 'rplidar' package."""

    def __init__(self, port, baud=115200):
        self.port = port
        self.baud = baud
        self.lidar = None

    def open(self):
        from rplidar import RPLidar
        self.lidar = RPLidar(self.port, baudrate=self.baud)
        info = self.lidar.get_info()
        print(f"[LIDAR] Connected: {info}")

    def iter_scans(self):
        for scan in self.lidar.iter_scans():
            yield [(m[1], m[2]) for m in scan]     # (quality, angle, dist)->(ang,dist)

    def close(self):
        try:
            self.lidar.stop()
            self.lidar.disconnect()
        except Exception:
            pass


def run(driver, serial_enabled):
    state = {"name": None, "risk": None, "cx": None, "cy": None,
             "last_any": 0.0, "last_halt": 0.0}
    last_alert = 0.0
    if serial_enabled:
        _v10.SERIAL_ENABLED = True
        _v10.SERIAL_PORT = SERIAL_PORT
        _v10.SERIAL_BAUD = SERIAL_BAUD
        print(f"[SERIAL] Link ON -> {SERIAL_PORT} @ {SERIAL_BAUD}")
    else:
        print("[SERIAL] Link OFF (dry run). Set SERIAL_ENABLED=True when the Mega is live.")

    print(f"[WATCH] Cone +/-{HALF_CONE_DEG:.0f} deg around {FORWARD_CENTER_DEG:.0f} deg | "
          f"halt<={HALT_MM}mm warn<={WARN_MM}mm")
    for pts in driver.iter_scans():
        now = time.monotonic()
        dist = nearest_in_cone(pts, FORWARD_CENTER_DEG, HALF_CONE_DEG)
        risk = distance_to_risk(dist)

        if risk is not None:
            summary = {"name": "LIDAR", "score": risk / 100.0,
                       "box": [0.0, 0.0, float(dist or 1.0), float(dist or 1.0)]}
            lines, state = _v10.serial_decide(state, summary, now)
            for ln in lines:
                if ln.startswith("R "):
                    # firmware packet: cx=angle, cy=distance (documented mapping)
                    parts = ln.split(" ")
                    ln = f"R LIDAR {parts[2]} {int(FORWARD_CENTER_DEG)} {int(dist or 0)}"
                    state.update({"cx": int(FORWARD_CENTER_DEG), "cy": int(dist or 0)})
                print(f"[SERIAL TX] {ln}")
                _v10._serial_send(ln)
            if now - last_alert > ALERT_PRINT_GAP_S:
                print(f"[WATCH] nearest={dist:.0f}mm risk={risk}%")
                last_alert = now
        elif dist is not None and now - last_alert > ALERT_PRINT_GAP_S:
            print(f"[WATCH] clear ({dist:.0f}mm)")
            last_alert = now


def main():
    global FORWARD_CENTER_DEG, HALF_CONE_DEG, HALT_MM, WARN_MM, SERIAL_ENABLED
    ap = argparse.ArgumentParser()
    ap.add_argument("--mock", action="store_true", help="synthetic scans, no hardware")
    ap.add_argument("--real", action="store_true", help="real RPLidar on --lidar-port")
    ap.add_argument("--lidar-port", default="/dev/ttyUSB0")
    ap.add_argument("--center-deg", type=float, default=FORWARD_CENTER_DEG,
                    help="lidar angle pointing straight ahead (set after mounting)")
    ap.add_argument("--half-cone", type=float, default=HALF_CONE_DEG)
    ap.add_argument("--halt-mm", type=int, default=HALT_MM)
    ap.add_argument("--warn-mm", type=int, default=WARN_MM)
    ap.add_argument("--serial", action="store_true", help="enable the Arduino link")
    args = ap.parse_args()

    FORWARD_CENTER_DEG = args.center_deg
    HALF_CONE_DEG = args.half_cone
    HALT_MM = args.halt_mm
    WARN_MM = args.warn_mm

    if args.mock:
        drv = MockDriver()
    elif args.real:
        drv = RealDriver(args.lidar_port)
    else:
        raise SystemExit("Pick --mock or --real")

    drv.open()
    try:
        run(drv, serial_enabled=args.serial)
    except KeyboardInterrupt:
        print("\n[WATCH] stopped.")
    finally:
        drv.close()


if __name__ == "__main__":
    main()
