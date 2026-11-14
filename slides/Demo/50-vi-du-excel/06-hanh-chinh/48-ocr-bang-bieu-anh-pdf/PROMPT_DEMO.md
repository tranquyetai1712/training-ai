# CẨM NANG HƯỚNG DẪN DEMO: 48-OCR-BANG-BIEU-ANH-PDF

## 1. Nỗi Đau & Bài Toán Thực Tế
Đối tác gửi báo cáo dạng ảnh scan hoặc PDF không copy được chữ, phải gõ tay lại vào Excel mất hàng giờ và dễ nhầm số.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Bao nhiêu bạn từng gặp trường hợp tài liệu giấy in có dấu đỏ của sếp nhưng dòng 'Tổng cộng' bên dưới bị cộng sai 200.000đ do người lập gõ tay máy tính cầm tay?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Đọc bảng số liệu trong bang_scan_du_lieu.txt. Chuyển toàn bộ sang file Excel Bang_so_lieu_chuyen_doi_OCR.xlsx, chuyển các con số về đúng định dạng Number và tự động dùng hàm SUM kiểm tra lại dòng Tổng cộng xem bản gốc có cộng sai không.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu các con số bị lưu dưới dạng Text (có dấu phẩy ngăn cách hàng nghìn dạng chuỗi), hàm SUM sẽ trả về 0 nếu không được chuyển kiểu dữ liệu.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Bang_so_lieu_chuyen_doi_OCR.xlsx` có bảng số liệu chuẩn chỉ và ghi chú phát hiện bản gốc giấy bị cộng lệch số.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Không chỉ chuyển ảnh thành bảng Excel mà còn tự kiểm tra xem tài liệu gốc trên giấy có cộng sai số không.
