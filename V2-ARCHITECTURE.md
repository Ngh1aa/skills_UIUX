# skills_UIUX V2 Architecture

V2 biến repository từ một collection `SKILL.md` thành một **UI/UX Agent Operating System** có progressive disclosure, profile routing, deterministic validation và agent evals.

## 1. Skill package contract

Một skill trưởng thành có thể dùng cấu trúc:

```text
<skill>/
├── SKILL.md                 # Trigger + workflow + routing, ưu tiên ngắn
├── references/              # Kiến thức chi tiết chỉ đọc khi cần
│   └── *.md
├── checklists/              # Quality gates có thể tick
│   └── *.md
├── examples/                # Concrete examples, không phải lorem ipsum
│   └── *.md
└── scripts/                 # Deterministic helpers nếu thật sự hữu ích
    └── *
```

Không bắt buộc mọi skill có đủ bốn folder. Chỉ thêm resource khi nó giảm context, tăng tính chính xác hoặc tạo verification loop.

## 2. Progressive disclosure

- Level 1: `name` + `description` giúp agent discover skill.
- Level 2: `SKILL.md` chứa quyết định và workflow cốt lõi.
- Level 3: `references/`, `checklists/`, `examples/`, `scripts/` chỉ load/chạy khi task cần.
- Không duplicate cùng một rule ở nhiều file. `SKILL.md` phải chỉ rõ resource nào dùng cho tình huống nào.

## 3. Profiles

`profiles/*.json` là preset skill cho loại project. Installer copy đúng subset vào `.claude/skills/` để tránh context/tool clutter.

Profiles V2:
- `professional-core`
- `redesign`
- `education`
- `corporate`
- `ecommerce`
- `prototype-uiux`

Profile không thay thế orchestrator. Nó chỉ chọn capability có khả năng cần thiết.

## 4. Eval-driven skill development

Mỗi capability quan trọng phải có representative evals. V2 phân hai loại:

### Structural/regression evals
Chạy tự động bằng script, kiểm:
- frontmatter/name/description;
- profile tham chiếu skill tồn tại;
- resource link local không hỏng;
- eval schema hợp lệ;
- duplicate skill;
- progressive-disclosure warnings.

### Agent capability evals
`evals/tasks/*.json` mô tả task, expected outcomes, must-not behaviors và rubric dimensions. Chạy bằng model/harness bên ngoài; repository không khóa vào một model cụ thể.

## 5. Quality philosophy

Chấm **outcome trước process**. Agent có thể tìm đường giải khác nhau miễn:
- giải quyết đúng user/business goal;
- không phá content/SEO/behavior tốt;
- UI có hệ thống và phù hợp domain;
- responsive/accessibility/performance được verify;
- có evidence thay vì tự tuyên bố hoàn tất.

## 6. Backward compatibility

Các folder skill ở root vẫn giữ nguyên để project V1 không gãy. V2 chỉ thêm resource, routing và tooling. Khi refactor skill lớn, `name` và intent cũ được giữ.
