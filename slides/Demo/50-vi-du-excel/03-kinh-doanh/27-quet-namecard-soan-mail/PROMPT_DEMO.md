# CẨM NANG HƯỚNG DẪN DEMO: 27-QUET-NAMECARD-SOAN-MAIL

## 1. Nỗi Đau & Bài Toán Thực Tế
Đi hội thảo về cầm 30 tấm danh thiếp, ngồi gõ từng thông tin vào Excel rồi gửi thư chào hỏi mất cả buổi sáng.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Sau khi dự hội thảo kết nối đối tác, trong vòng bao lâu bạn nên gửi email chào hỏi để đối phương còn nhớ đến bạn?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Đọc toàn bộ file danh thiếp trong thư mục Namecards. Trích xuất thông tin từng người ra file Danh_ba_doi_tac_hoi_thao.xlsx gồm: Họ tên, Chức vụ, Công ty, SĐT, Email. Đồng thời tạo mẫu thư chào hỏi kết nối sau sự kiện được cá nhân hóa theo Tên và Chức vụ của từng người.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không hướng dẫn bóc tách riêng Họ và Tên đệm với Tên gọi (First Name), email chào hỏi sẽ dùng cả họ lẫn tên một cách gượng gạo (Ví dụ 'Kính gửi Anh Nguyễn Tiến Đạt').

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Danh_ba_doi_tac_hoi_thao.xlsx` và các bản thư kết nối đối tác được chuẩn bị sẵn sàng.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Biến ảnh/chữ trên danh thiếp thành bảng dữ liệu khách hàng và thư chào hàng cá nhân hóa chỉ trong chớp mắt.
