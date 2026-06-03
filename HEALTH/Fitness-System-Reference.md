---
title: Fitness System Reference
category: reference
summary: All Notion database IDs, n8n setup instructions, and gym buddy app deployment guide
updated: 2026-05-30
---

# Fitness System Reference

## Notion Databases

| Database | URL | Collection ID |
|----------|-----|---------------|
| Health & Fitness (hub page) | [Open](https://www.notion.so/371b4695a24d81e3a50cf064f0a90104) | — |
| Workout Log | [Open](https://www.notion.so/cfbdbb064e5444a1800475b6b5b7aed8) | `b54dd30b-5321-47c0-8fa6-7e4f96c26583` |
| Calorie Tracker | [Open](https://www.notion.so/2054229d30c4432183a136773d78abbc) | `2aead031-8711-4016-a88b-71109e76f8de` |
| Body Measurements | [Open](https://www.notion.so/e5f1344980784a6f9bf33bb3d001f07b) | `9ebde5ef-4c99-41e5-9e0f-8b45092a38e5` |
| Exercise Library | [Open](https://www.notion.so/9e896e054fc640ea977a606b48d1cfb8) | `52e6aa5f-47e3-4d3e-acc9-94b50c174bf5` |

---

## Gym Buddy App Setup

### Files
- `HEALTH/Fitness/gym-buddy-app.html` — the web app to deploy on your domain
- `HEALTH/Fitness/n8n-gym-workflow.json` — n8n workflow to import

### Deployment steps

1. **Copy `gym-buddy-app.html` to your hosting root** (e.g., `gym.yourdomain.com/index.html`)

2. **Import `n8n-gym-workflow.json` into n8n**
   - n8n → Workflows → Import → select the file
   - Add your Notion API credential to both Notion nodes
   - Activate the workflow
   - Note your webhook base URL (e.g., `https://your-n8n.com/webhook`)

3. **Configure the app**
   - Open the gym app on your phone/browser
   - Tap ⚙️ Configure n8n webhook URL
   - Enter: `https://your-n8n.com/webhook/gym`
   - Save

4. **Test**
   - Open the app — it will auto-detect today's workout day
   - Enter a weight and tap Log
   - Check Notion Workout Log — the entry should appear

### How the feedback loop works
```
Gym App → n8n webhook → Notion Workout Log
                                ↓
                         Coach (Claude) reads Notion
                         → analyzes trends weekly
                         → adjusts weights/volume
```

When you finish a session and tap **Send to Coach**, n8n formats the full session summary. I can then query your Workout Log each week to track progressive overload and flag when adjustments are needed.

---

## Weekly Coach Review

Every week (ideally Friday), ask Coach to:
- Pull last week's workout data from Notion
- Check progressive overload progress (which lifts moved?)
- Flag any muscle groups lagging
- Adjust target weights for next week

---

## Calorie Tracking

To log a meal: describe it or upload a photo → I estimate macros → log to Notion Calorie Tracker.

Daily targets:
- Calories: ~2,300 kcal
- Protein: 145–155g
- Fibre: 35–40g
- B12: supplement daily (methylcobalamin 1,000–2,000 mcg)

---

## Body Composition Reviews

- Cadence: every 4–6 weeks, or when you feel ready
- Process: upload front/side/back photos → I analyze changes → log findings to Body Measurements
- First baseline: not yet set — do this at start of Phase 1

Take your first measurements and log them to the Body Measurements Notion database this week.
