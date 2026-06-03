---
title: HY-WU
category: entity
summary: Functional neural memory framework that generates instance-conditioned LoRA adapters on-the-fly for image editing — no test-time finetuning required.
tags: [ai-image, image-editing, lora, neural-memory, hunyuan, virtual-try-on, github]
sources: 1
updated: 2026-05-09
---

# HY-WU

**By:** Tencent Hunyuan Team (Mengxuan Wu, Xuanlei Zhao, Ziqiao Wang, Ruicheng Feng, et al.)
**Released:** 2026-03-06
**GitHub:** https://github.com/Tencent-Hunyuan/HY-WU
**Paper:** https://arxiv.org/abs/2603.07236
**Demo:** https://tencent-hy-wu.github.io/
**Models:** https://huggingface.co/tencent/HY-WU

---

## What It Is

HY-WU is a scalable framework that synthesizes instance-specific LoRA weight updates on-the-fly from hybrid image+instruction representations. Instead of fine-tuning at test time, a "neural memory" model generates conditioned adapter weights that inject into a frozen backbone (HunyuanImage-3.0-Instruct) during the forward pass. Strong results on clothing transfer, face identity, virtual try-on, and texture synthesis. Practical at 80B-parameter scale (13B active via MoE).

---

## Capabilities

- On-the-fly LoRA generation without test-time finetuning
- Instance-level personalization from hybrid image+text input
- Cross-domain clothing fusion and outfit transfer
- High-fidelity face identity transfer
- Virtual try-on / seamless outfit migration
- High-quality texture synthesis
- Creative cosplay and character outfit migration
- Scalable to 80B-parameter backbones (13B active, MoE)
- Gradio web UI included

---

## VFX / Filmmaking Use Cases

- **Virtual wardrobe / costume design**: Transfer any clothing from a reference image onto a character without a single fine-tune — ideal for rapid costume exploration in pre-production
- **Face/identity preservation in edits**: Maintain actor likeness across generated or composited frames using the identity transfer capability
- **Character outfit migration for animation**: Move costumes between character designs or rigs using image references alone
- **Texture and material transfer**: Synthesize specific texture styles (fabric, material, pattern) onto characters or props from reference imagery
- **Virtual try-on for production**: Test costume combinations on real talent photos before physical wardrobe fittings
- **Personalized scene elements**: Generate instance-specific variations of props or environment elements without retraining any model

---

## Requirements

- Multi-GPU required: ≥ 8 × 40GB or 4 × 80GB VRAM
- Base model: `tencent/HunyuanImage-3.0-Instruct` (80B, 13B active)
- HY-WU model: 8B parameters (`tencent/HY-WU`)
- Python, PyTorch (via `requirements.txt`)

---

## Quick Start

```bash
git clone https://github.com/Tencent-Hunyuan/HY-WU.git
cd HY-WU
pip install -r requirements.txt
python infer.py

# Or via Gradio UI
pip install gradio>=4.21.0
python gradio/app.py
```

---

## Notes

Architecture: a lightweight "neural memory" model (8B) generates LoRA updates conditioned on image+instruction, which are injected into the frozen 80B backbone (13B active via MoE). No test-time optimization — fully feedforward. Competitive with closed-source Nano Banana 2/Pro. Distilled checkpoint and other base model checkpoints planned but not yet released as of 2026-03. MoE implementation can use `eager` mode for compatibility.
