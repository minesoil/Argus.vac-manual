"""Temporarily add a camera to the running simulator and save a room overview."""

from workspace_paths import workspace
import struct
import subprocess
import time
import zlib
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import Image

WS = workspace()
out = WS / "validation/furnished-20261007"
out.mkdir(parents=True, exist_ok=True)
sdf = out / "preview-camera.sdf"
sdf.write_text(
    """<sdf version="1.9"><model name="room_preview"><static>true</static>
<pose>-12.0 -10.0 20.0 0 0.91 0.695</pose><link name="camera">
<sensor name="overview" type="camera"><topic>/room_preview</topic><always_on>true</always_on><update_rate>1</update_rate>
<camera><horizontal_fov>1.1</horizontal_fov><image><width>1200</width><height>900</height><format>R8G8B8</format></image>
<clip><near>0.05</near><far>45</far></clip></camera></sensor></link></model></sdf>"""
)
rclpy.init()
node = Node("furnished_room_preview_capture")
images = []
node.create_subscription(Image, "/room_preview", images.append, qos_profile_sensor_data)
bridge = None
created = False
try:
    result = subprocess.run(
        [
            "/opt/ros/jazzy/lib/ros_gz_sim/create",
            "-world",
            "vacuum_room",
            "-file",
            str(sdf),
            "-name",
            "room_preview",
            "-x",
            "-12",
            "-y",
            "-10",
            "-z",
            "20",
            "-R",
            "0",
            "-P",
            ".91",
            "-Y",
            ".695",
        ],
        capture_output=True,
        text=True,
        timeout=20,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    created = True
    log = (out / "preview-bridge.log").open("w")
    bridge = subprocess.Popen(
        [
            "/opt/ros/jazzy/lib/ros_gz_bridge/parameter_bridge",
            "/room_preview@sensor_msgs/msg/Image[gz.msgs.Image",
        ],
        stdout=log,
        stderr=subprocess.STDOUT,
    )
    end = time.monotonic() + 25
    while not images and time.monotonic() < end:
        rclpy.spin_once(node, timeout_sec=0.1)
    assert images, "Preview camera did not publish"
    m = images[-1]
    assert m.encoding == "rgb8", m.encoding
    data = bytes(m.data)
    raw = b"".join(
        b"\0" + data[y * m.step : y * m.step + m.width * 3] for y in range(m.height)
    )

    def chunk(kind, data):
        return (
            struct.pack(">I", len(data))
            + kind
            + data
            + struct.pack(">I", zlib.crc32(kind + data))
        )

    png = (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", struct.pack(">IIBBBBB", m.width, m.height, 8, 2, 0, 0, 0))
        + chunk(b"IDAT", zlib.compress(raw))
        + chunk(b"IEND", b"")
    )
    path = out / "room-overview.png"
    path.write_bytes(png)
    print(path, flush=True)
finally:
    if bridge:
        bridge.terminate()
        try:
            bridge.wait(timeout=5)
        except subprocess.TimeoutExpired:
            bridge.kill()
            bridge.wait(timeout=2)
        log.close()
    if created:
        result = subprocess.run(
            [
                "gz",
                "service",
                "-s",
                "/world/vacuum_room/remove",
                "--reqtype",
                "gz.msgs.Entity",
                "--reptype",
                "gz.msgs.Boolean",
                "--timeout",
                "5000",
                "--req",
                'name: "room_preview", type: MODEL',
            ],
            capture_output=True,
            text=True,
            timeout=8,
        )
        print(
            "Preview camera removal:",
            result.stdout.strip(),
            result.stderr.strip(),
            flush=True,
        )
    node.destroy_node()
    rclpy.shutdown()
