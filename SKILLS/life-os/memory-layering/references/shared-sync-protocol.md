# Shared Sync Protocol Between Agents

> **Purpose:** Handoff mechanism between Emily (Field) and Alfred (CEO) agents so neither loses context.

## Format

Both agents append to `AGENTS/shared_sync.md` using this format:

```
## [YYYY-MM-DD HH:MM] <agent> | <title>
<what was done, in 1-3 lines. Focus on changes, not restatements.>
---
```

## Rules

- **Append only.** Never edit old entries.
- **Short.** One line is fine. Don't repeat the full file content.
- **Specific.** "Filed 3 knowledge pages: runway-ml, kling-ai, helios + updated LEARNING/index.md" — not "did some filing."
- **Both agents read shared_sync.md before generating any response or briefing.** This is the "warm memory" bridge.

## When Agents Write

| Agent | When to write |
|--|--|
| **Emily** | After filing notes/links, daily briefing done, calendar changes, goals updated |
| **Alfred** | After strategic decisions, project changes, synthesis written, structural vault changes |

## Examples

```
## [2026-06-02 09:15] Emily | Knowledge filing
Filed 3 pages to LEARNING/Knowledge/AI-Video/: runway-ml, kling-ai, helios. Updated LEARNING/index.md.
---

## [2026-06-02 14:30] Alfred | Strategy shift
Decided to deprioritize RealityRowHub market research. Moved focus to CREATIVE/Imma-Nyala pilot production. Updated PROJECTS/RealityRowHub/Overview.md.
---
```

## Common Pitfalls

- **Don't write to shared_sync.md without actually making the change.** It's a log, not a request.
- **Don't skip this.** If you wrote to the vault but didn't log it, the other agent won't know.