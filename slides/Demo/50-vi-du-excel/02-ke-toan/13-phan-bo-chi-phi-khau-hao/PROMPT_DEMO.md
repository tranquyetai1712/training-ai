# CẨM NANG HƯỚNG DẪN DEMO: 13-PHAN-BO-CHI-PHI-KHAU-HAO

## 1. Nỗi Đau & Bài Toán Thực Tế
Theo dõi hàng trăm công cụ dụng cụ mua ở các ngày khác nhau trong tháng rất dễ tính sai số ngày sử dụng thực tế của tháng đầu tiên.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu mua 10 dàn máy vi tính ngày 12/03/2026, trong tháng 3 bạn sẽ tính phân bổ trọn tháng hay tính chính xác theo 20 ngày còn lại?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Từ file danh_muc_tscd_242.xlsx, hãy lập bảng tính phân bổ chi phí từng tháng cho cả năm 2026: tháng đầu tiên tính phân bổ theo số ngày thực tế sử dụng trong tháng, các tháng tiếp theo phân bổ tròn tháng, đảm bảo không phân bổ vượt quá Nguyên giá. Xuất ra file Bang_phan_bo_chi_phi_2026.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không hướng dẫn rõ quy tắc 'Ngày trong tháng - Ngày bắt đầu + 1', AI có thể tính thiếu 1 ngày sử dụng thực tế trong tháng đầu.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Bang_phan_bo_chi_phi_2026.xlsx` với 12 cột cho 12 tháng trong năm, xử lý mượt mà ngày lẻ tháng đầu và giá trị còn lại.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Xử lý gọn gàng bài toán phân bổ chi phí ngày lẻ tháng đầu và tháng cuối vốn là nỗi ám ảnh khi viết hàm Excel.
