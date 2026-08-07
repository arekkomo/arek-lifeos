# ComfyUI / RRHub Main Update Regression Checklist

Verified: 2026-08-06  
Owner: System  
Scope: RealityRove Hub ComfyUI production maintenance on Spark

## Current production baseline before main update

Main instance:
- Port: `8188`
- Manager: `systemd` service `comfyui.service`
- Checkout: `/home/realityrove/ComfyUI`
- Venv: `/home/realityrove/comfyui-env`
- Current pin: `86f987ca` — `chore(openapi): sync shared API contract from cloud@00ef9cc (#14423)`
- Expected local patches:
  - `comfy/utils.py`: DGX Spark safetensors `copy=False` workaround
  - `folder_paths.py`: `.onnx` detection model extension support

ComfyUI-Manager baseline:
- Path: `/home/realityrove/ComfyUI/custom_nodes/ComfyUI-Manager`
- Current pin: `d47c9346` — `update DB`

Current main venv baseline:
- `torch`: `2.12.0+cu130`
- `torchvision`: `0.27.0+cu130`
- `numpy`: `2.3.5`
- `comfyui-frontend-package`: `1.45.15`
- `comfyui-workflow-templates`: `0.10.0`
- `comfy-kitchen`: `0.2.10`
- `comfy-aimdo`: `0.4.10`

Parked instances verified before this checklist:
- `comfyui-h3`: stopped, `0b`
- `comfyui-qwen`: stopped, `0b`
- Main `8188 /queue`: empty

## Discovery summary

I scanned RRHub Comfy routes and graph/template files under:

- `/home/realityrove/Projects/RealityRoveHub/web/src/app/api/comfy`
- `/home/realityrove/Projects/RealityRoveHub/web/src/lib`

Current production `8188 /object_info` contains **134 of 136** discovered RRHub-required classes.

The only missing classes on 8188 are expected because they belong to H3 on 8190:

- `MiniMaxH3ImageToVideo`
- `MiniMaxH3ReferenceToVideo`

## Critical rule

Do not restart production `8188` after updating disk/venv until a test instance or direct object-info regression confirms required nodes remain available.

## RRHub workflow map and regression targets

### LTX 2.3 i2v / t2v — Main 8188

Files:
- `web/src/app/api/comfy/ltx23-i2v/queue/ltx23-i2v-workflow.json`
- `web/src/app/api/comfy/ltx23-i2v/queue/route.ts`
- `web/src/app/api/comfy/ltx2-t2v/queue/route.ts`

Key node classes:
- `CheckpointLoaderSimple`
- `LTXAVTextEncoderLoader`
- `LTXVConditioning`
- `LTXVImgToVideoInplace`
- `LTXVPreprocess`
- `LTXVCropGuides`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVAudioVAELoader`
- `LTXVAudioVAEDecode`
- `LTXVLatentUpsampler`
- `LatentUpscaleModelLoader`
- `ManualSigmas`
- `SamplerCustomAdvanced`
- `SaveVideo`

Key models/files:
- `ltx-2.3-22b-dev-fp8.safetensors`
- `ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors`
- `ltx-2.3-spatial-upscaler-x2-1.1.safetensors`
- `gemma_3_12B_it_fp4_mixed.safetensors`
- `gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors`

Smoke pass:
- Graph validates against updated object_info.
- Model filenames still visible in Comfy model lists.
- Low-cost tiny render only after no queues are active.

### Hunyuan Video 1.5 i2v — Main 8188

File:
- `web/src/app/api/comfy/hunyuan15-i2v/queue/route.ts`

Key node classes:
- `HunyuanVideo15ImageToVideo`
- `CLIPVisionLoader`
- `CLIPVisionEncode`
- `DualCLIPLoader`
- `UNETLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `SamplerCustomAdvanced`
- `SaveVideo`

Key models/files:
- `hunyuanvideo1.5_720p_i2v_fp16.safetensors`
- `hunyuanvideo15_vae_fp16.safetensors`
- `qwen_2.5_vl_7b_fp8_scaled.safetensors`
- `sigclip_vision_patch14_384.safetensors`
- `byt5_small_glyphxl_fp16.safetensors`

Smoke pass:
- Required node classes available.
- API graph validates.

### Wan 2.2 F2L — Main 8188

File:
- `web/src/app/api/comfy/wan22-f2l/queue/route.ts`

Key node classes:
- `WanFirstLastFrameToVideo`
- `UnetLoaderGGUF`
- `KSamplerAdvanced`
- `RIFE VFI`
- `CreateVideo`
- `SaveVideo`

Key models/files:
- `Wan2.2-I2V-A14B-HighNoise-Q3_K_S.gguf`
- `Wan2.2-I2V-A14B-LowNoise-Q3_K_S.gguf`
- `Wan2.2-Lightning_I2V-A14B-4steps-lora_HIGH_fp16.safetensors`
- `Wan2.2-Lightning_I2V-A14B-4steps-lora_LOW_fp16.safetensors`
- `wan_2.1_vae.safetensors`
- `umt5_xxl_fp8_e4m3fn_scaled.safetensors`
- `rife47.pth`

Smoke pass:
- Required nodes still registered.
- GGUF loader still sees Wan GGUF files.

### SAM3 Masking — Main 8188

Files:
- `web/src/lib/sam3-mask-graph.ts`
- `web/src/app/api/comfy/sam3-mask/queue/route.ts`

Key node classes:
- `SAM3_Detect`
- `SAM3_VideoTrack`
- `SAM3_TrackToMask`
- `LoadVideo`
- `GetVideoComponents`
- `SaveVideo`

Key models/files:
- `sam3.pt`
- `sam3.1_multiplex_fp16.safetensors`
- `params.ckpt`

Smoke pass:
- SAM3 nodes registered.
- Video graph validates.

### Trellis2 3D — Main 8188

Files:
- `web/src/app/api/comfy/trellis2/templates/*.json`
- `web/src/lib/trellis2-graph.ts`
- `web/src/app/api/comfy/trellis2/queue/route.ts`

Key node families:
- `Trellis2LoadModel`
- `Trellis2PreProcessImage`
- `Trellis2ImageCondGenerator`
- `Trellis2ShapeGenerator`
- `Trellis2ShapeCascadeGenerator`
- `Trellis2SparseGenerator`
- `Trellis2DecodeLatents`
- `Trellis2MeshWithVoxelToTrimesh`
- `Trellis2ReconstructMeshWithQuad`
- `Trellis2SimplifyMesh`
- `Trellis2ExportMesh`
- `Trellis2MeshTexturing`
- `Trellis2RenderMultiViewNvdiffrast`
- `Trellis2MultiViewTexturing`

Smoke pass:
- All selected Trellis2 template classes are present in object_info.
- At least one MeshOnly / MeshWithTexturing graph validates.

### SeFi Image t2i — Main 8188

Files:
- `web/src/lib/sefi-t2i.ts`
- `web/src/app/api/comfy/sefi-t2i/queue/route.ts`

Key node classes:
- `RebelsSeFiLoader`
- `RebelsSeFiSampler`
- `SaveImage`

Key models/files:
- `SeFi-5B-Turbo_transformer_bf16.safetensors`
- `SeFi_Qwen3-VL-4B_text_bf16.safetensors`
- `SeFi_VAE.safetensors`

Smoke pass:
- Rebels SeFi node classes present.
- Model filenames visible.

### Z-Image scene thumbnail t2i — Main 8188

File:
- `web/src/app/api/comfy/scene-thumb-t2i/queue/route.ts`

Key node classes:
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `EmptySD3LatentImage`
- `ModelSamplingAuraFlow`
- `KSampler`
- `SaveImage`

Key models/files:
- `z_image_turbo_bf16.safetensors`
- `qwen_3_4b.safetensors`
- `ae.safetensors`

Smoke pass:
- Core classes available.
- Model files visible.

### PiD Upscale — Main 8188

Files:
- `web/src/lib/pid-upscale-graph.ts`
- `web/src/app/api/comfy/pid-upscale/queue/route.ts`

Key node classes:
- `PiDConditioning`
- `EmptyChromaRadianceLatentImage`
- `SamplerCustom`
- `ImageScale`
- `SaveImage`

Key models/files:
- `pid_flux1_512_to_2048_4step_bf16.safetensors`
- `pid_flux1_1024_to_4096_4step_bf16.safetensors`
- `flux-vae-bf16.safetensors`
- `gemma-2-2b-it_elm_bf16.safetensors`

Smoke pass:
- PiD custom nodes present.
- Graph validates.

### Qwen Multiangle — Qwen 8189, shared main checkout/venv

File:
- `web/src/app/api/comfy/qwen-multiangle/queue/route.ts`

Important runtime condition:
- Uses shared `/home/realityrove/ComfyUI` and `/home/realityrove/comfyui-env`.
- Must run without `--use-sage-attention`.

Key node classes:
- `QwenMultiangleCameraNode`
- `TextEncodeQwenImageEditPlus`
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextImageScale`
- `CFGNorm`
- `ModelSamplingAuraFlow`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly`

Key models/files:
- `qwen_image_edit_2511_bf16.safetensors`
- `qwen_2.5_vl_7b_fp8_scaled.safetensors`
- `qwen_image_vae.safetensors`
- `Qwen-Edit-2509-Multiple-angles.safetensors`
- `Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors`

Smoke pass:
- Start `comfyui-qwen` only when queue/memory is clear.
- Verify it boots on 8189.
- Confirm command does not include `--use-sage-attention`.
- Run minimal graph validation / test prompt to ensure no black frames.
- Park it again.

### H3 MiniMax — H3 8190, separate checkout/venv

Files:
- `web/src/lib/minimax-h3-templates/fl2va.json`
- `web/src/lib/minimax-h3-templates/ref2va.json`
- `web/src/lib/minimax-h3-graph.ts`
- `web/src/app/api/comfy/minimax-h3-fl2va/queue/route.ts`
- `web/src/app/api/comfy/minimax-h3-r2v/queue/route.ts`

Already updated separately on 2026-08-06:
- H3 checkout now `2340099d` — `Fix full offload on minimax audio vae. (#15377)`
- `comfyui-h3` verified and parked.

Key H3 classes:
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3ReferenceToVideo`
- `EmptyMiniMaxH3LatentAV`
- `MiniMaxH3SigmaShift`

Critical input names:
- RRHub fixtures use dotted dynamic input names such as `ref_images.ref_image_0`.
- H3 object_info exposes autogrow group names rather than expanded dotted names; source schema still uses:
  - group `ref_images`, prefix `ref_image_`
  - group `ref_videos`, prefix `ref_video_`
  - group `ref_video_audios`, prefix `ref_video_audio_`
  - group `ref_audios`, prefix `ref_audio_`

## Main update execution plan

### 1. Snapshot before touching main again

Save under `/home/realityrove/comfyui-backup/<timestamp>-main-pre-update/`:

- `git rev-parse HEAD` for `/home/realityrove/ComfyUI`
- `git status -sb`
- `git diff -- comfy/utils.py folder_paths.py`
- `git rev-parse HEAD` for `ComfyUI-Manager`
- `/home/realityrove/comfyui-env/bin/pip freeze`
- Current `8188 /system_stats`
- Current `8188 /object_info` required-class pass/fail list

### 2. Update disk but do not restart production

- Stash local DGX patches.
- Pull `/home/realityrove/ComfyUI`.
- Reapply/verify:
  - `copy=False` workaround in `comfy/utils.py`
  - `.onnx` support in `folder_paths.py`
- Pull `ComfyUI-Manager`.
- Update venv requirements.
- Restore/pin CUDA torch if pip pulled a plain wheel:
  - `torch==2.12.0+cu130` or explicitly approved newer `+cu130` wheel
  - `torchvision==0.27.0+cu130` or matching approved newer `+cu130` wheel
  - `numpy<2.4`

### 3. Validate without production restart

Preferred: start a temporary test instance on port `8191` from `/home/realityrove/ComfyUI` + `/home/realityrove/comfyui-env` with production-equivalent flags and a **separate database**:

```bash
/home/realityrove/comfyui-env/bin/python /home/realityrove/ComfyUI/main.py \
  --listen 127.0.0.1 --port 8191 \
  --bf16-unet --use-sage-attention --disable-mmap --reserve-vram 32.0 \
  --database-url sqlite:////tmp/comfyui-8191-test.db
```

Do not omit `--database-url` when production 8188 is running. A second ComfyUI process can otherwise attempt migrations/locks against `/home/realityrove/ComfyUI/user/comfyui.db`.

Then verify:

- `curl -sf http://127.0.0.1:8191/system_stats`
- `curl -sf http://127.0.0.1:8191/object_info`
- Required-class diff has zero unexpected missing classes.
- Torch reports `+cu130` and CUDA true.

### 4. Regression validation

Before production cutover:

- Object-info validation for all RRHub Main/Qwen classes.
- Model-file existence/visibility validation for all listed model filenames.
- One low-cost graph validation for each workflow group.
- Optional render smoke tests in this priority:
  1. Z-Image scene thumbnail
  2. SeFi t2i
  3. SAM3 short clip/mask
  4. Wan tiny test
  5. LTX tiny test
  6. Hunyuan tiny test
  7. Trellis2 minimal mesh test
  8. Qwen Multiangle on 8189 with no SageAttention

### 5. Cutover gate

Only restart production `comfyui.service` when:

- Queues are empty.
- H3 and Qwen are parked.
- Test instance passes object_info and package checks.
- Arek approves production cutover.

After restart:

- Verify `8188 /system_stats`.
- Verify `8188 /object_info`.
- Run one minimal RRHub smoke job.

## Rollback trigger

Rollback immediately if:

- Torch is not `+cu130`.
- `torch.cuda.is_available()` is false.
- SageAttention crashes at startup or render time.
- Required RRHub node classes disappear.
- Dynamic H3/Qwen-style inputs validate but are silently ignored.
- Any production workflow loses exact model filename mapping.
