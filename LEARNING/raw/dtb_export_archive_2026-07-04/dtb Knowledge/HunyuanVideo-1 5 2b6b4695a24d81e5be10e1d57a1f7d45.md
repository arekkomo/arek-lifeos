# HunyuanVideo-1.5

Tags: AI Automation, AI Video, Content Creation
Description: Tencent’s HunyuanVideo 1.5 is a lightweight 8.3 B parameter text‑to‑video and image‑to‑video generator optimized for consumer GPUs.
URL: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5
Date Added: November 24, 2025 10:23 PM
Type: Github
Archive: No
Spark: Yes

## Summary

HunyuanVideo 1.5 is an advanced diffusion‑based video generation model from Tencent that enables text‑to‑video and image‑to‑video creation. With around 8.3 billion parameters, it delivers high‑quality, temporally coherent videos and can run efficiently on consumer‑grade GPUs.

## Features

- Diffusion Transformer (DiT) + 3D causal VAE architecture.
- Supports both text‑to‑video and image‑to‑video workflows.
- Integrated Video Super‑Resolution network for upscaling.
- SSTA (Selective & Sliding Tile Attention) for better memory and speed.
- Compatible with ComfyUI workflows and cache inference for 2× faster runs.

## Use Cases

- Generate realistic videos from text prompts or static images.
- Ideal for creative professionals, content producers, and researchers testing new video synthesis approaches.
- Useful for prototyping animations, cinematic sequences, or visual storytelling.

## Installation

Clone repo → install dependencies via requirements.txt → download model weights → run provided inference scripts or ComfyUI integration.

## Other Info

Released by Tencent Hunyuan Foundation Model Team (Nov 2025). Optimized for ~14 GB GPUs with model offloading. Includes cache inference to double generation speed.