---
title: "Higgs Audio v3 — Boson AI TTS (Source)"
category: source
summary: Production-grade text-to-speech framework with inline emotional tags, speaker adaptation, and fine-grained prosody control. Open-weight 4B model available for local deployment.
tags: [AI-Audio, Text-to-Speech, Emotional Control, Voice Cloning, Open-Weight]
sources: 1
updated: 2026-07-03
source_path: raw/notion-export/higgs-audio-entry.md
source_date: 2026-06
authors: [Boson AI]
ingested: 2026-07-03
---

# [[Higgs Audio v3]] (Source)

> ⚠️ **Cross-domain opportunity** — Higgs Audio v3's emotional tag system is directly relevant to [[Acting-Techniques]], specifically Stanislavski's emotional memory framework: can you program a voice to match the same emotional progression as an actor would? Also connects to [[Vocal-Performance]] for AI-driven character voices.

## Summary
Higgs Audio v3 by Boson AI is a controllable text-to-speech system that supports inline emotional tagging — meaning you can insert markers within the text to control the emotional quality of speech generation in real-time. The model (4B parameters) is open-weight and available for local deployment, making it suitable for production pipelines where privacy or cost matters. Core capabilities include speaker adaptation, prosody manipulation, and cinematic-quality voice synthesis.

## Key Claims
1. **Inline emotional tags**: Unlike traditional TTS that generates flat, emotionally neutral speech, Higgs v3 lets you inject emotional markers directly into the text pipeline (`--emotional 'happy'`), allowing dynamic emotional shifts mid-generation. > Cited from [[Higgs Audio v3]]
2. **Production-grade voice quality**: Marketed as "cinematic-quality" — suggests this is aimed at professional content creation rather than basic accessibility or demo use cases. > Cited from [[Higgs Audio v3]]
3. **Open-weight 4B model**: The HuggingFace model (`bosonai/higgs-audio-v3-tts-4b`) can be downloaded and run locally, removing dependency on paid APIs for production workflows. > Cited from [[Higgs Audio v3]]
4. **Prosody manipulation**: Fine-grained control over speech rhythm, intonation, and pacing — critical for natural-feeling dialogue rather than robotic monotone. > Cited from [[Higgs Audio v3]]

## Setup / How to Run
```bash
pip install transformers
python inference.py --model bosonai/higgs-audio-v3-tts-4b \
  --text 'your text' \
  --emotional 'happy'
```
Model hosted on HuggingFace: `https://huggingface.co/bosonai/higgs-audio-v3-tts-4b`

## Capabilities (from source)
| Capability | Description | Relevance |
|-----------|-------------|-----------|
| Inline emotional tags | Control emotion mid-sentence via markers | [[AI-Audio]], [[Text-to-Speech]] |
| Speaker adaptation | Adapt voice to match target speaker profiles | [[Voice-Cloning]], [[Character-Voices]] |
| Prosody manipulation | Fine-grained rhythm/pacing/intonation control | [[Vocal-Performance]], [[Dialogue-Delivery]] |
| Open-weight 4B | Local deployment, no API dependency | [[Pipeline-Automation]] |

## Use Cases (from source)
- Generate emotionally directed voiceovers for character content — directly relevant to film directing AI characters
- Produce cinematic-quality voice work with emotional control — bridges TTS and [[Voice-Performance]]
- Adapt voice to match character emotional states in production — useful for pre-vis and pitch deck generation
- Fast iteration on voice direction without external talent — reduces production cost/time for conceptual content

## Key Facts
| Property | Value |
|----------|-------|
| Author | Boson AI |
| Version | v3 (4B parameters) |
| Model Format | HuggingFace (open-weight) |
| URL | https://huggingface.co/bosonai/higgs-audio-v3-tts-4b |
| Primary domain | Text-to-Speech / Audio Synthesis |
| Input format | Text + optional emotional tags → audio output |

## Cross-Domain Connections
1. **To [[AI-Video]]**: NAVA (newly ingested page) generates video+nativaudio together; Higgs adds fine-grained emotional control to the *audio* layer — these two could be combined for AI-generated scenes with character voiceovers
2. **To [[Filmmaking]]**: Emotional speech output means you can generate "director's choice" voice direction in conceptual audio, testing emotional beats before live recording
3. **To [[VFX]]**: Cinematic-quality TTS reduces the need for ADR (Automated Dialogue Replacement) in post-production for AI-generated content

## Questions For Further Exploration
1. What's the latency/timing resolution of emotional tags — can you shift emotion mid-word or only at phrase boundaries?
2. Are there pre-trained speaker profiles, or does "speaker adaptation" require few-shot examples per voice?
3. Can Higgs v3 generate non-speech audio (breaths, laughs, sighs) alongside dialogue?
4. ComfyUI node available? Or CLI/Python only?

## Appears In
- This Notion knowledge base entry (2026-06-08) — tagged `VFX` with Type=`Github`
