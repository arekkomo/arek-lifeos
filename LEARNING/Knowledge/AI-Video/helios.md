---
title: Helios
category: entity
summary: Real-time long video generation model — 14B parameters running at 19.5 FPS on a single H100, supporting T2V, I2V, V2V up to minute-scale.
tags: [ai-video, real-time, long-video, text-to-video, image-to-video, video-to-video, diffusion-models, github]
sources: 1
updated: 2026-05-09
---

# Helios

**By:** PKU-YuanGroup
**Released:** 2026-03-04
**GitHub:** https://github.com/PKU-YuanGroup/Helios
**Paper:** https://arxiv.org/abs/2603.04379
**Demo:** https://huggingface.co/spaces/BestWishYsh/Helios-14B-RealTime
**Models:** https://huggingface.co/collections/BestWishYsh/helios

---

## What It Is

Helios is a 14B video generation model that achieves 19.5 FPS on a single H100 GPU for real-time long video generation — without standard acceleration tricks (no KV-cache, no causal masking, no quantization). It generates minute-scale videos in a 33-frame autoregressive chunked approach, with strong temporal coherence and no anti-drifting strategies. Three model variants: Base (best quality), Mid (intermediate), Distilled (best efficiency).

---

## Capabilities

- 19.5 FPS end-to-end on a single H100 (up to 20.89 FPS on better hardware)
- Minute-scale video generation (up to ~1449 frames / 60 seconds at 24 FPS)
- Text-to-Video, Image-to-Video, Video-to-Video modes
- Interactive generation mode (experimental)
- Group offloading: runs on ~6GB VRAM
- Context parallelism across multiple GPUs (Ulysses + Ring Attention)
- 4K video support on consumer-grade PC (community tutorial)
- Diffusers, SGLang, vLLM-Omni, Ascend-NPU compatible

---

## VFX / Filmmaking Use Cases

- **Real-time previsualization**: Generate a full 60-second rough-cut quality video in near-real-time for on-set or pre-production review
- **Image-to-video for stills**: Feed a reference image and prompt to generate a video sequence — great for turning concept art or photography into motion
- **Video-to-video stylization**: Run style transfer or shot variation on existing footage at real-time speeds
- **Long-form narrative shots**: Generate minute-length continuous shots — enough for a full scene without cutting
- **Low-VRAM production**: 6GB VRAM with group offloading means this runs on consumer GPUs for test generation
- **Interactive direction**: Use the experimental interactive mode to steer generation in real-time

---

## Requirements

- Python 3.11.2, PyTorch 2.10.0
- CUDA 12.6 / 12.8 / 13.0
- H100 for real-time performance; consumer GPU viable with group offloading (~6GB VRAM)
- Models: Helios-Base, Helios-Mid, Helios-Distilled (HuggingFace / ModelScope)

---

## Quick Start

```bash
git clone --depth=1 https://github.com/PKU-YuanGroup/Helios.git
cd Helios
conda create -n helios python=3.11.2
conda activate helios
pip install torch==2.10.0 torchvision==0.25.0 --index-url https://download.pytorch.org/whl/cu126
bash install.sh
# Download model weights
huggingface-cli download BestWishYSH/Helios-Distilled --local-dir BestWishYSH/Helios-Distilled
cd scripts/inference && bash helios-distilled_t2v.sh
```

---

## Notes

Generates 33 frames per chunk — `num_frames` auto-rounds up to nearest multiple of 33. Achieves speed without standard tricks by rethinking training and inference throughput at the architecture level (enables image-diffusion-scale batch sizes). Comparable to Wan1.3B quality-wise despite being 14B, per their claims. Community YouTube tutorial covers 4K + consumer PC setup.
