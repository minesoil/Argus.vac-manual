import sys
from pathlib import Path
import unittest
import cv2
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from argus_avoidance.obstacles import calibrate,detect,region_mask,Preview
import tempfile,json

class ObstacleTests(unittest.TestCase):
    def setUp(self):
        self.floor=np.full((480,640,3),210,np.uint8)
        self.profile=calibrate([self.floor]*5,now=100)
    def test_clear_floor_and_moderate_shadow(self):
        for value in (210,155):
            self.assertEqual(detect(np.full_like(self.floor,value),self.profile,now=101).state,'clear')
    def test_dark_colored_and_thin_obstacles(self):
        for color,thickness in (((15,15,15),35),((20,30,180),35),((0,0,0),4)):
            frame=self.floor.copy();cv2.line(frame,(250,435),(420,450),color,thickness)
            result=detect(frame,self.profile,now=101)
            self.assertEqual(result.state,'blocked');self.assertTrue(result.boxes)
    def test_obstacles_outside_watched_region_do_not_claim_coverage(self):
        frame=self.floor.copy();frame[50:200]=0
        self.assertEqual(detect(frame,self.profile,now=101).state,'clear')
    def test_expired_future_bad_or_resized_profile_faults(self):
        self.assertEqual(detect(self.floor,self.profile,now=1001).state,'fault')
        self.assertEqual(detect(self.floor,self.profile,now=99).state,'fault')
        self.assertEqual(detect(self.floor,{},now=101).state,'fault')
        self.assertEqual(detect(self.floor[:300],self.profile,now=101).state,'fault')
    def test_calibration_requires_multiple_uniform_bright_frames(self):
        with self.assertRaises(ValueError):calibrate([self.floor]*2)
        with self.assertRaises(ValueError):calibrate([np.zeros_like(self.floor)]*5)
        with self.assertRaises(ValueError):region_mask((.7,.8,.2,1))
    def test_detection_never_adapts_obstacle_into_floor(self):
        before=str(self.profile);frame=self.floor.copy();frame[410:470,250:450]=0
        for _ in range(20):self.assertEqual(detect(frame,self.profile,now=101).state,'blocked')
        self.assertEqual(str(self.profile),before)
    def test_missing_and_in_progress_profiles_cannot_continue_as_clear(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'floor.json';preview=Preview({},path)
            with self.assertRaises(OSError):preview.refresh_profile()
            path.write_text(json.dumps(self.profile));preview.refresh_profile()
            self.assertEqual(preview.profile,self.profile)
            path.with_suffix('.calibrating').write_text('in progress')
            with self.assertRaisesRegex(ValueError,'in progress'):preview.refresh_profile()

if __name__=='__main__':unittest.main()
