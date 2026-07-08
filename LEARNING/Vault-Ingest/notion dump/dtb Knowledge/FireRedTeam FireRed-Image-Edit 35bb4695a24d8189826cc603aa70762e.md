# FireRedTeam/FireRed-Image-Edit

Tags: AI Image, ComfyUI, Github
Description: State-of-the-art open-source image editing model with SOTA identity consistency, multi-element fusion (10+ images), portrait makeup, text style reference, and ComfyUI support.
URL: https://github.com/FireRedTeam/FireRed-Image-Edit
Date Added: May 9, 2026 4:38 PM
Type: Github
Archive: No
Spark: No

## About

FireRed-Image-Edit (v1.0 + v1.1) is a general-purpose image editing model achieving open-source SOTA on identity preservation, multi-element fusion, portrait makeup, and text style reference. Optimized: distillation + quantization + static compilation = 4.5s/sample at 30GB VRAM.

**GitHub:** [https://github.com/FireRedTeam/FireRed-Image-Edit](https://github.com/FireRedTeam/FireRed-Image-Edit)

**Paper:** [https://arxiv.org/abs/2602.13344](https://arxiv.org/abs/2602.13344)

**Demo:** [https://huggingface.co/spaces/FireRedTeam/FireRed-Image-Edit-1.1](https://huggingface.co/spaces/FireRedTeam/FireRed-Image-Edit-1.1)

**Models:** [https://huggingface.co/FireRedTeam/FireRed-Image-Edit-1.1](https://huggingface.co/FireRedTeam/FireRed-Image-Edit-1.1)

## Capabilities

- SOTA open-source identity consistency across complex edits
- Multi-element fusion: 10+ input images via Agent auto-crop/stitch
- Portrait makeup: dozens of styles (beauty to Halloween)
- Text/typography style transfer comparable to closed-source tools
- Photo restoration: old photo repair and enhancement
- ComfyUI node support + GGUF lightweight format
- Full LoRA training code (HSDP/FSDP, Disaggregated Training)
- Agent module: ROI detection, image stitching, Gemini/MiniMax recaption
- 4.5s/sample, 30GB VRAM optimized inference

## VFX / Filmmaking Use Cases

- Character consistency across generated or composited frames
- Wardrobe/costume transfer: fuse clothing from references onto characters
- Portrait makeup for look development without physical application
- Archival reference footage and production still restoration
- Typography / title design via text style transfer
- Multi-image composite direction for concept art (no 3D required)
- ComfyUI instruction-based editing node integration

## Requirements

- 30GB VRAM minimum for optimized inference (4.5s/sample)
- Optional: Gemini API key or MiniMax for Agent recaption feature
- LoRA Zoo: makeup + covercraft (text style) adapters on HuggingFace

## How to Run

```
pip install -r requirements.txt
python inference.py --input_image ./examples/edit_example.png --prompt "add a red hat" --output_image output.png
python inference.py --optimized True
```

## Notes

v1.1 improves portrait consistency, multi-element fusion, text reference, and makeup. Training: Pretrain → SFT → RL, backbone-agnostic and transferable. REDEdit-Bench is their evaluation benchmark.