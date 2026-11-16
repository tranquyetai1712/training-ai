---
name: q-xuat-excel-ticket-tuan
description: Báo cáo danh sách các ticket Jira đã và đang làm trong tuần làm việc (từ Thứ 2 tuần trước đến Thứ 2 tuần này nếu hôm nay là Thứ 2, hoặc từ Thứ 2 tuần này đến ngày hiện tại nếu không phải Thứ 2) thuộc tài khoản quyetchasqui, ghép nối với Link PR GitHub tương ứng, Story Point và xuất file Excel (.xlsx).
---

# 📊 Skill Báo Cáo Ticket Tuần & Xuất File Excel (q-xuat-excel-ticket-tuan)

Skill này giúp AI tự động thu thập danh sách ticket Jira của tài khoản `quyetchasqui`, đối chiếu với các Pull Request trên GitHub và xuất thành file Excel `.xlsx` phục vụ báo cáo retrospective / weekly report.

---

## ⚙️ Quy trình Thực Hiện (Workflow)

Bạn phải tuân thủ nghiêm ngặt các bước sau:

### 1️⃣ Tính toán Khoảng thời gian (Date Calculation)
Xác định ngày hiện tại trên hệ thống (ví dụ: `YYYY-MM-DD` và ngày trong tuần):
- **Nếu hôm nay là Thứ Hai**:
  - `tu_ngay`: Thứ Hai của tuần trước (`YYYY-MM-DD`).
  - `den_ngay`: Thứ Hai của tuần này (`YYYY-MM-DD`).
- **Nếu hôm nay KHÔNG PHẢI Thứ Hai**:
  - `tu_ngay`: Thứ Hai của tuần này (`YYYY-MM-DD`).
  - `den_ngay`: Ngày hiện tại (`YYYY-MM-DD`).

*(Đồng thời định dạng chuỗi ngày dạng `YYYYMMDD` để dùng làm tên file Excel, ví dụ: `20260727__20260803`)*.

---

### 2️⃣ Truy vấn Ticket Jira (Fetch Jira Tickets)
- Sử dụng tool `jira_get` để tìm kiếm danh sách ticket gán cho tài khoản `quyetchasqui`:
  - **path**: `/rest/api/3/search/jql`
  - **queryParams**:
    - `jql`: `assignee = "712020:d6cb0290-a934-4b40-a951-7aa86ab286a9"`
    - `maxResults`: `100`
    - `fields`: `summary,status,assignee,created,updated,subtasks,customfield_10026,customfield_10016`
  - **jq**: `issues[*].{key: key, summary: fields.summary, status: fields.status.name, story_points: (fields.customfield_10026 || fields.customfield_10016 || '-'), subtasks: fields.subtasks[*].key}`

#### Rules lọc ticket cha / ticket con / ticket đơn:
1. **Ticket Cha** (mảng `subtasks` có phần tử):
   - **Bỏ qua ticket cha** đó (không lấy ticket cha vào báo cáo).
   - Tiếp tục dùng `jira_get` lấy danh sách ticket con của ticket cha đó:
     - `jql`: `parent = "<ParentKey>" AND (status = "Processing" OR status = "In Progress" OR (status IN ("Review", "Done") AND updated >= "<tu_ngay>" AND updated <= "<den_ngay>"))`
2. **Ticket Đơn / Standalone** (mảng `subtasks` rỗng hoặc null):
   - Chỉ giữ lại nếu:
     - Trạng thái là `Processing` hoặc `In Progress`.
     - HOẶC trạng thái thuộc `Review` / `Done` VÀ ngày `updated` nằm trong khoảng từ `tu_ngay` đến `den_ngay`.

---

### 3️⃣ Tìm kiếm Link Pull Request GitHub (Fetch GitHub PRs)
Với mỗi ticket Jira hợp lệ (ví dụ ticket key là `CHQ-941`):
1. **Tìm kiếm trong Repository hiện tại**:
   ```bash
   gh pr list --search "CHQ-941 assignee:quyetchasqui" --state all --json number,title,url,state,mergedAt
   ```
2. **Mở rộng tìm kiếm toàn bộ Org/Account nếu chưa thấy**:
   Nếu trong repo hiện tại không có PR nào thỏa mãn, chạy command:
   ```bash
   gh search prs "CHQ-941" --assignee quyetchasqui --json number,title,url,state,repository,createdAt,closedAt
   ```
3. **Lọc PR hợp lệ**:
   - Trạng thái PR là `open`.
   - HOẶC trạng thái PR là `merged` VÀ thời gian `mergedAt` nằm trong khoảng `[tu_ngay, den_ngay]`.
4. **Ghép Link PR**:
   - Nếu không có PR thỏa mãn: Để trống `""` hoặc `"-"`.
   - Nếu có 1 PR: Lấy URL PR đó (ví dụ: `https://github.com/org/repo/pull/123`).
   - Nếu có nhiều PR: Ghép các URL PR lại với nhau bằng dấu xuống dòng (`\n`).

---

### 4️⃣ Xuất File Excel (.xlsx)
1. Ghi dữ liệu kết quả thu được ra file JSON tạm tại `/tmp/retrospective_temp.json` với cấu trúc:
   ```json
   [
     {
       "status": "Processing",
       "ticket_id": "CHQ-941",
       "ticket_url": "https://amap.atlassian.net/browse/CHQ-941",
       "link_pr": "https://github.com/org/repo/pull/123",
       "story_point": "3"
     }
   ]
   ```
2. Gọi script Python tạo file Excel:
   ```bash
   python3 /home/tranquyet/.gemini/config/plugins/quyetchasqui/skills/q-xuat-excel-ticket-tuan/scripts/export_excel.py /tmp/retrospective_temp.json storage/KPT/retrospective_report_<YYYYMMDD-tu-ngay>__<YYYYMMDD-den-ngay>.xlsx
   ```

---

### 5️⃣ Báo cáo Kết Quả
- Đảm bảo file Excel đã được tạo thành công tại `storage/KPT/retrospective_report_<YYYYMMDD-tu-ngay>__<YYYYMMDD-den-ngay>.xlsx`.
- In ra đường dẫn file và hiển thị bảng tổng hợp kết quả Markdown ngắn gọn cho user.
