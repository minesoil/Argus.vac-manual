"""Independent geometry and behavior checks for the small standalone simulator."""

import math
import unittest
from dataclasses import replace

from argus_avoidance.roam import navigation_config

from argus_avoidance.simulate import (
    Circle, Segment, World, point_segment_distance, ray_circle, ray_segment,
    run_scenario, scenarios,
)


class GeometryTests(unittest.TestCase):
    def test_finite_wall_hit_and_miss(self):
        wall = Segment(1.0, -0.1, 1.0, 0.1)
        self.assertAlmostEqual(ray_segment(0, 0, 1, 0, wall), 1.0)
        self.assertTrue(math.isinf(ray_segment(0, 0.2, 1, 0, wall)))
        self.assertTrue(math.isinf(ray_segment(0, 0, -1, 0, wall)))

    def test_collinear_wall_and_circle_near_surface(self):
        self.assertAlmostEqual(ray_segment(0, 0, 1, 0, Segment(1, 0, 2, 0)), 1.0)
        self.assertAlmostEqual(ray_circle(0, 0, 1, 0, 1.0, 0, 0.035), 0.965)
        self.assertTrue(math.isinf(ray_circle(0, 0, 0, 1, 1.0, 0, 0.035)))

    def test_body_clearance_includes_circle_radius_and_segment_endpoints(self):
        self.assertAlmostEqual(point_segment_distance(0, 0, Segment(1, 1, 1, 2)), math.sqrt(2))
        world = World(circles=(Circle(1, 0, 0.035),))
        self.assertAlmostEqual(world.clearance(0, 0, 0.22, 0), 0.745)
        self.assertLess(world.clearance(0.8, 0, 0.22, 0), 0)

    def test_lidar_pose_offset_is_applied_to_raycast(self):
        world = World(segments=(Segment(1.0, -2.0, 1.0, 2.0),))
        scan = world.scan(0, 0, 0, 0, sensor_x=0.1, sensor_y=0.05, samples=720)
        self.assertAlmostEqual(scan.ranges[360], 0.9)
        self.assertEqual(scan.sensor_x, 0.1)
        self.assertEqual(scan.sensor_y, 0.05)
        rotated = world.scan(0, 0, 0, 0, sensor_yaw=math.pi / 2, samples=720)
        self.assertAlmostEqual(rotated.ranges[180], 1.0)

    def test_full_unknown_scan_and_explicit_no_return(self):
        clear = World().scan(0, 0, 0, 0)
        unknown = World().scan(0, 0, 0, 0, unknown=True)
        self.assertEqual(len(clear.ranges), 720)
        self.assertTrue(all(x == float("inf") for x in clear.ranges))
        self.assertTrue(all(math.isnan(x) for x in unknown.ranges))

    def test_moving_obstacle_stops_at_configured_time(self):
        obstacle = Circle(1.2, 0.8, 0.08, vy=-0.1, stop_at=8.0)
        self.assertAlmostEqual(obstacle.position(4)[1], 0.4)
        self.assertAlmostEqual(obstacle.position(8)[1], 0.0)
        self.assertEqual(obstacle.position(8), obstacle.position(20))


class ControllerSimulationTests(unittest.TestCase):
    def test_close_wall_trial_finishes_with_a_one_to_two_centimetre_tire_gap(self):
        from argus_avoidance.wall_trial_sim import simulate

        result = simulate(20, track=0.3254, wheel_gain=0.004, seam=0.08,
                          finish_at_wall_end=True, cruise=35, slow=18, close_wall_radius_m=0.1854,
                          start_side_gap=0.063, row_end=0.90)
        self.assertEqual(result["transitions"][-1]["reason"], "Reached end of tracked wall")
        self.assertEqual(result["zero_command_ticks_after_motion"], 0)
        gaps = [frame["axle_tire_edge_gap_m"] for frame in result["trace"]
                if min(frame["wheels"]) > 0]
        self.assertGreaterEqual(min(gaps), 0.010)
        self.assertTrue(all(gap <= 0.020 for gap in gaps[-20:]))
        self.assertEqual(result["peak_wheel_command_percent"], 13)

    def test_close_wall_trial_can_cruise_at_35_and_slow_after_approach(self):
        from argus_avoidance.wall_trial_sim import simulate

        result = simulate(20, track=0.3254, wheel_gain=0.004, seam=0.08,
                          finish_at_wall_end=True, cruise=35, slow=18,
                          close_wall_radius_m=0.1854, start_side_gap=0.18, row_end=0.90)
        self.assertEqual(result["transitions"][-1]["reason"], "Reached end of tracked wall")
        self.assertEqual(result["zero_command_ticks_after_motion"], 0)
        self.assertEqual(result["peak_wheel_command_percent"], 35)
        self.assertTrue(all(max(frame["wheels"]) <= 18 for frame in result["trace"]
                            if frame["at_s"] >= 3))

    def test_reduced_wall_offset_still_crosses_seam_with_wider_track(self):
        from argus_avoidance.wall_trial_sim import simulate

        result = simulate(20, track=0.3254, wheel_gain=0.004, seam=0.08,
                          finish_at_wall_end=True, cruise=15)
        self.assertEqual(result["transitions"][-1]["reason"], "Reached end of tracked wall")
        self.assertEqual(result["zero_command_ticks_after_motion"], 0)
        self.assertLess(result["minimum_projected_axle_tire_edge_gap_m"], 0.07)
        self.assertGreater(result["minimum_projected_axle_tire_edge_gap_m"], 0.05)

    def test_35_percent_wall_trial_keeps_rolling_on_wider_approach(self):
        from argus_avoidance.wall_trial_sim import simulate

        result = simulate(10, track=0.22, wheel_gain=0.004, seam=0.08,
                          finish_at_wall_end=True, cruise=35, start_side_gap=0.18)
        self.assertEqual(result["peak_wheel_command_percent"], 35)
        self.assertEqual(result["zero_command_ticks_after_motion"], 0)
        self.assertGreater(result["forward_travel_m"], 0.50)
        self.assertGreater(result["minimum_modeled_side_gap_m"], 0.08)

    def test_optional_wall_end_finish_stops_once_without_pivoting(self):
        from argus_avoidance.wall_trial_sim import simulate

        result = simulate(20, track=0.22, wheel_gain=0.004, seam=0.08,
                          finish_at_wall_end=True, cruise=15)
        finish = result["trace"][-1]
        self.assertEqual(finish["reason"], "Reached end of tracked wall")
        self.assertEqual(finish["wheels"], [0, 0])
        self.assertGreaterEqual(finish["x_m"], 0.59)
        self.assertTrue(all(min(frame["wheels"]) > 0 for frame in result["trace"]
                            if 0.3 <= frame["at_s"] < finish["at_s"]))

    def test_box_row_keeps_known_wall_through_seam_until_near_end(self):
        from argus_avoidance.wall_trial_sim import simulate

        for seam in (0.04, 0.08):
            with self.subTest(seam=seam):
                result = simulate(25, track=0.22, wheel_gain=0.004, seam=seam)
                first_stop = next(item for item in result["transitions"]
                                  if item["at_s"] > 1 and item["wheels"] == [0, 0])
                self.assertGreaterEqual(first_stop["x_m"], 0.62)
                self.assertIsNotNone(result["row_end_reached_at_s"])
                self.assertGreater(result["minimum_modeled_side_gap_m"], 0.08)

    def test_bounded_wall_gap_curves_closer_without_pivot_or_contact(self):
        wall = replace(next(s for s in scenarios() if s.name == "wall"),
                       sensor_x=0.08)
        normal = run_scenario(wall, navigation_config(0.15, 0.30))
        closer = run_scenario(wall, navigation_config(0.15, 0.20))
        self.assertTrue(normal["passed"], normal["failures"])
        self.assertTrue(closer["passed"], closer["failures"])
        self.assertEqual(closer["contact_substeps"], 0)
        self.assertGreaterEqual(closer["minimum_physical_clearance_m"], 0.06)
        self.assertLess(closer["minimum_physical_clearance_m"],
                        normal["minimum_physical_clearance_m"] - 0.07)
        self.assertFalse(any(item["state"] in ("STOP", "TURN")
                             for item in closer["transitions"][1:]))

    def test_deterministic_scenarios(self):
        for scenario in scenarios():
            with self.subTest(scenario=scenario.name):
                result = run_scenario(scenario)
                self.assertEqual(result["contact_substeps"], 0)
                self.assertTrue(result["passed"], "\n".join(result["failures"]))
                self.assertEqual(result["turn_direction_flips_within_turn"], 0)
                if scenario.expect_turn:
                    self.assertTrue(result["turned"])
                    self.assertTrue(result["resumed_after_turn"])
                    self.assertGreater(result["distance_travelled_m"], 0.8)
                if scenario.expect_blocked:
                    self.assertEqual(result["final_state"], "BLOCKED")
                    self.assertLessEqual(result["distance_travelled_m"], 0.005)
                if scenario.dropout:
                    self.assertTrue(result["stopped_during_fault"])
                    self.assertTrue(result["explicit_rearm_succeeded"])
                    self.assertEqual(result["fault_motion_commands_before_rearm"], 0)


if __name__ == "__main__":
    unittest.main()
