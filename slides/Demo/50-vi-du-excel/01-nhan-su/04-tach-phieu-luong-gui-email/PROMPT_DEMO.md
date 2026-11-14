# CẨM NANG HƯỚNG DẪN DEMO: 04-TACH-PHIEU-LUONG-GUI-EMAIL

## 1. Nỗi Đau & Bài Toán Thực Tế
Sau khi chốt bảng lương tổng, C&B phải tách dòng của từng người để gửi email cá nhân. Làm tay mất 2-3 tiếng và cực kỳ nguy hiểm nếu gửi nhầm.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu gửi nhầm phiếu lương của người có thu nhập 50 triệu cho một bạn nhân viên mới vào lương 8 triệu thì hậu quả nhân sự sẽ thế nào?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Đọc file bang_luong_chot.xlsx. Với mỗi nhân viên, hãy tạo một bảng chi tiết phiếu lương đẹp mắt và tạo bản nháp (Draft) trên Gmail gửi tới địa chỉ email của nhân viên đó với tiêu đề '[Phiếu lương Tháng 10] - [Họ tên]'. Tuyệt đối chỉ gửi thông tin của đúng cá nhân đó.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Quên ghi rõ 'Chỉ tạo bản nháp Draft' có thể khiến AI gửi thư đi ngay lập tức khi chưa qua bước kiểm duyệt của HR.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** Hàng loạt bản nháp Gmail được tạo tự động với nội dung bảng HTML phiếu lương chỉn chu, đúng người đúng địa chỉ email.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Kết hợp Antigravity với Gmail tạo xong hàng chục bản nháp email cá nhân hóa trong 1 phút, an toàn 100% vì vẫn cho người dùng duyệt lại.
