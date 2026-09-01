# MASTER PROMPT V7.1 — STRUCTURAL + MEDIA-INTEGRITY REDESIGN IMPLEMENTATION OS
## V7.0 + IMAGE FOCAL / CROP / LAYOUT HARD GATE

> Kế nhiệm `MASTER-PROMPT-V7.0.md`. Đọc và thực thi toàn bộ V7.0 trước; file này override các phần liên quan media/layout verification.

Route bắt buộc cho media-heavy redesign:

```text
visual-redesign-delta-gate
media-crop-and-layout-integrity
```

## 1. BEFORE CODE: READ MEDIA CONTRACT

Đọc từ Design Contract:

- asset/media inventory;
- focal-point contract;
- component ratio strategy;
- desktop/mobile crop rules;
- risky assets/pressure points.

Nếu fashion/ecommerce có ảnh người mẫu nhưng chưa xác định focal point/crop rule → không code full rollout.

## 2. MEDIA OWNER BEFORE CSS

Không dùng một global rule kiểu:

```css
img { object-fit: cover; }
```

để giải quyết mọi media.

Mỗi media family phải có owner rõ:

```text
hero/editorial
product card
PDP main image
thumbnail
collection/lookbook
related products
```

Mỗi owner quyết định ratio + fit + focal point + responsive override.

## 3. FASHION CROP RULE — HARD FAIL

Nếu source là fashion portrait/full-body:

- không cắt mất đầu/mặt ngoài art-direction intent đã document;
- không crop mất garment chính;
- PDP main image ưu tiên xem sản phẩm đầy đủ hơn dramatic crop;
- product cards phải cho nhận diện silhouette/garment;
- không ép ảnh thành vertical sliver để fit grid.

Nếu screenshot cho thấy head crop/sliver/stretch → **P1, STOP ROLLOUT**.

## 4. CARD OWNERSHIP RULE

Product card phải giữ cùng visual owner:

```text
image → product name → price → metadata → quick action
```

Không cho CSS grid auto-placement khiến text/price/CTA rơi sang vùng khác hoặc cách xa ảnh.

Nếu nhìn screenshot không biết text thuộc product nào → FAIL.

## 5. HERO BOUNDS RULE

Oversized typography được phép, nhưng phải:

- nằm trong intended composition bounds;
- không bị clip ngoài viewport một cách vô nghĩa;
- không che nav hoặc media chính;
- không tạo blank column lớn do grid placement sai;
- giữ hierarchy đọc được tại 375/390/430/768/1440/1920 khi relevant.

## 6. REPRESENTATIVE PAGE GATE

Trước full rollout phải có actual screenshots cho:

- Home top + product/editorial section;
- Shop/PLP product grid;
- PDP main image + purchase panel;
- ít nhất một collection/editorial page;
- mobile equivalents.

Manual visual review bắt buộc. Automated metrics chỉ hỗ trợ.

PASS checklist:

- [ ] no head/face cut where not intentional;
- [ ] garment/product identifiable;
- [ ] no sliver/stretch;
- [ ] no unexpected blank region;
- [ ] text/price belongs to correct product image;
- [ ] CTA belongs to correct decision object;
- [ ] no viewport clip/overlap;
- [ ] crop strategy works on mobile separately.

## 7. VISUAL QA VETO

Nếu screenshot nhìn sai rõ ràng nhưng:

- HTTP 200;
- no console error;
- no horizontal overflow;
- CI green;

thì **screenshot thắng**. Kết quả là FAIL.

Không dùng automated green status để override visual evidence.

## 8. REGRESSION FROM USER FEEDBACK

Các feedback sau là process P1:

- `cắt hình lệch`;
- `mất đầu`;
- `layout lệch`;
- `hình bị kéo thành lát dọc`;
- `text sản phẩm rời khỏi ảnh`.

Bắt buộc:

1. capture exact viewport;
2. trace CSS/component/data owner;
3. fix root cause;
4. add screenshot regression;
5. inspect new screenshot manually;
6. only then continue rollout.

## 9. RELEASE CONDITION

Không merge/deploy nếu representative screenshot còn bất kỳ P1 nào về crop/layout integrity.

> **Rendered visual integrity is a release gate, not a polish step.**
