---
title: "Daily Research Scan — June 26, 2026"
category: source
summary: Daily autonomous scan of arXiv cs.CV, PyTorch Blog, HuggingFace, and dead feeds. Disco-LoRA and LiveEdit already filed; 8 additional papers flagged for follow-up. TokenSpeed-Kernel blog post from PyTorch captured.
tags: [daily-scan, arxiv, pytorch, research-monitoring]
sources: 190
updated: 2026-06-26
---

# Daily Research Scan — 2026-06-26

**Scope:** arXiv cs.CV (182 items), PyTorch Blog (2 active posts since yesterday), HuggingFace Blog (404 – dead RSS endpoint), Google GenAI Blog (404 – dead RSS endpoint).

**Prior session filed today:** [[disco-lora-multi-concept-video]], [[liveedit-streaming-video-editing]], [[mvtrack4gen]], [[tryoncrafter]]. Total 182 arXiv cs.CV entries scanned; Disco-LoRA and LiveEdit already captured by earlier cron run. This note covers remaining relevant papers and ecosystem updates.

---

## 1. arXiv cs.CV — Remaining High-Relevance Papers (not yet filed)

### Video Editing & Generation Pipeline

| # | Paper | Relevance | Notes |
|---|-------|-----------|-------|
| PhyEditBench | `PhyEditBench`, [link](https://arxiv.org/abs/2606.24175) | Physics-aware image editing benchmark — directly adjacent to video editing workflows | Multi-stage, real-world dataset for physics-grounded editing; benchmarks consistency across gravity, fluid, collision edit outcomes. Useful for evaluating ComfyUI + physics plugins. |
| PhysEditWorld | `PhysEditWorld`, [link](https://arxiv.org/abs/2606.24176) | Large-scale dataset for physics-editable world models | First dataset specifically targeting physically editable scenes for diffusion-based video generation. 1M+ frame pairs with edit instructions + ground-truth physics simulations (Blender, NVIDIA PhysX). |
| NaviCache | `NaviCache`, [link](https://arxiv.org/abs/2606.24187) | Test-time self-calibration caching for video generation | Caching mechanism that reuses cross-frame latent features during test time to stabilize video diffusion outputs without retraining. 1.8-3.2x speedup on Stable Video Diffusion and AnimateDiff pipelines. |
| SpatialFlow-GRPO | `SpatialFlow-GRPO`, [link](https://arxiv.org/abs/2606.24195) | Reinforcement learning for spatial-aware image/video editing | Adapts GRPO (Generalized PPO) to image editing tasks by introducing a spatial credit assignment layer — rewards are region-weighted based on attention overlap with the edited mask. Early results on InstructPix2Pix show 14% improvement in edit fidelity scores. |
| ResilPhase | `ResilPhase`, [link](https://arxiv.org/abs/2606.24208) | Plug-and-play phase mapping for diffusion acceleration | Phase-mapping technique that reduces sampling steps for flow-based diffusion models by 60-75% while preserving output quality. Macro-trajectory extrapolation + noise-resilient denoising. Applicable to any video diffusion pipeline (SVD, AnimateDiff, CogVideoX). |
| RayPE | `RayPE`, [link](https://arxiv.org/abs/2606.24217) | Positional encoding for 3D-aware video generation | Novel 3D positional encodings designed specifically for video latents (vs. flat image PE). Enables spatial-temporal coherence in video diffusion without explicit geometry conditioning. Benchmarked on 4D Gaussian Splatting + ControlNet hybrid pipelines. |
| SAM2Matting | `SAM2Matting`, [link](https://arxiv.org/abs/2606.24219) | Generalized image and video matting via SAM2 backbone | Extends Segment Anything 2 to precise boundary-aware matting — alpha matte extraction for both single images and multi-frame video. Uses temporal smoothing + fine-grained boundary refinement. Directly useful for VFX compositing in ComfyUI workflows. |
| RoPEMover | `RoPEMover`, [link](https://arxiv.org/abs/2606.24218) | Depth-aware object relocation via positional embedding manipulation | Modifies rotary positional embeddings to natively encode depth information, enabling spatially-aware object repositioning in images/videos without repaint artifacts. Works with stable diffusion pipelines; 92% SSIM on moving-object benchmarks. |

### Physics & 3D Simulation for Video/VFX

| # | Paper | Relevance | Notes |
|---|-------|-----------|-------|
| NeurVoxel Dynamics | `Neural Voxel Dynamics`, [link](https://arxiv.org/abs/2606.24178) | Implicit 3D physics via volumetric feature advection | Neural network learns to simulate 3D physical systems (fluid, rigid body, deformation) by advecting implicit voxel features — no explicit mesh required. Generates plausible dynamics at 60fps for 128³ grids; can be used as a post-gen physics layer over AI-generated footage. |
| PhysRAG | `PhysRAG`, [link](https://arxiv.org/abs/2606.24205) | Retrieval-augmented generation for physics-aware video | RAG pipeline that retrieves physics simulation priors (gravity constants, material properties, collision rules from a simulation corpus) and conditions them into text-to-video diffusion models. Addresses the "floaty physics" problem in AI-generated video. |
| LCG | `LCG: Long-Context Consistent Image Generation`, [link](https://arxiv.org/abs/2606.24168) | Sparse relational attention for long-image/video consistency | Not video-specific but the sparse relational attention mechanism is applicable to multi-frame temporal consistency in video generation. 3x memory reduction over full-attention with negligible quality loss. |

### Other Noteworthy Papers (borderline relevance)

| # | Paper | Relevance | Notes |
|---|-------|-----------|-------|
| PortraitGen | Generative portrait synthesis via GRPO dual reward | High-quality face portraits; useful for character reference workflows in filmmaking. |
| TMP (Tree-structured Mixed-policy Pruning) | Pruning framework for large-scale image gen/editing | Speeds up diffusion inference by 2-4x; applicable to any ComfyUI pipeline. |
| Scaling Multi-Reference Image Generation with Dynamic Reward Optimization | Multi-subject reference control in generation | Useful for scene composition workflows (characters + environments from separate references). |

---

## 2. PyTorch Blog — New since yesterday

### TokenSpeed-Kernel: Portable APIs and High-Performance Kernels for Multi-Silicon LLM Inference

**Date:** June 25, 2026
**Authors:** AMD Triton Team, TokenSpeed Team
**Link:** https://pytorch.org/blog/lightseek-tokenspeed-kernel/

TokenSpeed-Kernel is a standalone subsystem that decouples LLM inference runtime from hardware-specific kernels via a clean registration/selection API. Key findings:

- **GPT-OSS 120B on AMD MI355X:** Achieved 1.6x-3.6x end-to-end throughput improvements over Triton baseline using Gluon (Triton-family DSL) kernels for CDNA4.
- **Attention kernels (Gluon):** Persistent kernel with XCD scheduling logic — 1.4-2.3x faster than Triton, 1.1-1.3x faster than AITER. Tile-based QK/PV with online softmax exploiting CDNA4 matrix cores.
- **MoE kernels:** Ragged block schedules for prefill (handles uneven expert token distribution); warp-decode fused routing+GEMM path for small batches; direct grouped GEMM for medium batches. 1.7-2.1x faster than Triton at smallest batch sizes.
- **Registry mechanism:** `@register_kernel` decorator with platform capability, tensor format signature, trait matching, and priority ranking. Runtime calls are hardware-agnostic (e.g., `mha_prefill`, `moe_apply`).
- **Adopted by vLLM** — AMD attention/MoE kernels released as standalone `tokenspeed-kernel-amd` pip package.

**Relevance to Arek's stack:** Multi-silicon inference optimization is critical for local deployment of video/animation models. TokenSpeed-Kernel demonstrates how Gluon outperforms Triton for custom kernel development; this is relevant if running custom diffusion kernels on AMD hardware in ComfyUI.

### SGLang Serving DeepSeek-V4 on GB300 — 5x Higher Throughput

**Date:** June 23, 2026
**Authors:** SGLang Team and NVIDIA Team  
**Link:** https://pytorch.org/blog/serving-deepseek-v4-on-gb300-with-sglang-5x-higher-throughput/

SGLang team's performance optimization story for DeepSeek-V4 serving on NVIDIA GB300 and Blackwell Ultra:

- **Kernel fusions:** Deeper MHC (Multi-head Cross-attention) fusion via DeepGEMM kernels, fused RMSNorm into MHC path, new `mhc_fused_post_pre` kernel reduces scheduler-visible boundaries.
- **KV Compression V2:** New c4, c128, and online c128 compression kernels for DeepSeek-V4; updated compressor plumbing with fused norm/rope V2.
- **W4A4 MegaMoE:** Activation path now also quantized to MXFP4 (previously only weights), improving MoE efficiency at high throughput with negligible accuracy loss.
- **5x throughput improvement:** From ~2,200 tok/s/GPU (Day-0, April 2026) to ~11,200 tok/s/GPU on GB300 disaggregated lane at the same user-visible interactivity (50 tok/s/user).
- **Breakable CUDA graphs:** DeepSeek-V4 prefill path now graph-friendly via breakable-CUDA-graph support — reduces host-bound overhead.

**Relevance to Arek's stack:** While not directly AI video, multi-silicon inference optimization and kernel fusion patterns transfer to diffusion model serving (SVD, CogVideoX) on custom hardware. SGLang's approach to reducing intermediate tensor traffic via kernel fusion is applicable to ComfyUI node chain optimization.

---

## 3. Dead / Changed RSS Endpoints

| Feed | Status | Notes |
|------|--------|-------|
| HuggingFace Blog (`/blog/rss`) | **404** — dead endpoint as of mid-June 2026. Returns HTML error page. | Previously reliable AI tool announcements. Need alternate source (HuggingFace Twitter/X or direct blog scraping). |
| Google GenAI Blog | **404** — dead endpoint. Returns generic Google 404. | No RSS feed available; Google moved to different announcement channels. |
| YouTube channel feeds | **Blocked/Empty** — YouTube RSS returns minimal content for some channels (11 lines, no `<entry>` blocks). May need authentication or alternate scraping approach. |

---

## 4. Summary & Recommended Actions

1. **File PhyEditBench + PhysEditWorld** — Both highly relevant benchmarks/datasets for physics-aware editing in video workflows.
2. **File NaviCache** — Diffusion acceleration technique with direct applicability to ComfyUI pipelines.
3. **File TokenSpeed-Kernel (PyTorch blog)** — Multi-silicon inference patterns transferable to video model serving.
4. **Replace dead RSS sources:** HuggingFace and Google GenAI feeds no longer work. Switch to `huggingface.co/paper` API or Twitter/X monitoring (`@huggingface`).
5. **YouTube feed strategy change:** YouTube RSS is unreliable for channel monitoring — consider n8n-based YouTube Data API polling instead.

**arXiv scan stats:** 182 papers total in cs.CV for June 26, 2026. 4 already filed (Disco-LoRA, LiveEdit, MVTrack4Gen, TryOnCrafter). 8 additional papers flagged above with high relevance to AI video / VFX / ComfyUI workflows.
