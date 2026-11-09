"""Exercise editable layouts, exports, names and drive constraints."""

import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

repo = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(repo / "designer"))
from model import compile_model, drive_geometry, hardware_description, validate
from server import Store, export_zip


class ModelTests(unittest.TestCase):
    def setUp(self):
        self.design = json.loads((repo / "designs/default.json").read_text())

    def test_default_geometry(self):
        self.assertEqual(
            drive_geometry(self.design),
            {"wheel_radius_m": 0.035, "wheel_separation_m": 0.22},
        )

    def test_move_preserves_functional_sensor_and_template(self):
        original = copy.deepcopy(self.design)
        part = next(p for p in self.design["parts"] if p["id"] == "lidar_link")
        part["xyz_m"] = [0.1, -0.03, 0.25]
        part["rpy_rad"] = [0, 0, 0.5]
        model, _ = compile_model(self.design)
        root = ET.fromstring(model)
        self.assertEqual(
            root.find("joint[@name='lidar_joint']/origin").get("xyz"),
            "0.13 -0.03 0.134",
        )
        self.assertIsNotNone(root.find("gazebo[@reference='lidar_link']/sensor"))
        self.assertEqual(
            json.loads((repo / "designs/default.json").read_text()), original
        )

    def test_add_duplicate_and_remove(self):
        custom = dict(
            copy.deepcopy(self.design["parts"][9]),
            id="extra_scanner",
            label="Extra housing",
            role="fixed",
        )
        custom.pop("target")
        self.design["parts"].append(custom)
        self.design["parts"] = [
            p for p in self.design["parts"] if p["id"] != "arduino_mega"
        ]
        root = ET.fromstring(compile_model(self.design)[0])
        self.assertIsNotNone(root.find("link[@name='extra_scanner']"))
        self.assertIsNone(root.find("link[@name='arduino_mega']"))

    def test_missing_wheel_exports_but_cannot_drive(self):
        self.design["parts"] = [
            p for p in self.design["parts"] if p["role"] != "right_wheel"
        ]
        compile_model(self.design)
        with self.assertRaisesRegex(ValueError, "right wheel"):
            drive_geometry(self.design)

    def test_bad_transforms_and_target(self):
        for value in (float("nan"), float("inf"), 10):
            d = copy.deepcopy(self.design)
            d["parts"][0]["xyz_m"][0] = value
            with self.assertRaises(ValueError):
                validate(d)
        self.design["parts"][0]["target"]["link"] = "other"
        with self.assertRaises(ValueError):
            validate(self.design)

    def test_wheel_floor_and_alignment(self):
        wheel = next(p for p in self.design["parts"] if p["role"] == "left_wheel")
        wheel["xyz_m"][2] = 0.2
        with self.assertRaisesRegex(ValueError, "floor"):
            drive_geometry(self.design)
        wheel["xyz_m"][2] = 0.035
        wheel["xyz_m"][0] = 0.1
        with self.assertRaisesRegex(ValueError, "same X"):
            drive_geometry(self.design)

    def test_save_conflict_and_history(self):
        with tempfile.TemporaryDirectory() as directory:
            store = Store(Path(directory))
            data = store.load("default")
            store.save("default", self.design, data["revision"])
            self.design["name"] = "Changed"
            store.save("default", self.design, data["revision"])
            with self.assertRaises(FileExistsError):
                store.save("default", self.design, data["revision"])
            self.assertEqual(len(list((Path(directory) / "history").glob("*.json"))), 2)
            with self.assertRaises(ValueError):
                store.file("../escape")

    def test_hardware_export_removes_simulator(self):
        model = hardware_description(compile_model(self.design)[0])
        root = ET.fromstring(model)
        self.assertFalse(root.findall("gazebo"))
        self.assertFalse(root.findall("ros2_control"))
        self.assertNotIn("/home/robot", model)
        self.assertGreater(len(export_zip(self.design)), 1000)


if __name__ == "__main__":
    unittest.main()
