# ComfyUI Compendium

> **Purpose:** Central reference for ComfyUI on DGX Spark — setup, maintenance, troubleshooting, and best practices.
> Last updated: 2026-06-16

---

## System Information

| Item | Detail |
|---|---|
| **Host** | DGX Spark (NVIDIA GB10, 122 GB VRAM, 3.7 TB NVMe) |
| **Install path** | `/home/realityrove/ComfyUI` |
| **Virtual environment** | `/home/realityrove/comfyui-env` |
| **Port** | 8188, accessible at `10.0.0.61:8188` |
| **Version** | v0.25.0 |
| **Frontend** | 1.45.15 |
| **Python** | 3.12.3 |
| **PyTorch** | 2.12.0+cu130 |
| **Driver** | 580.142 |
| **Service** | systemd (enabled, auto-restart) |

---

## Startup Flags

```bash
/home/realityrove/comfyui-env/bin/python /home/realityrove/ComfyUI/main.py \
  --listen 0.0.0.0 --port 8188 \
  --highvram --bf16-unet --use-sage-attention --disable-mmap \
  --reserve-vram 40.0
```

**VRAM math:** 122 GB total → 40 GB reserved → ~58 GB for ComfyUI workflows (Ollama at 24 GB)

---

## Dependency Versions

| Package | Version | Notes |
|---|---|---|
| **numpy** | 2.3.5 | Pinned down from 2.4 — Numba-dependent nodes need <2.4 |
| **pillow** | 12.2.0 | Conflicts with moviepy/inference-cli but OK for ComfyUI |
| **comfy-kitchen** | 0.2.10 | **Required** for v0.25+ |
| **comfy-aimdo** | 0.4.10 | **Required** for v0.25+ |
| **comfyui-frontend-package** | 1.45.15 | Verify after updates; browser needs hard-refresh |


---

## Known Import Failures (non-blocking)

| Node | Issue | Notes |
|---|---|---|
| was-ns | Numba needs NumPy 2.3 or less | **Fixed** by pinning numpy<2.4 |
| ComfyUI-Allor | Same Numba issue | **Fixed** |
| teacache | API mismatch (precompute_freqs_cis) | Needs update for v0.25+ |
| SageAttention | Missing __init__.py | Corrupted install |
| Comfyui-Toolbox | No moviepy.editor | Not used |
| ComfyUI-reactor | No insightface | Not used |
| vertex-ai-comfyui-nodes | No google.cloud.storage | Not used |
| ComfyUI-Adforge | No google.cloud.storage | Not used |
| ComfyUI-GGUF-FantasyTalking | Unicode escape syntax error | Author bug |

---

## Maintenance Procedures

### Quick health check
```bash
# API status
curl -s http://127.0.0.1:8188/system_stats | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['system']['comfyui_version'])"

# VRAM
nvidia-smi --query-gpu=memory.used,memory.total --format=csv,noheader,nounits

# Ollama
ollama ps

# GPU load
nvidia-smi
```

### Update ComfyUI
```bash
cd /home/realityrove/ComfyUI && git pull
source /home/realityrove/comfyui-env/bin/activate
pip install -r requirements.txt
pip install --upgrade \
  comfyui-frontend-package comfyui-workflow-templates comfyui-embedded-docs \
  comfy-kitchen comfy-aimdo numpy pillow
systemctl restart comfyui
```

### Update custom nodes
- **UI:** Manager → Check Updates / Install Missing Custom Nodes
- **Manual:** `git pull` in node dir, then restart

### ComfyUI crash patterns

| Symptom | Cause | Fix |
|---|---|---|
| Node crashes mid-job | NumPy >2.4 breaks Numba | `pip install 'numpy<2.4'` |
| API unresponsive 10s after start | GPU warmup | Wait |
| "Frontend outdated" warning | Cached old frontend | Hard-refresh browser |
| Process running, GPU idle | Old version incompatibility | `kill + restart`, check logs |
| Process consuming RAM but crashing | OOM | Check `dmesg -T` |

### VRAM Management

- Reserve: `--reserve-vram 40.0` (40 GB for Ollama/system)
- Large video workflows: unload Ollama (`ollama rm qwen3.6:latest`) temporarily
- Always save `.json` before long renders — **no checkpoint/resume**

---

## Key Paths

- **ComfyUI:** `/home/realityrove/ComfyUI`
- **Venv:** `/home/realityrove/comfyui-env`
- **Custom nodes:** `/home/realityrove/ComfyUI/custom_nodes/`
- **Models:** `/home/realityrove/ComfyUI/models/`
- **Output:** `/home/realityrove/ComfyUI/output/`
- **Current log:** `/home/realityrove/ComfyUI/comfyui_restart.log`
- **Service config:** `/home/realityrove/comfyui.service.new`

---

## Ollama Status

- **Loaded model:** qwen3.6:latest (23 GB) — only model installed
- **Removed:** qwen3:14b, gemma4, qwen3-vl, qwen3, nomic-embed-text (saved ~30 GB)
- **VRAM cap:** `OLLAMA_MAX_VRAM=40000` in `/var/snap/ollama/common/env`
- **Restart:** `sudo snap restart ollama` (not `systemctl`)

---

## Resources

- ComfyUI docs: https://docs.comfy.org
- ComfyUI GitHub: https://github.com/Comfy-Org
- ComfyUI-Manager: https://github.com/ltdrdata/ComfyUI-Manager
- DGX Spark docs: https://docs.nvidia.com/dgx/dgx-spark/

---

## Lessons Learned

1. **Frontend version mismatch breaks workflows silently** — Always verify 1.45.15+ and hard-refresh browser
2. **NumPy 2.4+ breaks Numba-dependent nodes** — Keep pinned at <2.4
3. **v0.25+ requires comfy-kitchen + comfy-aimdo** — Separate install needed
4. **No auto-recovery of running jobs** — Save `.json` before long renders
5. **GB10 shared GPU** — Set `--reserve-vram` and manage Ollama models
6. **Ollama snap uses `snap set` not `systemctl`**
7. **ComfyUI takes ~10s to warm up after startup** — Don't send workflow immediately
8. **Models on disk don't use VRAM** — Only loaded models consume GPU; clean up unused ones

---

## Version History

- 2026-06-16: Initial creation — migration from troubleshooting session, v0.25.0 upgrade
