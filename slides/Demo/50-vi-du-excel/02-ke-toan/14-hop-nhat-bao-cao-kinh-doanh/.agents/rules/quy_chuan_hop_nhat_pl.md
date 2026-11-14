---
trigger: glob
globs: "*.xlsx"
description: "Quy chuẩn hợp nhất báo cáo kết quả hoạt động kinh doanh đa chi nhánh"
---

# QUY CHUẨN HỢP NHẤT BÁO CÁO P&L
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Tổng hợp số liệu từ các chi nhánh: Hà Nội, Đà Nẵng, TP.HCM.
2. Lập cột Tổng cộng toàn công ty = Sum(Hà Nội + Đà Nẵng + TP.HCM).
3. Xuất ra file `Bao_cao_PL_Hop_Nhat_T10.xlsx` kèm bảng xếp hạng chi nhánh hiệu quả nhất.
