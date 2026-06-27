# Knowledge Base Index

> Updated: 2026-06-27

## AI-Video
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
- **TryOnCrafter** — Camera-controllable video virtual try-on via renderable 4D Gaussian Splatting proxy with DiT backbone (2026-06-25)

## AI-Image-Midjourney
- **RoPEMover — Depth-Aware Object Relocation** — Geometry-aware object motion via positional embedding manipulation in diffusion transformers. Moves objects preserving occlusions, shadows, and reflections in single-pass inference. Requires per-model adaptation of RoPE field (arXiv 2606.27332, 2026-06-25)
- **DanceOPD — On-Policy Generative Field Distillation** — Training framework that unifies T2I, local editing, and global editing in flow-matching models via on-policy generative field distillation. Resolves capability interference during multi-skill training (arXiv 2606.27377, 2026-06-25)
- **Feature Self-Guidance — Diversity Collapse Mitigation** — Training-free plug-and-play method that disperses internal features during batch inference to mitigate diversity collapse in flow models while preserving fidelity via manifold regularization (arXiv 2606.27371, 2026-06-25)
- **FLUX.2 Klein Architecture** — BFL's compact diffusion family: KV-cache optimization, FP8, small decoder variants (2026-03–04)

## AI-Agents
- **Ask-Solve-Generate — Self-Evolving Unified LMM Training** — Framework that improves both visual understanding and image generation in unified multimodal models using only unlabeled images and internal consistency signals. Tested across BLIP3o, BAGEL, VARGPT architectures (arXiv 2606.27376, 2026-06-25)

## AI-3D
- **PhysiFormer — Diffusion Transformer for 3D Physical Motion** — Simulates physically-plausible 3D object motion by predicting vertex trajectories directly in world coordinates via a single denoising diffusion process, with attention factorized over time, space, and objects. No explicit physics constraints needed — dynamics learned from data (arXiv 2606.27364, 2026-06-25)
- [3D generation]

## Filmmaking
- [Visual storytelling, cinematic shooting]

## DaVinci-Resolve
- [Resolve workflows]

## AI-TTS
- **Higgs Audio v3 TTS** — Controllable text-to-speech with inline emotional tags (Boson AI, 2026-06-04)
- **Stable Audio 3** — Stability AI's text-to-audio diffusion model family: music and SFX variants (2026-06-16)

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
