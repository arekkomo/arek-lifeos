# ProEdit

Tags: AI, AI Image, AI Video, Content Creation
Description: Training-free inversion-based visual editing framework for image and video generation.
URL: https://github.com/iSEE-Laboratory/ProEdit
Date Added: January 4, 2026 10:17 AM
Type: Github
Archive: No
Spark: No

## Summary

ProEdit is a training-free inversion-based editing framework for diffusion models that enables high-fidelity, prompt-driven edits for both images and videos. It minimizes over-reliance on the original source image while preserving structure and background consistency.

## Features

- Flow-inversion mechanism for improved prompt editing balance
- KV-mix for controlled feature blending in edited regions
- Latents-Shift to reduce source bias during editing
- Works for both image and video editing
- Plug-and-play with existing inversion frameworks

## Use Cases

- Precise text-driven image and video editing
- Research in inversion-based generative editing
- Fine-grained attribute modifications without retraining

## Installation

Clone the repository, install Python dependencies via pip, and run the provided scripts for inversion and editing tasks following the README.

## Other Info

Implements 'ProEdit: Inversion-based Editing From Prompts Done Right' by iSEE-Laboratory. Licensed under MIT and integrates with RF-Solver, FireFlow, and UniEdit pipelines.