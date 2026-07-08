# AudioStory

Tags: AI Automation, Content Creation
Description: Framework that uses LLMs + diffusion to generate long‑form narrative audio from text or video.
URL: https://github.com/TencentARC/AudioStory
Date Added: November 15, 2025 5:14 PM
Type: Github
Archive: No
Spark: No

## Summary

AudioStory integrates large language models to decompose narrative instructions into temporally ordered sub‑tasks, then leverages a diffusion‑based audio generator with bridging tokens for semantic & residual cues, enabling coherent, long‑form audio generation beyond short clips.

## Features

- Decomposes prompts into sequential audio events using an LLM
- Uses bridging tokens (semantic + residual) to link reasoning and audio generation
- Supports video dubbing, audio continuation, and long‑narrative audio generation via benchmark AudioStory‑10K

## Use Cases

Generate long‑duration audio for film/VR, turn text/story into audio narrative, dub existing footage with aligned sound events.

## Installation

Clone the repo; python 3.10+, PyTorch 2.1+; run `bash install_audiostory.sh`; inference script: `python evaluate/inference.py --model_path ckpt/audiostory‑3B --guidance 4.0 --total_duration <secs>` (as per README). ([github.com](https://github.com/TencentARC/AudioStory?utm_source=chatgpt.com))

## Other Info

Released by Tencent ARC Lab in 2025; open‑source under Apache 2.0; inference code and demo videos available; full training code and dataset planned. ([github.com](https://github.com/TencentARC/AudioStory?utm_source=chatgpt.com))