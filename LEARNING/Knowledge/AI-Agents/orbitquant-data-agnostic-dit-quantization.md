---
title: OrbitQuant — Data-Agnostic Quantization for Diffusion Transformers
category: concept
summary: Post-training quantization for DiT backbones using a randomized rotated basis that eliminates per-checkpoint, per-timestep calibration data requirements. Tested on FLUX.1, Wan 2.1, and CogVideoX with W2A4 results at usable quality.
tags: [quantization, diffusion-transformer, inference-optimization, ptq, video-generation, image-generation, local-inference]
sources: 1
source_path: arXiv 2607.02461v1
source_date: 2026-07
authors: [Donghyun Lee, Jitesh Chavan, Sam Huang et al.]
ingested: 2026-07-03
updated: 2026-07-03
---

# OrbitQuant

Post-training quantization method for [[DiT]] models that removes the need for calibration data by operating in a normalized, randomized rotated basis.

## Problem

Diffusion transformers require multi-step iterative sampling with growing parameter counts.

Post-training quantization (PTQ) should reduce memory and accelerate inference, but DiTs have a structural mismatch with existing PTQ methods.

Activations shift across three independent dimensions:

Denoising timestep — early steps differ structurally from late steps
Prompt conditioning — same model produces different activation ranges per text input
Classifier-free guidance branches — unconditional vs conditional paths diverge in magnitude

Prior PTQ methods require re-fitting calibration data for every new checkpoint or modality.

## Architecture

### RPBH Rotation

OrbitQuant applies a Randomized Permuted Block-Hadamard rotation to both weights and activations before quantization.

The rotation concentrates each coordinate around one fixed, known marginal distribution regardless of input content.

A single Lloyd-Max codebook then serves all timesteps, prompts, layers, and modality branches of a given input dimension.

### Weight Absorption

Row-wise weight rotation is computed offline and absorbed into the weights during model loading.

Rotation cancels inside each linear layer at runtime. Only a forward activation rotation remains per-step.

This makes the computational overhead purely on the activation path, not the parameters.

## Results (Evaluated Models)

FLUX.1 image generation — sets PTQ state of the art at 4-bit and below
Wan 2.1 video generation — first usable quantized video DiT at W2A4
CogVideoX — matches unquantized quality at W4A8, exceeds prior methods at W2A2

Model transfers from image to video without per-modality tuning or recalibration.

First reported PTQ of any image diffusion transformer to W2A4 with usable sample quality.

## Practical Path for Local [[ComfyUI]] Users

Current local ComfyUI runs typically need 16-bit FP32 weight loading plus BF16 compute buffers.

OrbitQuant enables sub-8-bit inference, cutting GPU memory requirements by half for large models.

For Wan 2.1 14B: ~28 GB VRAM at BF16 → ~14 GB at W4A8 with OrbitQuant PTQ pipeline.

Workflow integration needs weight converter scripts to transform existing checkpoints into rotated-quantized format.

## Relation to Existing Work

> ⚠️ **Context:** [[Helion Kernels]] auto-tunes inference kernels for vLLM serving and diffusion backends. OrbitQuant is complementary — quantization reduces memory footprint, Helion optimizes compute throughput. Both target local deployment efficiency.

No direct contradiction with existing knowledge entries. Method addresses a different bottleneck (memory/weight precision vs kernel compute).

## References

- Paper: https://arxiv.org/abs/2607.02461
- Code: Not yet released at time of scan
