---
title: Qwen-Image-Layered ComfyUI Output Handling
category: concept
summary: Current ComfyUI workflow correction: remove the regenerated original-image slot before decoding editable layer outputs.
tags: [qwen-image-layered, comfyui, latent, rgba, workflow]
sources: 2
updated: 2026-08-09
---

# Qwen-Image-Layered ComfyUI Output Handling

## Critical workflow correction
The Qwen-Image-Layered latent allocation contains `layers + 1` temporal slots. In the current ComfyUI template correction, slot 0 is the model’s regenerated copy of the original image rather than an editable output layer; the Comfy-Org template fix was merged on 2026-08-09.[[qwen-image-layered-source]]

**Implication:** If a workflow requests `N` layers and decodes all temporal slots, it can display `N + 1` images. Discard the first/regenerated-original slot before batching and decoding the actual layer outputs.[[qwen-image-layered-source]]

## Correct node sequence
`KSampler → LatentCut (t dimension, start/index 1) → LatentCutToBatch (t dimension, slice size 1) → VAEDecode`

The merged Comfy-Org correction specifies `LatentCut(dim="t", index=1, amount=16384)` between `KSampler` and `LatentCutToBatch`; use the current official template/version as the source of truth if node names or values change.[[qwen-image-layered-source]]

## Validation check
For a request of `N` layers, confirm that the decoded deliverable contains exactly `N` RGBA layers after the slot-0 cut, then re-composite them to check the result against the input. The regenerated original is a diagnostic/reference output, not one of the deliverable layers.[[qwen-image-layered-source]]

Related: [[layer-decomposition-and-edit-workflow]] · [[qwen-image-layered-prompting-and-parameters]]
