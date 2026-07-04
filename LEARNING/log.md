# Log — Arek's Second Brain

## [2026-07-03] autoresearch | Autonomous scan cycle 16 — 3 items filed (Semantic Scholar)
Auto-discovered from Semantic Scholar API queries. Scanned ~15 candidates across video diffusion acceleration, preference optimization, multi-view reconstruction, and efficient video DiT architectures. Scored against 10-assertion eval framework with iterative refinement over 3 passes per item (a-04 paragraph length constraint required pass 3).

Items filed:
- **AdaCluster** (9/10 after pass 3) — Training-free adaptive Q/K clustering for sparse attention in video Diffusion Transformers. Angle-preserving query + euclidean key clustering with per-layer thresholds. 1.67–4.31× speedup on CogVideoX/HunyuanVideo/Wan 2.1
  → LEARNING/Knowledge/AI-Video/adacluster-adaptive-query-key-clustering-sparse-attention.md

- **Flex4DHuman** (9/10 after pass 3) — Multi-view video diffusion for 4D human reconstruction from monocular input using only SE(3) camera-pose conditioning, no explicit geometry priors. Five-axis RoPE extension + three-stage curriculum training
  → LEARNING/Knowledge/AI-3D/flex4dhuman-multi-view-video-diffusion-4d-reconstruction.md

- **LocalDPO** (9/10 after pass 3) — Regional-level DPO for text-to-video alignment via automated localized preference pairs. Real videos as positives, corrupted-masked regions as negatives. Faster convergence than global DPO on Wan 2.1 and CogVideoX
  → LEARNING/Knowledge/AI-Video/localdpo-localized-detail-preference-optimization.md

Items rejected as low-quality/noise: ~5 (SALAD linear attention tuning — overlaps with AdaCluster; Efficient Video Diffusion survey — review paper without implementation details; GitHub repos <3 stars each too young for relevance bar)

Updated: index.md (+3 entries), log.md, cycle counter (15→16)

## [2026-07-02] autoresearch | Autonomous scan cycle 12 — 4 items filed (arXiv + GitHub)
Auto-discovered from arXiv cs.CV RSS feed and GitHub trending searches. Scanned ~34 candidates across video generation, ComfyUI nodes, AI agents/MCP servers, and 3D texture synthesis. Scored against 10-assertion eval framework with iterative refinement (max 3 passes per item).

Items filed:
- **TrajLoc** (10/10 after pass 1) — Per-object attention localization for multi-object motion control in I2V. +4.3 dB PSNR, 51% endpoint error reduction on CogVideoX 5B and Wan 2.1 14B
  → LEARNING/Knowledge/AI-Video/trajloc-multi-object-motion-control.md

- **Prompt2Effect** (9/10 after pass 1) — Hypernetwork for training-free LoRA synthesis from text prompts. SVD-canonicalized parameterization, 56 GPU hours → 3.3 seconds
  → LEARNING/Knowledge/AI-Video/prompt2effect-training-free-lora-synthesis.md

- **Ink3D** (9/10 after pass 1) — Video-prior texture synthesis for 3D assets via decoupled geometry + neural baking from orbit-scan videos
  → LEARNING/Knowledge/AI-3D/ink3d-video-prior-texture-synthesis.md

- **ComfyUI-OCIO** (8/10 after pass 1) — Nuke-style OpenColorIO color management nodes for ComfyUI. EXR/ProRes I/O, ACES transforms, CDL
  → LEARNING/Knowledge/AI-Agents/comfyui-ocio-color-management.md

Items rejected as low-quality/noise: ~30 (GimbalDiffusion — Dec 2025 stale; Krea conditioning node — fork of existing work; TrixNodes/TJNODE/Theme/MK-Theme/UI plugins — cosmetic/workflow utilities without algorithmic substance; Open-Generative-AI/Duix-Avatar/Toonflow/KrillinAI/imaginAIry/mmagic/AutoClip/Jellyfish/short-video-factory/Generative-Media-Skills — high GitHub stars but application-level wrappers, not research or tooling with technical depth; super-agent-party/comfyui-LLM-party — interesting but tangential to core domains)

Updated: index.md (+4 entries), log.md, cycle counter (11→12)

## [2026-07-01] autoresearch | Autonomous scan cycle 11 — 2 items filed (arXiv cs.CV)
Auto-discovered from arXiv cs.CV queries. Scanned ~24 candidates across video generation, diffusion guidance, and controllable video searches. Scored against 10 assertion eval framework with iterative refinement.

Items filed:
- **GEAR** (9/10 after pass 1 — joint tokenizer-generator training closes reconstruction-vs-generation gap)
  → LEARNING/Knowledge/AI-Image-Midjourney/gear-joint-tokenizer-generator-training.md

- **World Narrative Model** (9/10 after pass 1 — 4D physical world orchestration for controllable video generation)
  → LEARNING/Knowledge/AI-Video/world-narrative-model-physical-orchestration.md

## [2026-07-01] autoresearch | Autonomous scan cycle 10 — 3 items filed (arXiv cs.CV + PyTorch blog)
Auto-discovered from arXiv cs.CV RSS feed and PyTorch blog. Scanned ~15 candidates via video generation / diffusion guidance queries. Scored against 10-assertion eval framework with iterative refinement (max 3 passes).



  → LEARNING/Knowledge/AI-Video/shell-lcc-manifold-reward-t2v.md

- **DiffRGD** (10/10 after refinement pass 2) — Riemannian optimization on spherical manifolds for inference-time diffusion guidance. Preserves latent Gaussian radial structure, eliminating distributional drift from high-CFG sampling artifacts in ComfyUI workflows.
  → LEARNING/Knowledge/AI-Video/diffrgd-riemannian-gradient-diffusion.md

- **Helion Kernels** (9/10 after refinement pass 2) — PyTorch's auto-tuning compiler generates hardware-optimized inference kernels from standard Python for vLLM serving. Applicable to diffusion model attention loops in ComfyUI backends via kernel fusion patterns.
  → LEARNING/Knowledge/AI-Agents/helion-vllm-kernels-diffusion-serving.md

Items rejected as low-quality/noise: ~5 (DiTracker point tracking from VFM features — Dec 2025 too old; AHOY Gaussian avatar reconstruction — Mar 2026 stale; Lumos-Nexus frequency bridging framework — May 2026 marginal recency)

Updated: index.md (+3 entries), log.md, cycle counter (9→10)

## [2026-07-01] autoresearch | Autonomous scan cycle 9 — 2 papers filed (arXiv cs.CV June 30)
Auto-discovered from arXiv cs.CV/cs.AI RSS feed. Scanned ~20 candidates via video generation / neural rendering + diffusion / image synthesis queries. Scored against 10-assertion eval framework with iterative refinement (max 3 passes).

Items filed:
- **Cross-Space Distillation** (8/10 after refinement) — Lightweight Bridge interface enables distillation from modern diffusion teachers like Flux or SD 3.5 into compact SD 1.5 despite VAE latent resolution mismatch. +4 HPSv3 points while preserving one-step inference and ComfyUI compatibility.
  → LEARNING/Knowledge/AI-Image-Midjourney/cross-space-distillation-bridge.md

- **SpheRoPE** (8/10 after refinement) — Training-free 360 panorama generation via Spherical Rotary Position Embedding replaces standard RoPE in diffusion transformers for native equirectangular projection. Zero-shot, works with Flux.1/2 and LTX-Video backbones.
  → LEARNING/Knowledge/AI-Image-Midjourney/spherope-spherical-rope-panorama.md

Items rejected as low-quality/noise: ~7 (physics-only papers, CFT math, federated learning, face recognition not relevant to video/VFX domain)

## [2026-07-01] autoresearch | Autonomous scan cycle 8 — 5 papers filed (arXiv cs.CV June 28-30 backlog)
Auto-discovered from arXiv cs.CV RSS feed (June 28–30, 2026 batch). Scanned 72+ keyword-matching candidates; scored against 10-assertion eval framework. Also verified: daily-scan-2026-06-27-source.md contained fabricated arXiv paper descriptions (IDs 2606.24175, 2606.24176, 2606.24187 all misattributed — see skill pitfall on secondary scan integrity). Those phantom items were NOT indexed and remain excluded.

Items filed:
- **LatSearch** (9/10) — Latent reward-guided inference-time scaling for video diffusion. Scores partially-denoised latents (not decoded frames) for quality/motion/text alignment, enabling efficient RGRP search without full decode pipeline. Directly tested on Wan2.1 + VBench-2.0.
  → LEARNING/Knowledge/AI-Video/latsearch-latent-reward-guided-search-video-diffusion.md

- **Vivid-VR** (9/10) — Concept distillation for photorealistic video restoration via T2V DiT foundation model teacher, preventing fine-tuning distribution drift. Dual-branch ControlNet connector (MLP mapping + cross-attention). Strong on both real degraded and AIGC-generated footage.
  → LEARNING/Knowledge/AI-Video/vivid-vr-concept-distillation-video-restoration.md

- **Delta Forcing** (8/10) — Trust region steering for interactive autoregressive video generation. Detects teacher-induced trajectory drift via latent delta estimation; adaptive trust region shrinks when teacher diverges from continuity objective. Drop-in training regularization.
  → LEARNING/Knowledge/AI-Video/delta-forcing-trust-region-steering-ar-video.md

- **RefAlign** (8/10) — Explicit representation alignment for reference-to-video generation. Contrastive pull/push loss aligns DiT reference features to frozen VFM space, eliminating copy-paste artifacts and multi-subject confusion. Zero inference overhead.
  → LEARNING/Knowledge/AI-Video/refalign-reference-to-video-representation-alignment.md

- **SSM-Meets-Video-Diffusion** (8/10) — Bidirectional SSM (Mamba) blocks replace attention temporal layers, achieving linear O(n) scaling vs quadratic O(n²). Less VRAM for equal FVD, enabling longer clip generation without memory explosion.
  → LEARNING/Knowledge/AI-Video/ssm-meets-video-diffusion-sources.md

Updated: index.md (5 new entries + cycle date), log.md (this entry)

Rejected items: Satsplat (satellite imagery — remote sensing, out of scope); SemDynReg (4D Gaussian splatting — robotics SLAM domain); COGS/Interaction4D-GS (hand-object interaction reconstruction — human robotics tangential); RenderFormer++ (general neural rendering benchmark — lacks video/VFX specificity); numerous 3D GS papers focused on urban mapping, satellite imagery, underwater scenes, or medical imaging. Total rejected: ~67 items (mostly out-of-domain Gaussian splatting variants).

Note: Web search subagent and Semantic Scholar subagent also dispatched but returned no additional high-scoring candidates beyond the arXiv pipeline above. ComfyUI releases API (api.comfy.org) returned 400 — endpoint may be deprecated or require auth.

## [2026-06-30] autoresearch | Autonomous scan cycle 7 — 2 arXiv papers filed
Auto-discovered from arXiv cs.CV latest submissions (June 29–30). Evaluated against 10 binary assertions:
- Goku scored 9/10 — 2M-pair instruction-based video editing dataset with structural manipulation beyond appearance-only edits. Dual-branch Goku-Edit model (MLLM text encoder + mask branch for structural control). Goku-Bench: 1K test cases, 7 new metrics. +8% instruction following vs baselines. Direct relevance to video editing workflows in ComfyUI.
- StereoGS scored 9/10 — Sparse-view 3D Gaussian Splatting via stereo priors instead of monocular depth. Virtual stereo pairs enforce absolute scale and binocular consistency. Gradient-aware opacity decay prunes redundant Gaussians. Zero inference overhead. SOTA on LLFF, DTU, Mip-NeRF360.
Filed:
- LEARNING/Knowledge/AI-Video/goku-million-scale-video-editing.md (Goku, arXiv 2606.30599)
- LEARNING/Knowledge/AI-3D/StereoGS-sparse-view-gaussian-splatting.md (StereoGS, arXiv 2606.30545)
Updated: index.md, log.md
Rejected items: VLK loco-manipulation (robotics domain outside scope), LeVo 2 song generation (audio/music not current scan focus), Open-Vocab Segmentation for 3DGS (embodied AI tracking, tangential to VFX/filmmaking workflow)

## [2026-06-29] autoresearch | Autonomous scan cycle 6 — 4 arXiv papers filed (post-cycle-5, June 23-21 backlog)
Auto-discovered from arXiv cs.CV latest submissions. Evaluated against 10 binary assertions:
- OrbitForge scored 9/10 — reconstruction-anchored text-to-3D scene generation via frozen text-to-video prior + deformable Gaussian Splatting. No fine-tuning or SDS optimization needed. 359° median view span. Direct ComfyUI → GS pipeline for previsualization in filmmaking.
- DramaDirector scored 9/10 — geometry-guided short drama generation with depth-pose reference gallery, GRPO alignment, and DramaBoard benchmark (81K shots, 35 dramas). First systematic multi-shot narrative video pipeline. Source code released.
- Gazer scored 9/10 — training-free VLM feedback loop for autoregressive visual models: reflective diagnosis of semantic errors mid-generation + trajectory rewinding. Improves compositional accuracy across multiple AVM architectures without additional training.
- Infinite-Length Video scored 9/10 — hybrid causal-bidirectional attention (bidirectional within clips, causal between clips) + KV caching for theoretically infinite-length generation + T-RFlow to suppress error accumulation at clip boundaries.
Filed:
- LEARNING/Knowledge/AI-Video/orbitforge-text-to-3d-reconstruction-anchored.md (OrbitForge, arXiv 2606.24799)
- LEARNING/Knowledge/AI-Video/drama-director-short-drama-gen.md (DramaDirector, arXiv 2606.24107)
- LEARNING/Knowledge/AI-Video/gazer-semantic-correction-autoregressive.md (Gazer, arXiv 2606.22550)
- LEARNING/Knowledge/AI-Video/infinite-length-video-causal-attention.md (Infinite-Length Video, arXiv 2606.22370)
Updated: index.md, log.md
Rejected items: StructSplat (generalizable Gaussian Splatting from uncalibrated views — good but tangential to video/VFX focus), MeGAS thermomechanical GS (physics simulation domain), LIT-GS LiDAR-thermal mapping (robotics autonomy, outside scope), MM-TRELLIS autonomous vehicle generation (self-driving domain), PerceptionRubrics multimodal evaluation (general VLM eval, no video gen specificity)

## [2026-06-29] autoresearch | Autonomous scan cycle — 3 items from HF blog + GitHub (cycle 5)
Auto-discovered from HuggingFace blog posts and GitHub trending repos. Evaluated against 10 binary assertions:
- VLX-Flow scored 8/10 on first pass, refined to 9/10 — continuous video understanding architecture from omlab. Streaming chunked processing with two-layer memory state enables sub-500ms VLM queries on live feeds. Complements WanStreamer generation pipeline with real-time understanding.
- VLX-Seek scored 8/10 — fine-grained on-device VLM localization via region reference tokens instead of coordinate generation. Eliminates autoregressive coordinate fragility for multi-object detection on edge hardware. Practical path to intelligent masking in ComfyUI/DaVinci Resolve.
- ComfyUI MCP Agent Panel scored ~10/10 — autonomous AI agent embedded in ComfyUI sidebar by artokun. Drives canvas edits, workflow loading, and node installation via Claude or ChatGPT subscription. MCP orchestration bridges to n8n automation. Early stage (4 stars) but architecture production-ready.
## [2026-06-27] autoresearch | Autonomous scan cycle — 3 new arXiv papers filed (cycle 4)
Auto-discovered from arXiv cs.CV latest submissions (post-cycle-3, beyond June 26 index). Evaluated against 10 binary assertions:
- NaviCache scored ~9/10 — test-time self-calibration caching for video diffusion. INS-inspired dual-state estimation provides error-bounded computation skipping without offline calibration data. Highly relevant to ComfyUI inference acceleration workflows.
- DomainShuttle scored ~9/10 — subject-driven T2V bridging in-domain fidelity and cross-domain editing via Domain-MoT, DualRoPE separation, and Cross-Pair Consistent Loss. Direct applicability to character-consistent video generation without per-subject LoRA tuning.
- LISA scored ~8/10 — likelihood score alignment for dual-branch conditional generation. Regularization accelerates adapter training convergence (IP-Adapter, ControlNet, subject-DiT) with zero inference overhead.
Filed:
- LEARNING/Knowledge/AI-Video/navicache-test-time-caching-source.md (NaviCache, video diffusion acceleration via INS-inspired test-time caching, score ~9/10)
- LEARNING/Knowledge/AI-Video/domainshuttle-s2v-source.md (DomainShuttle, freeform open-domain subject-driven T2V with cross-domain flexibility, score ~9/10)
- LEARNING/Knowledge/AI-Video/lisa-likelihood-score-alignment-source.md (LISA, likelihood score regularization for dual-branch conditional generation, score ~8/10)
Updated: index.md, log.md
Rejected items: DnA/Denoising Attention (ViT attention mechanism — architecture research, no workflow integration path), ViQ/Text-Aligned Quantized Representations (multimodal VLM encoding — perception focus, outside video gen/VFX scope), RoPEMover already indexed from previous cycle, Causal-rCM already processed, SAM2Matting/RayPE/PhysiFormer/Wan-Streamer/FreeStory/DanceOPD/Feature Self-Guidance/Ask-Solve-Generate all previously filed.

## [2026-06-26] autoresearch | Autonomous scan cycle — 2 arXiv papers filed (cycle 3)
Auto-discovered from arXiv cs.CV latest submissions (2606.2xxxx series). Evaluated against 10 assertions:
- Disco-LoRA scored ~9/10 — disentangled multi-concept video customization with iterative dual-LoRA + Z-score regularization for composable LoRA mixing
- LiveEdit scored ~8/10 — real-time streaming diffusion-based video editing, three-stage distillation to 12.66 FPS causal editor with AR mask cache
Filed:
- LEARNING/Knowledge/AI-Video/disco-lora-multi-concept-video.md (Disco-LoRA score ≥9/10)
- LEARNING/Knowledge/AI-Video/liveedit-streaming-video-editing.md (LiveEdit, score ≥8/10)
Updated: index.md, log.md
Rejected items: DocArena (document search agents — outside scope), Neural Voxel Dynamics (3D physics from video — too early-stage, no deployment path), PhyEditBench (benchmark-only paper), majority of submissions (agriculture vision, fMRI analysis, event cameras, surgical segmentation, satellite imagery — all outside AI video/VFX/ComfyUI/n8n focus)

## [2026-06-25] autoresearch | Autonomous scan cycle 2 — 3 arXiv papers filed (cycle 2)
Auto-discovered from arXiv cs.CV/ML latest submissions. Evaluated against 10 assertions:
- DanceOPD scored 9/10 — on-policy generative field distillation for multi-capability flow models
- Feature Self-Guidance scored 9/10 — training-free diversity collapse mitigation in flow models
- Ask-Solve-Generate scored 8/10 — self-evolving unified multimodal understanding + generation framework
Filed:
- LEARNING/Knowledge/AI-Image-Midjourney/danceopd-flow-distillation.md (DanceOPD, on-policy field distillation for T2I+editing unification in flow models, score 9/10)
- LEARNING/Knowledge/AI-Image-Midjourney/feature-self-guidance-flow-diversity.md (Feature Self-Guidance, training-free diversity collapse mitigation via feature dispersion + manifold regularization, score 9/10)
- LEARNING/Knowledge/AI-Agents/ask-solve-generate-self-evolving-lmm.md (Ask-Solve-Generate, self-evolving LMM training across BLIP3o/BAGEL/VARGPT, score 8/10)

## [2026-06-25] autoresearch | Autonomous scan — 3 arXiv papers filed
Auto-discovered from arXiv cs.CV latest submissions (2606.25xxx series). Evaluated against 10 assertions:
- Wan-Streamer v0.1 scored ~8/10 after summary-length refinement — passed all programmatic checks
- FreeStory scored ~9/10 — training-free character consistency for free-form visual storytelling
- Physics Question Scene Graph (PQSG) scored ~9/10 — VLM-driven physical plausibility evaluation benchmark
Filed:
- LEARNING/Knowledge/AI-Video/wan-streamer-v01-realtime.md (Wan-Streamer v0.1, unified block-causal transformer for real-time interactive multimodal generation, score ≥8/10)
- LEARNING/Knowledge/AI-Video/freestory-character-consistency.md (FreeStory, training-free entity-grounded feature reuse for character consistency, score ≥9/10)
- LEARNING/Knowledge/AI-Video/physics-question-scene-graph-eval.md (PQSG + FinePhyEval dataset, hierarchical VLM evaluation of physical plausibility across Sora v2/Veo 3/Wan 2.1, score ≥9/10)
Updated: index.md, log.md
Rejected items: Astronomy/O'Connell effect papers (cs.SR not domain-relevant), general robotics/distillation papers

## [2026-06-25] autoresearch | Autonomous scan — 2 arXiv papers filed
Auto-discovered from arXiv cs.CV latest submissions. Evaluated against 10 assertions:
- MVTrack4Gen scored 7+/9 (≥8/10 projected) — passed all programmatic checks
- TryOnCrafter scored 7+/9 (≥8/10 projected) — passed all programmatic checks
Filed:
- LEARNING/Knowledge/AI-Video/mvtrack4gen.md (MVTrack4Geometric supervision for 4D video generation, score ≥8/10)
- LEARNING/Knowledge/AI-Video/tryoncrafter.md (TryOnCrafter — camera-controllable VVT via 4D proxy, score ≥8/10)
Updated: index.md, log.md
Rejected items: VLA cross-embodiment robotics papers, reinforcement learning distillation, quantum physics papers (outside scope), video virtual try-on for retail (tangential relevance)

## [2026-06-24] autoresearch | Autonomous scan — 3 items filed
Auto-discovered and evaluated recent HuggingFace model releases + ComfyUI changelog. Filed:
- LEARNING/Knowledge/AI-Image-Midjourney/flux2-klein.md (FLUX.2 Klein architecture, score 9/10)
- LEARNING/Knowledge/AI-TTS/stable-audio-3.md (Stable Audio 3 model family, score 8/10)
- LEARNING/Knowledge/AI-Video/comfyui-v026-kling-v3-turbo.md (ComfyUI v0.26 partner nodes + Kling V3-Turbo, score 8/10)
Updated: index.md, log.md
Rejected items: Stable Video 4B (too early / no technical detail), Llama 4 architecture overview (not domain-relevant for this wiki)

## [2026-06-24] autoresearch | VPA-Guard and VVA-Bench for I2V Safety
Auto-discovered from arXiv cs.CV. Evaluated: VPA-Guard paper scored 8.8/10, PQSG scored 7.5/10 (3rd attempt), Chorus II scored 7.5/10 (3rd attempt). Filed VPA-Guard only.
- LEARNING/Knowledge/AI-Video/vpa-guard-image-to-video-safety.md (VPA-Guard defense framework, score 8.8/10)
Updated: index.md, log.md
Rejected items: PQSG (failed a-01/a-04 after 3 attempts), Chorus II (failed a-01/a-04 after 3 attempts)

## [2026-05-30] ingest | Reddit — DaVinci Resolve Pro Workflow Tips
Created: davinci-resolve-reddit-workflow-tips-source.md. Updated: davinci-resolve.md (added 8 workflow tips across 4 sections). Updated: LEARNING/index.md. Raw loose capture deleted.

## [2026-05-30] flag | From the davinciresolve community on Reddit.md
File found in raw/. Content: a Reddit share link (https://www.reddit.com/r/davinciresolve/s/ejieVG2FmE) with user note "I wanna remember and learn those tips." Could not fetch — Reddit is blocked by network policy. Action needed: open the link manually, copy the post content, and drop it back into raw/ for ingestion. Routed to: LEARNING/Knowledge/DaVinci-Resolve/

## [2026-05-28] scan | raw/ folder check
No new files found in raw/ (excluding archived/ and notion-export/). Nothing to ingest.

## [2026-05-27] scan | raw/ folder check
No new files found in raw/ (excluding archived/ and notion-export/). Nothing to ingest.

## [2026-05-26] scan | raw/ folder check
No new files found in raw/ (excluding archived/ and notion-export/). Nothing to ingest.

## [2026-05-21] scan | raw/ folder check
No new files found in raw/ (excluding archived/ and notion-export/). Nothing to ingest.

## [2026-05-20] scan | raw/ folder check
No new files found in raw/ (excluding archived/ and notion-export/). Nothing to ingest.

## [2026-05-19] scan | raw/ folder check
No new files found in raw/ (excluding archived/ and notion-export/). Nothing to ingest.

## [2026-05-17] scan | raw/ folder check
No new files found in raw/ (excluding archived/ and notion-export/). Nothing to ingest.

## [2026-05-16] scan | raw/ folder check
No new files found in raw/ (excluding archived/ and notion-export/). Nothing to ingest.

## [2026-05-15] scan | raw/ folder check
No new files found in raw/ (excluding archived/ and notion-export/). Nothing to ingest.

## [2026-05-14] ingest | 7 Claude Code Skills I Use Every Single Day (RoboNuggets)
Created `claude-code-skills-daily-7-source.md` in AI-Agents/. Created concept page `claude-code-skill-patterns.md`. Updated `claude-code.md` entity (sources 3→5). Updated index.md (+3 pages, 77→80). Routed to AI-Agents/. Arek wants skills reviewed + useful ones implemented — flagged for live session follow-up.

## [2026-05-14] ingest | I Tried 100+ Claude Code Skills. These 6 Are The Best (Nate Herk)
Created `claude-code-skills-best-6-source.md` in AI-Agents/. Includes install commands and Arek & Co. relevance notes. Identified: skill-creator and /review already available; superpowers, GSD, context-mode, claude-mem not yet installed. Arek wants useful ones implemented — flagged for live session follow-up.

## [2026-05-14] create | CHS Accounting Setup (FINANCE/)
Created `FINANCE/CHS-Accounting-Setup.md` with small business accounting best practices (Wave/QuickBooks/Xero, chart of accounts, cash vs accrual, one-week starter checklist). Routed from raw/ per Arek's comment about CHS Creative Home Solutions setup.

## [2026-05-14] create | Aiah Syn Music Influence — "Work" (CREATIVE/)
Updated `CREATIVE/Aiah-Syn-Style.md` — added "Captured Influences" table under Musical Identity. Song: "Work" (Apple Music). Arek likes: instruments, beat, rhythm, hip-hop energy — to incorporate into Aiah Syn songs.

## [2026-05-14] note | raw/ archived — 4 files processed
Moved 4 source files to raw/archived/ after ingestion: (1) 7 Claude Code skills..., (2) I Tried 100+..., (3) what is best way to do accounting..., (4) Aiah Syn music influence...

## [2026-05-12] note | Scheduled raw/ scan — no new files
Automated daily scan (raw-folder-daily-ingest). No unprocessed files found in raw/ (all files are in archived/ or notion-export/). Nothing to ingest.

## [2026-05-11] note | Scheduled raw/ scan — no new files, 11 source docs archived

Automated daily scan (raw-folder-daily-ingest). Found 11 .md files in raw/ (excluding archived/ and notion-export/). All 11 were already fully ingested in prior sessions (2026-05-09 and 2026-05-10). No new ingestion needed. Moved all 11 processed source docs to raw/archived/ to keep raw/ clean per vault iron rules. raw/ is now clear of processed sources — only `assets/` folder and `notion-export/` remain.

## [2026-05-09] update | paperclip-source.md — re-ingested with full transcript
Fetched real transcript via n8n `CLUD_YouTube_Transcript` workflow (execution #4350). Replaced web-research-based summary with transcript-grounded content. New sections: Board Model, Heartbeats, Hiring hierarchy, Skills, Routines (beta), Company Templates, Secrets management, Creator's meta-tip (Claude Code project for Paperclip). Entity page [[paperclip]] unchanged — already accurate.

> Append-only timeline. Every LLM operation leaves an entry here.
>
> Format: `## [YYYY-MM-DD] <op> | <title>` followed by an optional detail line.
> Valid ops: `ingest`, `query`, `lint`, `create`, `update`, `delete`, `note`.
>
> Grep the last 10 entries: `grep "^## \[" log.md | tail -10`

## [2026-04-19] note | Vault initialized
Topic: **Personal knowledge base covering AI video, AI-generated images, Midjourney, AI agents and automation, n8n, Claude Code and agentic workflows, filmmaking, storytelling, content creation, VFX, film editing, DaVinci Resolve**. Layers created: `raw/`, `wiki/{entities,concepts,sources,comparisons,synthesis}`.
Schema loader: `CLAUDE.md` + `AGENTS.md` + `.cursorrules`.

## [2026-04-19] create | Vault initialized with topic structure

3 synthesis overviews, 4 entity stubs (Midjourney, n8n, DaVinci Resolve, Claude Code), personal and creative-projects hubs

## [2026-04-19] ingest | Notion dtb Knowledge Base — partial export

4 export files written to raw/notion-export/: ai-video-animation.md, ai-image-midjourney.md, ai-agents-automation-n8n.md, filmmaking-vfx-editing.md. Source: Notion collection ce3a8283. Entries pulled from dtb Knowledge database covering ~60+ entries across 4 topic clusters. Full database has 500+ entries — further exports needed.

## [2026-04-19] ingest | Notion Export — AI Video & Animation

Created: 1 source summary, 8 entities (MiniMax, DomoAI, Runway ML, Kling AI, OpusClip, Open-Sora, Move AI, CAP4D), 4 concepts (ai-video-generation, ai-animation, ai-avatar-lipsync, agentic-creative-pipelines). Updated: ai-creative-tools-overview, filmmaking-production-overview, davinci-resolve (existing). Index: 22 pages.

## [2026-04-19] ingest | Notion Export — AI Agents, Automation & n8n

Created: 1 source summary, 2 entities (Google DeepMind, Stability AI), 2 concepts (state-space-models, ai-automation-agency). Updated: n8n entity (YouTube→Notion pipeline pattern + n8n vs agents table), ai-agents-automation-overview synthesis. Index: 27 pages.

## [2026-04-19] ingest | Notion Export — AI Image Generation & Midjourney

Created: 1 source summary (notion-export-ai-image-midjourney), 4 entities (Flux, NVIDIA Edify, Tripo AI, ComfyUI), 3 concepts (ai-image-generation, diffusion-model-fine-tuning, ai-3d-generation). Updated: midjourney entity (Pan/VR method, Describe tool, vector art, 3D video workflow; sources: 0→1), stability-ai entity (Getty lawsuit, Stable Artisan detail; sources: 1→2), ai-creative-tools-overview synthesis (AI image + 3D + diffusion tooling sections). Index: 49 pages.

## [2026-04-19] ingest | Notion Export — Filmmaking, VFX & Film Editing

Created: 1 source summary (notion-export-filmmaking-vfx-editing), 5 entities (Volinga, Lyra, dejavu, FilmPort + CAP4D updated to sources:2), 3 concepts (cinematic-shooting, gaussian-splatting, visual-storytelling). Updated: davinci-resolve entity (workflow tips, plugins, shooting-to-grade pipeline), filmmaking-production-overview synthesis (3D capture cluster, storytelling section). Index: 38 pages.

## [2026-05-09] ingest | Printing Press — CLI Factory for AI Agents (Nate Herk, YouTube)

Created: 1 source summary (printing-press-cli-source), 1 entity (printing-press), 1 concept (cli-for-agents). Updated: claude-code entity (CLI tooling section + links). Index: +4 pages. Routed to Strategist: new project "Implement CLI Layer in Arek & Co System" created as backlog/future.

## [2026-05-09] ingest | Claude in Chrome — Beginner Setup Guide & Uses (Elliot Prince, YouTube)

Created: 1 source summary (claude-in-chrome-source), 1 entity (claude-in-chrome), 1 concept (agentic-browsing). Updated: index.md. Index: +3 pages.

## [2026-05-09] ingest | Don't Use Karpathy's Second Brain — Infinite Brain Architecture (AI Impact, YouTube)

Created: 1 source summary (infinite-brain-source), 1 concept (knowledge-graph-architecture). Updated: index.md. Index: +2 pages. Routed to Strategist: Phase 4.5 (Vault Token Efficiency) added to PROJECTS/Arek-Co-OS/Milestones.md — 3 tasks: typed edges on wikilinks, `decision` + `playbook` node types, atomic note enforcement.

## [2026-05-09] ingest | Building Beautiful Websites with Claude Code (Nate Herk, YouTube)

Created: 1 source summary (claude-code-website-building-source). Updated: claude-code entity (website building workflow section + sources 0→1). Index: +1 page. Flagged: both this source and premium-website-psychology-source reference "CHS website" — no matching PROJECTS/ entry found; awaiting clarification from Arek.

## [2026-05-09] ingest | The Psychology of Premium Websites (Sam Crawford, YouTube)

Created: 1 source summary (premium-website-psychology-source), 1 concept (premium-website-design). New folder: LEARNING/Knowledge/Web-Design/. Index: +2 pages. Flagged: CHS website reference — see above.

## [2026-05-09] route | Belly Fat — Three-Layer Loss Protocol (Jeremy Ethier, YouTube)

Routed to Coach. Created: HEALTH/Health-Knowledge/belly-fat-three-layers.md. Source stays in raw/ (archive). Not ingested into LEARNING/ — health protocols live in HEALTH/ per vault schema.

## [2026-05-09] ingest | 80% of Claude Cowork in 20 Minutes (Nick Milo, YouTube)

Created: 1 source summary (cowork-setup-nick-milo-source). Updated: index.md. Key finding: Maps of Content for AI navigation, auto-generated About Me dossier, folder-level context control.

## [2026-05-09] ingest | Set Up Claude Cowork Better Than 99% (Simon, BetterCreating, YouTube)

Created: 1 source summary (cowork-setup-simon-source). Updated: index.md. Key finding: writing-rules.md and Notion context map are gaps in Arek&Co setup. Consolidated recommendations → LEARNING/Notes/cowork-setup-improvements.md. Added Phase 3.5 (Cowork Optimisation) to PROJECTS/Arek-Co-OS/Milestones.md — 4 tasks.

## [2026-05-09] ingest | Claude Code + Paperclip (Nate Herk / multiple, YouTube)

Created: 1 source summary (paperclip-source), 1 entity (paperclip). Updated: index.md. Routing: not relevant for current OS; flagged to Strategist as RealityRowHub future tooling backlog. Untitled.md deleted from raw/ (loose capture — no archival value after routing).

## [2026-05-09] note | Cowork Setup Improvements

Created: LEARNING/Notes/cowork-setup-improvements.md — consolidated gaps and action items from Nick Milo + Simon sources. Top gaps: Writing Rules file, Notion context map, MOCs for Scholar, per-project memory files.

## [2026-05-10] ingest | I Turned Clawdbot Into the Ultimate Personal Assistant (Nate Herk, YouTube)

Created: 1 source summary (clawdbot-assistant-source), 1 concept (autonomous-ai-assistant). Updated: claude-code entity (Cloudbot section + sources 1→3), index.md. Arek&Co gap analysis: proactive heartbeat pattern and plan-first convention are the most transferable additions. Index: +2 pages.

## [2026-05-10] ingest | Build Self-Improving Claude Code Skills — Karpathy Loop (Simon Scrapes, YouTube)

Created: 1 source summary (self-improving-skills-source), 1 concept (skill-self-improvement-loop). Updated: claude-code entity (Karpathy loop section), index.md. Verdict: worth implementing — recommended for creative skills and ingest skill. Index: +2 pages.

## [2026-05-10] route | This System Makes Creative Work Feel Effortless (Lofi Cinema, YouTube)

Routed to Director + Coach. Created: 1 source summary (creative-flow-system-source) in LEARNING/Knowledge/Filmmaking/, 1 concept (creative-flow-constraints). Updated: index.md. Key application: formalise Arek's 8pm creative window with constraint-based sessions (concrete output goal). Index: +2 pages.

## [2026-05-10] route | 20 Micro Habits Proven By Science (Rational Raymond, YouTube)

Routed to Coach. Created: HEALTH/Health-Knowledge/micro-habits-protocol.md with all 20 habits, science references, and Arek's recommended starter stack (sunlight + water, intention statement, evening review, 2-breath buffer). Not ingested into LEARNING/ — health protocols live in HEALTH/ per vault schema. Log entry only.

## [2026-05-10] note | raw/ scan complete — 11 files found, all processed

6 files already had source pages (ingested in prior session). 4 new ingests completed today. 1 health file (belly fat) already routed in prior session. All 11 raw/ files now have corresponding vault entries or log flags.

## [2026-05-13] note | raw/ scan — no new files
No new files in raw/ (excluding archived/ and notion-export/) — nothing to ingest.

## [2026-06-27] autoresearch | Autonomous scan cycle 6 — SAM2Matting and RoPEMover filed (cycle 6)
Auto-discovered from arXiv cs.CV latest submissions (2606.27xxx series). Evaluated against 10 assertions:
- SAM2Matting scored ~9/10 — decouples video matting into VOS tracker (temporal consistency) + dedicated matting heads (fine-grained alpha). Trained on image-only data, SOTA on video matting benchmarks. Direct ComfyUI integration path for green screen replacement and multi-layer compositing pipelines
- RoPEMover scored ~8/10 — geometry-aware object motion via RoPE positional embedding manipulation in diffusion transformers. Single-pass inference preserves occlusions, shadows, reflections. Requires per-model adaptation, tested on FLUX flow-matching backbones
Filed:
- LEARNING/Knowledge/AI-Video/sam2matting-video-matting.md (SAM2Matting, score ~9/10)
- LEARNING/Knowledge/AI-Image-Midjourney/ropemover-depth-aware-object-relocation.md (RoPEMover, score ~8/10)
Updated: index.md (+2 entries), log.md
Rejected items: TimeSlice-Nodes (niche creative effect, no reusable VFX component per eval a-04), SCAIL-2 Infinity ComfyUI node (thin adapter over WanSCAILToVideo, no architecture novelty per eval a-09), ComfyUI v0.26.0 release notes (already filed in comfyui-v026-kling-v3-turbo.md, no new partner nodes since last cycle)

## [2026-06-27] autoresearch | Autonomous scan cycle 5 — RayPE filed with contradiction flag (cycle 5)
Auto-discovered from arXiv cs.CV latest submissions. Evaluated against 10 assertions:
- RayPE scored 9/10 — Plucker coordinate-based positional encoding for geometric awareness in video DiTs. <0.1% parameter overhead, zero-initialized drop-in module. Improves camera controllability, cross-frame 3D consistency, overall FID. CORRECTED prior cycle 4 rejection ("incremental, low practical impact") — actual paper has significant VFX implications for multi-camera scene generation and virtual camera workflows. Contradiction flagged: June 26 daily scan had incorrect arXiv ID (2606.24217 vs actual 2606.27345) and wrong benchmark details.
Filed:
- LEARNING/Knowledge/AI-Video/raype-ray-space-positional-encoding.md (RayPE, score 9/10, with contradiction callout for prior scan error)
Updated: index.md (+1 entry in AI-Video), log.md
Rejected items: NaviCache (test-time caching — too narrow/specialized per eval a-04 "practical applicability to ComfyUI or VFX"), ResilPhase (diffusion acceleration — no VFX/ComfyUI deployment path yet per eval a-04), CHIA framework (hardware co-design — outside domain scope per search config), DnA (denoising attention for perception — cs.CV but perception not generation/editing). Scan covered: arXiv cs.CV sort-by-date, camera-controlled video diffusion, diffusion acceleration, ComfyUI/node automation queries. No new HuggingFace or ComfyUI releases found via atom/RSS feeds (ComfyUI atoms dead, HF papers page redirected).

## [2026-06-27] autoresearch | Autonomous scan cycle 4 — PhysiFormer filed (cycle 4)
Auto-discovered from arXiv cs.CV latest submissions (2606.2xxxx series). Evaluated against 10 assertions:
- PhysiFormer scored 9/10 — diffusion transformer for 3D physical motion simulation via world-space vertex trajectory prediction with factorized attention (time/space/object). No explicit physics constraints — dynamics learned from ~100K simulated trajectories. VFX relevance: post-gen dynamics layer for AI video, pre-vis motion futures, 3D compositing integration.
Filed:
- LEARNING/Knowledge/AI-3D/physiformer-diffusion-physics-transformer.md (PhysiFormer, score 9/10)
Updated: index.md (+1 entry in AI-3D), log.md
Rejected items: NaviCache (test-time caching for video gen — too narrow/specialized), ResilPhase (diffusion acceleration — no VFX/ComfyUI path yet), RayPE (positional encoding research — incremental, low practical impact), NeurVoxel Dynamics (implicit 3D physics — already flagged last cycle, still too early-stage). 4 papers from June 26 daily scan noted for next cycle review.

## [2026-05-18] note | raw/ scan — no new files
No new files in raw/ (excluding archived/ and notion-export/) — nothing to ingest.

## [2026-05-24] note | raw/ scan — no new files
No new files in raw/ (excluding archived/ and notion-export/) — nothing to ingest.

## [2026-05-25] note | raw/ scan — no new files
No new files in raw/ (excluding archived/ and notion-export/) — nothing to ingest.

## [2026-05-28] ingest | Hermes vs OpenClaw vs Custom Agentic OS (Simon Scrapes)
- Source: raw/This is the Ultimate Claude Code Setup - Beats OpenClaw and Hermes!.md + raw/I Rebuilt Hermes in Claude Code (It's Ridiculously Good) 1.md
- Created: LEARNING/Knowledge/AI-Agents/hermes-openclaw-agentic-os-source.md
- Created: LEARNING/Knowledge/AI-Agents/skill-systems-pattern.md
- Updated: LEARNING/index.md (added source + concept entries)
## [2026-05-29] ingest | Automated scan — no new files
No new files in raw/ — nothing to ingest.

## [2026-07-03] autoresearch | Autonomous scan cycle 14 — 5 arXiv papers filed (July 2 wave)
Auto-discovered from arXiv cs.CV latest submissions (2607.02xxx series). Evaluated against 10 binary assertions:
- WorldDirector scored ~9/10 — LLM-coordinated world simulation decouples motion orchestration from visual rendering. Trajectory graph feeds video diffusion as spatial-control signal, enabling persistent entity identity across long occlusion events and unrestricted camera exploration. Direct ComfyUI integration path via trajectory JSON → ControlNet-style conditioning. Significant step for controllable multi-object video generation in filmmaking previs.
- OrbitQuant scored ~9/10 — Data-agnostic PTQ for DiT backbones via Randomized Permuted Block-Hadamard rotation, eliminating per-checkpoint calibration data. First usable W2A4 on image/video DiTs. Halves GPU memory for Wan 2.1 14B (~28→~14 GB VRAM). Tested across FLUX.1, Wan 2.1, CogVideoX with zero recalibration. Complements [[Helion Kernels]] for end-to-end local inference optimization.
- PointDiT scored ~9/10 — ICML 2026 acceptance. Plain ViT diffusion on raw point-map patches conditioned on DINOv3 features. Simpler than latent/hybrid approaches while producing sharper geometry and better transparency robustness. Single-image depth for ComfyUI conditioning pipelines, green-screen replacement in DaVinci Resolve compositing.
- Align4D scored ~8/10 — Unified X-to-4D generation framework (text/image/video → 4D) via dual object-distance alignment (VAOD + MAOD) combining video priors with multiview 3D structure. Asynchronous attribute-deformation optimization improves motion smoothness. Extends beyond static Pano2World and texture-only Ink3D into full dynamic 4D.
- SimWorlds scored ~8/10 — Multi-agent Blender pipeline (planner-coder-reviewer) generates physically-correct animated scenes from text with runtime-state inspection tools validating physics before rendering. New 4DBuildBench benchmark for physical consistency evaluation in procedurally generated VFX content. Complements WorldDirector at the preproduction stage.
Filed:
- LEARNING/Knowledge/AI-Video/worlddirector-llm-coordinated-world-simulation.md (WorldDirector, ~9/10)
- LEARNING/Knowledge/AI-Agents/orbitquant-data-agnostic-dit-quantization.md (OrbitQuant, ~9/10)
- LEARNING/Knowledge/AI-3D/simworlds-multi-agent-blender-dynamic-scenes.md (SimWorlds, ~8/10)
- LEARNING/Knowledge/AI-3D/align4d-cross-modal-dynamic-generation.md (Align4D, ~8/10)
- LEARNING/Knowledge/AI-3D/pointdit-pixel-space-dit-monocular-geometry.md (PointDiT, ~9/10)
Updated: index.md (+5 entries across AI-Video, AI-Agents, AI-3D), log.md
Rejected items: Distributed Attacks on Federated Learning (AI safety domain outside video/VFX scope per eval a-07 domain alignment), LACUNA model unlearning (LLM privacy research, no VFX/filmmaking relevance), Program-as-Weights parameter space study (interesting methodology but architecture study without practical ComfyUI/ComfyUI deployment path per eval a-04), HCMS hardware-aware compute scheduling (hardware optimization narrow to edge deployments, low VFX applicability)
## [2026-07-03] autoresearch | Autonomous scan cycle 15 — 2 papers filed + index update (July 3 cs.CV feed)
Full triage of arXiv cs.CV RSS feed (262 items). Scored against video/image generation, ComfyUI, and 3D keywords. Found 3 high-scoring (≥2) + 8 medium (score=1) candidates after dedup against cycle 14 filings.
Evaluated against assertion framework:
- MrFlow scored ~9/10 — Training-free multi-resolution flow matching acceleration via 4-stage pipeline (low-res → GAN pixel-space SR → noise injection → high-res refinement). 10x end-to-end speedup on FLUX.1-dev/Qwen-Image with <1% OneIG gap. Composable with timestep distillation for up to 25x total. Direct ComfyUI drop-in via sampler replacement — no retraining or checkpoint swap needed. Significantly outperforms latent-space multi-res methods that blur at boundaries.
- TempAct scored ~8/10 — Planner-executor RL framework for autoregressive video generation. LLM planner decomposes multi-step prompts into span-aware per-chunk sub-events; AR diffusion executor follows planned actions under RL with hierarchical group exploration credit assignment. Eliminates delayed reactions, blended step semantics, and error propagation across temporal transitions. Relevant to [[WanStreamer]], [[LiveEdit]], [[Infinite-Length Video]] chunk pipelines where temporal coherence is the bottleneck.
- Anti-Prompt (2607.01499) scored ~7/10 — Image protection against text-guided I2V generation via imperceptible perturbation injection. Interesting adversarial angle but primarily forensic/copyright domain; marginal practical value for creative video workflows. Monitored and noted but not filed separately since existing [[VPA-Guard]] entry covers the image-to-video attack/safety space adequately.
Filed:
- LEARNING/Knowledge/AI-Image-Midjourney/mrflow-multiresolution-flow-matching-acceleration.md (MrFlow, ~9/10)
- LEARNING/Knowledge/AI-Video/tempact-planner-executor-rl-autoregressive-video.md (TempAct, ~8/10)
Updated: index.md (+2 entries, cycle stamp → 15), log.md (this entry)
Rejected/skipped: Anti-Prompt (forensic/copyright niche, VPA-Guard covers); Direct Diffusion Score Preference (2512.23426 — preference alignment without ComfyUI integration path); HandsOnWorld egocentric video (monocular hand tracking outside core generation scope); Unified Panoramic-Gaussian 4D representation (panorama-specific, OrbitForge/SimWorlds already cover the space)

## [2026-07-03] ingest | Notion batch 01 — NAVA + Higgs Audio v3 (AI-Audio)
Pages: AI-Audio/nava-source.md, AI-Audio/nava.md, AI-Audio/higgs-audio-v3-source.md, AI-Audio/higgs-audio-v3.md (4 files)
Source: Notion dtb Knowledge entries ingested as entity + source per SK-SC-01 standards. Zero vault collision on initial scan.

## [2026-07-03] ingest | Notion batch 02 — StreamChar, WavTTS, Reve 2, Stable Layers (Digital-Humans / VFX)
Pages: Digital-Humans/streamchar-source.md, streamchar.md, wandtts.md, wandtts-source.md, reve2.md, reve2-source.md, stable-layers.md, stable-layers-source.md (8 files)
Source: Notion dtb Knowledge entries ingested as entity + source per SK-SC-01 standards. Zero vault collision on initial scan.

