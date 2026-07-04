---
title: "Higgs Audio v3"
category: entity
summary: Production-grade open-weight text-to-speech framework by Boson AI supporting inline emotional tags, speaker adaptation, and fine-grained prosody control in a 4B model.
tags: [AI-Audio, Text-to-Speech, Emotional-Control, Voice-Cloning, Open-Weight]
sources: 1
updated: 2026-07-03
---

# [[Higgs Audio v3]]

> ⚠️ Contradiction with typical AI voice workflows: most TTS tools produce emotionally flat or pre-set vocal tones. Higgs v3's inline emotional tags allow *dynamic* emotional shifts within a single generation — meaning one model can cover the range of an actor's performance arc rather than requiring 10+ separate clips stitched together.

## What it is
[[Higgs Audio v3]] is a controllable text-to-speech system by Boson AI that supports inserting emotional markers directly within the text pipeline. The open-weight 4B model can be downloaded and run locally, enabling production-quality voice synthesis without API dependency or subscription costs. Core capabilities include speaker adaptation, prosody manipulation, and cinematic-level voice quality.

## Why it matters
This is significant for [[Vocal-Performance]] and [[Dialogue-Delivery]] because emotional control transforms AI-generated speech from a novelty into a directorial tool. Instead of generating multiple flat-toned clips and hoping to edit them together, you can inject emotional progression markers — matching Stanislavski's "emotional memory" concept in written form — for seamless character voiceovers with natural emotional arcs.

## Key facts
- Inline emotional tags: Emotional control markers inline (not pre-set emotional profiles) allow mid-sentence shifts without re-generating the entire clip
> Cited from [[higgs-audio-v3-source]]
- Open-weight 4B model locally deployable via `pip install transformers` — no API costs, full data privacy for production pipelines
- Prosody manipulation: Fine-grained control over speech rhythm, intonation, and pacing — critical for natural-feeling dialogue rather than robotic monotone
- HuggingFace model hosted at `bosonai/higgs-audio-v3-tts-4b`

## Setup / How to Run (from source)
```bash
pip install transformers
python inference.py --model bosonai/higgs-audio-v3-tts-4b \
  --text 'your text' \
  --emotional 'happy'
```

## Use Cases
1. Generate emotionally directed voiceovers for character content — directly relevant to [[Aiah-Syn]] and AI-driven characters in film
2. Produce cinematic-quality voice work with emotional control — bridges TTS and [[Vocal-Performance]] domains
3. Adapt voice to match character emotional states in production — useful for pre-vis generation and pitch deck creation
4. Fast iteration on voice direction without external talent — reduces production cost/time significantly

## Related to Vault Knowledge Base
- [[Audio-Generation]] — Higgs v3 is a production-grade tool within the AI Audio domain, specifically for speech synthesis
- [[AI-Audio]] — key entry point for text-to-speech workflows in the broader audio generation discipline
- Pre-vis-generation → bridges concept with full emotional content without live recording

## Cross-discipline Connections (from source analysis)
1. **To RealityRowHub**: Direct pipeline tool — Higgs v3's open-weight nature means it can be integrated locally for private production work
2. **Natively complementary to [[NAVA]]**: NAVA generates video+native audio; Higgs adds fine-grained emotional control to the *audio* layer — these two combined cover the AI-native voice + visual pipeline

## Questions For Further Exploration
1. What's the latency/timing resolution of emotional tags? Can you shift emotion mid-word or only at phrase boundaries?
2. Are there pre-trained speaker profiles, or does "speaker adaptation" require few-shot examples per voice profile?
3. Can Higgs v3 generate non-speech audio (breaths, laughs, sighs) alongside dialogue — useful for film scoring / Foley replacement?
4. Is there a ComfyUI node available? This matters for pipeline integration at RealityRowHub.

## Appears In
- [[higgs-audio-v3-source]] — Notion knowledge base entry (2026-06-08), tagged VFX / Github
