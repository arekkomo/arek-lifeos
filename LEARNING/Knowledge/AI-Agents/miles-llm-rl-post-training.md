---
title: "Miles — PyTorch-Native Stack for Large-Scale LLM RL Post-Training"
category: source
summary: |
  RadixArk's Miles composes SGLang, Megatron-LM, and Ray into a unified RL post-training stack with explicit MoE support through plug-in model 
specs that inject custom nn.Module subcomponents without maintaining long-lived forks. Low-precision recipes (BF16/FP8/MXFP8/INT4-QAT) span the 
full pipeline for numerically aligned reward estimation between rollout and training phases, preventing corruption from dtype mismatch. 
Practical deployment path: SGLang handles generation on multi-silicon clusters where Ray actors coordinate trainer ranks separately from rollout 
servers via GPU-aware scheduling and placement groups. Cross-references [[OrbitQuant]] quantization approaches, [[Helion vLLM Kernels]] 
generation pipeline optimization patterns, and [[ComfyUI Compendium]] DGX Spark environment context.
tags: [rl-post-training, llm-fine-tuning, sglang, megatron-lm, ray,
  mixture-of-experts, low-precision]
sources: 1
updated: "2026-07-04"
source_path: https://pytorch.org/blog/miles-a-pytorch-native-stack-for-large-scale-llm-rl-post-training/
source_date: "2026-06"
authors: ["Miles Team @ RadixArk"]
ingested: "2026-07-04"
---

# Miles Framework for LLM RL Post-Training

**Source:** PyTorch Blog (June 30, 2026) | RadixArk Engineering

## Problem

RL post-training of foundation models requires sample generation, reward
computation, distributed training, and cluster orchestration -- each
previously maintained as separate codebases with fork divergence risk.
Existing monolithic tools either fork SGLang (rollout server) or
Megatron-LM (distributed trainer), making upstream updates expensive.

## Architecture: Compose, Don't Fork

Miles inverts the traditional model. Instead of forking each component, it
wraps them as Ray actors with a slim training-loop core. User customization
(rollout logic, reward computation, loss functions, sample filtering)
enters as Python modules loaded at launch -- keeping the core small and
maintainable while supporting multiple architectures through plug-in model
specs.

### Core Components

- **SGLang** provides high-throughput generation with constrained decoding paths for PPO/GRPO rollout steps. Benchmarked on DeepSeek-V3, 
GLM-4.7, and Qwen3 MoE variants using SGLang 0.5.2 on NVIDIA H200 clusters (RadixArk internal testing).

- **Megatron-LM** integration hooks into the training loop at log-prob
Computation, loss, and per-step boundaries rather than monkey-patching
internals. Model specs inject custom blocks (e.g., gated DeltaNet layers)
as standard `nn.Module` subcomponents, so a new architecture needs only one
spec implementation instead of a full fork.

- **Ray** actor model with GPU-aware scheduling and placement groups.
Actors include trainer ranks, rollout servers, routing proxies, and async
workers. Supports disaggregated (trainer on GPU cluster A, rollout on B)
and co-located layouts. Process-level fault tolerance through Ray recovery,
bulk weight transfer over dedicated NCCL/RDMA channels.

## Low-Precision Recipes Across Phases

BF16, FP8, MXFP8, and INT4-QAT recipes span the full pipeline -- both the
policy that generates samples (rollout) and the one that computes gradients
(training). Since RL requires numerically aligned log-probabilities between
phases, low-precision mismatches corrupt reward estimation. Miles' explicit
recipe specification per run makes these choices reproducible rather than
implicit. This aligns with [[OrbitQuant]] -- data-agnostic quantization via
RPBH rotation that also addresses the alignment problem from a different
angle (codebook construction vs. recipe specification).

## Practical Tool Chain for Local Deployment

SGLang runs on Hugging Face and supports both single-GPU and 4090-class
GPUs via pip install or Conda. Combined with [[ComfyUI Compendium]] DGX
Spark workflows, Miles can post-train local diffusion checkpoints using
reinforcement learning. The Ray actor model handles mixed-hardware setups
where generation and compute nodes differ -- relevant to multi-silicon
environments like those targeted by TokenSpeed-Kernel's AMD MI355X path.

> **Contradiction:** Post claims Miles avoids the maintenance burden of forks
because "the core stays small while customization enters as modules loaded at
launch." However, tracking SGLang and Megatron upstream changes still
represents a form of fork-like synchronization cost -- users must test their
plug-in specs against new component versions. "No fork" is true architecturally
but not operationally; upgrade testing remains necessary.

## Cross-Reference

[[Helion vLLM Kernels]] generates portable kernels via compiler search
(tile-size auto-tuning), while Miles uses explicit SGLang/Megatron APIs for
distributed orchestration rather than kernel fusion. The two complement: Helion
optimizes compute within each component; Miles coordinates components as a RL
pipeline. [[AdaCluster]] provides training-free sparse attention acceleration
that reduces KV cache pressure during rollout inference -- improving the
generation throughput that Miles depends on for PPO/GRPO sampling steps.

[[LocalDPO]] demonstrates preference optimization in the video domain with
regional-level loss alignment. While LocalDPO focuses on image-to-video fine-
tuning and Miles targets language model RL, both share infrastructure
requirements around distributed rollout computation and numerically stable
reward estimation. [[NaviCache test-time caching]] covers diffusion
acceleration through feature-state reuse; the latency reduction during
denoising complements the throughput gain from Miles' optimized rollout phase
in multi-modal pipelines where video generation precedes reward scoring.
