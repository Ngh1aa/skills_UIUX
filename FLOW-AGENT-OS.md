# Flow Agent OS — Development Manager Architecture

This layer turns `skills_UIUX` from a large skill library into a declarative professional-website workflow runtime.

## Core operating principle

> **The user states the goal. The Development Manager chooses the Flow. The Flow determines the Agents and Skills. Agents use Tools to produce evidence and artifacts. Gates decide whether work may advance. Failures go to the Replanning Engine instead of blind retries. The user only intervenes at approval gates that materially require human judgment or authorization.**

In Vietnamese, the product principle is:

> **User chỉ nói mục tiêu. Development Manager quyết định Flow. Flow quyết định Agent và Skill. Agent sử dụng Tool để tạo evidence/artifact. Gate quyết định có được đi tiếp hay không. Failure đi vào Replanning Engine thay vì retry mù. User chỉ can thiệp ở những approval gate thực sự cần thiết.**

This principle is the source of truth for orchestration decisions. Runtime code, flows, skills, tools and UI should preserve this separation of responsibility instead of collapsing the system into one monolithic agent or a fixed prompt chain.

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

- **User owns goals and approvals.** The user describes the desired outcome and is only asked to intervene when a gate requires human judgment, policy authorization, external-write approval or release authority.
- **Development Manager owns orchestration.** It interprets task context, resolves the best applicable flow, manages lifecycle state and coordinates specialist stages without becoming a mega-agent.
- **Flow owns sequence and routing.** It declares stages, role, required/conditional skills, gates and replanning policy.
- **Agent owns role and authority.** `runtime/runtime-policy.json` declares purpose, maximum authority, default skills and legal handoffs.
- **Skill owns capability knowledge.** Agents and flows reference `SKILL.md`; they do not copy specialist guidance into a mega prompt.
- **Tool/script owns deterministic action.** Agents use tools/scripts to create, inspect, transform or verify concrete artifacts. Flow resolution never grants external/release authority.
- **Gate owns progression.** A stage advances only when the required evidence exists and the gate passes; model self-report alone is not proof.
- **Replanning Engine owns failure recovery.** Failures, invalid assumptions, new risks, tool failures and context drift are routed through bounded replanning rather than blind retries.

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

## Human intervention policy

The default experience should minimize orchestration burden on the user. A normal request may begin as one natural-language goal; the system should infer the applicable website type, features, mode and risk context when confidence is sufficient, then route work automatically.

Human intervention is appropriate when the decision is genuinely external to the runtime, for example:

- approving a Design Contract when the project is configured for approval mode;
- choosing between materially different brand/business directions when evidence cannot resolve the decision;
- authorizing destructive/external writes;
- approving production release or deployment when release authority is required;
- resolving missing business truth that cannot be safely inferred.

Do not ask the user to manually select internal skills, agents or routine retry behavior when the Flow Agent OS can resolve those decisions itself.

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
