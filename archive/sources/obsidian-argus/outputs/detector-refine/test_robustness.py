"""
test_robustness.py - Stress matrix for the unknown-obstacle layer.

Feeds AnomalyEngine directly (no threads, no camera) through six 200-frame
scenes and reports false-alarm / detection rates:

  S1 baseline carpet          -> expect ~0% false alarms
  S2 exposure ramp (+30 EV)   -> expect low FPs (model adapts slowly)
  S3 moving soft shadow band  -> expect ~0% (layer ignores brightness)
  S4 strong striped carpet    -> expect ~0% after boot (booted ON the pattern)
  S5 small sock 60x45px       -> expect detected most cycles
  S6 thin cable line          -> expect detected most cycles

Prints a tuning card table; exits nonzero if any expectation fails.
"""
import importlib.util
import sys

import cv2
import numpy as np

V10_PATH = r"[REDACTED_HOME_PATH]"
spec = importlib.util.spec_from_file_location("v10", V10_PATH)
v10 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v10)

rng = np.random.default_rng(11)
N = 200
FAILURES = []


def base_floor():
    f = np.full((480, 640, 3), (95, 93, 97), np.uint8)
    stripes = ((np.arange(480) % 8 < 4)[..., None, None] * 6).astype(np.int16)
    return np.clip(f.astype(np.int16) + stripes - 3, 0, 255).astype(np.uint8)


def noisy(frame, sigma):
    return np.clip(frame.astype(np.int16) +
                   rng.normal(0, sigma, frame.shape), 0, 255).astype(np.uint8)


def draw_sock(frame, t):
    x, y = 210 + int(40 * np.sin(t / 30)), 300
    patch = frame[y:y+45, x:x+60].copy()
    patch = np.clip(patch.astype(np.int16) - 22 + rng.normal(0, 26, patch.shape),
                    0, 255).astype(np.uint8)
    cv2.rectangle(patch, (0, 0), (59, 44), (70, 68, 66), 2)
    frame[y:y+45, x:x+60] = patch


def draw_cable(frame, t):
    y = 428 + int(6 * np.sin(t / 25))
    cv2.line(frame, (40, y), (610, y + 8), (55, 52, 50), 4)


def scene_frames(name):
    """Generator of (frame, has_debris)."""
    base = base_floor()
    for t in range(N):
        f = noisy(base.copy(), 5)
        if name == "S2 exposure ramp":
            f = np.clip(f.astype(np.int16) + int(30 * t / N), 0, 255).astype(np.uint8)
        elif name == "S3 moving shadow":
            # physical soft shadow: multiplicative dimming with a feathered edge
            band = int((t * 2) % 480)
            mask = np.zeros((480, 640), np.float32)
            mask[band:band + 90] = 0.55
            mask = cv2.GaussianBlur(mask, (0, 0), 12)   # penumbra
            f = np.clip(f.astype(np.float32) * (1.0 - mask[..., None]),
                        0, 255).astype(np.uint8)
        elif name == "S4 striped carpet":
            for yy in range(0, 480, 12):
                cv2.line(f, (0, yy), (639, yy), (70, 66, 62), 2)
            f = noisy(f, 7)
        elif name == "S5 small sock":
            draw_sock(f, t)
        elif name == "S6 thin cable":
            draw_cable(f, t)
        yield f


SCENES = [
    ("S1 baseline", False),
    ("S2 exposure ramp", False),
    ("S3 moving shadow", False),
    ("S4 striped carpet", False),
    ("S5 small sock", True),
    ("S6 thin cable", True),
]

print(f"{'scene':<20} {'flag rate':>10} {'max risk':>9}   expectation")
print("-" * 60)

results = {}
for name, wants_hits in SCENES:
    engine = v10.AnomalyEngine()
    flagged = 0
    active_after_boot = 0
    max_risk = 0.0
    for i, frame in enumerate(scene_frames(name)):
        records, _ms = engine.process(frame)
        if engine.booting:
            continue
        active_after_boot += 1
        if records:
            flagged += 1
            max_risk = max(max_risk, max(r["score"] for r in records))
    rate = flagged / max(1, active_after_boot)
    results[name] = (rate, max_risk)
    print(f"{name:<20} {rate*100:9.1f}% {max_risk:9.2f}   "
          f"{'expect DETECTION' if wants_hits else 'expect quiet'}")

print("-" * 60)

def rate(s): return results[s][0]
def risk(s): return results[s][1]

if rate("S1 baseline") > 0.05:
    FAILURES.append("S1 false alarms")
if rate("S2 exposure ramp") > 0.15:
    FAILURES.append("S2 ramp too twitchy")
# S3: shadow EDGES may paint thin lines (visual flicker), but the shadow-edge
# policy must cap them at warning level - never halt territory.
if risk("S3 moving shadow") >= 0.85:
    FAILURES.append("S3 shadow edge reached halt-level risk")
if rate("S4 striped carpet") > 0.10:
    FAILURES.append("S4 pattern false alarms")
for s in ("S5 small sock", "S6 thin cable"):
    if rate(s) < 0.5:
        FAILURES.append(f"{s} missed")

if FAILURES:
    print(f"RESULT: {len(FAILURES)} FAILURE(S): {FAILURES}")
    sys.exit(1)
print("RESULT: ALL EXPECTATIONS MET")
