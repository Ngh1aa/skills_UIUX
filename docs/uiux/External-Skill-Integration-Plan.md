# External UI/UX Specialist Integration

Checked: 2026-09-06 (Asia/Ho_Chi_Minh)

## Phase classification

- Scope: `system`
- Type: `research / implementation`
- Risk: `medium`
- Mode: `production_candidate`
- Local baseline: `35673d3983f51182ed2212590f55351908b36e03`
- Working branch: `feat/external-uiux-specialist-adapters`
- Release authorization: `no_release`

## Skill Activation Plan

| Task | Trigger/risk | Skill | Expected impact | Verification |
|---|---|---|---|---|
| Preserve project truth and precedence | system-level library mutation | `project-context` | external sources cannot override local contracts | inspect current main/core docs |
| Prevent context overload | multiple external skill families | `adaptive-skill-routing-and-context-budget` | adapters + progressive references instead of bulk loading | profile/catalog/routing review + evals |
| Preserve lifecycle ownership | new review/design capabilities | `website-delivery-pipeline` | skills enter the right phase and do not become parallel orchestrators | pipeline/catalog checks |
| Avoid duplicate capabilities | five requested external sources overlap local skills | `skill-authoring-and-governance` | narrow adapter boundaries, progressive disclosure, representative evals | overlap decision log + validators |

## Source findings

### FACT — Anthropic Frontend Design

Pinned: `anthropics/claude-plugins-official@85cce0381e7860082641b59d961a2b8c368b8b79`.

Useful capabilities:
- subject-matter-grounded visual choices;
- anti-template/anti-generic self-critique;
- deliberate typography/composition;
- restrained non-user-triggered motion;
- one memorable visual commitment rather than many decorations.

Decision: `ADAPT`. It overlaps local `visual-design-direction`, so the new local capability is a narrow calibration adapter: `visual-taste-calibration`.

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

Decision: `ADAPT`. Create `web-ui-code-review` with pinned local references; no mutable runtime fetch.

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

Decision: `ADAPT / REFERENCE_ONLY`. Create `figma-system-bridge`. No upstream Figma/OpenAI source text is copied because redistribution terms were not established in this review; only provenance + local synthesis are stored.

### FACT — Design Extractor/Auditor

Pinned: `billhector/design-skills@afee427d8f1e2d9deb004a96bcaa8391c572c9f5` (MIT).

Useful capabilities:
- structured extraction of colors/type/spacing/radius/elevation/layout/responsive/components;
- source-attributed audit of current project style systems;
- separation of dark-mode evidence from fabrication;
- accessibility observations attached to extracted system evidence.

Decision: `ADAPT`. Create `reference-extraction-and-design-audit`, but remove mandatory Firecrawl and Tailwind migration assumptions.

### FACT — UX Writing & Content Design

Pinned: `hueyexe/frontend-agent-skills@2841c079dd8a9c634882227194dc42e25227710d` (MIT).

Useful capabilities:
- words as interaction material;
- task/state-first microcopy;
- consequence-revealing actions;
- Avoid→Explain→Resolve errors;
- accessibility/localization/system-state awareness.

Decision: `ADAPT`. Create narrow `ux-writing-and-microcopy`, while existing `content-design-and-question-design` keeps broader question/content-flow ownership.

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
│   ├── vendor/ui-ux-pro-max/          # complete pinned runtime/data snapshot
│   └── vendor/external-uiux/          # source locks + adoption decisions
│
└── SPECIALIST ADAPTERS
    ├── design-intelligence-retrieval
    ├── visual-taste-calibration
    ├── web-ui-code-review
    ├── figma-system-bridge
    ├── reference-extraction-and-design-audit
    └── ux-writing-and-microcopy
```

External repositories are not bulk-loaded into prompt context. Deeper knowledge is read only through the adapter's directly linked references.

## Requirement coverage

| ID | Requirement | OWNER_PHASE | Status | Verification |
|---|---|---|---|---|
| EXT-001 | Learn from Anthropic Frontend Design without duplicate visual orchestrator | implementation | DONE_VERIFIED | `visual-taste-calibration` + pinned reference |
| EXT-002 | Add Vercel web UI + React/Next code review capability | implementation | DONE_VERIFIED | `web-ui-code-review` + two pinned references |
| EXT-003 | Add Design Contract ↔ Figma ↔ code bridge | implementation | DONE_VERIFIED | `figma-system-bridge` + reference-only source contract |
| EXT-004 | Add reference/design-system extraction and audit | implementation | DONE_VERIFIED | `reference-extraction-and-design-audit` |
| EXT-005 | Add microcopy/content UX specialist | implementation | DONE_VERIFIED | `ux-writing-and-microcopy` |
| EXT-006 | Keep external sources reproducible and context-efficient | implementation | DONE_VERIFIED | `vendor/external-uiux/SOURCE-LOCKS.md` + no mutable runtime fetch |
| EXT-007 | Route/install new capabilities without loading them by default | implementation | PENDING_FUTURE_PHASE | catalog/profile/router changes + validators/evals |
| EXT-008 | Structural/profile/eval verification | verification | PENDING_FUTURE_PHASE | GitHub Actions + eval harness |
| EXT-009 | Merge to `main` | release | PENDING_FUTURE_PHASE | explicit release authorization required |

## Current phase result

`PENDING VERIFICATION`

No due-now blocker has been identified. Release remains a separately owned future phase.
