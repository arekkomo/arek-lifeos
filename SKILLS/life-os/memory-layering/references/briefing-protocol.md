# Two-Agent Briefing Protocol

> **When:** Each morning, or on-demand for strategic briefings.
> **Where:** Telegram channel `#briefing` (or on-demand message).

## Emily - Personal Pulse Brief

**Trigger:** "Good morning" (or "Go Emily" in the future) in `#briefing`

**Output:**
1. Today's date
2. Top 5 world news headlines
3. [Later: Calendar summary, project status, pending items]

**News Sources:** BBC, Reuters, Google News

**Schema (future expansion):**
```
## [YYYY-MM-DD] Morning Briefing
- **Date:** {today}
- **Top Headlines:**
  1. ...
  2. ...
  3. ...
  4. ...
  5. ...
- **Calendar:** {today's events}
- **Priority Projects:** {active projects}
- **Pending Decisions:** {items requiring Arek's input}
- **Health Pulse:** {latest fitness/nutrition metrics}
```

## Alfred - Strategic CEO Brief

**Trigger:** "Go Alfred" (or user-requested) in `#briefing`

**Output:**
1. What we need to focus on (priority shift)
2. Plans reviewed against goals
3. Decisions to make (with trade-offs)
4. What we should be working on (action items)

**Sources:** Uses the same news sources (BBC, Reuters, Google News) to inform strategic perspective, plus system health metrics from `shared_sync.md` + vault status.

**Schema:**
```
## [YYYY-MM-DD] CEO Strategic Brief
- **Market Watch:** {key news impacting Arek&Co direction}
- **Priority Focus:** {1-3 things Arek should focus on this week}
- **Plan Review:** {active projects status vs timeline}
- **Decisions Needed:**
  1. {decision} → Trade-offs: {pros/cons}
  2. {decision} → Trade-offs: {pros/cons}
- **Action Items:** {specific next steps}
```

## Sync Between Briefings

Both agents contribute to `AGENTS/shared_sync.md` which serves as the handoff protocol. Each agent reads it before generating their briefing to ensure continuity.
