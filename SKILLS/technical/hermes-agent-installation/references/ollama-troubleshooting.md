---
name: ollama-troubleshooting
description: "Diagnose and fix Ollama issues: model loading, endpoint connectivity, provider errors, generation timeouts, and integration with Hermes Agent."
category: devops
---

# Ollama Troubleshooting

Diagnose and fix Ollama integration with Hermes Agent — model loading, provider configuration, endpoint connectivity, and generation issues.

## Quick Diagnose

```bash
# 1. Check Ollama is running and models loaded
curl -s http://localhost:11434/api/tags | python -m json.tool
# or remote endpoint:
curl -s http://10.0.0.15:11434/api/tags | python -m json.tool

# 2. Test generate with a minimal prompt (not stream)
curl -s -d '{"model":"qwen3.6:latest","prompt":"Say hello","stream":false}' http://localhost:11434/api/generate

# 3. Check Hermes doctor
hermes doctor

# 4. Check gateway logs
grep -E "error|fail|timeout|provider" ~/.hermes/logs/gateway.log | tail -15
```

## Common Issues

### Provider says "no AI backend"

1. Check gateway has restarted since config changes (`hermes doctor` shows config state)
2. Verify Ollama is running: `curl -s http://10.0.0.15:11434/api/tags`
3. Check `config.yaml` has the correct `providers:` entry matching `custom_providers` names
4. **Gateway caches config** — if you changed config but didn't restart the gateway, old state persists

### Ollama tags works but generate times out

- A 15s timeout on generate often means the model is evicted from VRAM or the endpoint is overloaded
- Fix: reload the model:
  ```bash
  ollama pull qwen3.6:latest
  # or
  ollama run qwen3.6:latest "hi"  # keeps it loaded
  ```
- Check model size vs GPU memory: large models (36B+) may evict under memory pressure

### Model not showing in /tags

```bash
# List all models
ollama list

# Pull a specific model
ollama pull qwen3.6:latest
```

### Provider not loading despite config

The `providers:` array in `config.yaml` must list each provider by name (matching `custom_providers[].name`):
```yaml
providers:
- Ollama
```

**This is read at gateway startup time.** If `providers` is empty `{}`, no provider loads — even with `custom_providers` defined. After adding, `/restart` the gateway.

### Wrong model configured

Check and update:
```yaml
custom_providers:
- name: Ollama
  base_url: http://IP:11434/v1
  model: qwen3.6:latest
```

## Integration Checklist

- [ ] Ollama accessible at configured base_url
- [ ] Model loaded in `/tags` response
- [ ] `providers:` array in `config.yaml` includes the custom provider name
- [ ] Gateway restarted after changes
- [ ] Model responds to `/api/generate` with a simple prompt
- [ ] Hermes `providers:` (top-level) reflects active providers

## Support Files

- `references/ollama-troubleshooting-hermes-model-recommendations.md` — Bookmark to YouTube video covering which models are best for which Hermes tasks (URL only, extract when Ollama generate works)

## Reference: Provider Names

Custom provider names go in TWO places:
1. `custom_providers[].name` — the identifier
2. `providers: [...]` — list of active providers

These must match. Example:

```yaml
providers:
- Ollama
custom_providers:
- name: Ollama      ← same name
  base_url: http://10.0.0.15:11434/v1
  model: qwen3.6:latest
```
