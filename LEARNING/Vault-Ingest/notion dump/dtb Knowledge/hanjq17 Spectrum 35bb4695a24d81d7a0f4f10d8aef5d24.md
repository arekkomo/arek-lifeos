# hanjq17/Spectrum

Tags: AI Image, AI Video, Diffusion Models, Github
Description: Training-free diffusion sampling accelerator via Chebyshev polynomial feature forecasting — up to 4.79x speedup on FLUX, 4.67x on Wan2.1-14B. CVPR 2026.
URL: https://github.com/hanjq17/Spectrum
Date Added: May 9, 2026 4:37 PM
Type: Github
Archive: No
Spark: No

## About

Spectrum accelerates diffusion model inference without any training. It forecasts denoiser latent features using Chebyshev polynomial approximation (ridge regression), skipping full network passes for multiple steps while keeping error bounds that don't compound with step size.

**GitHub:** [https://github.com/hanjq17/Spectrum](https://github.com/hanjq17/Spectrum)

**Paper:** [https://arxiv.org/abs/2603.01623](https://arxiv.org/abs/2603.01623)

**Project:** [https://hanjq17.github.io/Spectrum/](https://hanjq17.github.io/Spectrum/)

## Capabilities

- Up to 4.79x speedup on FLUX.1-dev; 4.67x on Wan2.1-14B
- Supports: FLUX.1, SD3.5-Large, SDXL, HunyuanVideo, Wan2.1-14B
- Training-free — works on any pre-trained diffusion model
- ComfyUI community implementations available (SDXL, FLUX, HunyuanVideo, Wan2.2)
- Multi-GPU parallel inference support

## VFX / Filmmaking Use Cases

- Cut Wan2.1-14B or HunyuanVideo generation time by ~4-5x for faster shot iteration
- Generate 4-5x more FLUX image variants in the same time budget for storyboard exploration
- Drop-in wrapper for existing pipelines — no retraining or model changes needed
- Plug into ComfyUI workflows via community nodes as a transparent acceleration layer

## Requirements

- Python 3.10, PyTorch, transformers, diffusers, hydra-core
- Models from HuggingFace downloaded separately

## How to Run

```
conda create -n spectrum python=3.10 && conda activate spectrum
pip install -r requirements.txt
CUDA_VISIBLE_DEVICES=0 python src/text_to_image.py model=flux algo=spectrum algo.w=0.5 window_size=2 flex_window=0.75
```

## Notes

flex_window (alpha) controls speedup — larger = faster, lower quality. algo.w=1.0 is pure Chebyshev; 0.5 mixes with linear interpolation for robustness. CVPR 2026. Stanford + ByteDance.