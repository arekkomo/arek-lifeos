# Stable Layers

Tags: VFX
Description: Stability AI framework for converting images into editable transparent layers. Professional-grade layer-based image decomposition for VFX workflows.
URL: https://github.com/stability-ai/stable-layers
Date Added: June 7, 2026 9:26 PM
Type: Github
Archive: No
Spark: No

## About

Stability AI framework for converting images into editable transparent layers. Professional-grade layer-based image decomposition for VFX workflows.

Project: https://stability-ai.github.io/stable-layers.github.io/

---

## Capabilities

- Automatic image decomposition into editable transparent layers
- Semantic segmentation-based layer separation
- Preserve spatial structure and detail during layer extraction
- Output structured layers suitable for compositing workflows

---

## VFX / Filmmaking Use Cases

- Fast layer extraction for VFX compositing pipelines
- Break down AI-generated images into element layers for manipulation
- Separate foreground/background/elements for targeted VFX treatment
- Generate layered reference assets for downstream compositing

---

## How to Run

```bash
git clone git@github.com:stability-ai/stable-layers.git
cd stable-layers
pip install -r requirements.txt
python separate.py --input image.png --output layers/
```