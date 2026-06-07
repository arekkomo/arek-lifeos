#!/bin/bash
# Quick diagnostic for Hermes provider connectivity issues
# Run after a reboot, SSH reconnect, or "no AI backend" messages

set -e

echo "=== Hermes Provider Diagnostic ==="
echo ""

# 1. Check providers in config
echo "--- providers in config ---"
grep "^providers:" ~/.hermes/config.yaml

# 2. Check Ollama
echo ""
echo "--- Ollama status ---"
if command -v ollama &>/dev/null; then
    ollama list
else
    echo "Ollama binary not found in PATH"
fi

# 3. Check if Ollama API is reachable on localhost
echo ""
echo "--- Ollama API on localhost ---"
curl -s --connect-timeout 3 http://localhost:11434/api/tags | head -2

# 4. Check if Ollama API is reachable on configured IP (if different)
echo ""
echo "--- Custom Ollama base_url ---"
BASE_URL=$(python3 -c "
import yaml
with open('$HOME/.hermes/config.yaml') as f:
    cfg = yaml.safe_load(f)
cp = cfg.get('custom_providers', [])
if cp:
    print(cp[0].get('base_url', 'NONE'))
else:
    print('NO_CUSTOM_PROVIDERS')
" 2>/dev/null || echo "PARSE_ERROR")
if [ "$BASE_URL" != "NONE" ] && [ "$BASE_URL" != "PARSE_ERROR" ]; then
    HOST=$(echo "$BASE_URL" | sed 's|^http[s]*://||' | sed 's|:\d.*||')
    PORT=$(echo "$BASE_URL" | sed 's|.*:||')
    echo "Custom provider IP: $HOST:$PORT"
    curl -s --connect-timeout 3 "http://$HOST:$PORT/api/tags" | head -2
fi

# 5. Check gateway status
echo ""
echo "--- Gateway live status ---"
hermes status 2>/dev/null | grep -A3 "Provider"

# 6. Check security allow_private_urls
echo ""
echo "--- Security settings ---"
grep "allow_private_urls" ~/.hermes/config.yaml

echo ""
echo "=== Done ==="
