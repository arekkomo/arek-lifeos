# Agent Task Bus

## Purpose
A durable, asynchronous delegation layer for all Arek & Co. agents. Any specialist can assign a bounded task to any other specialist without asking Arek to relay it or using Telegram as transport.

## Board
- **Board:** `agent-task-bus`
- **Transport:** Hermes Kanban dispatcher (embedded in each gateway)
- **Task lifecycle:** `todo → ready → running → done` or `blocked`
- **Default runtime:** 30 minutes unless a task needs a longer explicit limit.

## Active Agent Roster
| Profile | Primary responsibility |
|---|---|
| accountant | Finance, tax, budgets, commercial analysis |
| coach | Health, training, nutrition, recovery |
| connector | Relationships, contacts, partnerships |
| director | Creative direction, film, music, production pipelines |
| ltx-prompter | LTX cinematic video prompting |
| scholar | Research, source evaluation, knowledge synthesis, vault curation |
| strategist | Strategy, planning, curriculum, prioritization |
| systems | Technical architecture, tooling, integrations, reliability |

## Delegation Contract
Create a task only when work belongs to another specialist, needs durable tracking, or benefits from independent execution. Do not delegate trivial questions that can be answered from the current context.

Every task must include:
1. **Clear outcome** — what the receiving agent must deliver.
2. **Context** — why it matters and any constraints.
3. **Deliverables** — explicit output format or acceptance criteria.
4. **Priority** — numeric: `10` low, `50` medium, `80` high, `100` urgent.
5. **Source** — the requesting profile; use `created_by`.

### Research request template
```text
Title: Research: <question>
Assignee: scholar
Priority: medium

Objective: <decision or creative question this research supports>
Scope: <what to include / exclude>
Deliverables:
- Direct answer / executive summary
- Evidence-backed findings
- 3–8 credible sources with links
- Risks, limits, and uncertainty
- Recommendation or creative implications
Context: <project and why now>
```

## Completion Rules
- Receiving agent uses `kanban_complete` only after the requested deliverables are produced.
- Use `kanban_block` immediately for missing information, inaccessible sources, or a decision needed from Arek.
- The completion summary must be concise and state: result, important caveat, and where the full artifact lives.
- Do not send routine task-status messages to Arek. Surface only blockers, material decisions, or finished work that requires action.

## Safety Rules
- Assign only to a profile in the active roster.
- Do not include credentials, private tokens, or raw sensitive information in task bodies.
- Do not make irreversible file, financial, account, or external communication changes solely because a task asked for them; use normal approval requirements.
- Tasks may be parallel only when independent. Use parent dependencies for work that requires earlier findings.

## Examples
- Director → Scholar: research visual references, emerging tools, or filmmaking methods for a creative project.
- Strategist → Scholar: source a curriculum or evaluate a market/technology claim.
- Systems → Scholar: research a framework, vendor, or documented integration before implementation.
- Scholar → Director: translate research findings into creative implications or a production treatment.
- Any agent → Systems: request a technical feasibility assessment.
