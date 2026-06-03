---
title: Spectrum
category: entity
summary: Training-free diffusion sampling accelerator using spectral Chebyshev polynomial feature forecasting — up to 4.79x speedup on FLUX, 4.67x on Wan2.1-14B.
tags: [ai-video, ai-image, diffusion-models, inference-acceleration, flux, wan, hunyuanvideo, github]
sources: 1
updated: 2026-05-09
---

# Spectrum

**By:** Stanford University / ByteDance (Jiaqi Han, Juntong Shi, Puheng Li, Haotian Ye, Qiushan Guo, Stefano Ermon)
**Released:** CVPR 2026
**GitHub:** https://github.com/hanjq17/Spectrum
**Paper:** https://arxiv.org/abs/2603.01623
**Demo:** https://hanjq17.github.io/Spectrum/

---

## What It Is

Spectrum is a training-free method that accelerates diffusion model inference by forecasting denoiser features using Chebyshev polynomial approximation (ridge regression). Instead of running the full denoiser every step, it predicts latent features for multiple future steps from past observations — achieving large speedups with tightly controlled error bounds that don't compound with step size.

---

## Capabilities

- Training-free: works on any pre-trained diffusion model without fine-tuning
- Up to 4.79x speedup on FLUX.1-dev (image generation)
- Up to 4.67x speedup on Wan2.1-14B (video generation)
- Supports: FLUX.1, SD3.5-Large, SDXL, HunyuanVideo, Wan2.1-14B
- Community ComfyUI implementations available (SDXL, FLUX, HunyuanVideo, Wan2.2)
- Multi-GPU parallel inference support

---

## VFX / Filmmaking Use Cases

- **Faster batch video generation**: Cut Wan2.1-14B or HunyuanVideo generation time by ~4-5x — useful when iterating on shot compositions or style tests
- **Rapid concept iteration**: Generate 4-5x more FLUX image variants in the same time budget when developing visual references or storyboards
- **Production throughput**: Apply as a drop-in wrapper to existing pipelines running FLUX or Wan — no retraining, no model changes
- **ComfyUI integration**: Plug directly into existing ComfyUI workflows via community nodes — transparent acceleration layer
- **Cost reduction on cloud GPU**: Same quality output, ~4x fewer compute cycles per generation on commercial API or GPU rental

---

## Requirements

- Python 3.10, PyTorch, transformers, diffusers, hydra-core
- Models downloaded separately from HuggingFace (FLUX, SD3.5, SDXL, HunyuanVideo, Wan2.1-14B)
- Multi-GPU recommended for video generation

---

## Quick Start

```bash
conda create -n spectrum python=3.10
conda activate spectrum
pip install -r requirements.txt

# FLUX image generation example
CUDA_VISIBLE_DEVICES=0 python src/text_to_image.py \
    model=flux algo=spectrum \
    algo.w=0.5 algo.lam=0.1 algo.m=4 \
    window_size=2 flex_window=0.75 \
    ngpu=1 total_prompt_num=1000 \
    prompt_file=prompts/DrawBench200.txt
```

---

## Notes

Key hyperparameters: `window_size` (initial window N), `flex_window` / alpha (controls how many steps are skipped — larger = more speedup, lower quality). `algo.w=1.0` = pure Chebyshev predictor; `0.5` mixes with linear interpolation for robustness. `algo.m=4` Chebyshev bases is default. CVPR 2026 paper. Follow-up to CHORDS (ICCV 2025) by same team.
