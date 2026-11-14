# CẨM NANG HƯỚNG DẪN DEMO: 49-XEP-SO-DO-BAN-TIEC-CHECKIN

## 1. Nỗi Đau & Bài Toán Thực Tế
Tổ chức hội nghị hàng trăm khách mời, Admin phải xếp bàn tiệc sao cho người cùng ngành ngồi với nhau và thống kê suất ăn chay/mặn cho nhà hàng rất dễ nhầm.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu một bàn tiệc 10 người có 2 khách ăn chay, bạn sẽ đặt menu với nhà hàng như thế nào để phục vụ chuẩn xác đến đúng ghế ngồi?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Dựa vào khach_moi_su_kien.xlsx, hãy tạo Mã Check-in duy nhất cho từng khách, xếp khách vào các bàn tiệc (Bàn 1 cho VIP, các bàn còn lại gom theo ngành nghề). Thống kê số suất ăn chay/mặn từng bàn để báo nhà hàng và xuất file So_do_ban_tiec_va_checkin.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu xếp lẫn lộn khách VIP ngồi chung với khách tiêu chuẩn mà không theo dõi phân nhóm, sự kiện sẽ mất tính trang trọng và vi phạm quy chuẩn lễ tân.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `So_do_ban_tiec_va_checkin.xlsx` có sơ đồ phân bàn tiệc hợp lý và số lượng suất ăn chay/mặn chuẩn xác.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Giải quyết trọn gói bài toán hậu cần sự kiện rắc rối của dân Hành chính - Sự kiện.
