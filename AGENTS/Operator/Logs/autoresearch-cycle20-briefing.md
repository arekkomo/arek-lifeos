# Autonomous Research Briefing — Cycle 20 (2026-07-05)

## Scan Status

| Source | Status | Notes |
|--------|--------|-------|
| arXiv API (cs.CV/ML video) | ✅ Done | 5 items from feed; all already in vault |
| PyTorch blog RSS | ⚠️ Partial | Feed returned HTML redirect, not clean XML |
| HuggingFace RSS | ❌ 404 | SPA page, no real RSS endpoint |
| Google Developer Blog | ✅ Done | Content extracted from cached pages |
| ComfyUI Releases (GitHub) | ✅ Done | v0.24–v0.27 captured |
| ComfyUI Video Nodes (GitHub) | ✅ Done | 10 repos scanned by recency |
| n8n Automation Repos | ⚠️ Sparse | Search returned generic results |

## arXiv Findings — Cycle 20

**Result: 0 new filings.** All items from the RSS feed window (2607.02517, 2607.02516, 2607.02515, 2607.02508) were already captured in cycles 17–19 and present in the vault index:

| Paper | Vault Status |
|-------|-------------|
| WorldDirector (2607.02517) | ✅ In index line 51 |
| Align4D (2607.02516) | ✅ In AI-3D section, line 125 |
| PointDiT (2607.02515) | ✅ In AI-3D section, line 126 |
| From SRA to Self-Flow (2607.02508) | ✅ Filed cycle 17, line 49 |

## ComfyUI Release Notes — New Since v0.27 Entry

The vault index mentions v0.27 briefly. Here's what we're missing from **v0.24–v0.26** that may warrant enrichment:

### v0.25.1 (2026-06-18)
- **Kling V3-Turbo support** — New model tier for Kling video generation via Partner Nodes. Relevant since we track Kling workflows in AI-Video.

### v0.25.0 (2026-06-16)
- **WEBM alpha channel save** — `SaveWEBM` node now supports transparent backgrounds. Direct VFX compositing impact.
- **Bria Green Background node** — One-click green screen via Partner Node API. Cuts down rotoscoping steps.
- **Krea 2 Medium Turbo model** — Additional resolution tier in Krea pipeline.
- **Seedance 2.0 fix** — Resolved 1080p first/last-frame stretch jump issue.

### v0.24.0 (2026-06-03)
- **Tripo + DINOv3 fixes** — Triposplat preview and dtype corrections. Relevant for AI-3D workflows.
- **Radiance variant support** — `txt_ids` now works with nonzero values, enabling more flexible text conditioning in Radiance model node.

## New ComfyUI Custom Nodes (Recent GitHub Activity)

| Repository | Stars | Focus | Relevance |
|-----------|-------|-------|-----------|
| **Danisxxx/comfyUI-LongLook** | 1 | Smooth motion for 81+ frame Wan 2.2 generations | ⭐ HIGH — Direct Wan 2.2 workflow enhancement |
| **digital-garbage/ComfyUI-FunPack** | 16 | Non-linear video editing and generation via Comfy backend | ⭐ HIGH — Video editing workflow |
| **romanhacks/comfyui-wan-i2v-control** | 2 | Targeted character/scene adjustments in WAN I2V | ⭐ HIGH — Wan image-to-video control |
| **Ponlawat/ComfyUI-LTXVideo** | 1 | Custom nodes for LTX-2 video model | MEDIUM — Redundant since we track core [[LTX-Video]] |
| **PurpleDoubleD/locally-uncensored** | 853 | Local offline AI desktop (chat + ComfyUI bundling) | LOW — Distribution wrapper, not node logic |

## Candidate: ComfyUI-FunPack (16 stars)

This is the most notable new entry. Non-linear video editing in ComfyUI bridges a gap between raw generation and VFX post-production — essentially bringing timeline-based editing concepts into the ComfyUI graph paradigm. This deserves an entity card given our focus on compositing workflows.

## Candidate: comfyui-LongLook (1 star, fresh)

Very new (< 48 hours active). Focuses on Wan 2.2 frame consistency past the standard generation window. Worth monitoring but too early for filing — will appear in cycle 21 if it gains traction.

## Recommendations

1. **Enrich ComfyUI v0.27 index entry** with v0.24–v0.26 video-relevant changes (WEBM alpha, Bria green screen, Kling V3-Turbo) — these affect post-production and VFX pipeline.
2. **Create entity card: `ComfyUI-FunPack`** in AI-Video section — non-linear editing integration is uniquely relevant to our domain.
3. **Monitor `comfyui-wan-i2v-control`** and `comfyUI-LongLook` next cycle — too new/few stars for filing now.

## Vault Index Status After This Scan

| Metric | Value |
|--------|-------|
| Total items in index | ~97 entries (AI-Video dominant) |
| New filings this cycle | **0** (candidates identified, see above) |
| Candidates for next cycle | 2 repos + 1 release enrichment block |
| Stale sources detected | HuggingFace RSS (404), PyTorch RSS (redirect) |

## Source Health Notes

- **HuggingFace**: Their blog now serves a SPA. No RSS at `/blog/rss`. Recommend switching to their API for model/activity feeds: `https://huggingface.co/api/models?sort=likes`
- **PyTorch Blog**: The RSS URL appears to redirect to an HTML page. Direct blog scraping with `curl -sL https://pytorch.org/blog/ | xmllint --html...` needed.
- **arXiv API**: Stable and reliable, all feeds returning correctly.

---
*Generated: 2026-07-05 | Cycle: 20 | Scanned sources: 6 (4 viable, 2 unhealthy)*