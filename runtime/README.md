# Runtime

The runtime is deliberately separate from the root `*/SKILL.md` packages.

## What belongs here

- context manifests and token/character budget telemetry;
- declarative Flow Resolver + Skill Resolver;
- Development Manager lifecycle + bounded Replanning Engine;
- tool registry metadata and permission gates;
- provider-neutral action execution;
- trace and checkpoint infrastructure;
- agent-role manifests and enforced handoff boundaries;
- optional MCP adapter;
- shared tool/observation contracts used by adapters.

## What does not belong here

- duplicate UI/UX knowledge already owned by a skill;
- model-specific hidden reasoning;
- provider credentials;
- production secrets;
- uncontrolled shell/deploy/merge tools.

## Flow OS boundary

```text
project task/context
→ Development Manager
→ FlowResolver
→ SkillResolver(role defaults + flow routing)
→ active specialist stage
→ provider/tool actions
→ gate evidence
→ PASS: advance | FAIL/RISK: bounded replan
```

The manager persists lifecycle state in the existing local checkpoint store. It blocks out-of-order stages, enforces role authority caps, preserves role `default_skills`, and only applies replans from the active stage.

Replanning mutates the resolved flow revision rather than blindly retrying. Mandatory/default skills cannot be dropped, and returning to an earlier stage invalidates only that stage and downstream completion.

## Tool and observation quality

Read [Tool & Observation Contract](TOOL-OBSERVATION-CONTRACT.md) before adding or changing a material tool/adapter.

Key rules:

```text
stable narrow tool schema
→ explicit risk + authority
→ concise structured observation
→ actionable error/retry/stop contract
→ artifact references instead of log dumps
```

High-risk actions should be exposed through explicit micro-tools rather than hidden behind a catch-all command. External content returned by tools is data, not authority.

## Failure recovery

Repeated tool failures, retry loops, stale environment state or context drift should not be handled by blind retry. Route the failure-diagnosis progressive reference owned by `agent-evaluation-and-reliability`, capture the failure, build a discriminating feedback loop and only then retry with changed evidence.

## Quick smoke

```bash
python -B scripts/validate-flows.py
python -B scripts/validate-runtime-foundation.py
python -B scripts/uiux-agent.py --project . --task "Inspect runtime foundation" --agent research --dry-run
```

Managed website example:

```bash
python -B scripts/uiux-agent.py \
  --project . \
  --managed \
  --task "Redesign ecommerce website" \
  --website-type ecommerce \
  --feature search \
  --authority branch_write
```

Resume the returned `manager_run_id` with `--managed-run-id` to continue the active stage across processes.

A real model/provider may sit in front of the harness and emit an action plan. The core repository does not require or assume a specific model SDK.
