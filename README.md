# skills_UIUX V4 — Audience, Evidence & Experience-Driven UI/UX Agent OS

Bộ skill cho AI coding agent xây dựng/nâng cấp website theo quy trình chuyên nghiệp từ discovery → research/validation → audience/experience strategy → UX/IA → brand/system → implementation → QA → release → production learning.

V4 giữ toàn bộ V3 và bổ sung lớp **Audience, Brand Memory & Service Experience**.

## V4 có gì mới
- 8 specialist skills cho audience/top tasks, entry intent, journey-driven content/layout, digital brand distinctiveness, service-to-digital journey, experience principles/signature moments, omnichannel continuity và brand recognition QA.
- Capability pack opt-in mới: `experience-strategy`.
- 5 V4 evals chống generic layout, fake user evidence, logo-dependent branding, broken offline handoff và decorative immersion.
- QTSC example bật `experience-strategy` để CI kiểm pack routing thật.
- Không đổi schema: `.uiux-profile.json` schema v2 của V3 đã hỗ trợ generic `packs`.

Kiến trúc: [V4-ARCHITECTURE.md](V4-ARCHITECTURE.md), [V3-ARCHITECTURE.md](V3-ARCHITECTURE.md), [SKILL-CATALOG.md](SKILL-CATALOG.md).

## Recommended project config
```json
{
  "schema_version": 2,
  "profile": "uiux-corporate",
  "packs": ["research-validation", "experience-strategy", "inclusive-trust"],
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

## Capability packs
| Pack | Khi nào bật |
|---|---|
| `research-validation` | uncertainty, discovery, usability/IA validation, benchmarking |
| `experience-strategy` | audience intent, substantial content/layout redesign, experiential services, distinctive brand memory, online/offline journey |
| `advanced-interaction` | search, complex forms, states, workflows, tables, dashboards, account UX |
| `inclusive-trust` | broad audience, high trust/consequence, cognitive accessibility, AT testing |
| `designops-governance` | mature design systems and cross-project consistency |
| `human-ai` | end-user generative/predictive/agentic AI |

Use the smallest set justified by project risk.

## V4 working model
`project truth → audience/entry intent → top tasks → whole service journey → journey-driven content/IA → distinctive brand experience → implementation → joined-up handoff → recognition/UX verification`

Rules:
- never invent user evidence;
- distinguish owner goals from user goals;
- do not assume all visits start on the homepage;
- do not map content inventory directly to page blocks;
- logo + brand color alone is not a complete digital identity;
- do not confuse immersive service design with decorative 3D/motion;
- online completion must join coherently to offline/human steps when the real service continues.

## Validation
```bash
python scripts/validate-skills.py
python scripts/validate-v2.py
python scripts/skill-stats.py
```

GitHub Actions runs validation and installer smoke tests on push/PR.

## Standards/research baseline
At execution time verify time-sensitive requirements. V4 is informed by V3 sources plus GOV.UK user-needs and whole-service guidance, W3C/WAI findability/cognitive guidance, Nielsen Norman Group journey/IA research and Kantar distinctive-brand-asset research.

## Backward compatibility
- V2/V2.1/V3 profiles remain valid.
- Existing root skill names are unchanged.
- `install-profile.py` remains valid.
- Schema-version-1 and schema-version-2 project configs remain supported.
