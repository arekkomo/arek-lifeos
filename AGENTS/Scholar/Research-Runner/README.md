# Scholar Research Runner — Phase 1

## Status

**Verified 2026-07-19.** This is an isolated Last30Days-based runner for narrow, source-attributed research. It is not installed as a Hermes skill and does not grant Scholar shell, filesystem, browser, cookie, or credential access.

Pinned upstream source:

- Repository: `https://github.com/mvanhorn/last30days-skill`
- Base commit: `249c7a4c040558a903d6838dee31012980d4946d`
- Local safety patch: `vendor/last30days-skill/skills/last30days/scripts/lib/pipeline.py` preserves `EXCLUDE_SOURCES=jobs` when upstream auto-adds jobs for company-like topics. This patch is required for the Phase 1 allowlist boundary.

## Phase 1 security boundary

The wrapper (`phase1_research.py`) does not invoke the upstream setup wizard and starts the engine with a sanitized environment:

- dedicated empty `HOME` and `XDG_CONFIG_HOME` under this runner;
- dedicated empty `PATH`, preventing `gh auth token`, `pass`, and ambient optional CLIs;
- no inherited API keys, session tokens, browser profiles, or existing Last30Days configuration;
- an explicit source allowlist and exclusions.

Hard-disabled:

- Reddit and all Reddit collection methods
- X/Twitter and Truth Social
- Browser cookie extraction (`FROM_BROWSER=off`)
- YouTube, TikTok, Instagram, Bluesky, Threads, Pinterest, LinkedIn
- Trustpilot, ScrapeCreators, Perplexity, DripStack, StockTwits
- Private/local corpus retrieval
- Ambient API keys and tokens
- Upstream automatic setup and automatic package installation

Allowed source set:

- GitHub
- Hacker News
- Polymarket
- Digg, arXiv, Techmeme, and keyless web grounding only when their reviewed local adapters are available

## Current verified availability

| Source | Status | Notes |
|---|---|---|
| GitHub | Active | Uses unauthenticated REST; lower rate limits and no comment enrichment |
| Hacker News | Active | No relevant result in the ComfyUI verification run |
| Polymarket | Active | No relevant market in the ComfyUI verification run |
| Web grounding | Active | No result in the ComfyUI verification run |
| Digg / arXiv / Techmeme | Not active | The pinned Printing Press installer requires Go, which is not installed. No Go or CLI package was installed. |
| Reddit / X / all cookie-backed sources | Disabled by design | Requires a later explicit policy/security decision |

## Usage

Scholar (or the calling agent) must generate a concise JSON query plan. The runner requires it rather than using the upstream engine's low-quality deterministic fallback.

```bash
python3 AGENTS/Scholar/Research-Runner/phase1_research.py \
  "ComfyUI development and workflow ecosystem" \
  --plan-file AGENTS/Scholar/Research-Runner/plans/comfyui-phase1.json \
  --github-repo Comfy-Org/ComfyUI
```

Outputs are stored in `runs/`. Treat every report as **partial coverage** unless its `source_status` confirms the expected sources completed successfully.

## Verification artifact

- `runs/phase1-comfyui-verified.json`
- Window: 30 days ending 2026-07-19
- Result: 13 GitHub items from the ComfyUI ecosystem
- Examples observed: model reload/memory issues, INT8-ConvRot support and A100 performance reports, LoRA support, Krea 2, and TRELLIS2/Pixal3D work.

## Known limitations

1. This does not provide Reddit coverage or an exhaustive social-discussion digest.
2. GitHub is currently unauthenticated and must stay rate-limited.
3. The runner is not yet exposed to Scholar through a constrained Hermes tool; it is a verified standalone component only.
4. Installing Go would enable the pinned Digg/arXiv/Techmeme adapters, but that is a separate approval gate.
5. Phase 2, if approved, should use a dedicated research-only X account on Spark. Never use a personal browser profile.
