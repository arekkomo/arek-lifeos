---
name: memory-layering
domain: life-os
version: 1.1
description: Multi-agent memory architecture using Hot/Warm/Cold layers, Karpathy LLM Wiki pattern, recurring theme promotion, and Obsidian graph query via MCP.
---

# Memory Layering for Multi-Agent Systems

> **Core principle:** Never load everything into context. Use an index → reference pattern to load relevant memory only when needed. Keep main instruction files under 200 lines to prevent "context rot" (model's inability to recall information accurately when context window is flooded).

## The Three Layers

### 🔥 Layer 1: Hot Memory (Ephemeral)
**What:** Real-time chat logs (Telegram, Discord). Session context.
**Retention:** Transient. No persistence unless it leads to a decision or new idea.
**Trigger:** User messages. Agent responds from memory + Warm layer.

### 🌡️ Layer 2: Warm Memory (Session-Scoped)
**What:** Active plans, daily briefs, current goals, shared_sync logs.
**Retention:** Short-to-medium term. Relevant for the current sprint/month.
**Files:** `DAILY/`, `AGENTS/`, `shared_sync.md`
**Refresh:** New content daily. Stale content pruned by "dreaming" cron (see below).

### 🧊 Layer 3: Cold Memory (Permanent)
**What:** Deep knowledge, research, high-level synthesis, cross-domain analysis.
**Retention:** Permanent. Indexed and searchable.
**Files:** `LEARNING/Knowledge/*`, `LEARNING/Synthesis/*`, `PROJECTS/*`, `ABOUT-YOU/`
**Authority:** Root INDEX.md managed by CEO agent (Alfred). Sub-indexes managed by field agents.

---

## The Karpathy LLM Wiki Pattern (Level 5)

From Andre Karpathy's pattern — adopted because `raw/` + `wiki/` maps exactly to our vault:

```
raw/              → IMMUTABLE sources. Read only. Never write.
LEARNING/Knowledge/ → LLM-owned knowledge base. Full structure control.
```

- `raw/` holds source documents (articles, transcripts, PDFs, research). Always preserved for audit trail.
- `LEARNING/Knowledge/` is structured by discipline, maintained by the AI, with YAML frontmatter on every page.
- New discipline = new subfolder in `Knowledge/`.
- No file is dumped at top level. Every page ties into the index.

---

## The "Dreaming" Cron Pattern

A nightly cron job that maintains memory hygiene:

1. **Scan** `DAILY/` entries for the past 7–14 days.
2. **Score** topics by frequency and significance. Recurring themes score higher.
3. **Promote** recurring/pattern themes into long-term memory:
   - `ABOUT-YOU/*` for personal facts/preferences discovered through repetition
   - `LEARNING/Synthesis/*` for cross-domain patterns
   - `INDEX.md` updates
4. **Archive** daily entries to `raw/archive/` (no deletion — they're an audit trail).
5. **Report** what changed.

**Why this matters:** Without automated pruning, the system becomes a dump truck. Context windows fill with stale daily notes and the agent's ability to recall relevant facts degrades. The dreaming cron is the system's immune response to entropy.

---

## File Write Scoping (Per Agent)

| Agent | Writes To |
|-------|------|
| **Emily (Field)** | `LEARNING/Knowledge/*`, `DAILY/*`, `AGENTS/emily/*`, `shared_sync.md` |
| **Alfred (CEO)** | `PROJECTS/*`, `LEARNING/Synthesis/*`, `CREATIVE/*`, `AGENTS/alfred/*`, `INDEX.md` (root authority) |
| **Both (Read-only)** | `ABOUT-YOU/*`, `INDEX.md` (read), `DASHBOARD.md` (read) |

---

## When to Add More Layers

- Add Level 4 (verbatim RAG like Mem Palace) when you catch yourself saying "I know we discussed this weeks ago but I can't remember exactly what was said."
- Add Level 6 (cross-tool external DB like OpenBrain/Mem0) when you need the same memories in ChatGPT + Claude Code + Cursor simultaneously.
- For now, Layers 1–3 cover this user's setup. Level 5 (LLM Wiki pattern) is already baked in.

---

## Graph Query Layer (Obsidian MCP)

Our Hot/Warm/Cold architecture is functional but lacks a critical gap: **the agent cannot query the vault's knowledge graph**. It can read/write files as plain text, but cannot:
- Traverse linked notes (double-bracket wiki links)
- Query cross-references across `LEARNING/`, `PROJECTS/`, `ABOUT-YOU/`
- Do bidirectional sync (changes in either direction propagate instantly)

**The fix:** Install and configure an Obsidian MCP server in `~/.hermes/config.yaml` under `mcp_servers`. Once connected, the agent gains tools like `mcp_graphthulhu_get_page`, `mcp_graphthulhu_get_links`, `mcp_graphthulhu_traverse`, and `mcp_graphthulhu_find_connections` that let it navigate the vault as a graph, not just a flat filesystem.

**Selection:** graphthulhu (Go binary, `skridlevsky/graphthulhu`) — chosen for graph traversal (BFS), backlink queries, knowledge-gap detection, and topic clustering. No Obsidian app required (reads vault files directly).

**Setup checklist:**
1. `go install github.com/skridlevsky/graphthulhu@latest` (or download binary from releases)
2. Add to `~/.hermes/config.yaml` (see `templates/obsidian-mcp-config.yaml` for ready-to-paste block)
3. Restart Hermes to discover MCP tools

**Key tools you'll get:**
- `get_page` — full recursive block tree with parsed links, tags, properties
- `get_links` — forward/backward links with containing blocks
- `traverse` — BFS path-finding between any two pages through the link graph
- `find_connections` — direct links, shortest paths, shared connections between pages
- `knowledge_gaps` — orphan pages, dead ends, weakly-linked areas
- `topic_clusters` — connected components with hub identification
- `search` — full-text search with parent chain + sibling context
- `link_pages` — bidirectional linking (keeps Obsidian's [[wikilinks]] in sync)

**See also:** `references/obsidian-mcp-evaluation.md` for the full comparison of 5 candidates.

## Evaluating New Architecture Ideas

When evaluating a new technique, pattern, or tool against our existing system, use this comparison workflow:

1. **Map what we already have** — search the existing skills, config, and vault structure for equivalent functionality. Don't assume something is new just because it's described as new.
2. **Identify the actual delta** — list each new capability the proposed system provides that we DON'T already have.
3. **Determine implementation cost** — is this a config change (MCP server), a vault restructuring, a new cron job, or a fundamentally new system?
4. **Recommend with specificity** — "This would improve X because we currently lack Y" is more useful than "This is good."

**Pitfall:** Don't implement a "new" feature that already exists under a different name (e.g., our Hot/Warm/Cold layering was described in a video as novel, but we already had it).

## Pitfalls

- **Don't dump `raw/` content into `Knowledge/` directly.** Always process — create entity pages, cross-references, and update the index. Minimum 5 files per ingest.
- **Keep instruction files under 200 lines.** If it's bigger, split into referenced sub-files.
- **Never use the same path for two agents' writes.** Always enforce scoping or accept merge conflicts via branches.
- **Daily entries are not knowledge.** They are working memory. Promote recurring themes; don't leave noise.

## Legacy Layer-Memory Summary

The older `layer-memory` skill is absorbed here as the class-level Hot/Warm/Cold memory umbrella. Its full text and Life OS note are preserved at:

- `references/layer-memory.md`
- `references/layer-memory-life-os.md`

Use the older summary when you need the quick conceptual diagram; use this skill's main body for operational rules, promotion cadence, Obsidian/MCP evaluation, and multi-agent scoping.
