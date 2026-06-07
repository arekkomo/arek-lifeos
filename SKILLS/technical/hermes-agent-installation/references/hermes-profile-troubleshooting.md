---
name: hermes-profile-troubleshooting
description: "Quick diagnostic patterns and fixes for Hermes profile, gateway, MCP, and routing issues"
---

# Hermes Profile Troubleshooting

## Quick Diagnoses

### Gateway Won't Start / Fails Silently
1. Check if gateway is already running: `pgrep -fa hermes.*<profile>`
2. If stuck, kill old process then restart: `hermes gateway start --profile <name>`
3. For systemctl service: `systemctl --user status hermes-<profile>`

### MCP Servers Fail to Connect
Check profile's `.env` for required tokens (e.g. `NOTION_MCP_TOKEN`)
Check MCP config in `config.yaml` (URL, auth format, transport)

### Skills Not Loading
1. `hermes skills list` — verify installed
2. Check profile config.yaml `skills:` section lists them
3. `/reload-skills` in session or restart gateway

### Model/Provider Issues
1. `hermes doctor` — check config and dependencies
2. `hermes auth` — re-authenticate OAuth providers
3. Check `.env` has correct API keys

## Notion MCP Auth Format — Critical Pitfall

```yaml
mcp_servers:
  notion:
    auth: "token"  # STRING — NOT nested dict!
```

With token in profile's `.env` as `NOTION_MCP_TOKEN=***`.

**BROKEN:** `auth: {token: env:NOTION_MCP_TOKEN}` → `'dict' object has no attribute 'lower'`

**FIX:** Change to `auth: "token"` (plain string).

## Profile Structure

```
~/.hermes/profiles/<name>/
├── config.yaml        # Model, skills, tools, etc.
├── .env               # Tokens/secrets
├── skills/            # Profile-specific skills
└── logs/              # Gateway logs
```