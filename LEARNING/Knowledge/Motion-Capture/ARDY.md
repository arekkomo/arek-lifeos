---
title: "ARDY — Interactive Human Motion Generation"
category: source
summary: NVIDIA autoregressive diffusion system for responsive text-guided human/robot motion with long-horizon kinematic constraints such as root paths, waypoints, full-body keyframes, and sparse joints.
tags: [human-motion, motion-generation, autoregressive-diffusion, text-to-motion, kinematic-constraints, real-time, nvidia]
sources: 1
source_path: https://github.com/nv-tlabs/ardy
source_date: 2026-07
authors: [NVIDIA Toronto AI Lab]
ingested: 2026-07-19
updated: 2026-07-19
---

# ARDY — Interactive Human Motion Generation

**Repository:** [nv-tlabs/ardy](https://github.com/nv-tlabs/ardy) · **Project:** [NVIDIA Research](https://research.nvidia.com/labs/sil/projects/ardy/) · **License:** Apache 2.0 (code); NVIDIA Open Model Agreement (checkpoints)

## What it is

ARDY (*Autoregressive Diffusion with Hybrid Representation*) is NVIDIA's interactive motion-generation system. It continuously generates motion from streaming text prompts and constraints rather than creating one fixed clip upfront.

## Controls and outputs

- Streaming text-to-motion
- Root paths and waypoints
- Full-body keyframes
- Sparse joint position/rotation constraints
- Mouse waypoint and keyboard velocity control in the browser demo
- Optional post-processing for foot-skate reduction and constraint adherence

Released checkpoints cover a generic Core skeleton and Unitree G1, at 20–25 FPS with 8–52 frame prediction horizons. A SOMA human-body skeleton model is listed as forthcoming.

## Practical fit

File under **Motion Capture** rather than AI-Video: ARDY generates skeletal/kinematic motion data, not rendered footage. It is relevant to animation blocking, previz, virtual characters, and robotics; rendered character/video output needs a downstream animation or video-generation stage.

## Requirements / status

- Code + demos + checkpoints released
- Tested on Ubuntu 22.04 / RTX 4090; PyTorch >=2.4, Python >=3.10
- Text encoder is gated Meta-Llama-3-8B-Instruct and requires approved Hugging Face access plus a token
- TensorRT acceleration is optional

## Related

- [[NVIDIA ARDY — Official Source Summary]] — verified prompt/constraint evidence and scope boundary for ARDY-specific motion authoring
- [[ARDY Text-to-Motion Prompting]] — body-first prompt grammar; use this rather than cinematography vocabulary
- [[ARDY Streaming Prompt and Constraint Workflow]] — assign action semantics to text and spatial precision to explicit kinematic controls
- [[Interactive-Kinematic-Motion-Generation]] — control pattern and comparison points
- [[MotionLCM]] — real-time text/pose motion generation via latent consistency, versus ARDY's autoregressive diffusion approach
- [[ProxyPose]] — extracts 6-DoF motion from video; ARDY generates new constrained motion
