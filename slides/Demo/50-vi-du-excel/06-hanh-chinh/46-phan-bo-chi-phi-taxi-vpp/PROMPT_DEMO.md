# CẨM NANG HƯỚNG DẪN DEMO: 46-PHAN-BO-CHI-PHI-TAXI-VPP

## 1. Nỗi Đau & Bài Toán Thực Tế
Nhận bảng kê Grab for Business hàng trăm cuốc xe, Admin phải ngồi tra từng người thuộc phòng ban nào để phân bổ chi phí và tìm xem ai đi việc riêng ngoài giờ.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Một cuốc xe Grab lúc 23h15 đêm Chủ Nhật từ quán bar về nhà riêng nhưng ghi chú 'Gặp đối tác', bạn sẽ duyệt thanh toán hay yêu cầu giải trình bổ sung mã dự án?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Kết hợp bảng kê Grab trong bang_ke_taxi.xlsx và danh sách nhan_su.xlsx. Hãy ánh xạ từng chuyến xe về đúng Phòng ban, tổng hợp chi phí theo từng bộ phận, và lọc riêng các chuyến xe sau 22h đêm hoặc ngày Chủ Nhật ra sheet Canh_Bao_Ngoai_Gio trong file Phan_bo_chi_phi_Grab_T10.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không xử lý trùng tên nhân viên bằng Mã nhân viên hoặc chức danh, các chuyến xe của nhân viên trùng tên sẽ bị gán sai phòng ban chịu phí.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Phan_bo_chi_phi_Grab_T10.xlsx` phân bổ chi phí chuẩn xác về từng phòng ban và khoanh vùng các cuốc xe nghi vấn đi việc riêng.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Tự động gán Cost Center và lọc ngay các cuốc xe ngoài giờ trong 5 giây.
