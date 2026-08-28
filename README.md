# skills_UIUX V2 — Professional Website Agent Operating System

Bộ skill dành cho AI coding agent xây dựng/nâng cấp website theo quy trình chuyên nghiệp từ discovery → UX → IA → brand/visual → design system → implementation → QA → release → monitoring.

## V2 có gì mới

- **Progressive disclosure:** core skills lớn được tách `SKILL.md + references + checklists + examples` để giảm context waste.
- **Profiles:** cài đúng subset skill cho education/corporate/ecommerce/redesign/prototype thay vì load cả library.
- **Installer:** copy profile vào `.claude/skills/` của project bằng một command.
- **Agent evals:** capability + regression tasks, rubric và must-not behaviors.
- **CI validation:** kiểm frontmatter, profile dependencies, eval schema, local resource links.
- **Governance tooling:** scaffold skill mới và báo skill quá dài/cần refactor.

Chi tiết kiến trúc: [V2-ARCHITECTURE.md](V2-ARCHITECTURE.md)

## Quick start

### 1. Chọn profile

```bash
python scripts/install-profile.py education --target ../my-school-project --dry-run
python scripts/install-profile.py education --target ../my-school-project
```

Profiles:
- `professional-core`
- `redesign`
- `education`
- `corporate`
- `ecommerce`
- `prototype-uiux`

Installer đặt skills tại:

```text
<project>/.claude/skills/<skill-name>/SKILL.md
```

### 2. Bắt đầu bằng orchestrator

`website-delivery-pipeline/SKILL.md` route phase, domain overlay, conditional skill và quality gates.

### 3. Không load toàn library

Agent chỉ đọc skill/resource liên quan task. Resource chi tiết nằm dưới:

```text
<skill>/references/
<skill>/checklists/
<skill>/examples/
<skill>/scripts/
```

## Validation

```bash
python scripts/validate-skills.py
python scripts/validate-v2.py
python scripts/skill-stats.py
```

GitHub Actions chạy validators trên push/PR.

## Agent evals

Xem `evals/README.md`, `evals/tasks/` và `evals/RUBRIC.md`.

Eval philosophy:
- deterministic grader khi outcome có thể kiểm bằng code;
- rubric/model/human cho visual/UX judgment;
- grade outcome hơn exact tool path;
- capability suite để hill-climb;
- regression suite để chống backslide.

## Skill authoring

Tạo scaffold:

```bash
python scripts/scaffold-skill.py my-new-skill
```

Sau đó đọc `skill-authoring-and-governance/SKILL.md` trước khi merge.

## Design principles

- User/business goal trước decoration.
- Brand consistency trước trend.
- Reusable system trước one-off page styling.
- Preserve content/SEO/behavior tốt khi redesign.
- Accessibility/responsive/SEO/performance/security là quality gates, không patch cuối.
- Không áp cùng một SaaS/card-grid grammar cho mọi ngành.
- Không tuyên bố hoàn tất nếu chưa verify.

## Standards baseline

Library định hướng theo current official guidance cho Agent Skills, WCAG 2.2, Design Tokens Community Group format khi interchange cần thiết, Core Web Vitals, Google Search Essentials, OWASP và framework production guidance. Version/threshold time-sensitive phải được verify lại khi execution.
