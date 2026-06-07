# Security Scanner Blocking Private IPs

## Problem
Hermes security scanner blocks `curl`/`urllib.request`/any external call to private network IPs (10.x.x.x, 192.168.x.x, 172.16-31.x.x) by default, reporting: [MEDIUM] URL uses raw IP address, [HIGH] Private network access.

## Detection
When running commands that access your local-network Ollama server or other local services, you may see:
- Command Approval Required prompt for security scan
- `curl` calls silently blocked without output
- Discord app shows "No AI backend" even though the model server is running

## Fix
```bash
hermes config set security.allow_private_urls true
```

Verify:
```bash
hermes config show | tail -5
# or
grep allow_private_urls ~/.hermes/config.yaml
```

## Also check
- `allow_private_urls` can appear in multiple config sections. The `security:` section is the one that matters for the scanner.
- `model_catalog.providers: {}` is separate — don't confuse with `security.allow_private_urls`
- Browser config also has `auto_local_for_private_urls: true` by default but that's unrelated

## When to leave it false
If you have untrusted user input that gets passed to `curl`/`requests`, keep it false. Set to true only when you control the endpoints.
