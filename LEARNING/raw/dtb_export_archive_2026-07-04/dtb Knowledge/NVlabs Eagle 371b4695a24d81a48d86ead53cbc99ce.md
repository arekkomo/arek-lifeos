# NVlabs/Eagle

Tags: AI Automation, AI Tracking, Github, LLM, VFX
Description: NVIDIA VLM for fast visual grounding and object detection using Parallel Box Decoding — 10× faster than Qwen3-VL at SOTA accuracy.
URL: https://github.com/NVlabs/Eagle/tree/main/Embodied
Date Added: May 31, 2026 9:21 AM
Type: Github
Archive: No
Spark: No

## About

LocateAnything is a vision-language model (3B) from NVIDIA for visual grounding, object detection, and point-based localization. Uses Parallel Box Decoding (PBD) — 12.7 BPS on H100 (~10× faster than Qwen3-VL) at SOTA accuracy.

- **GitHub:** [https://github.com/NVlabs/Eagle/tree/main/Embodied](https://github.com/NVlabs/Eagle/tree/main/Embodied)
- **Paper:** [https://research.nvidia.com/labs/lpr/locate-anything/LocateAnything.pdf](https://research.nvidia.com/labs/lpr/locate-anything/LocateAnything.pdf)
- **Demo:** [https://huggingface.co/spaces/nvidia/LocateAnything](https://huggingface.co/spaces/nvidia/LocateAnything)
- **Model:** [https://huggingface.co/nvidia/LocateAnything-3B](https://huggingface.co/nvidia/LocateAnything-3B)

## Capabilities

- Object detection via natural language query
- Referring expression grounding (complex phrases → bounding boxes)
- GUI element grounding for automation
- Text localization (OCR)
- Layout grounding
- Point-based localization
- Hybrid Fast/Slow inference modes

## VFX / Filmmaking Use Cases

- AI-assisted roto — describe object in natural language, get bounding boxes for masking
- Shot analysis — detect/track props, characters, elements across frames
- RealityRowHub — ground real-world objects for AR overlays or environment mapping
- Scene composition analysis for AI-assisted directing
- GUI automation for DaVinci Resolve workflows via n8n or Claude Code

## Requirements

- Model: nvidia/LocateAnything-3B
- CUDA GPU (A100, H100; Hopper/Blackwell for long-context)
- transformers==4.57.1, deepspeed==0.15.4, accelerate==1.5.2

## How to run it

```bash
git clone https://github.com/NVlabs/Eagle.git eagle
cd eagle/Embodied
pip install -e .
```

```python
from locateanything_worker import LocateAnythingWorker
worker = LocateAnythingWorker("nvidia/LocateAnything-3B")
print(worker.detect(img, ["person", "car"])["answer"])
```

## Notes

- Arek's note: potentially useful for AI filmmaking pipeline and RealityRowHub project
- Output format: coordinates in [0, 1000], divide by 1000 for relative coords
- SOTA on all 7 pointing benchmarks, DocLayNet, M6Doc, ScreenSpot-Pro