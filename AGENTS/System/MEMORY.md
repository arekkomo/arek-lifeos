# System Agent — MEMORY.md
## Persistent System Facts

### Identity & Role
- Agent: System (technical infrastructure architect)
- Role: Technical setup, inventory, profile/agent ecosystem management, CoWork/Hermes optimization, hardware/software tracking

### Account Information
- Primary vault: `/home/realityrove/Obsidian/Arek&Co/`
- Hermes host: DGX "Spark" (10.0.0.61)
- Network credentials: NVIDIA Connect (no manual SSH needed)

### Technical Setup
- **MacBook Pro** 16" (Nov 2024), M4 Max, 36GB, macOS Tahoe 26.3.1
- **iPhone** 17 Pro Max
- **DGX Spark** (Linux/debian) — runs Hermes, Ollama, Open WebUI, Docker, SearXNG
- **Ollama**: `qwen3.6:latest` at http://10.0.0.61:11434/v1
- **Hermes Dashboard**: port 9119; Gateway: port 8080 (SearXNG)
- **Desktop app** connects to http://10.0.0.61:9119
- **Gateway remote access**: URL + session token from browser source via \`__HERMES_SESSION_TOKEN__\`
- **Debian workaround**: create venv first, then upgrade inside it (externally-managed Python)

### Current Profiles (6 total)
| Profile | Model | Running |
|---------|-------|---------|
| systems | qwen3.6:latest | ✅ Yes |
| coach | qwen3.6:latest (Ollama) | ✅ Yes |
| connector | — (no model) | ⛔ No |
| director | — (no model) | ⛔ No |
| finance | — (no model) | ⛔ No |
| systems | qwen3.6:latest | ✅ Yes |

### Vault Structure Notes
- \`raw/\` is immutable/read-only
- Skills live in \`/home/realityrove/Obsidian/Arek&Co/SKILLS/\`
- Agent Briefs in \`AGENTS/<agent>/Brief.md\`
- MEMORY.md/USER.md per agent in \`AGENTS/<agent>/\`

### Infrastructure Conventions
- Profile configs: \`~/.hermes/profiles/<profile>/config.yaml\`
- Memories: \`~/.hermes/profiles/<profile>/memory/\`
- Cron jobs: \`~/.hermes/cron/\`

### Key Decisions
- Coach (qwen3.6:latest via Ollama) has 6 skills, Notion MCP, dedicated Telegram bot, Arek Telegram ID 8178908137 approved
- Telegram binding now uses \`platforms.telegram.extra.group_topics\` — old \`telegram.group_topics: {'145': 'coach'}\` is stale
- Arek prefers direct specialist-agent communication over central routing when domain is clear
- Coach moving out of 'Arek & Emily & Co.' group to dedicated profile/bot

### Recent Changes
- 2026-06-07: Set up Holographic memory provider (local SQLite, no API key)
- 2026-06-07: Created MEMORY.md/USER.md files for all 6 profiles in vault
