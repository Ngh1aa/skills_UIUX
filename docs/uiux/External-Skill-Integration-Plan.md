# External UI/UX Specialist Integration

Checked: 2026-09-06 (Asia/Ho_Chi_Minh)

## Phase classification

- Scope: `system`
- Type: `research / implementation / remediation / verification / release`
- Risk: `medium`
- Mode: `production_candidate`
- Local baseline: `35673d3983f51182ed2212590f55351908b36e03`
- Working branch: `feat/external-uiux-specialist-adapters`
- PR: `#14`
- Original implementation commit: `3a3d4ebd933a0b7ceeeb7d9c21035ab11730b9aa`
- Original implementation validation: GitHub Actions `34026113160` = `success`
- Current user change: remove the Figma integration added by PR #14, then release the remaining external-skill integration to `main`.
- Release authorization: `explicitly authorized by user on 2026-09-06`.

## Skill Activation Plan

| Task | Trigger/risk | Skill | Expected impact | Verification |
|---|---|---|---|---|
| Preserve project truth and precedence | system-level library mutation | `project-context` | external sources cannot override local contracts | inspect current core docs and branch diff |
| Prevent context overload | multiple external skill families | `adaptive-skill-routing-and-context-budget` | progressive references instead of bulk loading | routing/profile/eval review |
| Preserve lifecycle ownership | new review/design capabilities | `website-delivery-pipeline` | external skills do not become parallel orchestrators | catalog/pipeline review |
| Avoid duplicate capabilities | four remaining external sources overlap local skills | `skill-authoring-and-governance` | narrow capability boundaries, progressive disclosure, representative evals | overlap decisions + validators |

## Skill Usage Ledger

| Skill | Trigger | Requirement applied | Change created | Verification | Evidence |
|---|---|---|---|---|---|
| `project-context` | source integration/removal could compete with local truth | user/project/Design Contract precedence | Figma additions removed without deleting unrelated pre-existing reference capabilities | branch diff review | PR #14 changed-file review |
| `adaptive-skill-routing-and-context-budget` | external knowledge can bloat context | smallest useful graph; installed ≠ active | four remaining adapters stay conditional; Figma routing removed | near-miss eval + validation | `external-uiux-006-adapter-near-miss.json` |
| `website-delivery-pipeline` | capabilities must preserve canonical lifecycle | external specialists hand back to local owners | no external lifecycle replaces the canonical pipeline | catalog review + CI | `SKILL-CATALOG.md` |
| `skill-authoring-and-governance` | source overlap / removal | clear boundaries + progressive references + evals | remaining capabilities: visual taste, web/code QA, reference extraction/audit, UX writing | validators + source comparison | source locks + adapter files |

## Source findings and decisions

### FACT — Anthropic Frontend Design

Pinned: `anthropics/claude-plugins-official@85cce0381e7860082641b59d961a2b8c368b8b79`.

Decision: `ADAPT_WITH_ATTRIBUTION` through `visual-taste-calibration` and the existing `visual-design-direction` owner. Useful upstream ideas include subject-matter-grounded design, anti-template self-critique, deliberate typography/composition, restrained unsolicited motion and one memorable visual commitment.

### FACT — Vercel Web Design Guidelines + React Best Practices

Pinned:
- `vercel-labs/agent-skills@063bee94c3f4df8453406c830b0a7df0f2860278`;
- `vercel-labs/web-interface-guidelines@e3d624baaf29dc1fc645aff3e38f03e564d2d6b1`.

Decision: `ADAPT_WITH_ATTRIBUTION` through `web-ui-code-review`. The local implementation intentionally replaces the upstream mutable-runtime fetch behavior with pinned review guidance; React/Next rules activate only after actual stack/version detection.

### FACT — Design Extractor/Auditor

Pinned: `billhector/design-skills@afee427d8f1e2d9deb004a96bcaa8391c572c9f5` (MIT).

Decision: `ADAPT_WITH_ATTRIBUTION` through `reference-extraction-and-design-audit`. The local capability keeps source-attributed design-system extraction but does not require Firecrawl and does not automatically migrate every project to Tailwind.

### FACT — UX Writing & Content Design

Pinned: `hueyexe/frontend-agent-skills@2841c079dd8a9c634882227194dc42e25227710d` (MIT).

Decision: `ADAPT_WITH_ATTRIBUTION` through `ux-writing-and-microcopy` plus the broader `content-design-and-question-design` owner. Words remain part of interaction design, including task-first labels, consequence-revealing actions, complete state conversations, recovery, accessibility and localization considerations.

## Removed from this integration

Per current user instruction, all **Figma-specific additions introduced by PR #14** are removed:

- `figma-system-bridge/` package;
- the Figma-specific eval introduced in this PR;
- Figma/OpenAI source-lock entries introduced for this integration;
- Figma adapter routing/catalog/README/DesignOps-pack references introduced in this PR.

Pre-existing generic capabilities that can analyze a Figma/screenshot/reference as one input type are outside this PR-removal scope and are preserved to avoid unrelated regression.

## Architecture after remediation

```text
skills_UIUX
│
├── CORE OS
│   ├── project-context
│   ├── adaptive-skill-routing-and-context-budget
│   ├── website-delivery-pipeline
│   ├── Design Contract
│   └── QA / Release
│
├── LOCAL SPECIALISTS
│   └── ...
│
├── EXTERNAL-KNOWLEDGE PROVENANCE
│   ├── vendor/ui-ux-pro-max/
│   └── vendor/external-uiux/
│
└── SPECIALIST ADAPTERS
    ├── design-intelligence-retrieval
    ├── visual-taste-calibration
    ├── web-ui-code-review
    ├── reference-extraction-and-design-audit
    └── ux-writing-and-microcopy
```

## Requirement coverage

| ID | Requirement | OWNER_PHASE | Status | Verification |
|---|---|---|---|---|
| EXT-001 | Learn from Anthropic Frontend Design without duplicate visual orchestrator | implementation | DONE_VERIFIED | local visual-taste adapter + pinned source |
| EXT-002 | Add Vercel web UI + React/Next code review capability | implementation | DONE_VERIFIED | local review adapter + pinned sources |
| EXT-003 | Remove Figma integration introduced by PR #14 | remediation | DONE_VERIFIED after branch diff confirms no added Figma adapter/source/eval/pack routing remains | branch diff + CI |
| EXT-004 | Add reference/design-system extraction and audit | implementation | DONE_VERIFIED | extraction/audit adapter + eval |
| EXT-005 | Add microcopy/content UX specialist | implementation | DONE_VERIFIED | UX writing adapter + handoff |
| EXT-006 | Keep external sources reproducible and context-efficient | implementation | DONE_VERIFIED | `vendor/external-uiux/SOURCE-LOCKS.md` |
| EXT-007 | Structural/profile/install/eval verification | verification | PENDING_FUTURE_PHASE | final PR-head CI after remediation |
| EXT-008 | Merge remaining integration to `main` | release | PENDING_FUTURE_PHASE | explicit authorization received; merge after final CI |
| EXT-009 | Post-merge verification | release | PENDING_FUTURE_PHASE | CI on resulting `main` |

Current remediation has no known due-now blocker. Release status is not final until final PR-head and post-merge validation complete.
