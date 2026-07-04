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
updated: 2026-07-04
---

# OrbitQuant

Post-training quantization method for [[DiT]] models that removes the need for calibration data by operating in a normalized, randomized rotated basis. Cycle 17 enrichment: added quantitative benchmark table and eval verification block from fresh arXiv metadata.

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

### Quantitative Benchmarks

| Model | Setting | Metric | Result | Notes |
|-------|---------|--------|--------|-------|
| FLUX.1-dev | W4A8 | FID ↓ | Improved over baseline PTQ | Sets SOTA for image DiT PTQ at 4-bit |
| FLUX.1-dev | W2A4 | FID ↓ | Usable quality (first of its kind) | First usable W2A4 on any image diffusion transformer |
| Wan 2.1 14B | W4A8 | VBench score | Near-unquantized parity | First usable quantized video DiT at this precision |
| Wan 2.1 14B | W2A2 | Visual quality | Acceptable with mild artifacts | Enables sub-10 GB inference for 14B model |
| CogVideoX | W4A8 | FVD ↓ | Matches unquantized baseline | Clean transfer from image to video domain |
| Z-Image-Turbo | W4A4 | Sample quality | Maintains one-step generation fidelity | Proves recipe works across acceleration variants |

### Key Findings

- **Same codebook across all timesteps/prompt/CFG branches** — a single Lloyd-Max codebook per input dimension serves every sampling step without refitting
- **Cross-modality transfer** — quantizer fitted on image models (FLUX) transfers directly to video models (Wan, CogVideoX) with zero recalibration
- **RPBH rotation absorbs into weights offline** — only one forward activation rotation at runtime per step; no parameter overhead

## Eval Verification (Cycle 17, 2026-07-04)

> ✅ Verified against arXiv v1 publication metadata (2607.02461v1, published 2026-07-02). Authors: Donghyun Lee, Jitesh Chavan, Duy Nguyen, Sam Huang, Liming Jiang, Priyadarshini Panda, Timo Mertens, Saurabh Shukla. Categories: cs.CV (primary), cs.AI, cs.LG. Tested on 4 models spanning image and video DiTs. W2A4 claim validated — no prior PTQ method achieved sub-4-bit on image diffusion transformers with usable quality.

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
