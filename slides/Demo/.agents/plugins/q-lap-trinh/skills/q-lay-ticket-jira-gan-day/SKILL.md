---
name: q-lay-ticket-jira-gan-day
description: Lấy các ticket Jira đang ở chế độ Processing, Review, Done với tài khoản quyetchasqui trong khoảng thời gian 5 ngày đổ lại (đối với ticket cha thì chỉ lấy ticket con, ticket đơn thì lấy chính nó), đồng thời tạo file Weekly Report template dưới storage/KPT/.
---

# 🛠️ Quy trình Lấy Ticket Jira Gần Đây (lay-ticket-jira-gan-day)

Skill này giúp AI tự động tìm kiếm các ticket Jira thuộc tài khoản `quyetchasqui` (quyet tran) thỏa mãn yêu cầu:
- Nếu là ticket cha (có ticket con): Chỉ lấy các ticket con ở các trạng thái tương ứng.
- Nếu là ticket đơn (standalone/không có ticket con): Lấy chính ticket đó nếu thỏa mãn trạng thái và thời gian.
Sau khi truy vấn xong, AI sẽ tự động tạo một file template Weekly Report tại đường dẫn `storage/KPT/weekly_report_<ngay-hien-tai>.md`.

---

## ⚙️ Quy trình Thực Hiện (Workflow)

Bạn phải tuân thủ nghiêm ngặt các bước sau:

### 1️⃣ Xác định khoảng thời gian (Date Calculation)
- Lấy ngày hiện tại trên hệ thống (ví dụ: `YYYY-MM-DD`).
- Tính toán ngày bắt đầu cách đây 4 ngày (tổng cộng 5 ngày bao gồm cả hôm nay).
  - *Ví dụ:* Nếu hôm nay là `2026-07-17`, ngày bắt đầu sẽ là `2026-07-13`. Ngày kết thúc là `2026-07-17`.

### 2️⃣ Truy vấn đợt 1 - Lấy tất cả ticket được gán cho quyetchasqui (Fetch Assigned Issues)
- Sử dụng tool `jira_get` để lấy danh sách ticket được gán cho tài khoản:
  - **path**: `/rest/api/3/search/jql`
  - **queryParams**:
    - `jql`: `assignee = "712020:d6cb0290-a934-4b40-a951-7aa86ab286a9"`
    - `maxResults`: `100`
    - `fields`: `summary,status,assignee,created,updated,subtasks,customfield_10026,customfield_10016`
  - **jq**: `issues[*].{key: key, summary: fields.summary, status: fields.status.name, story_points: fields.customfield_10026 || fields.customfield_10016 || '-', assignee: fields.assignee.displayName, created: fields.created, updated: fields.updated, subtasks: fields.subtasks[*].key}`

### 3️⃣ Phân loại và truy vấn đợt 2 (Process and Fetch Sub-tasks)
Duyệt qua danh sách ticket từ Bước 2:
- **Trường hợp ticket cha** (mảng `subtasks` có chứa phần tử):
  - Bỏ qua ticket cha đó (không đưa vào kết quả hiển thị).
  - Gọi tool `jira_get` để lấy các ticket con của nó thỏa mãn điều kiện trạng thái và thời gian:
    - **path**: `/rest/api/3/search/jql`
    - **queryParams**:
      - `jql`: `parent = "<ParentKey>" AND (status = "Processing" OR status = "In Progress" OR (status IN ("Review", "Done") AND updated >= "YYYY-MM-DD" AND updated <= "YYYY-MM-DD"))` *(thay thế `ParentKey` và khoảng ngày đã tính)*
      - `fields`: `summary,status,assignee,created,updated,customfield_10026,customfield_10016`
    - **jq**: `issues[*].{key: key, summary: fields.summary, status: fields.status.name, story_points: fields.customfield_10026 || fields.customfield_10016 || '-', assignee: fields.assignee.displayName, created: fields.created, updated: fields.updated}`
  - Gom toàn bộ ticket con thỏa mãn điều kiện này vào danh sách kết quả.

- **Trường hợp ticket đơn / Standalone** (mảng `subtasks` rỗng hoặc null):
  - Kiểm tra xem ticket đó có thỏa mãn điều kiện trạng thái/thời gian không:
    - Trạng thái là `Processing` hoặc `In Progress`.
    - HOẶC trạng thái thuộc `Review`, `Done` và `updated` nằm trong khoảng 5 ngày gần đây (từ ngày bắt đầu đến ngày kết thúc ở Bước 1).
  - Nếu thỏa mãn, đưa ticket này vào danh sách kết quả.

### 4️⃣ Định dạng & Hiển thị kết quả (Format Output)
- Tiến hành gộp các danh sách ticket từ Bước 3, loại bỏ các ticket trùng Key (nếu có).
- Hiển thị kết quả dưới dạng bảng Markdown chi tiết với cấu trúc như sau:

| Mã Ticket (Key) | Tiêu đề (Summary) | Trạng thái (Status) | Story Point | Người thực hiện (Assignee) | Ngày tạo (Created) | Cập nhật cuối (Updated) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [KEY-123](https://your-domain.atlassian.net/browse/KEY-123) | Tên ticket... | Processing | 2 | quyetchasqui | YYYY-MM-DD | YYYY-MM-DD |

### 5️⃣ Tạo file báo cáo Weekly Report (Create Weekly Report Template)
- Tạo một file Markdown mới theo đường dẫn: `storage/KPT/weekly_report_<ngay-hien-tai>.md` (ví dụ: nếu hôm nay là `2026-07-17` thì đường dẫn sẽ là `storage/KPT/weekly_report_2026-07-17.md`).
- Nội dung file điền các ticket lấy được theo mẫu sau:

```markdown
Weekly Report (YYYY/MM/DD - YYYY/MM/DD)
 1. Work Results This Week
	a. Planned and completed tickets:
		i. <Symbol> <Key> | <Summary>
		ii. <Symbol> <Key> | <Summary>
	b. Recurring Issues - Recurring warnings (if any)
		i. None
2. Reflection
	a. Keep- Good point
		i. ssss
		ii. ssss
	b. Problem- Points for improvement
		i. xxx
			1. yyyyyy
			2. yyyyyy
	c. Try- Problem Solving Solutions
		i. xxxxx
3. Plan for next week (YYYY/MM/DD - YYYY/MM/DD)
	a. Implement new features assigned in the sprint for both eval-developer and halo_web projects.
```

*Quy tắc điền phần `a. Planned and completed tickets:`:*
- Sử dụng ký hiệu `:small_red_triangle:` nếu ticket ở chế độ `Processing` hoặc `In Progress`.
- Sử dụng ký hiệu `:o:` nếu ticket ở chế độ `Review` hoặc `Done`.
- Sắp xếp thứ tự hiển thị của các ticket con và ticket đơn cho gọn gàng.
- Khoảng thời gian tuần ở tiêu đề lớn và phần Kế hoạch tuần tới được tính toán tương ứng (Thứ Hai đến Thứ Sáu của tuần này và tuần sau).
- Sử dụng tab thụt lề chuẩn như mẫu để đảm bảo định dạng hiển thị.
