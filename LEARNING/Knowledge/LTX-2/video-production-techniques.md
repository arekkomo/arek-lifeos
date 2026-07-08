---
title: LTX 2.3 Video Production Techniques & Workflow
category: concept
summary: Practical video production strategies for LTX-2.3 — pipeline selection, image-to-video workflows, keyframe interpolation, retakes, upscaling chains, optimization techniques, LoRA application strategies
tags: [ltx-2, ltx-2.3, video-production, workflow, pipelines, upsampling, lora, optimization, image-to-video, keyframe]
sources: 2
updated: 2026-07-04
---

# LTX 2.3 Video Production Techniques & Workflow

## Pipeline Selection Strategy

### When to Use Which Pipeline:

| Scenario | Recommended Pipeline | Why |
|----------|---------------------|-----|
| Final production video | [[TI2VidTwoStagesHQPipeline]] | HQ sampler = best quality, 2x spatial upscale baked in |
| Balanced quality/speed | [[TI2VidTwoStagesPipeline]] | Standard two-stage flow with upscaler for good results |
| Quick idea prototyping | [[TI2VidOneStagePipeline]] | Single-stage is fastest for concept validation |
| Speed testing prompts | DistilledPipeline | Only 8 steps (S1) + 4 steps (S2) — ~4x faster than standard |
| Video-to-video transform | IClora Pipeline | Requires distilled model + IC-LoRA Union Control |
| Image sequence animation | KeyframeInterpolationPipeline | Interpolates between uploaded keyframes naturally |
| Audio-reactive video | A2VidTwoStage | Generates video from audio input timing |
| Lip-sync dubbing | LipDub Pipeline | Matches lip motion to spoken audio, preserves speaker identity |
| HDR workflow | HRICLoraPipeline | EXR export capability for color grading in DaVinci Resolve |

## Two-Stage Generation Deep Dive (Production Quality)

The **TI2VidTwoStagesHQPipeline** is the gold standard for production work:

### Stage 1: Low-Res Base Pass
```
Prompt → [Distilled LoRA] → Base video at half resolution + low quality
              ↓
       Spatial Upscaler (x2 or x1.5) ← stage output is upscaled
              ↓
       Second-pass generation on upscaled input = polished result
```

### Stage 2: Hi-Res Refinement Pass
```
Upscaled frame → Second round of attention-based refinement
                → Higher spatial fidelity + cleaner details
```

**Why two-stage matters**: The model can focus temporal coherence at full resolution during stage 2 instead of trying to do both timing AND quality simultaneously in one pass. This is why HQ output looks noticeably better than single-stage outputs.

### Two-Stage Best Practices:

1. **Always use the Distilled LoRA** — it's required for two-stage workflows and dramatically accelerates stage 1
2. **Use a good keyframe image** as your starting point — upscaler enhances what's already there
3. **Run at least 40 diffusion steps** total (20 S1 + 20 S2) for critical productions
4. **If VRAM is limited, disable memory cleanup between stages** — it adds overhead without benefit

## Image-to-Video (I2V) Workflow

### Step 1: Prepare Keyframe Image
- Generate/select a strong base image first → ComfyUI + Midjourney/Flux pipeline
- Or shoot reference footage → extract ideal frame
- **Key**: The keyframe determines composition, character appearance, and scene layout permanently

### Step 2: Apply IC-LoRA Control (Optional but Recommended)
```
Recommended chain for precise control:
1. IClora Pipeline + Union Control LoRA (ref weight ~0.5)
2. Adds temporal continuity while preserving image fidelity
3. Essential for maintaining character consistency between frames
```

### Step 3: Refine with Prompt
- Apply full cinematographic prompt to guide motion within the keyframe scene
- LTX-2's cross-modal attention ensures audio sync with visual content automatically

## Keyframe Interpolation Technique

### When to Use:
- **Storyboard animation** — bridge from concept art to moving video without intermediate frames
- **Scene transition creation** — smooth morphing between two compositions
- **Morphing effects** — gradual character/object transformation

### How It Works:
```
Keyframe A (start image) → KeyframeInterpolationPipeline → Keyframe B (end image)
                                           ↓
                              Generates smooth intermediate frames
                            Character and scene elements transition naturally
                                       ↓
                             Audio generated in sync with visual motion patterns
```

## Retake Technique (Selective Regeneration)

### Use Cases:
- Bad segment at timestamp X but good elsewhere
- Need different action from same base video
- Fix specific moment without regenerating entire clip

### Method:
```python
RetakePipeline(regenerate_start=5.2, regenerate_end=7.8, prompt="new action")
```
> Regenerates only the time range 5.2s to 7.8s while keeping rest of footage intact

## Spatial Upscaling Chain (When You Need More Resolution)

### Available Upscalers:
| Upscaler | Multiplier | Best For |
|----------|-----------|----------|
| ltx-2.3-spatial-upsampler-x1.5 | 1.5x | Subtle resolution bump on strong base renders |
| ltx-2.3-spatial-upsampler-x2.0 | 2x | Full HD from quarter-HD (480p → 960p) or 720p → 1080p |

### Upscaling Decision Flow:

```
Do I need upsampling?
├── Yes (need more detail) → Use TwoStageHQPipeline (includes x2 upscale natively)
├── Already on two-stage pipeline? → Skip extra upscaling — redundant
└── Need 1.5x only? → Use the x1.5 model directly instead of x2
```

> ⚠️ **Warning**: Upscaling doesn't add information that wasn't in the base render — it interpolates. If your base has blurry faces, upsampling won't fix them. Fix at the source with better prompts or keyframes first.

## Optimization Techniques for DGX Spark Workflows

### VRAM Management (Critical on Limited GPUs):
| Technique | Impact on VRAM | Speed Impact | Quality Impact |
|-----------|---------------|-------------|--------------|
| FP8 Cast quantization | ~-25% | Comparable | Minimal |
| Block streaming (RAM mode) | ~-40% peak GPU | ~-10% (CPU RAM overhead) | None |
| Skip memory cleanup between stages | +10% peak VRAM | ~+30% processing speed (saves allocations) | None |

### Optimized DGX Spark Command Pattern:
```bash
# For 2-stage production quality on limited hardware:
TI2VidTwoStagesPipeline \
  --quantization fp8_cast \
  --steps 24 (16+8 split) \
  --enhance_prompt True \
  --lora_weight_distilled 0.9
```

### Speed vs Quality Tradeoff Grid:

| Pipeline | Steps/S1 | Steps/S2 | Approx Output Time | Quality Grade |
|----------|---------|---------|-------------------|--------------|
| DistilledPipeline (fastest) | 8 | 4 | ~30s on A6000 | ⭐⭐⭐ Quick test |
| One-Stage Pipeline | 24 | - | ~60s on A6000 | ⭐⭐⭐ Intermediate |
| Two-Stage Standard | 24 | 24 | ~90s on A6000 | ⭐⭐⭐⭐ Production |
| Two-Stage HQ (highest) | 32 | 32 | ~150s on A6000 | ⭐⭐⭐⭐⭐ Final output |

## LoRA Weight Strategies for Different Effects

### Motion Fidelity:
```python
IC_LoRA_Motion_Track_Control: ref_weight=0.5
# Balances motion quality with character appearance preservation
# Lower weight = more freedom to interpret motion but less temporal continuity
# Higher weight = tighter motion tracking but may constrain creative interpretation
```

### Detail Enhancement:
```python
IC_LoRA_Detailer: ref_weight=0.7-1.0
# Increases fine detail in faces, textures, and environmental elements
# Works best at high resolution (after spatial upscaler passes)
```

### Camera Motion Control:
| LoRA | Recommended Weight | Effect |
|------|-------------------|--------|
| Dolly-In/Out | 0.5-0.8 | Subtle camera movement without overshoot |
| Jib-Up/Down | 0.6-1.0 | Smooth vertical arc motion |
| Static | 1.0 | Locks all camera movement for stable compositions |

## Workflow Integration with RealityRowHub / n8n

For automating LTX-2.3 workflows:
> 💡 **Integration Tip**: Use `enhance_prompt=True` parameter in your ComfyUI nodes or Gradio app to automatically expand brief prompt concepts into full cinematographic descriptions before generation — then save the expanded version back to the vault as part of your workflow documentation

## Prompter Agent Design Considerations (for future development)

The following insights should inform any LTX-2.3 automated prompting system:

### Key Decision Points for an Auto-Prompter:
1. **Detect scene type** → select appropriate cinematographic language
2. **Determine target resolution** → choose correct pipeline
3. **Assess motion requirements** → recommend camera LoRA combination
4. **Measure complexity** → expand prompt length to 150-180 words max
5. **Evaluate image availability** → if no keyframe, generate one via ComfyUI first

### Prompt Enhancement Priority List:
- [ ] Convert passive voice to active (HIGHEST)
- [ ] Add specific movement/gesture details
- [ ] Insert camera angle specification
- [ ] Add lighting quality descriptors
- [ ] Specify environmental/atmospheric details
- [ ] Define temporal progression markers
- [ ] Remove abstract/non-visual terms

### What Prompt Enhancers Should NOT Do:
- Don't change the core action concept (stay faithful to user intent)
- Don't exceed 200 words (diminishing returns beyond that)
- Don't introduce contradictory visual elements
- Don't hallucinate specific details not grounded in the original request
