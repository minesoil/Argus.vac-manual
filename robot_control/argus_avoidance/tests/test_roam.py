"""Serial decoding and failure-driven checks of the actual roaming runner."""

import math
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from argus_avoidance.c1 import C1Reader, Sweep
from argus_avoidance.core import AvoidanceController, Config
from argus_avoidance.follow import ControlError
from argus_avoidance.roam import run
from argus_avoidance.usb_bridge import claim_phone_start


class Clock:
    now = 0.0
    def __call__(self):
        return self.now
    def sleep(self, seconds):
        self.now += seconds


class Reader:
    error = None
    def __init__(self, clock, scene=None, freeze=None):
        self.clock, self.scene, self.freeze = clock, scene, freeze
    @property
    def latest(self):
        now = min(self.clock(), self.freeze) if self.freeze is not None else self.clock()
        tick = int(now / 0.1)
        ranges = [2.0] * 72
        if self.scene:
            self.scene(now, ranges)
        return Sweep(tick + 1, tick * 0.1, tick * 0.1, tuple(ranges), 500)


class Client:
    def __init__(self, reject_after=None):
        self.session = None
        self.commands = []
        self.arms = []
        self.stopped = self.closed = False
        self.reject_after = reject_after
    def request(self, path):
        return {"mode": "stopped", "epoch": 42}
    def arm(self, expected_epoch):
        self.arms.append(expected_epoch)
        self.session = "session"
    def drive(self, left, right):
        if self.reject_after is not None and len(self.commands) >= self.reject_after:
            raise ControlError("Phone Stop won", 409)
        self.commands.append((left, right))
    def stop(self):
        self.stopped = True
    def close(self):
        self.closed = True


class RoamTests(unittest.TestCase):
    def execute(self, scene=None, freeze=None, client=None, duration=3):
        clock = Clock()
        reader = Reader(clock, scene, freeze)
        client = client or Client()
        output = []
        controller = AvoidanceController(Config(robot_radius_m=0.23, margin_m=0.06,
                                                scan_timeout_s=0.6))
        result = run(reader, controller, client, duration, clock=clock,
                     sleep=clock.sleep, emit=output.append)
        self.assertTrue(client.stopped and client.closed)
        return result, client, output

    def test_wall_stops_then_pivots_then_resumes(self):
        def scene(now, ranges):
            if 0.7 <= now < 1.8:
                ranges[0] = ranges[-1] = 0.5
        result, client, _ = self.execute(scene)
        self.assertEqual(result, 0)
        commands = client.commands
        forward = commands.index((18, 18))
        turn = commands.index((-15, 15))
        self.assertIn((0, 0), commands[forward:turn])
        self.assertIn((18, 18), commands[turn+1:])
        self.assertEqual(client.arms, [42])

    def test_expired_scan_stops_and_never_rearms(self):
        result, client, output = self.execute(freeze=0.5)
        self.assertEqual(result, 1)
        self.assertIn("Scan expired", output[-1])
        self.assertEqual(len(client.arms), 1)

    def test_unknown_return_cannot_be_treated_as_clear(self):
        def scene(now, ranges):
            if now > 0.8:
                ranges[15] = math.nan
        result, client, output = self.execute(scene)
        self.assertEqual(result, 1)
        self.assertIn("unknown", output[-1].lower())
        self.assertEqual(len(client.arms), 1)

    def test_obstacle_inside_rotation_footprint_prevents_turn(self):
        def scene(now, ranges):
            if now > 0.8:
                ranges[20] = 0.2
        result, client, output = self.execute(scene)
        self.assertEqual(result, 1)
        self.assertIn("footprint", output[-1])
        self.assertFalse(any(l*r < 0 for l, r in client.commands))

    def test_phone_stop_cannot_be_automatically_rearmed(self):
        client = Client(reject_after=10)
        result, client, output = self.execute(client=client)
        self.assertEqual(result, 1)
        self.assertIn("Phone Stop", output[-1])
        self.assertEqual(len(client.arms), 1)

    def test_never_finding_exit_times_out(self):
        def scene(now, ranges):
            ranges[0] = ranges[-1] = 0.5
        result, client, output = self.execute(scene, duration=18)
        self.assertEqual(result, 1)
        self.assertIn("Turn timed out", output[-1])
        self.assertIn((-15, 15), client.commands)

    def test_raw_angle_pose_places_front_target_in_front(self):
        ranges = [2.0]*72
        ranges[18] = 0.5  # raw 90 degrees
        controller = AvoidanceController()
        controller.observe(Sweep(1, 1, 1.1, tuple(ranges), 500).scan(front_deg=92.5))
        self.assertTrue(controller.arm(1.2)[0])
        self.assertAlmostEqual(controller.step(1.2).front_clearance, 0.25)

    def test_decoder_rejects_bad_sync_and_decodes_fixed_point(self):
        self.assertIsNone(C1Reader.node(bytes((0, 0, 0, 0, 0))))
        # quality 10, start bit true, angle 90 degrees, distance 1 metre
        angle = 90*64
        node = bytes(((10 << 2)|1, ((angle & 127)<<1)|1, angle>>7, 160, 15))
        self.assertEqual(C1Reader.node(node), (True, 90.0, 1.0, 10))

    def test_roaming_phone_request_is_not_fed_to_tape_follower(self):
        controller, launch = Mock(), Mock()
        state = {"follow_pending": True, "follow_kind": "roam", "epoch": 9, "follow_token": "abc"}
        claim_phone_start(controller, state, None, launch)
        controller.request.assert_not_called()
        args = ["--lidar", "/dev/c1", "--front-deg", "90", "--commissioned"]
        claim_phone_start(controller, state, None, launch, roam_args=args)
        command = launch.call_args.args[0]
        self.assertIn("argus_avoidance.roam", command)
        self.assertIn("9", command)

    def test_uncommissioned_profile_cannot_enable_phone_roaming(self):
        from argus_avoidance.usb_bridge import load_roam_args
        example = Path(__file__).resolve().parents[1] / "config" / "roam.example.json"
        self.assertIsNone(load_roam_args(example))

    def test_stop_during_initial_sensor_wait_keeps_original_epoch(self):
        clock = Clock()
        reader = Reader(clock)
        client = Client()
        def changed_epoch(expected_epoch):
            client.arms.append(expected_epoch)
            raise ControlError("Stop changed epoch", 409)
        client.arm = changed_epoch
        output = []
        result = run(reader, AvoidanceController(), client, 3, expected_epoch=77,
                     clock=clock, sleep=clock.sleep, emit=output.append)
        self.assertEqual(result, 1)
        self.assertEqual(client.arms, [77])
        self.assertEqual(client.commands, [])
        self.assertTrue(client.stopped and client.closed)


if __name__ == "__main__":
    unittest.main()
