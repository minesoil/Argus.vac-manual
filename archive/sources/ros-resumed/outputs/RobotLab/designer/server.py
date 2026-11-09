#!/usr/bin/env python3
"""Local designer API: versioned saves, exports and bounded simulator updates.

Bind only to loopback. Writes require the session token and a same-origin request.
No endpoint accepts shell commands or arbitrary filesystem paths.
"""
import argparse
from datetime import datetime, timezone
import hashlib
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import io
import json
import mimetypes
import os
from pathlib import Path
import secrets
import subprocess
import threading
import urllib.parse
import uuid
import zipfile

from model import (
    compile_model,
    drive_geometry,
    footprint,
    hardware_description,
    validate,
)

ROOT = Path(__file__).resolve().parents[1]
WEB = Path(__file__).parent / "web"
MAX_BODY = 16 * 1024 * 1024
NAME = __import__("re").compile(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,63}$")


def atomic_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def revision(design):
    return hashlib.sha256(json.dumps(design, sort_keys=True).encode()).hexdigest()


class Store:
    def __init__(self, path):
        self.path = path
        path.mkdir(parents=True, exist_ok=True)
        self.lock = threading.Lock()
        if not (path / "default.json").exists():
            atomic_json(
                path / "default.json",
                json.loads((ROOT / "designs/default.json").read_text()),
            )

    def file(self, name):
        if not NAME.fullmatch(name):
            raise ValueError(
                "Use letters, numbers, hyphens or underscores in the file name."
            )
        return self.path / (name + ".json")

    def load(self, name):
        with self.lock:
            design = json.loads(self.file(name).read_text())
            return {"design": design, "revision": revision(design), "file": name}

    def save(self, name, design, expected):
        validate(design)
        with self.lock:
            path = self.file(name)
            if path.exists():
                old = json.loads(path.read_text())
                if revision(old) != expected:
                    raise FileExistsError(
                        "This file changed in another editor. Reload it or save with a new name."
                    )
                backup = (
                    self.path
                    / "history"
                    / (
                        name
                        + "-"
                        + datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S-%f")
                        + ".json"
                    )
                )
                atomic_json(backup, old)
            atomic_json(path, design)
            return {"revision": revision(design), "file": name}


def export_zip(design):
    model, meshes = compile_model(design)
    data = io.BytesIO()
    with zipfile.ZipFile(data, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("design.json", json.dumps(design, indent=2))
        archive.writestr("robot.simulation.urdf", model)
        archive.writestr("robot.hardware.urdf", hardware_description(model))
        archive.writestr(
            "README.txt",
            "Coordinates: X forward, Y left, Z up. JSON: metres/radians.\nMeshes install into vacuum_sim/meshes/design.\nHardware URDF excludes Gazebo plugins. Firmware settings live separately in firmware/mega_drive.\n",
        )
        for filename, content in meshes.items():
            archive.writestr("meshes/" + filename, content)
    return data.getvalue()


def apply_to_workspace(design, workspace, progress):
    """Stop owned simulation, update model/controller/footprint, rebuild, then restart.

    An open driving panel owns manual-input.lock. Reject the operation instead of
    changing geometry under a live controller. Source changes roll back on failure.
    """
    import fcntl
    import yaml

    geometry = drive_geometry(design)
    if not workspace or not (workspace / "src/vacuum_sim").is_dir():
        raise ValueError(
            "Simulation workspace is unavailable. Save or export this design instead."
        )
    lock_path = workspace / ".lab/manual-input.lock"
    lock_path.parent.mkdir(exist_ok=True)
    with lock_path.open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise ValueError(
                "Close the driving panel before applying a design."
            ) from exc
        # Reserve manual input until the model is fully rebuilt and restarted.
        run = lambda args, timeout=180: subprocess.run(
            args, cwd=workspace, text=True, capture_output=True, timeout=timeout
        )

        def checked(args, timeout=180):
            result = run(args, timeout)
            if result.returncode:
                raise RuntimeError((result.stdout + result.stderr)[-4000:])
            return result

        progress("Stopping simulation")
        checked(["python3", "tools/lab_controller.py", "stop"], 70)
        package = workspace / "src/vacuum_sim"
        model, meshes = compile_model(design)
        updates = {package / "urdf/designed.urdf": model.encode()}
        for name, content in meshes.items():
            updates[package / "meshes/design" / name] = content
        controllers = package / "config/controllers.yaml"
        config = yaml.safe_load(controllers.read_text())
        params = config["diff_drive_controller"]["ros__parameters"]
        params.update(
            wheel_radius=geometry["wheel_radius_m"],
            wheel_separation=geometry["wheel_separation_m"],
        )
        updates[controllers] = yaml.safe_dump(config, sort_keys=False).encode()
        fp = footprint(design)
        for filename in ("nav2.yaml", "vacuum_nav2.yaml"):
            path = package / "config" / filename
            config = yaml.safe_load(path.read_text())
            for name in ("local_costmap", "global_costmap"):
                p = config[name][name]["ros__parameters"]
                p["footprint"] = str(fp)
            guard = config["collision_monitor"]["ros__parameters"]
            guard["FootprintApproach"]["points"] = str(fp)
            # Preserve validated braking distances; expand the width for larger parts.
            width = max(abs(point[1]) for point in fp) + 0.05
            for zone in ("StopZone", "SlowZone"):
                if zone not in guard or "forward" not in guard[zone]:
                    continue
                for direction in ("forward", "reverse"):
                    points = json.loads(guard[zone][direction]["points"])
                    for point in points:
                        point[1] = width if point[1] > 0 else -width
                        if point[0] > 0:
                            point[0] = max(point[0], max(x[0] for x in fp) + 0.15)
                        if point[0] < -0.04:
                            point[0] = min(point[0], min(x[0] for x in fp) - 0.15)
                    guard[zone][direction]["points"] = str(points)
            updates[path] = yaml.safe_dump(config, sort_keys=False).encode()
        # Bridge reports/radius use the same active design. Simulation caps stay unchanged.
        profile_path = workspace / "tools/robot-profile.json"
        profile = json.loads(profile_path.read_text())
        profile["hardware"]["wheel_diameter_m"] = geometry["wheel_radius_m"] * 2
        profile["hardware"]["wheel_separation_m"] = geometry["wheel_separation_m"]
        updates[profile_path] = (json.dumps(profile, indent=2) + "\n").encode()
        marker = workspace / ".lab/custom-design.json"
        updates[marker] = json.dumps(
            {"design": design, "revision": revision(design), "footprint": fp}, indent=2
        ).encode()
        backup = (
            workspace
            / "model-backups"
            / ("design-" + datetime.now().strftime("%Y%m%d-%H%M%S-%f"))
        )
        originals = {p: p.read_bytes() if p.exists() else None for p in updates}
        for p, content in originals.items():
            if content is not None:
                saved = backup / p.relative_to(workspace)
                saved.parent.mkdir(parents=True, exist_ok=True)
                saved.write_bytes(content)
        try:
            progress("Building robot model")
            for p, content in updates.items():
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_bytes(content)
            checked(
                [
                    "/bin/bash",
                    "-lc",
                    "source env.sh; colcon build --symlink-install --packages-select vacuum_sim",
                ]
            )
            checked(
                [
                    "/bin/bash",
                    "-lc",
                    "source env.sh; check_urdf src/vacuum_sim/urdf/designed.urdf",
                ]
            )
            progress("Starting simulation")
            checked(["python3", "tools/lab_controller.py", "drive"], 180)
        except Exception:
            run(["python3", "tools/lab_controller.py", "stop"], 70)
            for p, content in originals.items():
                if content is None:
                    p.unlink(missing_ok=True)
                else:
                    p.write_bytes(content)
            run(
                [
                    "/bin/bash",
                    "-lc",
                    "source env.sh; colcon build --symlink-install --packages-select vacuum_sim",
                ]
            )
            raise
        return {
            "backup": str(backup),
            "geometry": geometry,
            "footprint": fp,
            "revision": revision(design),
        }


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *_):
        pass

    def reply(self, status, body, content_type="application/json"):
        if not isinstance(body, bytes):
            body = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.end_headers()
        self.wfile.write(body)

    def authorized(self):
        host = self.headers.get("Host", "")
        if host not in (
            f"localhost:{self.server.server_port}",
            f"127.0.0.1:{self.server.server_port}",
        ):
            return False
        origin = self.headers.get("Origin")
        if origin and origin not in (f"http://{host}",):
            return False
        return secrets.compare_digest(
            self.headers.get("X-Robot-Lab-Token", ""), self.server.token
        )

    def do_GET(self):
        url = urllib.parse.urlparse(self.path)
        if url.path.startswith("/api/"):
            if not self.authorized():
                return self.reply(403, {"error": "Open this editor from the launcher."})
            try:
                query = urllib.parse.parse_qs(url.query)
                if url.path == "/api/state":
                    return self.reply(
                        200,
                        dict(
                            self.server.store.load(query.get("name", ["default"])[0]),
                            files=sorted(
                                p.stem for p in self.server.store.path.glob("*.json")
                            ),
                            data_dir=str(self.server.store.path),
                            can_apply=bool(self.server.workspace),
                            version="3.0",
                        ),
                    )
                if url.path == "/api/job":
                    with self.server.job_lock:
                        job = dict(self.server.job)
                    return self.reply(200, job)
                return self.reply(404, {"error": "Unknown operation."})
            except (ValueError, FileNotFoundError) as exc:
                return self.reply(400, {"error": str(exc)})
        path = (WEB / urllib.parse.unquote(url.path).lstrip("/")).resolve()
        if url.path == "/":
            path = WEB / "index.html"
        if not path.is_relative_to(WEB) or not path.is_file():
            return self.reply(404, {"error": "File not found."})
        self.reply(
            200,
            path.read_bytes(),
            mimetypes.guess_type(str(path))[0] or "application/octet-stream",
        )

    def do_POST(self):
        if not self.authorized():
            return self.reply(403, {"error": "Invalid editor session."})
        try:
            size = int(self.headers.get("Content-Length", "0"))
            if not 0 < size <= MAX_BODY:
                return self.reply(413, {"error": "Request exceeds 16 MB."})
            data = json.loads(self.rfile.read(size))
            path = urllib.parse.urlparse(self.path).path
            if path == "/api/save":
                return self.reply(
                    200,
                    self.server.store.save(
                        data["file"], data["design"], data.get("revision")
                    ),
                )
            if path == "/api/export":
                return self.reply(200, export_zip(data["design"]), "application/zip")
            if path == "/api/validate":
                validate(data["design"])
                try:
                    result = {
                        "geometry": drive_geometry(data["design"]),
                        "drive_valid": True,
                    }
                except ValueError as exc:
                    result = {"drive_valid": False, "reason": str(exc)}
                return self.reply(
                    200, dict(result, footprint=footprint(data["design"]))
                )
            if path == "/api/apply":
                drive_geometry(data["design"])
                with self.server.job_lock:
                    if self.server.job.get("running"):
                        raise ValueError("A simulation update is already running.")
                    self.server.job = {
                        "running": True,
                        "stage": "Queued",
                        "id": uuid.uuid4().hex,
                    }

                def execute():
                    def progress(stage):
                        with self.server.job_lock:
                            self.server.job["stage"] = stage

                    try:
                        result = apply_to_workspace(
                            copy_design(data["design"]), self.server.workspace, progress
                        )
                        with self.server.job_lock:
                            self.server.job.update(
                                running=False, stage="Applied", result=result
                            )
                    except Exception as exc:
                        with self.server.job_lock:
                            self.server.job.update(
                                running=False, stage="Failed", error=str(exc)
                            )

                threading.Thread(target=execute, daemon=True).start()
                return self.reply(202, {"started": True})
            return self.reply(404, {"error": "Unknown operation."})
        except FileExistsError as exc:
            return self.reply(409, {"error": str(exc)})
        except (ValueError, KeyError, TypeError) as exc:
            return self.reply(400, {"error": str(exc)})
        except Exception as exc:
            return self.reply(500, {"error": str(exc)})


def copy_design(design):
    return json.loads(json.dumps(design))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, required=True)
    parser.add_argument("--ready-file", type=Path)
    parser.add_argument("--workspace", type=Path)
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--token", required=True)
    args = parser.parse_args()
    server = None
    for port in range(args.port, args.port + 20):
        try:
            server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
            break
        except OSError:
            if port == args.port + 19:
                raise
    server.token = args.token
    server.store = Store(args.data_dir)
    server.workspace = args.workspace
    server.job_lock = threading.Lock()
    server.job = {"running": False, "stage": "Idle"}
    session = {
        "url": f"[REDACTED_CREDENTIAL_URL]",
        "token": args.token,
        "port": server.server_port,
        "pid": os.getpid(),
    }
    if args.ready_file:
        atomic_json(args.ready_file, session)
    print(session["url"], flush=True)
    try:
        server.serve_forever()
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
