---
title: Bernini
category: entity
summary: ByteDance unified video generation framework combining MLLM-based semantic planner with DiT renderer — text/image-to-video and video editing.
tags: [ai-video, video-generation, video-editing, diffusion-models, byte-dance]
sources: 1
updated: 2026-06-07
---

# Bernini

**By:** ByteDance (Chenchen Liu*, Junyi Chen*, Lei Li*, Lu Chi, Mingzhen Sun, Zhuoying Li, Yi Fu, Ruoyu Guo, Yiheng Wu, Ge Bai, Zehuan Yuan)
**Released:** Paper 2026-05-22 / Code + weights open 2026-06-01
**GitHub:** https://github.com/bytedance/Bernini
**Paper:** https://arxiv.org/abs/2605.22344
**Models:** https://huggingface.co/ByteDance/Bernini
**Project Page:** https://bernini-ai.github.io/

---

## What It Is

Bernini is a unified video generation and editing framework that combines an MLLM-based semantic planner with a DiT-based renderer. Instead of directly mapping text prompts to video, it first decomposes the prompt into structured semantic representations using a large multimodal language model, then renders the video using a diffusion transformer. This two-stage approach enables more controllable and semantically coherent video generation and editing.

On video editing benchmarks, Bernini reaches first tier among leading closed-source commercial models (per their self-built arena platform with human annotators).

---

## Key Architecture

### Semantic Planner (MLLM)
- Interprets the user prompt into structured semantic representations
- Can handle complex multi-step descriptions
- Uses optional OpenAI-compatible endpoint for prompt enhancement

### DiT Renderer (Bernini-R)
- Diffusion transformer-based generation engine
- Built on Wan2.2 base model
- Supports multiple task types: text-to-image, image-to-image, text-to-video, video-to-video

---

## Capabilities

- Multi-modal generation: text-to-image, image-to-image, text-to-video, video-to-video
- Video editing: add/remove elements, modify style, change content while preserving motion structure
- Semantic control: precise control over scene composition through structured representations
- Flexible inference: single-GPU or multi-GPU (Ulysses sequence parallel)
- Diffusers format: self-contained model bundles on HuggingFace

---

## VFX / Filmmaking Applications

- Semantic-driven pre-vis: Generate storyboards/plates from detailed narrative descriptions
- Scene modification: Edit existing footage (change elements, environments, props) without reshoot
- Storyboard-to-video pipeline: Convert written scene descriptions into animated sequences
- Commercial concept prototyping: Rapid visual concept validation for client pitches
- Style reference transfer: Apply reference video aesthetics to other footage via editing tasks

---

## Quick Start

```bash
git clone https://github.com/bytedance/Bernini.git bernini && cd bernini
pip install -r requirements.txt
hf download ByteDance/Bernini-R-Diffusers --local-dir Bernini-R-Diffusers
python infer_single_gpu.py --config Bernini-R-Diffusers --case assets/testcases/t2v/t2v.json
```

---
