---
title: "WavTTS — ByteDance Zero-Shot TTS"
category: source
summary: ByteDance zero-shot text-to-speech system enabling high fidelity voice synthesis from short vocal reference with controllable emotion, prosody, and speaking style. ComfyUI integration available for automated pipelines.
tags: [AI-Audio, TTS, Zero-Shot-Synthesis, Voice-Cloning, Emotion-Control]
sources: 1
updated: 2026-07-03
source_path: raw/notion-export/wavtts-entry.md
ingested: 2026-07-03
---

# [[WavTTS]] (Source)

## Summary
WavTTS is a zero-shot text-to-speech system developed by ByteDance that creates realistic voice synthesis from a short audio reference clip — without requiring any per-speaker retraining or fine-tuning. The model outputs controllable speech with adjustable emotion, prosody (speech rhythm), and speaking style parameters.

## Key Claims
- **Short-voice reference**: Can generate high-fidelity synthesis from just a brief vocal sample, lowering production barriers significantly over traditional 15+ second clip requirements
> Cited from [[wavtts-source]]
- **Full emotional/intonation control**: Prosody and emotion can be adjusted independently of voice identity — you change *how* someone speaks without changing *who* is speaking
- **ComfyUI integration**: Available as a ComfyUI node, meaning it integrates directly into visual pipeline workflows for automation

## Use Cases (from source)
- Generate dialogue voiceovers for AI-generated character content
- Clone voice from reference footage for lip-sync pipelines
- Create emotional variations for iterative ADR/voice direction
- Prototyping of audio assets with minimal voice samples

## How to Run (ComfyUI integration)
```bash
git clone git@github.com:Saganaki22/WavTTS-ComfyUI.git
cd WavTTs-ComfyUI
pip install -r requirements.txt
comfyui --node wavtts --ref_audio voice.wav
```

## Key Facts
| Property | Value |
|----------|-------|
| Author | ByteDance |
| Model Type | Zero-shot TTS, short reference cloning |
| URL: https://bytedance.github.io/WavTTS/
| Primary domain: AI Voice Synthesis (Text-to-Speech) |
| Delivery mode | ComfyUI plugin / Python package |

## Cross-Domain Connections
- [[Audio-Generation]] — represents the leading zero-shot voice synthesis approach in open-source TTS space
- [[Pipeline-Automation]] — ComfyUI integration means this can be wired into automated production pipelines without custom glue code
- [[Character-Avatar-Integration]] — pairs directly with [[StreamChar]] for full voice → animated avatar pipeline

## Appears In
- This Notion knowledge base entry (2026-06-08), tagged `VFX`, Type=`Github`
