# Stream-DiffVSR

Tags: AI, AI Automation, AI Video
Description: Low-latency, streamable diffusion-based video super-resolution framework for real-time enhancement.
URL: https://github.com/jamichss/Stream-DiffVSR
Date Added: January 4, 2026 10:07 AM
Type: Github
Archive: No
Spark: No

## Summary

Stream-DiffVSR implements a diffusion-based framework for real-time, streamable video super-resolution. It enhances video frames using auto-regressive diffusion models that operate causally on past frames, enabling low-latency and temporally consistent enhancement.

## Features

- Auto-regressive temporal guidance for motion-aware super-resolution
- Four-step distilled denoiser for faster inference
- Temporal-aware decoder for improved coherence
- Streamable inference on past frames only
- Pretrained models and demo scripts included

## Use Cases

- Real-time video enhancement in live streaming or conferencing
- Efficient diffusion model benchmarking
- Super-resolution for low-latency video pipelines

## Installation

Clone the repo and install dependencies via `pip install -r requirements.txt`. Run inference with provided scripts and pretrained weights.

## Other Info

Implements 'Stream-DiffVSR: Low-Latency Streamable Video Super-Resolution via Auto-Regressive Diffusion'; designed for efficiency and temporal consistency.