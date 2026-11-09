"""
test_dashboard.py - Validates the v10.2 web dashboard routes.

Starts the real _MJPEGHandler on an ephemeral port with seeded state, then:
  GET /        -> HTML mission view
  GET /threat  -> JSON (none when clear; name/score/cx/cy when seeded)
  GET /stats   -> text stats line
  GET /stream  -> multipart/x-mixed-replace content type
  GET /nope    -> 404
"""
import importlib.util
import sys
import threading
import time
import urllib.request

V10_PATH = r"[REDACTED_HOME_PATH]"

spec = importlib.util.spec_from_file_location("v10", V10_PATH)
v10 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v10)

from http.server import ThreadingHTTPServer

srv = ThreadingHTTPServer(("127.0.0.1", 0), v10._MJPEGHandler)
port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
time.sleep(0.2)

FAILURES = []


def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    print(f"  [{status}] {name}" + (f"  ({detail})" if detail else ""))
    if not cond:
        FAILURES.append(name)


def get(path):
    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}{path}", timeout=3) as r:
            return r.status, dict(r.headers), r.read()
    except urllib.error.HTTPError as e:
        return e.code, {}, e.read()
    except Exception as e:
        return 0, {}, str(e).encode()


# --- clear state ---
status, headers, body = get("/")
html = body.decode("utf-8", "replace")
check("/ serves the mission view shell",
      status == 200 and "Mission View" in html and "stream" in html
      and "app.js" in html and "style.css" in html,
      f"{len(body)} bytes")
check("dashboard has banner, stats block and threat table",
      'id="banner"' in html and 'id="stats"' in html and 'id="threat-table"' in html)

status, headers, body = get("/style.css")
check("/style.css served as css",
      status == 200 and "text/css" in headers.get("Content-type", "")
      and b".banner" in body)
status, headers, body = get("/app.js")
check("/app.js served as javascript",
      status == 200 and "javascript" in headers.get("Content-type", "")
      and b"pollThreat" in body)

status, headers, body = get("/threat")
check("/threat reports none when clear",
      status == 200 and b'"name": "none"' in body, body[:40])

# --- seed a threat ---
with v10._result_lock:
    v10._latest_risk_summary = {"name": "OBSTACLE?", "score": 0.87,
                                "box": [300.0, 340.0, 80.0, 80.0], "kind": "unknown"}

status, headers, body = get("/threat")
payload = body.decode("ascii", "replace")
check("/threat carries name+score+center",
      '"OBSTACLE?"' in payload and '"cx": 340' in payload and '"cy": 380' in payload,
      payload[:60])

status, _, body = get("/stats")
check("/stats serves a stats line", status == 200 and b"cam=" in body, body[:50])

# stream: just verify headers via a short read
import http.client
conn = http.client.HTTPConnection("127.0.0.1", port, timeout=3)
conn.request("GET", "/stream")
resp = conn.getresponse()
check("/stream is MJPEG multipart", resp.status == 200 and
      resp.getheader("Content-type", "").startswith("multipart/x-mixed-replace"))
resp.close()
conn.close()

status, _, _ = get("/bogus")
check("unknown path -> 404", status == 404)

# clear seeded threat so other runs start clean
with v10._result_lock:
    v10._latest_risk_summary = None

print("\n" + "=" * 60)
if FAILURES:
    print(f"RESULT: {len(FAILURES)} FAILURE(S): {FAILURES}")
    sys.exit(1)
print("RESULT: ALL TESTS PASSED")
