# Phase State

## Current phase

- Scope: `system`
- Type: `research / implementation`
- Risk: `medium`
- Mode: `production_candidate`
- Branch: `feat/external-uiux-specialist-adapters`
- PR: `PENDING_CREATE`
- Local baseline: `35673d3983f51182ed2212590f55351908b36e03`
- UI UX Pro Max lock: `314307f156aeab0c6b567bbaa1ce4e7aabd5a636`
- External source locks: `vendor/external-uiux/SOURCE-LOCKS.md`
- Release authorization: `no_release`

## Phase result

`PENDING VERIFICATION`

The requested external specialist capabilities have been researched and mapped to narrow local adapters, but the phase does not pass until catalog/profile/install/eval validation succeeds on the branch head.

## Gate accounting

- DUE-NOW `BLOCKED`: 0
- DUE-NOW `UNACCOUNTED`: 0
- Source/provenance review: `DONE_VERIFIED`
- Adapter capability implementation: `DONE_VERIFIED`
- Routing/profile integration: `PENDING_FUTURE_PHASE`
- Structural/install/eval verification: `PENDING_FUTURE_PHASE`
- Merge to `main`: `PENDING_FUTURE_PHASE`

## Implemented adapters

- `visual-taste-calibration` — subject-matter/anti-template calibration informed by Anthropic Frontend Design;
- `web-ui-code-review` — pinned web-interface review + conditional React/Next performance synthesis informed by Vercel;
- `figma-system-bridge` — canonical Design Contract/code ↔ Figma synchronization workflow informed by OpenAI/Figma references;
- `reference-extraction-and-design-audit` — source-attributed reference/current-system extraction informed by Bill Hector design skills;
- `ux-writing-and-microcopy` — state-level product copy/recovery patterns informed by Huey UX writing.

Detailed plan/coverage: `docs/uiux/External-Skill-Integration-Plan.md`.
Source provenance: `vendor/external-uiux/SOURCE-LOCKS.md`.

## Handoff rule

Finish routing/profile/eval integration, run GitHub Actions and representative eval/installer smoke, then open a PR. Do not merge to `main` without a later explicit release instruction.
