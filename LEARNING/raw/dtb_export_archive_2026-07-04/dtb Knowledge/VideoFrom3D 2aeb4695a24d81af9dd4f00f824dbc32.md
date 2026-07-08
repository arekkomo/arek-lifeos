# VideoFrom3D

Tags: AI 3D Model, AI Image, AI Video, Content Creation
Description: 3D scene video generation from geometry and image via complementary diffusion models.
URL: https://github.com/KIMGEONUNG/VideoFrom3D
Date Added: November 16, 2025 5:35 PM
Type: Github
Archive: No
Spark: No

## Summary

VideoFrom3D generates coherent videos from 3D geometry, camera trajectories, and reference images using complementary image and video diffusion models. It creates high-quality, consistent frames with style and geometry fidelity.

## Features

- Two-stage pipeline (SAG + GGI)
- Image diffusion for anchor-view generation
- Video diffusion for geometry-guided interpolation
- Works with coarse geometry
- No paired 3D-image dataset required

## Use Cases

- Filmmaking and content creation from rough 3D layouts
- Previsualization and look development
- Stylized scene generation with consistent camera motion

## Installation

Install dependencies via requirements.txt; run SAG preprocessing then GGI for interpolation; compatible with Python 3.10 + PyTorch.

## Other Info

Research code from SIGGRAPH Asia 2025; potentially suitable for integration into VFX/ComfyUI pipelines for experimental scene generation.