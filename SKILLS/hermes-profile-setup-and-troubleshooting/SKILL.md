---
name: hermes-profile-setup-and-troubleshooting
description: "Profile-level operations for Hermes Agent — setup patterns, gateway health, platform config cleanup, and skill management conventions."
version: 1.0.0
author: "Arek & Co. Agent Team"
---

# Hermes Profile Setup & Troubleshooting

## New Profile Setup Checklist

When standing up a new specialist (Systems, Connector, etc.) — do all of these, in order:

1. **Ingest SOUL.md from vault sources** — `AGENTS/` area for the specialist's domain. Copy relevant files into `SOUL.md` of the profile's home directory.
2. **Verify `config.yaml` platform settings** — specialist profiles should be **Telegram-only** unless there's a deliberate need for Discord or WhatsApp (those platforms belong on the default/main profile). This avoids credential conflicts and gateway health noise.
3. **Restart gateway service:**

```bash
systemctl --user restart hermes-<profile>
```

4. **Verify service is running:**

```bash
hermes --profile <name> gateway status
```

5. **Sanity ping to confirm the profile responds:**

```bash
hermes --profile <name> chat -q 'ping' --quiet
# expects: "<profile_name>:\n\npong"
```

6. **Clear stale runtime warnings if any** (see below).

## 🚨 Stale Gateway Runtime Status — Critical Pitfall

This is the #1 cause of misleading `hermes gateway status` output.

The gateway writes `gateway_state.json` in the profile's home directory. When a platform hits a **fatal** error once, the JSON records `"state": "fatal"`. Fixing the config **does not clear this** — the stale value persists across restarts until you manually remove it.

**Symptom:** Gateway status shows warnings like "⚠ discord: Discord bot token already in use" even though Discord is disabled in `config.yaml`.

**Diagnostic:**

```bash
cat ~/.hermes/profiles/<name>/gateway_state.json | jq .platforms
# Look for "state": "fatal" entries
```

**Fix — remove stale platform states (recommended):**

```python
python3 <<'PY'
import json
from pathlib import Path
p = Path(f'/home/realityrove/.hermes/profiles/{name}/gateway_state.json')
data = json.loads(p.read_text())
data['platforms'] = {k: v for k, v in data.get('platforms', {}).items() if v.get('state') != 'fatal'}
p.write_text(json.dumps(data))
PY
```

**Alternative — delete the file entirely:**

```bash
rm ~/.hermes/profiles/<name>/gateway_state.json
systemctl --user restart hermes-<profile>
```

## Profile-Local Skills Convention

Central skills live at `~/.hermes/skills/` and serve ALL profiles automatically.
Profile-local skills (`~/.hermes/profiles/<name>/skills/`) are ONLY for version-isolated copies that differ from the central version.

**Rule:** Profile-local skills that are identical to central should be removed. Duplicates are maintenance debt, disk waste, and cause confusion about which copy actually loads.

**Cleanup pattern:**

```bash
python3 <<'PY'
from pathlib import Path
import shutil
central = Path('/home/realityrove/.hermes/skills')
profile = Path(f'/home/realityrove/.hermes/profiles/{name}/skills')
for sk in profile.rglob('SKILL.md'):
    central_f = list(central.rglob(f'{sk.parent.name}/SKILL.md'))
    if central_f and central_f[0].read_text() == sk.read_text():
        print(f'REMOVE: {sk.parent.name} (identical to central)')
        shutil.rmtree(sk.parent)
PY
```

**After cleanup:**
1. Remove duplicate SKILL.md directories
2. Clean up empty parent directories
3. Review `config.yaml` `skills:` list section — remove any entries that referenced deleted skills (names may include prefixes like `hybrid-arch:coach-specialist`)
4. Profile will now load skills from central automatically for discovery

### Identifying duplicates before deletion

Before removing anything, compare:

```python
python3 <<'PY'
from pathlib import Path
central = Path('/home/realityrove/.hermes/skills')
profile = Path(f'/home/realityrove/.hermes/profiles/{name}/skills')
duplicates = []
for sk in profile.rglob('SKILL.md'):
    central_f = list(central.rglob(f'{sk.parent.name}/SKILL.md'))
    if central_f and central_f[0].read_text() == sk.read_text():
        duplicates.append(sk.parent.name)
print(f'Found {len(duplicates)} duplicates: {duplicates}')
PY
```

## Quick Diagnosis

### Gateway Won't Start / Fails Silently
1. Check if gateway is already running: `pgrep -fa hermes.*<profile>`
2. Kill old process then restart: `hermes gateway start --profile <name>`
3. For systemctl service: `systemctl --user status hermes-<profile>`

### MCP Servers Fail to Connect
Check profile's `.env` for required tokens (e.g. `NOTION_MCP_TOKEN`)
Check `config.yaml` in `mcp_servers` section — verify URL, auth format, transport

### Skills Not Loading
1. `hermes skills list` — verify installed
2. Check profile `config.yaml` `skills:` section lists them
3. `/reload-skills` in session or restart gateway
4. If skills live in the Obsidian vault, the symlink at `~/.hermes/skills` must resolve correctly — verify with readlink.

### Model/Provider Issues
1. `hermes doctor` — check config and dependencies
2. `hermes auth` — re-authenticate OAuth providers
3. Check `.env` has correct API keys

## Vault-Backed Skills Mirror Pattern

When skills live in the Obsidian vault (`Obsidian/Arek&Co/SKILLS/`), **do not change profile config**. Instead, replace the default `~/.hermes/skills/` directory with a symlink to the vault path. All profiles automatically read from the vault because they use the default skills path — no config changes needed.

**Procedure:**

1. **Copy all skills to `Vault/SKILLS/`** (not individual `.md` files at top level):
   ```bash
   rsync -a /home/realityrove/.hermes/skills/ "/home/realityrove/Obsidian/Arek&Co/SKILLS/"
   ```

2. **Back up the old skills dir:**
   ```bash
   mv /home/realityrove/.hermes/skills /home/realityrove/.hermes/skills.backup_20260606
   ```

3. **Create symlink using Python (NOT bash) to avoid bash interpreting `&` as a background operator:**
   ```python
   import os, shutil
   path = "/home/realityrove/.hermes/skills"
   shutil.rmtree(path) if os.path.isdir(path) else None
   os.readlink(path) and os.unlink(path) if os.path.islink(path) else None
   os.symlink("/home/realityrove/Obsidian/Arek&Co/SKILLS", path)
   ```

4. **Verify:**
   ```python
   import os
   os.path.islink("/home/realityrove/.hermes/skills")  # True
   os.readlink("/home/realityrove/.hermes/skills")     # /home/realityrove/Obsidian/Arek&Co/SKILLS
   os.path.exists("/home/realityrove/.hermes/skills")  # True
   ```

5. **Commit to vault:**
   ```bash
   cd /home/realityrove/Obsidian/Arek&Co
   git add SKILLS/
   git commit -m 'Add SKILLS/ - all skills to vault'
   ```

**Key pitfalls:**
- **Never use bash `ln -s` on paths containing `&`** — bash interprets `&` as background operator, which silently breaks the symlink. Always use Python `os.symlink()`.
- **Ensure vault SKILLS/ has proper directory structure** (category dirs with SKILL.md inside), not individual `.md` files at the top level. Clean up any stray `.md` or `._` files that rsync brings in.
- **All profiles read from `~/.hermes/skills/` by default** — no `skills_directory` override needed. Adding one would break the mirror.
- After migration, verify each profile config does NOT have `skills_directory` pointing elsewhere.