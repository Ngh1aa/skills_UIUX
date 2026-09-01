# MASTER PRE-DESIGN RESEARCH PROMPT V4.0
## V3.0 + MANDATORY OLD→NEW REDESIGN DELTA GATE

> Đây là phiên bản kế nhiệm `MASTER-PRE-DESIGN-RESEARCH-PROMPT-V3.0.md`.
> Trước khi thực thi, **đọc toàn bộ V3.0** và giữ nguyên mọi yêu cầu không bị override trong file này.

## Failure mode bắt buộc phải chặn

Không được tạo Design Contract dẫn tới kết quả: **code thay nhiều nhưng website nhìn vẫn như cũ ngoài màu/font/spacing**.

Route bắt buộc thêm:

```text
visual-redesign-delta-gate
```

## 1. OLD RENDERED BASELINE — HARD GATE

Nếu là redesign existing website và tooling cho phép render:

- capture current Home + 3–6 representative primary page roles;
- desktop + mobile;
- cùng viewport sẽ dùng để verify bản mới;
- ít nhất top-of-page + full/long screenshot khi relevant.

Source/code audit không thay screenshot baseline.

Tạo:

| Route/role | Viewport | Current silhouette | First visual anchor | Section rhythm | Decision object | Template smell |
|---|---:|---|---|---|---|---|

Nếu không capture được, ghi `OLD VISUAL BASELINE: BLOCKED/UNVERIFIED` và không được claim future visual delta là verified.

## 2. REFERENCE RESEARCH PHẢI TẠO STRUCTURAL DECISION

Research theo page role, ưu tiên production/category sites cho UX/task và curated/editorial sources cho craft.

Mỗi reference finalist phải trả lời:

- page/state nào đã inspect;
- principle nào transfer được;
- current-site problem nào principle đó giải quyết;
- nó tạo **structural delta** gì trong project;
- do-not-copy;
- mobile/performance/accessibility adaptation.

Nếu benchmark chỉ kết thúc bằng `minimal / premium / clean / editorial / glass / modern` mà không đổi composition → **REFERENCE FAIL**.

## 3. REDESIGN DELTA CONTRACT — BẮT BUỘC TRONG DESIGN CONTRACT

Thêm section:

| Page role | Current recognizable structure | New intended structure | What must visibly disappear/change | New visual anchor | Mobile transformation | Verification |
|---|---|---|---|---|---|---|

Structural delta hợp lệ gồm:

- first visual anchor;
- top-of-page composition;
- grid/silhouette;
- information hierarchy;
- media-copy relationship;
- decision-object placement;
- section order/rhythm;
- navigation/orientation;
- mobile composition;
- materially visible interaction model.

Không tính riêng lẻ: color, font, radius, shadow, spacing, gradient, glass, animation polish.

## 4. SILHOUETTE TEST — PRE-CODE FAIL CONDITION

Với 3 representative composition proofs, tưởng tượng bỏ:

- logo/brand name;
- text cụ thể;
- color;
- photo content (chỉ giữ gray blocks).

Nếu proof mới vẫn gần giống current screenshot về silhouette/hierarchy → **RESEARCH FAIL**.

## 5. COMPOSITION DIVERSITY MINIMUM

Với site có 5+ materially different primary roles:

- mặc định ≥3 top-of-page composition families;
- ≥3 materially different representative silhouettes;
- ít nhất 2 primary roles phải thay structural hierarchy so với current site;
- mobile có intentional re-composition, không chỉ stack desktop.

Repetition mạnh chỉ được giữ khi có documented brand/task rationale.

## 6. DESIGN CONTRACT ADDITIONS

`docs/DESIGN-CONTRACT.md` phải thêm:

```text
OLD RENDERED BASELINE
OLD TEMPLATE / SILHOUETTE SMELLS
REDESIGN DELTA CONTRACT
OLD→NEW REPRESENTATIVE COMPOSITION PROOFS
SILHOUETTE TEST RESULT
STRUCTURAL DELTA ACCEPTANCE CONDITIONS
OLD→NEW VIEWPORT MATRIX FOR PROMPT 2/3
```

## 7. HANDOFF CONDITION

Không chuyển Prompt 2 nếu chưa trả lời được:

1. Người dùng sẽ nhận ra bản mới khác bản cũ ở **cấu trúc nào** trong 3 giây đầu?
2. Sự khác đó phục vụ owner goal/user task nào?
3. Page roles nào có top composition khác nhau và vì sao?
4. Mobile thay đổi composition ra sao?
5. Old-vs-new sẽ được verify ở viewport nào?

> **Nếu câu trả lời chủ yếu là palette/type/spacing/effect → không được code.**
