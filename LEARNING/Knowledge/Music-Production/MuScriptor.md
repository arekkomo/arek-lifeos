---
title: "MuScriptor — Multi-Instrument Audio-to-MIDI Transcription"
category: source
summary: Kyutai/Mirelo transformer-decoder model that transcribes multi-instrument music audio into streamed note events or MIDI, trained on 170k songs across genres.
tags: [muscriptor, music-transcription, audio-to-midi, midi, multi-instrument, kyutai, music-production]
sources: 1
source_path: https://github.com/muscriptor/muscriptor
source_date: 2026-07
authors: [Kyutai, Mirelo]
ingested: 2026-07-19
updated: 2026-07-19
---

# MuScriptor — Multi-Instrument Audio-to-MIDI Transcription

**Links:** [GitHub](https://github.com/muscriptor/muscriptor) · [Paper](https://arxiv.org/abs/2607.08168v1) · [Models](https://huggingface.co/MuScriptor) · [Demo](https://muscriptor.kyutai.org)

## What it does

MuScriptor converts recorded music into instrument-labelled note events or a MIDI file. It is trained on 170k songs ranging from classical music to heavy metal, targeting multi-instrument transcription rather than just solo piano or vocals.

## Practical interface

- `uvx muscriptor transcribe` for CLI use
- `uvx muscriptor serve` for local web UI
- Python API streams note-start/note-end events or returns MIDI directly
- Optional expected-instrument list (e.g. `acoustic_piano`, `drums`) can constrain transcription

## Models and access

| Variant | Size | Practical note |
|---|---:|---|
| small | 103M | CPU-friendly option |
| medium | 307M | default quality/speed balance |
| large | 1.4B | best accuracy; GPU recommended |

Weights are gated on Hugging Face under **CC BY-NC 4.0**. A free HF account, accepted model license, and token/login are required. This makes it unsuitable for commercial use without separate permission.

## Where it fits

Use it to turn a reference track, jam, or recorded musical sketch into editable MIDI for arrangement analysis, DAW reconstruction, or visual-music synchronization. It analyzes existing audio; it does **not** generate new music.

## Related

- [[Audio-to-MIDI-Transcription]] — workflow pattern
- [[Suno Reference Song Analysis Template]] — MuScriptor can add note/instrument evidence to a reference-track analysis
- [[Magma RT2]] — generation counterpart: Magma creates audio; MuScriptor extracts editable note structure from audio
