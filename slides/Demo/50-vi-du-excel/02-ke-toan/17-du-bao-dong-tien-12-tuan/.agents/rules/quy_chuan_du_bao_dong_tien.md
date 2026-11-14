---
trigger: glob
globs: "*.xlsx"
description: "Quy chuẩn lập mô hình dự báo dòng tiền 12 tuần đa kịch bản"
---

# QUY CHUẨN MÔ HÌNH DỰ BÁO DÒNG TIỀN 12 TUẦN
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Số dư cuối kỳ = Số dư đầu kỳ + Tổng thu trong tuần - Tổng chi trong tuần.
2. Số dư đầu kỳ tuần N = Số dư cuối kỳ tuần N-1.
3. Xuất ra file `Du_bao_dong_tien_12_tuan.xlsx` kèm biểu đồ đường biểu diễn dòng tiền.
