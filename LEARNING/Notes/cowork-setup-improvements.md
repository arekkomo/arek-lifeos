---
title: Cowork Setup Improvements — Research Findings
category: note
summary: Consolidated recommendations for improving the Arek&Co Cowork setup, drawn from two expert setup guides (Nick Milo, Simon BetterCreating). Gaps identified against current setup.
tags: [cowork, setup, improvements, about-me, writing-rules, context-map]
updated: 2026-05-09
---

# Cowork Setup Improvements

*Synthesised from [[cowork-setup-nick-milo-source]] and [[cowork-setup-simon-source]]*

## Current Setup Strengths

Arek's setup is already ahead of most users:
- ✅ Vault-wide CLAUDE.md with full schema and routing rules
- ✅ ABOUT-YOU/ folder (General, Creative, Finance, Health, Working-Patterns)
- ✅ 8 agents with domain briefs
- ✅ Gmail, Calendar, Notion, Claude in Chrome all connected
- ✅ Full skills library
- ✅ Auto-memory system
- ✅ Scheduled tasks running

## Identified Gaps (Prioritised)

### 1. Writing Rules File ⭐ High Priority
**What:** A dedicated `ABOUT-YOU/Writing-Rules.md` that defines Arek's voice, tone, and explicit anti-AI writing guidelines.
**Why:** Without it, any written output (journal entries, drafts, emails) defaults to generic AI tone. Both guides emphasise this as one of the highest-leverage files to create.
**What to include:**
- Tone: concise, direct, no filler phrases, no preamble
- Voice: first-person, conversational but purposeful
- Anti-AI rules: ban "certainly", "absolutely", "I'd be happy to", "it's worth noting", "dive into", etc.
- Spelling preference (British? American?)
- When to use bullet points vs prose
**Action:** Create `ABOUT-YOU/Writing-Rules.md` — tracked in Milestones.

### 2. Notion Context Map ⭐ High Priority
**What:** A file that maps Arek's Notion workspace structure so Claude can navigate it without burning tokens exploring from scratch.
**Why:** When Claude has to discover Notion's structure mid-task, it reads many pages unnecessarily. A pre-built map = direct navigation.
**How to create:** Ask Claude to search the Notion MCP and build a context map of all databases and their purposes. Save as `ABOUT-YOU/Notion-Context-Map.md`.
**Action:** Create the map — tracked in Milestones.

### 3. Maps of Content for Scholar ⭐ Medium Priority
**What:** High-level index MOCs for the main LEARNING/ clusters (AI Agents, Filmmaking, etc.).
**Why:** Gives Claude a fast entry point into each knowledge cluster without reading all pages. Reduces token cost on Scholar queries.
**How:** Ask Claude to read each Knowledge/ subfolder and create a MOC linking key pages with one-line summaries.
**Action:** Create MOCs for AI-Agents/ and Filmmaking/ first — tracked in Milestones.

### 4. Per-Project Memory Files ⭐ Medium Priority
**What:** A `memory.md` or `CLAUDE.md` inside each active PROJECTS/ subfolder.
**Why:** Project-specific context that persists across sessions without polluting the vault-wide CLAUDE.md. Especially useful for CHS and RealityRowHub.
**Action:** Add to active projects — tracked in Milestones.

### 5. Auto-Generate About Me Dossier 🔲 Low Priority
**What:** Have Claude read the vault and generate a richer dossier for About-Me-General.md.
**Why:** Nick Milo's approach surfaces subconscious priorities from your actual notes — richer than what you'd write manually.
**How:** Ask Claude to read ABOUT-YOU/, DAILY/, LEARNING/Notes/ and synthesise an intellectual dossier. Review and merge into existing files.
**Action:** Run once when time permits — not urgent given existing files are solid.

## Not Worth Adding (Now)

- **Paperclip** — Multi-agent orchestration. No clear gain for current OS. Revisit for RealityRowHub.
- **Mobile Dispatch** — Requires always-on desktop. Revisit if Arek gets a dedicated home machine.
- **Custom plugin builder** — Simon's specialist sub-agent builder. Potentially useful later for Director/Scholar plugins. Not urgent.
