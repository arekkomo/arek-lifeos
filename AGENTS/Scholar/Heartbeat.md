---
title: Scholar Heartbeat
agent: Scholar
summary: What the Scholar checks at the start of every session.
updated: 2026-05-13
---

# Scholar Heartbeat

> Run at the start of every Scholar session — before any ingest, query, or synthesis work.

---

## 1. Scan raw/ for unprocessed source documents
- Check `raw/` for any files that haven't been ingested yet
- Source documents (articles, transcripts, Notion exports) → queue for ingest
- Do NOT delete source documents — they are immutable
- Loose captures (voice notes, test files) → flag for Operator to route

## 2. Check the knowledge index
Read: `LEARNING/index.md`
- What was last ingested, and when?
- Are there any disciplines with outdated content?
- Is there a synthesis that needs updating?

## 3. Check for pending queries
- Did any agent request a knowledge lookup that isn't resolved?
- Is Strategist waiting on curriculum content for a module?
- Is Director waiting on filmmaking reference material?

## 4. Check Synthesis.md
Read: `LEARNING/Synthesis.md`
- Does any cross-domain insight need updating?
- Has recent ingest created a contradiction that needs flagging?

---

## Ingest Priority Order
When there are multiple sources to ingest, prioritise:
1. Filmmaking / Directing content (feeds SK-ST-01 curriculum)
2. AI video / AI tools (feeds RRH + Director's work)
3. AI Agents / n8n (feeds System agent + automation work)
4. Other domains

---

## Knowledge Cluster Status
*(Update when new ingests complete)*

| Cluster | Folder | Last Ingest | Status |
|---|---|---|---|
| AI Video | LEARNING/Knowledge/AI-Video/ | 2026-05-10 | Active |
| AI Image | LEARNING/Knowledge/AI-Image-Midjourney/ | 2026-05-10 | Active |
| AI 3D | LEARNING/Knowledge/AI-3D/ | 2026-05-10 | Active |
| AI Agents / n8n | LEARNING/Knowledge/AI-Agents/ | 2026-05-10 | Active |
| Filmmaking | LEARNING/Knowledge/Filmmaking/ | 2026-05-10 | Active |
| DaVinci Resolve | LEARNING/Knowledge/DaVinci-Resolve/ | 2026-05-10 | Active |
| Motion Capture | LEARNING/Knowledge/Motion-Capture/ | 2026-05-10 | Active |

---

## Key Files to Reference
- `LEARNING/index.md` — content catalog
- `LEARNING/log.md` — append-only operation log
- `LEARNING/Synthesis.md` — cross-domain synthesis
- `raw/` — source documents (read only)
