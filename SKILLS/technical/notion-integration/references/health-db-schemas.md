# Health & Fitness Database Schemas

Discovered 2026-05-31 via Notion API `GET /v1/databases/{db_id}` queries.

## Exercise Library
- **ID:** `9e896e05-4fc6-40ea-977a-606b48d1cfb8`
- **Properties:**
  - `Exercise Name` → `title`
  - `Primary Muscle` → `select` (Chest, Anterior Deltoid, Medial Deltoid, Posterior Deltoid, Triceps, Lats, Rhomboids, Biceps, Core, Quads, Hamstrings, Glutes, Traps, Forearms)
  - `Secondary Muscles` → `multi_select` (same options as Primary Muscle)
  - `Phase` → `select` (Phase 1, Phase 2, Phase 3)
  - `Equipment` → `select` (Barbell, Dumbbell, Cable, Machine, Bodyweight)
  - `Day` → `multi_select` (Push A, Pull A, Shoulders+Core, Arms, Full Body)
  - `Image URL` → `url`
  - `Coaching Cues` → `rich_text`

## Body Measurements
- **ID:** `e5f13449-8078-4a6f-9bf3-3bb3d001f07b`
- **Properties:**
  - `Entry` → `title`
  - `Weight (kg)` → `number`
  - `Left Arm Flexed (cm)` → `number`
  - `Right Thigh (cm)` → `number`
  - `Left Thigh (cm)` → `number`
  - `Waist (cm)` → `number`
  - `Chest (cm)` → `number`
  - `Hips (cm)` → `number`
  - `Shoulder Width (cm)` → `number`
  - `Right Arm Flexed (cm)` → `number`
  - `Date` → `date`
  - `Notes` → `rich_text`
  - `Photo Analysis` → `rich_text`

## Calorie Tracker
- **ID:** `2054229d-30c4-4321-83a1-36773d78abbc`
- **Properties:**
  - `Calories (kcal)` → `number`
  - `Date` → `date`
  - `Meal Type` → `select` (Lunch, Dinner, Breakfast, Snack, Other)
  - `Meal` → `rich_text`
  - `Description` → `rich_text`
  - `From Photo` → `checkbox`
  - `Photo URL` → `url`
  - `Carbs (g)` → `number`
  - `Fat (g)` → `number`
  - `Protein (g)` → `number`
  - `Fibre (g)` → `number`
  - `B12 Source` → `rich_text`

## Workout Log
- **ID:** `cfbdbb06-4e54-44a1-8004-75b6b5b7aed8`
- **Properties:**
  - `Exercise` → `title`
  - `Date` → `date`
  - `Day Type` → `select` (Push A, Pull A, Shoulders+Core, Arms, Full Body)
  - `Muscle Group` → `multi_select` (Chest, Shoulders, Triceps, Back, Biceps, Core, Legs, Rear Delt)
  - `Total Sets` → `number`
  - `PR` → `checkbox`
  - `Set 1 Weight (kg)` → `number`
  - `Set 1 Reps` → `number`
  - `Set 2 Weight (kg)` → `number`
  - `Set 2 Reps` → `number`
  - `Set 3 Weight (kg)` → `number`
  - `Set 3 Reps` → `number`
  - `Set 4 Weight (kg)` → `number`
  - `Set 4 Reps` → `number`
  - `Notes` → `rich_text`
  - `Session ID` → `rich_text`
