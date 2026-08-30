# Website Research & Generation Architect Skill

## Overview

Skill này giúp AI phân tích, nghiên cứu và xây dựng chiến lược hoàn chỉnh cho việc redesign hoặc tạo mới website.

AI không chỉ tạo UI mà phải đóng vai trò:

- Product Designer
- UX Researcher
- Information Architect
- Business Analyst
- SEO Strategist
- Brand Consultant
- Frontend Architect

Mục tiêu:

Tạo ra bộ tài liệu đầy đủ để AI Coding Agent hoặc Developer có thể triển khai website chuẩn về:

- Business
- UX
- UI
- SEO
- Conversion
- Technical

---

# Trigger

Kích hoạt khi user yêu cầu:

- redesign website
- gen lại website
- rebuild website
- clone website
- tạo website mới
- phân tích website
- làm sitemap
- thiết kế landing page
- xây corporate website
- xây ecommerce website
- xây platform

---

# Workflow

## Phase 1 — Understand Requirement

Phân loại input:

### Case A — Có domain

Ví dụ:

"Redesign https://example.com"

Thực hiện:

Website Reverse Engineering.

---

### Case B — Không có domain

Ví dụ:

"Tạo website trường học"

Thực hiện:

Industry Research.

Nghiên cứu:

- Website hàng đầu trong ngành
- Pattern sitemap phổ biến
- UX flow
- Design trend
- Conversion model

---

# Phase 2 — Business Analysis

Phân tích:

## Website Type

Xác định:

- Corporate
- Education
- Technology
- SaaS
- Ecommerce
- Government
- Media
- Marketplace
- Portfolio
- Landing Page

## Business Goal

Xác định mục tiêu:

- Brand awareness
- Lead generation
- Sales conversion
- Recruitment
- Investor communication
- Content distribution
- Product discovery

## Target Audience

Xác định:

B2B:

- CEO
- Manager
- Investor
- Procurement

B2C:

- Customer
- Parent
- Student
- Buyer

---

# Phase 3 — Website Research

Nếu có domain:

## Sitemap Audit

Phân tích:

- Main navigation
- Footer
- Hidden pages
- Category
- Detail page
- Content type

Output:

```
Current Sitemap

Home

├── Category
│
├── Listing
│
├── Detail
│
└── Utility
```

## Content Audit

Đánh giá:

- Website đang truyền tải gì?
- Nội dung quan trọng?
- Nội dung dư thừa?
- Thiếu nội dung nào?
- Cơ hội SEO?

## UX Audit

Phân tích:

Navigation:

- User có tìm được thông tin không?
- Menu có quá phức tạp?
- CTA có rõ?

User Journey:

```
Visitor

↓

Understand Brand

↓

Explore Solution

↓

Build Trust

↓

Conversion
```

## UI Audit

Phân tích:

- Layout
- Typography
- Color
- Component
- Image style
- Motion
- Responsive
- Accessibility

---

# Phase 4 — Competitor Benchmark

Luôn nghiên cứu:

Top 5 website cùng ngành.

Phân tích:

## Information Architecture

Tìm pattern:

- Menu
- Sitemap
- Page structure
- Content hierarchy

## UI Pattern

Phân tích:

- Hero
- CTA
- Card
- Navigation
- Footer
- Interaction

Sau đó rút ra:

Best Practice.

Không coi competitor benchmark là đủ cho visual direction. Competitor giúp hiểu category truth; reference research bên dưới giúp mở rộng visual/interaction quality mà vẫn giữ business/domain fit.

---

# Phase 4A — Design Reference Research & Benchmark

Với website mới, redesign lớn, landing page quan trọng hoặc UI đang generic, route sang `design-reference-research-and-benchmark` trước khi khóa Design Direction.

## Source mix

Không dùng một loại nguồn cho mọi quyết định:

- **Website thật trong ngành / category leaders**: IA, journey, content hierarchy, trust, conversion, responsive behavior.
- **Awwwards, MUUUUU, SiteInspire, Godly, CSS Design Awards, Land-book...**: visual craft, layout, typography, storytelling, motion.
- **Behance**: brand-to-digital translation, design system/case-study thinking; cần phân biệt concept và production.
- **Dribbble**: component/hero/micro-layout ideas; không dùng shot đơn lẻ làm UX evidence.
- **Pinterest / editorial mood sources**: photography, typography mood, texture, campaign/art direction; không dùng để quyết định sitemap/flow.

## Research rule

Tạo mixed candidate pool khoảng 10–20 reference khi scope đủ lớn:

- 4–8 real industry/competitor sites;
- 3–6 curated best-in-class sites;
- 2–4 cross-industry references có pattern hữu ích;
- optional mood/case-study references.

Sau đó chọn 3–6 finalists theo role, ví dụ:

- IA/navigation;
- hero/layout grammar;
- typography/art direction;
- conversion/trust;
- interaction/motion;
- mobile adaptation.

## Scoring

Chấm theo fit thay vì “đẹp nhất”:

- Industry/domain fit: 20%
- Audience/top-task fit: 15%
- Business/conversion fit: 15%
- Brand fit: 15%
- UX/information usefulness: 10%
- Layout/composition usefulness: 10%
- Visual craft: 5%
- Interaction/motion: 5%
- Implementation feasibility: 5%

Score chỉ hỗ trợ critique, không phải truth tuyệt đối.

## Anti-copy rule

Extract principles, không clone pixels/surface:

- không copy nguyên composition;
- không reuse logo/copy/proprietary imagery/assets;
- không ghép nhiều trend thành Frankenstein UI;
- award status không chứng minh usability/accessibility/conversion;
- rationale cuối cùng phải quay về user + business + brand.

Output:

```
00-design-reference-benchmark.md
```

---

# Phase 5 — New Sitemap Architecture

Không copy website cũ.

Xây sitemap mới dựa trên:

- User intent
- Business goal
- SEO
- Conversion

## Sitemap Rules

- Navigation tối đa 5-7 nhóm.
- Không đưa toàn bộ category lên menu.
- Group page làm gateway.
- Listing dùng filter.
- Detail page tập trung conversion.

Output:

```
01-sitemap.md
```

Format:

```md
# Homepage

Purpose:

Target User:

CTA:

Blocks:

1.
2.
3.
```

---

# Phase 6 — Page Architecture

Mỗi page phải có:

```
Page Name

Purpose

Target User

User Journey

Business Goal

Sections

CTA

Content Requirement

Interaction
```

Output:

```
02-page-architecture.md
```

---

# Phase 7 — User Journey

Tạo flow theo persona.

Ví dụ:

```
User Entry

↓

Problem Awareness

↓

Information Discovery

↓

Trust Building

↓

Action
```

Output:

```
03-user-journey.md
```

---

# Phase 8 — Design Direction

Xây dựng Design System dựa trên project truth + domain + reference benchmark, không dựa trên adjective/trend cảm tính.

## Brand Concept

Bao gồm:

- Design concept
- Visual keywords
- Mood
- Personality

## Reference Synthesis

Nếu có `00-design-reference-benchmark.md`, phải ghi:

- reference role → principle extracted;
- adaptation cho project;
- phần không được copy;
- constraint mobile/performance/accessibility.

## Color System

Define:

- Primary
- Secondary
- Background
- Text
- Border
- Semantic colors

## Typography

Define:

- Heading font
- Body font
- Scale
- Usage

## Layout System

Define:

- Container
- Grid
- Spacing
- Radius
- Breakpoint

## Component System

Define:

- Header
- Hero
- Button
- Card
- Form
- Filter
- Tabs
- Footer

Output:

```
04-design-guideline.md
```

---

# Phase 9 — Component System

Tạo quy chuẩn component.

Bao gồm:

- Naming
- Variant
- State
- Responsive
- Interaction

Output:

```
05-component-system.md
```

---

# Phase 10 — Content Strategy

Xây:

- Content hierarchy
- SEO structure
- CTA strategy
- Keyword opportunity

Output:

```
06-content-strategy.md
```

---

# Phase 11 — Development Guideline

Tạo guideline cho AI Coding Agent.

Bao gồm:

## Architecture

- Folder structure
- Component structure
- Naming convention

## Frontend Rules

- Responsive
- Animation
- Performance
- SEO
- Accessibility

Output:

```
07-development-guideline.md
```

---

# Final Output Structure

Với substantial visual work:

```
website-strategy/

├── 00-design-reference-benchmark.md
├── 01-sitemap.md
├── 02-page-architecture.md
├── 03-user-journey.md
├── 04-design-guideline.md
├── 05-component-system.md
├── 06-content-strategy.md
└── 07-development-guideline.md
```

Nếu reference research không cần thiết cho scope nhỏ, `00-design-reference-benchmark.md` có thể được bỏ qua.

---

# Quality Rules

AI bắt buộc:

1. Không thiết kế website dựa trên cảm tính.
2. Luôn research trước khi đề xuất khi scope/risk yêu cầu.
3. Không copy website hiện tại hoặc external reference.
4. Không coi award/gallery popularity là UX proof.
5. Mỗi section phải có mục đích:

- Introduce
- Explain
- Prove
- Explore
- Convert

6. Mỗi page phải trả lời:

- Ai sử dụng?
- Vì sao cần page này?
- Người dùng làm gì tiếp theo?

7. Ưu tiên:

Business goal

>

User experience

>

Brand fit / visual direction

>

Animation

---

# Optional Advanced Output

Nếu user yêu cầu code generation:

Tạo thêm:

```
08-ai-code-generation-prompt.md
```

Chứa prompt cho:

- Cursor
- Claude Code
- Github Copilot
- Frontend Agent

Bao gồm:

- Project context
- Sitemap
- Design system
- Reference synthesis rules
- Component rules
- Coding requirements
