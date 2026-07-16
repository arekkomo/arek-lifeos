# Deja View

Tags: VFX
Description: Efficient 3D Gaussian reconstruction from multiple images using a 117M-parameter looping transformer. NVIDIA Research framework for fast sparse-to-dense reconstruction without iterative optimization.
URL: https://github.com/nv-tlabs/dvlt
Date Added: June 7, 2026 9:26 PM
Type: Github
Archive: No
Spark: No

## About

Efficient 3D Gaussian reconstruction from multiple images using a 117M-parameter looping transformer. NVIDIA Research framework for fast sparse-to-dense reconstruction without iterative optimization.

Project: https://nvlabs.github.io/DVLT/

---

## Capabilities

- 117M-parameter looping transformer for rapid Gaussian splat reconstruction
- Zero-shot sparse-to-dense point cloud generation from images
- No iterative optimization or per-scene training required
- High-quality multi-view geometry extraction without depth estimation

---

## VFX / Filmmaking Use Cases

- Fast 3D reconstruction of actor/reference assets from photos
- Convert 4D scan captures into interactive Gaussian scene representations
- Build rapid 3D props/characters for real-time rendering pipelines
- Generate dense point clouds from limited camera captures in production

---

## How to Run

```bash
git clone git@github.com:nv-tlabs/dvlt.git
cd dvlt
pip install -r requirements.txt
```