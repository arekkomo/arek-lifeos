# ComfyUI Compendium

> **Purpose:** Central reference for ComfyUI on DGX Spark — setup, maintenance, troubleshooting, and best practices.
> Last updated: 2026-06-16

---

## System Information

| Item | Details |
|---|---|
| **Host** | DGX Spark (NVIDIA GB10, 122 GB VRAM, 3.7 TB NVMe) |
| **Install path** | `/home/realityrove/ComfyUI` |
| **Virtual environment** | `/home/realityrove/comfyui-env` |
| **Port** | 8188, listens on 0.0.0.0 (accessible at 10.0.0.61:8188) |
| **Current version** | v0.25.0 (2026-06-16) |
| **Frontend** | 1.45.15 |
| **Templates** | 0.10.0 |
| **Python** | 3.12.3 |
| **PyTorch** | 2.12.0+cu130 |
| **NVIDIA Driver** | 580.142 |
| **Service** | systemd, enabled, restarts on crash/reboot |
| **User** | realityrove |

## Core-model capability notes

- **PixelDiT + PiD:** ComfyUI PR [#14103](https://github.com/Comfy-Org/ComfyUI/pull/14103) merged native support for NVIDIA PixelDiT T2I and PiD image encode/decode/upscaling models. See [[PixelDiT]] and [[PiD]]. Model weights are identified as NSCLv1 licensed; do not assume commercial permissiveness.

---

## Startup Flags

```bash
/home/realityrove/comfyui-env/bin/python /home/realityrove/ComfyUI/main.py \
  --listen 0.0.0.0 --port 8188 \
  --highvram --bf16-unet --use-sage-attention --disable-mmap \
  --reserve-vram 40.0
```

**VRAM allocation:** 122 GB total → 40 GB reserved for Ollama/system → ~82 GB for ComfyUI workflows. Current usage ~62 GB free after Ollama loads qwen3.6:latest.

---

## Ollama Integration

- **Model:** qwen3.6:latest (23 GB) — only model installed
- **Removed 5 other models** (saved ~30 GB disk): qwen3:14b, gemma4, qwen3-vl, qwen3, nomic-embed-text
- **VRAM cap:** `OLLAMA_MAX_VRAM=40000` in `/var/snap/ollama/common/env`
- **Snap config:** `snap set ollama max-queue=5` and `max-loaded-models=1`
- **Restart:** `sudo snap restart ollama`

---

## Dependency Versions (critical)

| Package | Version | Notes |
|---|---|---|
| **numpy** | 2.3.5 | Required by was-ns, ComfyUI-Allor (Numba). Older than default. |
| **pillow** | 12.2.0 | Conflicts with moviepy/inference-cli but fine for ComfyUI |
| **comfy-kitchen** | 0.2.10 | Required by v0.25+ |
| **comfy-aimdo** | 0.4.10 | Required by v0.25+ |
| **comfyui-frontend-package** | 1.45.15 | Serve via ComfyUI; browser must hard-refresh (Ctrl+Shift+R) |
| **comfyui-workflow-templates** | 0.10.0 | Required by v0.25+ |
| **comfyui-embedded-docs** | 0.5.4 | Required by v0.25+ |

---

## Known Import Failures (non-critical)

These nodes fail to import but don't block core functionality:

| Node | Error | Action needed |
|---|---|---|
| **was-ns** | `Numba needs NumPy 2.3 or less` | Fix: pinned NumPy to 2.3.5 |
| **ComfyUI-GGUF-FantasyTalking** | Unicode escape syntax error | File issue with author |
| **ComfyUI-Allor** | Same Numba issue as was-ns | Fix: pinned NumPy to 2.3.5 |
| **Comfyui-Toolbox** | `moviepy.editor` missing | Not used? |
| **ComfyUI-reactor** | `insightface` missing | Not used? |
| **vertex-ai-comfyui-nodes** | `google.cloud.storage` missing | Not used? |
| **teacache** | `precompute_freqs_cis` API mismatch | Needs update for v0.25 |
| **SageAttention** | Missing __init__.py | Corrupted install |
| **ComfyUI-Adforge** | `google.cloud.storage` missing | Not used? |

---

## Maintenance Procedures

### Quick Health Check
```bash
# 1. Is ComfyUI running?
curl -s http://127.0.0.1:8188/system_stats 2>/dev/null | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['system']['comfyui_version'])"

# 2. VRAM status
nvidia-smi --query-gpu=memory.used,memory.total --format=csv,noheader,nounits

# 3. Ollama status
ollama ps

# 4. ComfyUI Manager updates
# In ComfyUI UI: Manager → Check Updates
```

### Update ComfyUI
```bash
# 1. Pull latest
cd /home/realityrove/ComfyUI && git pull

# 2. Update venv deps
source /home/realityrove/comfyui-env/bin/activate
pip install -r /home/realityrove/ComfyUI/requirements.txt 2>&1 | tail -10

# 3. Update frontend versions (check API response for mismatch)
pip install --upgrade comfyui-frontend-package comfyui-workflow-templates comfyui-embedded-docs 2>/dev/null

# 4. Restart
systemctl restart comfyui

# 5. Verify
curl -s http://127.0.0.1:8188/system_stats | python3 -c "import sys,json; d=json.load(sys.stdin); v=d['system']['comfy_package_versions']; [print(f'  {x[\"Installed\"]} vs {x[Required\"]}') for x in v]"
```

### Update ComfyUI-Manager
- In UI: `Manager → Update` or `Manager → Install Missing Custom Nodes`

### Backup Workflows
- Save `.json` workflows from ComfyUI before major updates
- ComfyUI-Manager has backup feature in settings

### Troubleshooting Checklist

1. **"Frontend version outdated"** → Hard-refresh browser, check `/home/realityrove/comfyui-env/lib/python3.12/site-packages/comfyui_frontend_package/`
2. **"ModuleNotFoundError"** → Check NumPy version (should be <2.4), install missing deps
3. **"Address already in use"** → `kill $(pgrep -f 'main.py.*8188')`, check 5s, restart
4. **"GPU memory errors"** → Check `--reserve-vram`, reduce, or unload Ollama models
5. **"Nodes not loading"** → Check import times in startup log (`/home/realityrove/ComfyUI/comfyui_restart.log`)
6. **Process hangs with VRAM allocated but idle** → Old frontend version blocking, or model loading stuck. Restart ComfyUI and verify API responds.

### VRAM Management

- **Total VRAM:** 122 GB
- **ComfyUI reserve:** 40 GB (system reserves)
- **Ollama loads:** ~24 GB (qwen3.6:latest)
- **Available for ComfyUI:** ~58 GB when Ollama is loaded
- **Available if Ollama idle:** ~82 GB
- **For large video workflows:** Consider unloading Ollama temporarily: `ollama rm qwen3.6:latest`

---

## Common Workflows Reference

_TBD — Add links to important workflow configs, custom node setups as they become relevant._

---

## Hardware Reference

- **GPU:** NVIDIA GB10, 122 GB VRAM, AArch64 architecture
- **Storage:** 3.7 TB NVMe
- **RAM:** ~124 GB
- **Python:** 3.12.3 in venv at `/home/realityrove/comfyui-env`

---

## Key Files & Paths

- **ComfyUI dir:** `/home/realityrove/ComfyUI`
- **Venv python:** `/home/realityrove/comfyui-env/bin/python`
- **Venv pip:** `/home/realityrove/comfyui-env/bin/pip`
- **Frontend:** `/home/realityrove/comfyui-env/lib/python3.12/site-packages/comfyui_frontend_package/static`
- **Custom nodes:** `/home/realityrove/ComfyUI/custom_nodes/`
- **Models:** `/home/realityrove/ComfyUI/models/`
- **Output:** `/home/realityrove/ComfyUI/output/`
- **Logs:** `/home/realityrove/ComfyUI/comfyui_restart.log` (current)
- **Service file:** `/home/realityrove/comfyui.service.new`
- **Ollama config:** `/var/snap/ollama/common/env`

---

## Lessons Learned

1. **Frontend version mismatch breaks workflows silently** — Always verify `1.45.15+` after updating and hard-refresh browser
2. **NumPy 2.4+ breaks Numba-dependent nodes** — Pin `numpy<2.4` in venv requirements
3. **ComfyUI v0.25+ requires comfy-kitchen and comfy-aimdo** — Must be installed separately
4. **ComfyUI doesn't auto-save running jobs** — A crash means lost work; always save .json first for long jobs
5. **GB10 VRAM is huge but shared** — Set `--reserve-vram` and manage Ollama models to balance
6. **Ollama snap uses `snap set` not systemctl** — `sudo snap set ollama key=value` then `sudo snap restart ollama`
7. **ComfyUI API can be unresponsive for ~10s after startup** — Allow warmup time before checking
8. **Ollama models on disk don't use VRAM** — Only loaded models consume GPU; clean up unused ones for disk space
