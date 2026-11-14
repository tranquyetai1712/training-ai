# CẨM NANG HƯỚNG DẪN DEMO: 37-CANH-BAO-REORDER-POINT

## 1. Nỗi Đau & Bài Toán Thực Tế
Nhân viên mua hàng đặt hàng theo cảm tính: mã bán chạy thì đứt kho mất doanh số, mã bán chậm thì đọng vốn.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu một mã hàng mỗi ngày bán 10 cái, nhà cung cấp mất 10 ngày để giao hàng và cần giữ tồn an toàn 7 ngày bán, điểm đặt hàng lại (ROP) là bao nhiêu cái?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Từ file ton_kho_toc_do_ban.xlsx, hãy tính tốc độ tiêu thụ/ngày, mức tồn kho an toàn (7 ngày bán), và Điểm đặt hàng lại (ROP). Lọc các mã hàng cần đặt ngay hôm nay và tính số lượng cần đặt để đủ bán trong 45 ngày (làm tròn theo MOQ). Xuất file Ke_hoach_dat_hang_ROP.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không cộng lượng 'Hàng đang về trên đường' (In-transit Stock) vào lượng tồn hiệu dụng, bạn sẽ đặt hàng trùng lặp và gây dư thừa tồn kho gấp đôi.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Ke_hoach_dat_hang_ROP.xlsx` chỉ rõ mã nào cần đặt ngay và số lượng đặt chuẩn xác theo quy cách MOQ.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Biến bảng tính tồn kho tĩnh thành hệ thống hoạch định nhu cầu mua hàng thông minh (MRP thu nhỏ).
