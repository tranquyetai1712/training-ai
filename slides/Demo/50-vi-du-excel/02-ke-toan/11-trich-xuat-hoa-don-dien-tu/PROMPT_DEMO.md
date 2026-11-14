# CẨM NANG HƯỚNG DẪN DEMO: 11-TRICH-XUAT-HOA-DON-DIEN-TU

## 1. Nỗi Đau & Bài Toán Thực Tế
Kế toán phải mở từng hóa đơn PDF/XML gõ lại tay Số HĐ, Ngày, MST, Tiền hàng, Tiền thuế vào bảng kê rất mất thời gian.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Bao nhiêu bạn ở đây từng bị cơ quan thuế phạt vì kê khai sai lệch 1 chữ số trong Mã Số Thuế do gõ tay từ hóa đơn giấy/ảnh?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Quét tất cả hóa đơn trong thư mục Hoa_Don. Trích xuất thông tin từng hóa đơn gồm: Số HĐ, Ngày lập, Tên đơn vị bán, Mã số thuế, Mặt hàng, Tiền chưa thuế, Thuế suất GTGT, Tiền thuế, Tổng thanh toán. Kiểm tra xem Tiền chưa thuế + Tiền thuế có khớp Tổng thanh toán không. Xuất ra file Bang_ke_mua_vao_T10.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu hóa đơn áp dụng thuế suất giảm (8%) mà không hướng dẫn AI kiểm tra trường thuế suất riêng biệt, AI có thể mặc định tính thuế 10%.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Bang_ke_mua_vao_T10.xlsx` chuẩn kê khai thuế, tự động đối chiếu cộng trừ và cảnh báo nếu hóa đơn bị lệch số học.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Tự động bóc tách hóa đơn và tích hợp luôn bước kiểm toán chéo số học (Cross-audit validation).
