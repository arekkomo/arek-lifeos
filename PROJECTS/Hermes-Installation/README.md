---
title: Hermes Installation & Maintenance
category: project
summary: Local AI agent setup on DGX Spark with Discord and WhatsApp gateways for Arek and Robert
tags: [hermes, dgx-spark, ai-agent, discord, whatsapp, ollama]
updated: 2026-05-31
---

# Hermes Installation & Maintenance

## Overview

Two Hermes AI agent instances running locally on **NVIDIA DGX Spark** (`spark-6d75`, IP: `10.0.0.15`), connected to local Ollama models. Fully private — no cloud API costs.

---

## Hardware

- **Machine:** NVIDIA DGX Spark (`spark-6d75`)
- **OS:** DGX OS (Ubuntu 24.04, Linux 6.17, aarch64)
- **Memory:** 128GB unified
- **Network:** Must use **ethernet** (`enP7s7`) — WiFi via Deco mesh blocks GitHub/Discord IPs (Rogers ISP issue)

---

## Instances

### Arek's Agent (realityrove)
- **User:** `realityrove`
- **Model:** `qwen3.6:latest` (36B, Q4_K_M)
- **Discord:** Bot name `Hermés` — App ID `1510360723262537859`
- **WhatsApp:** Personal number (self-chat mode), port `4000`
- **Gateway:** User systemd service (`hermes-gateway.service`)
- **Install method:** pip (`hermes-agent==0.15.x`)

### Robert's Agent (Tula)
- **User:** `robert`
- **Model:** `qwen3:14b` (14B, Q4_K_M)
- **Discord:** None
- **WhatsApp:** Personal number (self-chat mode), port `6000`
- **Gateway:** User systemd service (`hermes-gateway.service`)
- **Install method:** pip (`hermes-agent==0.15.x`)

---

## Ollama

```bash
# Check running models
curl -sS http://localhost:11434/api/tags

# Pull a new model
ollama pull <model-name>

# Switch Hermes model
hermes model
```

**Installed models:**
- `qwen3.6:latest` (36B) — Arek
- `qwen3:14b` (14B) — Robert

---

## Key File Locations

### Arek (realityrove)
```
~/.hermes/config.yaml          # Main config
~/.hermes/.env                 # API keys and platform tokens
~/.hermes/whatsapp/session     # WhatsApp session (don't delete)
~/.hermes/hermes-agent/        # Git clone of hermes-agent repo
~/.local/bin/hermes            # Hermes binary
```

### Robert
```
/home/robert/.hermes/config.yaml
/home/robert/.hermes/.env
/home/robert/.hermes/whatsapp/session
/home/robert/.local/bin/hermes
```

---

## Gateway Management

```bash
# Check status
hermes gateway status

# Restart
hermes gateway restart

# View logs
journalctl --user -u hermes-gateway -n 50 --no-pager

# View WhatsApp bridge logs
cat ~/.hermes/whatsapp/bridge.log
```

---

## Known Issues & Fixes

### 1. Ethernet Required
WiFi via Deco mesh blocks GitHub, Discord, WhatsApp IPs (Rogers ISP).
**Fix:** Keep ethernet cable (`enP7s7`) connected to Spark at all times.

### 2. WhatsApp Bridge Port Conflict
Default port 3000 conflicts with other services.
- Arek's bridge: port `4000`
- Robert's bridge: port `6000`

Patches applied to:
- `~/.local/lib/python3.11/site-packages/gateway/platforms/whatsapp.py` — default port changed
- `~/.hermes/hermes-agent/scripts/whatsapp-bridge/bridge.js` — default port changed
- Robert's copy: `~/.local/lib/python3.11/site-packages/scripts/whatsapp-bridge/bridge.js`

### 3. SearXNG Web Search
Running on Docker, port `8080`. Config at `~/searxng-config/settings.yml`.
```bash
docker ps | grep searxng
docker restart searxng
```

### 4. Apt Sources Conflict
Two NVIDIA Workbench sources conflict. Fixed by adding `Signed-By` to `/etc/apt/sources.list.d/third-party.sources`.

### 5. Python 3.11 Location
Installed via deadsnakes PPA. Path: `/usr/bin/python3.11`

### 6. sudo hermes = command not found
Use full path: `sudo ~/.local/bin/hermes <command>`

### 7. pip upgrade wipes port patches ⚠️ CRITICAL
Any `hermes-agent` pip upgrade or reinstall overwrites the WhatsApp bridge port patches. After every upgrade, reapply manually:

```bash
# For Arek (realityrove) — port 4000
sed -i 's/config.extra.get("bridge_port", 3000)/config.extra.get("bridge_port", 4000)/' \
  ~/.local/lib/python3.11/site-packages/gateway/platforms/whatsapp.py

# For Robert — port 6000 (run as robert)
sed -i "s/getArg('port', '3000')/getArg('port', '6000')/" \
  ~/.local/lib/python3.11/site-packages/scripts/whatsapp-bridge/bridge.js
sed -i 's/config.extra.get("bridge_port", 3000)/config.extra.get("bridge_port", 6000)/' \
  ~/.local/lib/python3.11/site-packages/gateway/platforms/whatsapp.py

hermes gateway restart
```

### 8. Version pinned at 0.15.2
Do NOT use 0.15.1 — it's missing `gateway.slash_access` and `tools.tool_output_limits` modules, causing WhatsApp message dispatch to fail. Always reinstall to 0.15.2 if a downgrade occurs:
```bash
python3.11 -m pip install hermes-agent==0.15.2
# Then immediately reapply port patches (see Issue #7)
```

---

## Discord Bot (Arek only)

- **Bot name:** Hermés
- **App ID:** `1510360723262537859`
- **Developer Portal:** https://discord.com/developers/applications
- **Privileged Intents:** All three enabled (Presence, Server Members, Message Content)
- **Server:** Reality Rove server

---

## Updates

```bash
# Update Hermes (run as each user)
hermes update

# Or via pip
python3.11 -m pip install --upgrade hermes-agent

# Update Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Update models
ollama pull qwen3.6:latest
ollama pull qwen3:14b
```

---

## Reinstall from Scratch

If Hermes needs to be reinstalled:

```bash
# 1. Remove existing install
hermes uninstall  # or rm -rf ~/.hermes ~/.local/bin/hermes

# 2. Install via pip (GitHub is sometimes blocked on WiFi)
python3.11 -m pip install hermes-agent

# 3. Setup
export PATH="$HOME/.local/bin:$PATH"
python3.11 -m pip install cffi  # required fix
hermes setup

# 4. Fix WhatsApp bridge
# Copy bridge from git clone to pip path
cp -r ~/.hermes/hermes-agent/scripts/whatsapp-bridge \
  ~/.local/lib/python3.11/site-packages/scripts/

# 5. Fix WhatsApp port (change from 3000 to 4000 or 6000)
sed -i "s/getArg('port', '3000')/getArg('port', '4000')/" \
  ~/.hermes/hermes-agent/scripts/whatsapp-bridge/bridge.js
sed -i 's/config.extra.get("bridge_port", 3000)/config.extra.get("bridge_port", 4000)/' \
  ~/.local/lib/python3.11/site-packages/gateway/platforms/whatsapp.py

# 6. Install gateway service
hermes gateway install
hermes gateway start
```

---

## Tools Status

| Tool | Status | Notes |
|------|--------|-------|
| Terminal/Commands | ✅ | Built-in |
| Vision | ✅ | Built-in |
| Text-to-Speech | ✅ | Edge TTS |
| Task Planning | ✅ | Built-in |
| Skills | ✅ | Built-in |
| Web Search | ✅ | SearXNG at localhost:8080 |
| Browser Automation | ❌ | Needs `npm install -g agent-browser` |
| Image Generation | ❌ | Needs FAL_KEY or OPENAI_API_KEY |
| Mixture of Agents | ❌ | Needs OPENROUTER_API_KEY |
| Skills Hub (GitHub) | ❌ | Needs GITHUB_TOKEN |

---

## Useful Commands

```bash
# Test Hermes
hermes -z "Reply exactly OK"

# Check all config
hermes config

# Run diagnostics
hermes doctor

# Switch model
hermes model

# View sessions
hermes sessions

# Start dashboard (from Arek's account)
hermes dashboard --host 0.0.0.0 --insecure
# Then open: http://10.0.0.15:9119
```
