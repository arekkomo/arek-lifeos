# n8n Workflow — YouTube → Notion Pipeline

Tags: n8n
Description: n8n automation workflow that takes a YouTube video link, extracts transcript, summarizes it with AI, and saves structured notes to the dtb Knowledge database in Notion.
Date Added: March 29, 2026 12:55 PM
Type: Workflow
Archive: No
Spark: No

> Reference doc for building the automated YouTube knowledge base ingestion workflow in n8n.
> 

---

## Flow Overview

```
[Trigger] → [Extract Video ID] → [Fetch Transcript] → [Claude Summarize] → [Create Notion Entry]
```

---

## Node 1 — Trigger

Choose one trigger method:

- **Webhook** (recommended to start) — send a POST request with the YouTube URL
- **Gmail trigger** — watch for emails with a specific label or subject containing a YouTube URL
- **Telegram/Slack** — send YouTube link to a bot

**Webhook example payload:**

```json
{ "url": "https://youtu.be/Y_qxGWC0d38" }
```

---

## Node 2 — Extract Video ID (Code Node)

```jsx
const url = $input.first().json.url;
const match = url.match(/(?:youtu\.be\/|v=|v\/|embed\/|shorts\/)([\w-]{11})/);
const videoId = match ? match[1] : null;
return [{ json: { videoId, originalUrl: url } }];
```

---

## Node 3 — Fetch Transcript (HTTP Request)

- **Method:** GET
- **URL:** `https://www.youtube-transcript-api.com/api/transcript?videoId={{$json.videoId}}`
- **Alternative:** RapidAPI YouTube Transcript endpoint
- **Output:** full transcript text

Add a Code node after to flatten transcript segments into a single string:

```jsx
const segments = $input.first().json;
const transcript = segments.map(s => s.text).join(' ');
return [{ json: { transcript, videoId: $('Extract Video ID').first().json.videoId, originalUrl: $('Extract Video ID').first().json.originalUrl } }];
```

---

## Node 4 — Claude Summarize (HTTP Request)

- **Method:** POST
- **URL:** `https://api.anthropic.com/v1/messages`
- **Headers:**
    - `x-api-key`: your Anthropic API key
    - `anthropic-version`: `2023-06-01`
    - `content-type`: `application/json`

**Body:**

```json
{
  "model": "claude-sonnet-4-20250514",
  "max_tokens": 1000,
  "messages": [
    {
      "role": "user",
      "content": "You are a knowledge base assistant. Given this YouTube video transcript, return ONLY a valid JSON object (no markdown, no explanation) with:\n- title: video title (infer from content)\n- description: array of 3-5 bullet strings summarizing key tips/advice\n- key_insights: array of 2-3 most actionable takeaways\n- tags: array of relevant tags ONLY from this list: [AI Video, AI Image, VFX, Filmmaking, Tutorial, AI Automation, LLM, ComfyUI, Diffusion Models, AI, Productivity, Content Creation, Davinci, Video Editing, Research]\n- rating: one of: ⭐ or ⭐⭐ or ⭐⭐⭐ or ⭐⭐⭐⭐ or ⭐⭐⭐⭐⭐\n\nTranscript:\n{{ $json.transcript }}"
    }
  ]
}
```

**Parse response** with a Code node:

```jsx
const content = $input.first().json.content[0].text;
const parsed = JSON.parse(content);
return [{ json: { ...parsed, originalUrl: $('Flatten Transcript').first().json.originalUrl } }];
```

---

## Node 5 — Create Notion Entry (Notion Node or HTTP Request)

Use the **Notion integration** in n8n:

- **Operation:** Create a database item
- **Database ID:** `171b4695-a24d-8014-8354-cee9f58d98fc` (dtb Knowledge)

**Field mapping:**

| Notion Field | n8n Value |
| --- | --- |
| Name | `{{ $json.title }}` |
| Type | `Youtube` |
| URL | `{{ $json.originalUrl }}` |
| Description | `{{ $json.description.join('\n') }}` |
| Tags | `{{ $json.tags }}` |
| Rating | `{{ $json.rating }}` |
| Spark | `false` (always) |

**Page body** (Key Insights):

Add a second Notion node to append content to the created page:

```
## Key Insights
{{ $json.key_insights.map(i => '- ' + i).join('\n') }}
```

---

## Trigger Options Comparison

| Trigger | Effort | Best for |
| --- | --- | --- |
| Webhook | Low | Testing, dev use |
| Gmail label | Medium | "Forward to save" flow |
| Telegram bot | Medium | Mobile quick-save |
| Browser extension | High | One-click from YouTube |

---

## Notes

- Spark field must always be `false` — never auto-populate
- If transcript fetch fails, add an error branch that logs the URL only with a "Needs Review" tag
- Transcript APIs may have rate limits on free tiers — monitor usage
- Claude model: always use `claude-sonnet-4-20250514` for this workflow

---

## Status

- [ ]  Webhook trigger set up
- [ ]  Transcript API tested
- [ ]  Claude node tested with sample transcript
- [ ]  Notion node connected and mapped
- [ ]  End-to-end test passed
- [ ]  Switch to preferred trigger (Gmail / Telegram)