# Plugin `q-email` - Tự Động Phân Loại, Gán Nhãn Email & Báo Cáo Slack

Plugin tự động hóa quy trình quản trị hộp thư Gmail: phân tích ngữ cảnh email bằng AI, tự động tạo và gán nhãn nghiệp vụ trên Gmail, đồng thời chuyển tiếp tóm tắt kèm liên kết trực tiếp sang kênh Slack nội bộ tương ứng theo thời gian thực.

---

## 📁 Cấu Trúc Thư Mục

```text
q-email/
├── plugin.json                              # Khai báo thông tin plugin
├── README.md                                # Tài liệu hướng dẫn sử dụng plugin
└── skills/
    └── phan-loai-gan-nhan-email/
        └── SKILL.md                         # Quy trình chi tiết của Skill
```

---

## 🎯 Chức Năng Chính

1. **Phân tích ngữ cảnh Email bằng AI**:
   - Đọc tiêu đề, người gửi, đoạn trích và phân tích tập tin đính kèm để nắm bắt nội dung trọng tâm.
   - Tạo đoạn tóm tắt AI ngắn gọn (2 câu) phản ánh đúng vấn đề của email.

2. **Bộ Nhận Diện Nhãn Nghiệp Vụ (Label Taxonomy)**:
   - `KinhDoanh/BaoGia`: Yêu cầu báo giá, hỏi chi phí sản phẩm/dịch vụ.
   - `KinhDoanh/HopTac`: Đề xuất hợp tác kinh doanh, đối tác B2B, tài trợ.
   - `KeToan/HoaDon`: Hóa đơn điện tử (VAT), sao kê tài khoản, chứng từ chi tiêu.
   - `NhanSu/Tuyendung`: Hồ sơ ứng viên, CV, tuyển dụng.
   - `CongNo/ThanhToan`: Nhắc nợ, xác nhận chuyển khoản, hạn mức công nợ.
   - `HanhChinh/ThongBao`: Thông báo hệ thống, gia hạn dịch vụ, bản tin nội bộ.
   - `KhanCap`: Khiếu nại gay gắt từ khách hàng, sự cố hệ thống nghiêm trọng.
   - `QuangCao_Spam`: Email tiếp thị hàng loạt, thư rác.
   - `AI_DaPhanLoai`: Nhãn kiểm soát chống trùng lặp dữ liệu trong các lần quét tiếp theo.

3. **Tự Động Quản Trị Nhãn Trên Gmail**:
   - Kiểm tra nhãn trên tài khoản Gmail qua **Gmail MCP**.
   - Nếu nhãn chưa tồn tại, tự động tạo mới nhãn trước khi gán.
   - Gán đồng thời nhãn phân loại nghiệp vụ và nhãn kiểm soát `AI_DaPhanLoai`.

4. **Điều Hướng & Báo Cáo Thông Minh Sang Slack (Dynamic Channel Routing)**:
   - Tự động kiểm tra danh sách kênh trên Slack và quyền thành viên của Bot:
     - `KhanCap` ➡️ `#urgent` (kèm biểu tượng cảnh báo 🔴)
     - `KinhDoanh/*` ➡️ `#sales`
     - `KeToan/*`, `CongNo/*` ➡️ `#finance`
     - `NhanSu/*` ➡️ `#hr`
     - `HanhChinh/ThongBao` & các loại khác ➡️ `#email-notifications`
   - **Cơ chế Fallback an toàn**: Nếu kênh chuyên biệt chưa tạo hoặc Bot chưa gia nhập kênh, thông báo sẽ tự động gửi về kênh chung (`#all-chas` hoặc kênh General) để đảm bảo không bị thất lạc thông tin.
   - **Lọc thư rác (Anti-noise)**: Email thuộc nhóm `QuangCao_Spam` chỉ được gán nhãn lưu trữ trên Gmail, **không gửi tin nhắn sang Slack** nhằm tránh làm phiền kênh trao đổi của đội ngũ.

5. **Chế Độ Im Lặng (Silent Mode)**:
   - Khi chạy định kỳ nếu hòm thư không phát sinh email mới chưa xử lý, Agent sẽ tự động kết thúc im lặng, không gửi tin nhắn rác.

---

## 🔌 Yêu Cầu Tích Hợp (Prerequisites)

Plugin yêu cầu kết nối với 2 MCP Server đã cấu hình sẵn trong Antigravity:
1. **Gmail MCP**:
   - Các công cụ sử dụng: `search_emails`, `read_email`, `create_label`, `list_email_labels`, `modify_email`.
2. **Slack MCP**:
   - Các công cụ sử dụng: `slack_list_channels`, `slack_post_message`.

---

## 🚀 Hướng Dẫn Sử Dụng

### Cách 1: Kích Hoạt Qua Câu Lệnh Chat Với AI
Bạn có thể ra lệnh trực tiếp trong phiên chat:
```text
"Hãy kiểm tra hộp thư Gmail, phân loại email mới và gửi thông báo tóm tắt sang Slack."
```
hoặc chỉ định rõ mốc thời gian:
```text
"Quét email từ sau ngày 2026/08/22 chưa được phân loại, gán nhãn và gửi sang Slack."
```

---

### Cách 2: Thiết Lập Chạy Tự Động Định Kỳ Với Slash Command `/schedule`
Chạy lệnh trực tiếp trong thanh chat của Antigravity để hẹn giờ định kỳ (ví dụ mỗi 15 phút quét một lần):
```text
/schedule CronExpression="*/15 * * * *" Prompt="Thực hiện skill phan-loai-gan-nhan-email để phân loại email mới và gửi thông báo Slack"
```

---

### Cách 3: Chạy Ngầm 24/7 Bằng Crontab (Linux) Hoặc Task Scheduler (Windows)

#### Trên Linux / macOS:
Mở crontab:
```bash
crontab -e
```
Thêm dòng sau (chạy 15 phút một lần):
```bash
*/15 * * * * agy run "Sử dụng skill phan-loai-gan-nhan-email để xử lý email mới và bắn thông báo Slack" >> ~/.gemini/antigravity/logs/cron_email.log 2>&1
```

#### Trên Windows (PowerShell / Task Scheduler):
Tạo Scheduled Task chạy định kỳ lệnh `agy`:
```powershell
agy run "Sử dụng skill phan-loai-gan-nhan-email để xử lý email mới và bắn thông báo Slack"
```

---

## 📊 Định Dạng Thông Báo & Báo Cáo

### Mẫu Tin Nhắn Gửi Trên Slack:
```text
🚨 [KeToan/HoaDon] - Email mới từ ketoan@doitac.com
📌 Tiêu đề: Hóa đơn điện tử số HD-2026-0881
💡 Tóm tắt AI: Đối tác gửi hóa đơn VAT dịch vụ lưu trữ máy chủ tháng 08/2026, hạn thanh toán ngày 25/08.
🏷️ Nhãn: KeToan/HoaDon
🔗 Xem trực tiếp trên Gmail: https://mail.google.com/mail/u/0/#inbox/18a2bc4d8ef01
```

### Bảng Báo Cáo Tổng Hợp Trong Chat:
| ID Email | Tiêu Đề | Người Gửi | Nhãn Được Gán | Kênh Slack Đã Gửi | Trạng Thái |
|---|---|---|---|---|---|
| `18a2bc4d8ef01` | Hóa đơn điện tử HD-2026-0881 | ketoan@doitac.com | `KeToan/HoaDon` | `#finance` | Thành công |
