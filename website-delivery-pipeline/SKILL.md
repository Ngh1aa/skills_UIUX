---
name: website-delivery-pipeline
description: |
  Meta-skill điều phối toàn bộ lifecycle xây dựng hoặc redesign website chuyên nghiệp.
  Dùng khi bắt đầu project, task nhiều phase hoặc cần quyết định skill nào phải chạy trước/sau;
  quản lý dependencies, artifacts, quality gates và domain-specific overlays.
---

# Website Delivery Pipeline — Orchestrator

## Core principle

Không nhảy từ brief thẳng vào code. Pipeline phải nối được:

`business/user goal → evidence → UX/IA → visual/system → content → implementation → verification → production learning`

Đọc thêm `ai-agent-coding-guardrails` xuyên suốt mọi coding task.

## Pipeline

| Phase | Required skill(s) | Key output / gate |
|---|---|---|
| 0. Intake | `product-discovery`, `ai-agent-coding-guardrails` | Problem, audience, JTBD, constraints, KPI, scope |
| 0A. Existing-site audit | `website-audit-and-redesign` | Keep/Improve/Merge/Remove + migration risks |
| 1. Domain framing | One relevant domain playbook | Domain journeys, proof, conversion patterns |
| 2. Brand | `brand-guidelines` | Brand roles, voice, visual constraints |
| 3. UX | `ux-research-and-journey`, `ux-laws-and-heuristics` | Journey, task flows, pain points, edge cases |
| 4. IA | `information-architecture` | Sitemap, nav, page inventory, URL strategy |
| 5. Visual direction | `visual-design-direction`, `asset-media-and-art-direction` | Layout/hierarchy/art direction/media rules |
| 6. System & interaction | `design-system-and-components`, `interaction-patterns-and-form-ux`, `motion-and-microinteractions` | Tokens, component/state contracts, interaction specs |
| 7. Content | `conversion-and-content`; optional `content-governance-and-cms`, `localization-and-i18n` | Content hierarchy, CTA, schema, locale plan |
| 8. Architecture & implementation | `frontend-architecture-and-refactoring`, `frontend-implementation`; optional `reference-analysis-and-design-to-code`, `component-driven-development` | Maintainable code matching system |
| 9. Responsive + accessibility | `responsive-and-device-strategy`, `accessibility` | Target viewport and WCAG-level behavior verified |
| 10. Quality | `ui-craft-and-visual-qa`, `web-quality-and-performance`, `seo-strategy`, `security-and-privacy` | Visual/UX/SEO/performance/security findings resolved or documented |
| 11. Testing | `testing-strategy` | Critical path + regression evidence |
| 12. Analytics & release | `analytics-and-experimentation`, `code-review-and-release` | Tracking, build/release/smoke-test gate |
| 13. Production | `production-monitoring-and-maintenance` | Health signals, issues, maintenance loop |

## Domain overlay selection

Chọn tối đa domain skill cần thiết thay vì load tất cả:

- Company: `corporate-website`
- School/education: `education-website`
- Commerce/catalogue: `ecommerce-website`
- Office/property: `real-estate-and-building-website`
- Hotel/resort: `hospitality-website`
- Studio/individual work: `portfolio-website`
- Publication: `news-and-media-website`
- Software product: `saas-website`
- Campaign: `landing-page`
- Government/public services: `government-and-public-sector-website`
- NGO/charity: `nonprofit-website`
- Accelerator/ecosystem: `startup-and-incubator-website`

Nếu project hybrid, chọn primary domain + tối đa một secondary lens có rationale.

## Conditional skills

### Existing website

Luôn audit trước redesign. Không đổi URL/content architecture lớn khi chưa xác định SEO/content migration impact.

### Figma/screenshot/reference website

Dùng `reference-analysis-and-design-to-code`; extract rules và map vào existing design system, không copy pixel/asset mù quáng.

### Complex component/UI states

Dùng `component-driven-development` để cover variants/states trong isolation trước compose page.

### Multilingual

Dùng `localization-and-i18n` trước khi hardcode routes/content/components.

### CMS/content-heavy

Dùng `content-governance-and-cms` trước khi schema bị khóa vào markup.

## Required documents

Tạo artifact khi complexity thực sự cần; không tạo docs vô ích chỉ để tick box.

```text
docs/
├── product-brief.md
├── assumption-log.md
├── decision-log.md
├── website-audit.md              # existing site only
├── ux-journey.md
├── information-architecture.md
├── brand-guidelines.md
├── visual-direction.md
├── design-system.md
├── interaction-spec.md           # complex interactions
├── content-model.md
├── localization-strategy.md      # multilingual only
├── reference-to-design.md        # reference/Figma flow only
├── test-plan.md
├── release-checklist.md
└── maintenance-plan.md           # long-lived production projects
```

## Quality gates

### Gate A — Before visual design

- Problem/audience/JTBD known.
- Primary journeys known.
- Sitemap/navigation have rationale.

### Gate B — Before implementation

- Brand/visual direction defined.
- Component/state inventory exists.
- Content hierarchy exists for primary templates.
- Responsive/accessibility constraints understood.

### Gate C — Before release

- Primary journeys manually verified.
- Build/type/lint/test requirements pass for project.
- Critical accessibility issues resolved.
- SEO/indexability migration issues resolved.
- Performance checked against project budget and Core Web Vitals goals.
- Security/privacy relevant checks complete.
- Representative mobile/tablet/desktop visual QA complete.
- Analytics events verified if in scope.
- Known issues documented.

## Decision log

Important decision format:

```markdown
## Decision: [short name]
- Context:
- Options:
- Decision:
- Rationale:
- Trade-offs:
- Evidence:
- Revisit when:
```

## Fast-track mode

Landing page/prototype có thể combine phases nhưng **không bỏ principles**:

1. Brief + domain + brand.
2. Journey + IA + content narrative.
3. Visual + lightweight tokens/components.
4. Implementation + responsive/a11y.
5. Visual/performance/SEO/test gate.
6. Release/tracking if applicable.

## Completion rule

Không tuyên bố “done/perfect/fully responsive” chỉ vì code đã được viết. Completion phải kèm evidence phù hợp scope: build/test result, inspected interactions, representative viewport QA và known limitations.

## Anti-patterns

- Code trước khi hiểu primary user task.
- Load toàn bộ skills gây context overload.
- Dùng cùng một SaaS/card-grid visual grammar cho mọi domain.
- Redesign xóa hết content/URLs tốt.
- A11y/responsive/SEO/performance làm sau cùng như patch.
- Thêm animation trước khi layout/content ổn.
- Tuyên bố hoàn tất mà không verify.
