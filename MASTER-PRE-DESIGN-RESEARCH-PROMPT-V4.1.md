# MASTER PRE-DESIGN RESEARCH PROMPT V4.1
## V4.0 + MEDIA FOCAL / CROP / LAYOUT INTEGRITY PLANNING

> Kế nhiệm `MASTER-PRE-DESIGN-RESEARCH-PROMPT-V4.0.md`. Đọc và giữ toàn bộ V4.0; file này bổ sung hard gate cho image crop, focal point và layout integrity.

Route bắt buộc cho media-heavy redesign:

```text
visual-redesign-delta-gate
media-crop-and-layout-integrity
```

## 1. MEDIA BASELINE INVENTORY

Trước khi chọn composition, inventory các asset quan trọng:

| Asset | Source ratio/orientation | Subject | Focal point | Current crop problem | Intended role | Desktop strategy | Mobile strategy |
|---|---:|---|---|---|---|---|---|

Với fashion/ecommerce phải phân biệt:

- full-body look;
- half-body/portrait;
- garment detail;
- product-only/flat lay;
- editorial/campaign frame.

Không được mặc định `object-fit: cover; object-position: center` cho mọi asset.

## 2. REFERENCE RESEARCH MUST INCLUDE MEDIA BEHAVIOR

Khi benchmark production fashion/ecommerce, ngoài hierarchy và commerce flow phải ghi:

- product image ratio;
- whether full garment/body context is preserved;
- editorial vs catalogue crop behavior;
- how text/price/quick add remains visually owned by the correct product image;
- PDP main image behavior;
- mobile crop/reflow behavior.

Reference principle chỉ hợp lệ khi transfer được sang asset truth của project.

## 3. MEDIA CONTRACT — BẮT BUỘC TRONG DESIGN CONTRACT

Thêm section:

```text
MEDIA / FOCAL-POINT CONTRACT
```

với matrix:

| Component family | Media intent | Ratio | Fit mode | Focal ownership | Safe crop rule | Mobile override | Verification |
|---|---|---:|---|---|---|---|---|

Tối thiểu cho:

- Home hero/editorial;
- product cards/listing;
- PDP main image + thumbnails;
- collection/lookbook;
- related products.

## 4. PRE-CODE CROP FAILURE CONDITIONS

Direction FAIL trước code nếu proof yêu cầu:

- cắt đầu/mặt người mẫu để fit một ratio tùy tiện;
- ép ảnh ngang thành portrait slice;
- product card image và text phải auto-place qua nhiều grid column không có owner rõ;
- typography oversized dựa vào clip viewport thay vì intentional composition;
- fixed height + intrinsic media tạo khoảng trắng lớn hoặc crop không kiểm soát;
- một crop rule dùng cho mọi ảnh dù focal point khác nhau.

## 5. LAYOUT OWNERSHIP CONTRACT

Mỗi commerce card phải có owner rõ:

```text
image + name + price + metadata + quick action
```

không được để text visually detach khỏi ảnh.

Mỗi hero phải xác định:

```text
container bounds + type bounds + media bounds + focal point + CTA ownership
```

## 6. HANDOFF TO PROMPT 2

Prompt 1 chỉ PASS khi có thể trả lời:

1. Asset nào có nguy cơ crop cao nhất?
2. Focal point của từng hero/product family là gì?
3. Desktop và mobile có dùng cùng crop strategy không?
4. Product card text/price/CTA thuộc image nào và được giữ cùng owner ra sao?
5. Screenshot nào sẽ chứng minh không có head crop, sliver, overflow hoặc layout drift?

> **Nếu media strategy chỉ là `cover + center`, chưa đủ để handoff.**
