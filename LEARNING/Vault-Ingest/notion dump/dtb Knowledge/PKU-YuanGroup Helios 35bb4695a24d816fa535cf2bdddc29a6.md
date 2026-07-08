# PKU-YuanGroup/Helios

Tags: AI Video, Generation, Github
Description: Real-time long video generation — 14B model at 19.5 FPS on a single H100, T2V/I2V/V2V up to 60 seconds without standard acceleration tricks.
URL: https://github.com/PKU-YuanGroup/Helios
Date Added: May 9, 2026 4:38 PM
Type: Github
Archive: No
Spark: No

## About

Helios is a 14B video generation model achieving 19.5 FPS on a single H100 for real-time, minute-scale video generation — without KV-cache, causal masking, or quantization. Generates videos autoregressively in 33-frame chunks with strong temporal coherence.

**GitHub:** [https://github.com/PKU-YuanGroup/Helios](https://github.com/PKU-YuanGroup/Helios)

**Paper:** [https://arxiv.org/abs/2603.04379](https://arxiv.org/abs/2603.04379)

**Demo:** [https://huggingface.co/spaces/BestWishYsh/Helios-14B-RealTime](https://huggingface.co/spaces/BestWishYsh/Helios-14B-RealTime)

**Models:** [https://huggingface.co/collections/BestWishYsh/helios](https://huggingface.co/collections/BestWishYsh/helios)

## Capabilities

- 19.5 FPS end-to-end on single H100 (up to 20.89 FPS)
- Minute-scale generation (up to ~1449 frames / 60s at 24 FPS)
- Text-to-Video, Image-to-Video, Video-to-Video
- Group offloading: ~6GB VRAM minimum
- Context parallelism across multi-GPU (Ulysses + Ring Attention)
- 4K output on consumer PC (community tutorial)
- Diffusers, SGLang, vLLM-Omni, Ascend-NPU compatible

## VFX / Filmmaking Use Cases

- Real-time 60-second previsualization for on-set or pre-production review
- Image-to-video from concept art or photography references
- Video-to-video stylization at real-time speeds
- Long-form continuous shots (full scene without cuts)
- Low-VRAM test generation on consumer GPUs (6GB with offloading)

## Models

| Model | Notes |
| --- | --- |
| Helios-Base | Best quality, v-prediction, standard CFG |
| Helios-Mid | Intermediate checkpoint |
| Helios-Distilled | Best efficiency, x0-prediction, DMDScheduler |

## Requirements

- Python 3.11.2, PyTorch 2.10.0, CUDA 12.6+
- H100 for real-time; consumer GPU viable with group offloading (~6GB)
- num_frames must be multiple of 33

## How to Run

```
git clone --depth=1 https://github.com/PKU-YuanGroup/Helios.git && cd Helios
conda create -n helios python=3.11.2 && conda activate helios
bash install.sh
cd scripts/inference && bash helios-distilled_t2v.sh
```

## Notes

Achieves real-time speed without standard tricks by rethinking training/inference throughput at architecture level. 33-frame chunk size auto-rounds non-multiples up. Community YouTube tutorial covers 4K + consumer PC setup.