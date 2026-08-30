# Mango Ops – Technical Proposal

## 1. Tổng quan

### 1.1. Bối cảnh

Hiện tại team đang vận hành flow gen website theo mô hình:

```text
GitHub Issue
    ↓
Ghi task cần thực hiện
    ↓
Claude Code nhận task
    ↓
Claude Code xử lý code
    ↓
Claude Code comment kết quả lên Issue
    ↓
Push code
    ↓
Vercel Deploy
```

Ví dụ task:

- Tạo website mới
- Sửa website hiện tại
- Thêm block mới
- Sửa responsive
- Fix bug
- Update content
- Deploy production

Vấn đề hiện tại là không phải tất cả thành viên trong team đều có quyền truy cập GitHub, Claude Code hoặc Vercel.

Do đó team khó theo dõi:

- Có bao nhiêu task đang tồn tại
- Task nào đang được xử lý
- Task nào đang chờ
- Claude Code đang làm tới đâu
- Task nào đã hoàn thành
- Website nào đang deploy
- Website nào deploy thành công
- Website nào deploy lỗi
- Comment mới từ Claude Code
- Lịch sử xử lý của từng task

---

## 2. Mục tiêu hệ thống

Xây dựng một ứng dụng nội bộ React Native đóng vai trò như một:

> **DevOps / AI Task Command Center**

Ứng dụng giúp toàn bộ team theo dõi quá trình xử lý task mà không cần trực tiếp truy cập GitHub hoặc Vercel.

Ứng dụng cần trả lời nhanh 4 câu hỏi chính:

```text
Có những task nào?
        ↓
Task nào đang được AI xử lý?
        ↓
Website nào đang deploy?
        ↓
Website nào deploy thành công hoặc thất bại?
```

---

# 3. Kiến trúc tổng thể

```text
                    ┌─────────────────┐
                    │     GitHub      │
                    │ Issues/Comments │
                    └────────┬────────┘
                             │
                          Webhook
                             │
                             ▼
                    ┌─────────────────┐
                    │    Supabase     │
                    │ Edge Functions  │
                    │                 │
                    │ PostgreSQL      │
                    │ Auth            │
                    │ Realtime        │
                    └────────┬────────┘
                             │
                             │ Realtime
                             ▼
                    ┌─────────────────┐
                    │ React Native App│
                    │      Expo       │
                    └────────┬────────┘
                             │
                             ▼
                    Expo Push Service


                    ┌─────────────────┐
                    │     Vercel      │
                    │   Deployment    │
                    └────────┬────────┘
                             │
                          Webhook
                             │
                             ▼
                         Supabase
```

---

# 4. Công nghệ đề xuất

## Mobile App

```text
React Native
Expo
TypeScript
Expo Router
TanStack Query
Supabase SDK
Expo Notifications
```

## Backend

Không cần xây một backend truyền thống riêng bằng NestJS hoặc Express.

Sử dụng:

```text
Supabase Edge Functions
```

cho các logic server-side.

## Database

```text
Supabase PostgreSQL
```

## Authentication

```text
Supabase Auth
```

## Realtime

```text
Supabase Realtime
```

## Push Notification

```text
Expo Push Notification
```

## Task Source

```text
GitHub Issues
```

## Deployment Source

```text
Vercel
```

---

# 5. Vì sao vẫn cần Backend Logic?

React Native không nên gọi trực tiếp GitHub API hoặc Vercel API bằng secret token.

Không nên:

```text
React Native
    ↓
GitHub API

React Native
    ↓
Vercel API
```

Vì nếu đặt:

```env
GITHUB_TOKEN=xxx
VERCEL_TOKEN=xxx
```

trong app mobile thì token có thể bị reverse-engineer từ APK/IPA.

Người lấy được token có thể truy cập:

- Repository
- Issues
- Source code
- Deployment
- Vercel project
- Environment variables

Do đó cần kiến trúc:

```text
React Native
     ↓
Supabase
     ↓
GitHub / Vercel
```

Secret chỉ tồn tại phía server.

---

# 6. Environment Variables

Các secret nên đặt trong Supabase Edge Function hoặc secret manager.

Ví dụ:

```env
GITHUB_APP_ID=
GITHUB_PRIVATE_KEY=
GITHUB_WEBHOOK_SECRET=

VERCEL_TOKEN=
VERCEL_TEAM_ID=
VERCEL_WEBHOOK_SECRET=

SUPABASE_URL=
SUPABASE_SERVICE_ROLE_KEY=

EXPO_ACCESS_TOKEN=
```

Trong React Native chỉ cần:

```env
EXPO_PUBLIC_SUPABASE_URL=
EXPO_PUBLIC_SUPABASE_ANON_KEY=
```

---

# 7. GitHub Integration

## 7.1. GitHub là nguồn Task chính

GitHub Issue tiếp tục được xem là:

> Source of Truth của Task.

Ví dụ:

```text
Issue #231

Title:
Redesign HWS Homepage

Body:
- Làm lại hero
- Responsive mobile
- Update CTA
- Deploy production
```

---

## 7.2. GitHub Webhook

Backend sẽ nhận các event quan trọng:

```text
issues
issue_comment
pull_request
push
workflow_run
workflow_job
```

Một số event chính:

```text
Issue Created
Issue Edited
Issue Closed
Issue Reopened
Comment Created
Comment Edited
Comment Deleted
```

---

## 7.3. GitHub Authentication

Không nên dùng Personal Access Token lâu dài.

Khuyến nghị tạo:

```text
GitHub App
```

Ví dụ:

```text
Mango Ops GitHub App
```

Install vào GitHub Organization hoặc các repository cần theo dõi.

Permission gợi ý:

```text
Metadata: Read
Issues: Read
Contents: Read
Pull Requests: Read
Actions: Read
```

Nếu app có chức năng comment hoặc thay đổi status:

```text
Issues: Write
```

---

# 8. Vercel Integration

Vercel là:

> Source of Truth của Deployment.

Theo dõi các event:

```text
deployment.created
deployment.ready
deployment.succeeded
deployment.error
deployment.canceled
deployment.rollback
```

Ví dụ:

```text
deployment.created
        ↓
Status = DEPLOYING
        ↓
Push Notification

deployment.succeeded
        ↓
Status = DEPLOYED
        ↓
Push Notification
```

Nếu:

```text
deployment.error
```

thì:

```text
Status = DEPLOY_FAILED
```

---

# 9. Mapping Issue → Branch → Commit → Deployment

Đây là phần quan trọng nhất của hệ thống.

Nếu không có quy chuẩn này thì rất khó biết deployment nào thuộc task nào.

Khuyến nghị quy ước branch:

```text
issue/{issue_number}-{slug}
```

Ví dụ:

```text
issue/231-hws-homepage
```

Commit:

```text
feat: redesign homepage [#231]
```

Flow:

```text
GitHub Issue #231
        │
        ├── Repository: hws
        │
        ├── Branch
        │   issue/231-hws-homepage
        │
        ├── Commit
        │   a812c8...
        │
        └── Vercel Deployment
            dpl_xxxxx
```

Nhờ vậy backend có thể map:

```text
Task
 ↓
Branch
 ↓
Commit
 ↓
Deployment
```

---

# 10. Task Status

Không nên parse nội dung comment của Claude Code để đoán trạng thái.

Nên sử dụng state machine rõ ràng.

```text
NEW
 ↓
QUEUED
 ↓
WORKING
 ↓
CODE_COMPLETED
 ↓
DEPLOYING
 ↓
DEPLOYED
 ↓
DONE
```

Các trạng thái lỗi:

```text
WORKING
 ↓
FAILED
```

hoặc:

```text
DEPLOYING
 ↓
DEPLOY_FAILED
```

Có thể map thêm với GitHub Labels:

```text
status:new
status:queued
status:working
status:deploying
status:done
status:failed
```

---

# 11. Database Schema

Database không cần clone toàn bộ GitHub.

Chỉ lưu dữ liệu phục vụ Dashboard.

---

## 11.1. projects

```text
id
name
slug
github_owner
github_repo
vercel_project_id
production_url
created_at
updated_at
```

---

## 11.2. tasks

```text
id
project_id

github_issue_id
github_issue_number

title
description

status

branch
commit_sha

created_by
assigned_to

created_at
updated_at
completed_at
```

---

## 11.3. task_events

Dùng để tạo Timeline.

```text
id
task_id

type
message
actor

metadata

created_at
```

Ví dụ type:

```text
issue_created
claude_started
comment_created
code_pushed
deployment_started
deployment_completed
deployment_failed
issue_closed
```

---

## 11.4. deployments

```text
id
project_id
task_id

vercel_deployment_id

branch
commit_sha

environment

url

status

started_at
completed_at

created_at
```

Status:

```text
BUILDING
READY
ERROR
CANCELED
```

---

## 11.5. users

```text
id
email
name
avatar
role
created_at
```

Role:

```text
admin
developer
manager
viewer
```

---

## 11.6. devices

Dùng cho Push Notification.

```text
id
user_id

expo_push_token

platform

created_at
updated_at
```

---

# 12. Các màn hình chính

## 12.1. Dashboard

Màn hình quan trọng nhất.

Ví dụ:

```text
Good morning

TASKS

12
Đang làm

5
Chờ xử lý

3
Deploying

2
Failed
```

Recent Activity:

```text
VAS Career
Deployment successful
2m ago

HWS
Claude commented
5m ago

QTSC
New task created
8m ago
```

Active Tasks:

```text
#231 HWS Homepage
WORKING

#232 VAS Career Block
DEPLOYING

#228 QTSC Responsive
FAILED
```

---

# 13. Task List

Tabs:

```text
All
Working
Deploying
Done
Failed
```

Filter:

```text
Project
Repository
Status
Date
Assignee
Environment
```

Ví dụ:

```text
#231
HWS Homepage
WORKING
Updated 3m ago

#232
VAS Career
DEPLOYING
Updated 6m ago

#228
QTSC Responsive
FAILED
Updated 10m ago
```

---

# 14. Task Detail

Thông tin chính:

```text
#231

Redesign HWS Homepage

WORKING
```

Project:

```text
HWS
hws-website
```

Branch:

```text
issue/231-hws-homepage
```

Task Content:

```text
- Redesign hero
- Update CTA
- Responsive mobile
```

Timeline:

```text
20:30
Task created

20:31
Claude started

20:35
Claude:
Hero completed

20:41
Claude:
Responsive completed

20:42
Deployment started

20:44
Deployment successful
```

---

# 15. Deployment Screen

Ví dụ:

```text
HWS
Production
READY
3m ago

VAS
Preview
BUILDING
4m ago

QTSC
Production
ERROR
12m ago

KES
Production
READY
20m ago
```

Filter:

```text
All
Production
Preview

Ready
Building
Error
```

---

# 16. Notification Screen

Ví dụ:

```text
Today

VAS deploy completed
20:41

Claude commented #231
20:38

HWS deployment started
20:35

New task #238
20:32
```

---

# 17. Push Notification

Một số notification quan trọng.

## New Task

```text
New task

#232
Thêm block tuyển sinh VAS

Vừa được tạo
```

---

## Claude Started

```text
Claude Code

#232 đang được xử lý
```

---

## New Comment

```text
New comment

#232

Claude:
"Đã hoàn thành desktop..."
```

---

## Deployment Started

```text
Deploying

VAS Career đang được deploy
```

---

## Deployment Success

```text
Deployment successful

VAS Career

Production deployment completed
```

---

## Deployment Failed

```text
Deployment failed

HWS

BUILD_FAILED
```

Khi click notification:

```text
app://tasks/232
```

App mở trực tiếp Task Detail.

---

# 18. Flow hoàn chỉnh

Ví dụ người dùng tạo:

```text
GitHub Issue #351

Website:
QTSC

Task:
Thêm block đối tác homepage.
Responsive mobile.
Deploy production.
```

Flow hệ thống:

```text
20:01

Issue Created
     ↓
Supabase nhận Webhook
     ↓
Create Task
     ↓
Push Notification
     ↓
Team biết có task mới
```

Sau đó:

```text
20:02

Claude nhận task
     ↓
Status = WORKING
     ↓
Push Notification
```

Claude comment:

```text
20:10

"Đã hoàn thành block"
```

Backend nhận:

```text
issue_comment webhook
```

và tạo Task Event.

Tiếp tục:

```text
20:15

Code Push
     ↓
Vercel Build
     ↓
deployment.created
     ↓
Status = DEPLOYING
```

Push:

```text
QTSC đang deploy
```

Khi hoàn thành:

```text
20:17

deployment.succeeded
     ↓
Status = DEPLOYED
```

Push:

```text
QTSC deploy thành công
```

Sau đó:

```text
20:18

Claude comment kết quả
     ↓
Issue Closed
     ↓
Status = DONE
```

---

# 19. Chi phí dự kiến

## React Native

```text
$0
```

React Native là open source.

---

## Expo

Có thể sử dụng Free Plan cho MVP.

Push Notification:

```text
$0
```

Có giới hạn build theo plan nhưng với app nội bộ nhỏ thường đủ để phát triển MVP.

---

## Supabase

MVP có thể chạy trên Free Plan.

Bao gồm:

```text
PostgreSQL
Auth
Realtime
Edge Functions
Storage
```

Với team nội bộ nhỏ, số lượng:

```text
users
issues
comments
deployments
notifications
```

thường rất thấp so với giới hạn Free.

Chi phí ban đầu:

```text
$0 / tháng
```

Khi hệ thống quan trọng hơn có thể nâng:

```text
Supabase Pro
~$25 / tháng
```

---

# 20. GitHub Cost

GitHub API và Webhook không tính tiền theo request thông thường.

Nếu organization đang dùng GitHub hiện tại thì app này không làm phát sinh thêm đáng kể.

Có thể sử dụng:

```text
GitHub App
```

thay vì Personal Access Token.

---

# 21. Vercel Cost

App Mango Ops không cần host backend trên Vercel.

Vercel chỉ được dùng như nguồn Deployment Data.

```text
Vercel
   ↓
Webhook / API
   ↓
Supabase
```

Do đó app không nhất thiết làm phát sinh thêm chi phí Vercel.

Lưu ý:

```text
Vercel Hobby
```

là Free Plan, phù hợp chủ yếu cho:

```text
Personal
Testing
Demo
Non-commercial
```

Với project nội bộ doanh nghiệp chính thức nên kiểm tra điều khoản và cân nhắc Vercel Pro.

Nếu công ty đã dùng Vercel Pro thì app Mango Ops thường không làm tăng chi phí đáng kể.

---

# 22. Mobile Store Cost

## Android

Nếu chỉ dùng nội bộ:

```text
Build APK
↓
Gửi file cho team
↓
Cài trực tiếp
```

Chi phí:

```text
$0
```

Nếu muốn publish Google Play thì có phí đăng ký developer.

---

## iOS

Nếu cần:

```text
TestFlight
App Store
Ad Hoc
Custom App
```

thì cần Apple Developer Program.

Chi phí hiện tại thường khoảng:

```text
$99 / năm
```

---

# 23. Chi phí MVP đề xuất

Nếu sử dụng:

```text
React Native
Expo Free
Supabase Free
GitHub hiện tại
Vercel hiện tại
Android APK
```

thì:

```text
Chi phí vận hành MVP
≈ $0 / tháng
```

Không cần:

```text
VPS
Dedicated Backend Server
Redis
Message Queue
Kubernetes
NestJS Backend riêng
```

ở giai đoạn đầu.

---

# 24. Security

Các nguyên tắc bắt buộc:

## Không đặt token trong React Native

Không:

```env
GITHUB_TOKEN=
VERCEL_TOKEN=
SUPABASE_SERVICE_ROLE_KEY=
```

trong app.

---

## Verify Webhook Signature

GitHub:

```text
X-Hub-Signature-256
```

Vercel webhook cũng phải verify secret/signature theo tài liệu của Vercel.

---

## Row Level Security

Supabase phải bật:

```text
RLS
```

cho các table:

```text
tasks
projects
deployments
task_events
devices
```

---

# 25. MVP Scope

Giai đoạn đầu chỉ nên làm:

## Authentication

```text
Login
Logout
```

## Dashboard

```text
Task Summary
Recent Activity
Deploy Status
```

## Tasks

```text
Task List
Task Detail
Task Timeline
```

## Deployments

```text
Deployment List
Deployment Detail
```

## Notifications

```text
Push Notification
Notification History
```

## Integration

```text
GitHub Issue
GitHub Comment
Vercel Deployment
```

---

# 26. Phase 2

Sau khi MVP ổn định có thể thêm:

```text
Create GitHub Issue từ app

Comment vào Issue

Assign Task

Change Status

Retry Deployment

Cancel Deployment

Open Preview URL

Open Production URL
```

---

# 27. Phase 3 – AI Operations

Có thể thêm AI Summary.

Ví dụ:

```text
Hôm nay

14 task hoàn thành
3 task đang xử lý
2 task đang deploy
1 deployment lỗi
```

AI có thể tự phân tích:

```text
Task bị stuck lâu

Deployment fail nhiều lần

Task không có update

Website thường xuyên deploy lỗi
```

---

# 28. Phase 4 – Analytics

Dashboard analytics:

```text
Tasks / Project

Tasks / Developer

Tasks / Day

Average Completion Time

Claude Processing Time

Deployment Frequency

Deployment Failure Rate

Average Deploy Time
```

---

# 29. Naming Concept

Không nên định vị app chỉ là:

```text
GitHub Viewer
```

Nên định vị là:

```text
DevOps Command Center
```

hoặc:

```text
AI Development Operations
```

Tên gợi ý:

```text
Mango Ops
Mango Deploy
Mango Flow
Mango DevOps
Mango Command
```

Khuyến nghị:

```text
Mango Ops
```

---

# 30. Kiến trúc MVP đề xuất cuối cùng

```text
                 GitHub
                    │
                 Webhook
                    │
                    ▼
          ┌──────────────────┐
          │     Supabase     │
          │                  │
          │ Edge Functions   │
          │ PostgreSQL       │
          │ Auth             │
          │ Realtime         │
          └────────┬─────────┘
                   │
                   │
                   ▼
          React Native + Expo
                   │
                   ▼
          Expo Push Notification


                 Vercel
                    │
                 Webhook
                    │
                    ▼
                Supabase
```

Stack:

```text
Mobile
→ React Native + Expo

Backend Logic
→ Supabase Edge Functions

Database
→ Supabase PostgreSQL

Authentication
→ Supabase Auth

Realtime
→ Supabase Realtime

Push
→ Expo Notifications

Tasks
→ GitHub Issues

AI Worker
→ Claude Code

Deployment
→ Vercel
```

---

# 31. Kết luận

Dự án hoàn toàn khả thi.

Không cần xây dựng một backend truyền thống lớn.

Backend logic vẫn cần thiết để:

```text
Bảo vệ GitHub/Vercel Token

Nhận Webhook

Normalize dữ liệu

Mapping Issue → Deployment

Push Notification

Authentication

Permission
```

Nhưng có thể triển khai toàn bộ bằng:

```text
Supabase Edge Functions
```

Do đó kiến trúc MVP có thể rất gọn:

```text
GitHub
   ↓
Claude Code
   ↓
Vercel
   ↓
Supabase
   ↓
React Native
```

Mục tiêu cuối cùng là giúp người quản lý và thành viên team chỉ cần mở một app duy nhất để biết:

```text
Task nào đang làm?

Claude Code đang xử lý tới đâu?

Website nào đang deploy?

Deploy thành công hay thất bại?

Task nào cần chú ý?
```

Đây có thể trở thành dashboard vận hành chung cho toàn bộ flow gen website của team.
