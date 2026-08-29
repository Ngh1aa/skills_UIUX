# skills_UIUX V3 — Evidence-Driven UI/UX Agent Operating System

Bộ skill cho AI coding agent xây dựng và nâng cấp website theo quy trình chuyên nghiệp từ discovery → research/validation → UX/IA → brand/system → implementation → QA → release → production learning.

V3 giữ nguyên V2/V2.1 và bổ sung lớp **Research, Validation & Advanced UX**.

## V3 có gì mới
- 22 specialist skill mới cho research, IA validation, complex interaction, enterprise data UI, cognitive/inclusive UX, trust/ethics, DesignOps và human-AI interaction.
- 5 capability packs opt-in: `research-validation`, `advanced-interaction`, `inclusive-trust`, `designops-governance`, `human-ai`.
- `.uiux-profile.json` schema v2 hỗ trợ `packs` nhưng schema v1 vẫn chạy bình thường.
- Project-aware installer resolve `profile + packs + additional_skills - exclude_skills`.
- V3 validator kiểm pack references, project config và evals.
- Eval suite mở rộng sang behavior/evidence, không chỉ file structure.

Chi tiết: [V3-ARCHITECTURE.md](V3-ARCHITECTURE.md) và [SKILL-CATALOG.md](SKILL-CATALOG.md).

## Recommended project config
```json
{
  "schema_version": 2,
  "profile": "uiux-corporate",
  "packs": ["research-validation", "inclusive-trust"],
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

Skills are copied to:
```text
<project>/.claude/skills/<skill-name>/SKILL.md
```

A safe-sync manifest preserves unrelated custom project skills during normal re-install.

## Capability packs
| Pack | Khi nào bật |
|---|---|
| `research-validation` | redesign uncertainty, discovery, usability/IA validation, before/after benchmarking |
| `advanced-interaction` | search, complex forms, async states, workflows, tables, dashboards, account UX |
| `inclusive-trust` | broad audience, high-trust/high-consequence flows, cognitive accessibility, manual AT testing |
| `designops-governance` | mature design system, cross-project consistency, critique/governance |
| `human-ai` | end-user generative/predictive/agentic AI experiences |

Do not enable every pack by default. Use the smallest set justified by project risk.

## Validation
```bash
python scripts/validate-skills.py
python scripts/validate-v2.py
python scripts/skill-stats.py
```

GitHub Actions runs validation and installer smoke tests on push/PR.

## Agent evals
See `evals/README.md`, `evals/tasks/`, `evals/RUBRIC.md`.

Philosophy:
- grade outcome and evidence rather than rigid tool choreography;
- deterministic checks where possible;
- rubric/model/human judgment for visual and research quality;
- never invent research evidence;
- promote stable capabilities to regression tests.

## Standards/research baseline
At execution time verify time-sensitive requirements. V3 is informed by W3C WCAG/COGA guidance, GOV.UK Service Manual research/accessibility/content guidance, NN/g usability measurement methods, IBM Carbon enterprise-component guidance, FTC deceptive-pattern guidance and Google PAIR human-AI guidance.

## Backward compatibility
- Existing profiles remain valid.
- `install-profile.py` remains valid.
- Schema-version-1 `.uiux-profile.json` remains valid.
- Existing root skill names are not renamed.
