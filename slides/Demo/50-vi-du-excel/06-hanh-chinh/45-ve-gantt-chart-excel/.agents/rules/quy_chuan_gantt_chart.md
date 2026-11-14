---
trigger: glob
globs: "*.xlsx"
description: "Quy chuẩn lập lịch tiến độ dự án và vẽ biểu đồ Gantt Chart bằng lưới ô Excel"
---

# QUY CHUẨN BẢNG TIẾN ĐỘ GANTT CHART
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Tính Ngày kết thúc = WORKDAY(Ngày bắt đầu, Số ngày thực hiện - 1).
2. Thiết lập Conditional Formatting trên các cột ngày (từ 01/11 đến 30/11) để ô tự đổi màu xanh khi nằm giữa Ngày bắt đầu và Ngày kết thúc.
3. Xuất ra file `Gantt_Chart_Du_An_T11.xlsx`.
