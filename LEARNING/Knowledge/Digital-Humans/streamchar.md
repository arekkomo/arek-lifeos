---
title: StreamChar
category: entity
summary: Open-source real-time speech-to-animated-face framework by Alibaba that generates continuous animated avatar output from audio input with native lip-sync and facial motion, eliminating per-frame keyframe animation workflows.
tags: [Character-Animation, Speech-Driven, Real-Time, Digital-Humans, Lip-Sync]
sources: 1
updated: 2026-07-03
---

# StreamChar

> ⚠️ **Contradiction with current VFX workflows** — Existing lip-sync + character animation pipelines (LivePortrait + existing tools like [[WavTTS]]) require multiple sequential steps. StreamChar produces continuous animated avatars from audio input in a single step, eliminating the "audio → lip sync → head rotation → facial expression" chain that currently takes 15–30 minutes per minute of output video.

## What it is
[[StreamChar]] is a speech-driven animation system by Alibaba/Personetas (HUMAIIGC) that converts raw audio input into continuously animated character faces in **real time**. Unlike existing lip-sync tools that produce frozen-head mouth animations, StreamChar dynamically optimizes the entire face geometry during generation — head rotation, eyebrow movement, micro-expressions, and lip articulation are all produced from a single audio stream.

## Why it matters
For [[Digital-Humans]] production pipelines, this collapses 4 separate animation stages (lip-sync → facial expressions → head tracking → jaw motion) into one unified process driven purely by audio. This means a director or producer can run a script through any TTS system (including [[WavTTS]]) and stream the result directly to an animated avatar with professional-quality animation — in real time, without offline processing.

## Key Facts
| Feature | Detail |
|---------|--------|
| **Architecture** | Speech-to-face diffusion model optimized for real-time streaming output |
| **Latency** | Real-time (suitable for live streaming and interactive avatars) |
| **Output format** | .FBX animation data, compatible with Blender, Maya, Unreal Engine |
| **Input** | Audio-only (WAV/MP3), audio stream from TTS engines or voice actors |
| **Animation scope** | Full facial motion — lips, brows, eyes, jaw, head orientation |
| **Training source** | Paper: https://arxiv.org/abs/2605.14470, GitHub: github.com/humanaigc/StreamChar |

## Use Cases for Arek's Workflow
1. **Pre-production avatars** — Script → WavTTS voice → StreamChar animation = fully animated character in seconds rather than manual animation days
2. **Virtual production** — Real-time avatar streams during on-set previs sessions (director sees animated character responding to live dialogue)  
3. **Content pipeline** — RealityRowHub: generate video content with animated characters that have professional facial performance quality
4. **Pitch deck motion** — Animated talking storyboards instead of static reference images

## Cross-Domain Connections
1. [[WavTTS]] + [[StreamChar]] combo = complete voice-to-avatar pipeline. Text or audio input → WavTTS (voice) → StreamChar (animation). Single prompt-to-animated-character workflow.
2. Pre-production use in filmmaking — animated talking characters for pitch reels, concept visualization, and director communication without casting/production.

## Questions For Further Exploration
1. Does StreamChar support stylized/non-humanoid characters or only realistic human faces?
2. Minimum audio input duration per generation pass?
3. Can it be run locally on DGX Spark with ComfyUI integration or does it require cloud inference?
4. Output framerate and temporal stability over long sequences (for video content, not just single shots)?

## Appears In
- Notion dtb Knowledge database entry (2026-06-08), tagged `VFX, Github`, Type=`Github`
- Source: https://github.com/humanaigc/StreamChar