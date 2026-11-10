"""Exercise the real HTTP control client against a local test server."""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import math
from pathlib import Path
import sys
import threading
import time
import unittest
from unittest import mock
import urllib.parse

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from argus_avoidance.follow import ControlError, ESP32AutoClient, wheel_percentages
from argus_avoidance import follow, line_preview


class TestServer(BaseHTTPRequestHandler):
    def log_message(self, *_):
        pass

    def do_GET(self):
        self.server.requests.append((self.path, {}))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'{"mode":"stopped","epoch":1}')

    def do_POST(self):
        data = self.rfile.read(int(self.headers.get("Content-Length", "0"))).decode()
        values = {k: v[0] for k, v in urllib.parse.parse_qs(data).items()}
        self.server.requests.append((self.path, values))
        if self.server.manual and self.path in ("/auto/drive", "/auto/stop"):
            self.send_response(409)
            self.end_headers()
            return
        self.send_response(200 if self.path == "/auto/arm" else 204)
        self.end_headers()
        if self.path == "/auto/arm":
            result = {"mode": "auto", "session": "1234567890abcdef", "lease_ms": 350,
                      "max_auto_percent": self.server.cap}
            self.wfile.write(json.dumps(result).encode())
            if getattr(self.server, "takeover_after_arm", False):
                self.server.manual = True


class FollowClientTests(unittest.TestCase):
    def setUp(self):
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), TestServer)
        self.server.requests, self.server.manual, self.server.cap = [], False, 35
        self.worker = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.worker.start()
        self.client = ESP32AutoClient(f"http://127.0.0.1:{self.server.server_port}", timeout=1)

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.worker.join()

    def test_explicit_arm_drive_sequence_and_scoped_stop(self):
        with self.assertRaises(ControlError):
            self.client.drive(6, 6)
        self.client.arm()
        self.client.drive(6, 6)
        self.client.drive(8, 4)
        self.client.stop()
        self.assertEqual([p for p, _ in self.server.requests],
                         ["/state", "/auto/arm", "/auto/drive", "/auto/drive", "/auto/stop"])
        self.assertEqual(self.server.requests[2][1]["seq"], "1")
        self.assertEqual(self.server.requests[3][1]["seq"], "2")
        self.assertIsNone(self.client.session)

    def test_manual_override_ends_auto_and_cleanup_is_scoped(self):
        self.client.arm()
        self.server.manual = True
        with self.assertRaises(ControlError):
            self.client.drive(6, 6)
        self.client.stop()
        self.assertNotIn("/stop", [p for p, _ in self.server.requests])

    def test_phone_start_preserves_captured_epoch(self):
        self.client.arm(expected_epoch=42)
        self.assertEqual(self.server.requests, [("/auto/arm", {"epoch": "42"})])
        self.client.stop()

    def test_invalid_captured_epoch_never_arms(self):
        for epoch in (True, -1, 2**32, "1"):
            with self.subTest(epoch=epoch), self.assertRaises(ControlError):
                self.client.arm(expected_epoch=epoch)
        self.assertEqual(self.server.requests, [])

    def test_mismatched_profile_refuses_drive(self):
        self.server.cap = 30
        try:
            with self.assertRaises(ControlError):
                self.client.arm()
        finally:
            self.client.stop()
        self.assertNotIn("/auto/drive", [p for p, _ in self.server.requests])

    def run_follow(self, decisions, fresh=True, drive=True, seconds=0.6,
                   fail_after=None, read_delay=0, expected_epoch=None):
        class Reader:
            calls = 0

            def read(self, timeout):
                self.calls += 1
                if read_delay:
                    time.sleep(read_delay)
                if fail_after is not None and self.calls > fail_after:
                    raise OSError("Test camera disconnected")
                return object()

            def is_fresh(self):
                return fresh

        values = iter(decisions)
        last = decisions[-1]

        def decide(*_):
            return next(values, last)

        args = ["--seconds", str(seconds), "--esp32", self.client.address]
        if drive:
            args.append("--drive")
        if expected_epoch is not None:
            args += ["--expected-epoch", str(expected_epoch)]
        with mock.patch.object(line_preview, "SnapshotReader", Reader), \
             mock.patch.object(line_preview, "decide_tape", side_effect=decide), \
             mock.patch.object(line_preview, "print_decision"), \
             mock.patch("builtins.print"):
            return follow.main(args)

    def test_follower_uses_phone_request_epoch_for_arm(self):
        clear = line_preview.TapeDecision("FORWARD", "test", 0, 320, 1)
        self.assertEqual(self.run_follow([clear], expected_epoch=42), 0)
        self.assertEqual(self.server.requests[0], ("/auto/arm", {"epoch": "42"}))

    def test_normal_entrypoint_tape_loss_stops_own_session(self):
        clear = line_preview.TapeDecision("FORWARD", "test", 0, 320, 1)
        lost = line_preview.TapeDecision("STOP", "test tape lost")
        self.assertEqual(self.run_follow([clear] * 4 + [lost]), 1)
        paths = [p for p, _ in self.server.requests]
        self.assertEqual(paths, ["/state", "/auto/arm", "/auto/drive", "/auto/stop"])

    def test_normal_entrypoint_requires_clear_fresh_frames(self):
        for fresh, decision in (
            (True, line_preview.TapeDecision("STOP", "no line")),
            (False, line_preview.TapeDecision("FORWARD", "test", 0, 320, 1)),
        ):
            self.assertEqual(self.run_follow([decision], fresh=fresh, seconds=0.25), 1)
        self.assertEqual(self.server.requests, [])

    def test_default_entrypoint_only_calls_preview(self):
        with mock.patch.object(line_preview, "main", return_value=0) as preview:
            self.assertEqual(follow.main(["--seconds", "1"]), 0)
        preview.assert_called_once_with(["--tape", "black", "--seconds", "1.0"])
        self.assertEqual(self.server.requests, [])

    def test_camera_failure_after_arm_uses_scoped_stop(self):
        clear = line_preview.TapeDecision("FORWARD", "test", 0, 320, 1)
        self.assertEqual(self.run_follow([clear], fail_after=3), 1)
        self.assertEqual([p for p, _ in self.server.requests],
                         ["/state", "/auto/arm", "/auto/stop"])

    def test_manual_takeover_ends_entrypoint_without_global_stop(self):
        self.server.takeover_after_arm = True
        clear = line_preview.TapeDecision("FORWARD", "test", 0, 320, 1)
        self.assertEqual(self.run_follow([clear]), 1)
        paths = [p for p, _ in self.server.requests]
        self.assertIn("/auto/drive", paths)
        self.assertEqual(paths[-1], "/auto/stop")
        self.assertNotIn("/stop", paths)

    def test_run_deadline_prevents_late_arm_or_drive(self):
        clear = line_preview.TapeDecision("FORWARD", "test", 0, 320, 1)
        self.assertEqual(self.run_follow([clear], seconds=.15), 1)
        self.assertEqual(self.run_follow([clear], seconds=.05, read_delay=.1), 1)
        self.assertEqual(self.server.requests, [])

    def test_wheel_percentages_and_invalid_inputs(self):
        self.assertEqual(wheel_percentages(0), (25, 25))
        self.assertEqual(wheel_percentages(-1), (0, 25))
        self.assertEqual(wheel_percentages(1), (25, 0))
        for error in (math.nan, math.inf, 2):
            with self.assertRaises(ValueError):
                wheel_percentages(error)
        for pair in ((-1, 6), (36, 0), (True, 6)):
            self.client.session = "1234567890abcdef"
            with self.assertRaises(ValueError):
                self.client.drive(*pair)

    def test_small_visible_tape_error_produces_a_real_correction(self):
        self.assertEqual(wheel_percentages(-0.11), (24, 26))
        self.assertEqual(wheel_percentages(0.11), (26, 24))
        self.assertEqual(wheel_percentages(0.09), (25, 25))

    def test_large_offsets_reduce_forward_travel_and_tighten_turn(self):
        previous_ratio = 0.0
        previous_sum = 50
        for i in range(36, 101):
            error = i / 100
            left, right = wheel_percentages(error)
            self.assertEqual((right, left), wheel_percentages(-error))
            self.assertTrue(0 <= right <= left <= 35)
            self.assertLessEqual(left + right, previous_sum)
            ratio = (left - right) / (left + right)
            self.assertGreaterEqual(ratio, previous_ratio)
            previous_ratio, previous_sum = ratio, left + right
        self.assertEqual(wheel_percentages(0.71), (25, 0))


if __name__ == "__main__":
    unittest.main()
