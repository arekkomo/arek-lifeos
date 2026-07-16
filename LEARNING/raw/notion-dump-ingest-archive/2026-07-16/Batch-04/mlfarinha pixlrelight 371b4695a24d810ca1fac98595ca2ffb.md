# mlfarinha/pixlrelight

Tags: AI Image, Github, VFX
Description: Feed-forward single-image relighting with PBR control via intrinsic conditioning — relight any photo under Blender Cycles PBR lights in under 0.1 seconds.
URL: https://github.com/mlfarinha/pixlrelight
Date Added: May 31, 2026 11:06 AM
Type: Github
Archive: No
Spark: No

## About

PIXLRelight relights a single photograph under any PBR lighting authored in Blender in under 100ms feed-forward — no optimization, no multi-image capture.

**GitHub:** [https://github.com/mlfarinha/pixlrelight](https://github.com/mlfarinha/pixlrelight)

**Paper:** [https://arxiv.org/abs/2605.18735](https://arxiv.org/abs/2605.18735)

**Models:** [https://huggingface.co/mlfarinha/pixlrelight](https://huggingface.co/mlfarinha/pixlrelight)

**Project:** [https://mlfarinha.github.io/pixl-relight/](https://mlfarinha.github.io/pixl-relight/)

## Capabilities

- Sub-100ms single-image relighting, SOTA quality
- PBR-style lighting control via Blender Cycles OR reference photo
- Per-pixel affine modulation preserves fine image detail
- Weights auto-downloaded from HuggingFace

## VFX / Filmmaking Use Cases

- Relight actor reference photos to match target scene lighting
- Composite AI-generated characters into real footage with matched lighting
- Explore Aiah Syn lighting moods: author in Blender, apply to portrait in <0.1s

## How to Run

```bash
git clone git@github.com:mlfarinha/pixlrelight.git
conda create -n pixlrelight python=3.11 -y && conda activate pixlrelight
pip install -r requirements.txt
```