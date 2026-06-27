import os
import json
import time
import whisper
import pandas as pd
from jiwer import wer

DATASET_DIR = "dataset"
OUTPUT_DIR = "outputs"

MODELS = ["tiny", "base", "small"]

os.makedirs(OUTPUT_DIR, exist_ok=True)

audio_files = [
    f for f in os.listdir(DATASET_DIR)
    if f.endswith((".wav", ".mp3", ".m4a"))
]

if not audio_files:
    raise Exception("No audio files found in dataset folder.")

results = []

for model_name in MODELS:

    print(f"\nLoading model: {model_name}")
    model = whisper.load_model(model_name)

    for audio_file in audio_files:

        audio_path = os.path.join(DATASET_DIR, audio_file)

        transcript_file = os.path.splitext(audio_file)[0] + ".txt"
        transcript_path = os.path.join(DATASET_DIR, transcript_file)

        if not os.path.exists(transcript_path):
            print(f"Transcript file missing for {audio_file}")
            continue

        with open(transcript_path, "r", encoding="utf-8") as f:
            ground_truth = f.read().strip()

        start_time = time.time()

        result = model.transcribe(audio_path)

        processing_time = round(time.time() - start_time, 2)

        transcript = result["text"].strip()

        error_rate = round(
            wer(ground_truth, transcript),
            4
        )

        output = {
            "audio_file": audio_file,
            "model": model_name,
            "transcript": transcript,
            "processing_time": processing_time,
            "wer": error_rate
        }

        json_file = os.path.join(
            OUTPUT_DIR,
            f"{os.path.splitext(audio_file)[0]}_{model_name}.json"
        )

        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=4)

        results.append(output)

df = pd.DataFrame(results)

df.to_csv(
    os.path.join(OUTPUT_DIR, "benchmark_results.csv"),
    index=False
)

summary = (
    df.groupby("model")
    .agg({
        "processing_time": "mean",
        "wer": "mean"
    })
    .reset_index()
)

summary.to_csv(
    os.path.join(OUTPUT_DIR, "summary.csv"),
    index=False
)

print("\nBenchmark Complete")
print(summary)