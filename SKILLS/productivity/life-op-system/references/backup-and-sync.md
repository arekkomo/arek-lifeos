---
name: backup-and-sync
domain: system
version: 1.0
description: Set up and maintain automated backup/sync for the Arek&Co Life OS — Obsidian vault and .hermes config. Covers script creation, cron scheduling, vault state checks, and push-to-git.
updated: 2026-06-03
---

# Backup & Sync — Arek&Co Life OS

## Target Repositories

| Item | Local path | Remote | Branch |
|------|-----------|--------|--------|
| **Obsidian vault** | `~/Obsidian/Arek&Co/` | `https://github.com/arekkomo/arek-lifeos.git` | main |
| **.hermes config** | `~/.hermes/` | same `arek-lifeos` repo (subfolder) | main |

## Backup Workflow

### 1. Check vault state
```bash
cd ~/Obsidian/Arek\&Co
git log --oneline -3
git status --short
```

### 2. Check .hermes state
```bash
cd ~/.hermes
git log --oneline -3
git status --short
```

### 3. Commit and push uncommitted changes

**For the vault:**
```bash
cd ~/Obsidian/Arek\&Co
git add -A
git commit -m "Backup: $(date +%Y-%m-%d)"
git push origin main
```

**For .hermes:**
```bash
cd ~/.hermes
git add -A
git commit -m "Backup: $(date +%Y-%d)"
git push origin main
```

### 4. Create the backup cron job (if none exists)

```bash
hermes cron job create --name 'backup-arek-co' --schedule 'daily 2:00' \
  --prompt 'Run backup-and-sync: check and commit+push both vault and .hermes' \
  --skill backup-and-sync
```

## Pitfalls

- **No backup script exists by default.** You must create one; there's no pre-existing cron job or sync script.
- **The vault may have uncommitted changes.** Always `git status` before assuming sync status.
- **Both repos use `main` branch.** Don't create separate branches for backup — just commit on main.
- **The vault has 720+ files.** `git add -A` works fine but may be slow on first run.
- **`.hermes` includes node_modules.** Exclude those in `.gitignore` to keep the repo small.

## Verification

Running the backup should:
1. Find zero or few uncommitted files (most should be committed already)
2. Complete a commit+push in under 10 seconds
3. Report which files were changed
4. Return success exit code 0

## Session-Specific Notes

See `references/backup-and-sync-backup-state-2026-06-03.md` for the state discovered today.
