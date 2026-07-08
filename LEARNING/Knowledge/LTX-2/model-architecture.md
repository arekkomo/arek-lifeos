---
title: LTX 2.3 Model Architecture
category: entity
summary: Complete architecture deep-dive for LTX-2.3 — dual-stream DiT, 14B video + 5B audio streams, Gemma 3 text encoder, VAE codecs, RoPE schemes, transformer block internals
tags: [ltx-2, ltx-2.3, architecture, diffusion-transformer, model, audio-video, gemma-3, vae, transformer, rope]
sources: 3
updated: 2026-07-04
---

# LTX 2.3 Model Architecture

## Overview
LTX-2 is the **first DiT-based audio-video foundation model** that generates synchronized audio and video jointly — unlike sequential T2V→V2A pipelines, it captures true joint dependencies between visual and auditory signals.

**Reference**: [[github:LTX-2]] [[tech-docs:ltx-core]]
## Core Architecture

### Asymmetric Dual-Stream Transformer (48 Blocks)

LTX-2 processes video and audio tokens through a **asymmetric dual-stream diffusion transformer** with 48 layers:

| Component | Parameters | Purpose |
|-----------|-----------|---------|
| Video Stream | 14B | Spatiotemporal dynamics |
| Audio Stream | 5B | 1D temporal audio synthesis |
| Transformer Blocks | 48 shared | Bidirectional cross-modal attention between streams |

### Key Design Principles

- **Decoupled Latent Representations**: Separate modality-specific VAEs enable different positional encodings, independent compression optimization, and native V2A/A2V editing workflows
- **Asymmetric Dual-Stream**: Different widths for each modality reflect their distinct information densities
- **Bidirectional Cross-Modal Attention**: 1D temporal RoPE enables sub-frame alignment, mapping visual cues to auditory events (lip-sync, foley, environmental acoustics)
- **Cross-Modality AdaLN**: Scaling/shift parameters conditioned on the other modality's hidden states for synchronization across differing diffusion timesteps/temporal resolutions

### Transformer Block Architecture

Each dual-stream block performs four operations sequentially:

1. **Self-Attention** — Within-modality attention for each stream
2. **Text Cross-Attention** — Textual prompt conditioning for both streams
3. **Audio-Visual Cross-Attention** — Bidirectional inter-modal exchange (1D temporal RoPE)
4. **Feed-Forward Network (FFN)** — Feature refinement

```text
┌─────────── TRANSFORMER BLOCK ───────────┐
│                                         │
│  VIDEO: Input → RMSNorm → AdaLN →       │
│              Self-Attn →                 │
│              RMSNorm → Text Cross-Attn → │
│              RMSNorm → AdaLN →           │
│              A↔V Cross-Attn (1D RoPE) →  │
│              RMSNorm → AdaLN → FFN       │
│                                         │
│  AUDIO: Similar (5B params, 1D RoPE)    │
│                                         │
│  RoPE: Video=3D (x,y,t), Audio=1D (t)   │
└─────────────────────────────────────────┘
```

## Data Flow Pipeline

```
┌──────────────────────────────────────────────────────┐
│ INPUT PREPARATION                                    │
│                                                      │
│  Video Pixels → Video VAE Encoder → Video Latents    │
│  Audio Waveform → Audio VAE Encoder → Audio Latents  │
│  Text Prompt → Gemma 3 Encoder → Text Embeddings     │
└──────────────────────────────────────────────────────┘
                    ↓
┌──────────────────────────────────────────────────────┐
│ LTX-2 ASYMMETRIC DUAL-STREAM TRANSFORMER (48 Blocks) │
│                                                      │
│  Video Stream (14B) ↔ Audio Stream (5B)             │
│  · Shared AdaLN tokens across modalities             │
│  · Bidirectional cross-modal attention               │
│  · Separate RoPE: 3D spatial for video, 1D temporal │
│    for audio, 1D temporal for cross-attn              │
└──────────────────────────────────────────────────────┘
                    ↓
┌──────────────────────────────────────────────────────┐
│ OUTPUT DECODING                                      │
│                                                      │
│  Video Latents → Video VAE Decoder → Video Pixels    │
│  Audio Latents → Audio VAE Decoder → Mel Spectrogram │
│  Mel Spectrogram → Vocoder → Audio Waveform (24kHz)  │
└──────────────────────────────────────────────────────┘
```

## Positional Encodings

### RoPE Schemes (Critical Prompting Implication)

| Stream | RoPE Type | What This Means for Generation |
|--------|-----------|--------------------------------|
| Video Spatial | **3D RoPE** (x, y, t) | Each token knows its exact pixel grid position → spatial coherence across frames |
| Video Temporal | **3D RoPE** (included above) | Temporal position is encoded alongside spatial — crucial for motion understanding |
| Audio | **1D RoPE** (temporal only) | Audio tokens only know their temporal index — 14B params encode audio dynamics |
| Cross-Modal | **1D temporal** | Sub-frame alignment enables lip-sync, foley, sound-source localization |

> 💡 **Key Insight**: The 3D RoPE for video means the model has explicit spatial awareness. This is why LTX-2 excels at maintaining character/object consistency across frames when prompted with specific visual details.

## Text Encoder: Gemma 3

- Uses **Gemma 3-based multilingual encoder**
- Produces **separate embeddings for video and audio conditioning**
- Supports multi-layer feature extraction and thinking tokens
- Enables true joint audio-video conditioning from a single text prompt

## VAE Codecs

### Video VAE
- Encodes/decodes video pixels to/from latent space
- Provides temporal AND spatial compression
- Enables efficient transformer processing on reduced-resolution latents

### Audio VAE
- Encodes/decodes audio spectrograms to/from latent space
- Neural vocoder converts mel spectrograms to 24kHz audio waveforms

## Spatial Upscaler
- Upsamples latent representations for higher-resolution generation
- Required for current two-stage pipeline implementations
- Multiple variants available: x1.5, x2 (including HQ res_2s)

## Temporal Upscaler
- Supports temporal upscaling for smoother video
- For future pipeline implementations
- Version: x2-1.0

## Quantization Options

| Method | Checkpoint Type | Use Case | Performance Impact |
|--------|----------------|----------|-------------------|
| FP8 Cast (default) | bf16 checkpoints | General use, all GPUs | Reduced VRAM, minor quality loss |
| FP8 Scaled MM | fp8 checkpoints | Hopper GPUs w/ TensorRT-LLM | Best performance on A100/H100 |

FP8 Cast downcasts bf16 weights on-the-fly.
> ⚠️ **Warning**: For consumer GPU workflows, stick with FP8 Cast + bf16 checkpoints. FP8 Scaled MM requires Hopper architecture (A100/H100/B200).

> 💡 **Implication for prompt consistency**: Using quantized inference doesn't affect prompting strategy — only model quality/VRAM tradeoff. The core architecture remains identical.

## Attention Optimizations

| GPU Type | Optimization | Command |
|----------|-------------|---------|
| Blackwell (B200) | FlashAttention 4 | `uv pip install 'flash-attn-4==4.0.0b9'` |
| Hopper/Consumer CUDA | xFormers | `uv sync --extra xformers` |

## Memory-Efficient Block Streaming

For low-memory GPU deployments:
- **RAM streaming** (default): All blocks pre-loaded into pinned CPU buffers → faster inference, higher CPU memory
- **Disk streaming**: Blocks read from `.safetensors` file on-demand → slowest but lowest CPU/GPU memory footprint

## LoRA Ecosystem

### Control LoRAs

| LoRA | Purpose | Reference |
|------|---------|-----------|
| [[IC-LoRA: Union Control]] | Image+video conditional control | Lightricks/LTX-2.3-22b-IC-LoRA-Union-Control |
| [[IC-LoRA: Motion Track Control]] | Character/object tracking across frames | Lightricks/LTX-2.3-22b-IC-LoRA-Motion-Track-Control |
| [[IC-LoRA: Pose Control]] | Pose-driven video generation | LTX-2-19b-IC-LoRA-Pose-Control |
| [[LoRA: Detailer]] | High-detail enhancement | LTX-2-19b-IC-LoRA-Detailer |

### Camera Motion LoRAs

| LoRA | Effect | Reference |
|------|--------|-----------|
| Dolly In / Out | Forward/backward camera movement | LTX-2-19b-LoRA-Camera-Control-Dolly-In/Out |
| Dolly Left / Right | Horizontal camera tracking | LTX-2-19b-LoRA-Camera-Control-Dolly-Left/Right |
| Jib Up / Down | Vertical camera jib movement | LTX-2-19b-LoRA-Camera-Control-Jib-Up/Down |
| Static | Locked camera position | LTX-2-19b-LoRA-Camera-Control-Static |

### Specialty LoRAs

| LoRA | Purpose | Reference |
|------|---------|-----------|
| IC-LoRA: HDR | Video-to-video with HDR output (EXR export) | LTX-2.3-22b-IC-LoRA-HDR |
| IC-LoRA: LipDub | Lip dubbing, voice matching, face rephrasing | LTX-2.3-22b-IC-LoRA-LipDub |
| Distilled LoRA (384) | Required for two-stage pipeline generation | ltx-2.3-22b-distilled-lora-384-1.1 |

## Model Checkpoints

| Checkpoint | Parameters | Description | Reference |
|------------|-----------|-------------|-----------|
| ltx-2.3-22b-dev | 22B | Development checkpoint | HF: LTX-2.3 repo |
| ltx-2.3-distilled-1.1 | 22B | Fast inference (8 sigmas, ~8 steps S1) | HF: LTX-2.3 repo |

## Pipeline Options Overview

| Pipeline | Use Case | Speed | Quality |
|----------|----------|-------|---------|
| [[TI2VidTwoStagesHQPipeline]] | Production-quality with 2x upscale + HQ sampler | Slow | ⭐⭐⭐⭐⭐ |
| [[TI2VidTwoStagesPipeline]] | Standard production workflow | Medium | ⭐⭐⭐⭐ |
| [[TI2VidOneStagePipeline]] | Quick prototyping, fast iteration | Fast | ⭐⭐⭐ |
| [[DistilledPipeline]] | Fastest inference (8 steps) | Very Fast | ⭐⭐⭐ |

## Cross-Disciplinary Connections

- Links to: [[AI-Video/Runway Gen 4]] — Compare: LTX-2 uses *joint audio-video* generation vs Runway's TTS→lip-sync sequential pipeline
- Links to: [[AI-Video/Kling API]] — Both offer camera-controlled generation via LoRAs
- Links to: DaVinci-Resolve/Temporal-Upscaling — VAE compression parallels temporal upsampling concepts
- Links to: AI Image-Midjourney/Civitai-LoRA-Workflow — Similar LoRA ecosystem but LTX extends to temporal domain


[[Synthesis/AIVideoModelSurvey]] → LTX is unique in jointly generating audio+video
[[AI-Agents/n8n-automation]] → Prompt enhancement pipeline can be fully automated via n8n
