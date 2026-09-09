# Default Website Delivery Policy — Adaptive Prompt OS V4

This file defines the default website-delivery operating policy for projects that use `skills_UIUX`.

Canonical policy ID:

```text
adaptive-prompt-os-v4
```

The policy is **stack-agnostic** and **domain-aware**. It applies to corporate sites, ecommerce, SaaS, education, government/public sector, hospitality, portfolio, media/news, real estate, nonprofit, landing pages and other web experiences. Project truth and routed domain skills decide the actual design; this policy decides the default delivery discipline.

## Why this is the default

The strongest website outcomes require more than a sequence of styling tasks. The default workflow therefore separates:

- project truth and configuration;
- research/reference/design intelligence;
- structural design decisions;
- implementation;
- rendered QA and human visual judgment;
- release and production smoke when authorized.

The policy is designed to prevent a common failure mode where an agent starts coding too early, produces a cosmetic reskin, passes build/CI, and only later discovers that hierarchy, page roles, media, journey or production delivery are still wrong.

## Adaptive lane selection

Do **not** run the full lifecycle mechanically for every tiny edit.

### Full Prompt OS lane — default for substantial website work

Use the full lane when the task is any of the following:

- new website or major rebuild;
- substantial redesign;
- multi-page or whole-site visual/UX change;
- critical journey redesign;
- new page family that materially changes IA, composition or conversion behavior;
- design-system/art-direction reset;
- production-candidate or production release with meaningful UI/UX change;
- a local-looking request that reveals shared-owner or cross-route risk.

Default lifecycle:

```text
PROMPT 0 — PROJECT CONFIG
        ↓
PROMPT 1 — RESEARCH / AUDIT / DESIGN CONTRACT
        ↓
PHASE 1 PASS
        ↓
PROMPT 2 — STRUCTURAL IMPLEMENTATION
        ↓
REPRESENTATIVE PAGE GATE
        ↓
WHOLE-SCOPE ROLLOUT
        ↓
PROMPT 3 — FINAL VISUAL / CONTENT / SYSTEM QA + REMEDIATION
        ↓
HUMAN VISUAL VETO
        ↓
FINAL QA PASS
        ↓
PROMPT 4 — RELEASE + PRODUCTION SMOKE, ONLY WHEN AUTHORIZED
```

### Lightweight lane — default for small, bounded work

Use the lightweight lane when the task is genuinely local/component-level, low-risk, and does not alter the product's structural design direction.

Examples:

- fix one spacing/crop/contrast defect;
- repair one broken state;
- adjust a small component without changing its role;
- correct copy in a bounded surface;
- fix an isolated accessibility or browser defect.

Lightweight lifecycle:

```text
project truth
→ classify scope/type/risk/mode
→ smallest applicable skill graph
→ inspect root owner
→ implement focused change
→ focused rendered/browser verification
→ regression check for affected shared owners
→ release only when authorized
```

Do not manufacture Prompt 0–4 artifacts for a trivial edit unless an escalation trigger fires.

## Prompt 0 — Project Config

Before substantial work, resolve at minimum:

- project name and repository/source;
- request type and project mode;
- domain/industry and audience/market when known;
- business/product goal;
- critical journeys/conversion actions when applicable;
- `must_keep`, `must_improve`, and scope boundaries;
- responsive scope;
- source of truth;
- release authorization;
- system-reality boundaries;
- immutable `skills_UIUX` version lock for the active project phase.

Unknown facts remain `UNKNOWN`; do not invent them to complete the template.

## Prompt 1 — Research, Audit and Design Contract

**No broad implementation before this phase passes for substantial website work.**

Required outcomes are selected according to task scope, but substantial redesign/build work should normally account for:

- current project/site audit or new-site baseline rationale;
- audience/top tasks and journey understanding;
- IA/page-role understanding;
- reference benchmark with source-role labels;
- focused design-intelligence retrieval only when it reduces uncertainty;
- `ADOPT / ADAPT / REJECT` synthesis for material external ideas;
- redesign delta or structural design intent;
- brand/visual direction;
- media/focal-point contract when media is material;
- Design Contract;
- representative composition proofs;
- requirement coverage and verification plan;
- phase state with `BLOCKED = 0` and `UNACCOUNTED = 0` for due-now requirements.

A substantial redesign does **not** pass when the planned delta is primarily color, typography, spacing, radius, shadow, gradient, animation, or image replacement inside the same hierarchy/composition/journey.

## Prompt 2 — Structural Implementation

Implementation order defaults to:

```text
composition
→ hierarchy
→ media
→ decision objects / task objects
→ interaction and states
→ declared responsive transformation
→ design system / component consolidation
→ visual polish
```

For multi-page, journey or whole-site work:

1. choose 2–4 representative pages/surfaces from the actual sitemap, page-role matrix, critical journeys and risk;
2. implement those first;
3. render them at declared viewports/states;
4. inspect actual screenshots;
5. fix P0/P1 structural/craft issues;
6. only then authorize broad rollout.

Representative pages are domain-specific. Do not hard-code ecommerce roles into unrelated projects.

## Prompt 3 — Final QA and Remediation

Final QA must compare the implementation against the current Design Contract and against itself across affected routes/page roles.

At minimum, when applicable, verify:

- critical journeys and interaction/recovery states;
- page-role diversity and hierarchy;
- shared-owner visual sanity across affected routes;
- media crop/load/integrity;
- responsive behavior inside declared scope;
- accessibility baseline without overstating formal conformance;
- system-reality truthfulness;
- console/page/runtime errors;
- horizontal overflow and broken/incomplete media;
- regression of preserved behavior;
- brand recognition/consistency;
- OLD→NEW comparable evidence for redesigns when a valid baseline exists.

**Build success is not rendered evidence.**

**A screenshot that exists but was not opened and inspected is not visual evidence.**

**If a screenshot is visibly wrong, automated 100/100 does not override it.**

Human/Creative-Director visual review may return:

```text
KEEP
REVISE
REMOVE
```

Material `REVISE`/`REMOVE` feedback returns to the owning stage and must be re-rendered after repair.

## Prompt 4 — Release and Production Smoke

Prompt 4 runs only when release is in scope and authorized.

Supported authorization semantics remain:

```text
no_release
create_pr_only
merge_only
merge_and_deploy
```

When deployment occurs, a successful CI/deploy job is **not** the final release proof. Production smoke must verify the real served experience, including when applicable:

- exact expected version/commit or cache-busted assets;
- production URL loads;
- representative routes;
- critical journey entry points;
- stylesheet/font/image/media loading;
- console/network/runtime sanity;
- production-only configuration differences;
- no stale asset/build issue.

A deploy can be green while production is stale or visually wrong; in that case release status is not PASS.

## System-reality boundary

Before describing a capability as working, classify it:

```text
REAL | MOCK | STATIC | SIMULATED | PARTIAL | UNKNOWN
```

No stage may convert simulated/local/browser-only behavior into a production claim merely because the UI is polished.

## Evidence and phase states

Canonical requirement states:

```text
DONE_VERIFIED
N/A_JUSTIFIED
PENDING_FUTURE_PHASE
BLOCKED
```

Only due-now requirements participate in the current phase exit gate. Future-phase evidence receives an owner phase and verification plan rather than creating an artificial blocker or fake PASS.

## Default Creative Director rule

For substantial visual work, rendered evidence must be inspected after the latest material visual change. Final taste judgment covers at least:

- hierarchy;
- composition;
- brand distinctiveness;
- image/media coherence;
- page-role diversity;
- generic-template risk;
- whether the intended brand/product feeling is actually visible, not merely documented.

The Factory/process owns repeatable orchestration and deterministic gates. Routed skills own specialist rules. Creative Director review owns final visual judgment.

## Escalation triggers

A lightweight task escalates to the full lane when any of these becomes true:

- the root owner is shared across multiple routes/page families;
- the requested change materially alters hierarchy, IA, journey or art direction;
- a new Design Contract is needed;
- media changes require cross-family art direction;
- regression scope expands materially;
- a production/high-risk concern appears;
- an assumption is invalidated;
- visual review shows the problem is structural rather than local.

## Project override rules

Precedence:

```text
current user request
→ project .uiux-profile.json / project truth
→ passed project Design Contract
→ this default policy
→ routed specialist skills
→ generic model prior
```

A project may explicitly override the default lane, responsive scope, mode, release authorization or other policy details when the override is justified by project truth/user intent.

Project overrides must not silently weaken:

- system-reality honesty;
- evidence discipline;
- release authorization;
- requirement accounting;
- the rule that visual completion requires rendered inspection.

## Canonical supporting documents

The default policy is implemented with the current canonical files in this repository:

```text
PROJECT-INSTRUCTIONS-PHASE-AWARE.md
PHASE-AWARE-GATING.md
LATEST-3-PROMPT-REDESIGN-PIPELINE.md
MASTER-PRE-DESIGN-RESEARCH-PROMPT-V4.2.md
MASTER-PROMPT-V7.2.md
FINAL-UIUX-VISUAL-CONTENT-QA-REMEDIATION-V3.2.md
website-delivery-pipeline/SKILL.md
adaptive-skill-routing-and-context-budget/SKILL.md
project-context/SKILL.md
```

The three canonical redesign prompts represent Prompt 1–3. Prompt 0 is project configuration/governance. Prompt 4 is the authorized release + production-smoke wrapper.
