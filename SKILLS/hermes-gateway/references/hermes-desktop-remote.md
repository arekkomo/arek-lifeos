---
name: hermes-desktop-remote
description: Set up and troubleshoot Hermes Desktop app connections to a remote Hermes backend gateway on another machine. Covers gateway discovery, port navigation, connection steps, troubleshooting dead buttons, and auth methods.
---

# Hermes Desktop Remote Gateway Connection

Connect a Hermes Desktop app instance to a remote Hermes backend (Spark/DGX) so the Mac app acts as a thin UI client.

## Setup Steps

1. **Confirm gateway is running on target machine:**
   - Check dashboard port: `ps aux | grep hermes | grep dashboard`
   - Note the `--port` value (default `9119`)
   - The dashboard, NOT the gateway port (8080), is what the Desktop app connects to

2. **Check port availability on target:**
   ```
   ss -tlnp | grep <port>
   ```
   **WARNING:** Port 8080 may be occupied by SearXNG (a common collision). If it returns SearXNG on the network, use port 9119 (dashboard).

3. **On the Desktop app:**
   - Navigate to Settings → Gateway
   - Select **Remote gateway** (right card)
   - Enter URL: `http://<host-ip>:<port>` (use port 9119 for the dashboard)
   - Hit **Test remote** to verify
   - Hit **Save and reconnect** to apply

4. **Verify connection:** Status bar should confirm remote session. Top-left or status indicator shows the active remote.

## Troubleshooting

### Connection fails / buttons don't react
- **Quit and restart the Desktop app** — buttons can get stuck in a failed state without visual feedback
- Check `desktop.log` via the "Open logs" link for error details
- Confirm which user is running the gateway on Spark (it may not be your user)

### Port confusion
- Port `8080` = gateway process (but may be hijacked by SearXNG — check first!)
- Port `9119` = hermes dashboard (the actual connection target for Desktop app)
- If 8080 returns a search engine interface, use 9119
- **Docker container ports can hijack expected ports:** SearXNG (Docker) commonly grabs 8080; open-webui grabs 12000. Always verify `docker ps --format '{{.Names}} {{.Ports}}'` on Spark before assuming a port belongs to Hermes.

### Session token (critical: do NOT use local-extracted tokens remotely)
- The session token embedded in `http://<host>:9119/` HTML source (`window.__HERMES_SESSION_TOKEN__`) is **machine-scoped** — valid only for WebSocket connections initiated from localhost on Spark. Copying it to the Desktop app on a remote Mac will fail.
- If prompted for a session token on remote connections, **leave it blank** — self-hosted gateways may accept the connection without or with different auth. If that fails, check if the gateway requires OAuth (configured in `config.yaml` under `dashboard.oauth`).

## Known Quirks

- The Desktop app starts a local gateway by default — you must explicitly switch to Remote
- Self-hosted gateways may work without auth, or may need session token
- Once connected, all chat/skills/cron runs on the remote backend; the Mac app is UI-only
