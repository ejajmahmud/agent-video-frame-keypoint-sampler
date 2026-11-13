"""CLI for agent-video-frame-keypoint-sampler."""
import sys
import argparse
from .sampler import VideoKeypointSampler

def main():
    parser = argparse.ArgumentParser(description="Agent Video Frame Keypoint Sampler CLI")
    parser.add_argument("--demo", action="store_true", help="Run keypoint frame sampling demo")
    args = parser.parse_args()

    if args.demo:
        sampler = VideoKeypointSampler(novelty_threshold=0.2)
        sampler.feed_frame(0, 0.0, "hash_0", 1.0)
        sampler.feed_frame(1, 0.033, "hash_0", 0.0)  # Duplicate
        sampler.feed_frame(2, 0.066, "hash_1", 0.05) # Minor noise
        kf = sampler.feed_frame(3, 0.1, "hash_2", 0.45)   # Significant UI shift
        print(f"[+] Total frames evaluated: 4, Keyframes retained: {len(sampler.keyframes)}")
        print(f"[+] Latest keyframe at t={kf.timestamp_s}s with score={kf.novelty_score}")
    else:
        parser.print_help()
    sys.exit(0)

if __name__ == "__main__":
    main()
