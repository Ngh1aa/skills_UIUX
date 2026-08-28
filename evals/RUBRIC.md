# Common UI/UX Agent Rubric

Mỗi dimension chấm 0–4.

## 1. User & business alignment — 20%
- 0: giao diện trang trí, không giải task.
- 2: hiểu goal nhưng flow còn generic.
- 4: hierarchy, CTA và flow trace được về user/business goal.

## 2. UX coherence — 20%
- 0: dead-end/flow lỗi.
- 2: happy path dùng được nhưng edge/state yếu.
- 4: navigation, task flow, feedback, error/empty/loading states hợp lý.

## 3. Visual craft & brand fit — 20%
- 0: generic/template/brand sai.
- 2: tương đối consistent.
- 4: hierarchy, typography, spacing, imagery, motion và component grammar có chủ ý, phù hợp domain/brand.

## 4. System quality — 15%
- 0: hardcode/duplicate/one-off.
- 2: có reuse nhưng token/component contract chưa rõ.
- 4: reusable tokens/components/states, ít duplication, architecture maintainable.

## 5. Inclusive/responsive quality — 10%
- 0: unusable trên viewport/keyboard chính.
- 2: responsive cơ bản.
- 4: mobile-first behavior, focus/semantic/contrast/motion constraints được xử lý và verify.

## 6. Web quality — 10%
SEO/performance/security/content preservation theo scope.

## 7. Verification discipline — 5%
- 0: tuyên bố done không evidence.
- 4: build/test/viewport/interaction checks + known limitations rõ.

## Hard fail

Dù score cao vẫn fail nếu:
- phá primary user task;
- xóa content/URL quan trọng trong redesign mà không migration plan;
- tạo inaccessible critical interaction;
- giả mạo evidence/test result;
- vi phạm explicit brand constraint.
