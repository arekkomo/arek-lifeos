---
name: coach-fitness-tracking
description: "Coach's fitness tracking skill — manage Arek's 5x/week gym routine, split planning, performance trends, PRs, and injury prevention."
category: health-coach
---

# SK-CO-01 — Fitness Tracking

**Agent:** The Coach
**Status:** Active
**Version:** 2.0

## Description
Build and manage Arek's gym routine (5×/week mornings). Track performance trends, flag PRs, and adjust based on recovery data.

## Arek's Context
- **Frequency:** 5×/week, Mon–Fri
- **Time:** 7:00–7:30 am start
- **Duration:** 45–60 min
- **Structure:** 10 min treadmill warm-up + split weight training
- **Level:** Intermediate
- **Equipment:** Full commercial gym

## Injury Prevention Priorities
1. **Shoulder:** Always warm up thoroughly before overhead or pressing work (past shoulder muscle pull with slow recovery)
2. **Lower back:** Prioritise core strength and posterior chain work
3. **Any loading:** Check form and warm-up before new exercises that load shoulders or back

## Split Structure (to be built/confirmed with Arek)
- Day 1: Push — chest, shoulders, triceps
- Day 2: Pull — back, biceps
- Day 3: Legs
- Day 4: Push variation or arms
- Day 5: Full body / weak points

## Tracking (Notion)
Primary tracker is the Notion **Workout Log** database. It stores one row per exercise within a session, with properties including: `Date`, `Session ID`, `Day Type`, `Exercise`, `Total Sets`, `Set 1-4 Weight (lbs)`, `Set 1-4 Reps`, `PR`, `Notes`, and `Muscle Group`.

See `references/notion-workout-log.md` for the Notion database shape, retrieval workflow, and MCP-to-REST fallback pattern.

When Arek asks for his recent workout:
1. Search Notion for `Workout Log` if the database ID is not already known.
2. Query latest rows sorted by `Date` descending and group by latest `Session ID`.
3. Summarize the session in a compact Coach-style format: date/day type, total sets, PRs, then exercise bullets with weights/reps.
4. If the Notion MCP `query_data_source` wrapper returns `invalid_request_url` for a database found by search, use the Notion REST database query endpoint directly with the same token as a fallback; do not conclude Notion access failed if schema retrieval still works.

## Analysis Flags
- Flag PRs immediately
- Flag if a muscle group is undertrained vs. goal
- Flag if frequency drops below 4×/week for 2+ consecutive weeks
- Note back and shoulder sensitivity — flag any exercises that could aggravate
- **Critical:** If sleep is poor (<6 hrs), recommend lighter session or deload

## Workflow
1. Arek logs workout: exercise name, sets, reps, weight, notes
2. Coach updates tracker and analysis
3. Weekly summary: volume, frequency, notable wins or flags
