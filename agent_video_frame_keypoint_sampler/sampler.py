"""Novelty-based keyframe extractor for video streams."""
from typing import Dict, List, Optional, Tuple, Any

class Keyframe:
    def __init__(self, frame_index: int, timestamp_s: float, novelty_score: float, data_hash: str):
        self.frame_index = frame_index
        self.timestamp_s = timestamp_s
        self.novelty_score = novelty_score
        self.data_hash = data_hash

class VideoKeypointSampler:
    """Selects high-novelty keyframes and filters static duplicates."""

    def __init__(self, novelty_threshold: float = 0.15):
        self.novelty_threshold = novelty_threshold
        self.keyframes: List[Keyframe] = []
        self.last_hash: Optional[str] = None

    def feed_frame(self, frame_index: int, timestamp_s: float, frame_hash: str, difference_metric: float) -> Optional[Keyframe]:
        if self.last_hash == frame_hash:
            return None  # Exact duplicate

        if not self.keyframes or difference_metric >= self.novelty_threshold:
            kf = Keyframe(frame_index, timestamp_s, difference_metric, frame_hash)
            self.keyframes.append(kf)
            self.last_hash = frame_hash
            return kf

        return None
