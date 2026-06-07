# execute_code Tool Corruption Pitfall

## Problem
The `execute_code` tool consistently corrupts Python string literals containing:
- Long strings with mixed dots, alphanumerics (e.g., API keys, tokens, UUIDs)
- Mixed case + dots + numbers in sequence
- Certain character combinations involving `...` patterns

## Symptoms
- Python SyntaxError: unterminated string literal
- Values truncated mid-string
- Characters dropped or mangled

## Workaround
When `execute_code` corrupts your strings multiple times (3+ failures), switch to:

1. **bash heredoc** for scripts:
   ```bash
   cat << 'ENDSCRIPT' > /tmp/script.py
   #!/usr/bin/env python3
   ... your full script ...
   ENDSCRIPT
   python3 /tmp/script.py
   ```

2. **hermes CLI commands** for config/secrets:
   - `hermes config set <key> <value>` for config.yaml values
   - `hermes config set discord_bot_token '<token>'` for .env secrets

3. **write_file** for creating script files (less aggressive mangling than execute_code)

## Detection
After using `hermes config set` for long values, always verify by checking line length:
```bash
grep "^DISCORD_BOT_TOKEN" ~/.hermes/.env | wc -c
```
Compare against expected length — if short, the write was truncated.
