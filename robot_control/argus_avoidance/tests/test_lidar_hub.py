"""Map framing and USB failure isolation without opening hardware ports."""

import math
from pathlib import Path
import struct
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from argus_avoidance.c1 import Sweep
from argus_avoidance.lidar_hub import LidarHub, MAP_MAGIC, map_frame


class Clock:
    def __init__(self, now=1.0):
        self.now = now

    def __call__(self):
        return self.now


class Reader:
    def __init__(self, port):
        self.port = port
        self.latest = None
        self.error = None
        self.started = False
        self.closed = False

    def start(self):
        self.started = True
        return self

    def close(self):
        self.closed = True


class SerialPort:
    def __init__(self, *, fail_open=False, short_write=False, **kwargs):
        self.settings = kwargs
        self.fail_open = fail_open
        self.short_write = short_write
        self.dtr = self.rts = True
        self.port = None
        self.opened_with = None
        self.closed = False
        self.packets = []

    def open(self):
        self.opened_with = (self.port, self.dtr, self.rts)
        if self.fail_open:
            raise OSError("ESP USB unavailable")

    def write(self, packet):
        self.packets.append(bytes(packet))
        return len(packet) - 1 if self.short_write else len(packet)

    def close(self):
        self.closed = True


class SerialFactory:
    def __init__(self, fail_first=False, short_first=False):
        self.ports = []
        self.fail_first = fail_first
        self.short_first = short_first

    def __call__(self, **kwargs):
        port = SerialPort(fail_open=self.fail_first and not self.ports,
                          short_write=self.short_first and not self.ports,
                          **kwargs)
        self.ports.append(port)
        return port


def sweep(sequence, started, ranges=None):
    return Sweep(sequence, started, started + 0.05,
                 tuple(ranges if ranges is not None else [2.0] * 72), 450)


class LidarHubTests(unittest.TestCase):
    def hub(self, clock=None, serial_factory=None):
        clock = clock or Clock()
        factory = serial_factory or SerialFactory()
        hub = LidarHub("c1", "esp", reader_factory=Reader,
                       serial_factory=factory, clock=clock).start()
        return hub, clock, factory

    def test_frame_rotates_raw_bins_and_preserves_unknown(self):
        ranges = [math.nan] * 72
        ranges[18] = 1.00  # C1 raw 90 degrees is robot-forward.
        ranges[36] = 2.00  # 180 degrees becomes robot-right.
        ranges[0] = 0.50   # 0 degrees becomes robot-left.
        ranges[19] = math.inf
        ranges[20] = 20.0  # Out-of-range input cannot exceed protocol maximum.
        packet = map_frame(sweep(1, 1.0, ranges), front_deg=90)
        self.assertEqual(packet[:4], MAP_MAGIC)
        self.assertEqual(struct.unpack("<I", packet[4:8])[0], 72)
        self.assertEqual(len(packet), 80)
        self.assertEqual(packet[8], 20)
        self.assertEqual(packet[8 + 18], 40)
        self.assertEqual(packet[8 + 54], 10)
        self.assertEqual(packet[8 + 1], 0)
        self.assertEqual(packet[8 + 2], 240)
        self.assertEqual(sum(value != 0 for value in packet[8:]), 4)

    def test_preopen_map_usb_before_control_handshake(self):
        hub, _, serial_factory = self.hub()
        self.assertTrue(hub.open_map_port())
        self.assertTrue(hub.open_map_port())
        self.assertEqual(len(serial_factory.ports), 1)
        self.assertEqual(serial_factory.ports[0].opened_with, ("esp", False, False))
        self.assertEqual(serial_factory.ports[0].packets, [])
        hub._reader.latest = sweep(1, 0.9)
        self.assertTrue(hub.relay_once())
        self.assertEqual(len(serial_factory.ports), 1)
        hub.close()

    def test_relay_only_new_fresh_scans_at_most_four_per_second(self):
        hub, clock, serial_factory = self.hub()
        self.assertTrue(hub._reader.started)
        hub._reader.latest = sweep(1, 0.9)
        self.assertTrue(hub.relay_once())
        self.assertFalse(hub.relay_once())  # Same revolution is never resent.
        clock.now = 1.2
        hub._reader.latest = sweep(2, 1.15)
        self.assertFalse(hub.relay_once())  # Rate limit.
        clock.now = 1.25
        self.assertTrue(hub.relay_once())
        self.assertEqual(len(serial_factory.ports), 1)
        self.assertEqual(len(serial_factory.ports[0].packets), 2)
        self.assertEqual(serial_factory.ports[0].opened_with, ("esp", False, False))
        clock.now = 2.5
        hub._reader.latest = sweep(3, 1.7)
        self.assertFalse(hub.relay_once())  # Old scan does not get relayed.
        hub.close()
        self.assertTrue(serial_factory.ports[0].closed)

    def test_usb_failure_does_not_fault_c1_and_retries_later(self):
        serial_factory = SerialFactory(fail_first=True)
        hub, clock, _ = self.hub(serial_factory=serial_factory)
        hub._reader.latest = sweep(1, 0.9)
        self.assertFalse(hub.relay_once())
        self.assertEqual(hub.error, None)
        self.assertIs(hub.latest, hub._reader.latest)
        self.assertIn("ESP USB unavailable", hub.map_error)
        clock.now = 2.0
        hub._reader.latest = sweep(2, 1.9)
        self.assertFalse(hub.relay_once())
        self.assertEqual(len(serial_factory.ports), 1)
        clock.now = 3.1
        hub._reader.latest = sweep(3, 3.0)
        self.assertTrue(hub.relay_once())
        self.assertEqual(hub.map_error, None)
        self.assertEqual(len(serial_factory.ports), 2)
        hub._reader.error = "C1 link lost"
        clock.now = 3.7
        hub._reader.latest = sweep(4, 3.6)
        self.assertFalse(hub.relay_once())
        self.assertEqual(hub.error, "C1 link lost")
        self.assertEqual(len(serial_factory.ports[1].packets), 1)
        hub.close()

    def test_short_usb_write_is_display_fault_only(self):
        serial_factory = SerialFactory(short_first=True)
        hub, _, _ = self.hub(serial_factory=serial_factory)
        hub._reader.latest = sweep(1, 0.9)
        self.assertFalse(hub.relay_once())
        self.assertIn("Incomplete ESP32 map write", hub.map_error)
        self.assertIsNone(hub.error)
        self.assertTrue(serial_factory.ports[0].closed)
        hub.close()


if __name__ == "__main__":
    unittest.main()
