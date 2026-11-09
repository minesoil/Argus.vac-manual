"""Keep one serial owner for local automatic requests and optional phone frames."""

import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import subprocess
import signal
import sys
import threading
import time
import urllib.parse

from .follow import ControlError
from .line_preview import SnapshotReader
from .serial_control import SerialAutoClient


class BridgeHandler(BaseHTTPRequestHandler):
    def log_message(self, *_):
        pass

    def reply(self, status, value):
        body = b"" if status == 204 else json.dumps(value).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def forward(self, values=None):
        allowed = ("/state",) if values is None else ("/auto/arm", "/auto/drive", "/auto/stop")
        if self.path not in allowed:
            self.reply(404, {"error": "Unknown bridge request"})
            return
        try:
            with self.server.usb_lock:
                result = self.server.controller.request(self.path, values)
            self.reply(result.get("status", 200), result)
        except (ControlError, OSError) as error:
            self.reply(getattr(error, "status", 503), {"error": str(error)})
        except (KeyError, ValueError):
            self.reply(400, {"error": "Missing or invalid control fields"})

    def do_GET(self):
        self.forward()

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= 1024:
                raise ValueError("Invalid request size")
            fields = urllib.parse.parse_qs(self.rfile.read(length).decode("ascii"), strict_parsing=True)
            if any(len(value) != 1 for value in fields.values()):
                raise ValueError("Duplicate fields")
            values = {name: value[0] for name, value in fields.items()}
        except (ValueError, UnicodeError):
            self.reply(400, {"error": "Expected one set of URL-encoded control fields"})
            return
        self.forward(values)


def claim_phone_start(controller, state, follower, launch=subprocess.Popen):
    """Claim one request; a changed epoch means Stop or takeover won."""
    if not state.get("follow_pending"):
        return follower
    epoch, token = state.get("epoch"), state.get("follow_token")
    try:
        controller.request("/follow/claim", {"epoch": epoch, "token": token})
    except ControlError as error:
        if error.status != 409:
            raise
        return follower
    if follower is not None and follower.poll() is None:
        return follower
    return launch([
        sys.executable, "-m", "argus_avoidance.follow", "--drive",
        "--seconds", "30", "--expected-epoch", str(epoch),
    ])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--serial", default="/dev/argus_esp32",
                        help="ESP32 USB port; COM ports also support a laptop bench relay")
    parser.add_argument("--no-phone-preview", action="store_true",
                        help="Keep USB available for control without relaying phone JPEGs")
    args = parser.parse_args(argv)
    controller = SerialAutoClient(args.serial)
    camera = SnapshotReader()
    server = ThreadingHTTPServer(("127.0.0.1", 8766), BridgeHandler)
    server.daemon_threads = True
    server.controller = controller
    server.usb_lock = threading.Lock()
    ended = threading.Event()
    thread = None
    follower = None
    signal.signal(signal.SIGTERM, lambda *_: ended.set())
    try:
        initial = controller.request("/state")
        print(f"ESP32 serial ready on {args.serial}, mode {initial['mode']}", flush=True)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        while not ended.wait(0.5):
            # A USB reconnect invalidates the old descriptor even if this
            # process is still running. Probe without renewing any drive lease.
            with server.usb_lock:
                state = controller.request("/state")
                follower = claim_phone_start(controller, state, follower)
            if args.no_phone_preview:
                continue
            try:
                frame = camera.read(timeout=0.20)
            except (OSError, ValueError, RuntimeError):
                continue
            with server.usb_lock:
                controller.relay_camera(frame)
    except KeyboardInterrupt:
        pass
    finally:
        if follower is not None and follower.poll() is None:
            follower.terminate()
            try:
                follower.wait(timeout=1)
            except subprocess.TimeoutExpired:
                follower.kill()
        if thread is not None:
            server.shutdown()
            thread.join(timeout=1)
        server.server_close()
        controller.close()


if __name__ == "__main__":
    try:
        main()
    except (ControlError, OSError) as error:
        print(f"Serial bridge stopped: {error}. Check the Pi-to-ESP32 connection.", flush=True)
        raise SystemExit(1)
