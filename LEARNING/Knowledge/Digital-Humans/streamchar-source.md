---
title: "StreamChar — Alibaba/Personas (Source)"
category: source
summary: Real-time speech-driven character animation framework by Alibaba/Personas for continuous animated avatar streams with synchronized lip motion and dynamic face optimization.
tags: [Digital-Humans, Character-Animation, Speech-Driven, Real-Time, VFX]
sources: 1
updated: 2026-07-03
source_path: raw/notion-export/streamchar-entry.md
source_date: 2026-06
authors: [Alibaba Personas / HUMAIGC]
ingested: 2026-07-03
---

# [[StreamChar]] (Source)

> ⚠️ **Cross-domain breakthrough** — This directly bridges [[Character-Animation]] with [[Speech-Driven-Control]]. Traditional pipelines require keyframe animation + voiceover as separate stages; StreamChar produces continuous animated avatars from audio input in real-time, collapsing the workflow timeline.

## Summary
StreamChar is open-source speech-driven character animation research developed by Alibaba/Personetas (HUMAIIGC) that generates **real-time, continuously animated talking avatars** with synchronized lip motion driven purely by audio input — whether from generated speech, live voice feeds, or pre-recorded audio files.

## Key Claims
1. **Speech-driven continuous animation**: Converts audio → facia/moth facial motion in real-time without per-frame keyframing. The system optimizes face models dynamically during generation rather than using static rigging setups. > Cited from [[StreamChar]]
2. **Real-time streaming capability**: Unlike batch animation pipelines, StreamChar streams animated avatars output can be used for interactive/real-time deployments (virtual production, VTuber pipelines, digital human avatars)
3. **Synced facial motion & lip sync**: The "end-to-end character animation from audio" means lip sync is native to the generation pipeline — no post-hoc LIP syncing required
4. **Published as arXiv paper**: `https://arxiv.org/abs/2605.14470` — peer-reviewed research, not just a product experiment

## Use Cases (from source)
- Generate speech-driven digital humans for interactive content
- Create real-time talking avatar streams for virtual production  
- Sync facial animation to voiceover or live audio feeds
- Build animated character pipelines for real-time rendering

## Setup / How to Run
```bash
git clone git@github.com:humanaigc/StreamChar.git
cd StreamChar
pip install -r requirements.txt
python run.py --audio input.wav --output animation.fbx
```

Key Facts
| Property | Value |
|----------|-------|
| Authors | Alibaba Personas / HUMAIGC |
| Paper URL | https://arxiv.org/abs/2605.14470
| GitHub URL | https://github.com/humanaigc/StreamChar
| Output format | .FBX (animation data) |
| Primary domain | Character Animation / Digital Humans |
| Input formats | Audio (WAV), audio → facial animation mapping

## Related to Vault Knowledge Base
- [[Character-Animation]] — core addition as speech-driven approach bypasses traditional keyframe methods
- [[Digital-Humans]] — StreamChar enables real-time generation of animated talking avatars from voice input  
- [[Voice-Controlled-Avatar]] — bridges [[Vocal-Performance]] with computer graphics pipelines

## Open Questions
1. Does StreamChar support non-humanoid characters or only human faces?
2. What's the output framerate and quality compared to render-based animation?
3. Can it handle multiple speakers (dialogue) in a single audio input, or only one speaker at a time?
4. The arxiv paper — `arxiv.org/abs/2605.14470` should be read for methodology details

## Appears In
- This Notion knowledge base entry (2026-06-08), tagged `VFX, Github`, Type=`Github` as a Research Paper / Open Source tool in the database schema
