# CẨM NANG HƯỚNG DẪN DEMO: 04-TACH-PHIEU-LUONG-GUI-EMAIL

## 1. Nỗi Đau & Bài Toán Thực Tế
Sau khi chốt bảng lương tổng nhiều cột phụ cấp và khấu trừ, C&B phải tách phiếu lương chuẩn format công ty cho từng người để gửi email cá nhân. Làm tay mất 2-3 tiếng và cực kỳ nguy hiểm nếu gửi nhầm.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu gửi nhầm phiếu lương của người có thu nhập 34 triệu cho một bạn nhân viên khác thì hậu quả nhân sự sẽ thế nào?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Đọc file bang_luong_chot.xlsx. Với mỗi nhân viên, hãy tách ra một file Excel phiếu lương cá nhân trong thư mục Phieu_Luong_Ca_Nhan/ theo đúng cấu trúc, màu sắc và công thức sống của file mẫu _ket_qua_mau_chuan.xlsx; đồng thời tạo bản nháp (Draft) trên Gmail gửi tới đúng email của nhân viên đó với tiêu đề '[Phiếu Lương Tháng 10/2026] - [Họ và Tên] - [Mã NV]' kèm bảng HTML chi tiết đầy đủ các khoản thu nhập và khấu trừ.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Quên ghi rõ 'Chỉ tạo bản nháp Draft' có thể khiến AI gửi thư đi ngay lập tức khi chưa qua bước kiểm duyệt của HR.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** Thư mục Phieu_Luong_Ca_Nhan/ chứa 4 file Excel phiếu lương chuẩn format PAYROLL SLIP, cùng 4 bản nháp Gmail được tạo tự động đúng người, đúng email.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Kết hợp Antigravity với Gmail tích hợp sẵn: tách xong phiếu lương chuẩn thiết kế công ty và tạo hàng loạt bản nháp email cá nhân hóa trong 1 phút, an toàn 100% vì vẫn cho HR duyệt lại.
