# FINAL UI/UX / VISUAL / CONTENT QA & REMEDIATION V2.0
## RENDER → COMPARE → FIND MACRO ISSUES → FIX ROOT OWNER → RE-RENDER → HANDOFF ONLY WHEN VISUAL EVIDENCE PASSES

> **V2.0 purpose:** Prompt 3 không được bắt đầu bằng code grep/checklist. Nó phải bắt đầu bằng **rendered evidence** và so với Design Contract/visual target.
>
> **Failure this version prevents:** CI xanh nhưng logo mất, CTA chìm, hero mọi page giống nhau, mobile chỉ stack desktop, visual vẫn generic nhưng report lại nói “PASS”.

---

# 0. REQUIRED INPUTS

```yaml
website_url_or_local_render: [...]
source_repo: [...]
design_contract: [...]
brand_guideline_or_fallback: [...]
reference_benchmark_if_used: [...]
primary_routes: [...]
supported_viewports/browsers: [...]
```

Nếu không có actual rendered implementation để inspect:

> `FINAL VISUAL QA = BLOCKED / UNVERIFIED`

Không được dùng source/build/CI làm visual substitute.

---

# 1. SKILL ROUTING

Ưu tiên:

```text
ui-craft-and-visual-qa
visual-regression-and-design-drift
brand-recognition-and-consistency-qa
ui-improvement
design-system-and-components
responsive-and-device-strategy
accessibility
interaction-patterns-and-form-ux
state-feedback-and-error-recovery
content-design-and-question-design
conversion-and-content
```

Khi phát hiện **design direction itself** sai contract, route lại `visual-design-direction`; không cố polish một direction sai.

---

# 2. SOURCE OF VISUAL TRUTH

QA phải so actual render với:

1. Design Contract;
2. approved/selected visual direction or representative page proof;
3. brand rules;
4. page-role composition matrix;
5. responsive rules;
6. system reality/content truth.

Website cũ chỉ là baseline/preserve evidence, **không phải target visual** nếu đã redesign.

---

# 3. CAPTURE FIRST — HARD GATE

Trước findings, capture/open actual rendered UI.

Cho substantial multi-page site, tối thiểu khi feasible:

- primary route tops ở desktop;
- primary route tops ở mobile;
- representative full-page captures;
- header top/scrolled/mobile states;
- critical CTA/form/search/filter states;
- intermediate width cho layout risk.

Recommended viewport set khi không có project-specific matrix:

`375 | 390/430 | 768 | 1024 | 1280/1440 | 1920`.

Không cần mọi page ở mọi width nếu scope lớn; dùng risk-based representative matrix nhưng phải cover all primary page families.

---

# 4. CROSS-PAGE CONTACT SHEET — BẮT BUỘC

Đặt top-of-page screenshots của primary page roles cạnh nhau.

Audit trước micro details:

1. Page purpose có đọc được ngay không?
2. First visual anchor có khác theo task không?
3. Có universal hero/template monotony không?
4. Có page nào đáng lẽ dùng map/plan/data/evidence/form nhưng lại dùng generic image banner không?
5. Brand signature có coherent xuyên site không?
6. Trang có khác nhau đủ để hiểu role nhưng vẫn cùng một system không?

Với 5+ materially different primary roles, nếu gần như toàn bộ cùng một top composition family mà không có documented rationale → **P1**.

---

# 5. 5-SECOND FIRST-IMPRESSION TEST

Với từng primary page, trong 5 giây phải trả lời được:

- Đây là page về việc gì?
- Thứ quan trọng nhất là gì?
- CTA/next step là gì?
- Visual này có thuộc brand/domain này không?
- Page role này khác page role khác ở đâu ngoài copy/image?

Nếu fail → sửa hierarchy/composition trước typography micro-polish.

---

# 6. BRAND RECOGNITION TEST

Che logo/brand name trong đánh giá.

Kiểm:

- color roles;
- typography;
- imagery;
- grid/composition;
- graphic/wayfinding motif;
- shape/border language;
- motion.

Nếu site có thể đổi logo sang competitor khác mà không thấy sai → P1 brand/visual-direction issue.

Không fix bằng cách rải primary color nhiều hơn.

---

# 7. HEADER / LOGO / CTA STATE MATRIX

Render/inspect:

| State | Logo | Nav text | Active state | Primary CTA | Result |
|---|---|---|---|---|---|
| top | ... | ... | ... | ... | ... |
| scrolled | ... | ... | ... | ... | ... |
| mobile menu | ... | ... | ... | ... | ... |
| dark/light context | ... | ... | ... | ... | ... |

White-on-white, dark-on-dark, invisible CTA text, broken sticky state → P0/P1 tùy impact.

---

# 8. MACRO-TO-MICRO REVIEW ORDER

Không bắt đầu bằng shadow/radius.

1. User/page purpose.
2. Cross-page composition diversity.
3. Hierarchy / first visual anchor.
4. Brand recognition.
5. Journey / CTA timing.
6. Section rhythm / density.
7. Grid / alignment.
8. Typography / readability.
9. Color / contrast.
10. Components / states.
11. Imagery / iconography.
12. Motion / micro-details.

Không dành thời gian P2 khi P1 composition còn sai.

---

# 9. TYPOGRAPHY QA

Kiểm actual render:

- font loading/fallback;
- heading/body/action hierarchy;
- nav/button/meta minimum readability;
- Vietnamese/locale diacritics;
- line height;
- line length;
- letter spacing;
- mobile wrapping;
- text trên image/dark/light surface.

Text phải đọc được, không chỉ tồn tại trong DOM.

---

# 10. COLOR / CONTRAST / SURFACE QA

Kiểm:

- text/background actual states;
- logo contexts;
- button text/icon default/hover/focus;
- muted/meta text;
- borders/dividers;
- image overlay;
- semantic state colors;
- surface rhythm.

Subtle ≠ invisible.

Primary color phải có role; không dùng như decoration tràn lan.

---

# 11. PAGE DIVERSITY / TEMPLATE QA

Flag patterns vô lý:

- mọi page `large heading + copy left + image right`;
- mọi page full-bleed hero chỉ thay ảnh;
- mọi section heading + 3 cards;
- every page same section count/rhythm;
- same CTA block everywhere regardless decision context;
- domain-native decision object luôn bị đẩy xuống dưới photography.

Nguyên tắc:

> Consistency through system. Diversity through composition.

---

# 12. LAYOUT / SPACING / DESIGN SYSTEM

Check:

- container widths;
- alignment axes;
- vertical rhythm;
- spacing scale;
- button variants;
- card semantics;
- radii/borders;
- image ratios;
- icon sizes;
- section surface logic.

Fix shared owner/token/component trước page-specific patch.

Không tạo thêm `final-fix.css` nếu root cause là architecture/design-system ownership.

---

# 13. CONTENT / UX WRITING

Audit menu, heading, CTA, label, helper/error/success, footer.

Fix:

- vague corporate buzzword;
- generic CTA;
- random language mixing;
- misleading capability wording;
- internal terminology user không hiểu;
- copy không match destination.

CTA phải cho user đoán được click xong chuyện gì xảy ra.

---

# 14. USER JOURNEY / DEAD-END QA

Với từng primary page:

- entry orientation;
- current location;
- evidence before decision;
- primary/secondary CTA hierarchy;
- end-of-page next step;
- deep-link path;
- mobile contact/conversion.

Không ép conversion trước proof.

---

# 15. SYSTEM REALITY QA

So copy/state với capability:

`REAL | STATIC | MOCK | SIMULATED | PARTIAL | UNKNOWN`.

Catch:

- fake success;
- fake live availability;
- fake booking;
- fake pricing;
- fake search/filter;
- analytics naming nói “submit” khi chỉ prepare/open email.

Trust defect = P1/P0 tùy impact.

---

# 16. RESPONSIVE QA

Mobile/tablet không phải desktop stack.

Check:

- reading order;
- hero height;
- page-specific composition transform;
- nav;
- title/button wrapping;
- sticky/fixed overlap;
- safe area;
- maps/plans/tables;
- image crop;
- touch targets;
- horizontal scroll;
- whitespace/density.

Intermediate widths bắt buộc khi layout có pressure.

---

# 17. ACCESSIBILITY / INTERACTION QA

Baseline:

- keyboard;
- focus-visible;
- labels/names;
- headings/landmarks;
- contrast;
- error/recovery;
- no color-only meaning;
- reduced motion;
- zoom/reflow/touch.

Interaction states:

`default | hover | focus | active/selected | expanded | disabled | loading | error/success` khi applicable.

Không claim formal WCAG conformance nếu chưa evaluation tương xứng.

---

# 18. IMAGE / MEDIA / MOTION QA

Media:

- đúng subject/property/product;
- resolution;
- crop/focal point;
- no generic filler;
- overlay không phá ảnh/text;
- image supports message.

Motion:

- purpose;
- consistency;
- duration/easing;
- no excessive fade-up;
- no lag;
- reduced-motion behavior.

---

# 19. ISSUE MODEL

Mỗi issue:

```text
ID
Severity: P0/P1/P2/P3
Location/route/state/viewport
Visible evidence
Expected contract/design behavior
Actual behavior
User/business/brand impact
Root owner
Fix
Verification
```

Severity:

- P0 — task impossible / unreadable critical content / broken nav-conversion / severe accessibility.
- P1 — major hierarchy, brand, trust, composition, responsive or usability defect noticeable to users.
- P2 — craft/polish drift.
- P3 — preference/optional.

---

# 20. AUTONOMOUS FIX LOOP

Không chỉ report.

```text
capture
→ macro audit
→ log P0/P1/P2
→ fix P0
→ fix P1
→ fix high-confidence P2
→ rebuild
→ re-render same viewports/states
→ compare before/after
→ check cross-page regression
→ repeat
```

Không dừng sau source fix nếu actual pixels chưa verify.

---

# 21. BEFORE / AFTER EVIDENCE

Mỗi material P0/P1 fix cần:

- before evidence;
- owning change;
- after rendered evidence;
- pass/fail.

Nếu screenshot/capture không inspect được, issue không được gọi fixed visually.

---

# 22. USER-FEEDBACK DEBT RULE

Nếu stakeholder/user phải chỉ ra lỗi obvious mà QA đáng lẽ phải thấy:

1. ghi issue là process miss;
2. fix project;
3. xác định skill/prompt/checklist nào fail;
4. thêm regression test/eval;
5. không để class lỗi đó lặp lại ở project khác.

Ví dụ:

- logo biến mất khi scroll;
- CTA text invisible;
- mọi hero giống nhau;
- mobile broken;
- brand generic;
- fake live state.

---

# 23. NO-OVER-REDESIGN BOUNDARY

Prompt 3 là remediation, không tự đổi direction nếu Design Contract đúng.

Ưu tiên:

`correct → clarify → normalize → refine`.

Chỉ route lại visual direction khi evidence cho thấy implementation đang bám một contract/direction sai hoặc contract không đủ.

---

# 24. FINAL HANDOFF GATE

`FINAL RESULT = PASSED` chỉ khi:

- [ ] actual rendered UI đã inspect;
- [ ] no actionable P0/P1/P2 material mismatch within tested scope;
- [ ] cross-page composition không generic/template monotony vô lý;
- [ ] page purposes/hierarchy rõ trong first impression;
- [ ] brand recognition đạt contract;
- [ ] logo/nav/CTA states readable;
- [ ] mobile representative compositions usable;
- [ ] key interactions/states usable;
- [ ] wording/system reality truthful;
- [ ] fixes có after evidence;
- [ ] limitations/test gaps được ghi rõ.

Nếu rendered evidence không available hoặc P0/P1/P2 còn actionable:

`FINAL RESULT = BLOCKED`.

Không dùng `PARTIAL PASS` để greenwash blocker.

---

# 25. FINAL REPORT — NGẮN

```text
FINAL RESULT: PASSED | BLOCKED

P0 fixed
P1 fixed
Visual/composition fixes
Brand/logo/color fixes
UX/journey fixes
Typography/content fixes
Responsive/accessibility fixes
What intentionally stayed unchanged
Verification evidence
Remaining blockers / unverified scope
Regression tests added from process misses
```

Ưu tiên:

> **FIX WEBSITE > EXPLAIN WEBSITE**

---

# FINAL SELF-CRITIQUE

Trước handoff hỏi:

1. Có lỗi nào người dùng nhìn 5 giây là thấy mà mình đang bỏ qua không?
2. Có page nào chỉ là clone template đổi content không?
3. Logo/nav/CTA có state nào biến mất không?
4. Nếu che logo, site có ownable không?
5. Mobile có thật sự designed không?
6. Có fake capability/trust state không?
7. Có đang gọi build/CI là visual QA không?
8. Có P2 micro polish đang che P1 macro defect không?
9. Có user feedback nào trước đây chưa được biến thành regression gate không?

Nếu CÓ → tiếp tục sửa hoặc BLOCKED. Không handoff như đã hoàn tất.
