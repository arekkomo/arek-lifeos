---
title: "StatLUT — AI-Generated 3D LUTs for Multimodal Color Grading"
category: concept
summary: Transformer-based framework that generates photorealistic 3D LUTs from reference images or text prompts using Lab-color statistical features and a lightweight diffusion DiT, enabling AI-driven color grading in DaVinci Resolve workflows.
tags: ["color-grading", "3D-LUT", "style-transfer", "davinci-resolve", "diffusion-transformer", "lab-color-space"]
sources: 1
updated: 2026-07-11
---

# StatLUT — Multimodal 3D LUT Generation

| Detail | Value |
|--------|-------|
| arXiv ID | 2607.08227v1 [cs.CV] |
| Published | 2026-07-09 |
| Authors | Yifan Wang, Zhixiang Hao, Yu Wang, Congchao Zhu |
| Papers | 17 pages, 9 figures, 7 tables |

## The Problem

Photorealistic style transfer (PST) aims to transfer the color and tonal style of a reference
image to content while preserving structural integrity. Existing methods suffer from:

- **Semantic entanglement** — pretrained image encoders conflate structure with color, causing
  spatial distortions when extracting style features
- **Color gamut violations** — pixel-level mappings ignore 3D color topology, producing banding
  and clipped highlights/shadows
- **Single-modality lock-in** — most tools require a reference image; text-driven grading is rare

## StatLUT Pipeline

Three-stage design that bypasses traditional CNN/ViT encoders entirely:

### 1. Lab-Extractor — Statistical Feature Decoupling

Converts the reference image into CIE-Lab color space, then extracts spatially-agnostic
statistical features (mean, variance, higher moments of L/a/b channels). This fundamentally
decouples color distribution from structural semantics — no encoder weights to entangle edge
information with tone.

### 2. MR-Mapper — Transformer Seq2Seq LUT Synthesis

Formulates 3D LUT generation as a sequence-to-sequence translation task. A multi-dimensional
residual mapper processes the statistical features and predicts topologically smooth 17×17×17
cube maps (standard Resolve format). The residual structure enforces continuity across the
color volume, preventing discontinuities that cause banding.

### 3. H-Diffuser — Text-Driven Color Grading via DiT

A lightweight Diffusion Transformer that synthesizes statistical features directly from
natural language prompts (e.g., "desaturated teal/orange cinema look" or "high-contrast film
negative stock"). Enables text-guided grading without a reference image. Uses flow matching
instead of DDPM-style denoising for faster convergence.

## Results

Reports SOTA on standard PST benchmarks across both qualitative visual assessment and
quantitative metrics (LPIPS, SSIM delta). Key claim: maintaining structural fidelity while
achieving stronger style transfer than encoder-based baselines.

## Practical Relevance

**DaVinci Resolve workflows:** The generated 17×17×17 LUTs are directly importable into
[[davinci-resolve]] Color pages as custom Look nodes — no conversion needed, since the output
is already a standard .cube file format. This enables rapid look exploration: generate variants
from text prompts, test in Resolve, iterate without manual node construction.

**ComfyUI integration path:** If packaged as a ComfyUI custom node, H-Diffuser could produce
LUT files from generation-side text prompts, creating an automated color-grading step at the
end of AI video pipelines (after Wan2.2 or LTX-2.3 generation, before delivery).

**VFX compositing:** The Lab-Extractor approach is applicable to scene-matching for VFX —
extract statistical features from plate footage, feed into MR-Mapper to produce corrective LUTs
for CG elements that match the shot's tonal profile.

## Related

- [[davinci-resolve]] — primary grading destination in Blackmagic's post-production suite
- [[comfyui-ocio-color-management]] — OpenColorIO/ACES integration for ComfyUI pipelines
- [[ultraimagegen-hierarchical-local-attention]] — encoder-free feature extraction patterns
- [[gimbal-diffusion-gravity-aware-camera-control]] — camera control in video gen; StatLUT handles the color side of cinematic language
