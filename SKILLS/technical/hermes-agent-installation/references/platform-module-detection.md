# Platform Module Discovery Path Bug

## The Bug

When hermes-agent is installed as an editable package (`pip install -e`), the gateway's WhatsApp platform code discovers the bridge path from the editable install's source directory, **not** from `config.yaml`.

### Session Evidence

```
22:42:01 INFO gateway.platforms.whatsapp: [Whatsapp] Bridge found at /tmp/hermes-agent-src/the WhatsApp bridge.js file in the Hermes Agent repo
```

The gateway was reading the bridge path from the git temp clone (`/tmp/hermes-agent-src/`) instead of the user's configured path (`/home/realityrove/.hermes/hermes-agent/the WhatsApp bridge.js file in the Hermes Agent repo`).

## Root Cause

The editable install's `__editable__*.pth` finder redirects all `hermes_agent` package imports to the source directory, including the platform adapter code. This means `platforms/whatsapp.py` inside the gateway package resolves to the editable source, not the installed copy.

## Fix Pattern

When fixing hermes-agent installations, always:
1. Uninstall first: `pip uninstall hermes-agent -y --break-system-packages`
2. Remove all editable artifacts (pth files, finder modules, pyc cache)
3. Verify no `__editable__` files remain
4. Install fresh wheel: `pip install --break-system-packages .[messaging]`

After cleanup, the gateway will discover the correct bridge path from `config.yaml`.
