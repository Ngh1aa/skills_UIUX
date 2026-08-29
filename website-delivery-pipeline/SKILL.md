---
name: website-delivery-pipeline
description: Orchestrates the full lifecycle of building or redesigning a professional website. Use at project start, for multi-phase work, or when deciding which UI/UX skills, capability packs, domain playbooks, artifacts and quality gates are needed.
---

# Website Delivery Pipeline — V3 Orchestrator

## Core principle
`business/user goal → project truth → evidence → validated UX/IA → brand/system → implementation → verification → measured learning`

Do not load the whole library. Route the smallest useful profile + packs + specialists.

## Step 0 — Read project context
If `.uiux-profile.json` exists, read it plus every `source_of_truth` file before applying generic rules. Project evidence overrides generic defaults unless a higher-priority user instruction changes direction.

## Step 1 — Choose base profile
Use `profiles/*.json` for project/domain baseline. V2/V2.1 profiles remain valid.

## Step 2 — Add V3 packs only when risk justifies them
- High product/behavior uncertainty, redesign validation or IA risk → `research-validation`.
- Complex search/forms/state/workflow/data/account UI → `advanced-interaction`.
- Broad audience, high trust, accessibility or high-consequence decisions → `inclusive-trust`.
- Mature design system or repeated cross-project UI work → `designops-governance`.
- End-user AI features → `human-ai`.

## Pipeline
| Phase | Required / conditional capabilities | Gate |
|---|---|---|
| 0 Intake | discovery + project context | problem, audience, JTBD, scope, KPI |
| 0A Existing | website audit | preserve/change rationale |
| 1 Evidence | optional research-validation | assumptions tagged as evidence/hypothesis |
| 2 UX/IA | journey + IA + optional card/tree testing | primary flow and findability |
| 3 Brand/visual | brand + visual + media | implementable visual grammar |
| 4 System | design system + interaction + optional designops | reusable components/states |
| 5 Content | conversion/content + optional content-design | understandable hierarchy/questions |
| 6 Architecture/code | frontend architecture + implementation | maintainable working UI |
| 7 Inclusive | responsive + accessibility + optional cognitive/AT | usable critical journeys |
| 8 Advanced behavior | optional search/forms/state/data/auth/AI | no dead-end/undefined high-risk states |
| 9 Quality | visual QA + performance + SEO + security + ethical/trust where relevant | evidence-backed findings |
| 10 Test/release | tests + analytics + release | verified journeys and known issues |
| 11 Production | monitoring + UX metrics/research when useful | regression + learning loop |

## V3 routing rules
- Do not invent user research findings. Mark assumptions and propose research.
- For redesigns, preserve proven content/SEO/behavior until evidence supports change.
- Complex flows require state/error/recovery definitions before being called complete.
- Automated accessibility scans never replace manual critical-journey checks.
- Money/consent/subscription/privacy flows require deceptive-pattern review.
- AI flows require capability limits, control/correction and graceful failure.

## Evaluation loop
1. `python scripts/validate-skills.py`
2. `python scripts/validate-v2.py` (backward-compatible V3 validator)
3. Run representative `evals/tasks/*.json`
4. Grade outcome using `evals/RUBRIC.md` plus deterministic checks
5. Promote stable capability evals to regression coverage

## Completion rule
Never say `done`, `fully responsive`, `accessible` or `validated` without corresponding evidence. Report verified versus unverified explicitly.
