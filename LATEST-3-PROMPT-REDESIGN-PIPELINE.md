# Latest 3-Prompt Redesign Pipeline

This pipeline is the canonical Prompt 1–3 core inside the cross-project default policy:

```text
DEFAULT-WEBSITE-DELIVERY-POLICY.md
policy id: adaptive-prompt-os-v4
```

For substantial website work the complete default lifecycle is:

```text
Prompt 0 — Project Config
→ Prompt 1 — Pre-design research / audit / Design Contract
→ Prompt 2 — Structural implementation + representative gate + rollout
→ Prompt 3 — Final visual/content/system QA + remediation + human visual veto
→ Prompt 4 — Authorized release + production smoke
```

The three versioned redesign prompts in this file implement Prompt 1–3. Prompt 0 is governed by project configuration/phase-aware instructions. Prompt 4 runs only when release is authorized.

Use these versions for substantial website redesigns:

1. `MASTER-PRE-DESIGN-RESEARCH-PROMPT-V4.2.md`
2. `MASTER-PROMPT-V7.2.md`
3. `FINAL-UIUX-VISUAL-CONTENT-QA-REMEDIATION-V3.2.md`

Mandatory orchestration rules:

```text
DEFAULT-WEBSITE-DELIVERY-POLICY.md
website-delivery-pipeline/SKILL.md
PHASE-AWARE-GATING.md
```

Conditional design-intelligence augmentation when the active design/redesign decision benefits from the vendored UI UX Pro Max corpus:

```text
design-intelligence-retrieval/SKILL.md
DESIGN-INTELLIGENCE-AUGMENTED-REDESIGN-PROMPT.md
```

Do not activate the vendor corpus merely because it is installed. Project truth/domain/audience/page role must be known first, and retrieval must use the smallest relevant mode (`--design-system`, one explicit `--domain`, or detected `--stack`).

Mandatory hard gates when applicable:

```text
visual-redesign-delta-gate
media-crop-and-layout-integrity
```

## Adaptive lane rule

This 3-prompt core is **not** required for every tiny UI edit. Under `adaptive-prompt-os-v4`:

- substantial build/redesign/multi-page/journey/whole-site/system work → full Prompt 0→4 lifecycle;
- genuinely local/component low-risk work → lightweight lane using the smallest applicable skill graph and focused rendered/browser verification;
- lightweight work escalates when the root cause becomes shared, structural, cross-route, art-direction, production/high-risk or otherwise material.

## Phase-aware requirement states

```text
DONE_VERIFIED
N/A_JUSTIFIED
PENDING_FUTURE_PHASE
BLOCKED
```

Only DUE-NOW requirements participate in the current phase exit gate. Future QA/release verification must have `OWNER_PHASE` + verification plan instead of becoming an artificial early blocker.

## Responsive scope

Project Config / Design Contract owns responsive scope.

- `desktop_only` → verify declared desktop viewports/pressure points; mobile/tablet = `N/A_JUSTIFIED`; do not claim fully responsive.
- `responsive_all` → desktop/tablet/mobile must be intentionally verified.

Generic mobile requirements inherited from older prompt versions do not override explicit `desktop_only` scope.

## Representative page selection

Representative pages come from the actual sitemap, page-role matrix, critical journeys and risk. Do not hard-code ecommerce-only routes such as PLP/PDP/Collection for corporate, education, public-sector or other sites that do not contain those roles.

For multi-page/journey/whole-site work, Prompt 2 must not authorize broad rollout until representative pages/surfaces have been implemented, rendered, opened and inspected with no material P0/P1 blocker.

## Design-intelligence insertion point

When active, use the design-intelligence layer **after project truth + audience/domain/reference understanding and before final visual direction / Design Contract lock**.

Rules:
- new/system-wide direction → one focused `--design-system` query;
- targeted concern → one explicit `--domain` query;
- implementation-specific guidance → detected `--stack` query;
- one dominant intent with 2–5 meaningful terms and one useful constraint;
- verify returned match; retry once if empty/off-topic, then record `no verified match` rather than fabricate evidence;
- synthesize material candidates `ADOPT / ADAPT / REJECT` against project truth, brand, accessibility, content density, page role and feasibility;
- database output is candidate intelligence, not UX/conversion/accessibility proof;
- upstream persisted MASTER/page files are subordinate to the canonical `skills_UIUX` Design Contract;
- never use upstream `--force` without explicit user authorization;
- do not preload the full vendor database or all vendor skills into context.

## OLD baseline rule

For existing-site redesign, prefer actual OLD rendered evidence. If live capture is unavailable, documented fallback evidence may support Prompt 1 when it is sufficient to determine structural delta. Only block when missing baseline prevents a material redesign decision or due-now visual claim.

For a genuinely new site, OLD→NEW comparison = `N/A_JUSTIFIED`.

## Mandatory lifecycle

```text
Prompt 0 / Project Config
→ OLD rendered/fallback baseline when applicable
→ research/reference intelligence
→ domain/audience/page-role understanding
→ focused design-intelligence retrieval + ADOPT/ADAPT/REJECT when active
→ asset/focal-point inventory for applicable media families
→ Redesign Delta Contract + Media/Focal Contract + adopted Design Contract
→ representative composition proofs
→ Prompt 1 PASS with phase-aware ledger
→ Prompt 2 structural implementation
→ stack-specific retrieval only for active implementation gaps when needed
→ rendered representative review in declared responsive scope
→ OLD vs NEW comparable proof when applicable
→ crop/layout integrity screenshot review
→ representative PASS
→ whole-site rollout
→ Prompt 3 NEW→CONTRACT + cross-page QA
→ OLD→NEW when applicable
→ human visual veto (KEEP / REVISE / REMOVE)
→ Final QA PASS
→ Prompt 4 release/deploy only when authorized
→ production smoke on the real served experience when deployment occurs
```

## Non-negotiable failure rules

For a substantial redesign, **do not PASS** if the visible change is primarily cosmetic:

- background/color inversion;
- font changes;
- spacing/radius/shadow updates;
- image swaps inside the same layout;
- decorative animation/gradient/glass;
- universal hero/card shell with new content.

Also **do not PASS** a media-heavy implementation when screenshots of applicable component families show:

- accidental head/face/garment/subject crop;
- vertical slivers, stretched or squashed images;
- text/price/CTA detached from its owning card/media;
- hero title clipped outside intended composition;
- large unexplained blank regions;
- media assigned to the wrong grid/column;
- device-specific crop failure on devices that are in declared scope.

Automated success cannot override an obviously broken screenshot.

Deployment success cannot replace production smoke when release is in scope. A stale asset/version or live visual defect means Prompt 4 is not PASS even if CI/deploy is green.

The redesign must show useful structural change in hierarchy, composition, page-role behavior, decision-object placement and/or journey while preserving validated content, URLs, business facts and working behavior.
