# 3D-RE-GEN

Tags: AI, AI 3DModel, AI Automation, Filmmaking
Description: 3D-RE-GEN reconstructs complete, editable 3D indoor scenes from a single image using a compositional generative framework.
URL: https://github.com/cgtuebingen/3D-RE-GEN
Date Added: January 3, 2026 12:38 PM
Type: Github
Archive: No
Spark: No

## Summary

3D-RE-GEN is a framework for reconstructing full 3D indoor scenes from a single image. It decomposes the input into individual objects and background geometry, generating textured, editable meshes suitable for VFX and AR/VR pipelines. The model ensures spatial consistency and physical plausibility in reconstructed scenes.

## Features

- End-to-end 3D scene reconstruction from a single image
- Instance-level segmentation and inpainting for occluded regions
- 2D-to-3D object and background geometry generation
- Constrained optimization to ensure ground-plane alignment
- Outputs textured, editable meshes

## Use Cases

- Rapid 3D environment reconstruction for film, games, and AR/VR
- Research on compositional generative 3D models
- Automated asset generation for virtual production

## Installation

Clone the repository and install required dependencies following README instructions. Current release includes inference code for single-image reconstruction.

## Other Info

Based on the paper '3D-RE-GEN: 3D Reconstruction of Indoor Scenes with a Generative Framework' (Dec 2025). Developed by Tobias Sautter, Jan-Niklas Dihlmann, and Hendrik P.A. Lensch at CG Tübingen.