---
title: SK-OP-03 — Journal Facilitation Flow
agent: Operator
summary: Step-by-step for running a journal session, including learnings feedback loop.
updated: 2026-05-28
---

# SK-OP-03 — Journal Facilitation Flow

> Trigger: Arek says "journal", "let's journal", or similar.

---

## Learnings Reference

Before starting, read `AGENTS/Operator/Learnings-Journal.md` and apply all rules listed there.

---

## Steps

1. Pull current questions from `AGENTS/Operator/Skills/Journal-Questions.md`
2. Ask questions **one at a time** — don't dump all at once
3. Let Arek answer at whatever length feels right
4. When done: synthesise into a clean journal entry
5. Save to `DAILY/Journal/YYYY-MM-DD-Journal.md`
6. Flag if questions feel stale — propose updates every 2–4 weeks

---

## Entry Format

```
---
date: YYYY-MM-DD
mood: [1-10 if Arek mentions it]
energy: [1-10 if mentioned]
---

[Synthesised narrative — Arek's voice, not clinical]

## Wins
## Challenges
## Insights
## Tomorrow's Focus
```

---

## Feedback Step

After saving the entry, ask once:
> "Anything to improve on how we ran that session? (Y to give feedback / skip to move on)"

If Arek gives feedback: extract the rule, append it to `AGENTS/Operator/Learnings-Journal.md` with today's date.

---

## Edge Cases

| Situation | Response |
|---|---|
| Arek gives very short answers | Don't push — synthesise what you have |
| Questions feel stale | Note it: "These questions are [X weeks] old — want to update them?" |
| Session interrupted | Save partial entry with `[INCOMPLETE]` tag |
