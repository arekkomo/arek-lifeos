---
title: Claude Code Skill Patterns
category: concept
summary: Taxonomy of reusable Claude Code skill archetypes — session management, quality control, context engineering, and output exploration.
tags: [claude-code, skills, agentic-workflows, patterns, productivity]
sources: 2
updated: 2026-05-14
---

# Claude Code Skill Patterns

A taxonomy of the most valuable [[claude-code]] skill archetypes, synthesized from practitioner experience. Skills cluster into four functional categories.

---

## Category 1 — Session Management

Skills that structure how a session starts, runs, and carries knowledge forward.

| Skill | Function | Source |
|---|---|---|
| **calibrate** | Self-improvement at session end; scans conversation and updates skills/settings/memory | Jay, RoboNuggets |
| **coordinate** | Shared project folder (context.md + session log) for multi-session continuity | Jay, RoboNuggets |
| **onboard** | Loads existing project context into a new or forked session | Jay, RoboNuggets |
| **claude-mem** | Cross-session memory via SQLite + vector search; auto-updates CLAUDE.md files | Nate Herk |

**Pattern:** Context drift is the default enemy. These skills prevent it by externalizing memory and project state beyond any single conversation.

---

## Category 2 — Quality Control

Skills that force structured thinking before and after execution.

| Skill | Function | Source |
|---|---|---|
| **superpowers** | Plan → isolated env → test → 2-stage review; senior dev discipline | Nate Herk |
| **GSD** | Fresh sub-agent per task; prevents context rot; built-in quality gates | Nate Herk |
| **/review** | Local, fast structured code review (built-in to CC 2.1.86+) | Built-in |
| **/ultra-review** | Cloud, parallel reviewer agents; only confirmed bugs surface ($5–20/run) | Built-in |
| **devil** | Forces contrarian critique; counters LLM sycophancy | Jay, RoboNuggets |
| **align** | Clarifying questions before execution; narrows output scope | Jay, RoboNuggets |

**Pattern:** Claude's default mode is to comply and sprint. Quality control skills add friction at the right points — upfront (align, superpowers) and post-execution (review, devil).

---

## Category 3 — Context Engineering

Skills that manage what enters and stays in the context window.

| Skill | Function | Source |
|---|---|---|
| **context-mode** | Compresses tool output (315KB → 5KB); tracks session events in SQLite; rebuilds context post-compaction | mksglu (community) |
| **GSD** | Sub-agents with clean context windows prevent long-session degradation | Nate Herk |

**Context Rot:** Predictable degradation pattern — ~halfway through a long session, Claude forgets requirements, skips steps, and declares work done prematurely. Context Mode and GSD are the primary mitigations.

**Compression benchmark (context-mode):** 56KB Playwright snapshot → 299 bytes; 46KB access log → 155 bytes.

---

## Category 4 — Output Exploration

Skills that force variation and creative breadth.

| Skill | Function | Source |
|---|---|---|
| **burst** | Generates N simultaneous variations; chains for finer iteration | Jay, RoboNuggets |
| **tweak** | HTML sliders for design parameter adjustment; "bake" outputs a CSS patch | Jay, RoboNuggets |
| **skill-creator** | Builds, tests, and packages new skills from plain English (✅ installed) | Anthropic official |

**Agent Steering Model:** The agent is a search process; a prompt is a direction vector. `align` narrows direction; `burst` simultaneously explores multiple vectors — faster convergence to the desired output.

---

## Install Status for Arek & Co.

| Category | Skill | Status |
|---|---|---|
| Session Mgmt | calibrate | ❌ Not installed |
| Session Mgmt | coordinate | ❌ Not installed |
| Session Mgmt | onboard | ❌ Not installed |
| Session Mgmt | claude-mem | ❌ Not installed |
| Quality | superpowers | ❌ Not installed |
| Quality | GSD | ❌ Not installed |
| Quality | /review | ✅ Built-in |
| Quality | /ultra-review | ✅ Built-in |
| Quality | devil | ❌ Not installed |
| Quality | align | ❌ Not installed |
| Context | context-mode | ❌ Not installed |
| Exploration | burst | ❌ Not installed |
| Exploration | tweak | ❌ Not installed |
| Exploration | skill-creator | ✅ Installed |

**Recommended priority for Arek & Co.:**
1. **calibrate** — highest value; aligns all agents with Arek's preferences over time
2. **context-mode** — long Cowork sessions will benefit immediately from compression
3. **superpowers** — any coding/automation work (n8n, agents, web) benefits from plan-first discipline
4. **align** — reduces wasted tokens on misaligned creative and strategy sessions
5. **claude-mem** — evaluate overlap with existing manual memory system before installing

---

## Related Pages

- [[claude-code]] — entity page with full capability overview
- [[claude-code-skills-daily-7-source]] — RoboNuggets: calibrate, coordinate, onboard, align, devil, burst, tweak
- [[claude-code-skills-best-6-source]] — Nate Herk: skill-creator, superpowers, GSD, /review, context-mode, claude-mem
- [[skill-self-improvement-loop]] — autonomous eval-driven skill refinement
- [[autonomous-ai-assistant]] — Cloudbot pattern using Claude Code
