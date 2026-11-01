---
name: whisperx-caption-studio
description: Prepare transcription, alignment, and subtitle workflows with WhisperX.
---

Use when creating transcripts, word-level alignment, speaker diarization, or subtitle files with WhisperX.

Workflow:
1. Clarify audio/video file availability, language, model size, hardware, diarization needs, output formats, and privacy constraints.
2. Explain the pipeline: transcription, alignment, optional diarization, and subtitle export. Make model and token requirements explicit.
3. Preserve uncertainty in low-confidence segments; never silently invent words or speaker labels.
4. Use speaker diarization only when justified and avoid asserting real-world identities from speaker IDs.
5. Provide QA for timestamps, punctuation, overlap, names, multilingual sections, subtitle line length, and synchronization.

Do not claim to transcribe or align media without connected files and runtime. Protect private recordings and avoid uploading them to external services without approval.
