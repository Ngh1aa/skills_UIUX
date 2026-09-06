# Skill Catalog — V5

## Core pipeline

| Skill | Vai trò |
|---|---|
| `website-delivery-pipeline` | Orchestrator lifecycle + adaptive pack/specialist routing |
| `project-context` | Project config, constraints and source-of-truth |
| `product-discovery` | Problem, audience, JTBD, constraints, KPI, scope |
| `website-audit-and-redesign` | Audit live/legacy site before redesign |
| `brand-guidelines` | Brand foundation, color, type, voice |
| `ux-research-and-journey` | Journey, task analysis and flows |
| `information-architecture` | Inventory, taxonomy, labels, hierarchy, navigation/findability, page roles and URL migration |
| `ux-laws-and-heuristics` | Heuristic review |
| `design-reference-research-and-benchmark` | Search, score and synthesize real/curated design references by domain, audience, business goal and implementation fit |
| `reference-extraction-and-design-audit` | Extract source-attributed visual-system evidence from selected references or the current codebase without making it canonical |
| `design-intelligence-retrieval` | Retrieve a small verified subset from the pinned UI UX Pro Max design-intelligence corpus, then synthesize ADOPT/ADAPT/REJECT against project truth |
| `real-world-artifact-and-domain-metaphor-design` | Translate real domain objects, documents, spaces and rituals into mental-model-aligned digital structure, components and visual signatures without literal skeuomorphic imitation |
| `visual-design-direction` | Layout, hierarchy and visual grammar |
| `visual-taste-calibration` | Anti-template / subject-matter-fit calibration after a visual direction exists; does not replace visual-design-direction |
| `ui-improvement` | Existing UI remediation orchestrator: diagnose → preserve → route specialists → implement → verify |
| `conversion-and-content` | Value proposition, CTA, content model |
| `content-design-and-question-design` | Interface content structure and question design for forms/transactional journeys |
| `ux-writing-and-microcopy` | State-level UI copy, labels, CTA, errors, empty/loading/success/recovery, terminology and localization-safe microcopy |
| `design-system-and-components` | Tokens, components, variants, states |
| `interaction-patterns-and-form-ux` | Common forms/search/filter/dialog patterns |
| `motion-and-microinteractions` | Purposeful motion |
| `asset-media-and-art-direction` | Image/video/icon direction |
| `system-reality-and-production-readiness` | Distinguish real/mock/static/simulated/partial behavior, data contracts and production gaps |
| `responsive-and-device-strategy` | Responsive/device behavior |
| `accessibility` | WCAG, semantic, keyboard/focus baseline |
| `localization-and-i18n` | Multilingual UX architecture |
| `frontend-architecture-and-refactoring` | Structure, reuse, safe refactor |
| `frontend-implementation` | Semantic implementation |
| `component-driven-development` | Isolated component states/stories/tests |
| `reference-analysis-and-design-to-code` | Reference/Figma/screenshot to system/code |
| `web-ui-code-review` | Code-level web UI review with conditional React/Next performance specialization and local-owner routing |
| `ai-agent-coding-guardrails` | Safe AI coding/change discipline, proportional planning and verification |
| `seo-strategy` | Technical/on-page SEO |
| `web-quality-and-performance` | CWV, lab/field evidence and project performance budgets |
| `security-and-privacy` | Risk-based security/privacy baseline and verification |
| `analytics-and-experimentation` | Tracking, funnels, experiments |
| `testing-strategy` | Risk-driven functional/state/browser/visual/accessibility/performance verification |
| `ui-craft-and-visual-qa` | Visual craft and responsive QA |
| `code-review-and-release` | Two-stage review, release/rollback and post-deploy gate |
| `production-monitoring-and-maintenance` | Post-release technical health |
| `content-governance-and-cms` | Content schema/ownership/CMS |
| `skill-authoring-and-governance` | Maintain this library |

## Reference intelligence

`design-reference-research-and-benchmark` sits between UX/content decisions and `visual-design-direction` for substantial new design/redesign work. It uses a mixed source model: real industry sites for product/UX truth, curated/award sources for visual craft, case-study/shot platforms for system/component ideas and mood platforms for art direction. It must not treat awards or gallery popularity as evidence of usability/conversion success.

When a selected reference or the current project needs deeper system-level evidence, route `reference-extraction-and-design-audit`. It extracts color/type/spacing/radius/elevation/layout/component/responsive/theme evidence with source + certainty. External extraction feeds the benchmark/visual direction; current-project extraction feeds design-system/code owners. Extraction never licenses cloning and never makes frequent observed values canonical by itself.

## External design intelligence

`design-intelligence-retrieval` exposes the complete pinned UI UX Pro Max corpus without turning it into global prompt context. Vendor source is stored at `vendor/ui-ux-pro-max/`: all seven upstream skill packages plus the full `src/ui-ux-pro-max` engine/data snapshot and MIT license.

Routing rule:
- new page/project/system visual direction → `--design-system`;
- focused concern → one explicit `--domain`;
- implementation-specific concern → `--stack` only after detecting the actual stack from project source;
- empty/off-topic match → retry once, then record `no verified match` rather than fabricate evidence.

Retrieved candidates are synthesized as `ADOPT / ADAPT / REJECT`. The canonical Design Contract stays authoritative; upstream-generated MASTER/page files are subordinate candidate artifacts. Do not preload full catalogs and do not use upstream `--force` without explicit user authorization.

## External specialist adapters

Additional external knowledge is integrated through pinned provenance and local progressive-disclosure adapters. Source locks live in `vendor/external-uiux/SOURCE-LOCKS.md`; external repos are not bulk-loaded or made equal to project truth.

### Visual taste

`visual-taste-calibration` is informed by Anthropic Frontend Design but has a deliberately narrower boundary. Route it **after** `visual-design-direction` when the direction is coherent yet generic/interchangeable, over-decorated or visibly falling back to template/AI defaults. It returns `KEEP / REVISE / REMOVE` calibration and hands material changes back to the canonical visual direction/Design Contract.

### Web UI/code QA

`web-ui-code-review` is informed by Vercel Web Interface Guidelines + React Best Practices. Route it for source-level UI review/pre-merge review or when rendered findings need code root-cause analysis. General web-interface checks apply first; React/Next performance rules activate only after detecting the actual stack/version. It does not replace accessibility conformance, project performance measurement or rendered visual QA.

### UX writing

`ux-writing-and-microcopy` owns string/state-level product copy: labels, consequence-revealing actions, hints, validation, errors, empty/loading/success, notifications and recovery. `content-design-and-question-design` retains broader question/content-flow ownership; `conversion-and-content` retains marketing/value-proposition ownership.

## Real-world artifact intelligence

`real-world-artifact-and-domain-metaphor-design` complements digital reference research by studying physical products, printed/operational documents, spatial systems, tools and offline rituals in the domain. It maps these to five transfer layers — form, structural, information, behavioral and ritual — and uses an L0–L4 fidelity ladder. Default to the lowest useful fidelity; do not turn every domain cue into literal skeuomorphism. Route it before `brand-distinctiveness-and-visual-signature` / `visual-design-direction` when domain-native artifacts can improve recognition, structure or originality.

## Production reality & delivery

`system-reality-and-production-readiness` exists because rendered UI can imply behavior that is not actually integrated. Use it for forms, search, auth, checkout, CMS/API data, analytics and prototype-to-production work. The `production-delivery` pack groups this reality check with coding guardrails, security/privacy, performance budgets, verification, release/rollback and production monitoring.

## V5 measurement-reliability specialists
- `evidence-provenance-and-research-ops`
- `journey-outcome-and-service-health`
- `brand-recognition-validation`
- `accessibility-conformance-evaluation`
- `visual-regression-and-design-drift`
- `adaptive-skill-routing-and-context-budget`
- `agent-evaluation-and-reliability`
- `continuous-learning-and-improvement`

## V4 experience-strategy specialists
- `audience-intent-and-top-tasks`
- `entry-context-and-visit-intent`
- `journey-driven-content-and-layout`
- `brand-distinctiveness-and-visual-signature`
- `service-experience-to-digital-journey`
- `experience-principles-and-signature-moments`
- `omnichannel-experience-continuity`
- `brand-recognition-and-consistency-qa`

## V3 specialist skills

### Research & validation
- `user-research-planning-and-recruitment`
- `moderated-usability-testing`
- `research-synthesis-and-insight-management`
- `ux-benchmarking-and-metrics`
- `card-sorting-and-tree-testing`
- `service-blueprinting`
- `prototype-strategy-and-concept-testing`

### Advanced interaction & enterprise
- `site-search-and-findability`
- `complex-forms-and-wizards`
- `state-feedback-and-error-recovery`
- `complex-workflow-and-progress-ux`
- `data-tables-and-enterprise-ux`
- `data-visualization-and-dashboard-ux`
- `authentication-account-and-recovery-ux`
- `personalization-and-preference-ux`

### Inclusive, content & trust
- `content-design-and-question-design`
- `ux-writing-and-microcopy`
- `inclusive-design-and-cognitive-accessibility`
- `assistive-technology-testing`
- `trust-credibility-and-transparency`
- `ethical-ux-and-deceptive-patterns`

### DesignOps & AI
- `design-critique-and-rationale`
- `design-system-governance-and-adoption`
- `human-ai-interaction-design`

## Capability packs
- `measurement-reliability` (V5)
- `production-delivery` (V5 production hardening)
- `experience-strategy` (V4)
- `research-validation`
- `advanced-interaction`
- `inclusive-trust`
- `designops-governance`
- `human-ai`

## Domain playbooks
`corporate-website`, `education-website`, `ecommerce-website`, `real-estate-and-building-website`, `hospitality-website`, `portfolio-website`, `news-and-media-website`, `saas-website`, `landing-page`, `government-and-public-sector-website`, `nonprofit-website`, `startup-and-incubator-website`.

## Selection rule

Keep base profiles small. Add packs only when scope/risk justifies them.

- UI remediation → `ui-improvement` + only relevant specialists.
- Substantial new/redesign → `design-reference-research-and-benchmark`; use `reference-extraction-and-design-audit` only for selected references/current-system evidence that needs deeper extraction.
- External design database → `design-intelligence-retrieval` only for an active knowledge gap after project/domain/audience/page-role context is known.
- Generic/interchangeable visual direction → `visual-taste-calibration` after the visual direction exists, not as a replacement for research/Design Contract.
- UI state/string comprehension/recovery → `ux-writing-and-microcopy`.
- Code-level UI/pre-merge review → `web-ui-code-review`; React/Next specialization only after stack/version detection.
- Domain-native artifacts/rituals → `real-world-artifact-and-domain-metaphor-design` when they improve mental-model fit or visual signature.
- Production candidate/release → `production-delivery` when integrations/security/performance/browser/rollback/production truth are material.

Do not activate external specialist adapters merely because they are installed. A local styling fix whose owner/tokens are already known should stay local.
