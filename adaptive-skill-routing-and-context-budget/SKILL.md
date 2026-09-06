---
name: adaptive-skill-routing-and-context-budget
description: Selects the smallest useful skill graph for the current task based on project context, scope and risk, while escalating to deeper packs only when needed. Use at agent task start or when the skill library is large enough that loading everything would waste context and reduce focus.
---

# Adaptive Skill Routing & Context Budget

## Principle
`maximum decision quality / minimum unnecessary context`

Do not load every installed skill merely because it exists.

## Routing workflow
### 1. Classify task scope
Typical levels:
- **local** — one component/state/style defect;
- **page** — one page/flow redesign;
- **journey** — multiple pages/steps for a user outcome;
- **system/site** — IA, brand, design system or whole-site redesign;
- **production/reliability** — release, conformance, regression or measurement work.

### 2. Classify risk
Escalate for:
- money/privacy/consent/security;
- accessibility-critical flows;
- high traffic/conversion consequence;
- major brand/IA/content change;
- irreversible migration;
- complex data/workflow;
- weak/contradictory evidence.

### 3. Build the minimal graph
Always read project context/source-of-truth first. Then choose:
- domain/base capabilities;
- one orchestrating skill when needed;
- narrow specialists justified by task/risk;
- references/checklists only when their decision is active.

### 4. Escalate, do not pre-load
If evidence reveals a new risk, add the relevant specialist at that point.

### 5. Record material routing decisions
For large work, note `task → risk → skills/packs used → why`.

## Adaptive knowledge retrieval

Large searchable knowledge corpora follow the same context-budget principle as skills: **retrieve the smallest decision-relevant subset**.

For the vendored UI UX Pro Max corpus:
- route `design-intelligence-retrieval` only when an active UI/UX decision benefits from external design knowledge;
- select the smallest mode: system direction → `--design-system`, focused concern → explicit `--domain`, implementation concern → detected `--stack`;
- query first, then load only returned candidates and directly relevant provenance;
- retry once if empty/off-topic, then stop and record no verified match;
- never preload full CSV/JSON catalogs merely because they are installed;
- never activate all vendored skills as a default UI graph;
- keep persisted upstream design-system artifacts subordinate to the project Design Contract.

A larger installed knowledge base should reduce uncertainty, not increase prompt noise.

## External specialist adapter routing

External knowledge sources are represented by narrow local adapters with pinned provenance. **Installed does not mean active.** Route only the adapter that owns the current decision:

- `visual-taste-calibration` → only after a visual direction exists and feels generic/interchangeable, over-decorated or insufficiently subject-specific;
- `web-ui-code-review` → code-level UI/pre-merge review or source-level root-cause analysis; React/Next reference only after detecting stack/version;
- `reference-extraction-and-design-audit` → only for selected references/current-project system evidence needing deeper token/layout/component extraction, not every benchmark candidate;
- `ux-writing-and-microcopy` → only when interface strings/states materially affect comprehension, action, trust, recovery or localization.

### Progressive disclosure rule

For an external specialist:

```text
adapter SKILL.md
→ decide whether deeper knowledge is needed
→ read one directly linked reference
→ inspect project evidence
→ act / verify
```

Do not load every external reference in a phase. Do not load the original upstream repository merely to restate generic guidance.

### Precedence and collision control

When an external source recommends something that conflicts with project truth:

```text
current user request
→ project truth/source
→ passed Design Contract/artifacts
→ routed local owner skill
→ external specialist synthesis
→ generic model prior
```

Record material conflict; never silently let an external convention override brand, responsive scope, framework version, design-system ownership or release rules.

### External adapter near-miss examples

- Header button is 2px off a known project token → project-context + ui-improvement; **not** visual taste, Vercel, extraction or design database.
- One CTA label is vague during payment confirmation → route `ux-writing-and-microcopy`, plus system reality if consequence/recovery depends on backend behavior; do not activate full content strategy.
- Next.js component has serial data awaits → `web-ui-code-review` with React/Next reference; do not route visual-design skills unless UI composition is also in scope.
- User provides 15 inspiration URLs → benchmark all at appropriate depth, but run deep extraction only on shortlisted/material references.

## Examples
- `Fix mobile menu focus trap` → project-context + interaction + responsive + accessibility; not service blueprinting or full design-intelligence retrieval.
- `Redesign school admissions journey` → education + experience-strategy + research/validation + complex forms + inclusive/trust; add design-intelligence retrieval only for a concrete visual/product/stack knowledge gap; add visual taste only after a direction draft exists.
- `Formal pre-release UI code audit for Next.js` → project-context + web-ui-code-review + testing/release; escalate to accessibility/performance/rendered QA owners for material findings.
- `Choose direction for a new healthcare portal` → project-context + domain/UX graph + focused design-intelligence `--design-system`, then synthesize before visual-direction lock; run visual taste calibration only if the result remains interchangeable/generic.

## Gate
If a task is spending more effort restating generic guidance than inspecting the actual project, reduce the active skill set.

## Anti-patterns
- All packs on every task.
- Using a large profile as a substitute for project inspection.
- Never escalating after discovering new risk.
- Loading deep references before knowing they are relevant.
- Treating an installed database as prompt context instead of a retrieval source.
- Activating all external specialist adapters just because they are installed.
- Loading both local owner guidance and several external copies of the same rule when one pinned synthesis is enough.
- Letting a vendor/external skill become a second lifecycle orchestrator.
