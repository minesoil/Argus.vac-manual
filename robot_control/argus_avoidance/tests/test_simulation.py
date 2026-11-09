"""Independent geometry and behavior checks for the small standalone simulator."""

import math
import unittest

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
