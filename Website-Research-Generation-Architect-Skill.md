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


---

## Content Audit

Đánh giá:

- Website đang truyền tải gì?
- Nội dung quan trọng?
- Nội dung dư thừa?
- Thiếu nội dung nào?
- Cơ hội SEO?


---

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


---

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

Xây dựng Design System.


## Brand Concept

Bao gồm:

- Design concept
- Visual keywords
- Mood
- Personality


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

Luôn tạo:


```
website-strategy/

├── 01-sitemap.md

├── 02-page-architecture.md

├── 03-user-journey.md

├── 04-design-guideline.md

├── 05-component-system.md

├── 06-content-strategy.md

└── 07-development-guideline.md
```


---

# Quality Rules

AI bắt buộc:

1. Không thiết kế website dựa trên cảm tính.

2. Luôn research trước khi đề xuất.

3. Không copy website hiện tại.

4. Mỗi section phải có mục đích:

- Introduce
- Explain
- Prove
- Explore
- Convert


5. Mỗi page phải trả lời:

- Ai sử dụng?
- Vì sao cần page này?
- Người dùng làm gì tiếp theo?


6. Ưu tiên:

Business goal

>

User experience

>

Visual design

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
- Component rules
- Coding requirements
