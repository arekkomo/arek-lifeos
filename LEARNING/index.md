# Knowledge Base Index

> Updated: 2026-07-01 (cycle 8)

## AI-Video
- **NaviCache — Test-Time Self-Calibration Caching** — Plug-and-play video diffusion acceleration modeling feature evolution as an inertial navigation system. Dual-state estimation tracks feature change ratio + latent drift, enabling error-bounded computation skipping without offline calibration. Tested on HunyuanVideo, Wan, Open-Sora (arXiv 2606.26795, 2026-06-25)
- **DomainShuttle — Subject-Driven T2V with Cross-Domain Flexibility** — Bridges in-domain fidelity and cross-domain editing via Domain-MoT, Video-Reference DualRoPE (separate token spaces), and Cross-Pair Consistent Loss. Enables freeform character-consistent video without per-subject tuning (arXiv 2606.26058, 2026-06-24)
- **LISA — Likelihood Score Alignment** — Reframes dual-branch conditional generation: side network contributes implicit likelihood score, explicitly aligned via lightweight decoder + regularization loss. Accelerates training convergence, improves disentanglement, zero inference cost (arXiv 2606.27192, 2026-06-25)
- **SAM2Matting — Generalized Video Matting via VOS Tracker** — Decouples video matting into tracker (temporal consistency) + dedicated matting heads (fine-grained alpha). Trained on image-only datasets, yet achieves SOTA on video matting benchmarks with strong out-of-domain generalization. Direct ComfyUI integration path for green screen replacement and multi-layer compositing (arXiv 2606.27339, 2026-06-25)
- **RayPE — Ray-Space Positional Encoding** — Plucker coordinate-based positional encoding that injects 6D ray geometry into self-attention Q/K for native 3D awareness in video diffusion transformers. <0.1% parameter overhead, zero-initialized drop-in module. Improves camera controllability and cross-frame 3D consistency (arXiv 2606.27345, 2026-06-25)
- **AI-Video-Tools** — Overview of AI video tools (Runway, Kling, MiniMax, ComfyUI...)
- **Physics Question Scene Graph (PQSG)** — Hierarchical VLM-driven fine-grained evaluation of physical plausibility in generated video. FinePhyEval dataset benchmarks Sora v2, Veo 3, Wan 2.1; closed-source models rank higher on physics realism (2026-06-25)
- **Wan-Streamer v0.1** — Native-streaming end-to-end interactive foundation model with block-causal attention for sub-second duplex audio-visual interaction (~200ms model latency, ~550ms total at 25fps). Eliminates cascaded VAD→ASR→LLM→TTS→animation pipeline (2026-06-25)
- **FreeStory** — Training-free character consistency for free-form visual storytelling via entity-grounded feature reuse (dynamic masks, correspondence-aware matching, KV injection, query blending). FreeStoryBench benchmark included (2026-06-25)
- **ComfyUI v0.26 + Kling V3-Turbo** — Partner node architecture with native Kling V3-Turbo support (2026-06-24)
- **ComfyUI Compendium** — DGX Spark ComfyUI maintenance reference
- **LiveEdit** — Real-time diffusion-based streaming video editing via three-stage distillation (bidirectional→unidirectional). 12.66 FPS causal frame-by-frame editing with AR mask cache for VFX interactive workflows (arXiv 2606.26740, 2026-06-26)
- **Disco-LoRA** — Disentangled multi-concept video customization: iterative dual-LoRA isolation of content/style/motion with Z-score regularization for composable LoRA mixing in T2V models (arXiv 2606.26668, 2026-06-26)
- **VPA-Guard and VVA-Bench for I2V Safety** — Benchmark and defense for visual prompt attacks on image-to-video models. Wan 2.7 at 100% ASR; VPA-Guard reduces by 44.2% (2026-06-24)
- **MVTrack4Gen** — Motion-aware training framework using multi-view point tracking as geometric supervision for novel-view video diffusion models (2026-06-25)
- **VLX-Seek — Fine-Grained VLM Localization via Region Tokens** — On-device VLM localization that replaces coordinate generation with region reference tokens for exact multi-object detection on embedded vision (omlab, June 2026)
- **VLX-Flow — Continuous Video Understanding** — Streaming video architecture that processes chunks incrementally with two-layer memory state. Sub-500ms latency for real-time VLM queries on live feeds and edge devices (omlab, June 26 2026)
- **TryOnCrafter** — Camera-controllable virtual try-on via renderable 4D Gaussian Splatting proxy with DiT backbone (2026-06-25)
- **OrbitForge** — Reconstruction-anchored text-to-3D: converts single text-generated video into closed-orbit Gaussian Splatting scene using frozen video prior + deformable GS, no fine-tuning or SDS optimization. 359° median view span on T3Bench (arXiv 2606.24799, 2026-06-23)
- **DramaDirector** — Geometry-guided short-drama generation using depth-pose reference gallery, schema-constrained SFT + GRPO under text-visual reward. DramaBoard benchmark: 81K shots from 35 live-action dramas (arXiv 2606.24107, 2026-06-23)
- **Gazer** — Training-free mid-generation semantic correction for autoregressive visual models via VLM feedback loop with reflective diagnosis + trajectory rewinding. Improves compositional accuracy without additional training (arXiv 2606.22550, 2026-06-21)
- **Goku — Million-Scale Video Editing Dataset** — 2M-pair dataset extending instruction-based video editing from appearance-only to multi-task structural manipulation. Dual-branch Goku-Edit model uses MLLM text encoder + dedicated mask branch for structural control. Goku-Bench: 1K test cases, 7 editing-specific metrics. +8% instruction following vs open-source baselines (arXiv 2606.30599, 2026-06-29)
- **Infinite-Length Video** — Minute-level video synthesis using hybrid causal-bidirectional attention across clips, KV caching for constant memory budget, and truncation-rectified flow (T-RFlow) to suppress error accumulation in long sequences (arXiv 2606.22370, 2026-06-21)
- **LatSearch — Latent Reward-Guided Inference-Time Scaling** — Separate reward model scores partially denoised latents (not decoded frames) for visual quality, motion quality, and text alignment along the denoising trajectory. Reward-Guided Resampling & Pruning (RGRP) in latent space enables efficient search without full video decoding. Consistently improves Wan2.1 quality across VBench-2.0 dimensions with manageable inference overhead (arXiv 2603.14526, 2026-03)
- **Vivid-VR — Concept Distillation for Video Restoration** — DiT-based restoration via concept distillation from pretrained T2V foundation model instead of conventional fine-tuning, preventing distribution drift. Dual-branch ControlNet connector: MLP feature mapping (static control transfer) + cross-attention (dynamic modulation). Strong on both real degraded footage and AIGC-generated video artifact correction (arXiv 2508.14483, 2025-08)
- **Delta Forcing — Trust Region Steering for AR Video** — Detects teacher-induced trajectory drift in streaming autoregressive generation via latent delta estimation between teacher and student. Adapters trust region shrinks when teacher diverges from monotonic continuity objective, suppressing unreliable shifts while preserving event reactivity. Drop-in training regularization (arXiv 2605.14382, 2026-05)
- **RefAlign — Explicit Representation Alignment for R2V** — Pull/push contrastive loss aligns DiT reference-branch features to frozen VFM semantic space: same-subject attraction, different-subject repulsion. Eliminates copy-paste artifacts and multi-subject confusion in reference-to-video generation. Training-only with zero inference overhead, improves TotalScore on OpenS2V-Eval (arXiv 2603.25743, 2026-03)
- **SSM-Meets-Video-Diffusion — Structured State Spaces Replace Attention** — Bidirectional SSM blocks (Mamba) replace attention temporal layers in video diffusion, achieving linear O(n) vs quadratic O(n²) scaling for sequence length. Less GPU memory for equal FVD, often better performance at comparable VRAM. Enables longer clip generation without memory explosion (arXiv 2403.07711, 2026-03)

## AI-Image-Midjourney
- **RoPEMover — Depth-Aware Object Relocation** — Geometry-aware object motion via positional embedding manipulation in diffusion transformers. Moves objects preserving occlusions, shadows, and reflections in single-pass inference. Requires per-model adaptation of RoPE field (arXiv 2606.27332, 2026-06-25)
- **DanceOPD — On-Policy Generative Field Distillation** — Training framework that unifies T2I, local editing, and global editing in flow-matching models via on-policy generative field distillation. Resolves capability interference during multi-skill training (arXiv 2606.27377, 2026-06-25)
- **Feature Self-Guidance — Diversity Collapse Mitigation** — Training-free plug-and-play method that disperses internal features during batch inference to mitigate diversity collapse in flow models while preserving fidelity via manifold regularization (arXiv 2606.27371, 2026-06-25)
- **FLUX.2 Klein Architecture** — BFL's compact diffusion family: KV-cache optimization, FP8, small decoder variants (2026-03–04)

## AI-Agents
- **ComfyUI MCP Agent Panel** — Autonomous AI agent in ComfyUI sidebar that drives canvas edits via natural language. Supports Claude or ChatGPT subscription with no API keys. Part of comfyui-mcp orchestration project (artokun, June 2026)
- **Ask-Solve-Generate — Self-Evolving Unified LMM Training** — Framework that improves both visual understanding and image generation in unified multimodal models using only unlabeled images and internal consistency signals. Tested across BLIP3o, BAGEL, VARGPT architectures (arXiv 2606.27376, 2026-06-25)

## AI-3D
- **PhysiFormer — Diffusion Transformer for 3D Physical Motion** — Simulates physically-plausible 3D object motion by predicting vertex trajectories directly in world coordinates via a single denoising diffusion process, with attention factorized over time, space, and objects. No explicit physics constraints needed — dynamics learned from data (arXiv 2606.27364, 2026-06-25)
- **StereoGS — Sparse-View 3D Gaussian Splatting via Stereo Priors** — Replaces monocular depth priors with binocular stereo regularization for reliable geometry under sparse views. Virtual stereo pairs + foundation stereo model enforce absolute scale and cross-view consistency. Gradient-aware opacity decay prunes redundant primitives. Consistency-aware dense initialization anchors primitives before optimization. SOTA on LLFF, DTU, Mip-NeRF360 at 3–8 views with zero inference overhead (arXiv 2606.30545, 2026-06-29)
- [3D generation]

## Filmmaking
- [Visual storytelling, cinematic shooting]

## DaVinci-Resolve
- [Resolve workflows]

## AI-TTS
- **Higgs Audio v3 TTS** — Controllable text-to-speech with inline emotional tags (Boson AI, 2026-06-04)
- **Stable Audio 3** — Stability AI's text-to-audio diffusion model family: music and SFX variants (2026-06-16)

## Music-Production
- **Suno v5 Prompt Engineering Best Practices** — Comprehensive guide covering structure formulas, dynamic arc descriptions, metatag systems, vocal persona building, phonetic tricks for AI vocalists, and the critical artist-name restriction rule. Covers v5-specific features: extended song generation (7+ min), multi-song batch generation, improved structure adherence, and Exclude Styles field.
- **Suno Music Style Tags Guide** — Reference catalog of Suno-compatible tags organized by BPM/tempo range (40-200+ BPM), instrumentation families (strings, brass, woodwinds, keyboards, guitars, bass, drums, synths, orchestral hybrid), production quality terms, vocal character descriptors, mood/emotion categories, genre combos, and structural metatags. Builds complete prompts using the formula: Genre + BPM + Mood + Instruments + Vocal Persona + Production Quality + Energy Arc.
- **Reference Song Analysis Template** — Structured workflow for converting any song concept or reference track into a Suno style prompt and metatag set without using artist names. Includes fill-in worksheet, 3 worked examples (housy house track with no reference track), and quick-conversion cheat sheet mapping emotional descriptions to sonic tags.
- **Magma RT2 — Realtime Music Generation Engine** — Open-source low-latency realtime music generation engine by Google Magenta Team. Transformer-based framework for instrument and voice synthesis from text prompts with real-time inference (github.com/KytraScript/magenta-rt2). [Notion batch 01]

---

## Status

### Working well
- All agents active (8 total)
- ComfyUI on DGX Spark fully operational v0.26.0 (partner node architecture, Kling V3-Turbo)
- Hermes profiles: systems, coach running

### Needs attention
- Custom node compatibility after NumPy fix (was-ns, ComfyUI-Allor now working)

### Pending improvements
- [Add as workflows and setups develop]
