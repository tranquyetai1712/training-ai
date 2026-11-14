# CẨM NANG HƯỚNG DẪN DEMO: 35-TAO-LICH-CONTENT-FOLDER-DRIVE

## 1. Nỗi Đau & Bài Toán Thực Tế
Lên kế hoạch 30 bài đăng phải vào Google Drive tạo tay 30 folder con rồi copy link dán ngược lại vào file Excel rất tốn công.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu Designer cần tìm ảnh cho bài đăng ngày 12/11, cấu trúc tên folder thế nào sẽ giúp tìm ra ngay trong 3 giây mà không cần hỏi ai?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Đọc danh sách bài viết trong content_calendar.xlsx. Với mỗi bài, hãy tự động tạo thư mục con theo cú pháp [Mã bài] - [Ngày] - [Chủ đề] bên trong thư mục Assets_T11, sau đó điền đường link của từng thư mục vào cột 'Link Thư Mục Thiết Kế'. Xuất ra Content_Calendar_T11_Updated.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu trong chủ đề bài viết có chứa ký tự cấm của hệ điều hành như / : * ? < > |, script tạo folder sẽ bị crash nếu không được làm sạch tên trước.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Content_Calendar_T11_Updated.xlsx` có đầy đủ link thư mục tương ứng được tạo sẵn sàng cho Designer bỏ ảnh vào.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Kết hợp hoàn hảo giữa Excel và Google Drive: thư mục tự sinh ra và link tự nhảy vào từng dòng bảng tính.
