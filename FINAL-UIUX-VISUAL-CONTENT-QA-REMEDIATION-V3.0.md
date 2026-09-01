# FINAL UI/UX / VISUAL / CONTENT QA & REMEDIATION V3.0
## V2.0 + OLD→NEW REDESIGN DELTA VERIFICATION

> Kế nhiệm `FINAL-UIUX-VISUAL-CONTENT-QA-REMEDIATION-V2.0.md`. Đọc và giữ toàn bộ V2.0; file này bổ sung hard gate để Final QA không vô tình PASS một redesign chỉ thay skin.

Route bắt buộc:

```text
visual-redesign-delta-gate
```

## 1. THREE-WAY VISUAL REVIEW — REQUIRED

Final QA phải review ba quan hệ riêng:

1. **OLD → NEW**: substantial redesign có thật sự khác cấu trúc không?
2. **NEW → DESIGN CONTRACT**: implementation có đúng direction không?
3. **NEW → NEW CROSS-PAGE**: page roles có bị template monotony/brand drift không?

Build/source diff không thay screenshot evidence.

## 2. OLD→NEW SAME-VIEWPORT MATRIX

Tối thiểu representative primary roles ở desktop + mobile:

| Route/role | Viewport | Old evidence | New evidence | Structural delta | Cosmetic-only risk | Result |
|---|---:|---|---|---|---|---|

Structural delta phải xét:

- top composition;
- block silhouette/proportion;
- first visual anchor;
- information hierarchy;
- media/content relationship;
- decision-object/CTA placement;
- section rhythm;
- mobile transformation.

## 3. SILHOUETTE REVIEW

Compare old/new sau khi mentally loại:

- text cụ thể;
- logo;
- brand colors;
- image subject.

Nếu majority representative pages vẫn có cùng silhouette trong substantial redesign → **P1 PROCESS FAILURE**.

Không chữa bằng thêm effect. Quay lại layout/composition owner.

## 4. WHOLE-SITE COVERAGE CHECK

Không chỉ QA 3–4 showcase pages.

Inventory toàn bộ sitemap/page families:

```text
REDESIGNED
FAMILY-ALIGNED
UTILITY-ALIGNED
INTENTIONALLY-PRESERVED
LEGACY/DRIFT
BLOCKED
```

Nếu primary routes vẫn legacy trong khi report nói whole-site redesign → FAIL.

## 5. CROSS-PAGE CONTACT SHEET

Bắt buộc contact sheet/montage representative routes để thấy:

- page-role diversity;
- repeated universal hero;
- same `heading + cards` rhythm;
- media crop monotony;
- inconsistent nav/footer/system;
- legacy pages chưa nhận new design DNA.

Review macro trước micro.

## 6. COSMETIC-ONLY FAILURE CLASSIFICATION

Nếu old/new khác chủ yếu ở:

- màu nền/chữ;
- font;
- radius/shadow;
- spacing;
- image swap cùng layout;
- gradient/glass;
- animation;

thì classify:

`P1 — INSUFFICIENT REDESIGN DELTA`

khi scope là substantial redesign.

## 7. USER-FEEDBACK REGRESSION RULE

Nếu user từng phản hồi `website vẫn như cũ` hoặc `chỉ đổi nền trắng chữ đen`, Final QA phải verify regression trực tiếp:

- lưu finding vào remediation report;
- xác nhận root cause;
- thêm automated/manual regression check;
- không close finding dựa vào code diff.

## 8. REQUIRED REMEDIATION LOOP

```text
old/new evidence
→ macro finding
→ root composition owner
→ fix
→ re-render same viewport
→ compare again
→ only then micro polish
```

## 9. RELEASE / DEPLOYMENT CHECK

Final QA không kết thúc ở branch.

Nếu user yêu cầu cập nhật live site:

- verify target publishing branch/source;
- merge/fast-forward only after gates pass;
- verify deployment run conclusion;
- post-deploy smoke production URL;
- confirm expected visual signature actually appears live.

Branch QA PASS nhưng production chưa nhận commit = **NOT RELEASED**.

## 10. FINAL REPORT MUST SAY

```text
OLD→NEW redesign delta: PASS / FAIL / BLOCKED
Representative routes reviewed
Whole-site route coverage
Cross-page diversity status
Mobile delta status
P0/P1/P2 findings fixed / remaining
Deployment source + deployed commit
Production smoke status
```

Không dùng `PASS` chung chung nếu old→new delta chưa kiểm.

## COMPLETION RULE

Substantial redesign chỉ được gọi hoàn tất khi:

- old/new same-viewport evidence exists;
- silhouette gate passes;
- page-role diversity passes;
- whole-site primary route coverage audited;
- mobile recomposition inspected;
- no unresolved P0/P1 macro issue;
- deployed commit verified on live publishing source when release requested.

> **Prompt 3 không chỉ polish bản mới. Nó phải chứng minh rằng ba prompt đã tạo ra một website mới về cấu trúc trải nghiệm, chứ không phải một skin mới cho website cũ.**
