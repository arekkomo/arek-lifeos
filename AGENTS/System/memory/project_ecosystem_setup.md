---
name: Arek & Co. Ecosystem Setup Progress
description: Status of CoWork agent project setup and n8n connector bridges
type: project
originSessionId: 4639a801-82f1-4137-bd42-917ec652019c
---
All 8 agent CoWork project instructions written and saved to vault (2026-04-27). Arek set up all 7 projects in CoWork UI (System was already live).

**Why:** Full personal OS ecosystem — agents for Operator, Scholar, Director, Strategist, Accountant, Coach, Connector, System.

**CoWork instructions location:** `/AGENTS/<AgentName>/CoWork-Instructions.md` in Arek&Co for each agent.

**How to apply:** When Arek asks about agent setup or status, all instructions are written and deployed. The ecosystem is live except for 3 connector bridges below.

## Pending n8n bridges (Task #1, #2, #3)
> ℹ️ As of 2026-05-31 vault maintenance: these bridges remain not yet built. No confirmation received. Flagging as known pending work — no further ⚠️ needed until Arek addresses.

1. **Apple Reminders → Operator** — no native MCP connector; needs iOS Shortcuts → webhook → n8n
2. **Apple Health → Coach** — same pattern; iOS Shortcuts → webhook → n8n; existing "image to video from ios shortcut" workflow proves Shortcuts→n8n pattern already works
3. **Google Contacts → Connector** — n8n has native Google Contacts node; base workflow already created (ID: 8rwsSEDgFlC5TqLH "MCP Google Contacts Test 2"); Arek needs to add Google Contacts node manually in n8n UI and activate. Webhook path: `mcp-google-contacts`

## DGX Spark Infrastructure (added 2026-05-31)
The following is now live on the Spark and relevant to System agent scope:
- **Hermes agent:** Two instances (Arek/realityrove + Robert), see [[PROJECTS/Hermes-Installation/README]]
- **Open WebUI:** Running on Docker, port 12000. Access at http://10.0.0.15:12000
- **Ollama:** Models qwen3.6:latest (36B) and qwen3:14b live
- **Known issue:** pip upgrades wipe WhatsApp port patches — must reapply after any hermes-agent upgrade
