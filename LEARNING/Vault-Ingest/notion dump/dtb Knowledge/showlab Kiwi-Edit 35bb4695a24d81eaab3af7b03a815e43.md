# showlab/Kiwi-Edit

Tags: AI Video, Github, Video Editing
Description: Versatile video editing framework via instruction and reference image guidance — style transfer, object add/remove/replace, background swap. Built on Wan2.2-TI2V-5B (5B param video DiT).
URL: https://github.com/showlab/Kiwi-Edit
Date Added: May 9, 2026 3:59 PM
Type: Github
Archive: No
Spark: No

## About

Kiwi-Edit is a versatile video editing framework from [ShowLab](https://showlab.github.io/) built on an MLLM encoder and the Wan2.2-TI2V-5B video diffusion transformer. It supports both text instruction-based editing and reference image-guided editing — making it highly useful for VFX and post-production workflows.

**Paper:** [arxiv.org/abs/2603.02175](http://arxiv.org/abs/2603.02175)  

**HuggingFace Models:** [linyq/kiwi-edit](https://huggingface.co/collections/linyq/kiwi-edit)  

**Live Demo:** [huggingface.co/spaces/linyq/KiwiEdit](http://huggingface.co/spaces/linyq/KiwiEdit)  

**Project Page:** [showlab.github.io/Kiwi-Edit](http://showlab.github.io/Kiwi-Edit)

---

## Capabilities

- **Style Transfer** — Apply global visual styles to a video via text prompt
- **Object Replace** — Swap out objects in a scene with natural language instruction
- **Object Add** — Insert new objects into existing footage
- **Object Remove** — Remove unwanted elements from video
- **Background Replace** — Swap backgrounds via text or reference image
- **Subject Reference** — Use a reference image to guide subject edits
- **Background Reference** — Use a reference image to define the target background

---

## VFX / Filmmaking Use Cases

- Clean plate assists and object removal
- Background replacement without greenscreen
- Style pass for look dev and grade previews
- Prop replacement in post
- Reference-guided set extension

---

## Models

| Model | Description |
| --- | --- |
| `kiwi-edit-5b-instruct-only-diffusers` | Instruction-only fine-tune |
| `kiwi-edit-5b-reference-only-diffusers` | Reference image-only fine-tune |
| `kiwi-edit-5b-instruct-reference-diffusers` | Full model — instruction + reference |

---

## Requirements

- Python 3.10, CUDA 12.8
- PyTorch 2.7
- Base model: Wan2.2-TI2V-5B (~11GB)
- For training: DeepSpeed, FlashAttention

---

## How to run it

```bash
# Install environment
conda create -n diffusers python=3.10 -y
conda activate diffusers
pip install torch==2.7.0 torchvision==0.22.0 --index-url https://download.pytorch.org/whl/cu128
pip install diffusers decord einops accelerate transformers==4.57.0 opencv-python av

# Run inference
python diffusers_demo.py \
    --video_path ./input.mp4 \
    --prompt "Remove the monkey." \
    --save_path output.mp4 \
    --model_path linyq/kiwi-edit-5b-instruct-only-diffusers
```

---

## Notes

- Released March 2026 by ShowLab
- Diffusers-compatible — works with standard HuggingFace pipeline
- Reference image support is a key differentiator vs prompt-only editors