# CẨM NANG HƯỚNG DẪN DEMO: 24-CHIA-GIO-LEAD-ROUTING

## 1. Nỗi Đau & Bài Toán Thực Tế
Marketing đổ về hàng trăm leads mỗi tuần, trưởng phòng sales phải ngồi chia tay và copy vào file riêng của từng bạn rất mất thời gian.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu một lead đến từ Đà Nẵng mà đội ngũ chỉ có team Hà Nội và team Sài Gòn, quy tắc định tuyến của bạn sẽ ưu tiên theo khoảng cách hay theo tải công việc hiện tại của nhân viên?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Đọc file lead_moi_tuan_45.xlsx. Hãy chia đều các leads khu vực Hà Nội cho 2 Sales miền Bắc (Tuấn, Hà) và TP.HCM cho 2 Sales miền Nam (Hùng, My) theo xoay vòng, ưu tiên lead >100 nhân sự cho Senior Sales (Tuấn, Hùng). Xuất ra file Lead_Da_Phan_Bo_Tuan_45.xlsx gồm các sheet riêng cho từng Sales.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không hướng dẫn thứ tự ưu tiên: Ưu tiên điều kiện Senior trước, sau đó mới chia vòng tròn các lead còn lại, các lead lớn có thể bị chia nhầm cho nhân viên thử việc.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Lead_Da_Phan_Bo_Tuan_45.xlsx` với các sheet riêng cho từng nhân viên sales, dữ liệu chia công bằng và bảo mật.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Tự động hóa hoàn toàn quy trình Lead Routing phức tạp chỉ trong 10 giây.
