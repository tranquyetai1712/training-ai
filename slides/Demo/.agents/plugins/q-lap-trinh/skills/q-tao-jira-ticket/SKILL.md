---
name: q-tao-jira-ticket
description: Phân tích yêu cầu mơ hồ để lên cấu trúc Epic/Task/Sub-task/Bug chuyên nghiệp và tự động tạo ticket trên Jira Cloud.
---

# Hướng Dẫn Skill: Tự Động Tạo Jira Ticket Chuyên Nghiệp (Production Grade)

Skill này hỗ trợ AI đóng vai trò là một Business Analyst (BA) kết hợp Senior Developer để phân tích các yêu cầu mơ hồ từ người dùng, quét metadata dự án động, xây dựng cấu trúc ticket tối ưu và tự động tạo chúng trên Jira Cloud thông qua Model Context Protocol (MCP).

---

## 1. Quy Trình Thực Hiện (Workflow Steps)

### Bước 1: Xác Định Dự Án & Quét Metadata Động (Dynamic Metadata Discovery)
1. **Lấy danh sách dự án**: Gọi tool `jira_get` với `path: "/rest/api/3/project"` và `jq: "[.[] | {key: key, name: name, id: id}]"`.
2. **Xác định Project Key**: So khớp yêu cầu người dùng hoặc hiển thị danh sách dạng Multiple Choice nếu chưa rõ.
3. **Quét Issue Types hợp lệ của dự án (CRITICAL)**:
   - Gọi `jira_get` với `path: "/rest/api/3/project/{PROJECT_KEY}"` và `jq: ".issueTypes[] | {id: id, name: name, subtask: subtask}"`.
   - Lưu trữ danh sách `issueTypes` thực tế của dự án để nhận biết chính xác tên và ID của các issue types (ví dụ: dự án dùng `Sub-task` hay `Subtask`, `Story` hay `Feature`, `Bug` hay `Defect`).

### Bước 2: Phân Tích Loại Ticket, Độ Phức Tạp & Khung Description
Phân tích yêu cầu người dùng để chọn **Loại Ticket** và **Mô hình Hierarchy**:
- **Độ Phức Tạp Cao (Nhiều module/tính năng lớn)**:
  - Cấu trúc: 1 **Epic** -> Các **Task/Story/Bug** liên kết vào Epic đó qua trường `parent: {"key": "EPIC_KEY"}`.
- **Độ Phức Tạp Trung Bình (1 tính năng nhưng cần chia nhỏ công việc)**:
  - Cấu trúc: 1 **Task/Story** cha -> Các **Sub-task** con liên kết qua trường `parent: {"key": "PARENT_KEY"}`.
- **Độ Phức Tạp Thấp / Bug / Chỉnh Sửa Nhỏ**:
  - Cấu trúc: Đúng 1 **Task** hoặc 1 **Bug** đơn lẻ duy nhất.

Áp dụng Khung Description phù hợp với loại ticket:
- **Feature / User Story**:
  - `1. Context & Background`: Bối cảnh yêu cầu.
  - `2. User Story`: As a [role], I want [feature], So that [benefit].
  - `3. Acceptance Criteria (AC)`: Danh sách các tiêu chí nghiệm thu đánh số thứ tự.
  - `4. Out of Scope`: Các phạm vi không thuộc ticket này (nếu có).
- **Bug Report**:
  - `1. Bug Summary & Impact`: Tóm tắt lỗi và mức độ ảnh hưởng.
  - `2. Steps to Reproduce`: Các bước cụ thể để tái hiện lỗi.
  - `3. Expected vs Actual Behavior`: Kết quả mong đợi vs Kết quả thực tế.
  - `4. Environment & Logs`: Môi trường gặp lỗi, thiết bị, log/stack trace.
- **Technical Task / Refactor / Chore**:
  - `1. Technical Goal`: Mục tiêu kỹ thuật.
  - `2. Proposed Approach & Implementation Notes`: Giải pháp và các lưu ý kỹ thuật.
  - `3. Affected Services / Components`: Các thành phần/dịch vụ bị ảnh hưởng.
  - `4. Definition of Done (DoD)`: Tiêu chí hoàn thành kỹ thuật (Unit test, RuboCop, Spec, etc.).

### Bước 3: Soạn Thảo Bản Nháp & Xác Nhận (Draft Gate)
Tạo bản nháp cho từng ticket dự kiến tạo với đầy đủ thông tin:
- **Summary**: Tiêu đề súc tích, định dạng `[Loại] Hành động + Tên chức năng/nhiệm vụ`.
- **Issue Type**: Tên chính xác quét từ Metadata ở Bước 1.
- **Priority**: `Highest`, `High`, `Medium`, `Low`, hoặc `Lowest` (Mặc định `Medium`).
- **Labels**: Danh sách tags dạng array (vd: `["backend", "api"]`).
- **Description**: Nội dung chi tiết theo đúng khung đã chọn ở Bước 2.

Trình bày bản nháp dạng bảng Markdown cho người dùng xem và yêu cầu xác nhận:
```markdown
### 📝 BẢN NHÁP TICKET JIRA DỰ KIẾN (Project: [PROJECT_KEY])

| STT | Loại Ticket | Tiêu đề | Priority | Labels | Liên kết (Epic/Parent) |
|---|---|---|---|---|---|
| 1 | Story | [Story] Thêm tính năng thanh toán | High | ["payment", "api"] | None |
| 2 | Sub-task | [Sub-task] Tạo API Stripe charge | Medium | ["backend"] | Task #1 |
```
*Lưu ý: Dừng lại và chờ người dùng phản hồi. Chỉ tiến hành tạo ticket thật khi người dùng gõ "Tiến hành" hoặc xác nhận đồng ý.*

### Bước 4: Tạo Ticket Thực Tế Trên Jira & Error Handling
Khi người dùng đồng ý, thực hiện tạo ticket theo thứ tự logic bằng cách gọi tool `jira_post` với `path: "/rest/api/3/issue"`:
1. **Thứ tự tạo**: Tạo Epic/Task cha trước -> Lấy ID/Key -> Tạo Task con/Sub-task liên kết bằng trường `parent: { "key": "PARENT_KEY" }`.
2. **Cấu trúc Body JSON**:
   ```json
   {
     "fields": {
       "project": { "key": "PROJECT_KEY" },
       "summary": "[Task] Tiêu đề ticket",
       "issuetype": { "name": "Task" },
       "priority": { "name": "Medium" },
       "labels": ["backend", "api"],
       "description": {
         "type": "doc",
         "version": 1,
         "content": [...]
       }
     }
   }
   ```
3. **Cơ chế Xử Lý Lỗi API (Error Resilience)**:
   - Luôn sử dụng `jq: "{id: id, key: key, self: self}"` để tối ưu token trả về.
   - Nếu `jira_post` trả về lỗi HTTP 400 do không khớp `issuetype.name` -> Tự động chuyển sang sử dụng `issuetype: { "id": "ISSUE_TYPE_ID" }` từ Metadata ở Bước 1 và thử lại.
   - Nếu lỗi do định dạng ADF -> Kiểm tra và làm sạch cấu trúc JSON nodes ADF trước khi re-try.

---

## 2. Hướng Dẫn Định Dạng Atlassian Document Format (ADF) Mở Rộng

Khi tạo ticket bằng `jira_post` tới `/rest/api/3/issue`, trường `description` trong body JSON bắt buộc phải theo cấu trúc ADF sau:

### Mẫu ADF tổng hợp phong phú:
```json
{
  "type": "doc",
  "version": 1,
  "content": [
    {
      "type": "heading",
      "attrs": { "level": 2 },
      "content": [{ "type": "text", "text": "1. Context & Background" }]
    },
    {
      "type": "paragraph",
      "content": [
        { "type": "text", "text": "Đây là mô tả bối cảnh có " },
        { "type": "text", "text": "chữ in đậm", "marks": [{ "type": "strong" }] },
        { "type": "text", "text": " và " },
        { "type": "text", "text": "code inline", "marks": [{ "type": "code" }] }
      ]
    },
    {
      "type": "heading",
      "attrs": { "level": 2 },
      "content": [{ "type": "text", "text": "2. Acceptance Criteria (AC)" }]
    },
    {
      "type": "bulletList",
      "content": [
        {
          "type": "listItem",
          "content": [
            {
              "type": "paragraph",
              "content": [{ "type": "text", "text": "Tiêu chí nghiệm thu 1..." }]
            }
          ]
        }
      ]
    },
    {
      "type": "heading",
      "attrs": { "level": 2 },
      "content": [{ "type": "text", "text": "3. Technical Details & Logs" }]
    },
    {
      "type": "codeBlock",
      "attrs": { "language": "json" },
      "content": [
        { "type": "text", "text": "{\n  \"status\": 200,\n  \"message\": \"Success\"\n}" }
      ]
    },
    {
      "type": "panel",
      "attrs": { "panelType": "info" },
      "content": [
        {
          "type": "paragraph",
          "content": [{ "type": "text", "text": "Lưu ý: Panel hỗ trợ info, note, warning, error, success." }]
        }
      ]
    }
  ]
}
```
