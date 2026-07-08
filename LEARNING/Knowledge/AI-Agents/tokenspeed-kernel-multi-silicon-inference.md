---
title: "TokenSpeed-Kernel — Portable APIs for Multi-Silicon LLM Inference"
category: source
summary: Kernel registration/selection API decouples inference runtime from
  hardware-specific implementations, enabling GPT-OSS 120B deployment across
  AMD and NVIDIA silicon without code changes. Gluon (AMD path) achieves
  1.6-3.6x throughput on MI355X via XCD scheduling logic for decode-phase
  kernels. CuteDSL covers the NVIDIA path, Triton provides broad fallback
  coverage. Adopted by vLLM as tokenspeed-kernel-amd package, relevant for
  multi-silicon video diffusion serving backends beyond LLM inference.
tags: [inference-kernels, portability, gluon, triton, tokenspeed, amd, nvidia,
  vllm]
sources: 1
updated: "2026-07-04"
source_path: https://pytorch.org/blog/lightseek-tokenspeed-kernel/
source_date: "2026-06"
authors: ["AMD Triton Team", "TokenSpeed Contributors"]
ingested: "2026-07-04"
---

# TokenSpeed-Kernel: Portable APIs for Multi-Silicon LLM Inference

**Source:** PyTorch Blog (June 2026) | AMD/Triton/TokenSpeed Collaboration

## Problem Statement

LLM inference kernels determine latency, throughput, and hardware efficiency.
Previous approaches scattered platform-specific tuning through model code or
maintained separate codebases per vendor -- making cross-platform deployment
and maintenance expensive. The trade-off between portability (code runs anywhere)
and performance (each silicon target is optimized for its architecture) remained unresolved at scale.

## Registry + Selection Architecture

TokenSpeed-Kernel introduces a registration API with a selection layer that picks
the optimal kernel implementation based on hardware detection at initialization
time. The same inference runtime calls an identical kernel interface regardless
of whether the accelerator is AMD MI355X, NVIDIA H200, or another target.
Platform-specific work (Gluon for AMD CDNA3/4, CuteDSL for NVIDIA) stays behind that API boundary; Triton serves as a portable fallback where 
vendor-optimized kernels are unavailable.

- **Portable Triton paths** cover broad silicon without per-vendor maintenance overhead
- **Gluon (AMD)** achieves 1.6-3.6x end-to-end throughput improvement on MI355X for GPT-OSS 120B; kernel-level attention is 1.4-2.3x faster than 
Triton baseline and 1.1-1.3x faster than AITER (AMD's previous dedicated kernel backend)
- **CuteDSL (NVIDIA)** provides hand-tuned paths where maximum throughput matters
- **Vendor wrappers** plug in third-party optimized libraries when they outperform all internal options

The approach is additive: new models deploy quickly using portable kernels, then teams selectively replace individual operations with 
platform-specific optimizations without re-architecting the runtime.

## Gluon Details: XCD Scheduling for Decode Phase

Gluon extends Triton's programming model with explicit memory scheduling while preserving block-level simplicity. The critical innovation for 
video diffusion relevance lies in persistent kernel patterns with XCD (Cross-Cache-Dimension) scheduling logic -- tiles become visible through 
user-controlled timing, then rotate through buffers as different schedules execute. This matters because decode-phase kernels (the bottleneck 
for autoregressive generation and denoising step latency) depend on hiding memory latency while keeping matrix cores occupied, without pushing 
pipeline details into the inference runtime layer.

## Practical Implications for Video Diffusion Serving

Video diffusion models run long denoising loops with transformer attention blocks
per timestep. Kernel-level optimization of QK/PV computation, online softmax, and
residual projection directly impacts per-step latency in ComfyUI pipelines. TokenSpeed-
Kernel's approach to hardware abstraction complements [[Helion vLLM Kernels]], which
take an auto-tuning strategy (compiler searches over tile sizes) rather than manual
optimization-through-regeneration. Both aim for multi-silicon portability through API
abstraction layers but use different optimization strategies: Helion automates tuning,
TokenSpeed prioritizes expert-authored kernel selection by hardware capability.

[[ComfyUI v0.27]] introduces native int8 convolution support. Applied with optimized
kernel backends like TokenSpeed-Kernel, local diffusion inference on AMD MI300X GPUs
gains both quantization efficiency and kernel throughput -- relevant for the DGX Spark
environment documented in [[ComfyUI Compendium]]. TokenSpeed-Kernel deployment on
AMD hardware provides a path beyond NVIDIA-only serving clusters.

**Cross-reference with related work:** Gluon's explicit scheduling model shares
concerns with [[OrbitQuant]], which addresses numerical alignment for DiT models
via data-agnostic quantization. Both tackle the problem of matching kernel expectations
to actual weight layouts, though OrbitQuant focuses on calibration-free codebook
construction while TokenSpeed targets execution throughput.

**Training-free acceleration complement:** [[AdaCluster]] provides adaptive sparse
attention that reduces KV cache pressure during inference without retraining. Running
AdaCluster alongside a Gluon-optimized kernel stack would yield compounding latency
reduction -- AdaCluster cuts attention compute, Gluon accelerates whatever remains.

> **Reproduction note:** RadixArk reports the 1.6-3.6x Gluon throughput gains for
GPT-OSS 120B on MI355X under their internal benchmarking conditions. As of ingest
date (2026-07-04), no independent reproduction from third-party testing has been
published. Community verification would strengthen the performance claim, especially
for smaller models where kernel overhead dominates batch throughput.
