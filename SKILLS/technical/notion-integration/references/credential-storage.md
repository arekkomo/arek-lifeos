---
name: credential-storage-conventions
description: |
  Where Hermes stores OAuth/bot tokens for external services.
---

# Credential Storage Conventions

All external service tokens should go in `~/.hermes/.env` as uppercase env var names.

| Service | Env Var Name | Token Format |
|---------|-------------|--------------|
| Notion MCP / OAuth | `NOTION_MCP_TOKEN` | `ntn_xxx` |
| Notion API (legacy) | `MCP_NOTION_API_KEY` | `ntn_xxx` |
| Discord Bot | `DISCORD_BOT_TOKEN` | `MTUx...D0` (base64-like) |
| OpenRouter | `OPENROUTER_API_KEY` | `sk-or-v1:...` |

**NOTES:**
- `chmod 600 ~/.hermes/.env` after editing
- `.env` does NOT auto-load in shell — export manually or use `python-dotenv`
- `config.yaml` references env vars via `env:VAR_NAME` syntax (not plaintext tokens)
- Never store tokens in `config.yaml` or session logs