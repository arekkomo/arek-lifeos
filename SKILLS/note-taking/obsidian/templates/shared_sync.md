# Shared Sync Log — Hot/Warm/Cold Bridge

> This file is the critical infrastructure connecting all three memory layers. Append-only — never overwrite.

## Format

Append new entries with this structure:

```markdown
## YYYY-MM-DD HH:MM [agent] — [Short Topic Name]
- **Topic:** [topic name]
- **Saving to:** [vault path]
- **State:** [what was left unfinished]
- **Next action:** [what the next agent should do]
```

## Example Entry

```markdown
## 2026-06-05 14:30 emily — Venv Migration
- **Topic:** Venv Migration Complete
- **Saving to:** AGENTS/venv-migration/
- **State:** Gateway and dashboard consolidated to venv install. System-pip copy removed.
- **Next action:** Set up dashboard as systemd service
```
