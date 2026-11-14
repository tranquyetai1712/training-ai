# CẨM NANG HƯỚNG DẪN DEMO: 20-TINH-HOA-HONG-LUY-TIEN

## 1. Nỗi Đau & Bài Toán Thực Tế
Chính sách hoa hồng bậc thang nhiều tầng rất phức tạp, tháng nào tính thưởng kế toán và sales cũng tranh cãi nhau.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu một sales đạt 115% KPI thì số doanh số vượt 15% sẽ được nhân hoa hồng 5% hay toàn bộ 115% đều được hưởng mức 5%?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Từ file doanh_so_sales_t11.xlsx, hãy tính bảng thưởng hoa hồng tháng 11 cho từng Sales và Team Leader theo chính sách bậc thang: <80% KPI: 0%, 80-100%: 3%, 100-120%: 5%, >120%: 8%; cộng 1.5% cho Team Leader. Chỉ tính trên đơn 'Đã thu tiền'. Xuất ra Bang_tinh_hoa_hong_T11.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không hướng dẫn lọc bỏ đơn 'Chưa thanh toán', nhân viên bán được nhiều đơn ảo chưa thu tiền vẫn được tính thưởng sai quy định.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Bang_tinh_hoa_hong_T11.xlsx` minh bạch rõ ràng số tiền thưởng của từng bậc và thưởng nhóm.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Minh bạch hóa toàn bộ công thức tính thưởng bậc thang, xóa bỏ hoàn toàn tranh cãi giữa Sales và Kế toán.
