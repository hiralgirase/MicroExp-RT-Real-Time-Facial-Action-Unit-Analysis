import pandas as pd
import matplotlib.pyplot as plt

CSV_PATH = "results/all_videos_au_emotion.csv"

df = pd.read_csv(CSV_PATH)

# -------------------------
# Frame-level AU dynamics
# -------------------------
AUS = ["AU01", "AU04", "AU12"]

plt.figure(figsize=(10,5))
for au in AUS:
    if au in df.columns:
        plt.plot(df[au], label=au)

plt.title("Frame-Level AU Intensity Variation")
plt.xlabel("Frame Index")
plt.ylabel("AU Intensity")
plt.legend()
plt.tight_layout()
plt.savefig("results/au_time_series.png")
plt.close()

# -------------------------
# Video-level AU activity
# -------------------------
df["AU_SUM"] = df[AUS].sum(axis=1)
high_au_frames = df[df["AU_SUM"] > 0.6]

print("Total Frames:", len(df))
print("Frames with High AU Activity:", len(high_au_frames))

# -------------------------
# Emotion distribution
# -------------------------
emotion_cols = ["neutral", "happy", "sad", "surprise", "angry", "fear", "disgust"]
emotion_cols = [e for e in emotion_cols if e in df.columns]

emotion_counts = df[emotion_cols].idxmax(axis=1).value_counts()

plt.figure(figsize=(6,4))
emotion_counts.plot(kind="bar")
plt.title("Emotion Distribution Across Frames")
plt.ylabel("Frame Count")
plt.tight_layout()
plt.savefig("results/emotion_distribution.png")
plt.close()
