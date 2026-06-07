---
name: hermes-web-ui
description: "Hermes web UI and dashboard deployment — building the frontend, starting it, exposing remotely, and SSH tunneling from remote machines."
---

# Hermes Web UI / Dashboard

The Hermes web UI is a separate server from the gateway process. It serves config management, API key editing, sessions, and model picker. It does NOT replace Telegram/Discord — it's an admin/control plane.

## Quick Start

```bash
# 1. BUILD the frontend (only needed once, or after upstream updates)
cd ~/.hermes/hermes-agent/web && npm run build

# 2. Start dashboard
python3 -m hermes_cli.main dashboard --host 127.0.0.1 --port 9119 --no-open
```

Default: `http://127.0.0.1:9119`

## Exposing Remotely (LAN / Mac / SSH)

### Option A: Direct bind on LAN
```bash
python3 -m hermes_cli.main dashboard --host 0.0.0.0 --port 9119 --insecure --no-open
```
`--insecure` required for non-loopback binds (bypasses OAuth auth gate, since no auth config). Only use on trusted networks.

From Mac: `http://<spark-ip>:9119`

### Option B: SSH tunnel (recommended, no `--insecure` needed)
On Mac, create the tunnel:
```bash
ssh -fNL 9119:localhost:9119 realityrove@10.0.0.61
```
Then use `http://localhost:9119` — the tunnel makes it secure.

Make persistent: add to `~/.ssh/config`:
```ssh-config
Host spark
    HostName 10.0.0.61
    User realityrove
    LocalForward 9119 localhost:9119
```
Then: `ssh -fN spark`

## Dashboard CLI Options

| Flag | Purpose |
|------|---------|
| `--host ADDR` | Bind address (default `127.0.0.1`) |
| `--port N` | Port (default `9119`) |
| `--insecure` | Allow non-loopback binding without OAuth gate |
| `--no-open` | Don't auto-open browser |
| `--tui` | Enable embedded Chat tab (in-session via PTY) |
| `--skip-build` | Skip `npm run build` step (requires pre-built web_dist) |
| `--stop` | Stop all running dashboard processes |
| `--status` | List running dashboard processes |

## Dashboard Config (config.yaml)

```yaml
dashboard:
  theme: default          # default, midnight, ember, mono, cyberpunk, rose
  show_token_analytics: false
  public_url: ''          # optional: set your public-facing URL for OAuth
  oauth:
    client_id: ''
    portal_url: ''
```

Set via `hermes config set dashboard.theme midnight`.

## Key Pits

### web_dist is in the repo, not installed package (and env var override)
`npm run build` produces files at `~/.hermes/hermes-agent/hermes_cli/web_dist/`. The installed CLI reads from `~/.local/lib/python3.12/site-packages/hermes_cli/web_dist/` — these are **different locations**. The installed copy NEVER ships web assets. Fixes (pick one):
1. **Set the env var** before starting the dashboard (recommended):
   ```bash
   export HERMES_WEB_DIST=~/.hermes/hermes-agent/hermes_cli/web_dist
   python3 -m hermes_cli.main dashboard --host 0.0.0.0 --port 9119 --insecure --no-open
   ```
2. **Symlink** the built dist:
   ```bash
   ln -sfn ~/.hermes/hermes-agent/hermes_cli/web_dist ~/.local/lib/python3.12/site-packages/hermes_cli/web_dist
   ```
3. **Run from repo directory** (the CLI resolves relative to `__file__`):
   ```bash
   cd ~/.hermes/hermes-agent && python3 -m hermes_cli.main dashboard ...
   ```
Without one of these, dashboard starts but serves "Frontend not built" — because `web_server.py` looks for `web_dist/` in its own parent directory.

### --insecure is not default behavior
`--host 0.0.0.0` WITHOUT `--insecure` will FAIL with "no auth providers registered." Either use `--insecure` (trusted LAN only) or SSH tunnel (preferred).

### Default is localhost-only
Dashboard always defaults to `127.0.0.1`. You MUST specify `--host` for any remote access.

### OAuth gate on non-loopback
When bound to non-loopback (`0.0.0.0`) without `--insecure`, the OAuth auth gate engages. It requires at least one `DashboardAuthProvider` plugin (normally `nous` plugin). If unconfigured, the server refuses to start.

## Common URLs

| Interface | URL |
|-----------|-----|
| Loopback (default) | `http://127.0.0.1:9119` |
| All interfaces | `http://0.0.0.0:9119` |
| LAN from remote | `http://<server-ip>:9119` |
| Via SSH tunnel | `http://localhost:9119` |

### Desktop App Remote Connection — DON'T use session tokens

The Desktop app was designed to connect to remote gateways, but this path is fundamentally broken on the current version:

1. **"Save and reconnect" button is completely unresponsive** — it's greyed out and ignores clicks
2. **Session tokens are machine-scoped** — a token extracted on the server won't work from a remote machine even if pasted correctly
3. **The "Test remote" button silently fails** if you give it the wrong URL (e.g., 8080 → SearXNG)

**Use SSH tunneling instead** (it's more secure anyway and always works):

```bash
# On your Mac, one time:
echo -e "Host spark\n    HostName 10.0.0.61\n    User realityrove\n    LocalForward 9119 localhost:9119" >> ~/.ssh/config
ssh -fN spark  # start the tunnel in the background

# Then in Desktop app:
# Gateway type: Remote gateway
# Remote URL: http://localhost:9119
# Session token: leave blank
# Click "Save and reconnect"
```

If SSH tunneling isn't possible (e.g., direct LAN):
1. Confirm dashboard is on `0.0.0.0` with `--insecure`
2. Verify port 9119 specifically — **port 8080 is SearXNG on Spark**
3. Extract a fresh token from your *Mac's* browser (not the server's):
   ```bash
   curl -s http://10.0.0.61:9119/ | grep -o '__HERMES_SESSION_TOKEN__=*** | cut -d'"' -f2
   ```
4. Note: the Desktop app's **gateway buttons must remain clickable** for this workaround to work. If they're greyed out, the Desktop app version is broken for remote connections.
