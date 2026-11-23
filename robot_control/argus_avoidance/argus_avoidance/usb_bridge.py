"""Keep one serial owner for local automatic requests and optional phone frames."""

import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import math
from pathlib import Path
import subprocess
import signal
import sys
import threading
import time
import urllib.parse

from .follow import ControlError
from .line_preview import SnapshotReader
from .serial_control import SerialAutoClient
from .manual_guard import GuardPublisher
from .lidar_hub import LidarHub, ESP_PORT
from .roam import (CLOSE_WALL_MAX_PERCENT, CLOSE_WALL_MAX_SECONDS, FAST_WALL_MAX_SECONDS,
                   WALL_FOLLOW_MAX_PERCENT, WALL_FOLLOW_SLOW_PERCENT)


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
        if self.path == "/lidar/sweep":
            hub = getattr(self.server, "lidar_hub", None)
            if hub is None or hub.error:
                self.reply(503, {"error": hub.error if hub is not None else "C1 unavailable"})
                return
            sweep = hub.latest
            self.reply(200, {"sweep": None if sweep is None else {
                "sequence": sweep.sequence, "started": sweep.started,
                "finished": sweep.finished, "nodes": sweep.nodes,
                "ranges": [value if math.isfinite(value) else None
                           for value in sweep.ranges]}})
            return
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


def claim_phone_start(controller, state, follower, launch=subprocess.Popen, roam_args=None):
    """Claim one request; a changed epoch means Stop or takeover won."""
    if not state.get("follow_pending"):
        return follower
    kind = state.get("follow_kind", "tape")
    if kind not in ("tape", "roam") or (kind == "roam" and roam_args is None):
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
    command = ([sys.executable, "-u", "-m", "argus_avoidance.roam", "--drive"] + roam_args
               if kind == "roam" else
               [sys.executable, "-m", "argus_avoidance.follow", "--drive", "--seconds", "30"])
    return launch(command + ["--expected-epoch", str(epoch)])


def load_roam_args(path, lidar_bridge=False):
    """Load commissioned roam or an explicitly capped, low-power phone trial."""
    if path is None:
        return None
    profile = json.loads(Path(path).read_text())
    commissioned = profile.get("commissioned") is True
    trial = profile.get("trial_enabled") is True and not commissioned
    if not commissioned and not trial:
        return None
    follow_wall = profile.get("follow_wall")
    stop_ahead = profile.get("stop_ahead") is True
    close_radius = profile.get("close_wall_radius_m")
    if follow_wall not in (None, "left", "right"):
        raise ValueError("follow_wall must be left or right")
    required = ("lidar", "front_deg", "sensor_x", "sensor_y", "radius")
    if any(key not in profile for key in required):
        raise ValueError("Roam profile requires lidar, front_deg, sensor_x, sensor_y, radius")
    if trial:
        seconds = profile.get("seconds", 20)
        trial_limit = CLOSE_WALL_MAX_SECONDS if close_radius is not None else 20
        if (profile.get("continuous") is True or isinstance(seconds, bool)
                or not isinstance(seconds, (int, float)) or not 0 < seconds <= trial_limit):
            raise ValueError(f"Phone trial requires a duration from 1 to {trial_limit} seconds")
        cruise, slow, turn = (profile.get(key, 12) for key in ("cruise", "slow", "turn"))
        cruise_limit = WALL_FOLLOW_MAX_PERCENT if follow_wall else 12
        if (any(type(value) is not int for value in (cruise, slow, turn))
                or not 1 <= slow <= cruise <= cruise_limit or not 1 <= turn <= 12):
            raise ValueError(f"Phone trial requires cruise at or below {cruise_limit}% and turn at or below 12%")
        slow_limit = CLOSE_WALL_MAX_PERCENT if close_radius is not None else WALL_FOLLOW_SLOW_PERCENT
        if follow_wall and slow > slow_limit:
            raise ValueError(f"Phone wall trial slow speed must be at or below {slow_limit}%")
        fast_limit = 10 if stop_ahead else FAST_WALL_MAX_SECONDS
        if (follow_wall and close_radius is None and cruise > WALL_FOLLOW_SLOW_PERCENT
                and seconds > fast_limit):
            raise ValueError(f"Phone wall trial above 15% requires a duration of at most {fast_limit} seconds")
    result = ["--commissioned" if commissioned else "--trial"]
    for key in required + ("cruise", "slow", "turn"):
        if key in profile:
            value = "bridge" if key == "lidar" and lidar_bridge else profile[key]
            result.extend(["--" + key.replace("_", "-"), str(value)])
    if "wall_gap" in profile:
        result.extend(["--wall-gap", str(profile["wall_gap"])])
    if follow_wall is not None:
        result.extend(["--follow-wall", follow_wall])
    if profile.get("finish_at_wall_end") is True:
        if follow_wall is None:
            raise ValueError("Finishing at the wall end requires wall following")
        result.append("--finish-at-wall-end")
    if close_radius is not None:
        if (not trial or "--finish-at-wall-end" not in result or
                type(close_radius) not in (int, float) or not math.isfinite(close_radius)):
            raise ValueError("Close wall radius requires a finite radius and a bounded wall-end trial")
        result.extend(["--close-wall-radius", str(close_radius)])
    if stop_ahead:
        result.append("--stop-ahead")
    if profile.get("continuous") is True:
        result.append("--continuous")
    else:
        result.extend(["--seconds", str(profile.get("seconds", 20 if trial else 30))])
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--serial", default="/dev/argus_esp32",
                        help="ESP32 USB port; COM ports also support a laptop bench relay")
    parser.add_argument("--no-phone-preview", action="store_true",
                        help="Keep USB available for control without relaying phone JPEGs")
    parser.add_argument("--manual-guard", action="store_true",
                        help="Publish local obstacle-preview health to assisted-manual firmware")
    parser.add_argument("--roam-config", help="Measured C1 roaming profile; missing/uncommissioned disables roaming")
    args = parser.parse_args(argv)
    profile = json.loads(Path(args.roam_config).read_text()) if args.roam_config else {}
    hub = None
    if profile.get("lidar"):
        try:
            hub = LidarHub(profile["lidar"], profile.get("map_port", ESP_PORT),
                           front_deg=float(profile.get("front_deg", 90))).start()
            hub.open_map_port()
            relay_status = "disabled" if hub.esp_port is None else "optional"
            print(f"C1 scanner ready; ESP32 map relay {relay_status}", flush=True)
        except (OSError, ValueError) as error:
            if hub is not None:
                hub.close()
            hub = None
            print(f"C1 map unavailable: {error}; drive bridge remains available", flush=True)
    roam_args = load_roam_args(args.roam_config, lidar_bridge=hub is not None)
    try:
        controller = SerialAutoClient(args.serial)
    except BaseException:
        if hub:
            hub.close()
        raise
    camera = SnapshotReader()
    server = ThreadingHTTPServer(("127.0.0.1", 8766), BridgeHandler)
    server.daemon_threads = True
    server.controller = controller
    server.usb_lock = threading.Lock()
    server.lidar_hub = hub
    ended = threading.Event()
    thread = None
    follower = None
    guard = GuardPublisher(controller, "http://127.0.0.1:8767/status") if args.manual_guard else None
    signal.signal(signal.SIGTERM, lambda *_: ended.set())
    try:
        for attempt in range(3):
            try:
                initial = controller.request("/state")
                break
            except ControlError:
                if attempt == 2:
                    raise
                time.sleep(0.5)
        print(f"ESP32 serial ready on {args.serial}, mode {initial['mode']}", flush=True)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        state = initial
        next_health = 0.0
        while not ended.wait(0.1 if guard or hub else 0.5):
            # A USB reconnect invalidates the old descriptor even if this
            # process is still running. Probe without renewing any drive lease.
            with server.usb_lock:
                if time.monotonic() >= next_health:
                    state = controller.request("/state")
                    follower = claim_phone_start(controller, state, follower, roam_args=roam_args)
                    next_health = time.monotonic() + 0.5
                if guard:
                    guard.tick(state)
            if hub:
                hub.relay_once()
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
        if hub:
            hub.close()


if __name__ == "__main__":
    try:
        main()
    except (ControlError, OSError) as error:
        print(f"Serial bridge stopped: {error}. Check the Pi-to-ESP32 connection.", flush=True)
        raise SystemExit(1)
