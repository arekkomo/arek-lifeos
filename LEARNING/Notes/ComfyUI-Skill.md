# ComfyUI Maintenance Skill

Procedures for managing ComfyUI on DGX Spark.

## Current Setup

- **Host:** DGX Spark (NVIDIA GB10, 122 GB VRAM)
- **Path:** /home/realityrove/ComfyUI
- **Venv:** /home/realityrove/comfyui-env
- **Port:** 8188 (0.0.0.0 → 10.0.0.61:8188)
- **Version:** v0.25.0 (2026-06-16)
- **Service:** systemd (enabled, Restart=always)

## Startup Flags

```bash
/home/realityrove/comfyui-env/bin/python /home/realityrove/ComfyUI/main.py \
  --listen 0.0.0.0 --port 8188 \
  --highvram --bf16-unet --use-sage-attention --disable-mmap \
  --reserve-vram 40.0
```

## Critical Dependencies

| Package | Version | Notes |
|---|---|---|
| numpy | 2.3.5 | Pinned down! Numba nodes need <2.4 |
| pillow | 12.2.0 | Fine for ComfyUI |
| comfy-kitchen | 0.2.10 | **Required** for v0.25+ |
| comfy-aimdo | 0.4.10 | **Required** for v0.25+ |

## Maintenance Steps

### Health Check
```bash
curl -s http://127.0.0.1:8188/system_stats | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['system']['comfyui_version'])"
nvidia-smi
ollama ps
```

### Update ComfyUI
```bash
cd /home/realityrove/ComfyUI && git pull
source /home/realityrove/comfyui-env/bin/activate
pip install -r requirements.txt
pip install --upgrade comfyui-frontend-package comfyui-workflow-templates comfyui-embedded-docs comfy-kitchen comfy-aimdo numpy pillow 2>/dev/null
systemctl restart comfyui
```

### Update Custom Nodes
1. In ComfyUI: Manager → Check Updates
2. Or manual: `git pull` in node dir + restart

### Troubleshooting

| Symptom | Fix |
|---|---|
| Node crashes mid-job | `pip install 'numpy<2.4'` |
| API unresponsive 10s after start | Wait for GPU warmup |
| "Frontend outdated" warning | Hard-refresh browser (Ctrl+Shift+R) |
| Process running, GPU idle | `kill $(pgrep -f 'main.py.*8188')`, check logs, restart |
| OOM crash | Check `dmesg -T`, reduce `--reserve-vram` or unload Ollama |

### VRAM Management
- 122 GB total → 40 GB reserved → ~58 GB for ComfyUI (Ollama at 24 GB)
- Large workflows: `ollama rm qwen3.6:latest` temporarily
- Always save `.json` before long renders — **no checkpoint/resume**

### Ollama
- Loaded: qwen3.6:latest only (23 GB)
- Cap: `OLLAMA_MAX_VRAM=40000` in `/var/snap/ollama/common/env`
- Restart: `sudo snap restart ollama` (not systemctl)

## Key Paths
- ComfyUI: /home/realityrove/ComfyUI
- Venv: /home/realityrove/comfyui-env
- Custom nodes: /home/realityrove/ComfyUI/custom_nodes/
- Models: /home/realityrove/ComfyUI/models/
- Output: /home/realityrove/ComfyUI/output/
- Log: /home/realityrove/ComfyUI/comfyui_restart.log

## Known Import Failures
was-ns, ComfyUI-Allor: fixed with numpy<2.4. Others blocked but non-functional: teacache, SageAttention, Comfyui-Toolbox, ComfyUI-reactor, vertex-ai, ComfyUI-Adforge, ComfyUI-GGUF-FantasyTalking.

## Resources
- https://docs.comfy.org
- https://github.com/Comfy-Org
- https://github.com/ltdrdata/ComfyUI-Manager
- https://docs.nvidia.com/dgx/dgx-spark/