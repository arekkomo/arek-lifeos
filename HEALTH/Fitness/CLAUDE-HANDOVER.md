# Gym Buddy App — Claude Code Handover

> **Project:** Arek's personal gym coaching web app  
> **Handover from:** Cowork Coach agent (Claude)  
> **Date:** 2026-05-30  
> **Access:** Spark machine + Cloudflare account

---

## What This Is

A mobile-first gym coaching web app that:
- Shows today's workout based on day of week (Mon–Fri split)
- Displays exercise instructions with coaching cues
- Shows last session's weights (loaded from Notion via n8n)
- Lets the user log sets/reps/weights
- Sends session data back to Notion Workout Log → Coach (Claude in Cowork) reads and tracks progress

This is a **personal tool** accessed via a private Cloudflare domain. Single user: Arek Komorowski.

---

## Current State

### Files already created (in Obsidian vault)
```
HEALTH/Fitness/
├── Fitness-Plan-Phase1.md       ← Full workout plan (reference only)
├── Fitness-System-Reference.md  ← Notion IDs, setup guide
├── gym-buddy-app.html           ← The web app (complete, ready to deploy)
└── n8n-gym-workflow.json        ← n8n workflow (ready to import/deploy)
```

### Notion databases already created
| Database | Notion ID |
|----------|-----------|
| Health & Fitness (hub) | `371b4695a24d81e3a50cf064f0a90104` |
| Workout Log | `cfbdbb064e5444a1800475b6b5b7aed8` |
| Calorie Tracker | `2054229d30c4432183a136773d78abbc` |
| Body Measurements | `e5f1344980784a6f9bf33bb3d001f07b` |
| Exercise Library | `52e6aa5f-47e3-4d3e-acc9-94b50c174bf5` |

Exercise Library is fully populated with 26 Phase 1 exercises including coaching cues.

---

## Your Tasks

### 1. Deploy gym-buddy-app.html to Cloudflare

The app is a **single HTML file** with all JS/CSS inline — no build step required.

Options (in order of preference):
- **Cloudflare Pages** — deploy from a Git repo or direct upload. Zero config.
- **Cloudflare Worker serving static HTML** — if Pages isn't available.

Target URL: something like `gym.areks-domain.com` or `coach.areks-domain.com`

Steps:
1. Copy `gym-buddy-app.html` to a new repo (or upload directly to Cloudflare Pages)
2. Set up Cloudflare Pages project pointing to that file as `index.html`
3. Configure custom domain in Cloudflare dashboard
4. Confirm the app loads on the domain

### 2. Deploy the n8n workflow

The workflow file `n8n-gym-workflow.json` defines 3 webhook endpoints:

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/webhook/gym/log-set` | POST | Log an exercise set → writes to Notion Workout Log |
| `/webhook/gym/last-session?exercise=NAME` | GET | Returns last logged weights for an exercise |
| `/webhook/gym/session-complete` | POST | Sends full session summary for Coach analysis |

Steps:
1. Import `n8n-gym-workflow.json` into the n8n instance on Spark
2. Add the Notion API credential to both Notion nodes (the credential ID placeholder is `YOUR_NOTION_CREDENTIAL_ID`)
3. Activate the workflow
4. Note the production webhook base URL (e.g., `https://n8n.spark-host.com/webhook`)

### 3. Update the app with the real webhook URL

In `gym-buddy-app.html`, find this line near the top of the `<script>` block:

```javascript
const DEFAULT_WEBHOOK = 'https://YOUR-N8N-URL/webhook/gym';
```

Replace with the actual n8n base URL. Then redeploy to Cloudflare Pages.

Alternatively, the app has a built-in config UI (tap ⚙️) that stores the URL in localStorage — Arek can set this himself without a redeploy.

### 4. (Optional but recommended) Add CORS headers in n8n

If the Cloudflare domain and n8n are on different origins, add response headers to the n8n webhooks:
```
Access-Control-Allow-Origin: https://your-gym-app-domain.com
Access-Control-Allow-Methods: GET, POST, OPTIONS
Access-Control-Allow-Headers: Content-Type
```

This can be done in n8n via a "Respond to Webhook" node with custom headers, or a Cloudflare Worker proxy.

---

## App Architecture

```
[Gym app on Cloudflare]
        ↓  GET /gym/last-session?exercise=NAME
        ↓  POST /gym/log-set
        ↓  POST /gym/session-complete
[n8n on Spark machine]
        ↓  Read/Write
[Notion Workout Log DB]
        ↓  Queried by
[Coach (Claude in Cowork)] → weekly analysis → weight adjustments
```

---

## Workout Plan Context (for app improvements)

The 5-day split:
| Day | Type | Key muscles |
|-----|------|-------------|
| Mon | Push A | Shoulders, chest, triceps |
| Tue | Pull A | Back, biceps, rear delts |
| Wed | Shoulders+Core | All 3 delt heads, abs |
| Thu | Arms | Biceps, triceps specialisation |
| Fri | Full Body | Legs light, shoulders polish, core |
| Sat/Sun | Rest | — |

The exercise database is embedded in the HTML — no API call needed to load exercises. Only last-session weights are fetched from n8n/Notion.

---

## User Profile (for personalisation)
- **Name:** Arek Komorowski
- **Age:** 48 | Height: 192cm | Weight: 92kg
- **Goal:** Belly fat loss, bigger shoulders/arms
- **Injuries:** Shoulder history (warmup flags in exercises), occasional lower back pain
- **Level:** Intermediate, 5×/week, 45–60 min sessions

---

## Future Development Ideas

- [ ] Add exercise GIF images (Wger API or Giphy workout GIFs)
- [ ] Weekly progress chart (pull from Notion, render with Chart.js)
- [ ] Rest timer between sets
- [ ] Meal photo upload → sends to Coach for calorie estimation
- [ ] PWA manifest so it installs on home screen like a native app
- [ ] Push notifications for workout reminders (7am Mon–Fri)
- [ ] Coach notes section — weekly feedback from Claude appears in app

---

## Notion Integration Notes

The Notion integration token used by n8n must have access to the workspace containing these databases. All databases are under:
- Notion page: https://www.notion.so/371b4695a24d81e3a50cf064f0a90104

The Notion API used is the official REST API via n8n's built-in Notion node (v2).

For direct Notion API calls if needed:
- Base URL: `https://api.notion.com/v1`
- Auth: `Authorization: Bearer YOUR_NOTION_TOKEN`
- Notion-Version: `2022-06-28`

---

*Generated by Cowork Coach agent. Questions → ask Coach in Cowork.*
