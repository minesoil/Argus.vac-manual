"""Apply the 30 cm chassis to the existing Ubuntu simulator, with rollback."""

from workspace_paths import workspace
from datetime import datetime
import math
import subprocess
import xml.etree.ElementTree as ET
import yaml

WS = workspace()
PACKAGE = WS / "src/vacuum_sim"
XACRO = "http://www.ros.org/wiki/xacro"
ET.register_namespace("xacro", XACRO)


def circle(radius, count=32):
    # Circumscribed polygon: never underestimate the circular shell.
    outer = radius / math.cos(math.pi / count)
    return [
        [
            round(-0.03 + outer * math.cos(2 * math.pi * i / count), 6),
            round(outer * math.sin(2 * math.pi * i / count), 6),
        ]
        for i in range(count)
    ]


def prepare_driving_views():
    launch = PACKAGE / "launch/sim.launch.py"
    text = launch.read_text()
    text = text.replace(
        "DeclareLaunchArgument('camera_rate', default_value='5')",
        "DeclareLaunchArgument('camera_rate', default_value='60')",
    )
    if "DeclareLaunchArgument('rviz_config'" not in text:
        text = text.replace(
            "DeclareLaunchArgument('rviz', default_value='true'),",
            "DeclareLaunchArgument('rviz', default_value='true'),\n"
            "        DeclareLaunchArgument('rviz_config', default_value=str(package / 'config/view.rviz')),",
        )
        text = text.replace(
            "arguments=['-d', str(package / 'config/view.rviz')]",
            "arguments=['-d', LaunchConfiguration('rviz_config')]",
        )
    compile(text, str(launch), "exec")
    model = PACKAGE / "urdf/vacuum.urdf.xacro"
    root = ET.fromstring(model.read_text())
    rate = root.find(f'{{{XACRO}}}arg[@name="camera_rate"]')
    if rate is None:
        raise RuntimeError("The camera rate argument is missing.")
    rate.set("default", "60")
    view = PACKAGE / "config/view.rviz"
    data = yaml.safe_load(view.read_text())
    data["Visualization Manager"]["Global Options"]["Frame Rate"] = 60
    drive_data = yaml.safe_load(yaml.safe_dump(data))
    drive_data["Visualization Manager"]["Global Options"]["Fixed Frame"] = "odom"
    drive_data["Visualization Manager"]["Displays"] = [
        item
        for item in drive_data["Visualization Manager"]["Displays"]
        if item.get("Class") != "rviz_default_plugins/Map"
    ]
    updates = {
        launch: text,
        model: ET.tostring(root, encoding="unicode") + "\n",
        view: yaml.safe_dump(data, sort_keys=False),
        PACKAGE / "config/drive.rviz": yaml.safe_dump(drive_data, sort_keys=False),
    }
    world = PACKAGE / "worlds/room.sdf"
    scene = ET.fromstring(world.read_text())
    # 180 Hz physics divides into 60 Hz camera/control, 30 Hz odometry, 10 Hz lidar.
    # At the 1.5 m/s limit a physics step covers about 8.3 mm.
    scene.find("world/physics/max_step_size").text = "0.005555555555555556"
    updates[world] = ET.tostring(scene, encoding="unicode") + "\n"
    changed = {
        path: value
        for path, value in updates.items()
        if not path.exists() or path.read_text() != value
    }
    if not changed:
        return
    backup = WS / "model-backups" / datetime.now().strftime("camera60-%Y%m%d-%H%M%S-%f")
    backup.mkdir(parents=True)
    originals = {path: path.read_bytes() if path.exists() else None for path in changed}
    for path, content in originals.items():
        if content is not None:
            saved = backup / path.relative_to(PACKAGE)
            saved.parent.mkdir(parents=True, exist_ok=True)
            saved.write_bytes(content)
    try:
        for path, value in changed.items():
            path.write_text(value)
        built = subprocess.run(
            [
                "/bin/bash",
                "-lc",
                "source env.sh; colcon build --symlink-install --packages-select vacuum_sim",
            ],
            cwd=WS,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=180,
        )
        if built.returncode:
            raise RuntimeError(
                "Camera configuration build failed: " + built.stdout[-4000:]
            )
    except BaseException:
        for path, content in originals.items():
            if content is None:
                path.unlink(missing_ok=True)
            else:
                path.write_bytes(content)
        raise
    print("Camera target set to 60 FPS; direct driving view prepared.", flush=True)


def prepare():
    """Update view settings without changing the saved robot assembly."""
    prepare_driving_views()


if __name__ == "__main__":
    prepare()
