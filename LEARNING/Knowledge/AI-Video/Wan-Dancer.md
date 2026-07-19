---
title: "Wan-Dancer — Minute-Scale Music-to-Dance Video"
category: source
summary: Wan-based hierarchical system that generates coherent 720p/30fps dance video beyond one minute from a reference image, full music track, and dance-style prompt.
tags: [wan-dancer, music-to-dance, dance-video, audio-conditioned-video, long-form-video, wan2-1]
sources: 1
source_path: https://github.com/Wan-Video/Wan-Dancer
source_date: 2026-07
authors: [Mingyang Huang, Peng Zhang, Li Hu, Guangyuan Wang, Ruoshi Zhang, Yi Lu, Gang Cheng, Bang Zhang]
ingested: 2026-07-19
updated: 2026-07-19
---

# Wan-Dancer — Minute-Scale Music-to-Dance Video

**Links:** [GitHub](https://github.com/Wan-Video/Wan-Dancer) · [Project](https://humanaigc.github.io/wan-dancer-project/) · [Paper](https://arxiv.org/abs/2607.09581) · [Hugging Face 14B](https://huggingface.co/Wan-AI/Wan-Dancer-14B) · **License:** Apache 2.0

## What it does

Wan-Dancer creates long, rhythmically synchronized dance videos from:
- a **reference image** (performer identity / appearance)
- a **music track** (full-track rhythm and structure)
- a **dance-style prompt** (released examples: Chinese classical, K-pop, street, tap, Latin)

It targets output beyond one minute at 720p / 30fps, addressing the usual long-video failures: drift, identity changes, repetitive movement, and loss of musical structure.

## Method in one line

**Global keyframe planning** uses the entire music track for long-range structure; **local temporal refinement** creates the final high-resolution motion between those planned beats.

Reported technical elements: time-mapped RoPE for dynamic frame-rate alignment, optical-flow loss for motion continuity, and motion-speed control for detail retention during fast movement.

## Practical status

- Code + 14B model released
- Two scripts: `gen_video_global.sh` then `gen_video_local.sh`
- Reference environment is intensive: Ubuntu 22.04, CUDA 12.4, and 8× A800 80GB for the reported setup. Treat local use on the DGX Spark as unverified.

## Where it fits

Use it for music-video concepts and dance-led character shots where **a whole song segment needs one coherent movement arc**. It is a rendered video generator, unlike [[HY-Motion-1.0]] and [[ARDY]], which generate reusable skeletal motion data.

## Related

- [[Long-Form-Music-Conditioned-Video]] — architecture pattern
- [[HY-Motion-1.0]] — text-to-3D motion counterpart
- [[ARDY]] — interactive constraint-driven skeletal motion counterpart
- [[Suno Music Style Tags Guide]] — source-side music/style vocabulary for planning a music-video input
