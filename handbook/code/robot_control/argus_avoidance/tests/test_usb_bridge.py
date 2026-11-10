"""Check local bridge routing while its USB controller is replaced."""

from http.server import ThreadingHTTPServer
import json
from pathlib import Path
import sys
import threading
import unittest
from unittest import mock
import urllib.error
import urllib.request

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from argus_avoidance.follow import ControlError
from argus_avoidance.usb_bridge import BridgeHandler, claim_phone_start


class Controller:
    def __init__(self):
        self.calls = []
        self.fail = False

    def request(self, path, values):
        self.calls.append((path, values))
        if self.fail:
            raise ControlError("Expired", 409)
        return {"status": 204 if path.endswith("/drive") else 200, "mode": "stopped", "epoch": 3}


class USBBridgeTests(unittest.TestCase):
    def setUp(self):
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), BridgeHandler)
        self.server.controller = Controller()
        self.server.usb_lock = threading.Lock()
        self.worker = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.worker.start()
        self.address = f"http://127.0.0.1:{self.server.server_port}"

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.worker.join()

    def call(self, path, body=None):
        request = urllib.request.Request(self.address + path, data=body)
        return urllib.request.urlopen(request, timeout=1)

    def test_state_and_drive_reach_single_usb_owner(self):
        with self.call("/state") as response:
            self.assertEqual(json.load(response)["epoch"], 3)
        with self.call("/auto/drive", b"session=a&seq=1&l=5&r=5") as response:
            self.assertEqual(response.status, 204)
            self.assertEqual(response.read(), b"")
        self.assertEqual(self.server.controller.calls[1][1]["seq"], "1")

    def test_rejection_status_survives_transport(self):
        self.server.controller.fail = True
        with self.assertRaises(urllib.error.HTTPError) as error:
            self.call("/auto/drive", b"session=a&seq=1&l=5&r=5")
        self.assertEqual(error.exception.code, 409)

    def test_unknown_or_malformed_requests_do_not_reach_usb(self):
        for path, body, status in (("/auto/arm", None, 404), ("/stop", b"x=1", 404),
                                   ("/auto/arm", b"epoch=1&epoch=2", 400)):
            with self.subTest(path=path, body=body):
                with self.assertRaises(urllib.error.HTTPError) as error:
                    self.call(path, body)
                self.assertEqual(error.exception.code, status)
        self.assertEqual(self.server.controller.calls, [])

    def test_start_claim_launches_once_with_captured_epoch(self):
        controller = self.server.controller
        launch = mock.Mock(return_value=object())
        state = {"follow_pending": True, "epoch": 42, "follow_token": "1234567890abcdef"}
        child = claim_phone_start(controller, state, None, launch)
        self.assertIs(child, launch.return_value)
        self.assertEqual(controller.calls[0], ("/follow/claim", {"epoch": 42, "token": "1234567890abcdef"}))
        self.assertIn("42", launch.call_args.args[0])
        self.assertIn("--expected-epoch", launch.call_args.args[0])

    def test_stale_claim_and_running_child_do_not_launch(self):
        state = {"follow_pending": True, "epoch": 42, "follow_token": "1234567890abcdef"}
        launch = mock.Mock()
        self.server.controller.fail = True
        self.assertIsNone(claim_phone_start(self.server.controller, state, None, launch))
        self.server.controller.fail = False
        child = mock.Mock()
        child.poll.return_value = None
        self.assertIs(claim_phone_start(self.server.controller, state, child, launch), child)
        launch.assert_not_called()


if __name__ == "__main__":
    unittest.main()
