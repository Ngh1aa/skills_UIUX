# skills_UIUX V3 Architecture

V3 adds an evidence-and-validation layer on top of V2.1 without breaking existing project profiles.

## Core idea

`project truth → research evidence → validated UX/IA → system design → implementation → verification → measured learning`

V3 does **not** install every new skill by default. Advanced capability is grouped into opt-in packs.

## Capability packs

- `research-validation` — research planning, moderated testing, synthesis, benchmarking, card/tree validation, service blueprinting, prototype strategy.
- `advanced-interaction` — site search, complex forms, states, long workflows, enterprise tables, dashboards, auth and preferences.
- `inclusive-trust` — content design, cognitive inclusion, assistive-tech testing, trust and deceptive-pattern prevention.
- `designops-governance` — design critique and design-system governance/adoption.
- `human-ai` — human-centered AI interaction design.

Packs live in `packs/*.json` and can be enabled from a project `.uiux-profile.json` using schema version 2.

## Project config V3

```json
{
  "schema_version": 2,
  "profile": "uiux-corporate",
  "packs": ["research-validation", "inclusive-trust"],
  "additional_skills": ["website-audit-and-redesign"],
  "exclude_skills": []
}
```

Schema version 1 remains accepted for backward compatibility.

## Evidence hierarchy

1. Current user instruction
2. Project `.uiux-profile.json`
3. Project source-of-truth docs
4. Observed user/research/analytics evidence
5. Domain specialist skills
6. Generic UI/UX guidance

Generic patterns must not override project evidence without rationale.

## Validation philosophy

- Research skills produce traceable evidence, not invented personas.
- IA should be validated when findability risk is material.
- Complex UI must define full state and recovery behavior.
- Accessibility combines automated and manual/assistive-tech evidence.
- Ethical/trust review is a release gate for high-consequence flows.
- AI interfaces require control, correction and graceful failure.

## Backward compatibility

V2/V2.1 profiles and `install-profile.py` remain valid. Existing schema-version-1 project configs continue to install normally.
