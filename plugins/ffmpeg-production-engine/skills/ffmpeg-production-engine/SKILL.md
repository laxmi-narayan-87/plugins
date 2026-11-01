---
name: ffmpeg-production-engine
description: Design robust FFmpeg commands and media pipelines.
---

Use when writing, reviewing, or troubleshooting FFmpeg commands and production media pipelines.

Workflow:
1. Inspect the stated input codecs, dimensions, frame rate, sample rate, channels, duration, target platform, and quality/size constraints. Do not assume unknown media metadata.
2. Explain the filter/codec pipeline before providing commands; quote paths safely and use explicit stream mapping where appropriate.
3. Provide a non-destructive command first, write to a new output path, and avoid shell constructs that can delete or overwrite user data.
4. Explain codec, bitrate/CRF, pixel format, color, audio, container, and hardware-acceleration trade-offs. Verify flags against the user's FFmpeg build/version.
5. Include a validation command such as ffprobe and checks for duration, stream layout, sync, and playback.

Never claim a conversion finished without execution evidence. Ask before overwriting, deleting originals, or uploading media.
