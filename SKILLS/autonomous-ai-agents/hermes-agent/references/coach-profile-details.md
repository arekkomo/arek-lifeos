# Arek & Co. Life OS — Coach Profile Setup Details

## Coach Profile Architecture

Coach is a specialist Hermes profile in the Arek & Co. Life OS multi-agency system that:
- Runs as named profile "coach" at `~/.hermes/profiles/coach/`
- Receives messages routed from main gateway (Telegram thread 145 → Coach)
- Uses Ollama model `qwen3.6:latest` at `http://10.0.0.61:11434/v1`
- Has 6 skills loaded: coach-specialist, coach-fitness-tracking, coach-nutrition-tracking, coach-body-composition, coach-sleep-recovery, coach-health-intelligence
- Does NOT own its own Telegram client — relies on main gateway for routing
- Notion integration: OAuth tokens, 8 databases, 92 pages
- Primary Notion databases: dtb Writing, dtb Knowledge, Workout DB (cfbdbb06-4e54-44a1-8004-75b6b5b7aed8), Body Measurements (e5f13449-8078-4a6f-9465-3bb3d001f07b)

## Starting & Managing Coach Gateway

```bash
# Start
hermes gateway start --profile coach

# Check status
hermes gateway status --profile coach
hermes profiles list coach

# Check logs
tail -50 ~/.hermes/profiles/coach/logs/gateway.log
tail -30 ~/.hermes/profiles/coach/logs/errors.log
```

## Coach's config.yaml Key Values

```yaml
model:
  default: qwen3.6:latest
  provider: custom
  base_url: http://10.0.0.61:11434/v1

mcp_servers:
  notion:
    url: https://mcp.notion.com/mcp
    auth:
      token: env:NOTION_MCP_TOKEN
    transport: streamable_http
    name: Notion MCP
    enabled: true

skills:
- hybrid-arch:coach-specialist
- coach-fitness-tracking
- coach-nutrition-tracking
- coach-body-composition
- coach-sleep-recovery
- coach-health-intelligence
```

## Session Date: 2026-06-06