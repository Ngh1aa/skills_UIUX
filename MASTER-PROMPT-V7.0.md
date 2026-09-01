# MASTER PROMPT V7.0 — STRUCTURAL REDESIGN IMPLEMENTATION OS
## V6.0 + OLD→NEW VISUAL PROOF BEFORE SCALE

> Kế nhiệm `MASTER-PROMPT-V6.0.md`. Đọc và thực thi toàn bộ V6.0 trước; file này bổ sung/override các hard gate chống cosmetic-only redesign.

Route bắt buộc cho substantial redesign:

```text
visual-redesign-delta-gate
```

## 1. BEFORE FIRST CODE CHANGE

Đọc từ Design Contract:

- old rendered baseline;
- Redesign Delta Contract;
- representative composition proofs;
- old→new viewport matrix;
- preserve list;
- page-role composition matrix.

Nếu thiếu old baseline trong khi existing site có thể render → capture trước code.

## 2. STRUCTURAL OWNER FIRST

Không bắt đầu bằng đổi token/palette/font.

Thứ tự implementation mặc định:

```text
page structure / composition owner
→ information hierarchy
→ media treatment / crop / density
→ decision-object placement
→ responsive transformation
→ shared system/tokens
→ craft/polish
```

Token-first chỉ đúng khi token là root cause; nó không được dùng để giả substantial redesign.

## 3. REPRESENTATIVE PAGES MUST LOOK STRUCTURALLY DIFFERENT

Implement 2–4 materially different roles trước.

Tạo OLD vs NEW screenshots cùng viewport.

Review contact sheet và chạy silhouette test:

- blur/ignore text;
- ignore brand color;
- ignore image subject;
- compare blocks, proportions, anchor, hierarchy, rhythm.

Nếu new vẫn giống old và thay đổi chủ yếu là surface → **DO NOT SCALE**.

## 4. EXPLICIT COSMETIC-ONLY FAIL LIST

Substantial redesign FAIL nếu phần lớn delta là:

- dark → white hoặc white → dark;
- new font pairing;
- spacing rộng hơn;
- new button/radius/shadow;
- glass/gradient;
- scroll animation;
- image replacement trong cùng crop/layout;
- same hero shell with new copy;
- same card grid with new styling.

Các thay đổi trên có thể tồn tại, nhưng phải đi cùng structural delta.

## 5. PAGE-ROLE DIVERSITY GATE

Với 5+ primary roles, representative implementation phải chứng minh ≥3 composition families.

Check:

- Home/brand orientation có thể campaign/editorial/orientation-led;
- listing/search phải utility/catalogue-led;
- detail/spec/PDP phải decision-object-led;
- conversion/checkout phải distraction-reduced;
- trust/service/about có evidence/story structure riêng.

Không copy một shell vì code reuse thuận tiện.

## 6. FULL-SITE ROLLOUT GATE

Không rollout nếu chưa có matrix:

| Route | Old screenshot | New screenshot | Structural delta | User/business reason | Result |
|---|---|---|---|---|---|

Representative set phải PASS trước.

Khi rollout, map **mọi primary route** vào page family. Không để 4 trang demo đẹp còn các trang khác giữ style/layout legacy vô chủ.

## 7. WHOLE-SITE COVERAGE

Sau representative pass, audit toàn bộ sitemap:

```text
REDESIGNED / FAMILY-ALIGNED / UTILITY-ALIGNED / INTENTIONALLY-PRESERVED / BLOCKED
```

Báo cáo route nào chưa nhận design system mới. Không gọi whole-site redesign nếu primary routes còn legacy composition không có rationale.

## 8. MOBILE STRUCTURAL DELTA

Mobile không được chỉ là `grid-template-columns: 1fr`.

Bắt buộc review:

- order of information;
- media dominance;
- sticky purchase/filter/navigation behavior;
- content reduction vs preservation;
- typography scale/rhythm;
- task-specific first screen.

Ít nhất một representative role phải có mobile composition materially khác desktop.

## 9. VISUAL QA DURING IMPLEMENTATION

Loop:

```text
implement structural owner
→ render old/new pair
→ contact sheet
→ silhouette check
→ fix macro hierarchy
→ then polish micro craft
```

Không đợi Prompt 3 mới phát hiện "vẫn giống bản cũ".

## 10. USER FEEDBACK REGRESSION

Nếu user nói `website vẫn y như cũ`, `chỉ đổi màu`, hoặc tương đương:

- treat as process P1;
- stop cosmetic fixes;
- open old/new evidence;
- identify unchanged structural owner;
- redesign that owner;
- add regression assertion/eval before continuing.

## 11. RELEASE CONDITION

Không merge/deploy substantial redesign nếu:

- old/new same-viewport evidence chưa có;
- silhouette gate chưa PASS;
- ≥3 page-role composition families chưa chứng minh khi scope yêu cầu;
- whole-site route coverage chưa audit;
- mobile delta chưa inspect;
- final visual regression chưa chạy.

## FINAL PRINCIPLE

> **Implementation success = contract compliance + structural old→new delta + rendered proof. Number of changed files/lines is irrelevant.**
