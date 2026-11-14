# CẨM NANG HƯỚNG DẪN DEMO: 17-DU-BAO-DONG-TIEN-12-TUAN

## 1. Nỗi Đau & Bài Toán Thực Tế
Doanh nghiệp có lãi trên sổ sách nhưng hết tiền trả nợ và lương vì lệch kỳ hạn thu tiền khách và trả tiền nhà cung cấp.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Doanh nghiệp báo lãi 10 tỷ trên P&L nhưng tài khoản ngân hàng chỉ còn 50 triệu đến ngày trả lương, nguyên nhân phổ biến nhất là gì?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Dựa trên 3 sheet trong file ke_hoach_dong_tien.xlsx, hãy lập bảng Dự báo dòng tiền (Cashflow Forecast) theo từng tuần trong 12 tuần tới. Giả định 2 kịch bản: Cơ sở và Thận trọng (30% khách hàng lớn trả chậm 2 tuần). Cảnh báo màu đỏ tuần nào số dư cuối kỳ dưới 500 triệu đồng. Xuất ra file Du_bao_dong_tien_12_tuan.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không liên kết số dư đầu kỳ tuần này bằng số dư cuối kỳ tuần trước (Rolling Balance), toàn bộ mô hình dòng tiền sẽ bị tính sai hoàn toàn.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Du_bao_dong_tien_12_tuan.xlsx` với mô hình tài chính 12 tuần, chỉ rõ chính xác tuần nào rơi vào vùng nguy hiểm đứt dòng tiền.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Tạo ngay mô hình tài chính đa kịch bản (Scenario Modeling) sắc bén giúp ban lãnh đạo chủ động điều tiết vốn.
