---
title: "PyTorch 2.13 Release & RSS Scan — July 2026 Infrastructure Briefing"
category: source
summary: PyTorch 2.13 release notes and PyTorch blog RSS scan (Jul 2–10, 2026) covering FlexAttention on MPS, CuTeDSL backend, normalization fusion, Monarch on ROCm, Miles RL stack, TokenSpeed-Kernel, and ExecuTorch edge AI hackathon — filtered for ComfyUI/diffusion/VFX relevance.
tags: [pytorch, framework, performance, flexattention, cutedsd, normalization, distributed-training, execitorch, sglang]
source_path: /tmp/pytorch_rss.xml (RSS feed scrape, Jul 10 2026)
source_date: 2026-07
authors: [PyTorch Blog Team, Meta, AMD, Qualcomm]
ingested: 2026-07-10
updated: 2026-07-10
---

# PyTorch RSS Scan — July 2026 (Cycle 30)

> **Scope:** PyTorch blog RSS feed, Jul 2–10 2026 window. 10 articles extracted. HF Blog RSS and Google AI RSS both returned HTTP 404 HTML pages (feed URLs dead/blocked). arXiv API and Semantic Scholar blocked with 429 rate limits.

---

## PyTorch 2.13 Release Notes (Jul 8, 2026)

3,328 commits from 526 contributors. Live Q&A scheduled Jul 22. Key features organized by relevance to **[[ComfyUI]]** / diffusion inference workflows:

### ⭐ High Relevance — Directly Affects Diffusion/Video Inference

#### FlexAttention on Apple Silicon (MPS)

FlexAttention lands on Metal/MPS with hand-written Metal kernels for sparse prefill and decode paths. **Benchmark highlights:**
- 1×8×32768×64 shape, 256-element sliding window (0.8% density): **35ms vs 431ms SDPA (~12.3x speedup)**
- 8192-length / 64-window case: **~4.15x speedup**
- Dense patterns still favor SDPA as expected

Why this matters: Attention is the bottleneck in video diffusion transformers (Wan, CogVideoX, LTX). Sparse attention patterns (sliding window, causal masks) are common in autoregressive video generation. Apple Silicon users running ComfyUI get a meaningful inference boost for long-sequence workloads.

#### CuTeDSL "Native DSL" Backend for Inductor

CuTeDSL gives `torch.compile` a second high-performance code path alongside Triton — specifically targeting **GEMM** and **RMSNorm**, two of the most performance-critical operations in transformer training/inference. Kernels move from thread pool to subprocess pool, eliminating GIL bottleneck during compilation.

Why this matters: ComfyUI models compiled with `torch.compile` benefit from CUTLASS-grade kernel quality without manual Triton programming. Faster cold-start compilation times.

#### Normalization Fusion ("Towards Free Normalization")

Fuses LayerNorm/RMSNorm into adjacent GEMM kernels, hiding up to **90% of normalization latency** through compute overlap. Multi-CTA (compute thread agent) patterns for broader fusion coverage.

Why this matters: Diffusion transformers stack dozens of layers — each with RMSNorm/LayerNorm. Hiding normalization in GEMM means more FLOPs on actual model computation per token/latent step.

#### Deterministic Backward for FlexAttention Flash Backend

Replaces atomic operations in dQ accumulation with pre-computed write ordering. Bit-for-bit reproducible gradients at <1% overhead. Opt-in via `torch.use_deterministic_algorithms(True)`.

Why this matters: Reproducibility for research workflows and regression testing when tuning video generation pipelines. Not critical for inference-only ComfyUI usage.

#### nn.LinearCrossEntropyLoss (Fused Linear + CrossEntropy)

Reduces peak memory by **up to 4x** for large-vocabulary models by processing vocabulary dimension in chunks, never materializing full logits matrix. Drop-in replacement — no code changes needed.

Why this matters: Relevant if fine-tuning language models used alongside video pipelines (e.g., text encoders, reward models for RLHF). Memory headroom on consumer GPUs.

#### Native Safetensors Loading

`torch.load("model.safetensors")` now works natively — auto-detects format, returns tensors directly. Removes separate library dependency.

Why this matters: **Direct impact on ComfyUI** — most diffusion models distribute weights in safetensors format. Eliminates one dependency in minimal setups.

#### Large MPS Op Migration to Native Metal

Broad set of ops migrated from Apple's MPSGraph framework (which adds per-op compile overhead) to hand-written Metal kernels: copy/cast, random generation, comparisons, reductions, cumsum/cumprod, sort, embedding backward, scatter/gather.

Why this matters: Reduces kernel launch latency on Apple Silicon for training and inference workloads. Complements FlexAttention MPS support above.

### Medium Relevance — Infrastructure/Platform

#### torchcomms Backend

New distributed communications backend replacing c10d. Improved fault tolerance (graceful timeout, partial-group recovery), better scalability, structured logging. Maintains API compatibility.

#### FSDP2 Separate Reduce-Scatter Group

Opt-in dedicated NCCL communicator for reduce-scatter allows AG/RS overlap. Improves throughput for fully-sharded training without model code changes.

#### Python 3.15 Support + Free-threaded (3.15t)

Linux binaries available via download.pytorch.org. No Windows/macOS yet. `torch.compile` not supported on 3.15 still. Beta until October 2026 stable release.

#### CUDA 13.0 Default Build

CUDA 13.0 is now the default build target. CUDA 12.8/12.9 removed from wheels. Triton pinned to 3.7.1. oneDNN upgraded to v3.12.

#### ExecuTorch Integration into PyTorch Core

On-device inference becomes first-class capability. Previously a separate project; now part of main PyTorch distribution.

### Deprecations

- **Named tensors removed** (`Tensor.names` and associated APIs) — hard removal
- **Distributed collectives renamed**: `all_gather_into_tensor` → `all_gather_single`, `reduce_scatter_tensor` → `reduce_scatter_single` (old names remain as deprecated wrappers with FutureWarning)
- **Bazel build removed**

---

## Other Notable RSS Articles (Jul 2–10, 2026)

### PyTorch Monarch on ROCm: Fault-Tolerant Distributed Training (Jul 6)

PyTorch Monarch (single-controller distributed runtime with actor-based supervision trees) ported to AMD GPUs via ROCm. Tested with TorchTitan + TorchFT on:
- **16-node SLURM MI300 cluster (128 GPUs):** Llama 3 8B with injected RCCL failures every 180s — training continued seamlessly, loss converged normally
- **32-node Kubernetes MI355 cluster (256 GPUs):** Stable recovery with smooth loss from 12 to ~4

Key insight: Checkpoint-less fault tolerance via peer-to-peer state transfer between replicas instead of full checkpoint reload. Recovery completes in seconds for local restart, minutes only if escalated. Relevant context: distributed training on AMD hardware is production-ready now.

### Miles: PyTorch-Native Stack for LLM RL Post-Training (Jun 30)

End-to-end RL pipeline (PPO, GRPO, REINFORCE) built on native PyTorch distributed primitives instead of separate frameworks. Designed for large-scale post-training workflows where training and RL loops coexist in one cluster. Relevance to video generation: diffusion RLHF papers (like [[Selective Timestep Weighting]]) could theoretically leverage this stack.

### TokenSpeed-Kernel: Multi-Silicon LLM Inference (Jul 25)

Portable APIs + high-performance kernels for deploying LLM inference across CUDA, ROCm, and Apple Silicon with a unified kernel interface. Relevant if running text encoders (CLIP, T5) as part of ComfyUI workflows on mixed hardware.

### DeepSeek-V4 on GB300 with SGLang (Jul 23)

**5x higher throughput at the same interactivity** serving DeepSeek-V4 on NVIDIA GB300 via SGLang. Optimization focuses on KV cache management + speculative decoding. Less directly relevant to video diffusion but demonstrates inference optimization patterns applicable to any large transformer serving.

### ExecuTorch Hackathon Winners (Jul 2)

Three edge-AI projects stood out for their emphasis on why local execution matters:
1. **SafeScreen AI** — On-device visual content safety layer (blur/redact harmful media locally)
2. **SixthSense** — Haptic vision assistive wearable for blind users (phone camera → directional vibrations via ExecuTorch object detection + depth estimation)
3. **Toddle AI** — Privacy-first toddler gait analysis app (local pose estimation, no video leaves device)

Relevance: Demonstrates the trend toward on-device generative AI. [[MobileWan]] shows server-scale video models already running at 16 FPS on mobile hardware; ExecuTorch makes this pipeline more accessible.

---

## Actionable Items for Arek's Pipeline

| Priority | Item | Impact |
|----------|------|--------|
| 🔴 High | PyTorch 2.13 upgrade — FlexAttention + CuTeDSL + normalization fusion | Measurable inference speedup on diffusion workloads, especially long-sequence video generation |
| 🟡 Medium | Native safetensors `torch.load()` | One fewer dependency in ComfyUI environments |
| 🟡 Medium | torchcomms backend for distributed training | Fault-tolerant fine-tuning if cluster-training Wan/CogVideoX |
| ⚪ Low | ExecuTorch → PyTorch Core merge | On-device inference path becomes simpler; relevant for portable video editing workflows |

---

## Source Links

- [PyTorch 2.13 Release Blog](https://pytorch.org/blog/pytorch-2-13-release-blog/)
- [Towards Free Normalization](https://pytorch.org/blog/towards-free-normalization-fusing-normalization-into-gemm-and-attention-kernels/)
- [Monarch on ROCm](https://pytorch.org/blog/bringing-pytorch-monarch-to-amd-gpus-single-controller-distributed-training-on-rocm/)
- [Miles RL Stack](https://pytorch.org/blog/miles-a-pytorch-native-stack-for-large-scale-llm-rl-post-training/)
- [TokenSpeed-Kernel](https://pytorch.org/blog/lightseek-tokenspeed-kernel/)
- [DeepSeek-V4 on GB300](https://pytorch.org/blog/serving-deepseek-v4-on-gb300-with-sglang-5x-higher-throughput-at-the-same-interactivity-since-day-0/)
- [ExecuTorch Hackathon](https://pytorch.org/blog/building-the-future-of-on-device-ai-at-the-executorch-hackathon/)
