# MVInverse

Tags: AI, AI Automation, AI Video, Filmmaking
Description: MVInverse enables feed-forward multi-view consistent inverse rendering without per-scene optimization.
URL: https://github.com/Maddog241/mvinverse
Date Added: January 3, 2026 12:35 PM
Type: Github
Archive: No
Spark: No

## Summary

MVInverse is a feed-forward multi-view inverse rendering framework that predicts consistent scene geometry, materials, and intrinsic properties from multiple images in a single pass, avoiding slow per-scene optimization.

## Features

- Feed-forward multi-view inverse rendering
- Alternating attention for cross-view consistency
- Predicts albedo, normals, roughness, metallic, and shading maps
- Works in seconds without expensive optimization
- Includes inference scripts for multi-image input

## Use Cases

- Fast geometry and material estimation from multi-view image sets
- Consistent intrinsic image generation for rendering pipelines
- Practical inverse rendering for AR/VR, relighting, and scene reconstruction

## Installation

Clone the repo, install required Python dependencies (Torch, OpenCV, HF Hub), and run the provided inference scripts on input image sequences.

## Other Info

Based on the paper 'MVInverse: Feed-forward Multi-view Inverse Rendering in Seconds' (Dec 2025); leverages alternating attention for coherent multi-view predictions.