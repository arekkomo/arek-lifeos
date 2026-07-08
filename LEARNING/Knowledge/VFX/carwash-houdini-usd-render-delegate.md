---
title: "CarWash — Houdini/Solaris to AI-Generated Video Render Delegate"
category: entity
summary: "Hydra render delegate that conditions LTX-2.3 video generation on actual Houdini USD scene shading via ComfyUI, enabling scene-grounded AI video in a production VFX pipeline."
tags: [comfyui, houdini, solaris, hydra, usd, ltx-video, vfx-pipeline, ai-render-delegate]
sources: 2
updated: 2026-07-06
---

## About

CarWash is a Houdini/Solaris **Hydra render delegate** that converts USD scenes into AI-generated video sequences via [[ComfyUI]] and [[LTX-2.3 Model Architecture]]. Instead of traditional rasterization, it uses the scene's actual shaded lighting as conditioning input for diffusion-based video generation. The generated output respects real composition, lighting, and color geometry from USD — not just depth-pass approximation.

Appears as a renderer in Houdini's render settings. Runs asynchronously within Solaris (LOP), keeping the viewport responsive while frames generate on GPU.

## By

Joseph O. Ibrahim (2026). Proprietary license. Windows-only (10/11, 64-bit). Target build: Houdini 21.0.729.

## Key Architecture

- **USD Hydra receive**: Imports geometry, cameras, lights from Solaris viewport
- **Deterministic CPU rasterizer**: Produces AOVs — shaded color, depth, world normals, per-object prim IDs
- **Color conditioning**: Shaded color PNG uploaded as first-frame I2V conditioning (depth/normal AOVs reserved for future control inputs)
- **Generate-once convergence**: Hashes conditioning + style params to skip regeneration of unchanged scenes. Only re-submits when geometry, camera, light, or prompt changes
- **Async LTX-2.3 workflow**: 22B distilled transformer on GPU (~22 GB VRAM). Gemma 3 12B text encoder runs on CPU (offloaded from VRAM), leaving ~2 GB headroom
- **Delivery to directory**: 25-frame sequence + `carwash.json` metadata sidecar. Frame 0 shown as live viewpreview in Houdini
- **Renderer settings tab**: Controls prompt, negative prompt, inference steps, guidance scale, seed, deterministic mode, control strength, timeout, and backend selection (LTX-2 / FLUX / Cosmos)

## Capabilities

- Live progress feedback via Houdini's status bar with step count and completion percentage
- Frame-exact frame-rate synchronization in A/B comparison of upscale vs. interpolation results
- Multi-backend support: LTX-2.3 (primary), FLUX, SVD, Kling, Veo, Runway (planned)
- Generate-once-and-converge prevents wasted regeneration on static USD state
- FP8 quantization for transformer weights to fit 22B model on RTX 4090 (24 GB VRAM)

## VFX / Filmmaking Applications

- **Previs with AI enhancement**: Artists block geometry and lighting in Houdini, get photoreal AI-rendered output without waiting for heavy ray-trace passes
- **Lookdev iteration**: Change materials or lighting in Solaris — CarWash re-submits only when conditioning changes, surfacing visual difference within seconds
- **Stylized renders**: Use prompt to inject artistic style (e.g., "ink wash painting", "cell-shaded anime") on top of physically-correct USD composition
- **Multi-shot consistency**: Same seed + deterministic mode ensures identical regeneration for unchanged shots across a sequence
- **Compositing pipeline**: Output EXR or PNG sequences integrate directly into [[DaVinci Resolve]] or Nuke downstream workflows

## How to Run / Get Started

```bash
# Build plugin (Windows MSVC)
cmake -B build -G "Visual Studio 17 2022" -A x64 ^
  -DCMAKE_PREFIX_PATH="C:\Program Files\Side Effects Software\Houdini 21.0.729"
cmake --build build --target hdCarWash --config Release

# Deploy plugin (Python script)
python deploy_hdcarwash.py      # copies DLL + plugInfo + resources
python deploy_hdcarwash.py --skip-build  # skip rebuild if not needed
```

Required models:
- LTX-2.3 22B distilled UNet transformer (~22 GB, FP8): `ltx-2.3-22b-distilled_transformer_only_fp8_input_scaled_v3`
- Checkpoint config + tokenizer: `ltx-2.3-22b-distilled-fp8.safetensors`
- Gemma 3 12B IT FP4 mixed (text encoder, CPU-offloaded): `gemma_3_12B_it_fp4_mixed.safetensors`
- LTX full spatial VAE (bf16, ~1.35 GB): `LTX23_video_vae_bf16.safetensors`

```bash
# Or use provided model downloader
.\download_models.ps1
```

**System requirements:** GPU ≥ 24 GB VRAM (RTX 4090 tested). ComfyUI reachable on `localhost:8188` with LTX-2.3 nodes installed. Firewall must permit local WebSocket/HTTP connections.

> **VAE note**: Full 3× spatial VAE required (`LTX23_video_vae_bf16`). TAESD variant uses 16× spatial compression — incompatible with the node's latent allocation at `height // 32`.

## References

- [[ComfyUI]] — Node-based diffusion interface
- [[LTX-2.3 Model Architecture]] — Dual-stream DiT backbone
- [[AI Video Generation]] — Diffusion for film, VFX
- Houdini USD/Hydra: https://www.sidefx.com/docs/houdini/solaris/hydra_intro.html
- NVIDIA nvidia-vfx path used by install scripts: `nvidia-vfx.VideoSuperRes`
