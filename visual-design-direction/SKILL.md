---
name: visual-design-direction
description: |
  Chuyển brand, IA và reference intelligence thành visual direction cụ thể cho website: layout grammar,
  hierarchy, typography, color roles, imagery, depth và motion principles. Dùng trước design system/code
  hoặc khi UI hiện tại generic, thiếu nhịp điệu, không phản ánh brand/domain.
---

# Visual Design Direction

## Goal

Tạo một **visual grammar có lý do**, không phải moodboard adjective (“modern, clean, premium”) rồi code tùy hứng.

## Inputs

- Brand identity/constraints.
- Domain expectations và audience trust needs.
- Page templates/IA.
- Content/image reality.
- Existing design strengths cần preserve.
- `docs/design-reference-benchmark.md` khi substantial redesign/new visual direction đã chạy reference research.

Nếu scope đủ lớn nhưng visual direction còn generic và chưa có reference benchmark, route sang `design-reference-research-and-benchmark` trước khi khóa system.

## Workflow

1. Audit reference benchmark theo *principle*, không copy surface; nếu chưa có benchmark và task cần reference intelligence, tạo nó trước.
2. Synthesize nhiều reference roles thành một design DNA coherent; không Frankenstein nhiều style.
3. Define 4–7 visual attributes kèm biểu hiện cụ thể.
4. Define layout grammar: container, grid, asymmetry/symmetry, section rhythm, density.
5. Define hierarchy: display/H1/H2/body/meta/action.
6. Define color role map, không chỉ palette.
7. Define typography pairing/scale/line-length strategy.
8. Define image/illustration/icon art direction.
9. Define elevation/border/radius language theo brand, không theo trend mặc định.
10. Define motion purpose/intensity và reduced-motion behavior.
11. Stress-test trên 2–3 page types + mobile trước khi khóa system.

## Reference synthesis rules

- Mỗi reference cần có job rõ: IA, layout, type, imagery, motion, conversion hoặc mobile.
- Real production site có trọng lượng cao hơn gallery shot cho UX/task decisions.
- Award/curated reference có thể mạnh về craft nhưng không tự động chứng minh usability, accessibility, performance hay conversion.
- Không lấy nguyên “look” của một site; extract pattern rồi map về brand/content/assets hiện có.
- Nếu reference đòi asset/3D/video mà project không có, adapt grammar thay vì giả lập bằng filler.
- Final direction phải giải thích được mà không cần nhắc tên reference.

## Craft rules

- Không mọi section đều container + centered heading + 3 rounded cards.
- Whitespace có rhythm, không chỉ “nhiều khoảng trắng”.
- Một visual device mạnh lặp có chủ ý tốt hơn 10 effect ngẫu nhiên.
- Brand color có role; không fill mọi thứ chỉ vì là primary.
- Image crop/safe zone là design decision.
- Typography phải readable với content thật và tiếng Việt/locale thực tế.
- Motion phải feedback/orientation/hierarchy/delight có kiểm soát.
- Không dùng trend như glass/gradient/oversized type chỉ vì reference dùng; trend phải phục vụ brand và hierarchy.

## Progressive resources

- [Visual craft reference](references/visual-craft-reference.md)
- [Visual direction gate](checklists/visual-gate.md)
- [Direction example](examples/direction-example.md)

## Output

`docs/visual-direction.md` hoặc equivalent gồm layout grammar, hierarchy, color/type roles, media direction, motion/depth rules và do/don't.

Khi có reference benchmark, output nên thêm phần `Reference synthesis` ghi:

- reference role → principle extracted;
- adaptation cho project;
- rejected/non-transferable surface cues;
- constraints mobile/performance/accessibility.

## Acceptance criteria

- Visual direction mô tả được bằng rules có thể implement.
- Có ít nhất 2 page compositions proof-of-concept.
- Brand/domain fit có rationale.
- Mobile visual hierarchy được xem riêng, không chỉ shrink desktop.
- Art direction ảnh/icon rõ.
- Repetition được dùng để tạo consistency chứ không tạo template monotony.
- Nếu dùng external references, direction là synthesis nguyên bản và không phụ thuộc việc clone một site.
