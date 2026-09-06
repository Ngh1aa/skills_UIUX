# External UI/UX Specialist Integration

Checked: 2026-09-06 (Asia/Ho_Chi_Minh)

## Phase classification

- Scope: `system`
- Type: `research / implementation / verification`
- Risk: `medium`
- Mode: `production_candidate`
- Local baseline: `35673d3983f51182ed2212590f55351908b36e03`
- Working branch: `feat/external-uiux-specialist-adapters`
- PR: `#14`
- Implementation commit: `3a3d4ebd933a0b7ceeeb7d9c21035ab11730b9aa`
- Implementation validation: GitHub Actions `Validate Skills` run `34026113160` = `success`
- Release authorization: `no_release`

## Skill Activation Plan

| Task | Trigger/risk | Skill | Expected impact | Verification |
|---|---|---|---|---|
| Preserve project truth and precedence | system-level library mutation | `project-context` | external sources cannot override local contracts | inspect current main/core docs |
| Prevent context overload | multiple external skill families | `adaptive-skill-routing-and-context-budget` | adapters + progressive references instead of bulk loading | profile/catalog/routing review + evals |
| Preserve lifecycle ownership | new review/design capabilities | `website-delivery-pipeline` | skills enter the right phase and do not become parallel orchestrators | canonical lifecycle retained; adapter owner boundaries audited |
| Avoid duplicate capabilities | five requested external sources overlap local skills | `skill-authoring-and-governance` | narrow adapter boundaries, progressive disclosure, representative evals | overlap decisions + validators + near-miss eval |

## Skill Usage Ledger

| Skill | Trigger | Requirement applied | Change created | Verification | Evidence |
|---|---|---|---|---|---|
| `project-context` | external sources could compete with local truth | project/user/Design Contract precedence | every adapter declares local source precedence and truthful system reality | source/skill review | adapter SKILL.md files + source-lock ledger |
| `adaptive-skill-routing-and-context-budget` | five additional knowledge families could increase context | smallest useful graph; progressive disclosure; escalate not preload | external adapters use short SKILL.md + direct references; Figma conditional; React conditional; extraction only on selected refs | near-miss eval + V5 validation | `external-uiux-006-adapter-near-miss.json`, run `34026113160` |
| `website-delivery-pipeline` | capabilities must not become competing orchestrators | keep research/design/implementation/QA/release ownership phase-aware | adapters explicitly hand findings to existing owners; no external lifecycle replaces canonical pipeline | catalog/routing review + eval smoke | `SKILL-CATALOG.md`, adapter boundaries, run `34026113160` |
| `skill-authoring-and-governance` | source overlap > risk of duplicate skills | capability boundary, progressive resources, representative positive/negative evals | five narrow adapters, source-lock ledger, six evals; existing content/question skill updated for handoff | structural/V5/eval validation | run `34026113160` |

## Source findings and decisions

### FACT — Anthropic Frontend Design

Pinned: `anthropics/claude-plugins-official@85cce0381e7860082641b59d961a2b8c368b8b79`.

Useful capabilities:
- subject-matter-grounded visual choices;
- anti-template/anti-generic self-critique;
- deliberate typography/composition;
- restrained non-user-triggered motion;
- one memorable visual commitment rather than many decorations.

Decision: `ADAPT_WITH_ATTRIBUTION`. It overlaps local `visual-design-direction`, so the local capability is a narrow calibration adapter: `visual-taste-calibration`.

### FACT — Vercel Web Design Guidelines + React Best Practices

Pinned:
- `vercel-labs/agent-skills@063bee94c3f4df8453406c830b0a7df0f2860278`;
- `vercel-labs/web-interface-guidelines@e3d624baaf29dc1fc645aff3e38f03e564d2d6b1`.

Useful capabilities:
- code-level web-interface checklist;
- prioritized React/Next performance review;
- action/error copy guidance embedded in UI review;
- strong focus on source-level implementation quality.

Conflict: upstream `web-design-guidelines` fetches mutable `main` at review time. Local governance requires reproducibility.

Decision: `ADAPT_WITH_ATTRIBUTION`. `web-ui-code-review` uses pinned local references; no mutable runtime fetch.

### FACT — Figma Generate Library / Figma MCP workflow

Pinned:
- `openai/plugins@1e285826e604f66f7208f7ac4dba0fe8341d1f57`;
- `figma/mcp-server-guide@ae7e5e5f80da20f1dd7445e0c6ae5ac58a5b0bce`.

Useful capabilities:
- discovery before write;
- code↔Figma gap analysis;
- variables/tokens before components;
- library reuse before new components;
- Code Connect/actual-component mapping;
- sequential stateful mutations and visual validation.

Decision: `REFERENCE_ONLY` for upstream source text. `figma-system-bridge` is a local workflow synthesis. No OpenAI/Figma source text is vendored because redistribution terms were not established in this review.

### FACT — Design Extractor/Auditor

Pinned: `billhector/design-skills@afee427d8f1e2d9deb004a96bcaa8391c572c9f5` (MIT).

Useful capabilities:
- structured extraction of colors/type/spacing/radius/elevation/layout/responsive/components;
- source-attributed audit of current project style systems;
- separation of dark-mode evidence from fabrication;
- accessibility observations attached to extracted system evidence.

Decision: `ADAPT_WITH_ATTRIBUTION`. `reference-extraction-and-design-audit` removes mandatory Firecrawl and automatic Tailwind migration assumptions.

### FACT — UX Writing & Content Design

Pinned: `hueyexe/frontend-agent-skills@2841c079dd8a9c634882227194dc42e25227710d` (MIT).

Useful capabilities:
- words as interaction material;
- task/state-first microcopy;
- consequence-revealing actions;
- Avoid→Explain→Resolve errors;
- accessibility/localization/system-state awareness.

Decision: `ADAPT_WITH_ATTRIBUTION`. `ux-writing-and-microcopy` owns string/state-level product copy while existing `content-design-and-question-design` keeps broader question/content-flow ownership.

## Architecture after integration

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
│   ├── visual-design-direction
│   ├── accessibility
│   ├── responsive-and-device-strategy
│   ├── ui-craft-and-visual-qa
│   └── ...
│
├── EXTERNAL-KNOWLEDGE PROVENANCE
│   ├── vendor/ui-ux-pro-max/          # complete pinned public runtime/data snapshot
│   └── vendor/external-uiux/          # source locks + adoption decisions, not bulk repo dumps
│
└── SPECIALIST ADAPTERS
    ├── design-intelligence-retrieval
    ├── visual-taste-calibration
    ├── web-ui-code-review
    ├── figma-system-bridge
    ├── reference-extraction-and-design-audit
    └── ux-writing-and-microcopy
```

External repositories are not bulk-loaded into prompt context. Deeper knowledge is read only through an adapter's directly linked references.

## Routing / installation decisions

- `professional-core` and `prototype-uiux` install the four context-light, commonly useful adapters: reference extraction, visual taste, UX writing and web UI/code review. Installation does not imply activation.
- `figma-system-bridge` is installed through the `designops-governance` pack rather than generic profiles because it requires Figma-specific task/tool reality.
- `adaptive-skill-routing-and-context-budget` includes explicit trigger and near-miss rules for all five adapters.
- `content-design-and-question-design` delegates exact state-string problems to `ux-writing-and-microcopy` instead of duplicating its workflow.

## Verification evidence

Implementation commit: `3a3d4ebd933a0b7ceeeb7d9c21035ab11730b9aa`.

`Validate Skills` run `34026113160` = `success` across:

- `validate-skills.py` structure checks;
- V5 profiles/packs/project configs/evals/resources validation;
- vendored UI UX Pro Max integrity;
- source design-intelligence retrieval smoke;
- core profile installer dry-run;
- installed design-intelligence dependency smoke;
- project-aware installer dry-run with packs;
- project bootstrap/sync smoke;
- provider-neutral eval harness smoke.

Compare against baseline: `29 files changed`, `1656 additions`, `62 deletions`; branch is one commit ahead and zero behind the unchanged baseline.

## Requirement coverage

| ID | Requirement | OWNER_PHASE | Status | Verification |
|---|---|---|---|---|
| EXT-001 | Learn from Anthropic Frontend Design without duplicate visual orchestrator | implementation | DONE_VERIFIED | `visual-taste-calibration` + pinned reference + validation |
| EXT-002 | Add Vercel web UI + React/Next code review capability | implementation | DONE_VERIFIED | `web-ui-code-review` + two pinned references + validation |
| EXT-003 | Add Design Contract ↔ Figma ↔ code bridge | implementation | DONE_VERIFIED | `figma-system-bridge` + reference-only source contract + pack validation |
| EXT-004 | Add reference/design-system extraction and audit | implementation | DONE_VERIFIED | `reference-extraction-and-design-audit` + eval |
| EXT-005 | Add microcopy/content UX specialist | implementation | DONE_VERIFIED | `ux-writing-and-microcopy` + content-owner handoff + eval |
| EXT-006 | Keep external sources reproducible and context-efficient | implementation | DONE_VERIFIED | `vendor/external-uiux/SOURCE-LOCKS.md`; no mutable runtime fetch |
| EXT-007 | Route/install new capabilities without loading them by default | implementation | DONE_VERIFIED | catalog, adaptive router, profiles/designops pack, near-miss eval |
| EXT-008 | Structural/profile/install/eval verification | verification | DONE_VERIFIED | Actions run `34026113160` = success |
| EXT-009 | Open reviewable PR without release | handoff | DONE_VERIFIED | PR `#14` open; `main` unchanged at baseline when opened |
| EXT-010 | Merge to `main` | release | PENDING_FUTURE_PHASE | explicit future release authorization required |

## Phase result

`PASSED`

DUE-NOW `BLOCKED = 0`; DUE-NOW `UNACCOUNTED = 0`. Merge remains owned by a future release phase and is not required for this implementation phase to pass.
