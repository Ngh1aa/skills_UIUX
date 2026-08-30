# skills_UIUX V5 — Evidence, Measurement & Reliability UI/UX Agent OS

Bộ skill cho AI coding agent xây dựng/nâng cấp website theo quy trình chuyên nghiệp từ discovery → research → audience/experience strategy → UX/IA → **reference intelligence** → brand/system → implementation → conformance/regression QA → release → service measurement → continuous learning.

V5 giữ toàn bộ V4 và bổ sung lớp **Evidence, Measurement & Reliability**. Bản cập nhật hiện tại bổ sung `design-reference-research-and-benchmark` để agent có thể research website/design đẹp trên web theo ngành và mục tiêu thay vì tự tạo visual direction trong khoảng trống.

## V5 có gì mới
- 8 specialist skills: evidence provenance/ResearchOps, service outcome health, brand-recognition validation, accessibility conformance evaluation, visual/design drift, adaptive routing/context budget, agent reliability eval và continuous learning.
- Capability pack opt-in mới: `measurement-reliability`.
- 8 V5 eval tasks bảo vệ evidence integrity, outcome measurement, WCAG claim discipline, design drift, minimal routing, multi-trial reliability, learning loop và brand-recognition validation.
- Provider-neutral `scripts/eval-harness.py` để validate/summarize JSONL multi-trial results, gồm estimated `pass@k` / `pass^k` với caveat rõ.
- CI chạy cả structural checks, V5 project installer smoke và eval-harness smoke.

## Reference intelligence enhancement

Skill `design-reference-research-and-benchmark` được route trước `visual-design-direction` cho substantial website/page design hoặc redesign khi visual direction chưa đủ mạnh.

Nó phân vai nguồn thay vì trộn tất cả thành “inspiration”:

- **real industry/product sites** → IA, journey, trust, conversion, responsive behavior;
- **Awwwards, MUUUUU, SiteInspire, Godly, CSS Design Awards...** → visual craft, composition, typography, storytelling, motion;
- **Behance / Dribbble** → brand system, component và concept ideas với production caveat;
- **Pinterest / editorial mood sources** → photography, typography mood, texture và art direction.

Workflow mặc định:

`project truth → domain/audience/business goal → mixed candidate pool → score/shortlist → extract principles → visual direction → design system/code`

Hard rule: award/gallery popularity không phải bằng chứng UX, accessibility hoặc conversion performance; agent phải extract principle và adaptation, không clone surface.

Kiến trúc: [V5-ARCHITECTURE.md](V5-ARCHITECTURE.md), [V4-ARCHITECTURE.md](V4-ARCHITECTURE.md), [V3-ARCHITECTURE.md](V3-ARCHITECTURE.md), [SKILL-CATALOG.md](SKILL-CATALOG.md).

## Recommended project config
```json
{
  "schema_version": 2,
  "profile": "uiux-corporate",
  "packs": ["research-validation", "experience-strategy", "inclusive-trust", "measurement-reliability"],
  "additional_skills": ["website-audit-and-redesign"],
  "exclude_skills": [],
  "project": {"name": "My Project", "mode": "interactive-prototype", "domain": "corporate"},
  "source_of_truth": ["docs/brand.md", "docs/sitemap.md"],
  "constraints": ["Reuse existing tokens and components"]
}
```

## Install
```bash
python scripts/install-project.py ../MyProject --dry-run
python scripts/install-project.py ../MyProject
```

Skills are copied to `<project>/.claude/skills/<skill-name>/SKILL.md`. Safe-sync manifest preserves unrelated custom skills.

## Keep consumer projects current

Use the bootstrap command once in each project. It creates a project profile if
needed, installs the selected skills and adds a weekly/manual sync workflow that
opens or updates a pull request instead of writing directly to the default
branch.

```bash
python scripts/bootstrap-project.py ../MyProject --profile uiux-corporate
```

The generated workflow can also receive a `repository_dispatch` event of type
`skills-uiux-release` with `{"source_ref":"v5.1.0"}`. This enables an
organization-level release bot or GitHub App to notify every consumer project.
Configure that bot outside this repository with least-privilege `contents` and
`pull_requests` access; no personal access token is stored in a project.

For a release-critical project, dispatch a tag or immutable commit SHA instead
of `main`. The synchronization PR records the resolved source commit, so every
update is reviewable and reversible.

## Capability packs
| Pack | Khi nào bật |
|---|---|
| `research-validation` | uncertainty, discovery, usability/IA validation, benchmarking |
| `experience-strategy` | audience intent, journey/content redesign, experiential services, brand memory, online/offline continuity |
| `measurement-reliability` | substantial release, production outcome proof, formal accessibility review, repeated AI workflows, regression/reliability needs |
| `advanced-interaction` | search, complex forms, states, workflows, tables, dashboards, account UX |
| `inclusive-trust` | broad audience, high trust/consequence, cognitive accessibility, AT testing |
| `designops-governance` | mature design systems and cross-project consistency |
| `human-ai` | end-user generative/predictive/agentic AI |

Use the smallest set justified by task scope and risk.

## V5 working model
`project truth → evidence → audience/intent → whole journey → success definition → minimal skill routing → UX/IA → reference intelligence → brand/visual/system → implementation → conformance/regression → multi-trial eval → real outcomes → continuous learning`

Hard rules:
- no evidence → no `validated` research claim;
- no appropriate evaluation → no accessibility conformance claim;
- no outcome data → no claim that UX improved;
- no repeated trials → no reliability claim;
- no intentional review → no automatic visual-baseline acceptance;
- award/curated reference → inspiration evidence, not automatic UX proof;
- production failures should feed research, tests or regression evals.

## V5 eval harness
```bash
python scripts/eval-harness.py list
python scripts/eval-harness.py validate-results --results results.jsonl
python scripts/eval-harness.py summarize --results results.jsonl --k 3
python scripts/eval-harness.py smoke
```

Provider adapters follow [evals/ADAPTER-CONTRACT.md](evals/ADAPTER-CONTRACT.md).

## Validation
```bash
python scripts/validate-skills.py
python scripts/validate-v2.py
python scripts/skill-stats.py
python scripts/eval-harness.py smoke
```

## Standards/research baseline
At execution time verify time-sensitive requirements. V5 is informed by W3C/WAI WCAG-EM methodology, GOV.UK service success/performance guidance, Anthropic agent-eval guidance, plus all V4/V3 research baselines.

## Backward compatibility
- V2/V2.1/V3/V4 profiles remain valid.
- Existing root skill names are unchanged.
- `install-profile.py` remains valid.
- Schema-version-1 and schema-version-2 project configs remain supported.
