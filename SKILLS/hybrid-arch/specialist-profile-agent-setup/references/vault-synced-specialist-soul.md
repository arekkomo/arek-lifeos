# Vault-synced specialist SOUL.md pattern

Use this when building a dedicated Arek & Co specialist profile whose identity/instructions live in the Obsidian vault.

## Source-resolution pattern

1. Start with the specialist's vault folder, usually:

```text
/home/realityrove/Obsidian/Arek&Co/AGENTS/<Specialist>/
```

2. Do not assume `Brief.md` is the full instruction source. It may be a stub that points elsewhere.

3. Prefer the most operational files in this order when present:

```text
AGENTS/<Specialist>/CoWork-Instructions-LIVE.md
AGENTS/<Specialist>/CoWork-Instructions.md
AGENTS/<Specialist>/Brief.md
AGENTS/<Specialist>/Task-Management.md
AGENTS/<Specialist>/Technical-Setup/*.md
AGENTS/<Specialist>/memory/MEMORY.md
AGENTS/<Specialist>/memory/*.md
SKILLS/ files matching the specialist prefix, e.g. SK-SY-* for System
ABOUT-YOU/About-Me-General.md when the specialist needs stable user context
```

4. Quote vault paths in shell commands because `Arek&Co` contains `&`:

```bash
'/home/realityrove/Obsidian/Arek&Co/AGENTS/System/CoWork-Instructions.md'
```

## What to embed vs reference

Embed compact, always-needed instructions in `~/.hermes/profiles/<name>/SOUL.md`:

- identity and domain ownership
- mandate/responsibilities
- response style and prefix
- boundaries/handoff rules to other agents
- source-of-truth vault path and primary files
- tool discipline for simple greetings/check-ins
- key durable technical or operational context

Reference, but do not fully paste, bulky or changing material:

- long memory project logs
- monthly reports
- inventories that may change often
- detailed skill libraries
- raw transcripts or immutable `raw/` material

If deeper context is needed later, create a compact profile context file or skill reference rather than bloating `SOUL.md`.

## Verification

After writing `SOUL.md`, restart the specialist gateway and run a profile-local behavior test:

```bash
systemctl --user restart hermes-gateway-<name>
sleep 3
hermes --profile <name> gateway status
hermes --profile <name> chat -q 'Who are you and what are your source-of-truth files?' --quiet
```

Expected: the agent uses the specialist prefix, describes its domain, and names the vault source files. For a simple `hi`, expected behavior is a short direct reply with no tool use.

## Reporting status to Arek

Be precise:

- "Core instructions are ingested into the profile SOUL.md" means the always-loaded identity/mandate is synced.
- "Every vault file is embedded" is usually false and undesirable.
- Say which files were read/summarized and which optional files remain for deeper sync.
