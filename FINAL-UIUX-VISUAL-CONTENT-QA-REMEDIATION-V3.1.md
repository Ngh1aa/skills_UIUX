# FINAL UI/UX / VISUAL / CONTENT QA & REMEDIATION V3.1
## V3.0 + MEDIA CROP / FOCAL / LAYOUT INTEGRITY BLOCKERS

> Kế nhiệm `FINAL-UIUX-VISUAL-CONTENT-QA-REMEDIATION-V3.0.md`. Đọc và giữ toàn bộ V3.0; file này bổ sung final visual blockers cho crop và layout.

Route bắt buộc cho media-heavy redesign:

```text
visual-redesign-delta-gate
media-crop-and-layout-integrity
```

## 1. ACTUAL SCREENSHOT REVIEW IS REQUIRED

Final QA không được kết luận từ DOM metrics, source hoặc CI alone.

Với mỗi representative route phải mở screenshot thật và inspect bằng mắt ở desktop + mobile khi relevant.

## 2. P1 MEDIA / LAYOUT BLOCKERS

Classify **P1** nếu screenshot có bất kỳ lỗi obvious nào:

- người mẫu bị cắt đầu/mặt ngoài intentional art direction;
- garment/product chính bị crop mất;
- ảnh bị ép thành lát dọc/sliver;
- ảnh bị stretch/squash;
- product text/price/CTA visually detached khỏi ảnh;
- hero title bị clip/overflow vô nghĩa;
- large unexpected blank region do layout/grid bug;
- media biến mất hoặc nằm sai column;
- related/product grid không xác định được item ownership;
- mobile crop dùng desktop rule và phá focal point.

## 3. PAGE-SPECIFIC VISUAL CHECKS

### Home
- hero image/text đều nằm trong intended bounds;
- oversized type không phá first screen;
- product cards image/name/price/CTA thuộc cùng owner;
- editorial crops giữ focal subject.

### Shop / PLP
- consistent catalogue ratio;
- không crop full-body thành torso/leg slice tùy tiện;
- product metadata nằm đúng card;
- filter/sort không làm grid lệch.

### PDP
- main image cho thấy sản phẩm đủ để ra quyết định;
- head/garment không bị accidental crop;
- thumbnail nhận diện được;
- purchase panel không bị đẩy lệch bởi image height.

### Collection / Editorial
- asymmetry intentional nhưng focal subject còn nguyên;
- typography không che subject vô lý;
- image rhythm không tạo sliver/blank area.

## 4. HUMAN VISUAL VETO

Nếu automated checks đều xanh nhưng screenshot obvious broken → **FAIL**.

`HTTP 200 + no overflow + no console error` không chứng minh visual correctness.

## 5. SAME-VIEWPORT REMEDIATION LOOP

Với mỗi crop/layout P1:

```text
failing screenshot
→ exact component / CSS / data owner
→ source asset/focal analysis
→ root fix
→ same viewport screenshot
→ manual inspection
→ regression assertion
```

Không close bằng code diff.

## 6. REGRESSION ASSERTIONS

Khi lỗi từng xảy ra, thêm check phù hợp:

- image container ratio bounds;
- object-fit/position owner present;
- card children remain inside same card bounds;
- hero text bounding box stays inside intended region;
- screenshot diff/manual checklist at failing viewport.

Automation không thay manual inspection nhưng giúp ngăn tái phát.

## 7. USER-FEEDBACK REGRESSION

Nếu user phản hồi `cắt hình lệch`, `mất đầu`, `layout lệch`, coi đây là process regression đã chứng minh Prompt 2/3 PASS sai.

Final report phải nêu:

- screenshot evidence;
- root cause;
- fix owner;
- regression added;
- re-render result.

## 8. RELEASE BLOCK

Không merge/deploy nếu còn bất kỳ P1 media/layout blocker nào trên representative primary routes.

> **Screenshot is the final visual truth.**
