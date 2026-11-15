---
name: thu-ky-hop-tu-dong
description: "Nghe file ghi âm cuộc họp (.mp3, .m4a, .wav), lọc bỏ chuyện phiếm, trích xuất quyết định đã chốt và bảng Action Items ra biên bản Markdown; sau đó tự động tạo thẻ việc trên Trello và gửi thông báo tóm tắt sang Slack."
---

# Quy Trình Thư Ký Họp AI: Nghe Audio ➔ Biên Bản ➔ Trello & Slack

Hướng dẫn Agent thực hiện quy trình Thư ký họp thông minh theo 2 giai đoạn, tuân thủ [quy-chuan-bien-ban-hop.md](../../rules/quy-chuan-bien-ban-hop.md) và [quy-chuan-trello-slack.md](../../rules/quy-chuan-trello-slack.md).

---

## GIAI ĐOẠN 1: NGHE GHI ÂM & LẬP BIÊN BẢN HỌP

### Bước 1: Đọc/nghe trực tiếp file ghi âm
- Kiểm tra file âm thanh được chỉ định (ví dụ `cuoc_hop_giao_ban_tuan.mp3`).
- Nhận diện các vai trò phát biểu chính, lọc bỏ chuyện phiếm đầu giờ hoặc lời thoại thừa.

### Bước 2: Trích xuất & Soạn biên bản chuẩn 3 phần
- Trích xuất chính xác:
  1. **Tổng quan cuộc họp** (chủ đề, người chủ trì, thành phần tham dự).
  2. **Các quyết định đã được chốt** (chỉ ghi phần đã thống nhất).
  3. **Bảng Phân Công Hành Động (Action Items)** gồm 4 cột: `Công Việc Cụ Thể`, `Người Phụ Trách`, `Hạn Chót (Deadline)`, `Kết Quả Cần Bàn Giao`.
- Không tự suy diễn thông tin không có trong file ghi âm; nếu thiếu dữ liệu thì ghi rõ vào mục cảnh báo.

### Bước 3: Lưu file biên bản & Trình bày nghiệm thu
- Lưu kết quả ra tệp mới (mặc định `bien_ban_hop_giao_ban.md` cùng thư mục làm việc) và hiển thị tóm tắt để người dùng kiểm tra.

---

## GIAI ĐOẠN 2: ĐỒNG BỘ THẺ TRELLO & BẮN TIN SLACK (KHI NGƯỜI DÙNG YÊU CẦU)

### Bước 4: Tạo thẻ công việc trên Trello qua Trello MCP
- Tìm bảng mục tiêu (ví dụ `Chiến Dịch Tháng 10`) và cột `Cần Làm (To Do)`.
- Tạo lần lượt từng thẻ cho mỗi dòng trong bảng Action Items, điền đầy đủ mô tả, người phụ trách và hạn chót (Due Date).

### Bước 5: Gửi thông báo vào kênh Slack qua Slack MCP
- Định dạng tin nhắn ngắn gọn, rõ ràng theo đúng mẫu tại [quy-chuan-trello-slack.md](../../rules/quy-chuan-trello-slack.md) và gửi vào kênh `#thong-bao-chung` (hoặc kênh được yêu cầu).

### Bước 6: Báo cáo hoàn tất
- Liệt kê các thẻ Trello đã tạo thành công và xác nhận trạng thái tin nhắn đã gửi lên Slack.
