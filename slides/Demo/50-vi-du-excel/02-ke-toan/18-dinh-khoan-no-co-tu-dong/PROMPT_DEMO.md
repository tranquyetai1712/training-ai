# CẨM NANG HƯỚNG DẪN DEMO: 18-DINH-KHOAN-NO-CO-TU-DONG

## 1. Nỗi Đau & Bài Toán Thực Tế
Kế toán dịch vụ hoặc nhân viên mới phải ngồi gõ tay Tài khoản Nợ / Có cho hàng trăm dòng sao kê ngân hàng trước khi import vào phần mềm MISA.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Với giao dịch 'Rút séc tiền gửi ngân hàng về nhập quỹ tiền mặt', tài khoản nào ghi Nợ và tài khoản nào ghi Có theo Thông tư 200?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Đọc file giao_dich_raw.xlsx. Dựa vào cột Nội dung diễn giải (ví dụ: 'Thanh toán tiền điện T10', 'Thu tiền khách hàng ABC', 'Trả lương NV T10', 'Nộp BHXH'), hãy tự động điền Tài khoản Nợ và Tài khoản Có tương ứng theo Thông tư 200, sau đó định dạng lại đúng chuẩn file import phần mềm MISA vào file Giao_dich_da_dinh_khoan_import_misa.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không xác định rõ giao dịch là tiền mặt (111) hay tiền gửi ngân hàng (112), AI có thể gán nhầm sang 1111 dù chứng từ ghi rõ 'UNC/Chuyển khoản'.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Giao_dich_da_dinh_khoan_import_misa.xlsx` với 100% các dòng giao dịch đã được định khoản Nợ/Có chuẩn chỉnh sẵn sàng import.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> AI đọc hiểu tiếng Việt tự nhiên trong diễn giải giao dịch để tự định khoản kế toán như một kế toán viên kinh nghiệm.
