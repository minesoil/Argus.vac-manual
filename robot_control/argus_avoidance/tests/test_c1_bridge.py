"""The roaming reader consumes only fresh, complete bridge sweeps."""

import io
import json
import math
from pathlib import Path
import sys
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from argus_avoidance.c1_bridge import BridgeC1Reader


class BridgeC1Tests(unittest.TestCase):
    def read(self, payload):
        body = io.BytesIO(json.dumps(payload).encode())
        with mock.patch("urllib.request.urlopen", return_value=body):
            return BridgeC1Reader().latest

    def test_missing_scan_waits_and_unknown_bins_remain_unknown(self):
        self.assertIsNone(self.read({"sweep": None}))
        ranges = [2.0] * 72
        ranges[3] = None
        sweep = self.read({"sweep": {"sequence": 7, "started": 10.0,
                                     "finished": 10.1, "nodes": 500, "ranges": ranges}})
        self.assertEqual((sweep.sequence, sweep.started, sweep.nodes), (7, 10.0, 500))
        self.assertTrue(math.isnan(sweep.ranges[3]))

    def test_invalid_or_unavailable_bridge_fails_closed(self):
        with self.assertRaises(OSError):
            self.read({"sweep": {"sequence": 1, "started": 0,
                                 "finished": 0.1, "nodes": 1, "ranges": [1.0]}})
        with mock.patch("urllib.request.urlopen", side_effect=OSError("gone")):
            with self.assertRaises(OSError):
                _ = BridgeC1Reader().latest


if __name__ == "__main__":
    unittest.main()
