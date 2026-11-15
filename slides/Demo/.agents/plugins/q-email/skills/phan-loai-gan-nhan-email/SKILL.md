---
name: phan-loai-gan-nhan-email
description: "Tự động quét hòm thư Gmail, phân tích nội dung email bằng AI, tạo & gán nhãn thông minh qua Gmail MCP, đồng thời tự động gửi tin nhắn tóm tắt báo cáo sang Slack qua Slack MCP."
---

# Quy Trình Tự Động Phân Loại, Gán Nhãn Email & Gửi Thông Báo Slack

Hướng dẫn quy trình tự động dành cho Agent để kiểm tra hòm thư Gmail, phân tích nội dung email, tự động gán nhãn (Label) phân loại và gửi thông báo thời gian thực kèm tóm tắt sang kênh Slack thông qua các công cụ Gmail MCP và Slack MCP Server.

---

## I. CÁC BƯỚC THỰC THI (EXECUTION STEPS)

> ⚡ **QUY TẮC TỰ ĐỘNG THỰC THI (AUTONOMOUS EXECUTION - ZERO INTERACTION):**
> - Agent BẮT BUỘC tự động thực hiện liên hoàn từ Bước 1 đến Bước 6 mà **KHÔNG ĐƯỢC DỪNG LẠI HOẶC HỎI XÁC NHẬN** của người dùng.
> - Tự động gọi tool Gmail MCP để kiểm tra, tạo nhãn, gán nhãn và gọi Slack MCP để gửi thông báo ngay lập tức.
> - Chỉ xuất bảng tổng kết ở Bước 6 **SAU KHI ĐÃ GÁN NHÃN VÀ GỬI SLACK THÀNH CÔNG** cho toàn bộ các email trong đợt quét.

Agent thực hiện theo thứ tự 6 bước sau:

### Bước 1: Tìm kiếm Email cần xử lý
- Gọi công cụ Gmail MCP để tìm các email trong hòm thư thỏa mãn điều kiện:
  - Chưa có nhãn `AI_DaPhanLoai` (Query: `-label:AI_DaPhanLoai`).
  - Giới hạn tối đa 20 email gần nhất cho mỗi lượt chạy để đảm bảo hiệu năng.

### Bước 2: Phân tích Nội dung Email & Chọn Nhãn
- Đọc thông tin: **Tiêu đề (Subject)**, **Người gửi (Sender)**, **Nội dung tóm tắt (Snippet/Body)** và danh sách **File đính kèm (Attachments)** nếu có.
- Đọc file quy tắc [quy-tac-gan-nhan.md](../../rules/quy-tac-gan-nhan.md) để đối soát Bộ diện nhãn (Label Taxonomy) và chọn ra Nhãn chính xác nhất.
- Tạo một đoạn **tóm tắt AI 2 câu** nội dung chính của email (làm nổi bật yêu cầu cốt lõi).

### Bước 3: Đảm bảo Nhãn đã tồn tại trên Gmail
- Kiểm tra danh sách nhãn hiện có trên Gmail qua Gmail MCP.
- Nếu nhãn nghiệp vụ cần gán hoặc nhãn kiểm soát `AI_DaPhanLoai` chưa tồn tại trên tài khoản Gmail -> Gọi Gmail MCP tool để tạo nhãn mới trước khi gán.

### Bước 4: Thực hiện Gán Nhãn trên Gmail
- Gọi công cụ Gmail MCP để thêm các nhãn tương ứng vào Email:
  - Nhãn phân loại nghiệp vụ (Ví dụ: `KeToan/HoaDon`, `KinhDoanh/BaoGia`).
  - Nhãn kiểm soát `AI_DaPhanLoai`.

### Bước 5: Gửi Thông Báo Sang Slack qua Slack MCP
- Đọc file quy chuẩn [quy-chuan-slack-notification.md](../../rules/quy-chuan-slack-notification.md) để lấy mẫu cú pháp tin nhắn và quy tắc chọn kênh Slack tương ứng với nhãn đã gán.
- Sử dụng công cụ Slack MCP (`slack_post_message`) để gửi thông báo tóm tắt vào đúng kênh tiếp nhận.

### Bước 6: Báo cáo & Lập Log
- Tổng hợp danh sách các email đã được phân loại và gửi Slack thành công.
- Xuất kết quả ngắn gọn theo dạng bảng:
  | ID Email | Tiêu đề | Người gửi | Nhãn được gán | Trạng thái Slack |
  |---|---|---|---|---|

---

## II. HƯỚNG DẪN THIẾT LẬP CRONJOB TỰ ĐỘNG HÓA NGẦM

Để quy trình này tự động chạy ngầm trên máy Linux mà không cần thao tác bằng tay:

### Cách 1: Thiết lập qua Crontab Linux (Khuyên dùng cho vận hành 24/7)
1. Mở crontab bằng lệnh:
   ```bash
   crontab -e
   ```
2. Thêm dòng sau vào cuối file để hệ thống tự chạy 15 phút/lần:
   ```bash
   */15 * * * * agy run "Sử dụng skill phan-loai-gan-nhan-email để xử lý email mới và bắn thông báo Slack" >> /home/tranquyet/.gemini/antigravity/logs/cron_email.log 2>&1
   ```

### Cách 2: Thiết lập qua lệnh `/schedule` của Antigravity
Chạy lệnh sau trực tiếp trong cửa sổ chat với Agent:
```text
/schedule CronExpression="*/15 * * * *" Prompt="Thực hiện skill phan-loai-gan-nhan-email để phân loại email mới và gửi thông báo Slack"
```
