---
name: ui-craft-and-visual-qa
description: |
  Review và polish UI ở mức craft: hierarchy, spacing, alignment, density, typography,
  imagery, states, responsive consistency và visual regression. Dùng trước khi gọi giao diện
  hoàn tất hoặc khi UI “đúng chức năng nhưng chưa chuyên nghiệp / trông như AI template”.
---

# UI Craft & Visual QA

## Goal

Biến UI từ “đã code” thành **coherent, intentional, production-grade**.

## Non-negotiable evidence rule

Với substantial UI/redesign work, **source code + build success không phải visual QA**.

Muốn kết luận `PASS` phải có actual rendered evidence của implementation và phải **mở/inspect bằng mắt** evidence đó. Evidence phù hợp có thể là live/local browser, screenshots hoặc equivalent render capture.

Nếu không thể render/capture/inspect implementation:

- ghi `VISUAL QA: BLOCKED` hoặc `UNVERIFIED`;
- nêu blocker cụ thể;
- không gọi UI `finished`, `polished`, `visually verified` hoặc `production-grade`;
- không dùng static assertions/CSS grep thay cho nhìn giao diện thật.

## Review order

Không bắt đầu bằng shadow/radius. Review từ macro đến micro:

1. Page purpose và visual hierarchy.
2. Cross-page composition / template monotony.
3. Section rhythm và density.
4. Grid/alignment.
5. Typography/readability.
6. Components/states.
7. Imagery/icon consistency.
8. Micro-details/motion.

## Mandatory cross-page review

Với multi-page website, capture representative **top-of-page screenshots side-by-side** trước khi soi micro-detail.

Review ít nhất các primary page roles khác nhau và hỏi:

- first visual anchor có phản ánh đúng page task không?
- hero/top-of-page có bị copy cùng shell rồi thay copy/image không?
- page nào cần map, floor plan, product object, evidence, form, data, timeline... nhưng lại bị ép thành image banner?
- hierarchy giữa các page có đủ khác để người dùng hiểu “mình đang ở page loại gì”, nhưng vẫn cùng brand system?
- navigation/tokens/signature motif tạo consistency hay toàn layout đang tạo monotony?

Với site có 5+ materially different primary page roles, nếu gần như toàn bộ top-of-page dùng một composition family mà không có documented rationale, mặc định là **P1 design-system/composition issue**.

## Anti-generic UI checks

Cảnh báo nếu xuất hiện hàng loạt pattern thiếu rationale:

- Mọi section đều là card bo tròn.
- Gradient/glass/shadow dùng khắp nơi.
- Mọi title đều centered.
- Icon nằm trong badge tròn chỉ để trang trí.
- Section lặp `heading + 3 cards` liên tục.
- Nhiều màu accent cạnh tranh.
- Hero quá nhiều label/badge/CTA.
- Nhiều primary page dùng cùng `copy + image` hero chỉ đổi text/asset.
- Domain-native decision objects bị đẩy xuống dưới để nhường hero cho ảnh trang trí.

Nếu brand yêu cầu minimal, editorial, institutional, luxury... phải để visual grammar phản ánh đúng personality, không dùng default SaaS template.

## 5-second first-impression test

Cho mỗi primary page screenshot, trong 5 giây phải trả lời được:

1. Đây là page về việc gì?
2. Thứ quan trọng nhất user nên nhìn thấy là gì?
3. Primary action là gì?
4. Visual này có thuộc brand/domain này không, hay có thể đổi logo cho project khác?

Nếu không trả lời được, chưa xuống micro-polish; quay lại hierarchy/composition owner.

## Spacing audit

- Kiểm vertical rhythm giữa section, heading, paragraph, controls.
- Chỉ dùng spacing scale; exception phải có lý do.
- Parent dùng `gap`; tránh margin ngẫu nhiên giữa siblings.
- Cùng một relationship phải có cùng khoảng cách.

## Typography audit

- H1/H2/H3 khác nhau đủ rõ nhưng không nhảy scale vô lý.
- Body line-height và line length dễ đọc.
- Button/nav text không quá nhỏ.
- Font weight không dùng thay cho hierarchy duy nhất.
- Vietnamese diacritics và font fallback phải render tốt nếu site tiếng Việt.

## Alignment audit

- Text, image, card, CTA bám cùng grid line.
- Optical alignment được phép nhưng phải có chủ đích.
- Không để container widths thay đổi tùy page vô lý.

## Color/contrast and brand-role audit

Không chỉ check palette tồn tại. Kiểm actual rendered states:

- logo trên mọi nav/background state;
- CTA text/icon trên default/hover/focus;
- active nav/link states;
- text trên image/gradient/overlay;
- muted/meta text readability;
- accent color có semantic/brand role hay bị rải ngẫu nhiên.

Một logo hoặc CTA biến mất vì white-on-white / low contrast là P0/P1 visual defect tùy mức ảnh hưởng và phải chặn handoff.

## State audit

Mọi interactive component kiểm: default, hover, focus-visible, active, disabled, loading, error và selected/expanded nếu có.

## Responsive visual QA

Tại mobile/tablet/desktop kiểm riêng:

- Reading order.
- Crop ảnh.
- Line wrapping ở title/button/nav.
- Touch target.
- Overflow.
- Sticky/fixed elements che content.
- Density và white space.
- Hero/page composition có được **recomposed** hay chỉ stack/shrink desktop.

## Evidence set

Trước done, với substantial multi-page website nên có tối thiểu:

- desktop representative captures (thường 1280/1440 hoặc project target);
- mobile representative captures (thường 375/390 hoặc project target);
- tablet/intermediate width khi layout có risk;
- cross-page top-of-page montage/contact sheet;
- changed interactive state capture nếu state visual quan trọng.

Không bắt buộc một viewport cố định cho mọi project; chọn theo audience/device evidence. Nhưng không được chỉ inspect một desktop screenshot rồi gọi site responsive/finished.

Ghi issue severity P0/P1/P2 và phân biệt:

- `[product]` actual rendered UI sai;
- `[evidence]` screenshot/capture/render artifact không đủ để kết luận.

## Fix loop

`capture → inspect macro → log P0/P1/P2 → fix owning component/token/composition → recapture → compare`

- P0/P1 phải được xử lý hoặc ghi rõ blocker trước handoff.
- Không sửa micro-detail P2 trong khi composition/hierarchy P1 còn sai.
- Nếu user phải chỉ ra một lỗi obvious mà rendered evidence lẽ ra đã phát hiện, thêm lỗi đó thành regression check/checklist cho skill/project thay vì chỉ vá project.

## Acceptance criteria

- [ ] Actual rendered implementation đã được mở/inspect; nếu không thì status là BLOCKED/UNVERIFIED, không PASS.
- [ ] Không có spacing/alignment inconsistency rõ ràng.
- [ ] Không có component variant trùng chức năng.
- [ ] Visual hierarchy đọc được trong 5–10 giây.
- [ ] Cross-page composition không rơi vào template monotony vô lý.
- [ ] Primary page roles có first visual anchor phù hợp user task.
- [ ] Mobile không bị “compressed desktop”.
- [ ] Focus/error/loading states nhìn thấy được.
- [ ] Logo/nav/CTA vẫn rõ ở các background/state thực tế.
- [ ] UI phản ánh brand/domain thay vì generic template.
