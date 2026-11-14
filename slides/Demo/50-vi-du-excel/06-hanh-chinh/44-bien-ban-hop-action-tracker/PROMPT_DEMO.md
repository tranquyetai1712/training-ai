# CẨM NANG HƯỚNG DẪN DEMO: 44-BIEN-BAN-HOP-ACTION-TRACKER

## 1. Nỗi Đau & Bài Toán Thực Tế
Sau cuộc họp 2 tiếng có biên bản họp dài 5 trang chữ. Thư ký phải ngồi nhặt từng đầu việc ai làm, hạn nào để gõ vào Excel rất lâu.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu trong biên bản họp ghi 'Anh Tuấn phụ trách kết nối API cổng thanh toán VNPay trước 18/11/2026', làm sao để trích xuất chuẩn xác vào một bảng tính theo dõi công việc?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Đọc file bien_ban_hop.txt. Trích xuất toàn bộ các đầu việc cần làm (Action Items) và cập nhật vào file Project_Action_Tracker.xlsx theo các cột: STT, Hạng mục, Phòng ban, PIC, Deadline, Mức độ ưu tiên (High/Medium/Low), Trạng thái. Tô màu đỏ cho việc ưu tiên High.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu cuộc họp có câu thảo luận chung chung không chốt người làm (No PIC Assigned), AI cần gắn nhãn cảnh báo 'Chưa phân công' thay vì bỏ sót đầu việc.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Project_Action_Tracker.xlsx` được điền đầy đủ các đầu việc chuẩn xác phân theo từng cá nhân phụ trách.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Từ văn bản họp dài dòng biến ngay thành bảng theo dõi tiến độ công việc chuẩn chỉnh trên Excel.
