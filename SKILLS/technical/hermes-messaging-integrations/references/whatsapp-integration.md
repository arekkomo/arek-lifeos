---
name: whatsapp-integration
domain: technical
version: 1.2
description: Set up and troubleshoot WhatsApp integration with Hermes. Covers bridge configuration, port discovery, allowlist issues, setup modes, and common failures.
updated: 2026-06-01
---

# WhatsApp Integration (Hermes)

> **Status:** Active  
> **Last Updated:** 2026-06-01

## Setup Modes

Hermes WhatsApp supports two modes, chosen during `hermes whatsapp` interactive wizard:

| Mode | Use case | Requires |
|------|----------|----------|
| **Separate bot number** (recommended) | People message the bot directly | Second phone + WhatsApp on a device |
| **Personal number (self-chat)** | You message yourself to talk to the agent | Just your phone + QR scan |

## Configuration

### Config file (`~/.hermes/config.yaml`)
```yaml
whatsapp:
  bridge_path: /home/realityrove/.hermes/hermes-agent/the WhatsApp bridge.js file in the Hermes Agent repo
  bridge_port: <actual_port>       # must match the bridge's actual port
  extra:
    bridge_port: <actual_port>
```

### Environment (`~/.hermes/.env`)
```bash
WHATSAPP_MODE=self-chat
WHATSAPP_ALLOWED_USERS=16047676437,42906790428919
```

### Run interactive setup
```bash
hermes whatsapp
```
Requires TTY -- cannot be piped.

## Port Discovery -- CRITICAL

The WhatsApp bridge determines its own port at runtime -- it is **NOT always 3001**.

### How to find the actual bridge port
```bash
ps aux | grep whatsapp-bridge
```
Look for the node process -- the port is after `--port`:
```
/.../node .../whatsapp-bridge/bridge.js --port 4000 --session /home/.../session --mode self-chat
```

### Fix port mismatch
1. Find the actual bridge port from `ps aux`
2. Update `bridge_port` in `~/.hermes/config.yaml` **both** at the top level and in `extra`
3. Restart gateway: `systemctl --user restart hermes-gateway`

### Important
The bridge runs **per-user** -- if another Linux user is also running Hermes, their bridge may be on a different port. Each user's bridge is independent. The config's `bridge_port` must match the actual port your bridge claims in `ps aux`.

## Setup Wizard Path Bug -- CRITICAL

The `hermes whatsapp` interactive wizard **hardcodes** its own path check instead of reading `bridge_path` from your config:
```
✗ Bridge script not found at /home/realityrove/.local/lib/python3.12/site-packages/the WhatsApp bridge.js file in the Hermes Agent repo
```

**This is a known bug in the setup wizard -- NOT your actual config.**

**Fix:** Create a symlink so the wizard's hardcoded path points to your real bridge:
```bash
mkdir -p /home/realityrove/.local/lib/python3.12/site-packages/scripts
ln -s /home/realityrove/.hermes/hermes-agent/the WhatsApp bridge directory in the Hermes Agent repo /home/realityrove/.local/lib/python3.12/site-packages/the WhatsApp bridge directory in the Hermes Agent repo
```
Then re-run `hermes whatsapp`. After pairing, **your config is already correct** -- the symlink is only needed for the setup wizard.

## Allowlist Troubleshooting -- CRITICAL

The bridge **silently drops** messages from unlisted numbers. This is the #1 cause of "WhatsApp seems broken" -- bridge connects successfully but messages never arrive at Hermes.

### How to identify
Check the bridge log:
```bash
cat ~/.hermes/whatsapp/bridge.log
```
If you see repeating:
```
{"event":"ignored","reason":"allowlist_mismatch","chatId":"XXXXXX@lid"}
```
The sender number is NOT in `WHATSAPP_ALLOWED_USERS`.

### How to fix
1. **Get the sender number** from `allowlist_mismatch` entries in `bridge.log`
2. **Update `.env`:**
```bash
# Add the sender number to the existing list
WHATSAPP_ALLOWED_USERS=16047676437,42906790428919
```
3. **Restart gateway** after updating (changes don't apply live)

### Pitfall: Sender != phone number
The sender (from bridge logs) may use a different format than the configured number. Use the exact sender ID from bridge logs, not the phone number you set up with.

### Verify
After fixing, check bridge.log for new messages being accepted (no more `allowlist_mismatch` entries).

## Credential Storage

- **Config:** `~/.hermes/config.yaml` -- bridge path & port only (no auth)
- **Credentials:** `~/.hermes/.env` -- MODE, allowed users, etc.
- **Session data:** `~/.hermes/whatsapp/session/` -- persistent session files
- **Logs:** `~/.hermes/whatsapp/bridge.log` -- connection state & ignored messages

## Restarting After Configuration Changes

```bash
systemctl --user restart hermes-gateway
```

## Troubleshooting

### Check bridge status
```bash
cat ~/.hermes/whatsapp/bridge.log | grep -E "connected|connecting|closed"
```

### Check if bridge is running
```bash
ps aux | grep whatsapp-bridge
```

### Check Hermes sees WhatsApp as configured
```bash
hermes status | grep WhatsApp
```

### If bridge shows "not configured" in Hermes status
- Verify `~/.hermes/.env` has `WHATSAPP_MODE=` and `WHATSAPP_ALLOWED_USERS=`
- Verify `config.yaml` has `whatsapp:` section with `bridge_port`
- Restart gateway after any change

## Running the bridge process

The WhatsApp bridge is a `node` process. If it's not running, messages won't route even though config is correct.

**Start the bridge (for self-chat mode):**
```bash
node /home/realityrove/.hermes/hermes-agent/the WhatsApp bridge.js file in the Hermes Agent repo \
  --port 4000 \
  --session /home/realityrove/.hermes/whatsapp/session \
  --mode self-chat > /home/realityrove/.hermes/whatsapp/bridge.log 2>&1 &
```

**Change port to match your actual bridge** (find it with `ps aux | grep whatsapp-bridge`).

**Verify it's running:**
```bash
ps aux | grep whatsapp-bridge
```

### Common mistake: port mismatch
Config says `bridge_port: 3001` but bridge is actually on port 4000 -- messages never route.
**Always verify with `ps aux` before assuming.**

### EADDRINUSE crash -- bridge fails on startup
**Symptom:** Bridge log shows `Error: listen EADDRINUSE: address already in use 127.0.0.1:3000`
**Meaning:** Another process (often `next-server` or another bridge) occupies the bridge port.
**Fix:** `fuser 3000/tcp` to find the occupant. Then either stop the occupant or change `bridge_port` in config.yaml. See `references/whatsapp-integration-eaddrinuse-diagnostics.md` for the full diagnostic sequence (pre-flight port check, config-vs-reality verification).

### Gateway managed bridge -- kill-or-die behavior
The WhatsApp platform's `connect()` **always** calls `_kill_port_process()` on the configured port before starting its managed bridge. It does NOT reuse an existing bridge even if one is healthy and connected. If the managed bridge crashes (missing Node modules, permission issues, etc.), the session dies silently.

**Rule:** If you restart/re-pair the WhatsApp bridge manually, also restart the gateway (`systemctl --user restart hermes-gateway`) so it discovers the new bridge. If the gateway's managed bridge keeps dying, kill it manually and start your own bridge process instead (see "Running the bridge process" above).

### Session path mismatch -- CRITICAL
The platform defaults to `~/.hermes/platforms/whatsapp/session` unless `session_path` is explicitly set in `config.yml`. Your credentials are at `~/.hermes/whatsapp/session/creds.json`. If the gateway says "enabled but not paired" despite `creds.json` existing, **the gateway is looking in the wrong directory**.

**Fix:** Add `session_path` to `config.yaml`:
```yaml
whatsapp:
  extra:
    session_path: /home/realityrove/.hermes/whatsapp/session
```

### `hermes gateway restart` destroys the systemd service override
**Symptom:** Gateway crashes after restart with `RuntimeError: Failed to initialize OpenAI client: No module named 'pydantic_core._pydantic_core'` or similar import errors.

**Cause:** `hermes gateway restart` overwrites `~/.config/systemd/user/hermes-gateway.service`, resetting `WorkingDirectory` to the default and wiping any custom `PATH` or `VIRTUAL_ENV` environment variables. If you installed packages for Python 3.12 but the service reverts to Python 3.11 packages, imports fail.

**Fix:** After running `hermes gateway restart`, verify the service file:
```bash
cat ~/.config/systemd/user/hermes-gateway.service | grep WorkingDirectory
```
Must point to the correct environment: `WorkingDirectory=/home/realityrove/.local/lib/python3.12/site-packages` (Python 3.12) OR `WorkingDirectory=/home/realityrove/.local/lib/python3.11/site-packages` (Python 3.11). If wrong, restore the correct WorkingDirectory and reload:
```bash
systemctl --user daemon-reload
```

**Safer alternative:** Use `systemctl --user restart hermes-gateway` if you just want to restart without the service file being overwritten.

### Port mismatch after bridge port change
**Symptom:** Config says `bridge_port: 3000` but bridge is on `8080` -- no error, bridge runs fine but gateway can't connect. Silent failure.
**Fix:** Always verify port with `ps aux | grep whatsapp-bridge` before concluding the bridge is dead.

### Cross-user bridge -- CRITICAL: verify YOUR bridge is running
The WhatsApp bridge runs as a node process **per Linux user**. A different user's bridge (even another Hermes instance) running on the same machine will NOT receive your messages.

**Diagnose:**
```bash
ps aux | grep whatsapp-bridge
```
The process should be under **your user** (e.g., `realityrove`), not root or another user (e.g., `robert`).

**If another user owns the bridge:**
1. Kill it: `sudo kill <PID>`
2. Start your own bridge under your user (see "Running the bridge process" above)

**Starting your bridge:**
```bash
node /home/realityrove/.hermes/hermes-agent/the WhatsApp bridge.js file in the Hermes Agent repo \
  --port <actual_port> \
  --session /home/realityrove/.hermes/whatsapp/session \
  --mode self-chat > /home/realityrove/.hermes/whatsapp/bridge.log 2>&1 &
```

## Troubleshooting: Failed to start bridge

### Symptom
Gateway logs show: `ERROR: [Whatsapp] Failed to start bridge: No module named 'aiohttp'`
Repeated every reconnect cycle. Bridge never comes online.

### Cause
The system Python that the gateway uses (`/usr/bin/python3`) doesn't have `aiohttp` installed. The bridge is a Node.js process -- it starts fine -- but the **Python gateway code that talks to the bridge** crashes on import.

### Fix
```bash
/usr/bin/python3 -m pip install --break-system-packages aiohttp
```
Then restart the gateway:
```bash
systemctl --user restart hermes-gateway
```

### Why it happens
Debian/Ubuntu ships Python without `aiohttp` (PEP 668 externals-managed-environment). `pip install` alone won't work -- need `--break-system-packages` or a venv.

## Session Revocation (device_removed)

**What happens:** Running `hermes whatsapp` again re-pairs the bridge, which sends a `device_removed` event to the *previous* session. The old bridge gets **forced logged out**:
```
❌ Logged out. Delete session and restart to re-authenticate.
```

**Always clean up old sessions first:**
```bash
rm -rf ~/.hermes/whatsapp/session
hermes whatsapp
```

## Additional notes

- **Allowlist mismatches** are the #1 cause of silent failures -- bridge connects but drops messages
- **Cross-user bridges** are independent -- don't confuse another user's bridge config with yours
- **Bridge logs** are the single most useful diagnostic tool -- they show everything
- **EADDRINUSE and port occupancy** has a dedicated guide in `references/whatsapp-integration-eaddrinuse-diagnostics.md`
