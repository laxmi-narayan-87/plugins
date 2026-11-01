---
name: librosa-audio-intelligence
description: Analyze audio features and build reproducible librosa workflows.
---

Use when analyzing audio or designing Python workflows with librosa.

Workflow:
1. Clarify audio source, sample rate, channels, duration, task, output metrics, and whether files are available.
2. Choose appropriate operations such as loading/resampling, waveform inspection, spectrogram, STFT, MFCC, chroma, onset, tempo, or segmentation.
3. Explain parameter choices and units; distinguish estimates from ground truth.
4. Generate reproducible Python guidance with version-aware API usage and explicit handling of sample rate/channel shape.
5. Include validation for clipping, silence, file duration, resampling artifacts, and interpretation limits.

Do not infer identity or sensitive traits from voice. Do not claim to process audio unless a file or runtime is actually available.
