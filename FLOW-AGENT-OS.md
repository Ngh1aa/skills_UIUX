# Flow Agent OS — Development Manager Architecture

This layer turns `skills_UIUX` from a large skill library into a declarative professional-website workflow runtime.

## Contract

```text
User/project task
  ↓
Development Manager
  ↓
FlowResolver(task context)
  ↓
Resolved Flow
  ├─ research agent → research/domain skills
  ├─ implementation agent → design/system/code skills
  └─ qa agent → rendered/source/test verification skills
  ↓
Gate evidence
  ├─ PASS → next stage
  └─ explicit failure/risk signal → ReplanningEngine
                                      ↓
                                 bounded plan delta
```

## Ownership boundaries

- **Flow owns sequence and routing.** It declares stages, role, required/conditional skills, gates and replanning policy.
- **Agent owns role and authority.** `runtime/runtime-policy.json` declares purpose, maximum authority, default skills and legal handoffs.
- **Skill owns capability knowledge.** Agents and flows reference `SKILL.md`; they do not copy specialist guidance into a mega prompt.
- **Tool/script owns deterministic action.** Flow resolution never grants external/release authority.

## Development Manager

`runtime/manager.py::DevelopmentManagerAgent` is an A→Z manager, not a monolithic designer/developer. It resolves a flow, creates a manager checkpoint, starts stage-scoped specialist runs and asks the Replanning Engine for bounded changes when evidence signals a failure or new risk.

This preserves progressive disclosure: research does not load all implementation/QA skill bodies, and QA remains independently scoped.

## Modern professional website defaults

`professional-website-redesign` requires:

- project truth, audience intent and IA;
- reference research before locking visual direction;
- distinctive visual direction and reusable design system;
- responsive implementation and truthful system behavior;
- rendered visual QA, accessibility, code review, web quality and media-crop checks.

Domain routing is conditional for corporate, ecommerce, education, government, hospitality, news/media, real estate, SaaS, startup/incubator, portfolio, nonprofit and landing pages.

These defaults improve delivery discipline; they are not evidence by themselves that a rendered website is visually finished, accessible, performant or production-ready.

## Replanning is not retry

A replan requires:

1. an explicit configured signal (`GATE_FAIL`, `BLOCKED`, `NEW_RISK`, `INVALID_ASSUMPTION`, `TOOL_FAILURE`, `CONTEXT_DRIFT`);
2. remaining replan budget;
3. a matching declarative policy.

A replan may return to an earlier stage and add/drop skills. It never increases runtime authority.

## Extension rule

Prefer this order:

1. add/maintain a specialist skill only when there is a real capability gap;
2. route that skill from a flow;
3. change manager/runtime code only when the orchestration primitive itself changes.

This means adding an existing capability to ecommerce/education/corporate should normally be a flow edit, not a new branch in agent code.
