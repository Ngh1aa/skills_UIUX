---
name: website-delivery-pipeline
description: |
  Orchestrates the full lifecycle of building or redesigning a professional website. Use at project
  start, for multi-phase work, or when deciding which UI/UX skills, domain playbooks, artifacts and
  quality gates are needed before design, implementation, release and production maintenance.
---

# Website Delivery Pipeline — V2 Orchestrator

## Core principle

`business/user goal → evidence → UX/IA → brand/visual system → content/interaction → implementation → verification → production learning`

Không load cả library. Route đúng subset skill theo project/task.

## Step 0 — Choose execution profile

Khi bắt đầu project, chọn profile gần nhất rồi thêm/bớt skill theo scope:
- `professional-core`
- `redesign`
- `education`
- `corporate`
- `ecommerce`
- `prototype-uiux`

Profiles nằm ở `profiles/*.json`. Có thể cài bằng:

```bash
python scripts/install-profile.py education --target /path/to/project
```

Nếu task nhỏ trong project đã có skills, không cần reinstall profile.

## Pipeline

| Phase | Required / conditional skills | Gate |
|---|---|---|
| 0 Intake | `product-discovery`, coding guardrails | problem, audience, JTBD, scope, KPI |
| 0A Existing site | `website-audit-and-redesign` | keep/improve/merge/remove + migration risk |
| 1 Domain | one primary domain playbook | domain journeys/proof/conversion patterns |
| 2 UX/IA | journey + UX laws + IA | primary flow, sitemap/nav/page roles |
| 3 Brand/visual | brand + visual + media direction | implementable visual grammar |
| 4 System/interaction | design system + form/pattern UX + optional motion | tokens, component/state contracts |
| 5 Content | conversion/content + optional CMS/i18n | hierarchy, CTA, proof, schema/locale plan |
| 6 Architecture/code | frontend architecture + implementation; optional design-to-code/component-driven | maintainable working UI |
| 7 Inclusive/responsive | responsive + accessibility | critical journeys usable across target contexts |
| 8 Quality | visual QA + performance + SEO + security | findings resolved/documented |
| 9 Test/release | testing + analytics + release | evidence, smoke test, known issues |
| 10 Production | monitoring/maintenance | health loop + regression handling |

## Conditional routing

- Existing site/redesign → always audit first.
- Screenshot/Figma/reference → `reference-analysis-and-design-to-code`.
- Complex UI states → `component-driven-development`.
- Multilingual → `localization-and-i18n` before route/content hardcoding.
- CMS/content-heavy → `content-governance-and-cms` before schema lock-in.
- High motion → `motion-and-microinteractions` + accessibility reduced-motion review.

## Artifacts

Tạo artifacts vì chúng giúp decision/handoff, không vì checklist theater. Common:

```text
docs/product-brief.md
docs/decision-log.md
docs/website-audit.md
docs/ux-journey.md
docs/information-architecture.md
docs/brand-guidelines.md
docs/visual-direction.md
docs/design-system.md
docs/content-model.md
docs/test-plan.md
docs/release-checklist.md
```

## Quality gates

### Before visual/system work
- User/business goal known.
- Primary journeys/page roles known.
- Domain/brand constraints known.

### Before implementation
- Content hierarchy and visual grammar clear enough.
- P0 component/state inventory exists.
- Responsive/a11y constraints understood.

### Before release
- Build/type/lint/test requirements checked.
- Primary journeys manually verified.
- Representative viewport visual QA done.
- Critical a11y/SEO/performance/security issues resolved or documented.
- Analytics verified if in scope.
- Known limitations explicit.

## V2 evaluation loop

For skill/library changes:
1. run `python scripts/validate-skills.py`;
2. run `python scripts/validate-v2.py`;
3. select representative `evals/tasks/*.json`;
4. grade outcome with `evals/RUBRIC.md` + deterministic checks;
5. promote stable capability tests to regression suite.

## Progressive resources

- [Profile routing reference](references/profile-routing.md)
- [Project quality gate](checklists/project-gate.md)
- [Routing example](examples/project-routing.md)

## Completion rule

Không nói `done/perfect/fully responsive/compliant` nếu chưa có evidence tương ứng. Report verified vs unverified rõ ràng.
