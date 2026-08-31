# skills_UIUX V5 — Evidence, Reference Intelligence & Production Reliability Agent OS

Bộ skill cho AI coding agent xây dựng/nâng cấp website theo quy trình chuyên nghiệp từ discovery → research → audience/experience strategy → UX/IA → **reference intelligence** → brand/system → **system reality** → implementation → verification → release → service measurement → continuous learning.

V5 giữ toàn bộ lớp Evidence/Measurement/Reliability và reference intelligence, đồng thời bổ sung production hardening để tránh tình trạng UI nhìn hoàn chỉnh nhưng behavior/data/integration chưa thật sự production-ready.

## V5 production-grade enhancement

- `MASTER-PROMPT-V5.0.md`: master orchestrator dùng progressive disclosure thay vì nhồi toàn bộ library vào một prompt monolith.
- `system-reality-and-production-readiness`: label `REAL / MOCK / STATIC / SIMULATED / PARTIAL / UNKNOWN`, định nghĩa data/API/CMS contracts và chặn false success state.
- New `production-delivery` capability pack: system reality + coding guardrails + security/privacy + performance budgets + testing + release/rollback + production monitoring.
- `website-delivery-pipeline` có các phase mới cho system reality, implementation plan, verification matrix, two-stage review và safe release.
- `ai-agent-coding-guardrails` bổ sung proportional planning, preserve user changes, isolated branch/worktree khi phù hợp và spec-vs-quality review.
- `security-and-privacy` chuyển sang risk/trust-boundary model và current OWASP guidance thay vì copy universal header/regex examples.
- `web-quality-and-performance` dùng project/key-route performance budgets, tách lab/field evidence và bỏ universal Lighthouse vanity threshold.
- `testing-strategy` dùng critical journey + risk + browser/viewport pressure matrix + truthful system state.
- `code-review-and-release` dùng two-stage review, project-specific gates, safe rollback/revert và post-deploy smoke; destructive force-reset không còn là default rollback.

## Reference intelligence

`design-reference-research-and-benchmark` được route trước `visual-design-direction` cho substantial website/page design hoặc redesign khi visual direction chưa đủ mạnh.

Phân vai nguồn:

- **real industry/product sites** → IA, journey, trust, conversion, responsive behavior;
- **Awwwards, MUUUUU, SiteInspire, Godly, CSS Design Awards...** → visual craft, composition, typography, storytelling, motion;
- **Behance / Dribbble** → brand system, component và concept ideas với production caveat;
- **Pinterest / editorial mood sources** → photography, typography mood, texture và art direction.

Workflow:

`project truth → domain/audience/business goal → mixed candidate pool → score/shortlist → extract principles → visual direction → design system/code`

Hard rule: award/gallery popularity không phải bằng chứng UX, accessibility hoặc conversion performance; agent phải extract principle + adaptation, không clone surface.

## Architecture

- [MASTER-PROMPT-V5.0.md](MASTER-PROMPT-V5.0.md)
- [V5-ARCHITECTURE.md](V5-ARCHITECTURE.md)
- [V4-ARCHITECTURE.md](V4-ARCHITECTURE.md)
- [V3-ARCHITECTURE.md](V3-ARCHITECTURE.md)
- [SKILL-CATALOG.md](SKILL-CATALOG.md)

## Recommended project config

```json
{
  "schema_version": 2,
  "profile": "uiux-corporate",
  "packs": [
    "research-validation",
    "experience-strategy",
    "inclusive-trust",
    "measurement-reliability",
    "production-delivery"
  ],
  "additional_skills": ["website-audit-and-redesign"],
  "exclude_skills": [],
  "project": {
    "name": "My Project",
    "mode": "production-candidate",
    "domain": "corporate"
  },
  "source_of_truth": ["docs/brand.md", "docs/sitemap.md"],
  "constraints": ["Reuse existing tokens and components"]
}
```

Use `production-delivery` only when project mode/risk actually needs production hardening; interactive prototypes should still expose mock/simulated reality but do not need every production release gate.

## Install

```bash
python scripts/install-project.py ../MyProject --dry-run
python scripts/install-project.py ../MyProject
```

Skills are copied to `<project>/.claude/skills/<skill-name>/SKILL.md`. Safe-sync manifest preserves unrelated custom skills.

## Keep consumer projects current

```bash
python scripts/bootstrap-project.py ../MyProject --profile uiux-corporate
```

The generated workflow can receive `repository_dispatch` event `skills-uiux-release` with an immutable source ref. For release-critical projects, prefer tag/commit SHA over floating `main`; sync should remain reviewable/reversible.

## Capability packs

| Pack | Khi nào bật |
|---|---|
| `research-validation` | uncertainty, discovery, usability/IA validation, benchmarking |
| `experience-strategy` | audience intent, journey/content redesign, experiential services, brand memory |
| `measurement-reliability` | outcome proof, formal conformance, visual/system regression, repeated AI workflow reliability |
| `production-delivery` | production-candidate/release work: real integrations, security/privacy, performance/browser verification, rollback/monitoring |
| `advanced-interaction` | search, complex forms, workflows, tables, dashboards, account UX |
| `inclusive-trust` | broad audience, high trust/consequence, cognitive accessibility, AT testing |
| `designops-governance` | mature design systems and cross-project consistency |
| `human-ai` | end-user generative/predictive/agentic AI |

Use the smallest set justified by task scope and risk.

## V5 working model

`project truth → evidence → audience/intent → journey → success definition → UX/IA → reference intelligence → brand/system → system reality/data contract → plan → implementation → verification → release → real outcomes → learning`

Hard rules:

- no evidence → no `validated` research claim;
- no appropriate evaluation → no accessibility conformance claim;
- no outcome data → no claim that UX improved;
- no repeated trials → no reliability claim;
- no intentional review → no automatic visual-baseline acceptance;
- award/curated reference → inspiration evidence, not UX proof;
- rendered success state → not system success proof;
- lab score → not field performance proof;
- mock/simulated integration → not production-ready;
- deploy success → not completion until relevant post-deploy smoke;
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

## Research baseline

At execution time verify time-sensitive requirements. V5 is informed by W3C/WAI accessibility evaluation methodology, GOV.UK service/user-needs/performance guidance, current OWASP verification guidance, web performance budget practice and agent workflow patterns from modern public coding-agent skill ecosystems. External skill repos are used as benchmarking input only; this library keeps its own project-truth, evidence, UX, brand and adaptive-routing model.

## Backward compatibility

- V2/V2.1/V3/V4 profiles remain valid.
- Existing root skill names remain valid.
- `install-profile.py` remains valid.
- Schema-version-1 and schema-version-2 project configs remain supported.
