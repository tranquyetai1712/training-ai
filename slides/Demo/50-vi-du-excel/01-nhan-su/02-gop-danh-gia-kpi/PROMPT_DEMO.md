# CẨM NANG HƯỚNG DẪN DEMO: 02-GOP-DANH-GIA-KPI

## 1. Nỗi Đau & Bài Toán Thực Tế
Mỗi phòng ban gửi 1 file KPI cấu trúc cột hơi lệch nhau. HR phải mở từng file copy-paste thủ công và dễ nhầm thứ tự cột.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu cột ở file Kỹ thuật ghi là 'ID', còn file Kinh doanh ghi là 'Mã NV', khi dùng Power Query hoặc copy paste thông thường chuyện gì sẽ xảy ra?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Quét toàn bộ các file Excel trong thư mục KPI_2026. Dù tên cột giữa các file có hơi khác nhau (ví dụ: 'Mã NV'/'ID', 'Điểm KPI'/'Tổng điểm'), hãy tự động nhận diện và ánh xạ về chuẩn chung gồm: Mã NV, Họ tên, Phòng ban, Điểm Q1, Điểm Q2, Điểm Q3, Điểm Q4, Điểm trung bình năm. Gộp tất cả vào file Tong_hop_KPI_Nam_2026.xlsx và tự động xếp loại A/B/C/D theo thang điểm.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không yêu cầu rõ 'bảo toàn tên phòng ban xuất xứ', AI có thể gộp dữ liệu nhưng bỏ quên cột nhận diện phòng ban của nhân viên.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Tong_hop_KPI_Nam_2026.xlsx` chứa đầy đủ nhân sự từ tất cả các phòng ban, chuẩn hóa cột thống nhất và có cột xếp loại tự động.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> AI tự hiểu ngữ nghĩa của các cột khác tên nhau để gộp chính xác mà không báo lỗi như Power Query hay VBA.
