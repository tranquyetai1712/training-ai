# CẨM NANG HƯỚNG DẪN DEMO: 45-VE-GANTT-CHART-EXCEL

## 1. Nỗi Đau & Bài Toán Thực Tế
Sếp yêu cầu vẽ biểu đồ Gantt Chart trên Excel có tô màu theo ngày và tự trừ cuối tuần. Ngồi kẻ ô tô màu bằng tay mất nửa ngày.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu một công việc bắt đầu vào Thứ Sáu và kéo dài 5 ngày làm việc, ngày hoàn thành chính xác sẽ là Thứ Ba tuần kế tiếp hay Thứ Năm nếu không làm Thứ Bảy & Chủ Nhật?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Từ file hang_muc_du_an.xlsx, hãy tính Ngày bắt đầu và Ngày kết thúc cho từng hạng mục (loại trừ Thứ 7 và CN), sau đó tạo biểu đồ Gantt trực quan ngay trên lưới ô Excel bằng Conditional Formatting cho tháng 11/2026. Xuất ra file Gantt_Chart_Du_An_T11.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu dùng phép cộng ngày thông thường (Ngày BĐ + Thời lượng) thay vì hàm tính ngày làm việc (Workday logic), dự án sẽ bị trễ tiến độ vì tính cả ngày nghỉ.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Gantt_Chart_Du_An_T11.xlsx` với các thanh tiến độ Gantt Chart tự động đổi màu mượt mà theo ngày tháng.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Tạo ra một biểu đồ Gantt Chart động cực đẹp trên Excel mà không cần tốn hàng giờ kẻ ô thủ công.
