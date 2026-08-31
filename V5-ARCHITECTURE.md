# skills_UIUX V5 Architecture — Evidence, Reference Intelligence, Measurement & Production Reliability

V5 adds four coordinated layers on top of the existing UX/UI/domain foundation:

1. **Evidence & measurement** — claims, outcomes, conformance and reliability must be evidence-backed.
2. **Reference intelligence** — major visual direction can learn from real/curated references without copying or treating awards as UX proof.
3. **Production reality** — rendered UI must not be confused with real integrations/data/behavior.
4. **Delivery reliability** — proportional planning, verification, safe release/rollback and production feedback.

It does not replace V4 audience/experience strategy, V3 research/advanced UX, or domain playbooks.

## Core idea

`project truth → evidence → audience/intent → journey/IA → reference intelligence → brand/system → system reality/data contract → plan → implementation → verification → release → real outcomes → continuous learning`

## Why V5 exists

A strong framework can still fail if:

- research/user claims cannot be traced to a source;
- a prettier redesign is called an UX improvement without outcome data;
- an award/gallery reference is treated as proof of usability/conversion;
- accessibility is claimed from automated scans or spot checks;
- visual/design-system drift accumulates;
- every task loads too much context;
- UI success states imply backend success that does not exist;
- mock/static data ships as if it were live;
- CI/build/Lighthouse green is mistaken for production verification;
- release rollback relies on destructive history rewriting;
- an agent passes once and is called reliable;
- production feedback never becomes research/tests/regression coverage.

## Progressive disclosure

V5 deliberately keeps the master orchestrator smaller than a monolithic mega-prompt:

`orchestrator → specialist SKILL.md → references/checklists/examples only when decision is active`

This reduces context dilution and keeps project truth visible.

## Capability packs

### `measurement-reliability`

1. `evidence-provenance-and-research-ops`
2. `journey-outcome-and-service-health`
3. `brand-recognition-validation`
4. `accessibility-conformance-evaluation`
5. `visual-regression-and-design-drift`
6. `adaptive-skill-routing-and-context-budget`
7. `agent-evaluation-and-reliability`
8. `continuous-learning-and-improvement`

Use when substantial outcome/conformance/regression/reliability claims need stronger evidence.

### `production-delivery`

1. `system-reality-and-production-readiness`
2. `ai-agent-coding-guardrails`
3. `security-and-privacy`
4. `web-quality-and-performance`
5. `testing-strategy`
6. `code-review-and-release`
7. `production-monitoring-and-maintenance`

Use for production-candidate/release work where real integrations, data truth, security, browser/performance verification, rollback or post-release health are material.

Do not load either whole pack for a tiny low-risk style fix.

## Reference-intelligence contract

`project/domain context → source mix → candidate pool → fit scoring → finalists by role → principle extraction → project adaptation → visual/system handoff`

Rules:

- real production/category sites are stronger evidence for IA/journey/trust/conversion patterns;
- curated/award sources are strong visual-craft input but not automatic UX proof;
- case-study/shot/mood sources have explicit secondary roles;
- label production vs concept/unknown when material;
- extract Design DNA/rules, not branded surface/assets.

## System-reality contract

Material capabilities can be labeled:

`REAL | MOCK | STATIC | SIMULATED | PARTIAL | UNKNOWN`

Rules:

- rendered success state is not proof of backend success;
- search/login/checkout/CMS/analytics UI is not proof of real integration;
- dynamic features need data/API/state contracts when production-relevant;
- production gaps need severity/dependency/owner;
- `REAL/working/integrated/production-ready` require evidence appropriate to the exact claim.

## Implementation contract

Substantial/high-risk work should use proportional planning:

`goal → owning files/components → dependencies → expected behavior → edge cases → verification`

Preserve unrelated user changes. Prefer isolated branch/worktree when tooling supports it and scope/risk justifies isolation.

Review in two stages:

1. **spec/intent compliance**;
2. **code/experience quality**.

A clean implementation that violates the requested behavior/brand/project truth still fails.

## Verification contract

Every material change should be traceable through:

`change → expected outcome → verification method → pass condition → result`

Important distinctions:

- build pass ≠ visual/functional proof;
- automated accessibility scan ≠ formal conformance;
- one Lighthouse/lab run ≠ field performance outcome;
- deploy job success ≠ post-deploy service health;
- screenshot existence ≠ visual inspection.

## Security/privacy contract

Use risk/trust-boundary reasoning rather than one universal header/regex checklist.

`data/assets/actors → trust boundaries → threats/misuse → controls → verification → residual risk`

Use current authoritative standards/guidance when exact requirements matter. Security/privacy/compliance claims require evidence matching scope and jurisdiction.

## Performance contract

Use key-route/user-condition **performance budgets** instead of universal vanity thresholds.

Budget dimensions can include Core Web Vitals, resource size/count, hero/media/fonts, third parties and runtime work.

Always distinguish lab evidence from field/real-user data.

## Release contract

Production release should know:

- exact change scope;
- verification results/unverified areas;
- P0/P1 blockers/accepted risks;
- env/config/migration/redirect dependencies;
- safe rollback/recovery mechanism;
- post-deploy smoke scope;
- monitoring/learning signals.

Default rollback should be platform previous-deployment rollback or safe revert when appropriate, not destructive force-reset of shared history.

## Evidence contract

Important claims should trace:

`claim → source/evidence → date/context → confidence/limitations → decision → verification/outcome`

Never upgrade an assumption into research evidence.

## Reliability contract

One successful agent run demonstrates capability, not reliability.

Use multiple independent trials when reliability matters, deterministic graders where possible, judgment graders/human calibration where required, and outcome grading over brittle choreography.

## Accessibility contract

Formal accessibility evaluation should use a WCAG-EM-style scoped process: define scope/target, explore product, select representative sample/complete processes, evaluate with appropriate manual/automated/AT methods, and report limitations. Partial review is not a conformance claim.

## Measurement contract

Define success from service purpose/user need before claiming improvement:

`user need → service purpose → outcome → metric → data source → segment/channel → decision threshold → review cadence`

Combine performance data with user research; measure the relevant end-to-end journey when the service continues beyond the website.

## Provider-neutral eval harness

`scripts/eval-harness.py` supports task discovery, result validation and multi-trial summaries. Provider adapters emit the documented JSONL contract so the library remains model/vendor neutral.

## Backward compatibility

- V2/V2.1/V3/V4 profiles remain valid.
- Schema-version-1 and schema-version-2 configs remain valid.
- Existing skill names remain valid.
- V5 uses the existing profile/pack mechanism.

## Research / benchmarking baseline

At execution time verify time-sensitive guidance. V5 is informed by:

- W3C/WAI WCAG-EM evaluation methodology;
- GOV.UK user-needs/service-success/performance-measurement practice;
- OWASP ASVS and relevant Cheat Sheet guidance for web application verification;
- web.dev performance budget and lab/field performance practice;
- public coding-agent skill ecosystems for progressive disclosure, explicit skill routing, verification-before-completion, isolated execution and review patterns;
- project-specific research and evidence, which always takes precedence over generic examples when valid.
