# HunyuanWorld-Mirror

Tags: AI 3D Model, Filmmaking, VFX
Description: Feed-forward universal 3D reconstruction model supporting images + geometry priors to outputs point clouds, normals, depth, novel views.
URL: https://github.com/Tencent-Hunyuan/HunyuanWorld-Mirror
Date Added: November 15, 2025 3:29 PM
Type: Github
Archive: No
Spark: No

## Summary

HunyuanWorld-Mirror is a versatile feed-forward model for comprehensive 3D geometric prediction that integrates diverse geometric priors (camera poses, intrinsics, depth maps) and simultaneously generates various 3D representations (point clouds, multi-view depths, camera parameters, surface normals, 3D Gaussians) in a single forward pass.

## Features

- Multi-modal prior prompting
- Universal geometric prediction (point cloud, normals, depth, camera params, novel view synthesis)
- Pretrained weights and demo/inference code provided

## Use Cases

Useful for filmmakers/VFX artists or content creators wanting to build 3D reconstructions from video or multi-view images, AR/VR scene generation, novel view rendering.

## Installation

Clone repo; conda env with Python 3.10; install PyTorch (tested with CUDA 12.4) then pip install -r requirements.txt; optionally pip install gsplat for 3D Gaussian splatting.

## Other Info

From Tencent Hunyuan org; open-source; supports optional priors; model still under active issues (Windows, multi-image handling) so expect tinkering.