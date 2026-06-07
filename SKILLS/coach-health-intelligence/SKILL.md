---
name: coach-health-intelligence
description: "Coach's health intelligence skill — cross-check recommendations against Scholar's knowledge base, flag new evidence, and manage critical health context."
category: health-coach
---

# SK-CO-05 — Health Intelligence

**Agent:** The Coach
**Status:** Active
**Version:** 2.0

## Description
Cross-check all Coach recommendations against current research (via Scholar). Manage critical ongoing monitoring for Arek's specific medical context.

## Scholar Coordination
- Request Scholar pull relevant health and fitness knowledge from the knowledge base
- Cross-check Coach recommendations against current research
- Flag when new evidence contradicts current plan

## Critical Ongoing Monitoring

### B12 — HIGH PRIORITY
- Supplement daily
- Flag monthly if not confirmed
- Reduced meat + tenofovir = highest depletion risk tier

### Bone Density
- Note tenofovir long-term use
- If Arek mentions bone-related issues, flag for medical attention

### Inflammation Markers
- If Arek reports joint pain or persistent soreness, cross-check against nutrition and recovery data

### Vitamin D
- Monitor levels given Vancouver climate (limited sun Oct-Apr)
- Recommend supplementation if levels are low

### Omega-3
- Flag if diet is low in fatty fish or algae-based sources
- Relevant for joint health and recovery

### Fibre
- Current intake is low
- Track weekly and target 30-40g/day
- Suggest high-fibre plant foods aligned with dietary constraints (max 2× meat/week)

## Storage
- Health monitoring notes: `/HEALTH/Health-Knowledge/`
- Save any contradictions between current plan and new research to `/HEALTH/Health-Knowledge/contradictions/YYYY-MM-Summary.md`

## Rule: Always verify against current research before recommending new supplements or protocols that deviate from current plan.
