---
name: skill-authoring-and-governance
description: |
  Viết, review và bảo trì SKILL.md cho library này. Dùng khi thêm skill mới, tách skill quá dài,
  sửa trigger/description, loại bỏ overlap hoặc cập nhật quy trình theo tiêu chuẩn mới để agent
  discover đúng capability và không bị context overload.
---

# Skill Authoring & Governance

## Goal

Skill phải giống SOP cho một chuyên gia mới vào team: discoverable, actionable, testable và không lặp với skill khác.

## Frontmatter

- `name`: lowercase, number, hyphen; ngắn và cụ thể.
- `description`: phải nói **what + when** và chứa keyword user có thể dùng để trigger.
- Giữ metadata nhẹ.

## Main body

Ưu tiên cấu trúc:

1. Purpose/goal.
2. Preconditions/prerequisites.
3. Decision rules.
4. Step-by-step workflow.
5. Output.
6. Acceptance criteria.
7. Anti-patterns.

Nếu main skill trở nên dài, tách reference/examples/scripts để progressive disclosure. Không biến SKILL.md thành textbook.

## Overlap test

Trước skill mới hỏi:

- Capability này khác existing skill ở decision nào?
- Có thể thêm section vào skill hiện tại không?
- Trigger có phân biệt được không?
- Agent có cần load hai skill cùng lúc không?

Nếu overlap >70%, ưu tiên merge/refactor thay vì tạo folder mới.

## Time-sensitive knowledge

Không hardcode version/threshold nếu không cần. Nếu cần baseline, ghi rõ cần verify current official guidance khi execution.

## Quality evaluation

Test skill bằng ít nhất các case:

- Positive trigger: task rõ ràng phải load skill.
- Negative trigger: task gần giống nhưng không nên load.
- Complex case: cần compose với 2–3 skill khác.
- Failure case: missing input/edge case.

Đánh giá output có tuân procedure và quality gate không, không chỉ xem agent có nhắc lại lý thuyết.

## Governance

Mỗi lần standard/framework đổi:

1. Xác định skill bị ảnh hưởng.
2. Update minimal authoritative section.
3. Ghi source/date nếu knowledge time-sensitive.
4. Re-run representative evaluations.
5. Tránh fork nhiều version skill không cần thiết.

## Acceptance criteria

- [ ] Trigger description rõ what + when.
- [ ] Workflow action-oriented.
- [ ] Có output/gate.
- [ ] Không overlap vô lý.
- [ ] Main body đủ ngắn để load hiệu quả.
- [ ] Time-sensitive claims có strategy cập nhật.
