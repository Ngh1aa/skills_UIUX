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
| `visual-design-direction` | Layout, hierarchy and visual grammar |
| `ui-improvement` | Existing UI remediation orchestrator: diagnose → preserve → route specialists → implement → verify |
| `conversion-and-content` | Value proposition, CTA, content model |
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
Keep base profiles small. Add packs only when scope/risk justifies them. For UI remediation, route through `ui-improvement` and activate only relevant specialists. For substantial visual redesign/new-site work, activate `design-reference-research-and-benchmark` when reference intelligence materially improves direction. For production-candidate/release work, activate `production-delivery` when integrations, security, performance, browser verification, rollback or production truth are material. Do not activate deep production gates for a local styling fix or visual-only prototype unless the exact issue requires them.
