# Quy Chuẩn Đồng Bộ Thẻ Trello & Thông Báo Slack Sau Cuộc Họp

Tài liệu quy định cách ánh xạ từ bảng Action Items sang Trello và Slack cho plugin `q-thu-ky-hop`.

---

## I. QUY TẮC TẠO THẺ TRELLO (QUA TRELLO MCP)
1. **Bảng đích mặc định:** `Chiến Dịch Tháng 10` (hoặc bảng người dùng chỉ định).
2. **Cột đích mặc định:** `Cần Làm (To Do)`.
3. **Cấu trúc mỗi thẻ Trello:**
   - **Tiêu đề thẻ:** Tên công việc cụ thể + `[Tên Người Phụ Trách]`
   - **Mô tả (Description):** Ghi rõ Người phụ trách chính, Kết quả cần bàn giao và nguồn từ biên bản cuộc họp.
   - **Ngày hết hạn (Due Date):** Gắn đúng hạn chót đã chốt trong biên bản.

---

## II. ĐỊNH DẠNG TIN NHẮN SLACK (QUA SLACK MCP)
Gửi 1 tin nhắn tóm tắt gọn gàng vào kênh `#thong-bao-chung` (hoặc kênh phòng ban được chỉ định):

```text
🔔 *[THÔNG BÁO GIAO BAN ĐẦU TUẦN - CHIẾN DỊCH 25/10]*
📌 *Quyết định đã chốt:*
• {Quyết_Định_1}
• {Quyết_Định_2}

✅ *Phân công thực hiện:*
• *{Người_Phụ_Trách_1}:* {Công_Việc_1} (Hạn: {Deadline_1})
• *{Người_Phụ_Trách_2}:* {Công_Việc_2} (Hạn: {Deadline_2})
• *{Người_Phụ_Trách_3}:* {Công_Việc_3} (Hạn: {Deadline_3})
```
