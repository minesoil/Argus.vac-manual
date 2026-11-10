"""Export reviewed project source, not private configuration or build output.

Run from the local Argus workspace or a public repository clone. No networking,
hardware access, code execution, or automatic deletion is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil


EXCLUDED_DIRS = {"__pycache__", "node_modules", "build", "dist", "venv", ".venv", ".tools", ".state", ".ros", ".git", ".tmp"}
EXCLUDED_SUFFIXES = {".bin", ".elf", ".hex", ".uf2", ".map", ".o", ".a", ".so", ".dll", ".exe", ".pyc", ".zip", ".pem", ".key"}


def reviewed(path: Path, relative: Path) -> bool:
    if path.is_symlink():
        return False
    if any(p in EXCLUDED_DIRS for p in relative.parts):
        return False
    if any(p.startswith(".") and p != ".vscode" for p in relative.parts):
        return False
    if path.suffix.lower() in EXCLUDED_SUFFIXES:
        return False
    if path.name == "config.h" and relative.parts[-3:] != ("tests", "stubs", "config.h"):
        return False
    return True


def role(path: str) -> str:
    names = {
        "obstacles.py": "Calibrated floor-appearance detector and localhost preview.",
        "manual_guard.py": "Freshness checks and sequenced guard reports to ESP32.",
        "usb_bridge.py": "Single serial owner and phone-start/guard supervisor; now GPIO UART.",
        "serial_control.py": "Pi request/reply framing for ESP32 serial control.",
        "follow.py": "Bounded camera tape-following session and wheel percentages.",
        "line_preview.py": "Fresh camera snapshots and tape decisions without drive by default.",
        "core.py": "ROS-independent LiDAR avoidance algorithm.",
        "node.py": "Optional ROS 2 adapter around the LiDAR algorithm.",
        "simulate.py": "Lightweight modeled LiDAR/controller scenarios.",
        "bench.py": "Board/status, wall demo and scan-inspection commands.",
        "ManualGuard.h": "ESP32 assisted-mode bounds, guard expiry and stop latch.",
        "DriveControl.h": "ESP32 control ownership and driving-command expiry.",
        "PhoneStart.h": "Phone line-start token and heartbeat handling.",
        "ControlPacketParser.h": "Bounded parser for Pi serial messages.",
        "esp32_wifi_controlcam_auto.ino": "ESP32 Arduino setup/loop, UART, HTTP routes and phone UI.",
        "config.h.example": "Placeholder hotspot configuration; choose private values locally.",
        "argus": "Human-facing Bash command shortcuts.",
        "setup.py": "Python package and ROS executable/config installation metadata.",
        "package.xml": "ROS package dependencies and metadata.",
        "dashboard.js": "Static repository file browser and formatted file explanations.",
        "dashboard.css": "Dashboard layout and appearance.",
        "index.html": "Static dashboard page.",
    }
    name = Path(path).name
    if "/tests/" in path:
        return "Offline test or safe test stand-in for the neighboring implementation."
    if "mega-reference/" in path:
        return "Recovered M-command Mega source; exact installed binary is unverified."
    if name in names:
        return names[name]
    if "/systemd/" in path:
        return "Linux service or override for background program startup."
    if "/config/" in path or "/launch/" in path:
        return "ROS/simulation settings or output-disabled launch description."
    if "/reports/" in path:
        return "Dated verification evidence; consult current status for later results."
    if Path(path).suffix == ".md":
        return "Project explanation, instructions or dated design record."
    return "Supporting source, configuration, task or package resource."


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, required=True)
    parser.add_argument("--handbook", type=Path, required=True)
    parser.add_argument("--edition", default="2026-11-10")
    args = parser.parse_args()
    workspace, handbook = args.workspace.resolve(), args.handbook.resolve()
    local = workspace / "workspace"
    source_root = local if (local / "robot_control").is_dir() else workspace
    if not (source_root / "robot_control").is_dir():
        raise SystemExit("No maintained robot_control folder found; nothing copied.")
    planned: dict[str, tuple[Path, str]] = {}
    for folder in ("robot_control", "dashboard"):
        source = source_root / folder
        if not source.is_dir():
            raise SystemExit(f"Missing reviewed source folder: {folder}")
        for item in sorted(source.rglob("*")):
            relative = item.relative_to(source)
            if item.is_file() and reviewed(item, relative):
                planned[f"code/{folder}/{relative.as_posix()}"] = (
                    item, f"{folder}/{relative.as_posix()}")

    mega_sources = [
        (local / "github/argus-vac-firmware/mega/Arduino_Mega_Manual_Control/Arduino_Mega_Manual_Control.ino",
         "editable", "recovered editable Mega baseline"),
        (Path.home() / "OneDrive/Documents/Arduino/Arduino_Mega_Manual_Control/Arduino_Mega_Manual_Control.ino",
         "original", "recovered Arduino sketchbook original"),
    ]
    for source, label, origin in mega_sources:
        relative = f"code/mega-reference/{label}/Arduino_Mega_Manual_Control/Arduino_Mega_Manual_Control.ino"
        if source.is_file():
            planned[relative] = (source, origin)
        elif (handbook / relative).is_file():
            planned[relative] = (handbook / relative, origin)
        else:
            raise SystemExit(f"Missing reviewed Mega reference ({label}); recover before exporting.")

    code = handbook / "code"
    unexpected = [p.relative_to(handbook).as_posix() for p in code.rglob("*")
                  if p.is_file() and reviewed(p, p.relative_to(code))
                  and p.relative_to(handbook).as_posix() not in planned] if code.exists() else []
    if unexpected:
        raise SystemExit("Unexpected snapshot files need review; no files removed: " + ", ".join(unexpected))
    entries = []
    for relative, (source, origin) in sorted(planned.items()):
        destination = handbook / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        if source.resolve() != destination.resolve():
            shutil.copyfile(source, destination)
        data = destination.read_bytes()
        entries.append({"path": relative, "origin": origin, "bytes": len(data),
                        "sha256": hashlib.sha256(data).hexdigest(), "role": role(relative)})
    inventory = handbook / "inventory"
    inventory.mkdir(parents=True, exist_ok=True)
    manifest = {"edition": args.edition, "scope": "reviewed source snapshot, not a Pi disk image",
                "excluded": ["real config.h", "private .state", "credentials", "compiled firmware", "caches"],
                "files": entries}
    (inventory / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    lines = ["# Included files", "", f"Edition {args.edition}: {len(entries)} reviewed files.", "",
             "Every source copy is listed below. SHA-256 and origin are in [manifest.json](manifest.json).",
             "Reports retain dates; the current state is in [00_CURRENT_STATE.md](../00_CURRENT_STATE.md).", "",
             "| File | Role |", "|---|---|"]
    for e in entries:
        lines.append(f"| [{e['path']}](../{e['path']}) | {e['role']} |")
    (inventory / "FILES.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Exported {len(entries)} source files; no private config or binaries copied.")


if __name__ == "__main__":
    main()
