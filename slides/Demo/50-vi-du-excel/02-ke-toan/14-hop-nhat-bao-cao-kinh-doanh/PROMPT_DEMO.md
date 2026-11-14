# CẨM NANG HƯỚNG DẪN DEMO: 14-HOP-NHAT-BAO-CAO-KINH-DOANH

## 1. Nỗi Đau & Bài Toán Thực Tế
Công ty có nhiều chi nhánh gửi báo cáo doanh thu chi phí riêng biệt. Kế toán trưởng phải mở từng tab gom số lên báo cáo tổng rất dễ sai sót.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu một chi nhánh doanh thu cao gấp 3 chi nhánh khác nhưng tỷ suất lợi nhuận ròng chỉ đạt 5% so với 18% của chi nhánh nhỏ, chi nhánh nào đang hoạt động hiệu quả hơn?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Đọc toàn bộ file báo cáo của các chi nhánh trong thư mục Chi_Nhanh. Hãy tổng hợp số liệu Doanh thu, Giá vốn, Chi phí bán hàng, Chi phí quản lý và Lợi nhuận ròng của từng chi nhánh vào file Bao_cao_PL_Hop_Nhat_T10.xlsx, thêm cột Tổng công ty và cột % Biên lợi nhuận ròng, xếp hạng chi nhánh có tỷ suất sinh lời cao nhất.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu các chi nhánh đặt tên dòng chi tiêu hơi lệch nhau (ví dụ 'Chi phí QLDN' vs 'Chi phí quản lý'), AI cần có bước chuẩn hóa chỉ tiêu trước khi SUM.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Bao_cao_PL_Hop_Nhat_T10.xlsx` với cấu trúc cột đa chi nhánh, tổng cộng toàn công ty và biểu đồ so sánh lợi nhuận.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Chỉ 1 câu lệnh hợp nhất toàn bộ số liệu P&L từ nhiều chi nhánh thành báo cáo tài chính quản trị hoàn chỉnh.
