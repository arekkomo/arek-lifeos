---
title: Knowledge Graph Architecture for AI
category: concept
summary: Design principles for structuring a personal knowledge base to be token-efficient and AI-retrievable — atomic notes, typed nodes, and typed edges versus the human-centric PARA method.
tags: [knowledge-graph, vault-architecture, token-efficiency, obsidian, second-brain, ai-retrieval]
sources: 1
updated: 2026-05-09
---

# Knowledge Graph Architecture for AI

## The Core Insight

Knowledge bases built for humans (PARA, Building a Second Brain) optimise for human navigation: four broad folders, long documents, loose links. AI reads differently — it benefits from small, well-typed, richly-linked nodes that let it skip irrelevant content without burning tokens on it.

**The benchmark:** Same query against a PARA-style vault vs. an AI-optimised vault → ~9,000 tokens vs. ~600 tokens. (~15× reduction.)

## Two Architectures Compared

| Dimension | PARA / Human-First | Infinite Brain / AI-First |
|---|---|---|
| Folder structure | 4 (Projects, Areas, Resources, Archives) | 16 typed node categories |
| Note size | Unrestricted (often large) | Atomic: 50–300 lines max |
| Links | Bare `[[wikilinks]]` | Typed edges (10 relationship types) |
| Metadata | Loose / inconsistent | Structured frontmatter on every node |
| AI retrieval | Must read full docs to find data | Navigate by type + summary |

## The Three Levers

### 1. Atomic Notes
Cap pages at ~300 lines. If a topic needs more, split into Part 1 / Part 2 with a typed link. Result: Claude ingests one complete idea per read, not a sprawling document with buried relevant detail.

### 2. Typed Nodes
Classify every note by what it *is*, not just what topic it's about. A `decision` (choice made + rationale) is structurally different from a `concept` (idea to understand) or a `playbook` (repeatable process). Typed nodes let Claude pre-filter by type before reading content.

### 3. Typed Edges
Annotate wikilinks with the nature of the relationship:
- `[[Kling AI]] — contradicts` (vs Runway's approach)
- `[[n8n]] — depends_on` (for a workflow to work)
- `[[Printing Press]] — derived_from` (CLI-layer decision)

Result: Claude can traverse the graph intelligently — following only relevant relationship types for the query at hand — instead of reading everything connected.

## How Arek & Co Compares

**Already strong:**
- `summary:` frontmatter field — Claude reads this before deciding to expand (equivalent to one-line summaries in Infinite Brain)
- Topic-based folder structure — scoped retrieval by discipline
- Agent-based routing — right agent reads right files only
- `category:` frontmatter (entity / concept / source / synthesis / note) — partial node typing

**Gaps to close:**
1. **Typed edges** — wikilinks are currently bare; annotating relationship types is high-leverage, low-effort
2. **Missing node types** — `decision` and `playbook` are genuinely absent and useful
3. **Note length** — no enforced size limit on Knowledge/ pages; some pages will benefit from splitting

**Not worth adopting:**
- All 16 node types — overkill for a personal single-operator vault; 5 existing + 2 new = sufficient
- Full restructure — existing architecture is already better than PARA for AI retrieval

## Implementation in This Vault

See [[PROJECTS/Arek-Co-OS/Milestones]] for the tracked tasks:
- Add typed edge annotations to wikilinks (Phase 4)
- Introduce `decision` and `playbook` to page `category:` frontmatter (Phase 4)
- Enforce ~300-line cap on Knowledge/ pages (Phase 4)

**Sources:** [[infinite-brain-source]]
**Related:** [[cli-for-agents]], [[claude-code]], [[n8n]]
