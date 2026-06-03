---
name: Spark ComfyUI Model Downloads
description: ComfyUI folder structure on Spark machine and model type routing rules
type: reference
originSessionId: 2f5eb8b1-56f1-43b4-af73-96744d260e97
---
# Spark ComfyUI — Model Download Reference

**Machine:** `realityrove@spark-6d75`
**ComfyUI models base path:** `~/ComfyUI/models/`

## Folder → Model Type Mapping

| Folder | Model types |
|--------|-------------|
| `checkpoints/` | Main diffusion checkpoints (SD, SDXL, etc.) |
| `loras/` | LoRA files |
| `vae/` | VAE models |
| `controlnet/` | ControlNet models |
| `embeddings/` | Textual inversions / embeddings |
| `upscale_models/` | Traditional pixel-space upscalers (ESRGAN, etc.) |
| `latent_upscale_models/` | Latent/diffusion-based upscalers — **LTX spatial upscalers go here** |
| `diffusion_models/` | Video diffusion models (LTX-Video main models, etc.) |
| `text_encoders/` | CLIP / T5 text encoders |
| `clip/` | CLIP models |
| `unet/` | UNet models |

## Known Routing Rules

- **LTX spatial upscalers** (e.g. `ltx-2.3-spatial-upscaler-*.safetensors`) → `latent_upscale_models/` (NOT `upscale_models/`)

## Download Command Template

```bash
wget -O ~/ComfyUI/models/<folder>/<filename> <huggingface_url>
```

## Move Command Template

```bash
mv ~/ComfyUI/models/<source_folder>/<filename> ~/ComfyUI/models/<dest_folder>/
```
