# MASTER PRE-DESIGN RESEARCH PROMPT V3.0
## PROJECT TRUTH → BUSINESS ↔ USER → JOURNEY → IA/CONTENT → BRAND EVIDENCE → REFERENCE INTELLIGENCE → DESIGN DNA → PAGE-ROLE COMPOSITION → DESIGN CONTRACT

> **V3.0 purpose:** Prompt 1 KHÔNG code. Nó phải tạo một **Design Contract đủ cụ thể để Prompt 2 không được phép quay về generic/template UI**.
>
> **Failure this version prevents:** research rất dài nhưng cuối cùng coder vẫn dùng cùng hero/layout cho mọi page, chỉ đổi màu/font/ảnh; brand guideline thiếu thì tự đoán; reference chỉ dùng như moodboard; user phải tự chỉ ra lỗi visual hiển nhiên sau mỗi vòng.

---

# 0. PROJECT CONFIG

```yaml
project_name: [...]
project_type: [redesign_existing | improve_existing | new_website | application | landing_page | ecommerce | corporate | education | real_estate | SaaS | other]
current_website: [...]
source_code_repo: [...]
industry: [...]
market: [...]
languages: [...]
brand_guideline: [URL/file/UNKNOWN]
brand_assets: [logo/font/image/app/campaign/etc.]
existing_sitemap: [...]
existing_documents: [...]
primary_business_goal: [...]
secondary_business_goals: [...]
known_target_audience: [...]
known_conversion_actions: [...]
competitors_if_known: [...]
reference_websites_if_known: [...]
tech_stack: [...]
cms_backend: [...]
analytics: [...]
constraints: [...]
special_requirements: [...]
```

Unknown giữ `UNKNOWN`. Không fabricate để lấp brief.

---

# 1. OPERATING RULES

Đóng vai senior cross-functional team: Business/Product, UX Research/Strategy, IA, Content/Conversion, Brand, Visual/UI, Design System, Interaction, Accessibility, SEO, Frontend, Performance, Analytics/CRO.

Sử dụng `https://github.com/Ngh1aa/skills_UIUX` theo minimal skill graph.

Với substantial redesign, ưu tiên:

```text
website-delivery-pipeline
project-context
website-audit-and-redesign
product-discovery
audience-intent-and-top-tasks
entry-context-and-visit-intent
ux-research-and-journey
information-architecture
journey-driven-content-and-layout
brand-guidelines
design-reference-research-and-benchmark
real-world-artifact-and-domain-metaphor-design (conditional)
brand-distinctiveness-and-visual-signature
visual-design-direction
responsive-and-device-strategy
accessibility
seo-strategy
system-reality-and-production-readiness
```

Mỗi skill chỉ ghi `USED` nếu đã đọc + thay đổi decision.

---

# 2. HARD NO-CODE GATE

Prompt này **không được sửa source code**.

Không chuyển sang Prompt 2 nếu chưa khóa được các material decisions sau:

- business goal + primary conversion;
- owner wants ↔ user wants intersection;
- primary audiences + top tasks + entry contexts;
- primary journey;
- sitemap + page roles;
- preserve/change/remove/add decisions;
- brand source status + evidence ledger;
- semantic color roles + typography/media direction;
- reference benchmark theo page role;
- Design DNA + visual signatures;
- page-role composition matrix;
- hero/top-of-page strategy theo page role;
- 3 representative composition proofs cho substantial multi-page site;
- mobile transformation rules;
- system reality constraints;
- Visible Redesign Delta;
- explicit DO / DO NOT.

Nếu output vẫn chỉ là `modern / premium / clean`, một universal hero, hoặc one-layout-fits-all → **RESEARCH FAIL**.

---

# 3. EVIDENCE DISCIPLINE

Mỗi material finding label:

```text
FACT
EVIDENCE-BACKED INFERENCE
PROFESSIONAL HYPOTHESIS
ASSUMPTION
UNKNOWN
```

Mỗi recommendation dùng:

`Evidence → Insight → User impact → Business impact → Design implication → Recommendation → Priority`

Evidence hierarchy:

1. project truth / supplied docs / source;
2. first-party official source;
3. credible standards/research;
4. real production competitors/category sites;
5. curated/award/case-study/mood references.

---

# 4. PROJECT TRUTH & BUSINESS DISCOVERY

Tạo:

| Information | Finding | Source | Status/confidence | Design implication |
|---|---|---|---|---|

Xác định:

- website role trong business model;
- sản phẩm/dịch vụ;
- market/geography/languages;
- primary conversion;
- decision cycle;
- trust/compliance constraints;
- technical constraints.

Business mapping:

| Business goal | Website responsibility | User action | KPI/signal |
|---|---|---|---|

Không dùng KPI mơ hồ kiểu “tăng traffic” nếu business outcome là qualified lead/application/purchase.

---

# 5. BRAND SOURCE RESOLUTION — BẮT BUỘC

Phân loại:

```text
A — OFFICIAL BRAND GUIDELINE AVAILABLE
B — PARTIAL OFFICIAL BRAND ASSETS AVAILABLE
C — LOGO AVAILABLE, NO BRAND GUIDELINE
D — NO RELIABLE BRAND ASSET
```

Evidence priority:

`official guideline → official logo/vector → official website/app/report/profile → official campaign/signage → logo analysis → professional inference`

Nếu C: tạo **PROPOSED BRAND GUIDELINE — LOGO-DERIVED**.

Status dùng:

```text
OFFICIAL
VERIFIED_FROM_OFFICIAL_ASSET
INFERRED_FROM_LOGO
INFERRED_FROM_OFFICIAL_ASSETS
PROPOSED_FOR_DIGITAL
PROPOSED_FOR_ACCESSIBILITY
UNKNOWN
```

Không suy ra mission/positioning/tone từ logo.

### Brand evidence ledger

| Dimension | Finding | Source | Status | Confidence | UI/content implication |
|---|---|---|---|---|---|

### Semantic color role map

Không chỉ palette. Define:

- Brand Primary/Secondary;
- Page Background;
- Light/Dark/Alternate Surface;
- Text Primary/Secondary/Muted/Inverse;
- Border/Divider;
- Primary Action/Hover/Active/Focus;
- Link;
- Accent/Wayfinding;
- Success/Warning/Error/Info khi applicable.

`LOGO COLOR ≠ UI SEMANTIC COLOR`.

### Logo state matrix

Phải tính trước logo trên:

`top nav | scrolled nav | dark surface | light surface | mobile menu | footer`.

---

# 6. AUDIENCE / JTBD / TOP TASKS

Không tạo persona chỉ từ demographics.

| Audience | Trigger | Context | Motivation | Barrier | Top task | Success |
|---|---|---|---|---|---|---|

JTBD:

> Khi [context], tôi muốn [action], để [outcome].

Top tasks:

| Priority | User task | Main question | Evidence needed | Barrier | Next action |
|---:|---|---|---|---|---|

Page name không phải task.

---

# 7. OWNER GOAL ↔ USER GOAL

Artifact bắt buộc:

| Owner wants to show/prove | User wants to know/do | Intersection | Website responsibility | Proof needed | CTA timing |
|---|---|---|---|---|---|

Nếu owner muốn “show brand” còn user cần “evidence để quyết định”, layout phải phục vụ cả hai thay vì biến mọi page thành brand banner.

---

# 8. ENTRY CONTEXT

Không mặc định homepage.

| Entry source | Likely intent | Prior knowledge | Landing expectation | Required orientation | Next action |
|---|---|---|---|---|---|

Primary deep pages phải hoạt động như landing page độc lập.

---

# 9. EXISTING WEBSITE AUDIT — REDESIGN ONLY

Inventory:

| Page/template | Role | Primary user | CTA | Content/SEO value | Decision |
|---|---|---|---|---|---|

Decision:

`KEEP | IMPROVE | MERGE | REMOVE | ADD`

Bắt buộc có Preserve List:

- URLs/SEO equity;
- high-value content;
- business facts;
- useful flows;
- brand assets;
- useful components/tokens;
- user conventions.

### Page-family/template audit

| Page family | User question | Existing composition | What works | Template smell | Redesign implication |
|---|---|---|---|---|---|

Flag nếu các page role khác nhau đều dùng cùng hero/card rhythm mà không rationale.

### Design implementation debt

Audit:

- CSS override layers;
- duplicate components/tokens;
- page-local patches;
- stale generators;
- asset caching/versioning;
- scattered responsive rules;
- fake dynamic states.

---

# 10. USER JOURNEY

Map:

`Entry → Orientation → Exploration → Evaluation → Comparison → Trust → Decision → Conversion → Confirmation/Post-conversion`

| Stage | Intent | Main question | Required content/proof | Interaction | Pain | CTA | Signal |
|---|---|---|---|---|---|---|---|

CTA chỉ xuất hiện khi user có đủ decision context.

---

# 11. IA & CONTENT ARCHITECTURE

IA:

`Audience → Top Tasks → Questions → Content → Page Role → Navigation`

| Page | Role | Audience | Top task | Primary CTA | Secondary CTA | SEO intent |
|---|---|---|---|---|---|---|

Mỗi section có job:

`ORIENT | EXPLAIN | DEMONSTRATE | PROVE | COMPARE | INSPIRE | REDUCE_RISK | HELP_DECIDE | CONVERT | TRANSITION`

Không có job → remove/merge/redesign.

---

# 12. PAGE EXPERIENCE CONTRACT

Cho Homepage + primary pages:

```text
PAGE / ROLE:
PRIMARY AUDIENCE:
ENTRY CONTEXT:
USER GOAL:
OWNER GOAL:
OWNER ↔ USER INTERSECTION:
PRIMARY QUESTION:
SECONDARY QUESTIONS:
DECISION ENABLED:
PROOF REQUIRED:
OBJECTIONS:
PRIMARY CTA:
NEXT DESTINATION:
SEO INTENT:
CONTENT PRIORITY:
FIRST VISUAL ANCHOR:
VISUAL STRATEGY:
DOMAIN DECISION OBJECT / ARTIFACT:
INTERACTION STRATEGY:
MOBILE PRIORITY:
```

---

# 13. COMPETITOR + REFERENCE RESEARCH

Research 2–4 direct competitors + adjacent best-in-class khi useful.

Reference candidate pool cho substantial design: thường 10–20 candidates, nhưng quality > count.

Mỗi material reference phải inspect actual page/state khi accessible; không kết luận từ homepage thumbnail.

| Reference | Type | Page/state inspected | Role | Principle | Why it works | Do NOT copy | Project adaptation |
|---|---|---|---|---|---|---|---|

### Page-role reference matrix — bắt buộc

| Project page role | User question | Reference role | Extracted principle | Adaptation |
|---|---|---|---|---|

Nếu mọi page cuối cùng đều map về một “beautiful hero pattern”, benchmark FAIL.

---

# 14. DOMAIN ARTIFACT INTELLIGENCE — CONDITIONAL

Khi domain có objects/documents/spaces/rituals mạnh, research:

`artifact → user familiarity → anatomy → information structure → transferable property → do-not-copy → digital/mobile adaptation`

Fidelity:

`L0 reference | L1 cue | L2 structural | L3 direct form | L4 immersive`

Use lowest useful fidelity.

Không tạo metaphor theme park.

---

# 15. DESIGN DNA

Synthesize:

`brand truth + user mental model + reference principles + domain artifacts + content/media reality`.

Define:

- 4–7 concrete visual attributes;
- layout grammar;
- typography hierarchy;
- semantic color roles;
- imagery/media direction;
- border/radius/elevation language;
- motion purpose;
- 1–3 visual signatures;
- anti-patterns.

### Logo-hidden recognition test

Nếu che logo/brand name mà site có thể là bất kỳ competitor/template nào → FAIL.

Không sửa bằng cách rải primary color; sửa grammar/signature.

---

# 16. PAGE-ROLE COMPOSITION MATRIX — HARD GATE

Artifact bắt buộc:

| Page role | User question | Owner message | First visual anchor | Top composition | Decision object | CTA | Mobile transformation |
|---|---|---|---|---|---|---|---|

### Diversity rule

- Hero không phải universal component để copy rồi thay title/image.
- Materially different page jobs phải được cân nhắc first visual anchor khác nhau.
- Site có 5+ primary page roles: mặc định cần **≥3 top-of-page composition families**, trừ khi documented rationale chứng minh repetition là intentional.
- Utility pages có thể share family.

### Swap test

Nếu có thể đổi copy + image giữa 3 primary page screenshots/wireframes mà layout vẫn “hợp”, direction quá generic → FAIL.

---

# 17. REPRESENTATIVE COMPOSITION PROOFS

Trước Prompt 2, tạo ít nhất 3 proof-of-concept cho materially different primary roles.

Có thể là:

- wireframe text diagram;
- layout sketch;
- visual mock/reference montage;
- coded spike **chỉ nếu Prompt 1 execution environment cho phép visual exploration, không sửa production source**.

Mỗi proof phải thể hiện:

- hierarchy;
- first visual anchor;
- brand signature;
- decision object;
- CTA timing;
- mobile transformation.

Không rollout 15 page rồi mới phát hiện hero giống nhau.

---

# 18. VISIBLE REDESIGN DELTA

Cho redesign, tạo:

| Current visible problem | New behavior | Why it matters | Expected visible delta | Verification |
|---|---|---|---|---|

Substantial redesign phải nhìn before/after ở cùng viewport và nhận ra thay đổi ở **hierarchy/composition/journey/brand expression**, không chỉ màu/font/spacing.

Novelty không được phá preserve list.

---

# 19. RESPONSIVE / ACCESSIBILITY / PERFORMANCE / SEO

Responsive: desktop/tablet/mobile là intentional compositions.

Accessibility baseline: semantic headings, keyboard, focus, contrast, labels/errors, touch, alt, reduced motion, reflow.

Performance: hero/media/font/third-party budget theo project.

SEO redesign: URL preservation/redirect/canonical/sitemap/hreflang/schema trước migration.

---

# 20. SYSTEM REALITY

Feature labels:

`REAL | STATIC | MOCK | SIMULATED | PARTIAL | UNKNOWN`

Không coi:

`form UI = backend`, `search box = search engine`, `booking CTA = booking system`, `availability card = live inventory`.

CTA/copy phải phản ánh capability thật.

---

# 21. DESIGN CONTRACT — FINAL OUTPUT OF PROMPT 1

Tạo `docs/DESIGN-CONTRACT.md` hoặc equivalent.

```text
PROJECT TRUTH
BUSINESS GOAL / PRIMARY CONVERSION
PRIMARY AUDIENCES / ENTRY CONTEXTS / TOP TASKS
OWNER ↔ USER INTERSECTION
PRIMARY JOURNEY
SITEMAP + PAGE ROLES
PRESERVE / CHANGE / REMOVE / ADD
BRAND SOURCE STATUS + EVIDENCE
SEMANTIC COLOR ROLES
TYPOGRAPHY / MEDIA / SHAPE / MOTION
REFERENCE FINALISTS + PAGE-ROLE MATRIX
DOMAIN ARTIFACT PRINCIPLES (if applicable)
DESIGN DNA / VISUAL SIGNATURES
PAGE-ROLE COMPOSITION MATRIX
REPRESENTATIVE COMPOSITION PROOFS
MOBILE TRANSFORMATION RULES
SYSTEM REALITY
VISIBLE REDESIGN DELTA
DO / DO NOT
IMPLEMENTATION RISKS
VISUAL ACCEPTANCE CONDITIONS
```

---

# 22. VISUAL ACCEPTANCE CONDITIONS FOR PROMPT 2/3

Design Contract phải định nghĩa trước ít nhất:

- what must be visibly different from current site;
- what must remain recognizable from brand;
- required composition families;
- page roles that must NOT share hero;
- logo/nav/CTA state expectations;
- decision objects that must be visible above/before conversion;
- mobile-specific transformations;
- what counts as generic/template failure.

---

# 23. QUALITY GATE

Research chỉ PASS khi:

- [ ] Business model/goal/conversion hiểu rõ.
- [ ] Primary audience + top tasks + entry contexts rõ.
- [ ] Owner ↔ user intersection rõ.
- [ ] Primary journey + page roles rõ.
- [ ] Preserve list có nếu redesign.
- [ ] Brand source status/evidence rõ; logo fallback không fabricate.
- [ ] Semantic color roles rõ, không chỉ palette.
- [ ] Competitor/reference research theo actual page roles.
- [ ] Design DNA không generic adjective.
- [ ] Có page-role composition matrix.
- [ ] Có ≥3 representative composition proofs cho substantial multi-page redesign.
- [ ] Có cross-page monotony/swap test.
- [ ] Có mobile strategy.
- [ ] Có system reality.
- [ ] Có Visible Redesign Delta.
- [ ] Có final Design Contract đủ để Prompt 2 code mà không tự sáng tác lại direction.

Nếu bất kỳ hard gate material nào FAIL → chưa chuyển Prompt 2.

---

# FINAL PRINCIPLE

> **Prompt 1 không tồn tại để viết một research report dài. Nó tồn tại để loại bỏ ambiguity trước code.**
>
> Nếu Prompt 2 vẫn có thể chọn tùy ý hero, palette, page composition hoặc visual style sau khi đọc Prompt 1, thì Prompt 1 chưa hoàn thành nhiệm vụ.
