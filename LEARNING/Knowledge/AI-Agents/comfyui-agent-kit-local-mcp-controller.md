---
title: "ComfyUI-Agent-Kit — Local Multi-Agent ComfyUI Controller with OCIO/ACES"
category: entity
summary: "Local-first MCP driver that installs ComfyUI, registers skills for Claude Code/Codex/Gemini/Qwen Code agents, and provides per-model prompting recipes, hardware-aware model selection, ACES color management nodes, and 545 workflow templates."
tags: [comfyui, ai-agents, mcp, claude-code, codex, ocio, acs-color, aces, acses, node-building, multi-agent]
sources: 1
updated: 2026-07-06
---

## About

ComfyUI-Agent-Kit is a **local-first, multi-agent integration** for ComfyUI. Unlike cloud-based alternatives, it runs entirely on hardware you control — no hosted service, no per-generation billing. A single installer wires the same MCP driver stack into Claude Code, Codex CLI, Gemini CLI (via GLM note), and Qwen Code, enabling each coding agent to generate images, video, audio, and 3D content through ComfyUI.

By **AI VFX NEWS**. MIT license. Cross-platform (Windows PowerShell + Linux/macOS bash installers).

## Architecture (Four-Layer Stack)

The kit decomposes into a modular stack that the installer wires once at setup:

1. **Knowledge + Client** — The agent's skill/extension directory provides operating manuals and a zero-dependency HTTP client for ComfyUI's REST API
2. **MCP Driver (~90 tools)** — `comfyui-mcp` npm package gives structured operations: generate, build/edit graphs, validate, queue management, model download, VRAM tracking, diagnostics
3. **In-Graph LLM Nodes** — An `Anthropic Claude` or similar custom node steps inside a workflow for prompt enrichment and visual QA without the agent in the loop
4. **Node-Building Skills** — Agent can write/modify custom ComfyUI Python nodes (V3 API), bridging workflow design with extension authoring

## Key Features

### Per-Model "Mega-Brain"
69 distilled prompt recipes across image, video, audio, and 3D modalities. Recipes sourced from official model documentation — each modality's ideal prompting style is distinct:
- **SDXL**: command tags (single-line, structured)
- **FLUX**: natural-language paragraphs with detail
- **Video models**: camera motion + direction cues as primary conditioning

When you name a model, the agent reads that model's entry first and prompts it in its dialect.

Model coverage: FLUX.1/.2/Kontext, Z-Image, Qwen-Image/Edit, SDXL/SD 1.5/3.5, HiDream, Ideogram 2/3, Nano Banana Pro, Seedream, Recraft, GPT-Image, Grok, Reve, Kandinsky, BRIA, OmniGen, Chroma, Krea, ERNIE-Image, FireRed/LongCat image edit, Wan 2.1-2.7, LTX-2.3/Pro, Hunyuan Video, SVD, Kling, Veo, Sora, Sedance, Luna Ray + Runway Gen-4.5, MiniMax/Hailuo, Pika, Vidu, HappyHorser, HuMo, SCAIL-2, Stable Audio, ACE-Step, ElvenLabs/ChataterBox, SoniIO, Hunyuan3D, Tripo/Rodin/Meshy, plus 18 enhancement/utilities (Real-ESRGAN, SUPIR, SeedVR2, FILM, RIFE, SAM3, BiRefNet, Depth Anything).

### Hardware-Aware Model Selection
Detects system VRAM, RAM, and available disk space. Recommends a variant that fits — FP8 vs. offload vs. multi-GPU vs. quantized — and refuses downloads that won't fit before wasting bandwidth.

### OCIO/ACES Custom Nodes (ComfyUI-OCIO)
Eight Nuke-style OpenColorIO nodes — the author's own company work, shipped as part of this kit:

1. **Read a still** (image load with color space awareness)
2. **Sequence reader** (video frames with ACES management)
3. **Grade in ACES** (apply color transforms within an OCIO config)
4. **Write ProRes/EXR** (fully color-managed output to either codec)

Plus the field-tested guide to building a custom node pack from scratch, showing dependency wiring, registration patterns, and I/O contract design. See [[ComfyUI]] for context on node architecture.

### Template Library (545 workflows + 94 Blueprints)
Clones the official `Comfy-Org/workflow_templates` repo at install time, building a compact lookup index so any natural-language request maps to the correct template. Categories:
- 139 image templates
- 136 video templates
- 107 use-case templates
- 67 utility templates
- 33 3D templates
- 29 audio templates

### Persistence & GUI Bridge
Writes graphs directly into `<ComfyUI>/user/default/workflows/`, visible in the Workflows sidebar. No "agent panel" node required — graphs appear as native ComfyUI workflows you can reopen and iterate on later.

## Use Cases for VFX / Filmmaking Workflow

- **Rapid shot iteration without cloud dependency**: Local GPU, zero per-frame cost beyond electricity
- **ACES color pipeline prep**: OCIO nodes produce properly-managed EXR for downstream Nuke or [[DaVinci Resolve]] integration
- **Agent-driven batch production**: Multiple coding agents can queue different generative tasks (e.g., one for background plates, another for character renders) through the same ComfyUI instance
- **Template-based reproducibility**: 545 official templates + per-model prompting recipes reduce trial-and-error time

## Installation

### Claude Code (one-liner via marketplace plugin)
```bash
/plugin marketplace add SlavaSexton/ComfyUI-Agent-Kit
/plugin install comfyui@comfyui-agent-kit
```

### Multi-agent installer (all agents at once)
```bash
git clone https://github.com/SlavaSexton/ComfyUI-Agent-Kit.git
cd ComfyUI-Agent-Kit
# Linux/macOS:
./install.sh --comfyui-path /path/to/ComfyUI
# Windows:
.\install.ps1 -ComfyUIPath "E:\path\to\ComfyUI"
```

The installer auto-detects which of `claude`/`codex`/`gemini`/`qwen` are on PATH, writes appropriate config per agent, and runs a bootstrapping health check (GPU detection, model registry, network status).

## How It Differs from comfyui-mcp-panel
The existing [[ComfyUI MCP Agent Panel]] embeds an LLM directly in ComfyUI's sidebar for canvas editing. ComfyUI-Agent-Kit is the inverse: external coding agents (Claude Code etc.) control a full ComfyUI instance via MCP, with far broader scope — model management, workflow assembly, color pipeline nodes, template library, and multi-agent orchestration.

## References

- [[ComfyUI]] — Node-based diffusion interface
- [[AI Video Generation]] — Diffusion models for video
- GitHub: https://github.com/SlavaSexton/ComfyUI-Agent-Kit
- comfyui-mcp base (MCP driver): https://github.com/artokun/comfyui-mcp
- ComfyUI-OCIO: https://github.com/SlavaSexton/ComfyUI-OCIO
