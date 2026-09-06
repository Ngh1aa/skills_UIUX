# skills_UIUX V5 — Evidence, Reference Intelligence & Production Reliability Agent OS

Bộ skill cho AI coding agent xây dựng/nâng cấp website theo pipeline chuyên nghiệp từ project truth → research → audience/journey/IA → reference intelligence → design intelligence → Design Contract → implementation → rendered QA → release/production verification.

V5 là **library/agent-OS version**. Các prompt có version riêng; không suy ra library version từ prompt version.

## Canonical entrypoints

Cho substantial website redesign, bắt đầu từ:

- [LATEST-3-PROMPT-REDESIGN-PIPELINE.md](LATEST-3-PROMPT-REDESIGN-PIPELINE.md)
- [MASTER-PRE-DESIGN-RESEARCH-PROMPT-V4.2.md](MASTER-PRE-DESIGN-RESEARCH-PROMPT-V4.2.md)
- [MASTER-PROMPT-V7.2.md](MASTER-PROMPT-V7.2.md)
- [FINAL-UIUX-VISUAL-CONTENT-QA-REMEDIATION-V3.2.md](FINAL-UIUX-VISUAL-CONTENT-QA-REMEDIATION-V3.2.md)

Governance/runtime entrypoints:

- [website-delivery-pipeline/SKILL.md](website-delivery-pipeline/SKILL.md)
- [adaptive-skill-routing-and-context-budget/SKILL.md](adaptive-skill-routing-and-context-budget/SKILL.md)
- [project-context/SKILL.md](project-context/SKILL.md)
- [PHASE-AWARE-GATING.md](PHASE-AWARE-GATING.md)
- [PROJECT-INSTRUCTIONS-PHASE-AWARE.md](PROJECT-INSTRUCTIONS-PHASE-AWARE.md)
- [SKILL-CATALOG.md](SKILL-CATALOG.md)
- [V5-ARCHITECTURE.md](V5-ARCHITECTURE.md)

Superseded prompt/architecture revisions are intentionally not kept beside the canonical working files. Git history is the archive; see [docs/history/README.md](docs/history/README.md).

## Current lifecycle reliability rules

Canonical requirement states:

```text
DONE_VERIFIED
N/A_JUSTIFIED
PENDING_FUTURE_PHASE
BLOCKED
```

Only requirements **DUE NOW** participate in the current phase exit gate. Future QA/release evidence must use `OWNER_PHASE` + verification plan rather than create artificial early blockers.

## Routing model

Use the smallest skill graph justified by scope, phase, risk and mode. Do not load the whole library.

```text
project truth
→ scope/type/risk/mode
→ smallest applicable skill graph
→ evidence/reference/design intelligence only when useful
→ Design Contract
→ implementation
→ verification
→ release when authorized
```

For ordinary design/redesign implementation work, prefer `interactive_prototype`. Use `production_candidate` only when real integrations, security/privacy, performance/browser, release/rollback or production verification are materially required.

## Reference intelligence

`design-reference-research-and-benchmark` is used before visual direction when substantial work needs stronger reference grounding.

Source roles:

- real industry/product sites → IA, journey, trust, conversion and responsive behavior;
- curated/award sites → visual craft, typography, composition, storytelling and motion;
- case studies/shots → brand/component/concept ideas with production caveats;
- mood/editorial sources → photography, texture and art direction.

Hard rule: popularity/awards are not UX, accessibility or conversion proof. Extract principles and adapt; do not clone branded surface/assets.

## Vendored UI UX Pro Max design intelligence

`skills_UIUX` vendors the complete pinned UI UX Pro Max skill/runtime source under `vendor/ui-ux-pro-max/`:

- all seven upstream `.claude/skills/*` packages;
- complete `src/ui-ux-pro-max` data/search/reasoning/templates/tests tree;
- upstream MIT license and immutable provenance metadata.

The vendor corpus is **not** global prompt context. Route it through [design-intelligence-retrieval/SKILL.md](design-intelligence-retrieval/SKILL.md), which selects the smallest relevant mode (`--design-system`, one explicit `--domain`, or detected `--stack`), verifies the match, retries once when needed and requires `ADOPT / ADAPT / REJECT` synthesis against project truth.

Augmentation module: [DESIGN-INTELLIGENCE-AUGMENTED-REDESIGN-PROMPT.md](DESIGN-INTELLIGENCE-AUGMENTED-REDESIGN-PROMPT.md).

Precedence:

```text
current user request
→ project truth/source
→ passed Design Contract/artifacts
→ routed local skills
→ retrieved design intelligence
→ generic model prior
```

An upstream-generated `design-system/<project>/MASTER.md` is candidate intelligence, not the canonical project Design Contract. Never use upstream `--force` without explicit user authorization.

## Repository layout

```text
skills_UIUX/
├── README.md
├── SKILL-CATALOG.md
├── *current canonical prompt/governance docs*
├── <skill-name>/SKILL.md
├── profiles/
├── packs/
├── evals/
├── scripts/
├── examples/
├── docs/
│   ├── history/
│   └── uiux/
├── vendor/ui-ux-pro-max/
└── .github/workflows/
```

Root skill folders are intentionally preserved because profiles/installers/validators resolve `*/SKILL.md`. Do not reorganize them into another namespace without a migration of consumer install/runtime contracts.

The `vendor/ui-ux-pro-max/` trees are immutable snapshots for the locked upstream SHA. Local routing/adapter/docs must live outside the vendor tree.

## Recommended project config

```json
{
  "schema_version": 2,
  "profile": "uiux-corporate",
  "packs": [
    "research-validation",
    "experience-strategy",
    "inclusive-trust",
    "measurement-reliability"
  ],
  "additional_skills": ["website-audit-and-redesign"],
  "exclude_skills": [],
  "project": {
    "name": "My Project",
    "mode": "interactive-prototype",
    "domain": "corporate"
  },
  "source_of_truth": ["docs/brand.md", "docs/sitemap.md"],
  "constraints": ["Reuse existing tokens and components"]
}
```

Add `production-delivery` only when production-level integration/release requirements are active.

## Install / sync

```bash
python scripts/install-project.py ../MyProject --dry-run
python scripts/install-project.py ../MyProject
```

Or bootstrap a project profile:

```bash
python scripts/bootstrap-project.py ../MyProject --profile uiux-corporate
```

Skills are copied to `<project>/.claude/skills/<skill-name>/`. Dependency-aware install also carries the vendored design-intelligence runtime when `design-intelligence-retrieval` is selected.

For release-critical consumers, prefer immutable tag/commit SHA over floating `main`.

## Capability packs

| Pack | Khi nào bật |
|---|---|
| `research-validation` | discovery, uncertainty, IA/usability validation, benchmark |
| `experience-strategy` | audience intent, journey/content redesign, experiential services |
| `measurement-reliability` | outcome proof, conformance, regression, repeated-agent reliability |
| `production-delivery` | real integrations, security/privacy, performance/browser, release/rollback/monitoring |
| `advanced-interaction` | search, complex forms, workflows, tables, dashboards, account UX |
| `inclusive-trust` | broad audience, high consequence/trust, cognitive/AT concerns |
| `designops-governance` | mature design systems and cross-project consistency |
| `human-ai` | end-user generative/predictive/agentic AI |

## Hard truth rules

- no evidence → no `validated` research claim;
- no appropriate evaluation → no accessibility conformance claim;
- no outcome data → no claim that UX improved;
- award/curated reference → inspiration evidence, not UX proof;
- retrieved design recommendation → candidate intelligence, not project truth;
- rendered success state → not backend/system success proof;
- mock/simulated integration → not production-ready;
- build/CI success → not rendered visual QA;
- screenshot existence → not visual inspection;
- deploy success → not production verification without relevant smoke.

## Eval / validation

```bash
python scripts/validate-skills.py
python scripts/validate-v2.py
python scripts/validate-vendor-uiux-pro-max.py
python -B design-intelligence-retrieval/scripts/query.py "education admissions mobile" --design-system
python scripts/skill-stats.py
python scripts/eval-harness.py smoke
```

Provider adapters follow [evals/ADAPTER-CONTRACT.md](evals/ADAPTER-CONTRACT.md).

## Backward compatibility

- V2/V2.1/V3/V4 profiles remain valid;
- schema-version-1 and schema-version-2 project configs remain supported;
- existing root skill names remain valid;
- `install-profile.py` remains supported.

Historical architecture/prompt documents are not runtime compatibility contracts; Git history remains the source for superseded revisions.
