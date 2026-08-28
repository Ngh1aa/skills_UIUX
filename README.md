# skills_UIUX — Professional Website Agent Skill Library

Bộ skill dành cho AI coding agent xây dựng và nâng cấp website theo quy trình chuyên nghiệp từ discovery → UX → UI → design system → implementation → QA → release → monitoring.

## Mục tiêu

Không để agent nhảy thẳng vào code. Mỗi quyết định phải có đầu vào, rationale, output và quality gate. Bộ skill ưu tiên:

- User goal và business goal trước decoration.
- Brand consistency trước trend.
- Reusable system trước page-by-page styling.
- Accessibility, responsive, SEO, performance và security từ đầu.
- Evidence và QA trước khi tuyên bố hoàn tất.
- Preserve những gì đang tốt khi redesign; không phá SEO/content/code vô lý.

## Cách dùng

### Claude Code project skills

Claude Code auto-discover project skills tại:

```text
.claude/skills/<skill-name>/SKILL.md
```

Repo này là **skill library ở root** để dễ version và quản lý. Khi dùng cho một project, copy những folder skill cần thiết vào `.claude/skills/` của project hoặc dùng script/quy trình cài đặt riêng của bạn.

### Agent khác

Nếu agent hỗ trợ `SKILL.md`, giữ mỗi folder như một capability độc lập và chỉ load skill liên quan đến task hiện tại. Không load toàn bộ library cùng lúc.

## Orchestrator

Bắt đầu bằng `website-delivery-pipeline/SKILL.md`. Skill này điều phối thứ tự và gọi các skill chuyên môn khi cần.

## Nhóm skill

1. Discovery & strategy
2. Brand & visual direction
3. UX research, journey, IA, laws
4. Content & conversion
5. Design system & components
6. Interaction, motion, responsive, accessibility
7. Frontend architecture & implementation
8. SEO, performance, security, analytics
9. Testing, visual QA, release
10. Monitoring & maintenance
11. Redesign/design-to-code workflows
12. Domain-specific website playbooks

Xem `SKILL-CATALOG.md` để biết toàn bộ coverage và khi nào dùng từng skill.

## Standards baseline

Skill phải ưu tiên nguồn chính thức và kiểm tra lại khi tiêu chuẩn thay đổi. Baseline của library hiện tại gồm:

- WCAG 2.2 Level AA cho accessibility.
- Design Tokens Community Group stable format 2025.10 khi cần interchange token.
- Core Web Vitals: LCP, INP, CLS; ưu tiên field data và p75.
- Google Search Essentials cho search eligibility/best practices.
- OWASP Top 10:2025 cho web application security awareness.
- Framework production guidance tương ứng với version project đang dùng.

## Nguyên tắc authoring skill

- `name` ngắn, lowercase + hyphen.
- `description` nói rõ **skill làm gì** và **khi nào dùng**.
- SKILL.md tập trung vào procedure, decision rules và quality gate.
- Không nhồi reference dài vào main skill; tách resource nếu cần.
- Không hardcode công nghệ nếu requirement có thể framework-agnostic.
- Mọi checklist phải dẫn tới hành động hoặc bằng chứng kiểm chứng.

## Quy tắc chất lượng website

Một website chưa được coi là hoàn tất chỉ vì “nhìn đẹp”. Trước release phải chứng minh:

- Primary user journeys chạy được.
- Không có dead-end quan trọng.
- Responsive hoạt động trên viewport mục tiêu.
- Keyboard/focus/forms usable.
- Content thật hoặc content model hoàn chỉnh.
- SEO/indexability không bị phá.
- Core interactions không gây layout shift/jank.
- Build/test/audit đạt gate của project.
- Known issues được ghi rõ.
