---
title: "Build Self-Improving Claude Code Skills (Karpathy Loop)"
category: source
summary: Tutorial applying Andrej Karpathy's autoresearch loop to Claude Code skills — binary assertion eval files + autonomous loop that tests, scores, and refines skill.md overnight.
tags: [claude-code, skills, self-improvement, evaluation, binary-assertions, karpathy, arek-and-co]
sources: 1
source_path: raw/Build Self-Improving Claude Code Skills. The Results Are Crazy..md
source_date: 2026-03
authors: [Simon Scrapes]
ingested: 2026-05-10
updated: 2026-05-10
---

# Self-Improving Claude Code Skills (Karpathy Loop)

**Source:** Simon Scrapes · March 2026
**Routed by:** Operator — AI-Agents
**User Comment:** "do you think there is anything here worth implementing into our system?"

---

## TL;DR

Adapts Andrej Karpathy's "autoresearch" loop (make a change → run test → check score → keep or revert → repeat forever) to Claude Code skill improvement. An `evals.json` file with 25 binary (true/false) assertions drives the loop. Claude edits `skill.md`, reruns tests, and commits improvements autonomously overnight. Achieved 100% pass rate on a copywriting skill in 2 iterations.

---

## The Karpathy Loop (Applied to Skills)

```
Read skill.md → Make one change → Run test against evals.json
                                        ↓
                         Check pass rate vs. 25 binary assertions
                                        ↓
                    Score improved? → git commit, keep change, loop
                    Score dropped?  → git reset, try different change
                                        ↓
                         Loop until perfect score or manual stop
```

---

## The evals.json Structure

Each test entry has:
- `prompt` — what to ask Claude
- `expected_output` — the type of output expected
- `assertions` — array of 25 binary true/false checks

**Good binary assertions (automatable):**
- "Does not contain em-dashes"
- "Word count is under 300"
- "Final line is not a question"
- "First line appears as standalone sentence"
- "Contains at least one specific number or statistic"

**Poor assertions (not binary = not automatable):**
- "Has a compelling subject line" — subjective, can't be true/false
- "Tone sounds confident" — requires human judgment

---

## Two Layers of Skill Self-Improvement

**Layer 1 — Description improvement (already in skill-creator skill):**
Anthropic's built-in skill creator tests whether Claude *activates* the skill at the right time — using test queries and a trigger accuracy score. Loop runs until description is reliable.

**Layer 2 — Output quality (this video's addition):**
Binary assertion evals test whether the skill *produces correct output* when triggered. The Karpathy loop improves the skill's process instructions until all assertions pass.

---

## What It Cannot Fix

Binary loop handles: structure, format, word counts, forbidden patterns, required elements.

Still needs human judgment: tone of voice, creative quality, whether reference files are used correctly. The skill-creator's side-by-side dashboard is the tool for those.

---

## Arek & Co Applicability Assessment

**Verdict: Yes — worth implementing for key skills.**

The Arek&Co system already has:
- skill-creator skill (includes description eval loop = Layer 1)
- Multiple skills with skill.md files

**What to add:**
- `evals/eval.json` folder in each high-priority skill
- Binary assertions tailored to each skill's expected output
- One-line prompt to run the self-improvement loop overnight: *"Use the skill-creator skill, run a self-improvement loop on [skill name]. Use evals/eval.json. Loop until perfect score or I interrupt you."*

**Best candidates for implementation:**
1. Creative skills (song-pipeline, film-pipeline) — binary checks on format, required sections, frontmatter
2. Ingest skill (if formalised) — frontmatter completeness, source_path field, log entry format
3. Any skill that has had inconsistent outputs in past sessions

---

## Related

- [[claude-code]] — underlying tool
- [[skill-self-improvement-loop]] — concept page
- [[printing-press-cli-source]] — related Claude Code tooling
