# Remote Desktop App Connection Guide

## Architecture

The Desktop app connects to the **Dashboard** (port 9119), not the gateway directly. The Dashboard serves as the WebSocket/REST proxy between the Desktop app and the actual Hermes agent gateway.

```
your Mac:
  Desktop App → Dashboard (http://10.0.0.61:9119)
                                              ↕
Spark:
                      Dashboard ↔ Gateway ↔ Agent
```

## Step-by-Step Connection

### 1. Verify Network

On your Mac, confirm the Mac can reach Spark:
```bash
curl -v -I http://10.0.0.61:9119/
```
Expected: `HTTP/1.1 200 OK` (or `405 Method Not Allowed` for HEAD — that's fine, the API accepts GET).

If 200 OK → network is fine. If connection refused → firewall or wrong address.

### 2. Start the Dashboard

**Default (localhost only):**
```bash
hermes dashboard --port 9119
```

**Remote access — Option A (SSH tunnel, safer):**
On your Mac:
```bash
ssh -L 9119:127.0.0.1:9119 realityrove@10.0.0.61
```
In the SSH session:
```bash
hermes dashboard --port 9119
```

**Remote access — Option B (direct bind, trusted network only):**
```bash
hermes dashboard --host 0.0.0.0 --port 9119 --insecure
```

> **Important:** Dashboard does NOT have a `start` subcommand. It is launched directly via `hermes dashboard --port ...`.

### 3. Get the Session Token

1. Open the browser to the Dashboard URL (e.g. `http://10.0.0.61:9119` or `http://127.0.0.1:9119` via tunnel)
2. Right-click → **View Page Source** (`Cmd+Option+U` on Mac)
3. Search for `HERMES_SESSION_TOKEN`
4. Copy the long alphanumeric string between quotes (no spaces)
5. Paste into Desktop app's "Session token" field → **Save and reconnect**

> **Token is per-page-load** — fresh load = fresh token. Always get a new one at connection time.

### 4. Desktop App Configuration

- **Remote URL:** `http://10.0.0.61:9119` (Option A) or `http://127.0.0.1:9119` (SSH tunnel)
- **Session token:** The one you just extracted
- Hit **Save and reconnect**

## Common Failure Modes

### Cannot connect (even with correct token)
- Dashboard is not running → restart it (`hermes dashboard --port 9119`)
- Dashboard binding refused → auth gate refused non-loopback without a registered auth provider → use SSH tunnel or `--insecure`
- Wrong port → Dashboard defaults to 9119
- Gateway stopped after update → the update process can stop the Dashboard; restart it

### Dashboard won't bind to 0.0.0.0
- No `auth_provider` registered → the dashboard blocks non-loopback binds for security
- Use SSH tunnel (recommended) or `--insecure` flag

## Hidden Failure Modes

### Desktop app silently reverts to localhost (ECONNREFUSED 127.0.0.1:9119)
**Symptom:** Despite entering a remote URL (e.g. `http://10.0.0.61:9119`), the Desktop app shows "cannot connect" or the Gateway settings display fall into the localhost fallback (`127.0.0.1:9119`). Curl confirms `10.0.0.61:9119` returns HTTP 200 — the network is fine.

**Root cause:** An outdated Desktop app silently reverts to `127.0.0.1:9119` when the remote URL fails to apply or persist. This is NOT a network failure — it's the app's default fallback behavior.

**Fix:** **Always update the Desktop app to the latest binary first.** Then re-enter the Remote URL + fresh session token. The update is done in-app; there's no CLI command for the Desktop binary itself.

### Update command for direct pip installs
**Symptom:** `hermes update` hangs waiting for interactive confirmation you can't see (common over SSH/remote sessions).

**Fast fix:** Run `uv pip install --upgrade hermes-agent` directly — it works non-interactively.

### Check Dashboard health
```bash
hermes dashboard --status
hermes dashboard --stop
```

### Verify process is alive
```bash
pgrep -f 'hermes.*dashboard'
ss -tlnp sport = :9119
```

### Check logs
- Desktop app: Click "Open logs" in the error dialog → find `gateway.log` section
- Server-side: Check `~/.hermes/logs/gateway.log`

## Related Files
- `.../hermes-gateway/SKILL.md` — Gateway management and config
- `.../hermes-agent-installation/SKILL.md` — Hermes installation and update repair
