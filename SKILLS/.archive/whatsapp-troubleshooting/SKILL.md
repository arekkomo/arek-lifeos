---
name: whatsapp-troubleshooting
description: "Diagnose and fix WhatsApp bridge connection failures in Hermes Agent. Covers port conflicts, bridge startup failures, session expiry, and platform-specific setup issues."
---

# WhatsApp Bridge Troubleshooting

Hermes Agent's WhatsApp integration runs a Node.js bridge process that acts as a middleman between the gateway and WhatsApp Web. When WhatsApp fails to connect, it's almost always due to one of three categories: port conflict, missing bridge process, or stale session.

## Diagnose First — Run This Checklist

```bash
# 1. Is the bridge actually running?
ps aux | grep whatsapp-bridge | grep -v grep

# 2. What port is it on?
ps aux | grep "bridge.js --port" | grep -v grep

# 3. Is the gateway trying the right port?
grep bridge_port ~/.hermes/config.yaml

# 4. Is something else on the gateway's target port?
ss -tlnp | awk '{print $4}' | grep <port>

# 5. Does the bridge respond?
curl -s http://127.0.0.1:<bridge_port>/health
```

**Expected healthy state:**
- Bridge running with `--port 3000` (default) or your custom port
- `localhost:<port>/health` returns `{}`
- Config `bridge_port` matches the actual bridge port
- No other process bound to the same port

## Common Failures & Fixes

### 1. Port collision — most common
Bridge defaults to **port 3000**. Common apps on 3000:
- Local dev servers (Next.js, Node, Docker)
- Any other web apps you're running

**Fix:** Either set `whatsapp.bridge_port` in config.yaml, or move the conflicting app:

```yaml
whatsapp:
  bridge_port: 4000  # pick an available port
```

Then restart: `hermes gateway restart`

### 2. Bridge process never started
Gateway finds `bridge.js` but can't launch it:
- `node` installed? (`which node`, `node --version`)
- Bridge directory exists? (`ls ~/.local/lib/python3.12/site-packages/scripts/whatsapp-bridge/bridge.js`)
- Bridge log errors? (`cat ~/.hermes/logs/bridge.log | tail -30`)

### 3. Stale/expired bridge session
WhatsApp Web sessions expire ~30 days or on device logout:

```bash
rm -f ~/.hermes/whatsapp/session/*.json
hermes gateway setup  # fresh QR code
```

Scan the QR, then **confirm on the phone** when prompted ("Use WhatsApp on [device]").

### 4. Multi-user confusion
On shared servers, each user's WhatsApp bridge runs under their own user account. Another user's bridge doesn't help your gateway. Always `ps aux | grep bridge` under the correct user.

### 5. No reply when messaging the bot
- Send the message **TO the bot's WhatsApp number** (not "to yourself" — that's your own account)
- Verify yourself is in the `whatsapp.allowed_users` config
- Check the bridge shows as **connected** in logs, not just "bridge found"

## Log Locations

| Log | Purpose |
|-----|---|
| `~/.hermes/logs/gateway.log` | Connection attempts |
| `~/.hermes/logs/bridge.log` | Bridge internals |
| `systemctl --user status hermes-gateway` | Service health |
