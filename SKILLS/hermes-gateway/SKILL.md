---
name: hermes-gateway
description: Manage Hermes gateway configuration, provider connections, and service lifecycle. Covers custom providers, security scanning, config structure, and troubleshooting lost connections after disconnects.
---

# Hermes Gateway Configuration & Management

## Config Structure: Two Places, Two Purposes

| File | Purpose |
|------|---------|
| `~/.hermes/config.yaml` | Provider definitions, tool routing, display settings, platform configs |
| `~/.hermes/.env` | Secrets, API keys, tokens (Ollama has no key; Discord bot token goes here) |

**Critical distinction:** Discord API keys in `.env`, Discord channel settings (require_mention, etc.) in `config.yaml`.

## Provider Configuration

### How Providers Work

```yaml
# config.yaml
model:
  default: qwen3.6:latest
  provider: custom        # <-- tells gateway to look in custom_providers
  base_url: http://localhost:11434/v1

providers: ["Ollama"]   # <-- LOADED providers (empty = no backend!)

custom_providers:
- name: Ollama
  base_url: http://localhost:11434/v1
  model: qwen3.6:latest
```

**The providers section must list custom providers explicitly.** If it's empty (`{}`), even though `custom_providers` defines Ollama, the gateway has no active provider and will ask you to configure one.

### Adding a Custom Provider (Ollama example)

```bash
# 1. Add to custom_providers in config.yaml
hermes config set custom_providers '[{"name": "Ollama", "base_url": "http://localhost:11434/v1", "model": "your-model"}]'

# 2. Add to providers list
hermes config set providers '["Ollama"]'

# 3. Restart
systemctl --user restart hermes-gateway
```

**Pitfall:** If you set `providers` via `hermes config set`, it may write the value as a quoted string instead of a YAML list. Verify the file has `providers: ["name"]` not `providers: '["name"]'`.

## SSH Disconnect & Sleep Recovery

### Symptoms
- Gateway started but reports "no AI backend" or "no configured provider"
- Ollama/ollama-server is running and reachable from curl
- `providers: {}` is empty in config.yaml

### Diagnosis
1. Check config: `grep "^providers:" ~/.hermes/config.yaml` → should NOT be `{}`
2. Check gateway: `hermes status` → should show Provider as your custom endpoint
3. Check Ollama: `curl -s http://localhost:11434/api/tags` → should return models
4. Check gateway logs: `journalctl --user -u hermes-gateway -n 30`

### Fix
- Ensure `providers: ["YourProviderName"]` in config.yaml
- Add fallback providers to handle transient outages: `hermes config set fallback_providers '["provider_name"]'`
- Restart gateway: `systemctl --user restart hermes-gateway`

### Prevention
- Set explicit `providers` list (not just `custom_providers`) so it survives gateway restarts
- Configure `fallback_providers` in config.yaml to auto-switch providers if primary fails (rate limits, connectivity, etc.)

## Security Scanning Interference

### Symptom
- Gateway says Ollama/custom provider isn't working
- API call to private IP (10.x.x.x, 192.168.x.x, 172.16-31.x.x) gets blocked
- Discord app shows "No AI backend" even though Ollama is reachable on localhost

### Cause
Hermes security scanner blocks requests to private/internal IPs by default. Your Ollama runs on a separate machine (10.0.0.15) — the scanner sees this as SSRF risk.

### Fix
The `security.allow_private_urls` setting must be `true`:
```bash
hermes config set security.allow_private_urls true
```

Check the value: `hermes config show | grep -i "private\|security"`

### Also check
- **model_catalog.providers** — separate from main `providers`, don't confuse
- **web/allow_private_urls** — different from security.allow_private_urls, check for duplicates

## Gateway Service Management

### Restart the gateway
```bash
systemctl --user restart hermes-gateway
```

### Check status
```bash
hermes gateway status
journalctl --user -u hermes-gateway -n 30
```

### Warning: `hermes gateway restart` overwrites the systemd service file
`hermes gateway restart` replaces `~/.config/systemd/user/hermes-gateway.service`, potentially resetting custom `WorkingDirectory`, `PATH`, or `VIRTUAL_ENV` values. Use `systemctl --user restart hermes-gateway` instead for safe restarts without service file modification.

### Verify after restart
```bash
hermes status | grep -A3 "Provider"
hermes gateway status
```

## Platform Config: Where Secrets Go

| Secret | File | Key |
|--------|------|-----|
| Discord bot token | `.env` | `DISCORD_BOT_TOKEN` |
| Slack bot token | `.env` | `SLACK_BOT_TOKEN` |
| WhatsApp mode | `.env` | `WHATSAPP_MODE` |
| WhatsApp allowed users | `.env` | `WHATSAPP_ALLOWED_USERS` |
| Channel settings (all platforms) | `config.yaml` | `discord:/slack:/whatsapp:` sections |

**Never put API keys in config.yaml.** The `.env` file is the credential store.

## Health Check False Positives

The gateway health check runs before any user messages are processed. It may report "No API key configured" or "No AI backend" if it checks the `.env` for keys BEFORE loading the custom provider config.

**How to verify:** `hermes status` reads the live gateway state and is the authoritative check. If it shows your custom provider, the backend IS working — the health check message may be stale.

## Dashboard & Remote Desktop Connection

### Dashboard Security Gate

The dashboard has two security measures when binding to non-loopback addresses:

1. **Auth gate enforcement** — If any OAuth provider is registered, the dashboard redirects to the OAuth flow for non-loopback binds (normal behavior).
2. **Total refuse** — If NO auth providers are registered AND no `dashboard_auth` plugin reports a provider, the dashboard **refuses outright** to bind to non-loopback (`0.0.0.0`).

```
Refusing to bind dashboard to 0.0.0.0 — the OAuth auth gate engages on non-loopback binds,
but no auth providers are registered.
```

**Fix — Option 1: Use SSH tunnel (safer, recommended):**
On your Mac:
```bash
ssh -L 9119:127.0.0.1:9119 realityrove@10.0.0.61
```
In the SSH session on Spark:
```bash
hermes dashboard --port 9119
```
In the Desktop app: `http://127.0.0.1:9119`

**Fix — Option 2: Skip auth gate (trusted home network only):**
```bash
hermes dashboard --host 0.0.0.0 --port 9119 --insecure
```

**Fix — Option 3: Register a DashboardAuthProvider** (see `references/dashboard-auth-setup.md`).

> The Dashboard is NOT just a web UI — it IS the backend server that the Desktop app connects to (WebSocket, REST, session management). When the Dashboard process dies, Desktop app shows "cannot reach gateway" even if the actual Hermes agent gateway is fine.

### Dashboard Restart

The Dashboard does not have a separate `start` subcommand:
```bash
# WRONG — this fails:
hermes dashboard start

# CORRECT — launch directly:
hermes dashboard --port 9119
```

Check status: `hermes dashboard --status` or `hermes dashboard --stop` to stop it.

### Remote Desktop App Setup

The Desktop app connects to the **Dashboard** (port 9119), not the gateway directly:
```
your Mac:
  Desktop App → Dashboard (http://10.0.0.61:9119)
                                              ↕
Spark:
                      Dashboard ↔ Gateway ↔ Agent
```

**Session Token:** Extract from the Browser Dashboard:
1. Open the browser Dashboard (e.g. `http://10.0.0.61:9119`)
2. Right-click → **View Page Source** (or `Cmd+Option+U`)
3. Search (Ctrl+F / Cmd+F) for `HERMES_SESSION_TOKEN`
4. Copy the long alphanumeric string between the quotes
5. Paste into Desktop app's "Session token" field → **Save and reconnect**

> **Token changes per page load** — always get a fresh one. The browser must already be connected to the Dashboard for the token to exist in the page HTML.

## Remote Access, Desktop, and Web Dashboard Operations

This skill is now the umbrella for Hermes gateway operations, including the previously separate remote-access, Desktop remote, and web UI/dashboard playbooks.

### Remote gateway access
- Use `gateway-remote-access` patterns when a local GUI/CLI/MCP client needs to reach a gateway on another machine.
- First verify network binding with `ss -tlnp | grep <port>`; `127.0.0.1` means remote clients need an SSH tunnel, while `0.0.0.0` / LAN IP means direct LAN access may work.
- Prefer SSH tunnels for untrusted networks; bind directly only on trusted LANs with the dashboard's auth/insecure tradeoffs understood.

### Desktop remote app
- The Desktop app connects to the **dashboard/control-plane port** (commonly `9119`), not the raw gateway adapter port.
- If buttons stop reacting after failed connection attempts, restart the Desktop app before deeper debugging.
- Port 8080 is commonly occupied by unrelated services; confirm the real dashboard port before configuring the client.

### Web UI / dashboard
- Build frontend after updates, then start the dashboard with the intended host/port.
- For LAN exposure, `--host 0.0.0.0 --insecure` is convenient but only acceptable on trusted networks; SSH tunneling avoids that.
- Dashboard start/stop failures often reduce to stale processes, port conflicts, or a mismatch between installed package and checkout.

## Related Files
- `references/ssh-disconnect-recovery.md` — Deep dive on SSH disconnect → provider loss debugging path
- `references/security-scan-blocking.md` — Security scan blocking private IPs, allowlist patterns, detection
- `scripts/provider-diagnostic.sh` — Script to quickly diagnose provider connectivity issues
- `references/dashboard-auth-setup.md` — Registering a DashboardAuthProvider for secure remote binds
- `references/desktop-remote-connection.md` — Full step-by-step for remote Desktop app setup
- `references/gateway-remote-access.md` — Legacy full remote gateway access playbook
- `references/hermes-desktop-remote.md` — Legacy Desktop remote setup and troubleshooting playbook
- `references/hermes-web-ui.md` — Legacy web UI/dashboard deployment playbook
- `references/hermes-desktop-remote-docker-port-conflicts.md` — Desktop remote port-conflict notes
- `references/hermes-web-ui-desktop-remote-connection.md` — Web UI remote Desktop connection notes
- `references/hermes-web-ui-session-2026-06-04.md` — Session-specific dashboard deployment notes