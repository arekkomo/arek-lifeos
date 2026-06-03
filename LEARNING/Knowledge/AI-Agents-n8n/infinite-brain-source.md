---
title: "Don't Use Karpathy's Second Brain (I Built Something Better) — AI Impact"
category: source
summary: YouTube video comparing PARA-style second brain to an "Infinite Brain" knowledge graph architecture optimised for AI retrieval — atomic notes, 16 typed node types, and 10 edge types reduce token costs from ~9,000 to ~600 for the same query.
tags: [knowledge-graph, second-brain, obsidian, token-efficiency, ai-retrieval, vault-architecture]
sources: 1
updated: 2026-05-09
source_path: "raw/Don't Use Karpathy's Second Brain (I BUILT SOMETHING BETTER).md"
source_date: 2026-05
authors: [AI Impact, Andrew Warner, Mats Staffsberg]
ingested: 2026-05-09
---

# Don't Use Karpathy's Second Brain (I Built Something Better)

**Source:** [YouTube](https://www.youtube.com/watch?v=z02Y-1OvWSM) · AI Impact · May 2026

**Arek's note:** *"Interesting idea for knowledge base / second brain architecture. Specifically interested in token-efficient structure. Compare to our architecture and advise on solutions worth introducing."*

## TL;DR

PARA (Projects / Areas / Resources / Archives) was designed for humans, not AI. AI reads differently: it benefits from small, typed, richly-linked nodes rather than large monolithic documents. The "Infinite Brain" system restructures Obsidian knowledge graphs around how Claude actually parses and traverses information — achieving a ~15× token reduction for equivalent queries.

## The Core Problem with PARA for AI

- **Giant documents** — PARA encourages long notes per topic; AI has to read the whole thing
- **Untyped links** — `[[page]]` tells Claude nothing about *why* two things are linked
- **Loose metadata** — no consistent schema for AI to pre-filter relevance
- **Scope retrieval problem** — finding a specific decision buried in a long project note requires reading the whole note

## The Infinite Brain Architecture

### 1. Atomic Notes (50–300 lines max)
Each note covers one thing. If a topic needs more space, split into Part 1 / Part 2 with a typed link. Atomic size = ideal AI ingestion unit: enough context without wasted tokens.

### 2. 16 Node Types (vs. PARA's 4)
Instead of Projects / Areas / Resources / Archives:

| Type | Purpose |
|---|---|
| pillar | Core belief or principle |
| decision | A choice made, with rationale |
| concept | Idea or framework |
| question | Open question being explored |
| playbook | Repeatable process / SOP |
| task | Actionable item |
| event | Time-bound occurrence |
| pattern | Observed recurring behaviour |
| hypothesis | Testable claim |
| fact | Sourced data point |
| source | External reference |
| bookmark | URL/resource to revisit |
| note | Free-form capture |
| contact | Person |
| reference | Pointer to external system |
| custom | Anything else |

### 3. Typed Edges (10 types)
Instead of bare `[[wikilinks]]`, the nature of the relationship is encoded:

| Edge | Meaning |
|---|---|
| supports | This evidence/argument supports that claim |
| contradicts | This conflicts with that |
| depends_on | This requires that to be true |
| derived_from | This was created from that |
| related_to | Loose association |
| part_of | This is a component of that |
| preceded_by | This comes after that (sequence) |
| followed_by | This comes before that |
| authored | Who created this |
| tag | Flexible catch-all |

### 4. One-Line Summaries on Every Node
The AI reads the summary first (50 tokens) and decides whether to expand. Equivalent to the `summary:` field in our YAML frontmatter — we already do this.

## Token Efficiency Claim
Same question posed to both systems:
- PARA-style knowledge graph: **~9,000 tokens**
- Infinite Brain: **~600 tokens**

Reason: atomic notes + typed edges let Claude navigate directly to the relevant node without reading surrounding noise.

## Relevance to Arek & Co

Our architecture already does several things right (see [[knowledge-graph-architecture]] for full comparison). The highest-leverage improvements to introduce:
1. **Typed edges** — annotate wikilinks with relationship type
2. **Two new node types** — `decision` and `playbook` in LEARNING/
3. **Atomic note enforcement** — keep Knowledge/ pages under ~300 lines; split if over

**Sources:** this file
**Related:** [[knowledge-graph-architecture]], [[cli-for-agents]]
