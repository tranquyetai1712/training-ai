# CẨM NANG HƯỚNG DẪN DEMO: 03-TINH-LUONG-GROSS-NET-THUE

## 1. Nỗi Đau & Bài Toán Thực Tế
Công thức tính thuế TNCN 7 bậc lũy tiến trên Excel cực kỳ dài và dễ sai khi nhân viên có thay đổi người phụ thuộc và lương OT.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Ai ở đây từng viết công thức tính thuế TNCN 7 bậc bằng 7 hàm IF lồng nhau và bị sót dấu ngoặc đóng chưa?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Dựa vào file du_lieu_luong_thang.xlsx, hãy tính bảng lương hoàn chỉnh: trừ BHXH/BHYT/BHTN (10.5%), trừ giảm trừ gia cảnh bản thân (11 triệu) và người phụ thuộc (4.4 triệu/người), miễn thuế ăn trưa tối đa 730k và phần chênh lệch OT. Tính thuế TNCN 7 bậc và lương Net thực nhận. Chèn công thức Excel vào các cột và lưu vào Bang_luong_chi_tiet_T10.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không nhắc AI về ngưỡng miễn thuế tiền ăn trưa (tối đa 730k) hoặc không dặn chèn Live Formulas, AI có thể chỉ dán số chết (hardcoded static values) làm mất khả năng audit của kế toán.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Bang_luong_chi_tiet_T10.xlsx` có đầy đủ công thức Excel hoạt động tại từng ô, tính đúng từng bậc thuế và lương Net.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Không chỉ điền kết quả tĩnh mà ghi trực tiếp công thức Excel chuẩn vào từng ô để kế toán kiểm tra được.
