# Tencent-Hunyuan/HY-WU

Tags: AI Image, Github
Description: Functional neural memory framework generating instance-conditioned LoRA adapters on-the-fly for image editing — no test-time finetuning, scalable to 80B-parameter backbones.
URL: https://github.com/Tencent-Hunyuan/HY-WU
Date Added: May 9, 2026 4:38 PM
Type: Github
Archive: No
Spark: No

## About

HY-WU synthesizes instance-specific LoRA weight updates on-the-fly from hybrid image+instruction representations. A lightweight 8B neural memory model generates conditioned adapters that inject into a frozen 80B backbone (HunyuanImage-3.0-Instruct) during the forward pass — no test-time optimization needed.

**GitHub:** [https://github.com/Tencent-Hunyuan/HY-WU](https://github.com/Tencent-Hunyuan/HY-WU)

**Paper:** [https://arxiv.org/abs/2603.07236](https://arxiv.org/abs/2603.07236)

**Demo:** [https://tencent-hy-wu.github.io/](https://tencent-hy-wu.github.io/)

**Models:** [https://huggingface.co/tencent/HY-WU](https://huggingface.co/tencent/HY-WU)

## Capabilities

- On-the-fly LoRA generation without test-time finetuning
- Instance-level personalization from image+text input
- Cross-domain clothing fusion and outfit transfer
- High-fidelity face identity transfer
- Virtual try-on / seamless outfit migration
- High-quality texture synthesis
- Scalable to 80B parameter backbones (13B active via MoE)
- Gradio web UI included

## VFX / Filmmaking Use Cases

- Virtual wardrobe / costume design: transfer any clothing from reference to character without finetuning
- Face/identity preservation across generated or composited frames
- Character outfit migration for animation using image references alone
- Texture and material transfer from reference imagery onto characters or props
- Virtual try-on: test costume combos on talent photos before physical fittings

## Memory Requirement

| Base model | HY-WU param | Recommended VRAM |
| --- | --- | --- |
| 80B (13B active MoE) | 8B | >= 8 x 40GB or 4 x 80GB |

## Requirements

- Multi-GPU required
- Base: tencent/HunyuanImage-3.0-Instruct (80B, 13B active)
- HY-WU: tencent/HY-WU (8B)

## How to Run

```
git clone https://github.com/Tencent-Hunyuan/HY-WU.git && cd HY-WU
pip install -r requirements.txt
python infer.py
python gradio/app.py
```

## Notes

Fully feedforward — no test-time optimization. Competitive with Nano Banana 2/Pro (closed-source). Distilled checkpoint planned but not released as of 2026-03. MoE impl can use eager mode for compatibility.