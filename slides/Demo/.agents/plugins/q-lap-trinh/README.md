# Plugin `quyetchasqui` - Hệ Thống Trợ Lý Kỹ Sư Cấp Cao & Tự Động Hóa Toàn Diện

Plugin tổng hợp mạnh mẽ nhất trong hệ thống, cung cấp hơn 40 kỹ năng tự động hóa chuyên sâu (AI Skills), các cơ chế kiểm soát chất lượng tự động (Hooks / Quality Gates), cùng các công cụ quản lý dự án, review code, báo cáo và đồng bộ dữ liệu.

---

## 📁 Cấu Trúc Thư Mục

```text
quyetchasqui/
├── plugin.json                              # Khai báo plugin và cấu hình hooks
├── README.md                                # Tài liệu hướng dẫn sử dụng toàn diện
├── hooks/                                   # Các Hook can thiệp tự động (Quality Gates)
│   ├── hooks.json                           # Cấu hình can thiệp trước lệnh git push
│   ├── check-pr-quality-gate.sh             # Script kiểm tra tiêu chuẩn chất lượng
│   ├── pre-push                             # Git hook pre-push mẫu
│   ├── checks/                              # Các kiểm tra thành phần (linter, tests, rules)
│   └── lib/                                 # Thư viện bash script hỗ trợ
└── skills/                                  # Hơn 40 Skills tự động hóa chuyên biệt
```

---

## 🛡️ Hệ Thống Kiểm Soát Tự Động (Hooks & Quality Gates)

Plugin được trang bị hook can thiệp trước khi đẩy mã nguồn (`PreToolUse` với `git push`):
* **Cơ chế hoạt động**: Khi Agent chuẩn bị chạy lệnh `git push`, script `check-pr-quality-gate.sh` sẽ tự động kích hoạt.
* **Các chốt chặn kiểm tra**:
  1. Kiểm tra dead code, `console.log`, `debugger`, `binding.pry`.
  2. Kiểm tra tính cân bằng thẻ HTML / JSX.
  3. Kiểm tra các rủi ro bảo mật (Brakeman, SQL Injection, Secret leak).
  4. Rà soát chuẩn RuboCop / Linter.
  5. Đảm bảo toàn bộ test case (RSpec) vượt qua 100%.

---

## 🧭 Bản Đồ Phân Loại Kỹ Năng (Skill Taxonomy)

Hơn 40 skills trong plugin được tổ chức thành 6 nhóm nghiệp vụ chính:

### 1. Đánh Giá Mã Nguồn & Kiểm Định Chất Lượng (Code Review & Quality Assurance)
* **`q-code-review` / `code-review-excellence`**: Đánh giá PR đa góc nhìn thông qua các Subagents chạy song song, phân loại nhận xét theo chuẩn **MUST / IMO / NITS**, loại bỏ nhiễu và chấm điểm độ tin cậy.
* **`q-kiem-tra-lan-cuoi-truoc-khi-tao-pull-request`**: Bảng kiểm tra tổng thể cuối cùng (Dead code, Naming, RSpec, Brakeman, Performance, Pagination Guard) xuất 1 báo cáo Markdown duy nhất.
* **`q-kiem-tra-chat-luong-code`**: Rà soát tuân thủ nguyên lý SOLID, bảo mật và các rules trong thư mục `storage/rules/`.
* **`q-tinh-gon-code` / `q-simplify-code`**: Tối ưu hóa code sau khi chạy đúng: giảm độ phức tạp, tăng tái sử dụng, cải thiện hiệu năng.
* **`q-dang-comment-review-pr-nguoi-khac` / `q-post-pr-review-external-author`**: Tự động đăng các inline comments chất lượng lên PR của tác giả khác trên GitHub.
* **`q-phan-hoi-comment-tren-pr` / `q-reply-pr-review-inline-comments`**: Trả lời phản hồi các ý kiến đánh giá trực tiếp trên Pull Request.
* **`q-tu-dong-them-rule-tu-pr-merged-trong-ngay`**: Phân tích comment từ các PR vừa được merge trong ngày để tự động đúc kết thành engineering rule mới nhằm ngăn chặn lỗi lặp lại.

---

### 2. Quản Trị Yêu Cầu & Kế Hoạch Jira (Jira & Agile Planning)
* **`q-tao-jira-ticket` / `q-tao-ticket-jira`**: Phân tích các yêu cầu sơ khai để chia nhỏ thành cấu trúc Epic/Task/Sub-task và tạo trực tiếp lên Jira Cloud.
* **`q-lay-ticket-jira-gan-day`**: Truy xuất các ticket của tài khoản `quyetchasqui` đang ở trạng thái Processing, Review hoặc Done trong 5 ngày gần nhất.
* **`q-uoc-luong-story-point` / `q-uoc-luong-thoi-gian-ticket`**: Phân tích chi tiết rủi ro, độ phức tạp và đưa ra ước lượng thời gian hoàn thành (không đoán mò).
* **`q-ra-soat-ke-hoach-trien-khai` / `q-review-ke-hoach-trien-khai`**: Thẩm định kế hoạch triển khai kỹ thuật trước khi gõ phím viết code.
* **`q-de-xuat-giai-phap-ky-thuat` / `q-proposed_solution`**: Soạn thảo văn bản đề xuất giải pháp kỹ thuật trình cấp quản lý hoặc khách hàng.
* **`q-xuat-excel-ticket-tuan` / `q-retrospective-report`**: Ghép nối mã ticket Jira với link PR GitHub tương ứng, tính tổng Story Point và xuất file Excel (`.xlsx`).

---

### 3. Báo Cáo KPT & Biên Bản Cuộc Họp (KPT Retrospective & Meetings)
* **`q-tao-bao-cao-kpt-tuan` / `q-viet-bao-cao-kpt-tuan`**: Tự động phân tích PR và các review comment nhận được trong tuần để viết báo cáo Keep - Problem - Try, tìm nguyên nhân gốc rễ và đề xuất hành động cải thiện.
* **`q-tao-khung-kpt-tu-jira` / `q-phan-tich-pr-viet-kpt`**: Trích xuất dữ liệu thô từ Jira và GitHub để tạo template báo cáo KPT sẵn sàng.
* **`q-viet-bien-ban-cuoc-hop`**: Chuyển đổi các ghi chú thô sơ sài thành biên bản cuộc họp chuyên nghiệp chuẩn cấu trúc, hỗ trợ xuất định dạng Markdown và `.docx`.

---

### 4. Phân Tích Nghiệp Vụ & Tài Liệu Hóa (Business Analysis & Docs)
* **`q-phan-tich-luong-hoat-dong-pm` / `q-phan-tich-luong-nghiep-vu`**: Đọc mã nguồn thực tế để dựng lại luồng nghiệp vụ chi tiết dưới góc nhìn Project Manager (PM), tối ưu hóa hoàn toàn cho **NotebookLM** (Podcast Audio Overview, Q&A, Study Guide).
* **`q-cap-nhat-mo-ta-pr` / `q-update-pull-request`**: Tự động cập nhật tiêu đề và nội dung PR trên GitHub sau các lần refactor/cập nhật code.

---

### 5. Tự Động Hóa Vận Hành & Đồng Bộ (Operations & Sync)
* **`q-tu-dong-phan-bo-cong-viec-tren-trello`**: Phân tích danh sách công việc thô, tự động tạo thẻ Trello với đầy đủ nhãn màu, checklist và link Jira trên bảng *My Daily Hub*.
* **`q-crawler-email-automation` / `q-thu-thap-email-doan-hoi`**: Thu thập dữ liệu liên hệ công khai (Email, Hotline, Fanpage, Zalo) của các tổ chức sinh viên trên cả nước và xuất file Excel.
* **`q-sync-agents` / `q-dong-bo-agents`**: Đồng bộ 3 chiều các AI Agents và Workflows giữa Gemini, Copilot và Antigravity.
* **`q-sync-storage` / `q-dong-bo-storage`**: Đồng bộ hóa thư mục `storage/` giữa các dự án có chung tiền tố.

---

### 6. Trợ Lý Cá Nhân & Trình Chiếu (Personal Assistant & Slides)
* **`q-tao-slide-bai-giang`**: Thiết kế và sinh slide trình chiếu tương tác chất lượng cao (Single-file HTML 0-dependency) tích hợp ngăn kéo kịch bản người thuyết trình (Speaker Notes Drawer).
* **`q-daily-greeting` / `q-chao-buoi-sang-agent`**: Tự động gửi thông điệp chào buổi sáng 5:00 AM tới Antigravity CLI.

---

## 🚀 Hướng Dẫn Sử Dụng Nhanh

### 1. Code Review Đa Chiều Cho PR:
```text
"Sử dụng skill q-code-review để đánh giá Pull Request #45 và phân loại theo MUST/IMO/NITS."
```

### 2. Kiểm Tra Chất Lượng Trước Khi Tạo PR:
```text
"Chạy skill q-kiem-tra-lan-cuoi-truoc-khi-tao-pull-request để rà soát toàn bộ nhánh hiện tại."
```

### 3. Tạo Báo Cáo KPT Tuần Tự Động:
```text
"Sử dụng skill q-viet-bao-cao-kpt-tuan để tạo báo cáo tuần này từ các ticket Jira và PR đã thực hiện."
```

### 4. Phân Bổ Công Việc Lên Trello:
```text
"Sử dụng skill q-tu-dong-phan-bo-cong-viec-tren-trello để phân bổ các việc sau: Fix comment CHQ-865(Halo), Review CHQ-1055(Halo)."
```
