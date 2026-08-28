# Agent Eval Suite

Mục tiêu của evals là đo xem agent **có tạo outcome UI/UX tốt hơn** khi dùng skill library hay không, thay vì chỉ kiểm nó có nhắc lại nội dung SKILL.md.

## Task schema

Mỗi `tasks/*.json` gồm:
- `id`: stable identifier;
- `category`: capability/regression;
- `prompt`: realistic user request;
- `recommended_skills`: skill có khả năng hữu ích, không phải exact tool-call contract;
- `expected_outcomes`: điều output cuối phải đạt;
- `must_not`: failure modes;
- `rubric`: dimensions và trọng số.

## Cách chấm

Ưu tiên thứ tự:
1. Deterministic grader cho file/code/state có thể kiểm chính xác.
2. Rubric/model grader cho chất lượng UX/UI khó biểu diễn bằng assertion.
3. Human review định kỳ để calibrate rubric.

Không fail chỉ vì agent dùng flow/tool khác nếu outcome hợp lệ.

## Hai suite

- **Capability**: case khó, dùng để nâng chất lượng; pass rate ban đầu có thể thấp.
- **Regression**: behavior đã làm tốt; mục tiêu gần 100% để chống backslide.

## Chạy structural checks

```bash
python scripts/validate-skills.py
python scripts/validate-v2.py
```

Agent evals cần harness/model bên ngoài. Repo cố ý lưu task/rubric độc lập model để dùng được với nhiều coding agent.
