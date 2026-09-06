# Cross-Functional Intelligence Upgrade

Checked: 2026-09-06 (Asia/Ho_Chi_Minh)

## Phase classification

- Scope: `system`
- Type: `research / implementation / verification`
- Risk: `medium`
- Mode: `production_candidate`
- Baseline `main`: `279c9e01ca85779fa4af2d60551fb9b1e0d16111`
- Branch: `feat/cross-functional-product-growth-intelligence`
- Release authorization: `no_release`
- Merge/deploy: `PENDING_FUTURE_PHASE`

## Skill Activation Plan

| Task | Trigger/risk | Skill | Expected impact | Verification |
|---|---|---|---|---|
| Preserve project truth while extending a system-level library | external disciplines can override local owners | `project-context` | local source-of-truth/precedence remains authoritative | inspect baseline + final diff |
| Keep new knowledge conditional | six external source families can cause context bloat | `adaptive-skill-routing-and-context-budget` | route only active cross-functional decision | catalog/router + near-miss evals |
| Preserve lifecycle ownership | PM/growth/engineering sources can become parallel orchestrators | `website-delivery-pipeline` | `skills_UIUX` remains the only lifecycle OS | pipeline/collision review |
| Decide extend vs new skill | overlap with product-discovery, conversion, analytics, SEO, guardrails | `skill-authoring-and-governance` | four new boundaries; four existing owners extended instead of duplicated | overlap review + validators |
| Ground external claims | time-sensitive/quantitative source material | `evidence-provenance-and-research-ops` | exact SHAs/licenses/adoption decisions and UNKNOWN/NO_DATA rules | source-lock ledger |
| Protect routing/outcome behavior | new specialists may trigger too broadly | `agent-evaluation-and-reliability` | positive + near-miss capability tasks | eval schema + harness/CI |

## Skill Usage Ledger

| Skill | Trigger | Requirement applied | Change created | Verification | Evidence |
|---|---|---|---|---|---|
| `project-context` | system-level external integration | user/project truth above generic external advice | all new skills state local precedence/UNKNOWN discipline | source/diff review | baseline project docs |
| `adaptive-skill-routing-and-context-budget` | context risk | smallest active decision graph | added product/growth/search/experiment routing + near-misses | routing evals | updated router |
| `website-delivery-pipeline` | lifecycle collision risk | no second orchestrator | cross-functional skills are specialists/pack only; pipeline retained | architecture review | catalog/source-lock docs |
| `skill-authoring-and-governance` | capability creation/overlap | distinct owner + progressive reference + eval | 4 new skills; existing analytics/conversion/SEO/guardrails extended | structural validators | skill packages/evals |
| `evidence-provenance-and-research-ops` | external research claims | source/date/confidence/limitations | exact source locks; NO_DATA/UNKNOWN; no fake CRO/search/stat claims | provenance review | source-lock ledger |
| `agent-evaluation-and-reliability` | behavior reliability | representative positive/negative/complex evals | six new eval tasks | eval harness/CI | `evals/tasks/cross-functional-*` |

## Source research and locks

### FACT — ProductSkills

Pinned `assimovt/productskills@66f9cee5868d6daf9cf106b4a74090428d6fa83e` (MIT). Reviewed actual positioning, prioritization, scope-cutting, metrics and experiment-design skills. Useful concepts: competitive-alternative-first positioning, RICE with confidence, blocker/enabler lens, appetite/fixed-time-variable-scope, counter-metrics and pre-registered experiment hypotheses.

Decision: `ADAPT_WITH_ATTRIBUTION`. Do not copy universal scope/duration heuristics or fabricate quantitative inputs.

### FACT — Mind the Product

Pinned `mindtheproduct/skills@3fb3d46092c4149d1653fc317aed77d63f2a98ca` (MIT). Reviewed `make-the-call` and its three stages: translate asks to problems; stress-test evidence/blind spots/impact; pick using leverage/reversibility/strategic ground while the user owns the call.

Decision: `ADAPT_WITH_ATTRIBUTION`. Interactive turn rules are adapted for autonomous project phases using project evidence and UNKNOWN gaps.

### FACT — ai-vita marketing skills

Pinned `ai-vita/skills@dda98df83ec242cf32c208a0a78b759f0b3e658b` (MIT). Reviewed `page-cro` and `copywriting`: page type/conversion/traffic context, value proposition, CTA/hierarchy, proof, objections/friction, clarity/customer language, page-specific argument patterns.

Decision: extend `conversion-and-content`; no separate CRO orchestrator. Best-practice findings remain hypotheses until measured.

### FACT — Rampstack experimentation analytics

Pinned `rampstackco/claude-skills@a67dd34c609f034c0cfd736a348659bbdf1605bf` (MIT). Reviewed completed-result interpretation covering CIs, p-values, multiple/sequential testing, CUPED, heterogeneous treatment effects, ratio/network effects and dashboard reconciliation.

Decision: create `experimentation-interpretation` because pre-run `analytics-and-experimentation` and post-run result reading are materially different decision boundaries.

### FACT — Addy Osmani agent skills

Pinned `addyosmani/agent-skills@48cb1168aeaaa70dfc2bbf709eddfa2a8ed8129a` (MIT). Reviewed context engineering and planning/task breakdown: context hierarchy/trust, conflict handling, dependency graphs, vertical slices and checkpoints.

Decision: extend existing `ai-agent-coding-guardrails`; do not add a duplicate engineering lifecycle.

### FACT — mblode SEO Program

Pinned `mblode/agent-skills@0a639b1ef3b75aa6cc945e778fb1486def1d41bf` (MIT). Reviewed `seo-program`: current demand data, natural-language question maps, decision-shaped content briefs, evidence tables, `No data` discipline and search monitoring.

Decision: create `search-demand-and-content-briefing` and narrow `seo-strategy` to technical/on-page implementation. Vendor-specific/timely search claims are not copied as durable facts.

## Architecture

```text
skills_UIUX CORE OS
  project-context
  adaptive router
  website-delivery-pipeline
  Design Contract / evidence / QA / release
        ↓
LOCAL UX OWNERS
        ↓
CROSS-FUNCTIONAL SPECIALISTS (conditional)
  product-decision-and-stakeholder-framing
  product-strategy-and-prioritization
  conversion-and-content (upgraded)
  analytics-and-experimentation (upgraded)
  experimentation-interpretation
  search-demand-and-content-briefing
  seo-strategy (technical boundary)
  ai-agent-coding-guardrails (upgraded)
        ↓
PINNED EXTERNAL KNOWLEDGE / PROVENANCE
```

No external source becomes equal to project truth or a second lifecycle orchestrator.

## Capability changes

### New
- `product-decision-and-stakeholder-framing`
- `product-strategy-and-prioritization`
- `experimentation-interpretation`
- `search-demand-and-content-briefing`
- `packs/product-growth-intelligence.json`
- `vendor/cross-functional-intelligence/*`

### Extended
- `conversion-and-content` → traffic/message match, CRO diagnostic, proof/objection/CTA and testable hypothesis discipline.
- `analytics-and-experimentation` → outcome/counter-metric tree + pre-run experiment design; tracking remains evidence/privacy-aware.
- `seo-strategy` → explicit technical/on-page boundary, removes brittle universal metadata/link quotas.
- `ai-agent-coding-guardrails` → context trust/budget, dependency-aware tasks, vertical slices/checkpoints.
- `adaptive-skill-routing-and-context-budget` → cross-functional routing and near-miss logic.

## Collision rules

- `product-discovery` discovers problem/audience/JTBD; `product-decision...` resolves ambiguous asks; `product-strategy...` ranks/scopes after evidence is sufficient.
- `conversion-and-content` handles marketing-page argument; `ux-writing-and-microcopy` retains product state/string copy.
- `analytics-and-experimentation` is pre-run; `experimentation-interpretation` is post-result.
- `search-demand-and-content-briefing` researches demand/brief; `seo-strategy` implements technical/on-page SEO.
- `ai-agent-coding-guardrails` remains proportional and does not force planning ceremony on tiny fixes.

## Requirement coverage

| ID | Requirement | OWNER_PHASE | Status | Verification |
|---|---|---|---|---|
| CFI-001 | Product strategy/prioritization intelligence | implementation | DONE_VERIFIED | new skill/reference + source pin |
| CFI-002 | Stakeholder/product-call framing | implementation | DONE_VERIFIED | new skill/reference + source pin |
| CFI-003 | CRO/marketing copy intelligence | implementation | DONE_VERIFIED | upgraded `conversion-and-content` + source pin |
| CFI-004 | Experiment design + result interpretation | implementation | DONE_VERIFIED | upgraded analytics + new interpretation skill |
| CFI-005 | Search demand/content brief intelligence | implementation | DONE_VERIFIED | new search skill + SEO boundary |
| CFI-006 | Engineering/context/planning complement | implementation | DONE_VERIFIED | upgraded coding guardrails |
| CFI-007 | Adaptive conditional routing / avoid context bloat | implementation | DONE_VERIFIED | router + pack + near-miss eval |
| CFI-008 | Reproducible provenance/licenses | implementation | DONE_VERIFIED | source locks |
| CFI-009 | Representative eval coverage | verification | PENDING_FUTURE_PHASE | run validators/eval harness on branch head |
| CFI-010 | PR-head CI | verification | PENDING_FUTURE_PHASE | GitHub Actions after commit/PR |
| CFI-011 | Merge to main | release | PENDING_FUTURE_PHASE | requires explicit user release authorization |

## Current phase result

Before branch-head validators/CI complete: `BLOCKED` only if a due-now implementation/verification gate fails. Merge is not due now under `no_release`; it remains `PENDING_FUTURE_PHASE`.
