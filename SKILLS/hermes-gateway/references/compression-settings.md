# Compression Settings Guide

Hermes uses session context compression to manage large conversations. Settings live in `~/.hermes/config.yaml` under `compression:`.

## Recommended Settings For Detailed Work

When preserving technical detail is important (architecture discussions, model evaluations, infrastructure design):

```yaml
compression:
  enabled: true
  threshold: 0.85        # only compress at 85% of context (not 50%)
  target_ratio: 0.4       # keep 40% of old turns (not 20%)
  protect_last_n: 40      # protect 40 recent turns (not 20)
  hygiene_hard_message_limit: 600
  protect_first_n: 3
  abort_on_summary_failure: false
```

## Settings Explained

| Setting | What it does | Recommendation |
|---------|------|-|------|
| `threshold` | % of context when compression kicks in | 0.85 (later = less aggressive) |
| `target_ratio` | % of old turns kept after compression | 0.4 (higher = more detail preserved) |
| `protect_last_n` | Number of recent turns to keep intact | 40 (more protection for active work) |
| `hygiene_hard_message_limit` | Absolute line limit before forced compression | 600 (more headroom) |

## Default (Aggressive) Settings — AVOID For Deep Work

```yaml
compression:
  threshold: 0.5       # compress at 50% of context — too early
  target_ratio: 0.2    # shrink to 20% — loses most detail
  protect_last_n: 20   # protects fewer turns
  hygiene_hard_message_limit: 400
```

**Why this matters:** Threshold 0.5 + target_ratio 0.2 means compression kicks in halfway through the conversation and shrinks everything to a skeleton. Technical detail (model routing decisions, infrastructure choices, architectural tradeoffs) gets vaporized.

## Pitfalls

1. **Too aggressive compression loses technical detail** — Use 0.85 + 0.4 for sessions involving architecture, code review, or multi-stage decisions.
2. **Suggest compression review at session start** — Don't wait for context to fill mid-session. If the user says they're starting a deep technical session, recommend this check first.
3. **Config writes are protected** — `config.yaml` has write protection on some operations. Use `hermes config set` CLI where possible or `skill_manage(action='patch')` if working from skills.