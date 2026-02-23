# MicroExp-RT

Real-Time Micro-Expression Analysis using Py-Feat

## Overview

MicroExp-RT is a real-time micro-expression analysis pipeline built
using Py-Feat. The system processes interview or observational videos to
extract frame-level Facial Action Units (AUs) and emotion probabilities,
followed by temporal analysis and visualization.

This project supports research in affective computing, psychological
response modeling, and behavioral analysis using facial dynamics.

------------------------------------------------------------------------

## Objectives

-   Extract frame-level facial Action Unit intensities\
-   Detect emotion probabilities per frame\
-   Perform temporal AU signal analysis\
-   Identify high AU activity segments\
-   Visualize emotion distribution across frames\
-   Support psychological and behavioral modeling research

------------------------------------------------------------------------

## System Architecture

Video Input\
↓\
Frame Extraction (OpenCV)\
↓\
Py-Feat Detection\
↓\
AU & Emotion CSV Generation\
↓\
Temporal Analysis\
↓\
Visualization

------------------------------------------------------------------------

## Project Structure

MicroExp-RT/ │ ├── data/ │ └── videos/ \# Input video files (.avi) │ ├──
frames/ \# Extracted frames │ ├── results/ │ ├──
all_videos_au_emotion.csv │ ├── au_time_series.png │ └──
emotion_distribution.png │ ├── module1_frame_extraction.py ├──
module2_3\_pyfeat_extraction.py ├── all_videos_au_emotion.py │ ├──
requirements.txt └── README.md

------------------------------------------------------------------------

## Installation

1.  Clone Repository

git clone https://github.com/your-username/MicroExp-RT.git cd
MicroExp-RT

2.  Install Dependencies

pip install -r requirements.txt

Required Libraries:

-   opencv-python\
-   numpy\
-   pandas\
-   matplotlib\
-   py-feat

------------------------------------------------------------------------

## How to Run

Step 1: Frame Extraction

Store videos inside:

data/videos/

Run:

python module1_frame_extraction.py

Frames will be saved in:

frames/`<video_name>`{=html}/

------------------------------------------------------------------------

Step 2: AU & Emotion Extraction

Run:

python module2_3\_pyfeat_extraction.py

Output:

results/all_videos_au_emotion.csv

This file contains:

-   Frame-level AU intensities\
-   Emotion probabilities\
-   Video identifiers

------------------------------------------------------------------------

Step 3: Temporal Analysis & Visualization

Run:

python all_videos_au_emotion.py

Generated outputs:

-   results/au_time_series.png
-   results/emotion_distribution.png

------------------------------------------------------------------------

## Output Description

1.  AU Time-Series Plot

Displays frame-level intensity variation for selected Action Units
(e.g., AU01, AU04, AU12). Used to identify micro-expression spikes and
temporal facial dynamics.

2.  Emotion Distribution Plot

Shows dominant emotion per frame based on maximum probability selection.
Useful for understanding emotional dominance across videos.

------------------------------------------------------------------------

## Key Features

-   Batch-based frame processing\
-   Multi-video support\
-   Frame-level AU intensity extraction\
-   Emotion probability modeling\
-   Temporal signal analysis\
-   Automated visualization generation\
-   Structured CSV export for research

------------------------------------------------------------------------

## Research Applications

-   Micro-expression analysis\
-   Psychological response modeling\
-   Interview behavior analysis\
-   Affective computing\
-   Behavioral biomarker research\
-   Temporal AU fusion studies

------------------------------------------------------------------------

## Methodology Summary

1.  Convert videos into frame sequences\
2.  Detect facial landmarks and AUs using Py-Feat\
3.  Extract emotion probabilities\
4.  Aggregate results into unified CSV dataset\
5.  Perform temporal modeling and visualization

------------------------------------------------------------------------

## Limitations

-   Performance depends on video quality and lighting\
-   Subtle micro-expressions require high frame-rate recordings\
-   Model accuracy depends on Py-Feat training data\
-   Real-time performance depends on hardware capability

------------------------------------------------------------------------

## Future Enhancements

-   Webcam-based real-time AU extraction\
-   Deep learning temporal models (LSTM / Transformer)\
-   Micro vs Macro expression classification\
-   Psychological state prediction\
-   Real-time dashboard deployment

------------------------------------------------------------------------

## License

MIT License

This project is open for academic and research use.

------------------------------------------------------------------------

## Author

Hiral\
Research in Facial Action Unit Modeling and Micro-Expression Analysis
