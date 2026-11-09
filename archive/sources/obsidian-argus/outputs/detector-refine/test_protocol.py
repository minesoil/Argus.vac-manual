"""
test_protocol.py - Software-in-the-loop test of the Pi <-> Mega link.

Part 1: A VirtualMega TCP server that mirrors mega-controller.ino's exact
        command handling (P/S/B/V/H/G/R, boot banner, auto-halt at risk>=85).
        Conformance-checks framing and the command vocabulary.
Part 2: FULL LOOP: real detector threads (fake camera) + serial_decide +
        a socket adapter plugged in as the serial port. A high-risk obstacle
        is planted; the test asserts the detector's H arrives at the virtual
        Mega and triggers its AUTO-HALT path. Also asserts the detector never
        sends G (releasing halts stays human-only).
"""
import importlib.util
import socket
import sys
import threading
import time

V10_PATH = r"[REDACTED_HOME_PATH]"

spec = importlib.util.spec_from_file_location("v10", V10_PATH)
v10 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v10)

FAILURES = []


def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    print(f"  [{status}] {name}" + (f"  ({detail})" if detail else ""))
    if not cond:
        FAILURES.append(name)


from virtual_mega import VirtualMega, SocketSerial, AUTO_HALT_RISK

# ============================================================================
print("\nPART 1 - VirtualMega conformance (framing + vocabulary)")
print("=" * 60)

mega = VirtualMega()
mega.start()
time.sleep(0.3)
ser = SocketSerial(mega.port)

def drain():
    out = []
    try:
        while True:
            chunk = ser.sock.recv(4096)
            if not chunk:
                break
            out.append(chunk)
    except socket.timeout:
        pass
    return b"".join(out).decode("ascii", "replace")

banner = drain()
check("boot banner says HALTED", "HALTED" in banner, banner.strip()[:60])

ser.write(b"P\n")
time.sleep(0.2)
check("P -> ACK", "ACK ARGUS-MEGA ready" in drain())

ser.write(b"S 1\n")   # halted at boot -> must refuse politely
time.sleep(0.2)
check("drive refused while halted", "Drive OFF" in drain())

ser.write(b"G\n"); time.sleep(0.15); drain()
ser.write(b"S 1\n"); time.sleep(0.2)
check("drive accepted after G", "Drive ON" in drain())
ser.write(b"H\n"); time.sleep(0.15); drain()
ser.write(b"S 1\n"); time.sleep(0.2)
check("H re-latches and refuses drive", "Drive OFF" in drain())

ser.write(b"G\n"); time.sleep(0.15); drain()
ser.write(b"R OBSTACLE? 92 320 380\n"); time.sleep(0.25)
resp = drain()
check("R at 92% triggers firmware AUTO-HALT", "AUTO-HALT: camera threat OBSTACLE? risk 92" in resp, resp.strip())
ser.write(b"R sock 40 100 100\n"); time.sleep(0.2)
resp = drain()
check("low-risk R only noted (already halted)", "Threat noted: sock 40" in resp)

# ============================================================================
print("\nPART 2 - full loop: detector threads -> serial wire -> virtual Mega")
print("=" * 60)

from mediapipe.tasks.python import BaseOptions
from mediapipe.tasks.python import vision

opts = vision.ObjectDetectorOptions(
    base_options=BaseOptions(model_asset_path="efficientdet_lite2.tflite"),
    score_threshold=v10.CONFIDENCE_THRESHOLD,
    running_mode=vision.RunningMode.VIDEO,
    max_results=v10.MAX_RESULTS)
det = vision.ObjectDetector.create_from_options(opts)


class CleanCam:
    def __init__(self):
        self.base = np.full((480, 640, 3), (95, 93, 97), np.uint8)
        self.n = 0
        self.t0 = time.perf_counter()

    def isOpened(self):
        return True

    def read(self):
        self.n += 1
        target = self.n / 30.0
        behind = target - (time.perf_counter() - self.t0)
        if behind > 0:
            time.sleep(min(behind, 0.05))
        return True, self.base.copy()

    def release(self):
        pass


import numpy as np

cam = CleanCam()

# plug the socket adapter in as the serial port BEFORE enabling serial
v10._serial_port = ser
v10.SERIAL_ENABLED = True

stop = v10._stop_event
threads = [
    threading.Thread(target=v10._capture_thread_fn, args=(cam,), daemon=True),
    threading.Thread(target=v10._inference_thread_fn, args=(det,), daemon=True),
    threading.Thread(target=v10._render_thread_fn, args=(False,), daemon=True),
]
for th in threads:
    th.start()

# let the anomaly layer finish booting on clean floor (~3s at 10Hz)
time.sleep(6)

# release the boot-time halt (as a human would) so the robot is "live",
# then mark the log: everything after this must be caused by the detector
ser.write(b"G\n")
time.sleep(0.3)
drain()
with mega.log_lock:
    log_mark = len(mega.log)   # everything AFTER this belongs to part 2

def part2_tx():
    with mega.log_lock:
        return [m for k, m in mega.log[log_mark:] if k == "TX"]

# plant a HIGH-RISK track and keep it alive like a persistent detection
seed_stop = threading.Event()


def seeder():
    box = [240.0, 340.0, 160.0, 130.0]
    rec = {"name": "OBSTACLE?", "score": 0.93, "box": box, "kind": "unknown"}
    while not seed_stop.is_set():
        now_ms = time.monotonic() * 1000.0
        with v10._result_lock:
            existing = next((t for t in v10._latest_tracks if t["name"] == "OBSTACLE?"), None)
            if existing is None:
                v10._latest_tracks.append({**rec, "last_seen_ms": now_ms})
            else:
                existing["last_seen_ms"] = now_ms
                existing["score"] = 0.93
        seed_stop.wait(0.15)


seed_th = threading.Thread(target=seeder, daemon=True)
seed_th.start()

t_seed = time.time()
auto_halt_at = None
deadline = time.time() + 8
while time.time() < deadline:
    txs = part2_tx()
    if any("AUTO-HALT" in m for m in txs):
        auto_halt_at = time.time() - t_seed
        break
    time.sleep(0.05)

seed_stop.set()
time.sleep(0.5)

all_tx = part2_tx()
g_sent = [m for m in all_tx if m.startswith("Halt released")]
halt_lines = [m for m in all_tx if "HALT latched" in m or "AUTO-HALT" in m]
r_lines = [m for m in all_tx if m.startswith("Threat noted")]

with v10._stats_lock:
    sent = v10._stats.get("serial_sent", 0)

print(f"\n  detector->mega packets observed : {len(all_tx)} TX lines")
print(f"  sample packets                  : {[m[:46] for m in all_tx[:4]]}")
if auto_halt_at is not None:
    print(f"  auto-halt arrived after         : {auto_halt_at:.2f}s")
else:
    print("  auto-halt NEVER ARRIVED")

fired = auto_halt_at is not None and auto_halt_at < 6.0
label = f"{auto_halt_at:.2f}s" if auto_halt_at is not None else "never"
check(f"auto-halt fired ({label})", fired)
check("detector reached the virtual Mega over the wire", len(all_tx) > 0)
check("firmware is latched in HALT state now", mega.halted is True)
check("detector NEVER sent G (human-only rule)", len(g_sent) == 0)
check("R packet carried full payload (name + risk through to firmware)",
      any("camera threat OBSTACLE? risk 93" in m for m in all_tx),
      f"{[m[:60] for m in all_tx]}")
check(f"serial stats counter advanced ({sent})", sent > 0)

stop.set()
for th in threads:
    th.join(timeout=2.0)
det.close()
ser.close()
mega.running = False

print("\n" + "=" * 60)
if FAILURES:
    print(f"RESULT: {len(FAILURES)} FAILURE(S): {FAILURES}")
    sys.exit(1)
print("RESULT: ALL TESTS PASSED")
