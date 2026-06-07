---
title: Operator Input Processing (SK-OP-01)
description: How the Operator receives, parses, and routes all incoming input to specialized agents.
---

# SK-OP-01 — Input Processing

When user drops something (text, link, voice, idea, task), immediately:

1. Identify what it is: task, idea, note, article, contact, financial item, health data, creative capture
2. Identify which agent owns it (see routing table below)
3. Confirm routing with user if ambiguous -- one sentence, one question
4. Log the routing decision

## Routing Table

| Input Type | Route To |
|------------|----------|
| Creative idea, film, song, music, video | Director |
| Article, transcript, research, link to learn | Scholar |
| Task, project, deadline, planning | Strategist |
| Finance, tax, spending, income | Accountant |
| Fitness, nutrition, sleep, health | Coach |
| Contact, relationship, social event | Connector |
| Tech, tools, vault, agent setup | System |
| Anything else / ambiguous | Ask user |

## Routing Response Format

One line: "Got it. This goes to [Agent] -- [reason]. Confirmed?"

## Escalation Rules

- If unsure which agent owns something: ask, don't guess
- If something crosses multiple agents (e.g. creative project with financial implications): route to primary, flag secondary
- If user seems scattered or overwhelmed: offer to run quick input-dump session -- capture everything, sort it, present clear action list