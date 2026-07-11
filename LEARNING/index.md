# Knowledge Base Index

> Updated: 2026-07-10 (cycle 30 — PyTorch RSS scan + framework infrastructure briefing; arXiv/Semantic Scholar/HF/Google AI RSS sources blocked or rate-limited)

## AI-Video

### Autonomous Cycle 30 (2026-07-10 — PyTorch RSS feed scan, framework infrastructure update)

| **PyTorch 2.13 Framework Update** 🟠 | infra source | PyTorch 2.13 released Jul 8: FlexAttention on MPS (~12x sparse, ~4x medium), CuTeDSL Native DSL backend for Inductor (CUTLASS-grade GEMM/RMSNorm kernels), normalization fusion hiding 90% LayerNorm latency via GEMM overlap, native `torch.load()` for safetensors, FSDP2 AG/RS overlap, torchcomms backend. Filed full briefing with ComfyUI/diffusion relevance analysis. Other Jul articles: Monarch on ROCm (fault-tolerant training), Miles RL post-training stack, TokenSpeed-Kernel multi-silicon inference, DeepSeek-V4 on GB300 via SGLang (5x throughput), ExecuTorch hackathon winners |

### Autonomous Cycle 29 (2026-07-10 — arXiv cs.CV/cs.AI fresh harvest, 3 new pages filed after eval pass at 9–10/10)
| **OpenCoF** — Fine-tuned Wan2.2-I2V model for Chain-of-Frame reasoning through temporally connected video frames. 17K dataset spanning 11 task families + visual/textual reasoning tokens injected at step-specific denoising stages. +15–22pp gains on CoF benchmarks (arXiv 2607.08763, Jul 9)
| **Score Accuracy ≠ Numerical Stability** — Theoretical proof that small forward-marginal score error does NOT guarantee stable Euler-Maruyama sampling: rare trajectories cause divergent moments even under bounded Lipschitz denoisers. Denoiser-onto-convex-set projection restores Wasserstein convergence. ComfyUI sampler selection implications (arXiv 2607.08757, Jul 9)
| **DeltaV** — Spares visual token redundancy in Unified Multimodal Models by predicting per-frame delta updates instead of full intermediate images. 67–83% visual token reduction with mask-guided conditional synthesis. Impacts for iterative video editing and chunk-boundary AR workflows (arXiv 2607.08434, Jul 9)

### Autonomous Cycle 28 (2026-07-10 — arXiv cs.CV fresh harvest, 2 new pages filed after eval pass at 9/10)
| **OPSD-V** — On-Policy Self-Distillation fixes long-horizon error accumulation in few-step AR video diffusion. Teacher uses cleaner temporal cache while student follows its own KV trajectory. No sampler or step-count changes. +66% user preference on VBenchLong vs base (arXiv 2026-07, Jul 9)
| **SAGA** — Training-free spectral acceleration guidance for chunk-wise AR diffusion. Detects high-frequency temporal perturbations via Slepian projections in latent acceleration domain + structured noise initialization suppresses error seeding at each chunk boundary. Zero retraining (arXiv 2026-07, Jul 9)

## Real-Estate-Investing | New domain added cycle 20

### Vancouver Condos & Apartments (Jul 2026 Deep Dive)
| Page | Category | Summary | Tags |
|---|---|---|---|
| **[[Vancouver Condo Market 2026\*]]** | synthesis | Five-year outlook, timing, mortgage sizing for cash flow. ~40 sources Jan-Jul 2026 | vancouver, condo, investment, cash-flow |
| **[[Vancouver Condo Oversupply Crisis]]** | entity | Record unabsorbed inventory, 32% sales shortfall, forced developer fire-sales | oversupply, cmhc, rebgv |
| **[[BC Government Condo Buyout Program]]** | entity | Jun 2026 $3.2B program buys unsold inventory for rent-to-own housing. ~2,200 Metro units at risk of losses up to 20% below cost | government-policy, bc-eby |
| **[[Cash Flow Matrix Model]]** | entity | Tiered analysis showing positive cash flow doesn't exist at any price point currently. Optimal $390K mortgage max on sub-$600K units for break-even potential | cash-flow, mortgage-sizing, rental-yield |
| **[[Metro Vancouver Rental Market]]** | entity | Resilient yields with ~two percentage point gain at budget tier bottom since early 2025. Vacancy ~3-4% downtown. Gov buyout adds subsidized competitors by 2027 | vacancy, rental-supply, affordable-housing |

### Key Data Points (Accountant-ready reference)
| Metric | Value | Confidence | — PyTorch blog + arXiv ingestion: Miles, TokenSpeed-Kernel, iRDM)

## AI-Video

| **ProxyPose** — Monocular 6-DoF pose tracking from raw video alone via v2v translation loss through diffusion spatial consistency. No 3D mesh or depth map required for initialization (arXiv 2607.06555, 2026-07-08)

### Autonomous Cycle 27 (2026-07-09 — arXiv scanning, 1 new page filed after eval pass at 10/10)
| **Guidance Breaks the Fitted Operator** — Numerical analysis proving CFG re-stiffens the discriminative subspace to exponent 1+w, breaking DDIM's fitted-operator property. One-coefficient zero-extra-NFE repair formula (replace w(r-1) with r^(1+w)-r) eliminates σ_min divergence. 9/9 FID wins over vanilla CFG at high guidance on test grid. Direct relevance to ComfyUI sampler tuning and high-guidance VFX pipelines (arXiv 2607.07665, 2026-07-08)

### Autonomous Cycle 26 (2026-07-09 — arXiv scanning, 2 new pages filed after eval pass at 9/10)
| **Dynamic-in-Few-Step** — Joint optimization of denoising steps + structural sparsity creates per-timestep Mixture-of-Models for any VDM. 30x real-time speedup on Wan-14B with no measurable quality loss (arXiv 2607.06631, 2026-07-07)
| **Gen4U** — Probing intermediate diffusion activations reveals structured semantic latents; frozen VDMs are zero-shot encoders for classification, depth, camera pose, captioning with ~2pp gap to supervised baselines (arXiv 2607.06856, 2026-07-07)

### Autonomous Cycle 25 (2026-07-09 — arXiv scanning, 2 new pages filed after eval pass at 9/10)
| **Selective Timestep Weighting for Diffusion RLHF** — Cut reward model evaluation calls ~4× via timestep-level importance weighting and advantage-based trajectory replay. Early denoising steps waste gradient quality; mid-late steps carry structural signal. Drop-in sampler mod, no architecture change (arXiv 2607.07693, 2026-07-08)
| **LingBot-Video MoE for Embodied Intelligence** — Mixture-of-Experts DiT video pretraining optimized for physical realism over visual fidelity. Sparse activation keeps inference cost bounded while scaling total capacity. Data profiler augments internet video with robot manipulation footage (arXiv 2607.07675, 2026-07-08)

### Autonomous Cycle 24 (2026-07-08 — arXiv RSS + GitHub trending, 3 new pages filed after eval refinement)
| **PACR-Video** — Parameter-efficient multi-shot long video extrapolation via LoRA-style temporal adapters with recursive prompt routing. Preserves entity consistency, visual style, and narrative coherence across shot boundaries without full model fine-tuning. Composable with Wan/CogVideoX backends (arXiv 2607.06481, 2026-07-07)
| **MobileWan** — Demonstrates server-scale 5B video diffusion transformer (Wan2.2) can run on commercial mobile GPUs at 16 FPS via recurrence distillation and learnable attention head pruning. SOTA VBench for mobile video generation (arXiv 2607.06173, 2026-07-07)
| **Geometric Reciprocity** — Self-supervised stereoscopic video generation from unlimited monocular footage via cycle-consistency training. Novel geometric theorem enables analytical disocclusion mask computation without stereo ground truth (arXiv 2607.05354, 2026-07-06)

### From Notion Dump Ingest
New entities captured from raw Notion bookmark cards — tools/models not already in the existing AI-Video knowledge base:

| Tool/Model | Category | Key Focus | New Page |
|---|---|---|---|
| **VACE** (Alibaba) | Reference-to-video | Character swap, motion transfer between videos | `[[VACE]]` ✅ exists from prior work |
| **CineMaster** | 3D camera control | Object bbox + camera trajectory in 3D space | `[[CineMaster]]` ✅ exists — updated with deep research content |
| **FilmPort** | Production OS | Multi-generator workflow orchestration | `[[FilmPort]]` (new entity card) |
| **FastVideo** | Acceleration | Inference optimization for diffusion-based T2V models | `[[FastVideo]]` ✅ (new entry card) |
| **SkyReels-V2** | T2V model | Cinematic text/image-to-video generation | `[[SkyReels-V2]]` ✅ (new entity card) |
| **SkyReels-A2** | Audio-to-video | Audio-driven talking head with body animation | `[[SkyReels-A2]]` ✅ (new entity card) |
| **DreamO** (ByteDance) | Reference animation | Image-conditioned character animation | `[[DreamO-ByteDance]]` ✅ (new entity card) |
| **Magic-1-For-1** | Cinematic model | 2.39:1 native aspect-ratio video generation | `[[Magic-1-For-1]]` ✅ (new entity card) |
| **MotionLCM** | Motion control | Real-time controllable motion, ECCV 2024 paper | `[[MotionLCM]]` ✅ exists from prior work |
| **SeedVR2** | Post-processing | Video upscaling/restoration enhancement | `[[SeedVR2]]` ✅ (new entity card) |
| **UniAnimate-DiT** | Animation | Single reference image → video animation via DiT | `[[UniAnimate-DiT]]` ✅ (new entity card) |
| **DreamActor-M1** | Avatar | Expressive face/head animation from audio | `[[DreamActor-M1]]` ✅ (new entity card) |
| **FlowMo** | Motion control | Flow-mapped trajectory and gesture control | `[[FlowMo]]` ✅ (new entity card) |
| **ReVideo** | Video transformation | Structured video-to-video content control | `[[ReVideo]]` ✅ (new entity card) |
| **SpaceTimePilot** | Scene transitions | Interpolation between generated scenes | `[[SpaceTimePilot]]` ✅ (new entity card) |
| **Story2Board** | Pre-production | Concept → multi-shot storyboard pipeline | `[[Story2Board]]` ✅ (new entity card) |

### Substantive Content from Notion Dump
Full-length guides and operational docs preserved at full depth:
- [[n8n-YouTube-to-Notion]] — Automated video metadata capture workflow note
- [[Midjourney-MoodBoard-Guide]] — Step-by-step mood board prompting guide (3.1KB comprehensive content)

### Notable Existing Entries (already covered before this batch, AI-Video already had ~97 pages):
> Wan2 / Wan2.1, Wan2.2-Lightning, Wan-Alpha, CineMaster, VACE, MotionLCM, LTX-2.3, LTX-2.3 Prompting Guide, Open-Sora, Kling AI, Runway ML, MiniMax, DramaDirector, Gazer, WorldDirector, Physics-RAG, RefAlign, and many more...

### Notes from This Batch
⚠️ **95% of dump entries were sparse bookmark cards** (1 line + URL + tags). Knowledge pages written as structured entity cards with contextual summaries based on available metadata — not deep research pages. These represent saved links you've collected; each entry now has consistent formatting and cross-links.

> [[LTX-Video]] | [[LTX-2.3-Prompting-Guide]] | [[LTX-2.3-Production-Workflow]] 

## LTX-2.3
|- **Model Architecture** — Dual-stream DiT (14B video + 5B audio), 48 shared transformer blocks, Gemma 3 text encoder, VAE codecs, 3D RoPE for video / 1D RoPE for audio, FP8 quantization options, block streaming for low-memory deployment
|- **Prompting Guide** — Complete methodology: 7-part structure (main action → movement → appearance → environment → camera → lighting → temporal), cinematographic terminology reference, prompt length sweet spots (130-160 words), DO/DON'T language patterns, camera LoRA trigger integration, enhancement techniques
|- **Video Production Techniques** — Pipeline selection strategy (HQ two-stage / one-stage / distilled / keyframe interpolation / retake), I2V workflow with IC-LoRA control, spatial upsampling chains, DGX Spark optimization table, VRAM management, motion tracking via Motion-Track Control LoRA

## AI-Video (continued — entries from earlier cycles)

| **AdaCluster — Adaptive Query-Key Clustering for Sparse Attention** — Training-free adaptive clustering of attention Q/K in video DiTs. Angle-similarity-preserving query clustering + euclidean key clustering with per-layer adaptive thresholds. 1.67–4.31× speedup on CogVideoX, HunyuanVideo, Wan 2.1 on single A40 GPU (Semantic Scholar, 2026-07-03)
|- **LocalDPO — Direct Localized Detail Preference Optimization** — Post-training alignment for T2V diffusion via region-level preference pairs. Real videos as positives, locally corrupted versions as negatives. Region-aware DPO loss restricts learning to masked areas, faster convergence global DPO on Wan 2.1 and CogVideoX (Semantic Scholar, 2026-07-03)
||- **From SRA to Self-Flow — Data Augmentation Over Self-Supervision** — Mechanistic analysis showing Self-Flow's dual-timestep speedup comes from data augmentation along the noise dimension, not cross-timestep token interaction. Attention Separation blocks inter-timestep communication without degrading performance. Changes how self-supervised diffusion training acceleration is understood (arXiv 2607.02508, 2026-07-04)
|- **WorldDirector — LLM-Coordinated World Simulation** — Two-phase pipeline: LLM generates structured 3D trajectory graph for dynamic entities + synchronized camera paths, then video diffusion model uses trajectory as spatial-control conditioning signal. Persistent entity identity across prolonged occlusion events, unrestricted viewpoint exploration without generation collapse (arXiv 2607.02517, 2026-07-02)
- **GimbalDiffusion — Gravity-Aware Camera Control for Video Generation** — Defines camera trajectories in absolute world coordinates using gravity as a global reference (like a real gimbal), enabling precise 180° turnarounds and extreme pitch/roll. Trained on 360° panoramic videos to cover out-of-distribution camera angles. Null-pitch conditioning prevents prompt-camera conflict. New benchmarks for extreme-angle fidelity (arXiv 2512.09112v3, updated 2026-07-01)
- **TrajLoc — Per-Object Attention Localization** — Replaces cross-attention weights with Gaussian heatmaps per object token for strict spatial trajectory control in I2V. Up to 20 simultaneous objects, +4.3 dB PSNR, 51% endpoint error reduction on CogVideoX 5B and Wan 2.1 14B. Maps directly to VFX node-level compositing workflows (arXiv 2607.00861, 2026-07-01)
- **Prompt2Effect — Training-Free LoRA Synthesis** — Hypernetwork synthesizes effect-specific LoRA weights in a single forward pass from base model weights + text prompt. SVD-canonicalized parameterization stabilizes large-scale synthesis. 56 GPU training hours → 3.3 seconds (arXiv 2606.13971, 2026-06-11)
- **GEAR — Joint Tokenizer-Generator Training** — Closes decoupling gap between reconstruction tokenizers and autoregressive generators via end-to-end joint optimization. Tokenizer learns representations that maximally benefit the AR predictor rather than pure reconstruction loss. Compatible with [[DiT]] backbones, drops into [[ComfyUI]] workflows (arXiv 2606.32039, 2026-07-01)
- **World Narrative Model — Physical World Orchestration** — Frames video generation as explicit 4D instance orchestration rather than pixel distribution sampling. Instance graph with positions, orientations, velocities enables direct camera path and object trajectory control without prompting hacks. Order-of-magnitude controllability improvement on multi-object benchmarks (arXiv 2606.31946, 2026-07-01)
- **Shell-LCC — Manifold Reward for Text-to-Video** — Cost-free reward signals from data manifold structure via Shell Local Coordinate Coding. Encourages generated video latents to lie on SFT training manifold, improving visual quality without extra compute or reward model overhead. Model-agnostic ComfyUI integration path (arXiv 2606.30248, 2026-06-29)
- **DiffRGD — Riemannian Guidance for Diffusion** — Inference-time diffusion guidance via constrained optimization on spherical manifolds that preserves latent Gaussian radial structure, reducing distributional drift in conditional generation modes like high-CFG sampling. Sampler-level drop-in (arXiv 2606.28417, 2026-06-25)
- **NaviCache — Test-Time Self-Calibration Caching** — Plug-and-play video diffusion acceleration modeling feature evolution as an inertial navigation system. Dual-state estimation tracks feature change ratio + latent drift, enabling error-bounded computation skipping without offline calibration. Tested on HunyuanVideo, Wan, Open-Sora (arXiv 2606.26795, 2026-06-25)
- **DomainShuttle — Subject-Driven T2V with Cross-Domain Flexibility** — Bridges in-domain fidelity and cross-domain editing via Domain-MoT, Video-Reference DualRoPE (separate token spaces), and Cross-Pair Consistent Loss. Enables freeform character-consistent video without per-subject tuning (arXiv 2606.26058, 2026-06-24)
- **LISA — Likelihood Score Alignment** — Reframes dual-branch conditional generation: side network contributes implicit likelihood score, explicitly aligned via lightweight decoder + regularization loss. Accelerates training convergence, improves disentanglement, zero inference cost (arXiv 2606.27192, 2026-06-25)
- **SAM2Matting — Generalized Video Matting via VOS Tracker** — Decouples video matting into tracker (temporal consistency) + dedicated matting heads (fine-grained alpha). Trained on image-only datasets, yet achieves SOTA on video matting benchmarks with strong out-of-domain generalization. Direct ComfyUI integration path for green screen replacement and multi-layer compositing (arXiv 2606.27339, 2026-06-25)
- **RayPE — Ray-Space Positional Encoding** — Plucker coordinate-based positional encoding that injects 6D ray geometry into self-attention Q/K for native 3D awareness in video diffusion transformers. <0.1% parameter overhead, zero-initialized drop-in module. Improves camera controllability and cross-frame 3D consistency (arXiv 2606.27345, 2026-06-25)
- **AI-Video-Tools** — Overview of AI video tools (Runway, Kling, MiniMax, ComfyUI...)
- **Physics Question Scene Graph (PQSG)** — Hierarchical VLM-driven fine-grained evaluation of physical plausibility in generated video. FinePhyEval dataset benchmarks Sora v2, Veo 3, Wan 2.1; closed-source models rank higher on physics realism (2026-06-25)
- **Wan-Streamer v0.1** — Native-streaming end-to-end interactive foundation model with block-causal attention for sub-second duplex audio-visual interaction (~200ms model latency, ~550ms total at 25fps). Eliminates cascaded VAD→ASR→LLM→TTS→animation pipeline (2026-06-25)
- **FreeStory** — Training-free character consistency for free-form visual storytelling via entity-grounded feature reuse (dynamic masks, correspondence-aware matching, KV injection, query blending). FreeStoryBench benchmark included (2026-06-25)
- **MrFlow** — Training-free 10x diffusion acceleration via multi-resolution flow matching sampling pipeline with GAN-based pixel-space super-resolution and low-strength noise injection for high-frequency refinement. Tested on FLUX.1-dev, Qwen-Image (<1% OneIG gap, arXiv 2607.01642, 2026-07-02)
- **TempAct** — LLM planner-executor RL framework for chunk-wise autoregressive video generation: span-aware step prompts + hierarchical group exploration credit assignment eliminate delayed reactions, blended semantics, and error propagation across temporal transitions (arXiv 2606.28016v2, 2026-07)
- **ISPA — Instance-Specific Parametric Absorption** — Distills KV cache context into model weights via closed-form least-squares instead of dropping tokens. Removes up to 50% of KV cache with near-lossless quality in autoregressive video, preventing temporal flickering and identity loss. Works across 1.3B–14B architectures at inference time (arXiv, 2026-07-01)
|- **QWERTY — Query-Warped Motion Control for Video DiTs** — Training-free spatial control of object trajectories/optical flow via warping frame-invariant query embeddings in 3D full attention layers. Noise from warmed queries self-guides diffusion trajectory toward desired motion. Competitive with fine-tuned methods, zero training required (arXiv 2607.xxxx, 2026-07-02)
|- **Vega — Unified Video Understanding + Generation** — Hybrid AR + diffusion architecture: AR predicts semantic keyframe tokens, diffusion renders dense high-res frames from the same shared vocabulary. Single model replaces cascaded VLM+T2V pipeline (arXiv 2606.31946, 2026-07-01)
- **AVTok — Unified 1D Audio-Video Tokenization** — Dual-stream transformer encodes audio-video pairs into compact 1D latent via unified codebook, eliminating modal representation gap. Enables audio-to-video, video-to-audio, and joint generation with native synchronization (arXiv, 2026-07-01)
- **EcoVideo — Entropy-Orchestrated Cloud-Edge Video Generation** — Self-attention entropy estimates frame-wise information density; high-entropy frames denoised on cloud GPU, low-entropy frames reconstructed via edge interpolation. Adapts to real-time bandwidth/compute constraints, up to 2.9x speedup (arXiv, 2026-06-29)
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
## AI-Image

||- **UltraImageGen — Ultra-High-Res T2I with Hierarchical Local Attention** — Replaces quadratic global attention with fixed-size local windows + low-res semantic anchor, enabling 8K+ resolution with 10× speedup and 45% VRAM of baseline. LoRA bridge adapts pretrained Flux/SD3 models without full retraining. Window-first token repermutation makes GPU kernels resolution-agnostic (arXiv 2510.16325v4, updated 2026-07-01)
||- **Cross-Space Distillation via Bridge** — Lightweight latent-space Interface enables knowledge transfer from high-capacity diffusion teachers like [[Flux]] or SD 3.5 into compact SD 1.5 students despite VAE and latent resolution mismatch. SD 1.5 improved from 5.4 to 9.4 HPSv3 while preserving one-step inference. Drop-in compatible with existing [[ComfyUI]] workflows (arXiv 2606.32020, 2026-07-01)
||- **SpheRoPE - Zero-Shot 360 Panorama via Spherical RoPE** — Training-free framework that replaces rotary position embeddings with spherical priors for native 360 panorama and video generation using [[Flux]] or [[LTX-Video]] backbones. Harmonic quantization enforces exact ERP periodicity with zero fine-tuning overhead (arXiv 2606.32033, 2026-07-01)
||- **RoPEMover — Depth-Aware Object Relocation** — Geometry-aware object motion via positional embedding manipulation in diffusion transformers. Moves objects preserving occlusions, shadows, and reflections in single-pass inference. Requires per-model adaptation of RoPE field (arXiv 2606.27332, 2026-06-25)
|- **DanceOPD — On-Policy Generative Field Distillation** — Training framework that unifies T2I, local editing, and global editing in flow-matching models via on-policy generative field distillation. Resolves capability interference during multi-skill training (arXiv 2606.27377, 2026-06-25)
|- **Feature Self-Guidance — Diversity Collapse Mitigation** — Training-free plug-and-play method that disperses internal features during batch inference to mitigate diversity collapse in flow models while preserving fidelity via manifold regularization (arXiv 2606.27371, 2026-06-25)
|- **FLUX.2 Klein Architecture** — BFL's compact diffusion family: KV-cache optimization, FP8, small decoder variants (2026-03–04)
|**- Midjourney ** - [[stability-ai]] | [[flux]] | [[flux2-klein]] | [[UltraImageGen]] | [[Cross-Space Distillation]] | [[SpheRoPE]] | [[DanceOPD]] | [[Feature Self-Guidance]]

## AI-3D (continued — Batch 2 from Notion dump)
|- **Material Anything (Diffusion PBR)** — Xin Huang et al. unified diffusion framework for PBR material generation on any mesh type: texture-less, albedo-only, generated, scanned. Triple-head + rendering loss + confidence masks + UV-space refiner for production-ready output. Relightable materials across lighting conditions (arXiv 2411.15138)
|- **Meta 3D AssetGen (PBR Text-to-Mesh)** — Meta/NeurIPS 2024 text/image-to-mesh producer of full PBR materials from dual-stage pipeline: t2i → mesh reconstructor (SDF + deferred shading loss) → UV-space texture refiner. +17% Chamfer, +40% LPIPS, 72% human preference vs competitors. Relightable assets with albedo/metalness/roughness channels
|- **Hierarchical 3D Gaussians / HUGS** — Meuleman et al / SIGGRAPH 2024. Divide-and-conquer training splits km-scale scenes into independent chunks consolidated into LOD hierarchy. Enables real-time rendering of very large captures (tens of thousands of images, multiple km trajectories) with sparse-coverage regularization


## AI-Agents
- **ComfyUI-Agent-Kit — Local Multi-Agent MCP Controller** — Local-first ComfyUI integration for Claude Code/Codex/Gemini/Qwen Code. 4-layer stack: knowledge client + ~90-tool MCP driver + in-graph LLM nodes + node-building skills. 69 per-model prompt recipes, hardware-aware model selection, OCIO/ACES color management nodes, 545 workflow templates. MIT (github.com/SlavaSexton, 2026-07-06)
- **ComfyUI v0.38 — Multi-Agent ComfyUI Controller** — Portable, machine-independent multi-agent version with shared MCP driver + per-agent adaptors. Local-first architecture. One installer wires same stack into Claude Code/Codex/Gemini/Qwen agents. 210+ tools across generate, workflow editor, node library search, model selection, VRAM management (github.com/SlavaSexton/ComfyUI-Agent-Kit, June 2026)
- **Helion — Portable vLLM Kernels for Diffusion Serving** — Helion auto-generates hardware-optimized inference kernels from standard Python code without CUDA authoring. vLLM integration proves concept; applicable to diffusion model attention loops in ComfyUI backends via kernel fusion (PyTorch blog, June 2026)
- **TokenSpeed-Kernel Multi-Silicon Inference** — Kernel registration/selection API decouples inference from hardware-specific implementations. Gluon achieves 1.6-3.6x throughput on AMD MI355X for GPT-OSS 120B via XCD scheduling logic. Portability layer for video diffusion backends (PyTorch blog, June 2026)
- **From SRA to Self-Flow — Mechanistic Analysis** — Inversion-free editing via iterative self-guidance along noise dimension, not cross-timestep token interaction as originally claimed. Attention Separation experiment blocks inter-timestep communication with no degradation in quality (arXiv 2607.12554, July 2026)
- **iRDM One-Step Image Generation** — Distribution matching under 14 frozen encoders using MMD at batch sizes above 2048 for stable estimation eliminates multi-step denoising overhead entirely. Converts FLUX.2 from four-step to one-step while improving GenEval score (arXiv 2607.02375, July 2026)
- **ComfyUI-OCIO — Nuke-Style Color Management Nodes** — OpenColorIO + ACES integration for ComfyUI. EXR/ProRes I/O, LogConvert, CDL, Display mapping, LookTransform. Brings professional VFX color pipeline into AI generation workflows (github.com/SlavaSexton, 2026-07-02)
- **ComfyUI MCP Agent Panel** — Autonomous AI agent in ComfyUI sidebar that drives canvas edits via natural language. Supports Claude or ChatGPT subscription with no API keys. Part of comfyui-mcp orchestration project (artokun, June 2026)
- **ComfyUI v0.27** — Native int8 convolution support with progressive optimizations (faster kernel, Turing GPU compat, lora fix, memory leak fix). Partner nodes: HappyHorse 1.1, SeeDance 2.0-Mini w/ 4K, Nano Banana 2 Lite. New core: Seed node, bounding box canvas + Ideogram JSON prompt, advanced Krea 2 merging, ConditioningMultiply (github release 2026-06-30)
- **Ask-Solve-Generate — Self-Evolving Unified LMM Training** — Framework that improves both visual understanding and image generation in unified multimodal models using only unlabeled images and internal consistency signals. Tested across BLIP3o, BAGEL, VARGPT architectures (arXiv 2606.27376, 2026-06-25)
- **OrbitQuant — Data-Agnostic DiT Quantization** — RPBH rotation concentrates activation coordinates around fixed marginals regardless of timestep/prompt/modality, enabling a single Lloyd-Max codebook for post-training quantization. First usable W2A4 on image/video DiTs with zero per-checkpoint calibration data. Tested on FLUX.1, Wan 2.1, CogVideoX (arXiv 2607.02461, 2026-07-02)

## AI-3D
|- **MV-Forcing — Long Multi-View Video via 4D Self-Forcing** — Temporal autoregression chained through lightweight Gaussian Splatting proxy; renders new viewpoints as spatial priors for bidirectional attention. Generates minutes of consistent multi-view dynamic sequences, not just short clips (arXiv 2607.05376, 2026-07)
|- **Flex4DHuman — Multi-View Video Diffusion for 4D Reconstruction** — Converts monocular video to synchronized dense multi-view using only SE(3) camera-pose conditioning, no explicit geometry priors. Five-axis positional encoding extends RoPE with view indices and continuous camera geometry. Three-stage curriculum: pose following → flexible reference → temporal rollout. Feeds directly to [[Gaussian Splatting]] for dynamic 4D assets (Semantic Scholar, 2026-07-03)
|- **SimWorlds — Multi-Agent Blender 4D Scene Generation** — Planner-coder-reviewer LLM agents generate physically-correct animated 3D scenes from text via Blender Python API. Runtime-state inspection tools validate physics correctness before rendering. New 4DBuildBench benchmark for physical consistency evaluation (arXiv 2607.01766, 2026-07-02)
- **Align4D — X-to-4D Generation via Diffusion Alignment** — Unified framework converting text/image/video input into coherent 4D scenes by aligning video guidance with 3D geometric priors through object distance optimization and asynchronous Gaussian attribute/deformation training (arXiv 2607.02516, 2026-07-02)
- **PointDiT — Pixel-Space DiT for Monocular Geometry** — ICML 2026 acceptance. ViT-based diffusion on raw point-map patches, no latent tokenization or hybrid architecture, conditioned on DINOv3 image features. Simpler design with sharper geometry and better transparency robustness (arXiv 2607.02515, 2026-07-02)
- **Pano2World — Single Panorama to Explorable 3D Scene** — Converts one indoor panorama into a persistent Gaussian Splatting scene in a single pass via View-Aware Attention Routing (VAAR) and Latent Feature Adapter (LFA). No iterative inpainting; joint denoising of all target views with geometric + semantic dual guidance. Outperforms multi-stage pipelines on novel-view synthesis benchmarks (arXiv 2607.00832, 2026-07-01)
- **PhysiFormer — Diffusion Transformer for 3D Physical Motion** — Simulates physically-plausible 3D object motion by predicting vertex trajectories directly in world coordinates via a single denoising diffusion process, with attention factorized over time, space, and objects. No explicit physics constraints needed — dynamics learned from data (arXiv 2606.27364, 2026-06-25)
- **StereoGS — Sparse-View 3D Gaussian Splatting via Stereo Priors** — Replaces monocular depth priors with binocular stereo regularization for reliable geometry under sparse views. Virtual stereo pairs + foundation stereo model enforce absolute scale and cross-view consistency. Gradient-aware opacity decay prunes redundant primitives. Consistency-aware dense initialization anchors primitives before optimization. SOTA on LLFF, DTU, Mip-NeRF360 at 3–8 views with zero inference overhead (arXiv 2606.30545, 2026-06-29)
- **Ink3D — Video-Prior Texture Synthesis for 3D Assets** — Decouples geometry from texture, using conditional video model to generate dense orbit-scan videos of objects, then neural optimizer bakes coherent UV textures. Bridges gap between sparse 3D data corpora and massive video priors. Rich surface detail beyond what dedicated 3D generators reproduce (arXiv 2607.01222, 2026-07-01)

## Filmmaking
- [Visual storytelling, cinematic shooting]

## DaVinci-Resolve
- [Resolve workflows]

## AI-Audio
||- **NAVA — ERNIE Research** — Multimodal generation framework producing synchronized audio + video simultaneously via joint diffusion architecture (Notion batch 01)
||- **Higgs Audio v3 TTS — Boson AI** — Production-grade zero-shot voice synthesis with inline emotional tags, fine-grained prosody control and speaker adaptation (Notion batch 01)

## Digital-Humans
||- **StreamChar — Alibaba/Personas** — Real-time speech-driven animation, avatar streaming for continuous talking avatars synchronized to audio input. Enables real-time character synthesis pipelines (Notion batch 02)
||- **WavTTS — ByteDance** — Production-grade zero-shot voice cloning from seconds of audio reference, emotion control for content pipeline integration (Notion batch 02)
||- **Reve 2 — Meta** — AI voice synthesis model with ultra-realistic emotional range, speaker cloning, and expressive dialogue capabilities (Notion batch 02)

## AI-TTS
- **Higgs Audio v3 TTS** — Controllable text-to-speech with inline emotional tags (Boson AI, 2026-06-04) [Notion batch 01]
- **Stable Audio 3** — Stability AI's text-to-audio diffusion model family: music and SFX variants (2026-06-16) [Notion batch 01]

## VFX (continued)
- **CarWash** — Houdini/Solaris USD Render Delegate that conditions [[LTX-2.3 Model Architecture]] on actual USD scene shading via [[ComfyUI]] (github.com/JOIbrahim, 2026-07-06)
- **Stable Layers** — Stability AI image decomposition for compositing (Notion batch 02)
- **LightCrafter** — PBR-conditioned video relighting via hybrid inverse-render + diffusion refinement. Bakes illumination targets into PBR proxy before CogVideoX translates to photorealistic output (arXiv 2026-07, Jul 9)

## Music-Production
- **Suno v5 Prompt Engineering Best Practices** — Structure formulas, dynamic arc descriptions, metatag systems, vocal persona building, phonetic tricks, artist-name restriction rule. Covers extended generation (7+ min), multi-song batch, Exclude Styles field.
- **Suno Music Style Tags Guide** — Reference catalog by BPM, instruments, production quality terms, mood categories. Prompt formula: Genre + BPM + Mood + Instruments + Vocal Persona + Production Quality + Energy Arc.
- **Reference Song Analysis Template** — Structured workflow for converting song concept into Suno style prompt without artist names. Includes fill-in worksheet and worked examples.
- **Magma RT2** — Realtime music generation engine by Google Magenta Team (github.com/KytraScript/magenta-rt2) [Notion batch 01]

## Real-Estate-Investing | New domain added cycle 20
- **Vancouver Condo Market 2026*** — Five-year outlook, timing, mortgage sizing for cash flow. ~40 sources Jan-Jul 2026

---

## Status

### Working well
All agents active (8 total)
- ComfyUI on DGX Spark fully operational v0.27.0 (native int8 convolution, partner node updates incl. SeeDance 2.0-Mini)- Hermes profiles: systems, coach running

### Needs attention
- Custom node compatibility after NumPy fix (was-ns, ComfyUI-Allor now working)

### Pending improvements
- [Add as workflows and setups develop]
