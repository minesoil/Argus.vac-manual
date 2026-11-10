"""USB control framing and reply matching without touching a serial port."""

import json
from pathlib import Path
import struct
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from argus_avoidance.follow import ControlError
from argus_avoidance.serial_control import CONTROL_MAGIC, SerialAutoClient, control_packet


class FakePort:
    def __init__(self):
        self.received = []
        self.incoming = bytearray()
        self.respond = True
        self.status = 200
        self.noise = True

    def write(self, packet):
        length = (packet[4] & 127) | ((packet[5] & 127) << 7)
        text = bytes(b & 127 for b in packet[6:]).decode()
        assert length == len(text)
        self.received.append(text)
        request_id = int(text.split(",")[0])
        if self.respond:
            data = json.dumps({"request_id": request_id, "status": self.status}).encode()
            self.incoming.extend(b"boot noise" if self.noise else b"")
            self.incoming.extend(b"AVR1" + struct.pack("<I", len(data)) + data)
        return len(packet)

    def read(self, size):
        piece = bytes(self.incoming[:3])
        del self.incoming[:3]
        return piece


class SerialControlTests(unittest.TestCase):
    def client(self):
        obj = SerialAutoClient.__new__(SerialAutoClient)
        obj.port = FakePort()
        obj.timeout = 0.03
        obj.buffer = bytearray()
        obj.request_id = 0
        obj.session = None
        return obj

    def test_probe_bytes_cannot_contain_legacy_mega_ascii_commands(self):
        text = "1,state"
        packet = control_packet(text)
        self.assertEqual(packet[:4], CONTROL_MAGIC)
        self.assertTrue(all(byte >= 128 for byte in packet))
        self.assertEqual(bytes(b & 127 for b in packet[6:]).decode(), text)
        for payload in ("", "x" * 161, "\u00e9"):
            with self.assertRaises(ValueError):
                control_packet(payload)

    def test_fragmented_reply_and_boot_noise(self):
        client = self.client()
        self.assertEqual(client.request("/state")["request_id"], 1)
        self.assertEqual(client.request("/auto/arm", {"epoch": 9})["status"], 200)
        self.assertEqual(client.port.received, ["1,state", "2,arm,9"])

    def test_wrong_reply_id_is_ignored(self):
        client = self.client()
        wrong = json.dumps({"request_id": 99, "status": 200}).encode()
        client.port.incoming.extend(b"AVR1" + struct.pack("<I", len(wrong)) + wrong)
        self.assertEqual(client.request("/state")["request_id"], 1)

    def test_expired_session_and_missing_reply_fail(self):
        client = self.client()
        client.port.status = 409
        with self.assertRaises(ControlError):
            client.request("/auto/stop", {"session": "1234567890abcdef"})
        client = self.client()
        client.port.respond = False
        with self.assertRaises(ControlError):
            client.request("/state")

    def test_drive_fields_and_scoped_cleanup(self):
        client = self.client()
        client.session = "1234567890abcdef"
        client.sequence = 0
        client.port.status = 204
        client.drive(6, 6)
        client.port.status = 200
        client.stop()
        self.assertEqual(client.port.received,
                         ["1,drive,1234567890abcdef,1,6,6", "2,stop,1234567890abcdef"])
        self.assertIsNone(client.session)


if __name__ == "__main__":
    unittest.main()
