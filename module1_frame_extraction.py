import cv2
import os

VIDEO_DIR = "data/videos"
FRAME_ROOT = "frames"

os.makedirs(FRAME_ROOT, exist_ok=True)

video_files = [v for v in os.listdir(VIDEO_DIR) if v.endswith(".avi")]

for video_file in video_files:
    video_path = os.path.join(VIDEO_DIR, video_file)

    video_name = os.path.splitext(video_file)[0]
    output_dir = os.path.join(FRAME_ROOT, video_name)
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    frame_id = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imwrite(f"{output_dir}/frame_{frame_id:05d}.jpg", frame)
        frame_id += 1

    cap.release()
    print(f"{video_name}: Extracted {frame_id} frames")
