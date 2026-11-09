"""Behavior and fail-closed checks; standard library only."""

from dataclasses import replace
import math
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from argus_avoidance.core import AvoidanceController, Config, Scan


def scan(at=0.0, obstacles=(), fill=4.0, **kwargs):
    ranges = [fill] * 720
    for angle, distance in obstacles:
        index = round((angle + math.pi) / math.tau * 720) % 720
        ranges[index] = distance
    return Scan(tuple(ranges), -math.pi, math.tau / 720, 0.05, 12.0, at, **kwargs)


class ControllerTests(unittest.TestCase):
    def ready(self, obstacles=(), config=None):
        controller = AvoidanceController(config)
        controller.observe(scan(0.0, obstacles))
        self.assertTrue(controller.arm(0)[0])
        for now in (0.1, 0.2, 0.3):
            controller.observe(scan(now, obstacles))
            decision = controller.step(now)
        return controller, decision

    def test_starts_disarmed_and_no_scan_cannot_arm(self):
        controller = AvoidanceController()
        self.assertFalse(controller.arm(0)[0])
        self.assertEqual(controller.step(0).linear, 0)

    def test_clear_forward_crawl(self):
        _, decision = self.ready()
        self.assertEqual(decision.state, "FORWARD")
        self.assertEqual(decision.linear, 0.05)

    def test_clearance_uses_entire_width(self):
        # A thin object off the centerline but in the inflated chassis corridor.
        _, decision = self.ready(((math.atan2(0.20, 0.70), math.hypot(0.20, 0.70)),))
        self.assertEqual(decision.state, "SLOW")
        self.assertEqual(decision.linear, 0.025)

    def test_stop_then_turn_without_reverse(self):
        controller, _ = self.ready()
        controller.observe(scan(0.4, ((0, 0.5),)))
        decision = controller.step(0.4)
        self.assertEqual((decision.state, decision.linear, decision.angular), ("STOP", 0, 0))
        controller.observe(scan(0.7, ((0, 0.5),)))
        decision = controller.step(0.7)
        self.assertEqual(decision.state, "TURN")
        self.assertEqual(decision.linear, 0)
        self.assertGreater(decision.angular, 0)

    def test_chooses_clearer_right_side(self):
        _, decision = self.ready(((0, 0.5), (math.pi / 2, 0.45)))
        self.assertEqual(decision.state, "TURN")
        self.assertLess(decision.angular, 0)

    def test_trapped_remains_stopped_until_rearmed(self):
        controller, decision = self.ready(((0, 0.5), (math.pi / 2, 0.45), (-math.pi / 2, 0.45)))
        self.assertEqual(decision.state, "BLOCKED")
        controller.observe(scan(0.4))
        self.assertEqual(controller.step(0.4).linear, 0)
        self.assertFalse(controller.armed)

    def test_sweep_checks_rear_obstacle_too(self):
        _, decision = self.ready(((math.pi, 0.24),))
        self.assertEqual(decision.state, "BLOCKED")
        self.assertEqual(decision.angular, 0)

    def test_scan_dropout_latches_and_does_not_auto_resume(self):
        controller, _ = self.ready()
        decision = controller.step(0.81)
        self.assertEqual(decision.state, "FAULT")
        self.assertEqual((decision.linear, decision.angular), (0, 0))
        controller.observe(scan(0.9))
        self.assertEqual(controller.step(0.9).state, "FAULT")
        self.assertTrue(controller.arm(0.9)[0])

    def test_unknown_and_infinity_not_clear_by_default(self):
        for fill in (math.inf, math.nan, 0, -math.inf):
            controller = AvoidanceController()
            controller.observe(scan(fill=fill))
            self.assertFalse(controller.arm(0)[0], repr(fill))

    def test_documented_infinite_no_returns_can_be_enabled(self):
        controller = AvoidanceController(Config(no_return_is_clear=True))
        controller.observe(scan(fill=math.inf))
        self.assertTrue(controller.arm(0)[0])

    def test_contiguous_unknown_sector_blocks_even_with_high_overall_coverage(self):
        controller = AvoidanceController()
        reading = scan()
        values = list(reading.ranges)
        values[300:320] = [math.nan] * 20
        controller.observe(replace(reading, ranges=tuple(values)))
        self.assertFalse(controller.arm(0)[0])

    def test_unknown_gap_across_full_scan_boundary_is_detected(self):
        controller = AvoidanceController()
        reading = scan()
        values = list(reading.ranges)
        values[:10] = [math.nan] * 10
        values[-10:] = [math.nan] * 10
        controller.observe(replace(reading, ranges=tuple(values)))
        self.assertFalse(controller.arm(0)[0])

    def test_small_unknown_forward_cone_cannot_hide_a_chair_leg(self):
        controller = AvoidanceController()
        reading = scan()
        values = list(reading.ranges)
        values[355:366] = [math.nan] * 11
        controller.observe(replace(reading, ranges=tuple(values)))
        self.assertFalse(controller.arm(0)[0])

    def test_even_one_unknown_ray_stops_an_armed_controller(self):
        controller, _ = self.ready()
        reading = scan(0.4)
        values = list(reading.ranges)
        values[540] = 0.0
        controller.observe(replace(reading, ranges=tuple(values)))
        decision = controller.step(0.4)
        self.assertEqual((decision.state, decision.linear, decision.angular), ("FAULT", 0, 0))

    def test_partial_scan_refuses_rotation(self):
        controller = AvoidanceController()
        controller.observe(replace(scan(), angle_increment=math.pi / 720))
        self.assertFalse(controller.arm(0)[0])

    def test_sensor_translation_changes_body_relative_clearance(self):
        controller = AvoidanceController()
        controller.observe(scan(obstacles=((0, 0.6),), sensor_x=0.1))
        self.assertAlmostEqual(controller.step(0).front_clearance, 0.45)

    def test_sensor_yaw_is_applied(self):
        controller = AvoidanceController()
        controller.observe(scan(obstacles=((math.pi, 0.5),), sensor_yaw=math.pi))
        self.assertAlmostEqual(controller.step(0).front_clearance, 0.25)

    def test_short_sensor_range_cannot_prove_path_clear(self):
        controller = AvoidanceController()
        controller.observe(replace(scan(fill=0.7), range_max=0.8))
        self.assertFalse(controller.arm(0)[0])

    def test_repeated_timer_ticks_do_not_count_as_distinct_clear_scans(self):
        controller = AvoidanceController()
        controller.observe(scan())
        controller.arm(0)
        for now in (0.1, 0.2, 0.3, 0.4):
            self.assertEqual(controller.step(now).linear, 0)

    def test_duplicate_scan_receipt_does_not_count_or_refresh(self):
        controller = AvoidanceController()
        reading = scan()
        controller.observe(reading)
        controller.arm(0)
        for now in (0.1, 0.2, 0.3):
            controller.observe(reading)
            self.assertEqual(controller.step(now).linear, 0)
        self.assertEqual(controller.step(0.6).state, "FAULT")

    def test_future_and_backwards_clocks_fail_closed(self):
        controller = AvoidanceController()
        controller.observe(scan(1))
        self.assertFalse(controller.arm(0)[0])
        controller, _ = self.ready()
        self.assertEqual(controller.step(0.29).state, "FAULT")

    def test_nonfinite_metadata_fails_closed(self):
        controller = AvoidanceController()
        controller.observe(replace(scan(), sensor_yaw=math.nan))
        self.assertFalse(controller.arm(0)[0])

    def test_direction_stays_latched(self):
        controller, decision = self.ready(((0, 0.5),))
        self.assertGreater(decision.angular, 0)
        # Now the opposite side looks better, but the existing rotation is safe.
        controller.observe(scan(0.4, ((0, 0.5), (math.pi / 2, 0.75))))
        self.assertGreater(controller.step(0.4).angular, 0)

    def test_clear_scans_and_settling_required_before_resuming(self):
        controller, _ = self.ready(((0, 0.5),))
        for now in (0.4, 0.5):
            controller.observe(scan(now))
            self.assertEqual(controller.step(now).state, "TURN")
        controller.observe(scan(0.6))
        self.assertEqual(controller.step(0.6).state, "STOP")
        controller.observe(scan(0.9))
        self.assertEqual(controller.step(0.9).state, "FORWARD")

    def test_turn_timeout_latches_blocked(self):
        controller, _ = self.ready(((0, 0.5),), Config(turn_timeout_s=0.5))
        controller.observe(scan(0.9, ((0, 0.5),)))
        self.assertEqual(controller.step(0.9).state, "BLOCKED")
        self.assertFalse(controller.armed)

    def test_invalid_configuration_is_rejected(self):
        for kwargs in ({"robot_radius_m": 0}, {"clear_scans": 2.5},
                       {"scan_timeout_s": math.inf}, {"no_return_is_clear": 1},
                       {"stop_clearance_m": 0.7}, {"slow_m_s": 0.1}):
            with self.assertRaises(ValueError, msg=repr(kwargs)):
                Config(**kwargs)


if __name__ == "__main__":
    unittest.main()
