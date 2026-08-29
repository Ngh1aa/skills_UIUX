# skills_UIUX V2.1 — Professional Website Agent Operating System

Bộ skill dành cho AI coding agent xây dựng/nâng cấp website theo quy trình chuyên nghiệp từ discovery → UX → IA → brand/visual → design system → implementation → QA → release → monitoring.

## V2.1 có gì mới

V2 vẫn giữ progressive disclosure, evals và quality gates. V2.1 bổ sung **multi-project routing** để mỗi repository tự khai báo đúng capability cần dùng.

- **Project config:** mỗi repo có thể đặt `.uiux-profile.json` ở root.
- **Hybrid UIUX profiles:** corporate, education, ecommerce, real-estate, SaaS, startup, news, nonprofit, hospitality, government, landing và portfolio.
- **Project-aware installer:** `install-project.py` đọc config và cài đúng subset skill vào `.claude/skills/`.
- **Project context:** agent đọc project constraints + source-of-truth trước khi generic skill ra quyết định.
- **Safe sync manifest:** đổi profile chỉ remove skill do skills_UIUX từng quản lý; custom project skills được giữ nguyên.
- **CI V2.1:** validate profile inheritance, project configs, evals, resources và installer smoke tests.

Chi tiết kiến trúc: [V2-ARCHITECTURE.md](V2-ARCHITECTURE.md)

## Recommended workflow cho nhiều project

### 1. Tạo `.uiux-profile.json` ở project root

Ví dụ QTSC:

```json
{
  "schema_version": 1,
  "profile": "uiux-corporate",
  "additional_skills": ["website-audit-and-redesign"],
  "exclude_skills": [],
  "project": {
    "name": "QTSC",
    "mode": "interactive-prototype",
    "domain": "technology-park-corporate"
  },
  "source_of_truth": [
    "docs/digital-brand-guideline.md",
    "docs/ui-foundation.md",
    "docs/source-architecture.md"
  ],
  "constraints": [
    "Prioritize UI/UX fidelity and realistic interactions over production backend scope"
  ]
}
```

Xem thêm [project examples](examples/projects/README.md) và schema tại `schemas/uiux-profile.schema.json`.

### 2. Dry-run rồi install

```bash
python scripts/install-project.py ../QTSC --dry-run
python scripts/install-project.py ../QTSC
```

Installer đặt skills tại đúng path auto-discovery:

```text
<project>/.claude/skills/<skill-name>/SKILL.md
```

### 3. Update profile về sau

Sửa `.uiux-profile.json`, rồi chạy lại:

```bash
python scripts/install-project.py ../QTSC
```

Manifest `.claude/skills/.skills-uiux-manifest.json` giúp sync chỉ quản lý skill do library cài. Dùng `--clean` chỉ khi thật sự muốn xóa toàn bộ `.claude/skills/` trước khi cài lại.

## Hybrid profiles

- `uiux-corporate`
- `uiux-education`
- `uiux-ecommerce`
- `uiux-real-estate`
- `uiux-saas`
- `uiux-startup`
- `uiux-news`
- `uiux-nonprofit`
- `uiux-hospitality`
- `uiux-government`
- `uiux-landing`
- `uiux-portfolio`

Các profile này extend `prototype-uiux`; specialist như `website-audit-and-redesign` nên thêm bằng `additional_skills` khi project thực sự là redesign.

## Legacy/profile-level installer

Vẫn dùng được:

```bash
python scripts/install-profile.py education --target ../my-school-project --dry-run
python scripts/install-profile.py education --target ../my-school-project
```

Profiles V2 cũ vẫn được giữ để backward compatibility: `professional-core`, `redesign`, `education`, `corporate`, `ecommerce`, `prototype-uiux`.

## Progressive disclosure

Agent chỉ đọc skill/resource liên quan task. Một skill trưởng thành có thể gồm:

```text
<skill>/
├── SKILL.md
├── references/
├── checklists/
├── examples/
└── scripts/
```

`project-context` yêu cầu agent đọc `.uiux-profile.json` và source-of-truth liên quan trước quyết định lớn.

## Validation

```bash
python scripts/validate-skills.py
python scripts/validate-v2.py
python scripts/skill-stats.py
```

GitHub Actions chạy validators và installer smoke tests trên push/PR.

## Agent evals

Xem `evals/README.md`, `evals/tasks/` và `evals/RUBRIC.md`.

- deterministic grader khi outcome có thể kiểm bằng code;
- rubric/model/human cho visual/UX judgment;
- grade outcome hơn exact tool path;
- capability suite để hill-climb;
- regression suite để chống backslide.

## Design principles

- User/business goal trước decoration.
- Project source-of-truth trước generic visual trend.
- Brand consistency trước trend.
- Reusable system trước one-off page styling.
- Preserve content/SEO/behavior tốt khi redesign.
- Accessibility/responsive/SEO/performance/security là quality gates, không patch cuối.
- Không áp cùng một SaaS/card-grid grammar cho mọi ngành.
- Không tuyên bố hoàn tất nếu chưa verify.

## Standards baseline

Library định hướng theo current official Agent Skills guidance, WCAG 2.2, Design Tokens Community Group format khi interchange cần thiết, Core Web Vitals, Google Search Essentials, OWASP và framework production guidance. Version/threshold time-sensitive phải được verify lại khi execution.
