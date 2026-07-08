# Lumos-Custom

Tags: AI Automation, AI Video, Content Creation, VFX
Description: Unified image and video relighting framework combining physical correctness and generative flexibility.
URL: https://github.com/alibaba-damo-academy/Lumos-Custom
Date Added: November 15, 2025 6:00 PM
Type: Github
Archive: No
Spark: No

## Summary

Lumos-Custom by Alibaba DAMO Academy introduces UniLumos, a unified image and video relighting system integrating generative AI with geometry-based feedback for physically plausible results. It can relight images and videos while maintaining realism and temporal consistency.

## Features

- Unified framework for image and video relighting
- Integrates geometry feedback (depth/normal maps)
- Six-dimensional illumination attribute annotation protocol
- LumosBench benchmark for relighting evaluation
- Up to 20x faster inference than previous baselines

## Use Cases

- Adjust or redesign lighting in filmed content
- Re-light foreground subjects for compositing or VFX
- Improve lighting realism in AI-generated or captured footage
- Useful for filmmaking, VFX, and AI-assisted content creation

## Installation

Clone the repo, set up conda environment (Python 3.10), install requirements including flash-attn, run provided inference scripts (unilumos_infer_ab.py or unilumos_infer_image.py).

## Other Info

Developed by Alibaba DAMO Academy. Apache-2.0 licensed. Published Nov 2025. Benchmarked on LumosBench; optimized for fast, realistic relighting in production workflows.