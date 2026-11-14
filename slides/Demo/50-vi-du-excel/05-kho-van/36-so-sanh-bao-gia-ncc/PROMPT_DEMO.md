# CẨM NANG HƯỚNG DẪN DEMO: 36-SO-SANH-BAO-GIA-NCC

## 1. Nỗi Đau & Bài Toán Thực Tế
Cần mua 20 mặt hàng vật tư, 3 NCC gửi về 3 file báo giá: chỗ đã gồm VAT, chỗ chưa VAT, chiết khấu khác nhau, rất khó so sánh.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu một NCC báo giá gốc cao hơn 5% nhưng chiết khấu 8%, trong khi NCC khác giá gốc rẻ hơn nhưng không chiết khấu, bên nào thực sự rẻ hơn?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Đọc 3 file báo giá trong thư mục NCC_Quotes. Quy đổi đơn giá các mặt hàng về cùng mặt bằng chưa VAT sau chiết khấu. Tạo bảng Ma trận so sánh giá giữa 3 NCC, tô màu xanh lá cho NCC có giá thấp nhất ở từng món, và đề xuất 2 phương án: mua tối ưu từng món và mua trọn gói 1 NCC rẻ nhất. Xuất ra Ma_tran_so_sanh_bao_gia_NCC.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không quy đổi các báo giá về cùng trạng thái thuế (đều chưa VAT hoặc đều đã VAT), việc so sánh trực tiếp số tiền sẽ làm sai lệch quyết định đấu thầu.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Ma_tran_so_sanh_bao_gia_NCC.xlsx` có bảng so sánh trực quan và đề xuất phương án mua sắm tối ưu.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Tự động chuẩn hóa đơn giá về cùng hệ quy chiếu và lập bảng so sánh báo giá (Bid Tabulation) chuẩn quy trình đấu thầu.
