# Quy Chuẩn Gửi Thông Báo Slack Cho Email

Tài liệu này định nghĩa cấu trúc nội dung tin nhắn và nguyên tắc ánh xạ kênh Slack khi gửi thông báo phân loại email thuộc plugin `q-email`.

---

## I. ĐỊNH DẠNG TIN NHẮN (MESSAGE FORMAT)

Khi gửi thông báo email sang Slack qua Slack MCP (`slack_post_message`), Agent BẮT BUỘC tuân thủ đúng định dạng chuẩn:

```text
🚨 *[{TÊN_NHÃN}]* - Email mới từ *{Người_Gửi}*
📌 *Tiêu đề:* {Tiêu_Đề}
💡 *Tóm tắt AI:* {Nội_Dung_Tóm_Tắt_2_Câu}
🏷️ *Nhãn:* `{Tên_Nhãn}`
🔗 <https://mail.google.com/mail/u/0/#inbox/{ID_Email}|Xem trực tiếp trên Gmail>
```

*Lưu ý:*
- `{Nội_Dung_Tóm_Tắt_2_Câu}`: Tóm tắt súc tích nội dung chính của email trong tối đa 2 câu, làm nổi bật yêu cầu hoặc vấn đề quan trọng.
- `{TÊN_NHÃN}`: Tên nhãn nghiệp vụ chính được gán (Ví dụ: `KinhDoanh/BaoGia`, `KhanCap`).

---

## II. QUY TẮC ÁNH XẠ KÊNH SLACK (CHANNEL MAPPING)

Dựa vào nhãn nghiệp vụ đã gán, Agent định tuyến tin nhắn vào kênh Slack tương ứng:

| Nhóm Nhãn | Kênh Ưu Tiên | Kênh Fallback | Lưu ý |
| :--- | :--- | :--- | :--- |
| **`KhanCap`** | `#urgent` | `#general` | Kèm emoji 🔴 KHẨN CẤP |
| **`KinhDoanh/*`** | `#sales` | `#general` | Dành cho báo giá, hợp tác |
| **`KeToan/*`**, **`CongNo/*`** | `#finance` | `#general` | Dành cho hóa đơn, công nợ |
| **`NhanSu/*`** | `#hr` | `#general` | Dành cho ứng tuyển, CV |
| **Các nhãn còn lại** | `#email-notifications` | `#general` | Mặc định |
