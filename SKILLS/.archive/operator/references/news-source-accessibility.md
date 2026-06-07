# News Source Accessibility — Cron Mode Guide

> Last verified: 2026-06-04. Updated as new sources break.

## Unreliable for Cron (SPA/CORS/Empty)

These return HTTP 200 but ZERO usable content via raw curl:

| Source | Symptom |
|--------|-----|
| BBC News | SPA HTML — CSS classes, no text |
| Variety, Hollywood Reporter | Cloudflare/SPA |
| Animation Magazine | CloudFront 403 |
| VFX Voice, Reuters, AP News | SPA |
| Google News RSS | Empty response |

## Partially Reliable

| Source | Notes |
|--------|-------|
| Daily Hive `/vancouver/*` | ~70% — headlines extractable via grep |
| Wikipedia `/wiki/June_4` | Works well. Parse `<li>` tags. |
| Wikipedia `Special:OnThisDay` | Does NOT exist (404). Use main date page instead. |

## Reliable for Cron

| Source | Access |
|--------|--------|
| Wikipedia `/wiki/Special:Currentevents` | Structured HTML |
| Reddit RSS | `r/worldnews/hot.rss` — may need UA |
| Archive.org cached | `web.archive.org/web/<timestamp>/` |

## Recommendation

When cron runs with no browser:
1. **Headlines**: Acknowledge if sources are SPA-blocked. Use what works (Daily Hive, Reddit RSS). If nothing yields results, write "quiet news" — never fabricate.
2. **Industry news**: Use whatever sources return content. Fall back to last-known context.
3. **On This Day**: Wikipedia is reliable.
4. **Local events**: Daily Hive is best for Vancouver.
