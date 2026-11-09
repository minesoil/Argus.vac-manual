"""Wire corruption, wheel scaling and USB count rollover tests."""

from pathlib import Path
import sys
import unittest

repo = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo / "ros2/src/vacuum_hardware"))
from vacuum_hardware.protocol import (
    command,
    crc16,
    frame,
    parse_status,
    wheel_rates,
    count_delta,
)


class ProtocolTests(unittest.TestCase):
    def test_known_crc(self):
        self.assertEqual(crc16(b"123456789"), 0x29B1)

    def test_signed_status(self):
        status = parse_status(frame("S1,65535,1,0,-100,200"))
        self.assertTrue(status.armed)
        self.assertEqual(status.left_steps, -100)

    def test_bad_frames(self):
        for value in (
            b"S1,1,1,0,0,0,0000",
            frame("S1,1,9,0,0,0"),
            b"garbage",
            frame("S1,1,1,0,2147483648,0"),
        ):
            with self.assertRaises((ValueError, UnicodeError)):
                parse_status(value)

    def test_velocity_and_limit(self):
        left, right = wheel_rates(0.15, 0, 0.035, 0.22, 1600)
        self.assertEqual(left, right)
        self.assertAlmostEqual(left, 1091, delta=1)
        left, right = wheel_rates(2, 5, 0.035, 0.22, 1600, max_rate=1000)
        self.assertLessEqual(max(abs(left), abs(right)), 1000)
        self.assertGreater(right, left)
        with self.assertRaises(ValueError):
            wheel_rates(float("nan"), 0, 0.035, 0.22, 1600)

    def test_command_cap(self):
        self.assertTrue(command(1, False, 0, 0).startswith(b"V1,1,0,0,0,"))
        with self.assertRaises(ValueError):
            command(1, True, 16001, 0)

    def test_counter_rollover(self):
        self.assertEqual(count_delta(-2147483648, 2147483647), 1)


if __name__ == "__main__":
    unittest.main()
