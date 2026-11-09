"""Stationary camera checks with synthetic floor scenes."""

from pathlib import Path
import itertools
import math
import sys
from types import SimpleNamespace
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from argus_avoidance import line_preview

cv2, np = line_preview.cv2, line_preview.np


def camera_headers(grab=10.0, sent=10.02, online="true"):
    return {"X-UStreamer-Online": online, "X-UStreamer-Grab-Timestamp": str(grab),
            "X-UStreamer-Send-Timestamp": str(sent)}


class CameraFreshnessTests(unittest.TestCase):
    def test_fresh_capture_uses_source_clock(self):
        self.assertEqual(line_preview.check_snapshot_headers(camera_headers(), 10.05), 10.0)

    def test_frozen_and_out_of_order_capture_rejected(self):
        for previous in (10.0, 10.01):
            with self.assertRaisesRegex(ValueError, "cached"):
                line_preview.check_snapshot_headers(camera_headers(), 10.05, previous)

    def test_missing_and_offline_metadata_rejected(self):
        for headers in ({}, camera_headers(online="false"), {"X-UStreamer-Online": "true"}):
            with self.assertRaises(ValueError):
                line_preview.check_snapshot_headers(headers, 10.05)

    def test_old_future_and_inconsistent_timestamps_rejected(self):
        examples = ((camera_headers(), 10.30), (camera_headers(), 9.90),
                    (camera_headers(sent=10.30), 10.31), (camera_headers(sent=9.99), 10.05))
        for headers, now in examples:
            with self.subTest(headers=headers, now=now), self.assertRaises(ValueError):
                line_preview.check_snapshot_headers(headers, now)

    def test_nonfinite_capture_metadata_rejected(self):
        for value in (math.nan, math.inf, -math.inf):
            with self.assertRaises(ValueError):
                line_preview.check_snapshot_headers(camera_headers(grab=value), 10.05)

    def test_remote_url_has_no_same_clock_freshness_contract(self):
        with self.assertRaisesRegex(ValueError, "loopback"):
            line_preview.SnapshotReader("http://192.168.1.20:8080/snapshot")

    def test_failed_read_invalidates_previously_fresh_capture(self):
        reader = line_preview.SnapshotReader()
        reader.last_grab, reader.capture_ok = 10.0, True
        with mock.patch.object(line_preview, "cv2", object()), mock.patch.object(line_preview, "np", object()), \
                mock.patch.object(line_preview, "raw_clock", return_value=10.05), \
                mock.patch.object(line_preview.urllib.request, "urlopen", side_effect=OSError("offline")):
            with self.assertRaises(OSError):
                reader.read()
            self.assertFalse(reader.is_fresh())

    def test_last_accepted_capture_expires_without_another_request(self):
        reader = line_preview.SnapshotReader()
        reader.last_grab, reader.capture_ok = 10.0, True
        with mock.patch.object(line_preview, "raw_clock", return_value=10.05):
            self.assertTrue(reader.is_fresh())
        with mock.patch.object(line_preview, "raw_clock", return_value=10.30):
            self.assertFalse(reader.is_fresh())


class LivePreviewHealthTests(unittest.TestCase):
    def run_fake_preview(self, fail_after_first=False):
        decisions = []
        camera = mock.Mock()
        camera.is_fresh.return_value = True
        captures = 0

        def read(timeout):
            nonlocal captures
            captures += 1
            if fail_after_first and captures > 1:
                raise OSError("camera offline")
            return object()

        camera.read.side_effect = read
        ticks = iter(value * .05 for value in itertools.count())
        with mock.patch.object(line_preview, "cv2", SimpleNamespace(error=ValueError)), \
                mock.patch.object(line_preview, "np", object()), \
                mock.patch.object(line_preview, "SnapshotReader", return_value=camera), \
                mock.patch.object(line_preview, "decide_tape", return_value=line_preview.stop("No tape found")), \
                mock.patch.object(line_preview, "print_decision", side_effect=decisions.append), \
                mock.patch.object(line_preview.time, "monotonic", side_effect=lambda: next(ticks)), \
                mock.patch.object(line_preview.time, "sleep"):
            result = line_preview.main(["--seconds", "0.6"])
        return result, decisions

    def test_success_then_camera_loss_finishes_with_fault(self):
        result, decisions = self.run_fake_preview(fail_after_first=True)
        self.assertEqual(result, 1)
        self.assertEqual(decisions[-1].state, "STOP")
        self.assertIn("camera fault", decisions[-1].reason)
        self.assertIn("camera offline", decisions[-1].reason)

    def test_healthy_camera_with_missing_tape_finishes_normally(self):
        result, decisions = self.run_fake_preview()
        self.assertEqual(result, 0)
        self.assertEqual(decisions[-1].state, "STOP")
        self.assertIn("fresh frames", decisions[-1].reason)


@unittest.skipIf(cv2 is None or np is None, "Camera preview requires OpenCV and NumPy")
class TapePreviewTests(unittest.TestCase):
    def floor(self, value=210):
        return np.full((480, 640, 3), value, np.uint8)

    def stripe(self, image, x, color=(15, 15, 15), thickness=28):
        cv2.line(image, (x, 240), (x, 479), color, thickness)
        return image

    def test_black_tape_left_center_and_right(self):
        for x, state in ((180, "LEFT"), (320, "FORWARD"), (460, "RIGHT")):
            with self.subTest(x=x):
                result = line_preview.decide_tape(self.stripe(self.floor(), x))
                self.assertEqual(result.state, state)
                self.assertGreater(result.confidence, 0.60)
                self.assertAlmostEqual(result.center_x, x, delta=1)

    def test_gentle_bend_follows_lower_part_of_visible_path(self):
        image = self.floor()
        cv2.line(image, (270, 250), (430, 479), (15, 15, 15), 28)
        result = line_preview.decide_tape(image)
        self.assertEqual(result.state, "RIGHT")

    def test_absent_or_low_contrast_tape_stops(self):
        for image in (self.floor(), self.stripe(self.floor(140), 320, (120, 120, 120))):
            self.assertEqual(line_preview.decide_tape(image).state, "STOP")

    def test_parallel_paths_are_ambiguous(self):
        image = self.stripe(self.floor(), 180)
        self.stripe(image, 460)
        result = line_preview.decide_tape(image)
        self.assertEqual(result.state, "STOP")
        self.assertIn("ambiguous", result.reason)

    def test_crossing_paths_are_ambiguous(self):
        image = self.floor()
        cv2.line(image, (200, 245), (440, 479), (15, 15, 15), 24)
        cv2.line(image, (440, 245), (200, 479), (15, 15, 15), 24)
        self.assertEqual(line_preview.decide_tape(image).state, "STOP")

    def test_broad_patch_and_small_blob_stop(self):
        broad = self.floor()
        cv2.rectangle(broad, (100, 260), (540, 479), (15, 15, 15), -1)
        blob = self.floor()
        cv2.circle(blob, (320, 430), 25, (15, 15, 15), -1)
        for image in (broad, blob):
            self.assertEqual(line_preview.decide_tape(image).state, "STOP")

    def test_large_gap_in_line_stops(self):
        image = self.stripe(self.floor(), 320)
        image[340:400] = 210
        self.assertEqual(line_preview.decide_tape(image).state, "STOP")

    def test_shallow_separate_camera_edge_preserves_offset_tape(self):
        image = self.floor()
        image[364:402] = 15
        cv2.line(image, (520, 420), (590, 479), (15, 15, 15), 28)
        result = line_preview.decide_tape(image)
        self.assertEqual(result.state, "RIGHT")
        self.assertGreater(result.confidence, 0.9)

    def test_edge_trim_does_not_hide_a_gap_below_the_edge(self):
        image = self.floor()
        image[364:390] = 15
        cv2.line(image, (320, 400), (320, 479), (15, 15, 15), 28)
        image[424:453] = 210
        self.assertEqual(line_preview.decide_tape(image).state, "STOP")

    def test_connected_crossbar_is_not_cropped_away(self):
        image = self.stripe(self.floor(), 320)
        image[364:390] = 15
        self.assertEqual(line_preview.decide_tape(image).state, "STOP")

    def test_deep_dark_band_does_not_become_a_new_floor(self):
        image = self.floor()
        image[364:435] = 15
        cv2.line(image, (320, 450), (320, 479), (15, 15, 15), 28)
        self.assertEqual(line_preview.decide_tape(image).state, "STOP")

    def test_blue_and_white_tape_are_explicit_options(self):
        blue = self.stripe(self.floor(), 320, (230, 40, 30))
        white = self.stripe(self.floor(25), 320, (235, 235, 235))
        self.assertEqual(line_preview.decide_tape(blue, "blue").state, "FORWARD")
        self.assertEqual(line_preview.decide_tape(white, "white").state, "FORWARD")

    def test_missing_or_malformed_frames_stop(self):
        for frame in (None, np.zeros((40, 50, 3), np.uint8), np.zeros((480, 640), np.uint8)):
            self.assertEqual(line_preview.decide_tape(frame).state, "STOP")

    def test_invalid_tape_name_is_rejected(self):
        with self.assertRaises(ValueError):
            line_preview.decide_tape(self.floor(), "green")


if __name__ == "__main__":
    unittest.main()
