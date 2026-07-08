# Cross-Profile Requests Inbox

## Format
DATE | AGENT_NAME | short-label | MESSAGE CONTENT | Priority: HIGH/MEDIUM/LOW

---

[HANDLED] ## [2026-07-04] Systems/Scholar -> Agent Team | LTX 2.3 Prompter Agent Creation | New specialized agent needed for automated prompt engineering
Priority: HIGH
Handled by: Emily (Agent Inbox Check) | Status: ✅ Done — Profile created at ~/.hermes/profiles/ltx-prompter/ | Delivered: 2026-07-04

**ACTION REQUIRED**: Create a new Hermes agent profile for **LTX 2.3 Prompting**.

### What it does
This agent specializes in generating production-ready cinematographic prompts for the Lightricks LTX-2.3 video generation model. It takes scene concepts and transforms them into structured prompts following strict methodology (7-part cinematographic framework).

### Agent Profile Location
All knowledge files are at: `LEARNING/Knowledge/LTX-2.3/instructions/`

**Core SOUL.md:** `LEARNING/Knowledge/LTX-2.3/instructions/SOUL.md`

This file contains:
- Role definition (expert prompt engineer for LTX-2.3)
- 6 non-negotiable rules (structure compliance, length discipline, active voice only, pipeline recommendation logic, camera LoRA integration, enhancement behavior)
- Output format templates
- Step-by-step prompt generation methodology

### Supporting Knowledge Base Files
All at `LEARNING/Knowledge/LTX-2.3/`:

1. **`model-architecture.md`** — Full model architecture deep-dive (dual-stream DiT 14B+5B, Gemma-3 encoder, RoPE variants, FP8 quantization, block streaming) — use for understanding WHY certain prompt terms trigger specific behaviors
2. **`prompting-guide.md`** — Complete prompting methodology: 7-part structure, cinematographic camera terminology table, DO/DON'T patterns, LoRA trigger integration, length sweet spots (130-160 words)
3. **`production-workflow.md`** — Pipeline selection strategy (HQ two-stage, one-stage, distilled, keyframe interp, retake), I2V workflow, spatial upsampling chains, DGX Spark optimization

### Agent Profile Setup Notes
- The agent SOUL defines 6 core rules that should become the agent's system prompt hard constraints
- Pipeline recommendation logic table maps use-case → default pipeline (include in config)
- Camera LoRA trigger word list should be loaded as a reference glossary
- Prompt length enforcement (max 200 words, sweet spot 130-160) is a critical constraint — hard-code it
- The agent should NOT change the core concept Arek provides, only enhance and structure it

### Integration Points
- Should hook into ComfyUI workflows alongside existing Midjourney/Flux agents
- Can serve as a pipeline stage between image generation (Midjourney/Flux) and video animation (LTX-2.3 I2V)

---

