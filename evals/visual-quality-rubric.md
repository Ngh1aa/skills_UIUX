# Visual Quality Eval Rubric — V5.1

Chuyên dùng để chấm **visual output quality** của website được tạo/redesign bởi agent. CI chứng minh "không hỏng"; rubric này chứng minh "đẹp và ổn định hơn".

## Grading approach

1. **Deterministic gates** (pass/fail — machine verifiable):
   - Route renders without runtime crash
   - Required pages exist and load
   - Screenshots captured for evidence
   - No horizontal overflow at standard viewports
   - Media assets not broken (no 404, no missing `<img>`)
   - Viewport meta tag present
   - Build/runtime usable

2. **Model/human judgment** (0–4 scale per dimension):
   - Requires rendered screenshots or live page
   - Model grader provides initial score
   - Human review calibrates and validates

> **Note**: Không hard-check CSS custom properties hay font-family declarations. Website đẹp hoàn toàn có thể dùng `system-ui`. Next.js/React có thể không có `.html` tĩnh để analyze.

## 7 Dimensions — 0–4 scale

### 1. Hierarchy & information architecture — 20%

- 0: no discernible visual hierarchy; all elements compete equally.
- 1: basic heading size difference but priority unclear.
- 2: hierarchy exists but inconsistent across sections; some competing elements.
- 3: clear primary/secondary/tertiary hierarchy; CTA prominence appropriate.
- 4: hierarchy perfectly supports user scanning and task completion; content priority matches business/user goal; entry points clear at every scroll depth.

### 2. Typography system — 15%

- 0: browser defaults throughout; no intentional type system.
- 1: single font applied but no scale/rhythm.
- 2: basic scale (2–3 sizes) with reasonable readability.
- 3: considered type system with proper scale, line height, measure; distinct heading/body/caption roles.
- 4: polished typographic rhythm; pairing has character and rationale; micro-typography (letter-spacing, ligatures, optical sizing) appropriate; type reinforces brand voice.

### 3. Media & art direction — 15%

- 0: broken images, placeholder boxes, or irrelevant stock.
- 1: images present but generic stock with no cropping consideration.
- 2: relevant images with basic sizing; some crop/aspect issues.
- 3: images support content; consistent aspect ratios; appropriate sizing.
- 4: art direction has clear intent; crops highlight subject; media-to-copy relationship considered; images contribute to brand narrative; no watermarks or obviously AI-generated artifacts.

### 4. Page-role diversity — 15%

- 0: all pages are visually interchangeable (same hero → cards → CTA).
- 1: minor variations (different hero image) but same skeleton.
- 2: 2 distinct compositions for 5+ page roles.
- 3: 3+ distinct composition families; page structure reflects content purpose.
- 4: each page role has composition optimized for its user task; homepage ≠ about ≠ services ≠ project detail; cross-page coherence maintained through system, not template cloning.

Automated signal: `scripts/template-monotony-detector.py` provides structural diversity data.

### 5. Responsive transformation — 10%

- 0: broken at mobile widths; horizontal scroll; unreadable.
- 1: content reflows but no intentional adaptation.
- 2: basic responsive; stacks to single column with acceptable results.
- 3: breakpoint-appropriate layout changes; touch targets adequate; navigation adapts.
- 4: mobile has intentional re-composition (not just stacked desktop); critical actions accessible; media/type adapts; mobile-specific interaction patterns where appropriate.

### 6. Brand distinctiveness — 15%

- 0: could be any website; no brand expression.
- 1: logo present but design is generic template.
- 2: brand colors applied but interchangeable with a different logo.
- 3: consistent brand expression; recognizable color/type/imagery system.
- 4: design is recognizable with logo hidden; visual signature extends beyond color; brand personality expressed through composition, motion, imagery style and interaction character.

### 7. Anti-generic-AI — 10%

- 0: obvious AI-template: glass cards, gradient borders, rounded everything, identical section spacing, over-decorated.
- 1: 3+ generic AI patterns present; decorative gradients, unnecessary blur effects.
- 2: mostly clean but 1–2 template-ish patterns.
- 3: purposeful design choices; decoration justified by function.
- 4: no template smell; design choices are specific to the domain/brand/content; ornamentation serves hierarchy or brand, never filler.

## Composite score

```
score = sum(dimension_score × dimension_weight) / 4 × 100
```

Range: 0–100.

## Hard fail triggers

Regardless of dimension scores, the visual quality eval FAILS if:

- All primary pages share the same hero+cards+CTA silhouette
- Stock photos with visible watermarks on hero/primary images
- Mobile is pure column-stack of desktop with zero layout adaptation
- Critical content/CTA is invisible or unreachable without horizontal scroll
- Page has no visible content (blank, all-white, all-black)
- Brand assets are from a different company/industry

## Grading protocol

1. Deterministic gates first — any gate failure → score capped at 30.
2. Capture screenshots: desktop (1440px) + mobile (375px) for each page.
3. Score each dimension 0–4.
4. Compute composite score.
5. Check hard fail triggers.
6. Record confidence: `high` (clear) / `medium` (borderline) / `low` (needs human).
