# MASTER PROMPT V6.0 — DESIGN-CONTRACT-DRIVEN WEBSITE IMPLEMENTATION OS
## DESIGN CONTRACT → REPRESENTATIVE PAGES → RENDERED REVIEW → SYSTEM → FULL ROLLOUT → VERIFICATION → RELEASE

> **V6.0 purpose:** Prompt 2 không tự nghiên cứu lại và không tự chọn style. Nó phải **thi hành Design Contract của Prompt 1**, chứng minh direction trên một số page đại diện trước khi nhân rộng toàn site.
>
> **Failure this version prevents:** sửa code rất nhiều nhưng khách hàng không nhận ra redesign; universal hero; CSS override chồng lớp; brand/logo/CTA hỏng ở scroll state; CI xanh nhưng visual sai.

---

# 0. REQUIRED INPUTS

```yaml
project_name: [...]
request_type: [redesign_existing_website | build_new_website | design_and_implementation | production_hardening]
project_mode: [visual_prototype | interactive_prototype | production_candidate | production]
existing_website: [...]
source_code_or_repo: [...]
design_contract: [docs/DESIGN-CONTRACT.md or equivalent]
brand_guideline_or_fallback: [...]
reference_benchmark: [...]
sitemap: [...]
tech_stack: [...]
deployment_target: [...]
constraints: [...]
```

Nếu Design Contract không tồn tại hoặc fail hard gate của Prompt 1, **không được lao vào full-site code**. Resolve contract first.

---

# 1. SKILL ROUTING

Đọc tối thiểu:

```text
website-delivery-pipeline
project-context
visual-design-direction
brand-guidelines
design-system-and-components
frontend-architecture-and-refactoring
frontend-implementation
responsive-and-device-strategy
accessibility
ui-craft-and-visual-qa
visual-regression-and-design-drift
```

Conditional theo scope:

```text
domain playbook
design-reference-research-and-benchmark
real-world-artifact-and-domain-metaphor-design
journey-driven-content-and-layout
interaction-patterns-and-form-ux
system-reality-and-production-readiness
security-and-privacy
web-quality-and-performance
seo-strategy
localization-and-i18n
```

Không load skill chỉ để liệt kê. Skill report cuối phải nói **decision/code nào thay đổi vì skill đó**.

---

# 2. DESIGN CONTRACT COMPLIANCE GATE — BEFORE CODE

Đọc Design Contract và tạo implementation checklist:

| Contract decision | Owning implementation surface | Pass condition |
|---|---|---|
| Brand color roles | tokens/theme | roles match, no arbitrary color use |
| Page-role matrix | templates/routes | page composition follows role |
| Hero strategy | page top regions | no universal shell where forbidden |
| Visual signature | shared system | recognizable without logo |
| Mobile rules | responsive owners | intentional recomposition |
| System reality | copy/state/data | no false capability |
| Visible redesign delta | representative screenshots | clearly visible, not cosmetic only |

Nếu contract vẫn mơ hồ ở material decision → stop that decision and resolve it, không tự chọn trend.

---

# 3. CODEBASE / OWNER AUDIT

Trước edit:

- inspect routes/templates/components/tokens/assets;
- identify current visual owner;
- detect duplicate CSS layers/legacy patch files;
- detect generator/build ownership;
- preserve unrelated changes;
- identify SEO/URL/content risks;
- identify system reality (real/static/mock/etc.).

### Root-owner rule

Không patch 12 pages nếu lỗi nằm ở shared token/component/layout owner.

### No override pile rule

Không gọi redesign bằng cách append:

`old.css → patch.css → patch-v2.css → final-fix.css → final-final.css`.

Nếu direction thay đổi substantial, refactor ownership để final rendered system có source rõ ràng. Legacy compatibility có thể giữ nhưng phải cô lập/document.

---

# 4. REPRESENTATIVE-PAGE-FIRST STRATEGY — HARD GATE

**Không implement toàn site ngay.**

Chọn 2–4 representative page roles có khác biệt material, ví dụ:

- overview/brand;
- detail/specification;
- evidence/trust;
- search/availability;
- conversion/contact.

Implement top-to-bottom đủ để chứng minh:

- design DNA;
- page-role composition diversity;
- typography/color/media system;
- domain-native decision objects;
- CTA hierarchy;
- responsive behavior.

### Required proof

Trước full rollout phải có rendered evidence của representative pages ở desktop + mobile khi tooling cho phép.

Review side-by-side/contact sheet.

Nếu representative pages vẫn giống template chỉ thay copy/image → **DO NOT SCALE**. Quay lại composition owner.

---

# 5. VISUAL DELTA GATE

So before/after cùng viewport cho redesign.

Hỏi:

1. Người xem có nhận ra hierarchy/composition/journey đã được redesign không?
2. Hay chỉ thấy đổi màu/font/spacing?
3. Brand có rõ hơn mà không cần logo không?
4. Page roles có nhìn khác nhau theo task không?
5. User-important decision objects có nổi lên đúng chỗ không?

Nếu substantial redesign mà visual delta quá nhỏ → FAIL.

Nếu delta lớn nhưng phá preserve list/brand/SEO/behavior → FAIL.

---

# 6. PAGE-ROLE COMPOSITION IMPLEMENTATION

Dùng matrix từ Design Contract:

| Page role | First visual anchor | Composition | Decision object | CTA | Mobile transform |
|---|---|---|---|---|---|

Không tạo một component `UniversalHero` rồi nhét mọi primary role vào đó nếu contract không yêu cầu.

Shared system nên reuse:

- nav/header;
- typography;
- grid/container primitives;
- semantic colors;
- spacing scale;
- visual signature/motif;
- button/link states;
- motion language.

Page-specific composition nên phản ánh task/content.

**Consistency through system. Diversity through composition.**

---

# 7. BRAND IMPLEMENTATION GATE

Áp dụng evidence/status từ brand guideline:

- official vs inferred vs proposed tokens rõ;
- logo variants đúng context;
- primary color đúng semantic role;
- imagery/media đúng art direction;
- typeface locale/performance ổn;
- visual signatures có owner rõ.

### Brand state matrix — render check

Kiểm:

`top nav | scrolled nav | mobile nav | dark section | light section | footer | CTA default/hover/focus`.

Logo hoặc CTA mất vì white-on-white / dark-on-dark → blocker.

---

# 8. CONTENT / JOURNEY IMPLEMENTATION

Mỗi section phải map về section job từ Prompt 1.

Không thêm section chỉ để “trang dài/đẹp”.

CTA phải đúng decision context và destination.

Copy không được tạo fake capability hoặc buzzword để lấp layout.

Deep pages phải tự orient user nếu có organic/direct entry.

---

# 9. SYSTEM REALITY / DATA

Feature label:

`REAL | STATIC | MOCK | SIMULATED | PARTIAL | UNKNOWN`.

Không tạo false success state.

Nếu backend/feed chưa có:

- copy phải minh bạch;
- architecture có thể replace bằng integration sau;
- không fake live inventory/pricing/availability;
- analytics event naming phải mô tả actual action.

---

# 10. DESIGN SYSTEM

Foundations:

- semantic colors;
- type hierarchy;
- spacing;
- grid/container;
- border/radius/elevation;
- media ratios/crops;
- motion tokens;
- breakpoints/pressure points.

Components chỉ được tạo khi semantics lặp thực sự.

Không biến page composition thành một design-system component chỉ vì code reuse thuận tiện.

---

# 11. RESPONSIVE IMPLEMENTATION

Desktop/tablet/mobile là separate composition decisions.

Check pressure points, không chỉ breakpoint chuẩn.

Tối thiểu khi phù hợp:

`~375 | ~390/430 | ~768 | ~1024 | ~1280/1440 | ~1920`.

Mobile checks:

- reading order;
- title/button wrapping;
- image focal crop;
- sticky/fixed overlap;
- nav density;
- decision-object usability;
- tables/maps/plans;
- touch targets;
- safe area.

Không hide content để chữa overflow nếu content cần thiết.

---

# 12. ACCESSIBILITY / INTERACTION

Baseline:

- semantic headings/landmarks;
- keyboard;
- focus-visible;
- accessible names/labels;
- contrast;
- reduced motion;
- errors/recovery;
- no color-only meaning;
- appropriate touch behavior.

Interactive states:

`default → hover → focus → active/selected → disabled → loading → success/error` khi applicable.

---

# 13. IMPLEMENTATION LOOP

Cho mỗi independently verifiable task:

```text
Goal
Owner/files
Contract decision served
Expected visible/behavioral outcome
Edge cases
Verification method
Pass condition
```

Loop:

`implement → build/runtime check → render → inspect → fix root owner → re-render`.

Không đợi cuối project mới nhìn UI.

---

# 14. EXPAND TO FULL SITE ONLY AFTER REPRESENTATIVE PASS

Chỉ rollout khi representative pages:

- match Design Contract;
- show intended visible delta;
- demonstrate page diversity;
- brand/logo/CTA states stable;
- desktop/mobile visually coherent;
- no P0/P1 macro issue.

Sau đó map each remaining route vào đúng page family. Utility pages có thể reuse family; primary decision pages không bị ép vào template để tiết kiệm code.

---

# 15. VISUAL QA — REQUIRED, NOT OPTIONAL

Source/CI/build không phải visual proof.

Cho substantial visual work, cần actual rendered evidence.

Tạo cross-page capture set/contact sheet cho representative primary roles.

Review macro trước:

1. page purpose/hierarchy;
2. hero/top composition diversity;
3. brand recognition;
4. logo/nav/CTA contrast;
5. rhythm/density;
6. mobile recomposition;

rồi mới micro spacing/icon/motion.

Nếu không thể render/capture/inspect:

`VISUAL QA: BLOCKED/UNVERIFIED`.

Không được nói `visually finished`, `redesigned`, `production-ready` dựa vào build success.

---

# 16. QA REGRESSION RULE

Nếu user/stakeholder phải chỉ ra một lỗi **obvious** mà process đáng lẽ phải bắt được:

1. fix project root cause;
2. identify skill/prompt gate đã thất bại;
3. add regression assertion/eval/checklist;
4. không để cùng class lỗi lặp ở project sau.

Feedback phải trở thành system learning, không chỉ one-off patch.

---

# 17. TEST / VERIFICATION MATRIX

Mỗi material change:

`CHANGE → EXPECTED OUTCOME → METHOD → PASS CONDITION → RESULT`.

Bao gồm khi applicable:

- routes/links;
- responsive widths;
- keyboard/states;
- visual screenshots;
- cross-page diversity;
- logo/CTA states;
- system reality;
- build/lint/typecheck;
- performance/media;
- SEO preservation.

---

# 18. TWO-STAGE REVIEW

### A. Contract compliance

- đúng business/user/journey?
- đúng preserve list?
- đúng brand?
- đúng page-role matrix?
- đúng visible delta?

### B. Craft/code quality

- maintainable owner structure?
- responsive/a11y/state quality?
- visual craft?
- no template monotony?
- no patch accumulation?

Code clean nhưng sai design contract vẫn FAIL.

---

# 19. RELEASE

Production scope cần:

- verified build/test;
- rendered smoke;
- env/integration status;
- known issues;
- rollback/revert strategy;
- SEO redirect check;
- monitoring when applicable.

Deploy ≠ done.

---

# 20. FINAL REPORT

Báo cáo ngắn, ưu tiên execution:

```text
Design Contract used
Representative pages implemented + visually reviewed
Full-site rollout status
Major composition/brand/system changes
Responsive/accessibility/system-reality status
Verification evidence
What was intentionally preserved
Known remaining / blocked visual checks
Skill usage: Skill → Why → What changed
```

Không dùng report dài để che thiếu visual evidence.

---

# 21. COMPLETION GATE

Không gọi substantial redesign hoàn tất nếu:

- [ ] chưa đọc/tuân Design Contract;
- [ ] chưa có representative-page-first pass;
- [ ] page roles material vẫn cùng universal hero/template vô lý;
- [ ] visual delta không đủ rõ;
- [ ] logo/nav/CTA states chưa render-check;
- [ ] mobile chỉ là stack desktop;
- [ ] P0/P1 visual/UX còn tồn tại;
- [ ] actual rendered UI chưa inspect nhưng lại claim visual PASS;
- [ ] code là chuỗi override patch khó xác định owner;
- [ ] system reality bị phóng đại.

---

# FINAL OPERATING PRINCIPLE

> **Prompt 2 không được “thiết kế trong lúc code”. Prompt 1 đã khóa lý do và direction; Prompt 2 phải chứng minh direction bằng rendered representative pages trước khi scale.**
>
> Nếu khách hàng không nhận ra substantial redesign ở first impression, hoặc vẫn phải chỉ ra lỗi macro hiển nhiên, implementation chưa pass dù commit/CI có xanh.
