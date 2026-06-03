---
title: Skill Self-Improvement Loop (Karpathy Pattern)
category: concept
summary: Autonomous loop that tests a Claude Code skill against binary assertions, edits skill.md if any fail, and repeats overnight until a perfect score — no human input required after setup.
tags: [claude-code, skills, evaluation, binary-assertions, autonomous-improvement, karpathy]
sources: 1
updated: 2026-05-10
---

# Skill Self-Improvement Loop (Karpathy Pattern)

An autonomous eval-driven loop that improves Claude Code skills overnight without human input, inspired by Andrej Karpathy's autoresearch concept.

---

## How It Works

1. Create an `evals/eval.json` file in the skill folder with 25 binary assertions
2. Prompt Claude: "Run a self-improvement loop on this skill. Use evals/eval.json. Loop until perfect score or I interrupt you."
3. Claude edits `skill.md`, runs tests, checks pass rate, keeps changes if score improves, reverts and tries again if it drops
4. Wake up to a skill with a perfect (or higher) pass rate

---

## Binary Assertion Rules

Assertions must be **true/false** (not subjective):

✅ "Final line is not a question"
✅ "Word count under 300"
✅ "Contains at least one number or statistic"
✅ "Frontmatter has required fields: title, category, summary"
❌ "Tone sounds confident" — subjective, not automatable
❌ "Subject line is compelling" — requires human judgment

---

## Two Improvement Layers

| Layer | What it improves | Tool |
|---|---|---|
| 1 — Description | Skill activation (does Claude trigger the skill?) | Built into skill-creator skill |
| 2 — Output | Skill output quality (does the result meet criteria?) | Karpathy loop + evals.json |

---

## Sources

- [[self-improving-skills-source|Self-Improving Claude Code Skills (Simon Scrapes)]]
