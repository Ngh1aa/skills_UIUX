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
  ├─ PASS → complete active stage → next stage
  └─ explicit failure/risk signal → ReplanningEngine
                                      ↓
                              apply bounded flow delta
                                      ↓
                         resume from affected stage
```

## Ownership boundaries

- **Flow owns sequence and routing.** It declares stages, role, required/conditional skills, gates and replanning policy.
- **Agent owns role and authority.** `runtime/runtime-policy.json` declares purpose, maximum authority, default skills and legal handoffs.
- **Skill owns capability knowledge.** Agents and flows reference `SKILL.md`; they do not copy specialist guidance into a mega prompt.
- **Tool/script owns deterministic action.** Flow resolution never grants external/release authority.

## Development Manager

`runtime/manager.py::DevelopmentManagerAgent` is an A→Z manager, not a monolithic designer/developer. It resolves a flow, creates a manager checkpoint, starts only the active specialist stage, records stage runs, advances only after a completed stage run, resumes across processes, and applies bounded replans when evidence signals a failure or new risk.

The manager blocks out-of-order stage execution. A caller cannot jump from research directly to QA or apply a replan from a stage that is not currently active.

This preserves progressive disclosure: research does not load all implementation/QA skill bodies, and QA remains independently scoped.

## Managed lifecycle

A managed run persists:

- `manager_run_id`;
- resolved flow + flow revision;
- active stage;
- completed stages;
- specialist stage run IDs;
- replan count and history;
- task context and authority.

The normal lifecycle is:

```text
START
→ research
→ design
→ implementation
→ qa
→ COMPLETED
```

A replan invalidates only the affected stage and downstream completed stages. Example: a QA `GATE_FAIL` can return to implementation while preserving verified research/design work.

## Modern professional website defaults

`professional-website-redesign` requires:

- project truth, audience intent and IA;
- reference research before locking visual direction;
- distinctive visual direction and reusable design system;
- explicit anti-generic visual signature and art direction;
- responsive implementation and truthful system behavior;
- rendered visual QA, accessibility, code review, web quality and media-crop checks.

Domain routing is conditional for corporate, ecommerce, education, government, hospitality, news/media, real estate, SaaS, startup/incubator, portfolio, nonprofit and landing pages.

These defaults improve delivery discipline; they are not evidence by themselves that a rendered website is visually finished, accessible, performant or production-ready.

## Replanning is not retry

A replan requires:

1. an explicit configured signal (`GATE_FAIL`, `BLOCKED`, `NEW_RISK`, `INVALID_ASSUMPTION`, `TOOL_FAILURE`, `CONTEXT_DRIFT`);
2. remaining replan budget;
3. a matching declarative policy;
4. the signal to originate from the active stage when the replan will be applied.

An accepted replan can target an earlier stage, add/drop non-mandatory skills, increment the flow revision and invalidate only affected downstream stage completion. Role `default_skills` and flow-required skills cannot be dropped. Replanning never increases runtime authority.

## CLI lifecycle

Start a professional ecommerce redesign flow:

```bash
python -B scripts/uiux-agent.py \
  --project . \
  --managed \
  --task "Redesign ecommerce website" \
  --website-type ecommerce \
  --mode interactive-prototype \
  --feature search \
  --authority branch_write
```

The output includes `manager_run_id`. Resume and run the active stage:

```bash
python -B scripts/uiux-agent.py \
  --project . \
  --managed-run-id <manager_run_id> \
  --plan path/to/provider-plan.json \
  --advance-on-success
```

Inspect without executing:

```bash
python -B scripts/uiux-agent.py --project . --managed-run-id <manager_run_id>
```

Apply a QA failure replan:

```bash
python -B scripts/uiux-agent.py \
  --project . \
  --managed-run-id <manager_run_id> \
  --replan-signal GATE_FAIL
```

Use `--no-apply-replan` for diagnostic what-if routing without mutating the persisted managed run.

## Validation

```bash
python -B scripts/validate-flows.py
python -B scripts/validate-runtime-foundation.py
```

`.github/workflows/flow-os-validate.yml` runs these checks for relevant pushes and pull requests.

## Extension rule

Prefer this order:

1. add/maintain a specialist skill only when there is a real capability gap;
2. route that skill from a flow;
3. add a new flow when sequence/gates materially differ;
4. change manager/runtime code only when the orchestration primitive itself changes.

This means adding an existing capability to ecommerce/education/corporate should normally be a flow edit, not a new branch in agent code.
