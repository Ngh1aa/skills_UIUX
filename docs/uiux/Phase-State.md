# Phase State

## Current phase

- Scope: `system`
- Type: `research / implementation / verification`
- Risk: `medium`
- Mode: `production_candidate`
- Branch: `feat/external-uiux-specialist-adapters`
- PR: `#14` — open
- Local baseline: `35673d3983f51182ed2212590f55351908b36e03`
- Implementation commit: `3a3d4ebd933a0b7ceeeb7d9c21035ab11730b9aa`
- Implementation validation: GitHub Actions `34026113160` = `success`
- UI UX Pro Max lock: `314307f156aeab0c6b567bbaa1ce4e7aabd5a636`
- External source locks: `vendor/external-uiux/SOURCE-LOCKS.md`
- Release authorization: `no_release`

## Phase result

`PASSED`

Rationale: all five requested knowledge areas were integrated as narrow local specialist adapters with immutable provenance, progressive disclosure and explicit owner boundaries; profiles/packs/routing/evals were updated; the complete validation/install/retrieval/bootstrap/eval workflow passed on the implementation commit; `main` was unchanged when the PR was opened.

## Gate accounting

- DUE-NOW `BLOCKED`: 0
- DUE-NOW `UNACCOUNTED`: 0
- Source/provenance review: `DONE_VERIFIED`
- Adapter capability implementation: `DONE_VERIFIED`
- Routing/profile integration: `DONE_VERIFIED`
- Structural/install/eval verification: `DONE_VERIFIED`
- Reviewable PR handoff: `DONE_VERIFIED`
- Merge to `main`: `PENDING_FUTURE_PHASE`

## Verified evidence

- Anthropic Frontend Design pinned at `85cce0381e7860082641b59d961a2b8c368b8b79` with Apache-2.0 source license observed;
- Vercel Agent Skills pinned at `063bee94c3f4df8453406c830b0a7df0f2860278` and Web Interface Guidelines at `e3d624baaf29dc1fc645aff3e38f03e564d2d6b1` with MIT licensing observed;
- OpenAI Figma workflow pinned at `1e285826e604f66f7208f7ac4dba0fe8341d1f57` and Figma MCP guide at `ae7e5e5f80da20f1dd7445e0c6ae5ac58a5b0bce`, used as `REFERENCE_ONLY` rather than copied source;
- Bill Hector design skills pinned at `afee427d8f1e2d9deb004a96bcaa8391c572c9f5` with MIT licensing observed;
- Huey frontend agent skills pinned at `2841c079dd8a9c634882227194dc42e25227710d` with MIT licensing observed;
- new adapters: `visual-taste-calibration`, `web-ui-code-review`, `figma-system-bridge`, `reference-extraction-and-design-audit`, `ux-writing-and-microcopy`;
- `professional-core` and `prototype-uiux` install common context-light adapters; `figma-system-bridge` routes through `designops-governance`;
- six new eval cases include a near-miss that rejects all external adapters for a known-token local fix;
- `Validate Skills` run `34026113160` completed successfully across structure, V5 resources, vendor integrity, retrieval, installer, bootstrap and eval smoke;
- PR `#14` opened from exact baseline `35673d3983f51182ed2212590f55351908b36e03` with no merge performed.

Detailed source/adoption decisions and requirement coverage: `docs/uiux/External-Skill-Integration-Plan.md`.
Source provenance: `vendor/external-uiux/SOURCE-LOCKS.md`.

## Handoff rule

Review PR #14. Do not merge to `main` until explicit release authorization is provided. Any change to external source pins, adapter boundaries, generic profiles, `designops-governance`, or the UI UX Pro Max vendor reopens the relevant verification gates.
