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

2026-08-02 | Director | creative-project-dashboard | Build a local, browser-accessible Creative Dashboard for Arek. It should read the Obsidian vault source of truth at `/home/realityrove/Obsidian/Arek&Co/CREATIVE/` and present: (1) all creative projects grouped by domain with status, stage, last-active date, concise next action, and a link/path to source files; (2) Creative Library items grouped by the five existing categories, with tags/source; (3) clear separation of active, paused/waiting, completed/archived, and unclassified projects; (4) a lightweight refresh mechanism that reflects catalog/library changes without manual data re-entry. Do not treat Notion as source of truth; it is currently inaccessible to the Director integration, so use the vault. Deliver a local URL and run instructions, with a clean single-page UI optimized for a fast creative overview. | Priority: HIGH

2026-08-02 | Director | notion-access-and-creative-sync | Repair Director’s Notion access and then create a safe Notion → Obsidian creative-data sync. The Director Notion MCP integration returns `object_not_found` for dtb Writing (ID `175b4695a24d806981f3e5dcac3348d6`) even though a Notion token is available in the Hermes `.env`; verify the MCP configuration uses the correct credential and the database is explicitly shared with the integration (database-level connection, not merely page sharing). **Diagnostic evidence:** an authenticated probe using the token currently stored as `MCP_NOTION_API_KEY` returned HTTP 401 from both `/v1/users/me` and the legacy database retrieval endpoint. Treat the configured token as invalid/revoked/malformed first; replace it with a valid integration secret, update the Director MCP configuration, then share dtb Writing at database level with that exact integration. Do not expose tokens in logs or messages. Once access is verified with a real database read/query, import/sync all dtb Writing creative entries into `/home/realityrove/Obsidian/Arek&Co/CREATIVE/` with a deterministic, idempotent mapping that preserves Notion page IDs, metadata, body content, and last-edited time. Obsidian must remain the human-facing source of truth; avoid overwriting existing project files and produce a reconciliation report for duplicates/conflicts/unclassified records. Deliver verification evidence, run instructions, and the resulting sync report. | Priority: HIGH

