# CẨM NANG HƯỚNG DẪN DEMO: 08-PHAN-TICH-TURNOVER-DASHBOARD

## 1. Nỗi Đau & Bài Toán Thực Tế
Sếp yêu cầu báo cáo tỷ lệ nghỉ việc theo phòng ban và lý do nghỉ việc, nhưng HR chỉ có danh sách nhân viên nghỉ việc rời rạc.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu sếp hỏi phòng ban nào đang có tỷ lệ nghỉ việc cao nhất quý vừa qua và lý do hàng đầu là gì, bạn sẽ mất bao lâu để làm bảng biểu này?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Phân tích file nhan_su_bien_dong_2026.xlsx để lập báo cáo biến động nhân sự: tính tỷ lệ nghỉ việc (Turnover Rate) theo từng tháng, theo từng phòng ban, và thống kê tỷ trọng lý do nghỉ việc. Xuất ra file HR_Turnover_Report.xlsx có sẵn bảng tổng hợp trực quan.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Tính sai mẫu số của Turnover Rate (phải là số nhân sự bình quân trong kỳ = (Đầu kỳ + Cuối kỳ) / 2, không phải chỉ lấy số đầu kỳ).

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `HR_Turnover_Report.xlsx` chứa bảng chỉ số Turnover Rate chi tiết từng tháng và ma trận phân tích lý do nghỉ việc.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Biến dữ liệu biến động nhân sự thô sơ thành một bản báo cáo phân tích quản trị nhân lực sắc bén.
