# EADDRINUSE and Port Occupancy Diagnostics

When the WhatsApp bridge crashes on startup with EADDRINUSE, it means another process already has the intended port.

## EADDRINUSE Crash Pattern

```
Error: listen EADDRINUSE: address already in use 127.0.0.1:3000
```

**Common causes:**
1. **next-server** (Next.js) often binds to 3000
2. **Another WhatsApp bridge** running on the same port
3. **Previous bridge instance** that didn't fully exit
4. **Old config** still targeting a port you changed

## Diagnostic Sequence

### Step 1: Find what occupies the port
```bash
fuser 3000/tcp
# or
ss -tlnp | grep 3000
```

### Step 2: Check all bridge instances
```bash
ps aux | grep whatsapp-bridge | grep -v grep
```
Look for bridges owned by different users. Each user needs their own bridge on their own port.

### Step 3: Verify config matches reality
Check `~/.hermes/config.yaml` for the expected bridge_port, then confirm with `ps aux`:
```bash
# Expected port (from config)
grep bridge_port ~/.hermes/config.yaml
# Actual port (from running process)
ps aux | grep whatsapp-bridge | grep -v grep
```
If they differ, update config.yaml to match the actual port, then restart.

### Step 4: Fix the occupant
If it is your bridge on the wrong port:
```bash
# Kill old bridge
kill <old_bridge_pid>
# Start on correct port
node /home/realityrove/.hermes/hermes-agent/scripts/whatsapp-bridge/bridge.js \
  --port <correct_port> \
  --session /home/realityrove/.hermes/whatsapp/session \
  --mode self-chat > /home/realityrove/.hermes/whatsapp/bridge.log 2>&1 &
```

If it is next-server or another process:
- Stop it: `kill <pid>`
- Or change your bridge_port in config.yaml to an unused port

## Pre-flight Check (always do before starting)

```bash
ss -tlnp | grep -E '3000|4000'  # check common bridge ports
ps aux | grep whatsapp-bridge | grep -v grep  # check for existing bridges
```

This prevents the crash cycle of "start -> crash on EADDRINUSE -> fix port -> repeat".
