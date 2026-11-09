"""Serial-worker heartbeat and shutdown checks with an in-memory Mega."""

from pathlib import Path
import sys
import threading
import time
import unittest

repo = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo / "ros2/src/vacuum_hardware"))
from vacuum_hardware.protocol import frame
from vacuum_hardware.serial_link import SerialLink


class FakeMega:
    def __init__(self):
        self.lock = threading.Lock()
        self.buffer = b""
        self.commands = []
        self.closed = False

    def write(self, packet):
        fields = packet.decode().strip().split(",")
        with self.lock:
            self.commands.append(fields)
            self.buffer += frame(f"S1,{fields[1]},{fields[2]},0,0,0")
        return len(packet)

    @property
    def in_waiting(self):
        with self.lock:
            return len(self.buffer)

    def read(self, size):
        with self.lock:
            data = self.buffer[:size]
            self.buffer = self.buffer[size:]
            return data

    def close(self):
        self.closed = True


class LinkTests(unittest.TestCase):
    def test_heartbeat_and_shutdown(self):
        mega = FakeMega()
        link = SerialLink("fake", factory=lambda: mega)
        try:
            for _ in range(30):
                if link.snapshot()[1]:
                    break
                time.sleep(0.01)
            self.assertIsNotNone(link.snapshot()[1])
            link.update(True, 300, -400)
            time.sleep(0.08)
            self.assertTrue(any(c[2:5] == ["1", "300", "-400"] for c in mega.commands))
            time.sleep(0.25)
            self.assertEqual(mega.commands[-1][2:5], ["0", "0", "0"])
        finally:
            link.close()
        self.assertTrue(mega.closed)
        self.assertFalse(link.thread.is_alive())


if __name__ == "__main__":
    unittest.main()
