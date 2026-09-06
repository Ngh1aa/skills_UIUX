# Runtime

The runtime is deliberately separate from the root `*/SKILL.md` packages.

## What belongs here

- context manifests and token/character budget telemetry;
- tool registry metadata and permission gates;
- provider-neutral action execution;
- trace and checkpoint infrastructure;
- agent-role manifests and handoff boundaries;
- optional MCP adapter.

## What does not belong here

- duplicate UI/UX knowledge already owned by a skill;
- model-specific hidden reasoning;
- provider credentials;
- production secrets;
- uncontrolled shell/deploy/merge tools.

## Quick smoke

```bash
python -B scripts/validate-runtime-foundation.py
python -B scripts/uiux-agent.py --project . --task "Inspect runtime foundation" --agent research --dry-run
```

A real model/provider may sit in front of the harness and emit an action plan. The core repository does not require or assume a specific model SDK.
