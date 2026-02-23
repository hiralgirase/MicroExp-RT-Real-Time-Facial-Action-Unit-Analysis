from feat import Detector
import pandas as pd
import os
import glob

# -------------------------
# Paths
# -------------------------
FRAME_ROOT = "frames"
OUTPUT_CSV = "results/all_videos_au_emotion.csv"

os.makedirs("results", exist_ok=True)

# -------------------------
# Initialize Detector
# -------------------------
detector = Detector(
    enable_identity=False,
    output_size=(224, 224)
)

all_dfs = []

# -------------------------
# Process each video
# -------------------------
video_folders = [
    d for d in os.listdir(FRAME_ROOT)
    if os.path.isdir(os.path.join(FRAME_ROOT, d))
]

for video_name in video_folders:
    frame_dir = os.path.join(FRAME_ROOT, video_name)
    image_files = sorted(glob.glob(os.path.join(frame_dir, "*.jpg")))

    if not image_files:
        print(f"⚠️ No frames found for {video_name}, skipping")
        continue

    print(f"🚀 Running Py-Feat on {video_name} ({len(image_files)} frames)...")

    BATCH_SIZE = 50
    batch_dfs = []

    for i in range(0, len(image_files), BATCH_SIZE):
        batch = image_files[i:i + BATCH_SIZE]
        print(f"   Processing frames {i}–{i + len(batch)}")

        results = detector.detect_image(
            batch,
            batch_size=1
        )

        # ✅ CORRECT conversion for your Py-Feat version
        df_batch = pd.DataFrame(results)
        batch_dfs.append(df_batch)

    video_df = pd.concat(batch_dfs, ignore_index=True)
    video_df["video_id"] = video_name
    all_dfs.append(video_df)

# -------------------------
# Save final CSV
# -------------------------
final_df = pd.concat(all_dfs, ignore_index=True)
final_df.to_csv(OUTPUT_CSV, index=False)

print("✅ All videos processed successfully")
print(f"📄 Combined CSV saved at: {OUTPUT_CSV}")
