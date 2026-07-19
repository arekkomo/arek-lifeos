---
title: "Lucida — Specialist Image Matting and Background Removal"
category: source
summary: MIT-licensed BiRefNet fine-tune for alpha-matte extraction in difficult imagery: transparent objects, camouflage, typography, glow/VFX, and illustrations.
tags: [lucida, image-matting, background-removal, alpha-matte, vfx-compositing, birefnet, rgba]
sources: 1
source_path: https://github.com/egeorcun/lucida
source_date: 2026-07
authors: [Ege Orçun]
ingested: 2026-07-19
updated: 2026-07-19
---

# Lucida — Specialist Image Matting and Background Removal

**Links:** [GitHub](https://github.com/egeorcun/lucida) · [Hugging Face model](https://huggingface.co/egeorcun/lucida) · [Live demo](https://huggingface.co/spaces/egeorcun/lucida-demo) · **License:** MIT

## What it is

Lucida is a BiRefNet-based image matting model designed for situations where generic background removal breaks: semi-transparent glass, camouflaged subjects, text/logos with soft shadows, glow/VFX effects, and illustrations.

## Practical strengths and limits

| Strong fit | Better alternative noted by its benchmark |
|---|---|
| Camouflage, illustrations, text/logos, open-model transparency | InSPyReNet for complex scenes/thin structures; RMBG-2.0 for hair; Ideogram’s commercial API still leads its transparency benchmark |

The repository reports a 191-image, eight-category alpha-MAE benchmark. Treat its comparative claims as author-reported rather than an independent benchmark.

## Integration options

- Python / Transformers inference at recommended 1024² input
- CLI: `bgr remove input.jpg -o output.png --model lucida-v6`
- FastAPI service with `/remove` and `/health`
- RGBA output with optional edge refinement and color decontamination

## Where it fits

Use Lucida for **single-image asset extraction** before compositing—especially source graphics, product shots, VFX glow, logos, and transparent props. For temporally stable multi-frame video mattes, use [[SAM2Matting]] instead.

## Related

- [[Image-Matting-for-VFX]] — selection guide
- [[Stable Layers]] — semantic image decomposition; Lucida supplies pixel-accurate alpha separation for specific foreground/background cuts
- [[Wan-Alpha]] — generates RGBA video natively, avoiding post-generation matting in some cases
