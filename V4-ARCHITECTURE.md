# skills_UIUX V4 Architecture — Audience, Brand Memory & Service Experience

V4 adds an **experience-strategy layer** on top of V3. It does not replace V3 research, IA, design-system, advanced interaction or accessibility capabilities.

## Core idea

`project truth → audience/visit intent → top tasks → whole service journey → journey-driven content → distinctive brand memory → implementation → omnichannel continuity → recognition/experience QA`

## Why V4 exists

V3 can validate usability and interaction quality, but a technically strong site can still fail if:
- it is not explicit about who the primary users are and why they visit;
- content order mirrors the organization instead of the user's decision journey;
- every cropped screen looks like a generic category template once the logo is removed;
- a website sells a real-world experience but feels like a brochure;
- online and offline steps do not join up coherently.

## New capability pack

`experience-strategy` contains:
1. `audience-intent-and-top-tasks`
2. `entry-context-and-visit-intent`
3. `journey-driven-content-and-layout`
4. `brand-distinctiveness-and-visual-signature`
5. `service-experience-to-digital-journey`
6. `experience-principles-and-signature-moments`
7. `omnichannel-experience-continuity`
8. `brand-recognition-and-consistency-qa`

## When to enable
Enable for:
- redesigns where content/layout is being substantially rethought;
- schools, buildings, hospitality, retail/showroom and other experiential services;
- corporate sites where credibility and brand differentiation matter;
- acquisition-heavy sites with multiple entry contexts;
- multi-channel journeys involving visits, sales, admissions, calls, bookings or follow-up.

Do not enable merely because a site has branding. For a tiny one-purpose landing page, individual skills may be enough.

## Evidence discipline
- User evidence beats internal opinion.
- Business objectives matter, but do not overwrite critical user needs.
- Distinguish observed evidence from assumptions.
- Screenshot recognition is an internal heuristic unless tested with real users; do not present it as standardized brand-recall research.
- "Immersive" interactions require task/service value, not spectacle.

## Relationship to V3
- `research-validation` finds/validates user evidence.
- `information-architecture` organizes destinations and findability.
- `experience-strategy` determines audience intent, journey logic and recognizable service expression.
- `visual-design-direction` + `design-system-and-components` implement the expression systematically.
- `inclusive-trust` ensures clarity, cognitive access, trust and ethical behavior.
- `advanced-interaction` handles complex functional states.

## Project config
```json
{
  "schema_version": 2,
  "profile": "uiux-corporate",
  "packs": ["research-validation", "experience-strategy", "inclusive-trust"],
  "additional_skills": ["website-audit-and-redesign"],
  "exclude_skills": []
}
```

No schema change is required because V3 pack routing is generic.

## V4 quality gates
Before major layout/content redesign:
- primary audiences and top tasks are explicit;
- assumptions vs evidence are visible;
- important entry contexts are known;
- current/desired whole-service journey is understood when relevant.

Before visual lock:
- experience principles are actionable;
- digital signature cues are defined;
- content order follows user questions/decisions.

Before release:
- representative sections pass consistency/recognition review;
- online/offline handoffs have confirmation and recovery;
- no major journey ends at an organizational boundary or unexplained form submission.
