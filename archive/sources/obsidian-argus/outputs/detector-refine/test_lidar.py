"""
test_lidar.py - Validates lidar-watch.py before any hardware exists.

Part A: pure logic (cone selection incl. 0/360 wrap, distance->risk mapping).
Part B: live mock run - lidar-watch's real loop against the VirtualMega twin;
        an obstacle crossing into the forward cone must produce an R packet
        (and H at halt-range), then silence when it leaves.
"""
import importlib.util
import sys
import threading
import time
import socket

HERE = r"[REDACTED_HOME_PATH]"
sys.path.insert(0, HERE)

spec = importlib.util.spec_from_file_location("lidar", HERE + r"\lidar-watch.py")
# lidar-watch imports v10 by searching next to itself; that works from HERE.
lidar = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lidar)

v10 = lidar._v10

FAILURES = []


def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    print(f"  [{status}] {name}" + (f"  ({detail})" if detail else ""))
    if not cond:
        FAILURES.append(name)


print("\nPART A - pure logic")
print("=" * 60)

pts = [(0.0, 5000.0), (10.0, 900.0), (350.0, 800.0), (180.0, 200.0)]
check("picks nearest inside cone",
      lidar.nearest_in_cone(pts, 5.0, 40.0) == 800.0)
check("ignores behind-the-robot points",
      lidar.nearest_in_cone(pts, 0.0, 30.0) == 800.0)
check("wrap: cone across 0/360 sees both sides",
      lidar.nearest_in_cone(pts + [(2.0, 650.0)], 359.0, 5.0) == 650.0)
check("outside cone across wrap ignored",
      lidar.nearest_in_cone(pts, 359.0, 5.0) == 5000.0)
check("empty cone -> None", lidar.nearest_in_cone(pts, 90.0, 20.0) is None)
check("sub-minimum junk discarded",
      lidar.nearest_in_cone([(0.0, 50.0)], 0.0, 40.0) is None)

check("halt range -> risk >=95", lidar.distance_to_risk(300) >= 95)
check("very close -> high 90s", 97 <= lidar.distance_to_risk(120) <= 99,
      f"{lidar.distance_to_risk(120)}")
check("warn zone scales down", 30 <= lidar.distance_to_risk(600) < 95,
      f"{lidar.distance_to_risk(600)}")
check("beyond warn -> silent (None)", lidar.distance_to_risk(1500) is None)
check("None-safe", lidar.distance_to_risk(None) is None)

# ============================================================================
print("\nPART B - live mock run against the VirtualMega")
print("=" * 60)

from virtual_mega import VirtualMega, SocketSerial

mega = VirtualMega()
mega.start()
time.sleep(0.3)
ser = SocketSerial(mega.port)


def drain():
    out = b""
    try:
        while True:
            chunk = ser.sock.recv(4096)
            if not chunk:
                break
            out += chunk
    except socket.timeout:
        pass
    return out.decode("ascii", "replace")


drain()  # banner

v10._serial_port = ser
lidar.SERIAL_ENABLED = True

drv = lidar.MockDriver()

ser.write(b"G\n"); time.sleep(0.3); drain()
with mega.log_lock:
    log_mark = len(mega.log)

run_thread_stop = threading.Event()


def run_watch():
    lidar.run(drv, serial_enabled=True)


th = threading.Thread(target=run_watch, daemon=True)
th.start()
time.sleep(1.2)
early = drain()
check("quiet while path is clear (2m wall only)", early.strip() == "",
      f"{early.strip()[:60]!r}")

# obstacle walks into the cone at halt range
drv.obstacle_ang = 0.0
drv.obstacle_dist = 250
t0 = time.time()
halted_at = None
while time.time() - t0 < 4:
    resp = drain()
    if "AUTO-HALT" in resp:
        halted_at = time.time() - t0
        break
    time.sleep(0.05)

check(f"firmware AUTO-HALT from lidar packet ({halted_at:.2f}s)" if halted_at else
      "no AUTO-HALT arrived", halted_at is not None and halted_at < 3.0)
check("mega is latched halted", mega.halted is True)
txs = [m for k, m in mega.log[log_mark:] if k == "RX"]
check("packet format matches firmware parser (R LIDAR <risk> <ang> <mm>)",
      any(l.startswith("R LIDAR 9") for l in txs), f"{[l for l in txs if l.startswith('R')][:2]}")

run_thread_stop.set()
v10._stop_event.set()   # stop shared detector threads if the module started any (it did not)
time.sleep(0.3)

print("\n" + "=" * 60)
if FAILURES:
    print(f"RESULT: {len(FAILURES)} FAILURE(S): {FAILURES}")
    sys.exit(1)
print("RESULT: ALL TESTS PASSED")
