---
title: "ID-LoRA — Identity-Driven Audio-Video Personalization"
category: source
summary: Identity-preserving unified audio-video generation model that jointly generates a subject's appearance and voice in a single diffusion pass. Text prompt + reference image + short audio clip produce talking video with matching face and voice. ECCV 2026 accepted. Trained on ~3K pairs; zero-shot inference via LoRA weights.
tags: [id-lora, voice-transfer, identity-preservation, talking-heads, ltx-2-series, unified-audio-video, comfui-native, eccv-2026]
sources: 2
source_path: raw/id-lora/README.md + arXiv 2603.10256
source_date: 2026-03
authors: [Aviad Dahan et al.]
ingested: 2026-07-13
updated: 2026-07-13
---

# ID-LoRA — Identity-Driven Audio-Video Personalization

## TL;DR

ID-LoRA (In-Context LoRA) enables **identity-preserving audio-video generation in a single unified model**. Given a text prompt, reference image, and short (~5s) audio clip, it produces a talking video where the face matches the reference subject and the voice sounds like the reference speaker — all generated simultaneously.

Unlike cascaded pipelines (face + lip-sync separately, then voice cloning), ID-LoRA operates in a **unified latent space** where scene content, vocal identity, and environment acoustics are co-synthesized.

## Architecture

### Unified Audio-Diffusion Design

Built on top of LTX-2 (19B parameters, now also LTX-2.3 22B), ID-LoRA introduces a LoRA adaptation that:
- Preserves the base model's generative capabilities
- Adds identity conditioning branches for visual likeness and vocal fingerprint
- Requires only ~3K image-audio pairs for training (single GPU)

### Inference Modes

| Mode | Description | VRAM | Best For |
|------|-------------|------|----------|
| One-stage | Standard inference, single pass | 24GB+ | Fast prototyping |
| Two-stage HQ | 2x spatial upsampling + refined audio output | 48GB+ | Final production assets |

### Prompt Format (Structured)

ID-LoRA uses a tagged prompt format for simultaneous control:

```
[VISUAL]: <scene, subject appearance, clothing, setting>
[SPEECH]: <exact dialogue to speak>
[SOUNDS]: <vocal quality + ambient/environmental sounds>
```

**Example:**
```
[VISUAL]: Medium shot, woman with curly hair in white blouse, modern kitchen
[SPEECH]: "Hello everyone, welcome to our channel."
[SOUNDS]: Calm conversational tone at moderate volume, soft birds chirping background
```

## Key Capabilities

- **Zero-shot inference**: Load LoRA weights — no per-speaker fine-tuning
- **Voice identity transfer**: Matching vocal characteristics from ~5s reference audio
- **Visual likeness via first-frame conditioning**: Reference image controls facial features
- **Prompt-driven environment control**: Scene + acoustics both controlled by text prompts
- **Unified generation**: Voice and appearance synthesized jointly, not cascaded

## Integration

### ComfyUI Native Support
Upstream PR #13111 adds native ID-LoRA support to ComfyUI (via `[VISUAL]`/`[SPEECH]`/`[SOUNDS]` parsing). Compatible with both LTX-2 and LTX-2.3 checkpoints.

**Custom node repo**: [ID-LoRA-LTX2.3-ComfyUI](https://github.com/ID-LoRA/ID-LoRA-LTX2.3-ComfyUI) (if native PR not yet applied in your ComfyUI instance)

### Requirements
- **Hardware**: 24GB+ VRAM minimum. 48GB recommended for two-stage HQ mode.
- **Base models**: LTX-2 or LTX-2.3 checkpoints
- **Pre-trained LoRA weights**: Available via [HuggingFace - AviadDahan](https://huggingface.co/AviadDahan)
- **Reference data**: CelebV-HQ / TalkVid datasets (for training, not inference)

## Relevance to Creative Directorial Workflow

### Pre-Visualization Application
ID-LoRA is a **character-consistent prototyping tool**. For film directing development:
1. Take a photo/reference image of an actor or character design
2. Upload short voice sample (from audition tape, location scout audio, etc.)
3. Generate short talking-head video clips with the exact character look + voice

This enables **rapid storyboarding with consistent character identity** across shots — crucial for pre-vis sequences where maintaining character recognition is essential.

### Director's Use Cases
- **Shot blocking tests**: Try different framing/compositions on a character prototype
- **Audition tape integration**: Generate mock responses from audition recordings into your narrative scenarios  
- **Location-independent performances**: Generate dialogue performances with consistent voice/face across any background scene the prompt generates

## Limitations / Constraints (from README notes)

- **Reference audio duration matters**: Optimized for ~5s; shorter/longer may reduce fidelity. This is a hard constraint on the training data design.
- **Hardware requirement 48GB VRAM** for two-stage HQ mode — may be expensive if only occasional use needed. Single-stage inference at 24GB is cheaper but lower quality.
- **Trained on ~3K pairs** — likely limited to celebrity/face datasets available in CelebV-HQ; generalization to non-standard faces not documented.

## Connections

- [[Parametric-Digital-Humans]] / [[GNM]] — an explicit 3D head model offers a complementary upstream asset for identity and facial-control workflows; ID-LoRA remains the image/audio-conditioned video-generation layer.
- `[[LTX 2-Series|LTX-2/LTX-2.3]]` — base model architecture
- `Diffusion-Video-Models` — unified multi-modal diffusion approach
- **Convergence note**: Combines with [[PixWorld|3D scene generation]], [[Alaya Workd|long-horizon world models]] for a full pipeline: generate 3D environments → animate characters within them → consistent voice identity across scenes
