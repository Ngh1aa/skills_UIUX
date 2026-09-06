# Phase State

## Current phase

- Scope: `system`
- Type: `remediation / verification / release`
- Risk: `medium`
- Mode: `production_candidate`
- Branch: `feat/external-uiux-specialist-adapters`
- PR: `#14` — open
- Local baseline: `35673d3983f51182ed2212590f55351908b36e03`
- Original implementation commit: `3a3d4ebd933a0b7ceeeb7d9c21035ab11730b9aa`
- Original implementation validation: GitHub Actions `34026113160` = `success`
- UI UX Pro Max lock: `314307f156aeab0c6b567bbaa1ce4e7aabd5a636`
- External source locks: `vendor/external-uiux/SOURCE-LOCKS.md`
- Current remediation: remove Figma-specific additions introduced by PR #14.
- Release authorization: `explicitly authorized by user on 2026-09-06`.

## Phase result

`PENDING VERIFICATION`

The remaining external-skill integration keeps four sources: Anthropic Frontend Design, Vercel Web Design Guidelines + React Best Practices, Design Extractor/Auditor, and UX Writing & Content Design. Figma-specific additions from PR #14 are being removed before release.

## Gate accounting

- DUE-NOW `BLOCKED`: 0
- DUE-NOW `UNACCOUNTED`: 0
- Figma-specific remediation: `DONE_VERIFIED` once branch diff confirms removal set
- Remaining adapter capability implementation: `DONE_VERIFIED`
- Final PR-head structural/install/eval verification: `PENDING_FUTURE_PHASE`
- Merge to `main`: `PENDING_FUTURE_PHASE` with authorization granted
- Post-merge verification: `PENDING_FUTURE_PHASE`

## Current verified evidence

- Anthropic Frontend Design remains pinned at `85cce0381e7860082641b59d961a2b8c368b8b79`;
- Vercel Agent Skills remains pinned at `063bee94c3f4df8453406c830b0a7df0f2860278` and Web Interface Guidelines at `e3d624baaf29dc1fc645aff3e38f03e564d2d6b1`;
- Bill Hector design skills remains pinned at `afee427d8f1e2d9deb004a96bcaa8391c572c9f5`;
- Huey frontend agent skills remains pinned at `2841c079dd8a9c634882227194dc42e25227710d`;
- remaining adapters are `visual-taste-calibration`, `web-ui-code-review`, `reference-extraction-and-design-audit`, and `ux-writing-and-microcopy`;
- Figma-specific additions introduced by this PR are intentionally removed without deleting unrelated pre-existing reference-analysis behavior.

Detailed decisions and coverage: `docs/uiux/External-Skill-Integration-Plan.md`.

## Handoff rule

Run the full repository validation on the final remediated PR head. Merge PR #14 only if that exact head passes and the PR remains mergeable against the expected `main` base. After merge, rerun/confirm validation on resulting `main` before marking release `PASSED`.
