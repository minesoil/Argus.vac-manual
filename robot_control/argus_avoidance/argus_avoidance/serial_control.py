"""ESP32 automatic sessions over USB or a direct GPIO UART."""

import json
import struct
import time

from .follow import ControlError, ESP32AutoClient


CONTROL_MAGIC = bytes((0xA5, 0xDA, 0xC3, 0xBC))


def control_packet(payload):
    data = payload.encode("ascii")
    if not 1 <= len(data) <= 160 or any(value >= 128 for value in data):
        raise ValueError("Invalid USB control payload")
    # All outgoing control bytes have their high bit set. Legacy Mega ASCII
    # motor commands cannot be produced by a probe to a misidentified adapter.
    length = bytes((0x80 | (len(data) & 127), 0x80 | (len(data) >> 7)))
    return CONTROL_MAGIC + length + bytes(value | 0x80 for value in data)


class SerialAutoClient(ESP32AutoClient):
    def __init__(self, port, timeout=0.25):
        import serial

        super().__init__("http://localhost", timeout)
        self.port = serial.Serial(port=None, baudrate=115200, timeout=0.015,
                                  write_timeout=0.15, exclusive=True)
        self.port.dtr = False
        self.port.rts = False
        self.port.port = port
        self.port.open()
        self.buffer = bytearray()
        self.request_id = 0
        self.last_relay = 0.0
        # Allow a partial camera packet from the previous program to expire.
        time.sleep(1.6)
        self.port.reset_input_buffer()

    def request(self, endpoint, values=None):
        values = values or {}
        arguments = {
            "/state": ("state", ()),
            "/follow/claim": ("claim", ("epoch", "token")),
            "/auto/arm": ("arm", ("epoch",)),
            "/auto/drive": ("drive", ("session", "seq", "l", "r")),
            "/auto/stop": ("stop", ("session",)),
        }
        if endpoint not in arguments:
            raise ValueError("Unsupported USB control operation")
        action, names = arguments[endpoint]
        self.request_id += 1
        payload = ",".join([str(self.request_id), action] + [str(values[n]) for n in names])
        packet = control_packet(payload)
        try:
            if self.port.write(packet) != len(packet):
                raise ControlError("Incomplete serial control write")
            deadline = time.monotonic() + self.timeout
            while time.monotonic() < deadline:
                self.buffer.extend(self.port.read(512))
                while len(self.buffer) >= 8:
                    start = self.buffer.find(b"AVR1")
                    if start < 0:
                        del self.buffer[:-3]
                        break
                    del self.buffer[:start]
                    if len(self.buffer) < 8:
                        break
                    length = struct.unpack("<I", self.buffer[4:8])[0]
                    if not 1 <= length <= 512:
                        del self.buffer[0]
                        continue
                    if len(self.buffer) < length + 8:
                        break
                    data = bytes(self.buffer[8:8+length])
                    del self.buffer[:8+length]
                    reply = json.loads(data)
                    if not isinstance(reply, dict) or reply.get("request_id") != self.request_id:
                        continue
                    status = reply.get("status")
                    if status == 409:
                        raise ControlError("Control session ended or the phone took over", 409)
                    if status not in (200, 204):
                        raise ControlError(f"ESP32 rejected serial control ({status})", status if status == 400 else 503)
                    return reply
        except (OSError, ValueError) as error:
            raise ControlError("Serial control connection failed") from error
        raise ControlError("ESP32 serial control reply timed out")

    def relay_camera(self, frame):
        """Small optional phone previews fit between the control heartbeats."""
        if time.monotonic() - self.last_relay < 1.0:
            return
        import cv2

        image = cv2.resize(frame, (96, 72))
        for quality in (15, 10):
            success, encoded = cv2.imencode(".jpg", image, [cv2.IMWRITE_JPEG_QUALITY, quality])
            if success and len(encoded) <= 1200:
                packet = b"AVF1" + struct.pack("<I", len(encoded)) + encoded.tobytes()
                if self.port.write(packet) != len(packet):
                    raise ControlError("Incomplete phone preview write")
                self.last_relay = time.monotonic()
                break

    def close(self):
        self.port.close()
