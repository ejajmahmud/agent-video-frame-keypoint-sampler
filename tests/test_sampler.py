"""Unit tests for agent-video-frame-keypoint-sampler."""
import unittest
from agent_video_frame_keypoint_sampler.sampler import VideoKeypointSampler

class TestVideoSampler(unittest.TestCase):
    def setUp(self):
        self.sampler = VideoKeypointSampler(novelty_threshold=0.2)

    def test_first_frame_retained(self):
        kf = self.sampler.feed_frame(0, 0.0, "h0", 0.0)
        self.assertIsNotNone(kf)
        self.assertEqual(len(self.sampler.keyframes), 1)

    def test_ignore_duplicates(self):
        self.sampler.feed_frame(0, 0.0, "h0", 0.0)
        kf2 = self.sampler.feed_frame(1, 0.033, "h0", 0.0)
        self.assertIsNone(kf2)
        self.assertEqual(len(self.sampler.keyframes), 1)

if __name__ == "__main__":
    unittest.main()
