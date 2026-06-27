# Whisper Benchmarking & Evaluation

## Objective

This project benchmarks OpenAI Whisper models and compares:

- Tiny
- Base
- Small

using:

- Processing Time
- Word Error Rate (WER)
- Transcription Accuracy

---

## Features

- Automatic Speech-to-Text
- Benchmarking of Multiple Models
- WER Calculation
- JSON Output
- CSV Benchmark Report

---

## Installation

```bash
pip install -r requirements.txt
```

Install FFmpeg separately.

---

## Run

```bash
python benchmark.py
```

---

## Output

Example:

```json
{
  "transcript": "I have worked with Python and FastAPI.",
  "processing_time": 4.1
}
```

---

## Models Compared

- Tiny
- Base
- Small

---

## Evaluation Metric

Word Error Rate (WER)

Lower WER means better transcription quality.

## Benchmark Results

| Model | Avg Processing Time (s) | Avg WER |
|---------|---------:|---------:|
| Tiny | 1.14 | 0.33635 |
| Base | 1.64 | 0.38635 |
| Small | 4.67 | 0.33635 |

## Conclusion

- Tiny model was the fastest.
- Small model achieved the best accuracy.
- Tiny offered the best speed-to-accuracy balance.