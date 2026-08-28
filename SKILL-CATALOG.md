# Skill Catalog

## Core pipeline

| Skill | Vai trò |
|---|---|
| `website-delivery-pipeline` | Orchestrator toàn bộ lifecycle |
| `product-discovery` | Problem, audience, JTBD, constraints, KPI, scope |
| `website-audit-and-redesign` | Audit website live/legacy trước redesign |
| `brand-guidelines` | Brand foundation, color, type, voice |
| `ux-research-and-journey` | Persona, journey, task analysis, flows |
| `information-architecture` | Sitemap, nav, URL, hierarchy |
| `ux-laws-and-heuristics` | UX laws + heuristic review |
| `visual-design-direction` | Layout, hierarchy, art direction, visual style |
| `conversion-and-content` | Value proposition, CTA, content model, microcopy |
| `design-system-and-components` | Tokens, components, variants, states |
| `interaction-patterns-and-form-ux` | Forms, search, filters, menus, dialogs, onboarding |
| `motion-and-microinteractions` | Purposeful motion + reduced motion |
| `asset-media-and-art-direction` | Image/video/icon selection and delivery |
| `responsive-and-device-strategy` | Mobile-first and device behavior |
| `accessibility` | WCAG/keyboard/focus/ARIA/forms |
| `localization-and-i18n` | Multilingual architecture and content UX |
| `frontend-architecture-and-refactoring` | Structure, boundaries, reuse, safe refactor |
| `frontend-implementation` | Semantic implementation |
| `component-driven-development` | Isolated component states/stories/tests |
| `reference-analysis-and-design-to-code` | Convert reference/Figma/screenshot to original system/code |
| `ai-agent-coding-guardrails` | Safe AI coding behavior and change discipline |
| `seo-strategy` | Technical/on-page SEO |
| `web-quality-and-performance` | CWV, budgets, quality |
| `security-and-privacy` | Security/privacy baseline |
| `analytics-and-experimentation` | Tracking, funnels, experiments |
| `testing-strategy` | Unit/integration/E2E/cross-browser tests |
| `ui-craft-and-visual-qa` | Visual polish, consistency, responsive visual QA |
| `code-review-and-release` | Review, release and deployment gate |
| `production-monitoring-and-maintenance` | Post-release health and maintenance |
| `content-governance-and-cms` | Content schema, ownership, migration, CMS readiness |
| `skill-authoring-and-governance` | Maintain and improve this skill library |

## Domain playbooks

Domain skills are overlays. Chúng không thay thế core pipeline; chúng thêm các user goals, page patterns, conversion paths và pitfalls đặc thù ngành.

- `corporate-website`
- `education-website`
- `ecommerce-website`
- `real-estate-and-building-website`
- `hospitality-website`
- `portfolio-website`
- `news-and-media-website`
- `saas-website`
- `landing-page`
- `government-and-public-sector-website`
- `nonprofit-website`
- `startup-and-incubator-website`

## Skill selection rules

- New website: chạy core pipeline từ discovery.
- Existing website redesign: thêm `website-audit-and-redesign` trước khi thay IA/UI.
- Có Figma/screenshot/reference: thêm `reference-analysis-and-design-to-code`.
- UI phức tạp hoặc nhiều state: thêm `component-driven-development` + `interaction-patterns-and-form-ux`.
- Site nhiều ảnh/video: thêm `asset-media-and-art-direction`.
- Site song ngữ/đa ngôn ngữ: thêm `localization-and-i18n` trước implementation.
- Trước release: luôn dùng `ui-craft-and-visual-qa`, `testing-strategy`, `accessibility`, `web-quality-and-performance`, `seo-strategy`, `security-and-privacy`, `code-review-and-release`.
- Sau release: dùng `production-monitoring-and-maintenance`.
