# CẨM NANG HƯỚNG DẪN DEMO: 42-KIEM-KE-KHO-LECH-THUC-TE

## 1. Nỗi Đau & Bài Toán Thực Tế
Kiểm kê xong có nhiều phiếu đếm tay rời rạc, cộng gộp lại so với phần mềm ERP rất dễ rối, không tìm ra nguyên nhân lệch.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu kiểm kê thấy Áo Polo size M thừa 5 cái còn Áo Polo size L thiếu đúng 5 cái, nguyên nhân phổ biến nhất trong vận hành kho là gì?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Đối chiếu kết quả đếm kho kiem_ke_ke_1.xlsx với tồn sổ sách ton_erp.xlsx. Tính số lượng Thừa/Thiếu cho từng mã hàng, phân tích nguyên nhân nghi ngờ (đặc biệt là lỗi xuất nhầm chéo size/mã giữa 2 sản phẩm tương đồng). Xuất file Bien_ban_kiem_ke_xu_ly_chenh_lech.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu gom nhóm kiểm kê mà không gộp chung các dòng cùng mã hàng nhưng nằm ở các vị trí kệ kho khác nhau (Multi-bin storage), số lượng thực đếm sẽ bị thiếu hụt giả tạo.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Bien_ban_kiem_ke_xu_ly_chenh_lech.xlsx` chỉ rõ số lượng chênh lệch và phát hiện chính xác ca xuất nhầm chéo size.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Điểm thông minh vượt trội: AI phát hiện được lỗi xuất nhầm chéo mã (Áo size M thừa 5 cái, Áo size L thiếu đúng 5 cái).
