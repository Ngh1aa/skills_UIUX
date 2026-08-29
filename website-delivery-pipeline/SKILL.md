---
name: website-delivery-pipeline
description: Orchestrates the full lifecycle of building or redesigning a professional website. Use at project start, for multi-phase work, or when deciding which UI/UX skills, capability packs, domain playbooks, artifacts and quality gates are needed.
---

# Website Delivery Pipeline — V4 Orchestrator

## Core principle
`business/user goal → project truth → audience/entry intent → evidence → whole journey → validated UX/IA → distinctive experience/system → implementation → joined-up verification → measured learning`

Do not load the whole library. Route the smallest useful profile + packs + specialists.

## Step 0 — Read project context
If `.uiux-profile.json` exists, read it plus every `source_of_truth` file before applying generic rules. Project evidence overrides generic defaults unless a higher-priority user instruction changes direction.

## Step 1 — Choose base profile
Use `profiles/*.json` for project/domain baseline. Older profiles remain valid.

## Step 2 — Add packs only when risk justifies them
- Substantial content/layout redesign, experiential service, brand differentiation or online/offline journey → `experience-strategy`.
- High product/behavior uncertainty, redesign validation or IA risk → `research-validation`.
- Complex search/forms/state/workflow/data/account UI → `advanced-interaction`.
- Broad audience, high trust, accessibility or high-consequence decisions → `inclusive-trust`.
- Mature design system or repeated cross-project UI work → `designops-governance`.
- End-user AI features → `human-ai`.

## Pipeline
| Phase | Required / conditional capabilities | Gate |
|---|---|---|
| 0 Intake | discovery + project context | problem, owner goal, scope, KPI |
| 0A Audience | optional/likely V4 audience + entry intent | who, why now, top tasks, evidence gaps |
| 0B Existing | website audit | preserve/change rationale |
| 1 Evidence | optional research-validation | assumptions tagged as evidence/hypothesis |
| 2 Whole journey | optional V4 service/omnichannel mapping | real journey, channels and key moments known |
| 3 UX/IA | journey + IA + optional card/tree testing | primary flows and findability |
| 4 Content/experience | optional V4 journey-driven layout + experience principles | sections follow user questions/decisions |
| 5 Brand/visual | brand + visual + media + optional V4 digital signature | implementable, recognizable visual grammar |
| 6 System | design system + interaction + optional designops | reusable components/states |
| 7 Architecture/code | frontend architecture + implementation | maintainable working UI |
| 8 Inclusive | responsive + accessibility + optional cognitive/AT | usable critical journeys |
| 9 Advanced behavior | optional search/forms/state/data/auth/AI | no dead-end/undefined high-risk states |
| 10 Quality | visual QA + V4 recognition/continuity + performance + SEO + security + trust/ethics | evidence-backed findings |
| 11 Test/release | tests + analytics + release | verified journeys and known issues |
| 12 Production | monitoring + UX metrics/research when useful | regression + learning loop |

## V4 routing rules
- Distinguish owner goals from user goals; design should reconcile them rather than silently substitute one for the other.
- Do not assume all visits start at the homepage. Important deep pages must orient entry traffic.
- Do not map content inventory directly into page blocks; order content around user questions and decision confidence.
- Logo + primary color alone is not sufficient evidence of a distinctive digital identity.
- Screenshot/crop recognition is a useful internal heuristic, not a standardized brand-recall metric unless tested with real users.
- For experiential services, translate meaningful service moments—not physical steps literally—into digital representations.
- If the real service continues after a form, booking or application, design the handoff, confirmation and recovery.

## V3 rules retained
- Do not invent user research findings. Mark assumptions and propose research.
- For redesigns, preserve proven content/SEO/behavior until evidence supports change.
- Complex flows require state/error/recovery definitions before being called complete.
- Automated accessibility scans never replace manual critical-journey checks.
- Money/consent/subscription/privacy flows require deceptive-pattern review.
- AI flows require capability limits, control/correction and graceful failure.

## Evaluation loop
1. `python scripts/validate-skills.py`
2. `python scripts/validate-v2.py` (backward-compatible V4 validator)
3. Run representative `evals/tasks/*.json`
4. Grade outcome using `evals/RUBRIC.md` plus deterministic checks
5. Promote stable capability evals to regression coverage

## Completion rule
Never say `done`, `fully responsive`, `accessible`, `validated` or `brand-consistent` without corresponding evidence. Report verified versus unverified explicitly.
