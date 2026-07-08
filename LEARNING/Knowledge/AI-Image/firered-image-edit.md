---
title: FireRed-Image-Edit
category: entity
summary: State-of-the-art open-source image editing model with strong identity consistency, multi-element fusion, portrait makeup, text style reference, and ComfyUI support.
tags: [ai-image, image-editing, comfyui, lora, diffusion-models, github]
sources: 1
updated: 2026-05-09
---

# FireRed-Image-Edit

**By:** FireRedTeam
**Released:** 2026-02-14 (v1.0), 2026-03-03 (v1.1)
**GitHub:** https://github.com/FireRedTeam/FireRed-Image-Edit
**Paper:** https://arxiv.org/abs/2602.13344
**Demo:** https://huggingface.co/spaces/FireRedTeam/FireRed-Image-Edit-1.1
**Models:** https://huggingface.co/FireRedTeam/FireRed-Image-Edit-1.1

---

## What It Is

FireRed-Image-Edit is a general-purpose image editing model (v1.0) and its enhanced version (v1.1) that delivers high-fidelity, instruction-following editing across diverse scenarios. It achieves open-source state-of-the-art on identity preservation, multi-element fusion (10+ images), portrait makeup, and text style reference. Fully distilled and quantized variant runs in 4.5s with 30GB VRAM.

---

## Capabilities

- SOTA identity consistency: subjects remain recognizable across complex edits
- Multi-element fusion: combine 10+ input images via Agent-powered auto-crop/stitch
- Portrait makeup: dozens of styles from beauty retouching to creative looks
- Text/typography style reference: high-fidelity styled text comparable to closed-source tools
- Photo restoration: old photo repair and enhancement
- ComfyUI node support + GGUF lightweight format
- Full LoRA training code released (HSDP/FSDP, Disaggregated Training)
- Agent module: automatic ROI detection, image stitching, prompt rewriting via Gemini/MiniMax
- Optimized inference: distillation + quantization + static compilation → 4.5s/sample at 30GB VRAM

---

## VFX / Filmmaking Use Cases

- **Character consistency across shots**: Maintain actor identity and costume across generated or composited frames — essential for AI-assisted scene continuity
- **Wardrobe/costume transfer**: Fuse clothing from reference images onto characters (virtual try-on pipeline)
- **Portrait makeup for characters**: Apply specific makeup looks from reference images to talent — useful for look development without physical application
- **Old photo / aged-film restoration**: Restore archival reference footage or production stills to high quality
- **Typography and title design**: Transfer text styles from reference images for titles and lower-thirds
- **Multi-image composite direction**: Combine characters, props, and environments from separate references into a single image — concept art composition without 3D
- **ComfyUI workflow integration**: Drop into existing ComfyUI pipelines for instruction-based editing nodes

---

## Requirements

- Python, PyTorch (standard diffusion setup)
- 30GB VRAM minimum for optimized inference (4.5s/sample)
- Full precision requires more; LoRA zoo available for specific styles
- Optional: Gemini API key or MiniMax API key for Agent/Recaption features

---

## Quick Start

```bash
pip install -r requirements.txt
python inference.py \
    --input_image ./examples/edit_example.png \
    --prompt "add a red hat to the person" \
    --output_image output_edit.png \
    --seed 43

# Optimized inference (30GB VRAM)
python inference.py --optimized True
```

---

## Notes

v1.1 specifically improves portrait consistency, multi-element fusion, stylized text reference, and makeup. Training pipeline: full Pretrain → SFT → RL, making editing capabilities backbone-agnostic and transferable. REDEdit-Bench is their new evaluation benchmark. LoRA Zoo on HuggingFace includes makeup and covercraft (text style) specialized adapters.
