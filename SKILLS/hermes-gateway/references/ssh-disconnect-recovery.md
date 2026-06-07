## Session-Specific Case: 2026-06-01 SSH Disconnect Recovery

### What happened
- User had long SSH session, computer went to sleep
- SSH disconnected, gateway restarted
- Next session: Ollama was running and reachable (confirmed with curl)
- Hermes gateway had `providers: {}` (empty) — no active provider
- Discord bot token was expired/invalid (needs rotation)
- Security scanner blocked `10.0.0.15` (Ollama's IP) via SSRF protection

### Root cause chain
1. SSH disconnect → gateway restart → `providers` section cleared to `{}`
2. `custom_providers` still had Ollama defined but not loaded
3. Security scanner blocked private IP `10.0.0.15` (model_catalog.providers had empty dict, security.allow_private_urls was false)
4. Discord had old expired token → bot couldn't re-auth → health check showed "no AI backend"

### Key findings
- `providers` (loaded providers) and `custom_providers` (defined providers) are separate — both must be set
- `security.allow_private_urls` defaults to `false` even for trusted local-network endpoints
- Gateway health checks can lag — `hermes status` is the authoritative live check
- Ollama at `10.x.x.x` IPs are blocked by security scanner even when running from the same LAN

### Verification commands that worked
```bash
# 1. Ollama reachable?
curl -s http://10.0.0.15:11434/api/tags | head -5

# 2. Gateway sees provider?
hermes status | grep -A3 "Provider"

# 3. Providers in config?
grep "^providers:" ~/.hermes/config.yaml

# 4. Security allow_private_urls?
grep "allow_private_urls" ~/.hermes/config.yaml
```

### Fixes applied
```bash
# 1. Add providers to config
hermes config set providers '["Ollama"]'
# Verify YAML format: line should show providers: ["Ollama"] not providers: '["Ollama"]'

# 2. Update Discord bot token
# (new token provided by user, written to ~/.hermes/.env)

# 3. Restart gateway
systemctl --user restart hermes-gateway

# 4. Verify
hermes status
hermes gateway status
```
