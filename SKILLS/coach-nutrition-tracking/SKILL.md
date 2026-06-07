---
name: coach-nutrition-tracking
description: "Coach's nutrition tracking skill — daily macro estimation, meal planning, grocery lists, and dietary constraint management for Arek."
category: health-coach
---

# SK-CO-02 — Nutrition Tracking

**Agent:** The Coach
**Status:** Active
**Version:** 2.0

## Description
Daily calorie and macro tracking through meal description or food photo analysis. Weekly meal planning and grocery list generation.

## Tracking Method
- Manual: Arek describes meals → Coach estimates calories and macros
- AI Vision: Coach analyses food photos for portion size and macro estimate
- Running daily total: calories, protein, carbs, fat, fibre

## Targets
- **Calories:** ~deficit phase (~500 kcal below TDEE for fat loss)
- **Protein:** 1.4–1.6 g/kg BW = ~128–147 g/day (prioritise given mostly plant-based)
- **Fibre:** 30–40 g/day minimum (currently low)
- **B12:** supplement daily — high depletion risk (reduced meat + tenofovir)

## Dietary Constraints
- Meat: max 2×/week
- Lactose: avoid where easy, not strict
- High-fibre priority

## Meal Timing Pattern
- Post-gym (morning): protein shake
- Lunch: ~1 pm
- Dinner: ~7–8 pm

## Weekly Meal Planning (every Friday)
1. Review last week's nutritional gaps
2. Generate 7-day meal plan aligned with macro targets and dietary preferences
3. Produce grocery list from the meal plan
4. Save meal plan to /HEALTH/Nutrition-Plan/YYYY-WW-Meal-Plan.md
5. Save grocery list to /HEALTH/Nutrition-Plan/Grocery-Lists/YYYY-WW-Groceries.md

## Storage
- Meal plans: `/HEALTH/Nutrition-Plan/`
- Grocery lists: `/HEALTH/Nutrition-Plan/Grocery-Lists/`
