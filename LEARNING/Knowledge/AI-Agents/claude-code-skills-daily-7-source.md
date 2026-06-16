---
title: "7 Claude Code Skills I Use Every Single Day (RoboNuggets)"
category: source
summary: Advanced tutorial covering 7 agentic skills for Claude Code — calibrate, coordinate, onboard, align, devil, burst, and tweak.
tags: [claude-code, skills, agentic-workflows, productivity, multi-session]
sources: 1
source_path: raw/7 Claude Code skills I use every single day (Advanced Tutorial).md
source_date: 2026-05
authors: [Jay (RoboNuggets)]
ingested: 2026-05-14
updated: 2026-05-14
---

# Source: 7 Claude Code Skills I Use Every Single Day

**Original:** https://www.youtube.com/watch?v=UpgjdQJShWg  
**Channel:** RoboNuggets (Jay)  
**Published:** 2026-05-12

> **Arek's Comment:** "this could be interesting for my claude code. could you check if i already have those skills in my claude code and if note can we implement some of them if they are useful?"
> ⚠️ **Action Required:** Arek wants these skills reviewed against his current setup and useful ones implemented. This requires a live session — flagged for follow-up.

---

## TL;DR

Seven reusable skills that Jay runs on Claude Code daily inside an AI education/consulting business. The core theme: skills that make agents smarter over time, enable multi-session coordination, and improve output quality through structured prompting patterns.

---

## The 7 Skills

### 1. Calibrate
**Purpose:** Self-improvement loop at session end.  
- Invoke `/calibrate` at the end of any session
- Agent scans the conversation, detects corrections, preferences, repeated patterns
- Suggests numbered updates to skills, settings, and memory files
- Accepts `calibrate light` for a quick sweep when context is low
- Pattern: accept all suggestions, let continuous calibration polish the agent over time

**Why it matters:** Agents gradually learn your preferences rather than starting fresh every session. Eliminates repeated corrections.

### 2. Coordinate
**Purpose:** Shared project context for multi-session work.  
- Creates a shared project folder with `context.md` + `session_log.md`
- Any Claude Code session can be onboarded to the same project without re-explaining context
- Supports `coordinate light` for smaller, personal research tasks
- Can be used for non-work projects (research, personal errands)

**Why it matters:** Enables true parallel work across sessions — multiple agents on the same project without context drift.

### 3. Onboard (Context Bridge)
**Purpose:** Brings a new session up to speed on an existing project.  
- Invoke the skill, give it a project name; it reads context.md + session logs from the shared folder
- Works via Telegram integration too (mobile pickup of Claude Code projects)
- Advanced: fork a conversation mid-session to spawn a parallel agent already onboarded

**Why it matters:** Removes the cost of re-briefing every new session. Supports long-running projects across days.

### 4. Align
**Purpose:** Forces upfront clarification before work begins.  
- Invoke `/align <N>` to receive N numbered clarifying questions, each with lettered options
- Keeps the scope of possible outputs narrow from the start
- Combine with voice dictation (Aqua app) for fast Q&A input

**Why it matters:** Misaligned prompts waste tokens and produce wrong outputs. Align front-loads intent specification before execution.

### 5. Devil (Devil's Advocate)
**Purpose:** Counters LLM sycophancy.  
- Forces Claude to generate a contrarian critique of whatever option/approach was just chosen
- Takes a number parameter (depth of feedback)
- Surfaces overlooked risks, alternative approaches, and weak assumptions

**Why it matters:** LLMs default to agreeing with the user. Devil breaks this pattern and exposes blind spots.

### 6. Burst
**Purpose:** Generates N simultaneous variations.  
- `/burst <N>` forces the agent to produce N distinct variations of the current output
- Applicable to writing, images, code, HTML slides, UI designs
- Can chain: burst → select → burst again at finer granularity
- Mathematically: searching multiple vectors simultaneously gets to target faster

**Why it matters:** Parallel exploration narrows the gap to the desired output faster than sequential attempts.

### 7. Tweak (Design Parameter Sliders)
**Purpose:** Visual fine-tuning of HTML/design outputs.  
- Inserts an HTML slider UI into the output for adjusting design parameters (font size, density, saturation, letter spacing, accent glow)
- Claude auto-selects relevant sliders based on context; user can specify custom ones
- "Bake" button outputs a CSS patch that locks the choices into the final design

**Why it matters:** Design iteration without code — replaces guessing prompt parameters with direct visual control.

---

## Key Frameworks

**Agent Steering Model:** Agent = search process; your prompt = direction vector. More specific direction = narrower search space = faster output convergence. `align` narrows direction, `burst` explores multiple vectors simultaneously.

**Multi-Session Architecture:** Shared Projects folder → coordinate + onboard + fork = true parallel agent orchestration on one project.

---

## Relevance to Arek & Co.

- **Calibrate** — high value for all Arek & Co. agents; would auto-refine skill files over time
- **Coordinate** — relevant for RealityRowHub, Director, and any multi-session creative projects
- **Align** — useful for Director and Strategist sessions where scope creep is a risk
- **Devil** — useful for Strategist and Accountant to stress-test decisions
- **Burst** — high value for Director (script variations, shot options) and creative work
- **Tweak** — lower priority; useful if building web artifacts or HTML outputs

## Related Pages
- [[claude-code]] — main entity page
- [[claude-code-skill-patterns]] — patterns and taxonomy across all skill tutorials
- [[skill-self-improvement-loop]] — Karpathy eval loop (related self-improvement concept)
- [[claude-code-skills-best-6-source]] — companion tutorial from Nate Herk
