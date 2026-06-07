---
title: Emily Morning Brief — Live News Data Sources
summary: Google News RSS + Daily Hive scraping patterns for the daily 7:30 AM briefing
updated: 2026-06-05
---

# Emily Morning Brief — News Data Sources

## Google News RSS

Endpoint: `https://news.google.com/rss?topic={hhh|hbb|hwu}&hl=en-US&gl=US&ceid=US:en`

Topic codes:
- `hhh` — Top Stories
- `hbb` — Business
- `hwu` — World

Parse pattern:
```
items = re.findall(r'<item>(.*?)</item>', rss_text, re.DOTALL)
for item in items[:10]:
    title = re.findall(r'<title>(.*?)</title>', item, re.DOTALL)
    link  = re.findall(r'<link>(.*?)</link>', item)
    src   = re.findall(r'<font color="[^"]*">(.*?)</font>', item)
    # Clean HTML entities and strip tags
    t = html.unescape(re.sub(r'<[^>]+>', '', title[-1])).strip()
```

Filter: keep headlines > 20 chars. Store the full Google News URL as-is.

## Daily Hive Vancouver (Local Events)

- Homepage: `https://dailyhive.com/vancouver` — main Vancouver news
- Events: `https://dailyhive.com/vancouver/listed/events` — event listings
- Business/Tech: `https://dailyhive.com/vancouver/venture` — Tech & Business news

Parse: `re.findall(r'<a[^>]*href="([^"]*)"[^>]*>([^<]+)</a>', html)` to get title + URL tuples. Filter for Vancouver-relevant stories.

## The Verge (AI/Tech News)

- AI: `https://www.theverge.com/ai-artificial-intelligence`
- Tech: `https://www.theverge.com/tech`

Parse same regex pattern against `<a>` tags. Filter for AI/tech keywords.

## Variety/Hollywood Reporter (VFX/Film)

- Variety: `https://variety.com/`
- Filmmaker Magazine: `https://www.filmmakermagazine.com/`

Parse for film/VFX/relevance keywords. **Note**: These sites often return 308 redirects without `-L` flag on curl.

## Curl Pitfalls

- Always use `-sL` (silent + follow redirects) — many sites return 308
- Run `html.unescape()` on all scraped text — `&amp;`, `&#x27;`, etc. will corrupt links
- Google News RSS links are short-lived redirect URLs — they resolve correctly from the Google News domain
