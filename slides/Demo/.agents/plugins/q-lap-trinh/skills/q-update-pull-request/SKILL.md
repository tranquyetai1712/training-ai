---
name: q-update-pull-request
description: Phân tích các thay đổi mới (sau refactor/code update) và tự động cập nhật lại PR Title cùng PR Body description bằng ngôn ngữ tự nhiên khái quát chức năng cho Pull Request hiện tại thông qua GitHub CLI (`gh`).
---

# 🔄 Update Pull Request — Cập nhật Miêu tả & Title cho Pull Request

Quy trình tự động phân tích diff mới sau khi refactor/chỉnh sửa code, đọc miêu tả PR hiện tại, giữ nguyên các thông tin cố định (Jira link, checklist...) và cập nhật lại phần **Changes** (bằng ngôn ngữ tự nhiên khái quát chức năng) cùng **PR Title** thông qua GitHub CLI (`gh`).

---

## 🎭 Vai trò (Persona)
Bạn là một **Senior Software Engineer**. Bạn luôn đảm bảo Pull Request phản ánh chính xác, dễ hiểu và cập nhật đầy đủ các thay đổi mã nguồn mới nhất dưới dạng **ngôn ngữ tự nhiên khái quát chức năng/mục đích** (tránh liệt kê danh sách file thô).

---

## ⚙️ Quy trình thực hiện (Workflow)

### Bước 1: Thu thập Context & Lấy thông tin PR hiện tại
1. Lấy tên nhánh hiện tại:
   `BRANCH_NAME=$(git rev-parse --abbrev-ref HEAD)`
2. Kiểm tra thông tin PR hiện tại trên GitHub thông qua GitHub CLI:
   `gh pr view --json number,title,body,baseRefName`
   - Bóc tách `baseRefName` làm **Base Branch** cho việc so sánh diff.
   - Lấy `title` và `body` hiện tại của PR để làm dữ liệu gốc.

### Bước 2: Phân tích mã nguồn thay đổi (Git Diff) & Tổng hợp Chức năng
- Lấy danh sách toàn bộ thay đổi giữa Base Branch và nhánh hiện tại:
  `git diff origin/[baseRefName]...HEAD`
- **Phân tích tổng quan bằng ngôn ngữ tự nhiên**:
  - Xác định **Mục đích & Bối cảnh chính của PR** (PR Purpose & Goal).
  - Khái quát các **thay đổi chức năng chính & cải tiến quan trọng**, nhóm theo từng khía cạnh (Bảo mật, Độ chính xác dữ liệu, Hiệu năng, Giao diện di động UI/UX, Kiểm thử).
  - Mỗi dòng mô tả diễn đạt bằng ngôn ngữ tự nhiên khái quát mục đích & thay đổi chính (tuyệt đối không liệt kê danh sách file hay tên file thô).

### Bước 3: Xử lý Tên Nhánh & Link JIRA
Giả sử tên nhánh có định dạng: `[Prefix]/[TICKET-ID]_...` (Ví dụ: `feature/CHQ-1001` hoặc `fix/CHQ-362_update`).
Bóc tách `[TICKET-ID]` (Ví dụ: `CHQ-1001`, `CHQ-362`).

### Bước 4: Xây dựng PR Title & PR Body Mới Chuẩn Template

- **PR Title Mới**: Bắt buộc giữ `[TICKET-ID]` ở đầu tiêu đề (Ví dụ: `[CHQ-1001] Add Pagy pagination and resolve all review comments`).
- **PR Body Mới**: Tuân thủ khắt khe khung `.github/pull_request_template.md` của dự án:
  - `Fixes [TICKET-ID]`
  - `# Changes`:
    - **`### 🎯 PR Purpose & Goal`**: 1-2 câu ngôn ngữ tự nhiên tóm tắt mục đích chính và giá trị PR mang lại.
    - **`### ✨ Key Functional & Architectural Updates`**: Các bullet point bằng ngôn ngữ tự nhiên mô tả các chức năng chính/cải tiến kỹ thuật lớn, nhóm theo module hoặc mục tiêu (Security, SQL Integrity, UI/UX, Tests).
  - `# Checklist`: Đánh dấu `[x]` CHỈ CHO CÁC MỤC ĐÃ ĐƯỢC CHECK PASS (AI Code Review, RuboCop, RSpec), giữ `[ ]` cho các mục chưa check riêng.
  - `# Screenshots (if applicable)`
  - `# [Pre/Post]-release tasks`

### Bước 5: Xuất ra Lệnh Bash Execution Block
Bắt buộc sử dụng kỹ thuật `HereDoc (EOF)` kết hợp với `gh pr edit` để cập nhật trực tiếp PR trên GitHub.

---

## 📝 Quy tắc Bắt buộc (Strict Rules)
1. **Viết theo ngôn ngữ tự nhiên**: Diễn đạt tổng quan các thay đổi chức năng chính để người đọc/PM hiểu ngay mục đích PR. Tuyệt đối KHÔNG liệt kê danh sách file thô dạng `Updated app/controllers/...` hay tên file trong ngoặc.
2. **Tuân thủ khung `.github/pull_request_template.md`**: Giữ đúng 4 phần header của dự án (`Fixes CHQ-XXX`, `# Changes`, `# Checklist`, `# Screenshots`, `# [Pre/Post]-release tasks`).
3. **Chỉ tick `[x]` các mục đã check**: Chỉ đánh dấu `[x]` cho RuboCop, RSpec, AI Code Review nếu đã kiểm tra Pass; giữ `[ ]` cho các mục chưa chạy.
4. **Chỉ output block lệnh Shell ````bash...````.
