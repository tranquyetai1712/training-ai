# CẨM NANG HƯỚNG DẪN DEMO: 25-THEO-DOI-PACING-RUNRATE-SALES

## 1. Nỗi Đau & Bài Toán Thực Tế
Đang ở giữa tháng, giám đốc kinh doanh muốn biết cuối tháng ai dự kiến đạt KPI, ai cần tăng tốc bao nhiêu tiền mỗi ngày còn lại.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Hôm nay là ngày 18 của tháng có 26 ngày làm việc, một sales mới đạt 42% chỉ tiêu thì mỗi ngày còn lại bạn ấy phải bán gấp mấy lần tốc độ hiện tại?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Kết hợp file doanh_so_luy_ke.xlsx (tính đến ngày 18/11, tháng có 26 ngày làm việc). Hãy tính: % Hoàn thành hiện tại, Dự phóng cuối tháng (Run-rate), và Số tiền cần đạt mỗi ngày trong 8 ngày làm việc còn lại để cán đích 100% KPI. Định dạng màu sắc cảnh báo vào file Bao_cao_pacing_sales_T11.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu chia đều theo tổng số ngày trong tháng (30 ngày) thay vì số ngày làm việc thực tế (26 ngày, trừ Chủ nhật), mục tiêu ngày sẽ bị tính thấp hơn thực tế.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Bao_cao_pacing_sales_T11.xlsx` chỉ rõ từng nhân viên đang chạy trước hay chậm hơn tiến độ kèm chỉ tiêu ngày.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Tạo báo cáo quản trị điều hành sắc bén kèm icon đèn giao thông chỉ trong 1 câu lệnh.
