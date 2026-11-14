---
trigger: glob
globs: "*.xlsx"
description: "Quy chuẩn tính toán nhu cầu nguyên vật liệu từ kế hoạch sản xuất"
---

# QUY CHUẨN BÓC TÁCH ĐỊNH MỨC BOM
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Tổng nhu cầu NVL = Số lượng thành phẩm * Định mức * (1 + % Hao hụt).
2. Nhu cầu mua thêm = Max(0, Tổng nhu cầu NVL - Tồn kho hiện có).
3. Xuất ra file `Nhu_cau_nguyen_vat_lieu_BOM.xlsx`.
