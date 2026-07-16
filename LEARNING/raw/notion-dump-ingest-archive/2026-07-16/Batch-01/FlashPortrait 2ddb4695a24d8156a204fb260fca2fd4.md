# FlashPortrait

Tags: AI, AI Animation, AI Video, Content Creation
Description: FlashPortrait generates identity-preserving, infinite-length portrait animations using an accelerated video diffusion transformer.
URL: https://github.com/Francis-Rings/FlashPortrait
Date Added: January 3, 2026 12:26 PM
Type: Github
Archive: No
Spark: No

## Summary

FlashPortrait is an open-source implementation of a video diffusion transformer designed to synthesize identity-preserving, infinite-length portrait animations. It achieves 6× speed acceleration through adaptive latent prediction and introduces a facial expression normalization mechanism for consistent identity over time.

## Features

- End-to-end video diffusion transformer for long portrait animations
- Up to 6× faster inference vs previous diffusion approaches
- Identity consistency maintained across infinite frames
- Sliding-window inference with weighted blending
- Supports multiple resolutions including 512×512, 720p, etc.

## Use Cases

- Generate animated portraits from single images
- Research on diffusion-based video generation
- Creative tools for portrait animation and visual storytelling

## Installation

Clone the repo and follow setup instructions for dependencies in Python; includes model weights and inference scripts.

## Other Info

Based on the paper 'FlashPortrait: 6× Faster Infinite Portrait Animation with Adaptive Latent Prediction'; open-source under Apache-2.0.