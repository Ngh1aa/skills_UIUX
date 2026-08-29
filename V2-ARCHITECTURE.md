# skills_UIUX V2.1 Architecture

V2.1 biến repository thành **UI/UX Agent Operating System cho nhiều project**: progressive disclosure + profile routing + project context + deterministic validation + agent evals.

## 1. Skill package contract

```text
<skill>/
├── SKILL.md                 # Trigger + workflow + routing, ưu tiên ngắn
├── references/              # Kiến thức chi tiết chỉ đọc khi cần
├── checklists/              # Quality gates
├── examples/                # Concrete patterns
└── scripts/                 # Deterministic helpers nếu hữu ích
```

Không bắt buộc skill có đủ mọi folder. Resource chỉ nên tồn tại khi giúp giảm context, tăng accuracy hoặc verification.

## 2. Progressive disclosure

- Level 1: `name` + `description` luôn available để discovery.
- Level 2: `SKILL.md` được đọc khi request match.
- Level 3: references/checklists/examples/scripts chỉ dùng khi task cần.
- Main SKILL.md là runbook, không phải textbook.

## 3. Library profiles

`profiles/*.json` là capability presets. V2.1 có hai lớp:

### Base/production profiles

`professional-core`, `redesign`, `education`, `corporate`, `ecommerce`, `prototype-uiux`.

### Hybrid UIUX profiles

`uiux-corporate`, `uiux-education`, `uiux-ecommerce`, `uiux-real-estate`, `uiux-saas`, `uiux-startup`, `uiux-news`, `uiux-nonprofit`, `uiux-hospitality`, `uiux-government`, `uiux-landing`, `uiux-portfolio`.

Hybrid profiles extend `prototype-uiux` rồi thêm đúng domain lens. Redesign là một concern độc lập và được thêm qua `additional_skills` khi cần.

## 4. Project-level contract

Mỗi project có thể khai báo `.uiux-profile.json`:

```text
project/
├── .uiux-profile.json
├── .claude/
│   └── skills/
├── docs/
└── ...
```

Config chọn profile, specialist bổ sung, exclusions, project metadata, source-of-truth và constraints. Schema nằm tại `schemas/uiux-profile.schema.json`.

`project-context` là bridge giữa generic library và project-specific truth. Rule priority:

`current user instruction → .uiux-profile.json → source-of-truth docs → specialist/domain skill → generic defaults`

## 5. Project-aware install & safe sync

`scripts/install-project.py` resolve profile inheritance + additions/exclusions rồi copy đúng skill vào `.claude/skills/`.

Manifest `.claude/skills/.skills-uiux-manifest.json` ghi các folder do library quản lý. Lần sync sau chỉ remove managed skills không còn cần; custom skill khác trong project được giữ. `--clean` là destructive opt-in.

## 6. Why this matches Agent Skills architecture

Repository skills phải nằm đúng `.claude/skills/<skill-name>/SKILL.md`. Chỉ metadata luôn được announce; full instructions/resources được đọc on demand. Vì vậy project-level selection giảm capability clutter và vẫn giữ progressive disclosure bên trong từng skill.

## 7. Eval-driven development

### Structural/regression evals

CI kiểm:
- frontmatter/name/description;
- profile inheritance và missing skills;
- `.uiux-profile.json` examples;
- local resource links;
- eval schema;
- installer dry-runs.

### Agent capability evals

`evals/tasks/*.json` chấm expected outcomes, must-not behaviors và weighted rubric. Ưu tiên outcome hơn exact tool choreography.

## 8. Backward compatibility

- Existing skill names/folders giữ nguyên.
- V2 profile-level installer vẫn hoạt động.
- Project-aware config là opt-in.
- Hybrid profiles và `project-context` chỉ mở rộng capability, không làm gãy V1/V2 project.
