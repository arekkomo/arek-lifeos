---
title: "DramaDirector — Geometry-Guided Short Drama Generation"
category: source
summary: Geometry-grounded framework for plot-to-short-drama video generation using cinematographic depth-pose references, GRPO alignment training, and multi-shot storyboard consistency. Includes DramaBoard benchmark with 81K shots from 35 live-action dramas.
tags: [short-drama, video-generation, ai-filmmaking, geometry-guided, ai-video]
sources: 1
source_path: arxiv.org/abs/2606.24107
source_date: 2026-06
authors: [Hengji Zhou, Sijie Liu, Jianrun Chen, Xingchen Zou, Lianghao Xia]
ingested: 2026-06-29
updated: 2026-06-29
---

# DramaDirector — Geometry-Guided Short Drama Generation

**arXiv:** [2606.24107](https://arxiv.org/abs/2606.24107)
**Published:** 2026-06-23 | **Categories:** cs.CV, cs.AI
**Authors:** Hengji Zhou et al. (iLearn Lab)

## Problem Statement

Short dramas demand rapid shot rhythms, dialogue-driven focus shifts, and cinematographic grounding. Standard text-to-video pipelines using prompt-only conditioning struggle with multi-shot coherence, character consistency across scenes, and director-level camera control.

## Architecture

DramaDirector decouples each shot into static visual conditions (blocking, lighting, composition) and dynamic narrative conditions (pacing, emotion, action).

Pipeline stages:

1. **Plot parsing** — Global plot + local context fed to planner module
2. **Schema-constrained SFT** — Planner trained via supervised fine-tuning under schema constraints for storyboard generation
3. **GRPO alignment under text-visual reward** — Reinforcement training aligns visual output with textual intent
4. **Depth-pose gallery retrieval** — Reference library of real short-drama shots indexed by camera depth and actor pose
5. **First-frame generation + image-to-video synthesis** — Retrieved geometry guides both conditions

## DramaBoard Benchmark

- 35 live-action dramas, 2.8K episodes, 81K shots
- Structured storyboards with multi-dimensional evaluation protocols
- Measures faithfulness, consistency, and controllability dimensions

## Practical Relevance

First systematic approach to plot-driven multi-shot video generation in [[ai-video-generation]] — moves beyond single-clip synthesis toward structured narrative output. The depth-pose retrieval gallery concept is directly applicable to DaVinci Resolve previsualization: reference real cinematography for AI-shot composition, then use image-to-video diffusion for final frames. Workflow-compatible with [[comfyui-v026-kling-v3-turbo]] if gallery references node is added.

## Results

Improves over representative multi-agent and single-prompt video baselines on all three dimensions (faithfulness, consistency, controllability). Architecture released with source code at https://github.com/iLearn-Lab/DramaDirector.

## Related Work

- [[freestory-character-consistency]] — Character consistency in free-form visual storytelling via entity-grounded feature reuse
- [[drama-director-short-drama-gen]] — Same paper (index cross-ref)
- [[free-story-character-consistency]] — Adjacent problem: character grounding without geometry control

## References

1. Hengji Zhou, Sijie Liu, Jianrun Chen, Xingchen Zou, Lianghao Xia. "DramaDirector: Geometry-Guided Short Drama Generation." arXiv:2606.24107, 2026-06-23.
