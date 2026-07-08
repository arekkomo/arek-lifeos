# yfyang007/ControlLight

Tags: AI Image, Diffusion Models, Github
Description: Controllable, consistent low-light image enhancement via FLUX.2 LoRA with slider-based brightness control and Light100K dataset.
URL: https://github.com/yfyang007/ControlLight
Date Added: May 31, 2026 11:06 AM
Type: Github
Archive: No
Spark: No

## About

ControlLight is a low-light image enhancement model with linear, continuous brightness control. Built as a LoRA on FLUX.2-klein-base-9B, trained on Light100K dataset.

**GitHub:** [https://github.com/yfyang007/ControlLight](https://github.com/yfyang007/ControlLight)

**Paper:** [https://arxiv.org/abs/2605.25569](https://arxiv.org/abs/2605.25569)

**Models:** [https://huggingface.co/ControlLight/ControlLight](https://huggingface.co/ControlLight/ControlLight)

**Project:** [https://yfyang007.github.io/ControlLight/](https://yfyang007.github.io/ControlLight/)

## Capabilities

- Linear slider-based brightness control (0–1 range)
- Consistent spatial detail and colour fidelity across diverse scenes
- FLUX.2-based LoRA — combinable with other adapters
- Training + inference scripts released; Light100K dataset public

## VFX / Filmmaking Use Cases

- Correct underexposed footage frames without losing spatial detail
- Standardise lighting across a batch of reference images for AI training data
- Pre-process low-light stills before AI video generation (Runway, Kling)

## Requirements

- Python 3.12, ~21 GB VRAM, FLUX.2-klein-base-9B base model

## How to Run

```bash
conda create -n controlight python=3.12 -y
conda activate controlight
python -m pip install -e diffusers
python -m pip install -r requirements.txt && python -m pip install -e .
bash scripts/predict.sh
```