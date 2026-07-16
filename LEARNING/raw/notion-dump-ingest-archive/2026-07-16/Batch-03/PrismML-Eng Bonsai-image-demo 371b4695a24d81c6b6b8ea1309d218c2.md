# PrismML-Eng/Bonsai-image-demo

Tags: AI Image, Diffusion Models, Github
Description: First image generation model to run on iPhone — 1-bit and ternary FLUX.2 Klein 4B compressed to 0.93–1.21 GB, 6–8× smaller with 88–95% quality retention. Apache 2.0.
URL: https://github.com/PrismML-Eng/Bonsai-image-demo
Date Added: May 31, 2026 11:06 AM
Type: Github
Archive: No
Spark: No

## About

Bonsai Image 4B compresses FLUX.2 Klein 4B into 1-bit and ternary weight formats for on-device image generation on iPhone, iPad, Mac, and NVIDIA GPU. Apache 2.0.

**GitHub:** [https://github.com/PrismML-Eng/Bonsai-image-demo](https://github.com/PrismML-Eng/Bonsai-image-demo)

**Models:** [https://huggingface.co/collections/prism-ml/bonsai-image](https://huggingface.co/collections/prism-ml/bonsai-image)

**Project:** [https://prismml.com/news/bonsai-image-4b](https://prismml.com/news/bonsai-image-4b)

## Models

| Variant | Transformer | Reduction | Quality |
| --- | --- | --- | --- |
| 1-bit | 0.93 GB | 8.3× | 88% |
| Ternary | 1.21 GB | 6.4× | 95% |

## Capabilities

- On-device: iPhone 17 Pro Max, iPad, Mac, NVIDIA GPU
- 512×512 in ~6s on Mac M4 Pro (5.6× faster than MFLUX)
- macOS (MLX), NVIDIA (gemlite+HQQ), Windows (triton-windows)
- Apache 2.0 open weights + code

## VFX / Filmmaking Use Cases

- Generate reference images and mood boards on-device, private and instant
- Run locally on DGX Spark without cloud dependency

## How to Run

```bash
./setup.sh
./scripts/download_model.sh ternary
./scripts/generate.sh --prompt "An icy Bonsai tree."
```