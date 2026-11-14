# CẨM NANG HƯỚNG DẪN DEMO: 15-PHAT-HIEN-GIAN-LAN-CHI-PHI

## 1. Nỗi Đau & Bài Toán Thực Tế
Duyệt bảng kê chi phí hàng nghìn dòng, kế toán rất khó phát hiện các hóa đơn bị thanh toán trùng, hoặc nhân viên cố tình tách nhỏ hóa đơn để lách duyệt tiền mặt.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu hai nhân viên ở hai phòng ban khác nhau nộp cùng một số hóa đơn để thanh toán hoàn ứng cách nhau 1 tuần, làm sao kế toán phát hiện kịp trước khi chuyển tiền?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Kiểm toán file de_nghi_thanh_toan_q3.xlsx: Tìm và đánh dấu các dòng có dấu hiệu rủi ro: (1) Trùng số hóa đơn + MST nhà cung cấp dù khác người đề nghị, (2) Hóa đơn từ 20 triệu trở lên thanh toán Tiền mặt, (3) Cùng 1 nhân viên thanh toán nhiều hóa đơn cùng 1 NCC trong 1 ngày tổng trên 20 triệu (nghi vấn tách hóa đơn). Xuất báo cáo ra file Bao_cao_kiem_toan_chi_phi_Q3.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu chỉ so khớp số hóa đơn mà không kèm MST người bán, AI có thể báo sai trùng lặp giữa 2 nhà cung cấp khác nhau nhưng tình cờ trùng số HĐ 0012.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Bao_cao_kiem_toan_chi_phi_Q3.xlsx` chỉ đích danh các khoản thanh toán trùng lặp và các giao dịch vi phạm quy chế tài chính.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Biến AI thành Kiểm toán viên nội bộ rà soát 100% giao dịch trong vài giây thay vì chỉ chọn mẫu ngẫu nhiên.
