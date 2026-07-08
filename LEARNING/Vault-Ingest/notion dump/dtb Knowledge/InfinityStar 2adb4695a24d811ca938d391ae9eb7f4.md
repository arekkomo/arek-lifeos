# InfinityStar

Tags: AI Automation, AI Video, Content Creation, VFX
Description: Unified spacetime autoregressive model for image and video generation across multiple modalities (T2I, T2V, I2V, interactive video).
URL: https://github.com/FoundationVision/InfinityStar
Rating: ⭐⭐⭐⭐
Date Added: November 15, 2025 6:05 PM
Type: Github
Archive: No
Spark: No

## Summary

InfinityStar is a unified autoregressive model developed by FoundationVision/ByteDance for text-to-image, text-to-video, image-to-video, and interactive long video generation. It models spatial and temporal information jointly using a discrete autoregressive architecture for efficient, high-quality generation.

## Features

- Joint spatial-temporal modeling in one framework
- Supports T2I, T2V, I2V, and interactive long video synthesis
- 720p video generation with ~10× faster inference than diffusion-based models
- Autoregressive design ensures temporal consistency and coherence

## Use Cases

- Generate or extend footage from text or image prompts
- Interactive video generation for VFX or filmmaking
- Rapid content creation and motion prototyping
- Research into autoregressive video generation

## Installation

Requires PyTorch ≥ 2.5.1. Clone repo, install dependencies, run provided inference tools (e.g., tools/infer_video_720p.py or tools/infer_interact_480p.py).

## Other Info

Developed by FoundationVision (ByteDance). Licensed under MIT. Presented as oral paper at NeurIPS 2025. Unified autoregressive approach for scalable high-resolution image/video generation.