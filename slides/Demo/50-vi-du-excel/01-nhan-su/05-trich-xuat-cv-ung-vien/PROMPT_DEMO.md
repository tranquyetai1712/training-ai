# CẨM NANG HƯỚNG DẪN DEMO: 05-TRICH-XUAT-CV-UNG-VIEN

## 1. Nỗi Đau & Bài Toán Thực Tế
Tuyển dụng nhận về hàng chục CV mỗi ngày. Ngồi mở từng CV gõ họ tên, SĐT, kinh nghiệm vào file Excel mất 2-3 tiếng.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Mỗi đợt tuyển dụng các bạn nhận được bao nhiêu CV? Có bao giờ bị hoa mắt gõ nhầm số điện thoại của ứng viên tiềm năng chưa?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Đọc toàn bộ các file CV trong thư mục CV_Ung_Vien. Trích xuất thông tin từng ứng viên gồm: Họ tên, SĐT (chuẩn hóa về dạng 09xx), Email, Vị trí ứng tuyển, Số năm kinh nghiệm, Công ty gần nhất, Học vấn, Kỹ năng chính, và chấm điểm độ phù hợp (thang 100) so với yêu cầu Senior Marketing. Xuất ra file Tracking_Ung_Vien.xlsx sắp xếp từ điểm cao xuống thấp.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không quy định thang điểm cụ thể và tiêu chí chấm điểm (ví dụ: Senior Marketing cần kinh nghiệm Performance, Teamwork), AI sẽ chấm điểm rất cảm tính.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Tracking_Ung_Vien.xlsx` tổng hợp đầy đủ thông tin các ứng viên kèm điểm số và nhận xét tóm tắt.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Biến đống file hồ sơ rời rạc thành bảng Excel quản lý tuyển dụng sạch đẹp chỉ sau 1 câu lệnh.
