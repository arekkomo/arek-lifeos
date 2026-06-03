---
title: Kiwi-Edit
category: entity
summary: Versatile AI video editing framework via instruction and reference image guidance — built on Wan2.2 5B video DiT.
tags: [ai-video, video-editing, vfx, diffusion, github]
sources: 1
updated: 2026-05-09
---

# Kiwi-Edit

**By:** ShowLab  
**Released:** March 2026  
**GitHub:** https://github.com/showlab/Kiwi-Edit  
**Paper:** https://arxiv.org/abs/2603.02175  
**Demo:** https://huggingface.co/spaces/linyq/KiwiEdit  
**Models:** https://huggingface.co/collections/linyq/kiwi-edit

---

## What It Is

Kiwi-Edit is a video editing framework that combines an MLLM (multimodal LLM) encoder with the Wan2.2-TI2V-5B video diffusion transformer (5B params). It accepts either text instructions or a reference image (or both) to guide edits — making it one of the more flexible open-source video editors available.

---

## Capabilities

- **Style Transfer** — Apply global visual styles via text prompt
- **Object Replace** — Swap objects in a scene with natural language
- **Object Add** — Insert new elements into existing footage
- **Object Remove** — Remove unwanted subjects or objects
- **Background Replace** — Swap backgrounds via text or reference image
- **Subject Reference** — Use a reference image to guide subject edits
- **Background Reference** — Use a reference image to define target background

---

## VFX / Filmmaking Use Cases

- Clean plate assists and object removal in post
- Background replacement without greenscreen
- Style pass for look dev and grade previews
- Prop or wardrobe replacement in post
- Reference-guided set extension
- Non-destructive exploratory edits on footage

---

## Models

| Model | Type |
|---|---|
| `kiwi-edit-5b-instruct-only-diffusers` | Instruction-only |
| `kiwi-edit-5b-reference-only-diffusers` | Reference image-only |
| `kiwi-edit-5b-instruct-reference-diffusers` | Full — instruction + reference |

All available on HuggingFace: https://huggingface.co/collections/linyq/kiwi-edit

---

## Requirements

- Python 3.10 + CUDA 12.8
- PyTorch 2.7
- Base model: Wan2.2-TI2V-5B
- Training (optional): DeepSpeed, FlashAttention

---

## Quick Start (Diffusers)

```bash
conda create -n diffusers python=3.10 -y && conda activate diffusers
pip install torch==2.7.0 torchvision==0.22.0 --index-url https://download.pytorch.org/whl/cu128
pip install diffusers decord einops accelerate transformers==4.57.0 opencv-python av

python diffusers_demo.py \
    --video_path ./input.mp4 \
    --prompt "Remove the monkey." \
    --save_path output.mp4 \
    --model_path linyq/kiwi-edit-5b-instruct-only-diffusers
```

---

## Notes

- Diffusers-compatible — works with standard HuggingFace pipeline
- Reference image guidance is a key differentiator vs prompt-only video editors
- Built on top of Wan2.2 — same base model family as other leading open video DiTs
