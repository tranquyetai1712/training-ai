# CẨM NANG HƯỚNG DẪN DEMO: 16-CHUYEN-SO-THANH-CHU

## 1. Nỗi Đau & Bài Toán Thực Tế
Excel mặc định không có hàm đọc số thành chữ tiếng Việt. Người dùng thường phải cài Add-in lạ dễ dính virus hoặc lỗi font tiếng Việt.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Theo chuẩn kế toán Việt Nam, con số 2.500.000.000 đọc là 'Hai tỷ năm trăm triệu đồng' hay 'Hai tỷ năm trăm triệu đồng chẵn'?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Đọc file danh_sach_phieu_chi.xlsx. Thêm 2 cột mới: 'Bằng chữ (Tiếng Việt)' và 'In Words (English)' đọc chính xác số tiền ở cột Số tiền theo đúng chuẩn kế toán (viết hoa chữ đầu, có chữ 'đồng chẵn' ở cuối). Xuất ra file Danh_sach_phieu_chi_chuan.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không quy định 'viết hoa chữ cái đầu', AI có thể trả về chuỗi viết thường toàn bộ làm giảm tính trang trọng của chứng từ kế toán.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Danh_sach_phieu_chi_chuan.xlsx` có đầy đủ 2 cột đọc số thành chữ song ngữ chuẩn chỉnh cho tất cả các con số hàng trăm triệu, hàng tỷ.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Không cần cài bất kỳ Add-in hay viết code VBA nào mà vẫn có cột đọc số thành chữ chuẩn xác cả tiếng Việt lẫn tiếng Anh.
