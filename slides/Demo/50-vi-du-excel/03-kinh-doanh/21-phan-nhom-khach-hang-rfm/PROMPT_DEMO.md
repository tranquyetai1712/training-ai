# CẨM NANG HƯỚNG DẪN DEMO: 21-PHAN-NHOM-KHACH-HANG-RFM

## 1. Nỗi Đau & Bài Toán Thực Tế
Có hàng nghìn đơn hàng trong 2 năm qua nhưng không biết ai là khách VIP sắp bỏ đi, ai là khách ngủ đông để kích hoạt lại.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Một khách hàng chi 200 triệu năm ngoái nhưng 9 tháng nay không phát sinh đơn hàng nào, bạn xếp họ vào nhóm khách VIP hay nhóm có Nguy cơ rời bỏ?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Áp dụng mô hình RFM lên file lich_su_don_hang.xlsx: Tính Recency, Frequency, Monetary của từng khách hàng. Chấm điểm và phân nhóm: VIP, Khách trung thành, Có nguy cơ rời bỏ, Khách ngủ đông. Xuất danh sách từng nhóm ra các sheet riêng trong file Phan_khuc_khach_hang_RFM.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không xác định mốc thời gian cố định làm điểm neo tính Recency (Ví dụ ngày 15/11/2026), điểm R sẽ bị thay đổi mỗi lần chạy.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Phan_khuc_khach_hang_RFM.xlsx` có các sheet phân khúc khách hàng kèm điểm số và hành động đề xuất.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Đưa một kỹ thuật phân tích dữ liệu cao cấp (RFM Data Analytics) thành 1 câu lệnh đơn giản cho dân văn phòng.
