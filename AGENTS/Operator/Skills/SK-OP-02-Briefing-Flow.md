---
title: SK-OP-02 — Daily Briefing Flow
agent: Operator
summary: Implementation spec for the morning briefing. Tool sequence, data sources, format, and edge case handling.
updated: 2026-05-13
---

# SK-OP-02 — Daily Briefing Flow

> Trigger: Arek says "morning briefing", "good morning", "briefing", or the scheduled heartbeat fires.
> Target: Delivered in under 2 minutes of reading time. Scannable. No prose padding.

---

## Tool Sequence

Run these in order. Each step is independent — if a tool fails, skip it gracefully and note the gap.

| Step | Tool / Source | What to pull |
|---|---|---|
| 1 | `mcp__489b3c48__list_events` | Today's calendar events (primary calendar) |
| 2 | `mcp__489b3c48__list_events` | Next 7 days (flag anything time-sensitive) |
| 3 | `mcp__f90aaabc__search_threads` | Unread / flagged email since last briefing |
| 4 | Web search | Vancouver weather (current + today's forecast) |
| 5 | Web search | VFX industry news (1–2 items) |
| 6 | Web search | AI / ML news (1–2 items) |
| 7 | Vault read | `AGENTS/Operator/Logs/` — any unresolved items |
| 8 | Vault read | Check if any agent has flagged a pending item |

**Order rationale:** Calendar first (affects the day's shape), email second (anything urgent), weather (affects commute / mood), news last (background context).

---

## Briefing Template

```
# Morning Briefing — [Day], [Date]

## Today
[Weather: current temp + day forecast — 1 line]
[Calendar: time-blocked events for today — bullets]
[If no events: "Clear calendar today."]

## This Week
[Any events in the next 7 days worth flagging — 2–4 bullets max]
[If nothing: omit this section]

## Top Priorities
[3 High-priority open items across all projects — pulled from Strategist Board context]
[Format: "· [Project] — [Task]"]

## Email
[Flagged threads since last briefing — 2–4 bullets]
[Subject + sender + one-line summary]
[If nothing urgent: "No flagged email."]

## News
**VFX:** [1–2 items — headline + 1-line summary]
**AI:** [1–2 items — headline + 1-line summary]

## Flags
[Any items from other agents that need Arek's input or decision]
[If none: omit this section]
```

---

## Edge Case Handling

| Situation | Response |
|---|---|
| Calendar MCP fails | Note "Calendar unavailable" — don't skip the section |
| Email MCP fails | Note "Email unavailable" — continue with rest |
| No events today | "Clear calendar." |
| No flagged email | "No flagged email." |
| No news found | Skip news section |
| Agent flags section | Only include if there's actually something pending |
| Briefing triggered at night | Adapt greeting; focus on tomorrow's calendar |

---

## Learnings Reference

Before running the briefing, read `AGENTS/Operator/Learnings-Briefing.md` and apply all rules listed there.

After delivering the briefing, ask once:
> "Anything to improve on this briefing? (Y to give feedback / skip to move on)"

If Arek gives feedback: extract the rule, append it to `Learnings-Briefing.md` with today's date. Don't ask again until next session.

---

## Tone Rules (per Writing-Rules.md)

- No "Good morning! Here's your briefing for today!" opener — start with the date header
- Bullets over prose for every section
- If a section is empty, either omit it or write one clean line — no padding
- No sign-off at the end

---

## Scheduled Heartbeat (I.1)

When running on a scheduled basis (not Arek-triggered):
- Run the full briefing flow
- Save output to `DAILY/Briefings/YYYY-MM-DD-Briefing.md`
- Do NOT surface in chat unless Arek has requested it or there's a High-priority flag

---

## Calendar IDs

| Calendar | ID |
|---|---|
| Primary (Arek) | `arek.komorowski@gmail.com` |
| realityroveSM | `f038b90c084dca4e7868b0490d16f8ed3a3bdd47e6dcf60eabb5319cd87f1a12@group.calendar.google.com` |
| Holidays in Canada | `en.canadian#holiday@group.v.calendar.google.com` |
