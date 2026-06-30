---
title: STORM — Multi-Perspective Autonomous Research Method
category: concept
summary: Stanford research method using 5 expert lens perspectives (practitioner, academic, skeptic, economist, historian) to catch blind spots single-angle prompts miss. Each lens analyzes independently, maps disagreements, verifies sources before delivering final briefing.
tags: [ai-agents, research-methodology, multi-agent, stanford, autonomous-research, claude]
sources: 1
updated: 2026-06-30
---

# STORM — Multi-Perspective Autonomous Research

> 📌 **STATUS:** Logged for future reference. NOT implemented in Arek&Co OS (2026-06-30). Single-lens Scholar agent sufficient for current knowledge domains. Revisit if research output quality drops or new domain requires multi-angle verification.

## Source

**Video:** "Stanford's Method Turns Claude Into a PhD Level Research Team" by Nate Herk (~12 min)
**URL:** https://youtu.be/Tj3018n5MVg

> ⚠️ NOT Karpathy's autoresearch — this is a research methodology video from a different creator. Karpathy's repo handles autonomous ML training hyperparameter optimization. STORM handles topic research depth. Both have value, different domains.

## Architecture Overview

1. **Topic enters** → spawns 5 independent lens-specialist agents:
   - **Practitioner** — hands-on, real-world application focus
   - **Academic** — theoretical backing, citations, peer-reviewed sources
   - **Skeptic** — challenges assumptions, identifies weak claims
   - **Economist** — cost/benefit analysis, resource tradeoffs
   - **Historian** — precedent, trend evolution, lessons from similar cases

2. **Each analyzes independently** — no cross-contamination between lenses during individual analysis phase

3. **Convergence/divergence mapping** — explicit comparison of where lenses agree vs disagree on key points

4. **Source verification** — every claim traced back to a primary source before final synthesis

5. **Delivers clean HTML briefing** — unified document with all perspectives integrated

## Why Multi-Perspective Beats Single-Prompt

- Catch domain-specific blind spots (skeptic catches overconfidence, academic catches missing citations)
- Prevent echo-chamber thinking in single-agent research
- Map actual disagreement surfaces rather than flattening to a "balanced" middle
- Source verification step is last line of defense against hallucination

## Comparison to Our Current Scholar

| Aspect | STORM (5-lens) | Arek&Co Scholar (single) |
|---|---|---|
| Depth per angle | High (specialized lens) | Medium-broad |
| Blind spot detection | Built-in via disagreement mapping | Relies on eval assertions |
| Source verification | Explicit step | Partial (eval suite checks quality, not provenance) |
| Token cost | 5x agent runs + synthesis | 1x agent run |
| Best for | Research-heavy topics, controversial claims, decision-critical briefs | Knowledge curation, tool documentation, creative research |

## When to Consider Implementation

- Topic requires cross-domain expert input (e.g., technical + business implications)
- Single-agent output consistently misses nuance or angle
- Need explicit disagreement surface mapping before user decision
- Research topic is controversial or has known bias/side-taking in literature
- Domain benefits from "red team" perspective on findings

## Not Applicable For

- Tool/documentation research (practitioner angle covers 90%)
- Creative topic exploration (subjective — lenses add noise, not signal)  
- Finance/health tracking data (objective numbers don't need multi-perspective framing)
- Music/Suno prompt research (already verified & filed successfully with single agent)

## Related

- [[Karpathy Autoresearch]] — autonomous ML training loop (different thing entirely)
- Scholar eval suite at `AGENTS/Scholar/evals/scholar_ingestion_evals.json` (10 binary assertions)
- Scholar autonomous scanner at `META/autoresearch_scanner_config.yaml`
