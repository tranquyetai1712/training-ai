# CẨM NANG HƯỚNG DẪN DEMO: 30-TAO-LINK-UTM-TRACKING-QR

## 1. Nỗi Đau & Bài Toán Thực Tế
Gắn tham số UTM thủ công cho 50 bài đăng của 10 KOLs rất dễ gõ nhầm dấu cách hoặc chữ hoa/thường làm hỏng báo cáo Google Analytics.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu tên chiến dịch là 'Khuyến Mãi Mùa Thu 2026', đường dẫn UTM campaign chuẩn mực nên là gì để Google Analytics không bị phân mảnh số liệu?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Đọc file ke_hoach_content.xlsx. Tự động chuẩn hóa Tên chiến dịch, Kênh, Tên KOL về chữ thường không dấu nối bằng dấu gạch ngang, ghép thành đường dẫn Full UTM URL hoàn chỉnh và tạo thêm công thức tạo mã QR. Xuất ra file Ke_hoach_UTM_Tracking_Chuan.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không xử lý ký tự khoảng trắng thành dấu gạch ngang, đường link sẽ sinh ra các ký tự '%20' lộn xộn và dễ bị lỗi khi quét mã QR.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Ke_hoach_UTM_Tracking_Chuan.xlsx` với 100% đường dẫn URL chuẩn chỉnh không sai 1 ký tự.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Tự động bỏ dấu tiếng Việt, chuẩn hóa quy tắc đặt tên UTM và sinh mã QR cho hàng trăm link chiến dịch.
