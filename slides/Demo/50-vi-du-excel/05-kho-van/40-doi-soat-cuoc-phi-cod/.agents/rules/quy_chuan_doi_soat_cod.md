---
trigger: glob
globs: "*.xlsx"
description: "Quy chuẩn đối soát cước vận chuyển và tiền thu hộ COD"
---

# QUY CHUẨN ĐỐI SOÁT BẢNG KÊ VẬN CHUYỂN & COD
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Phát hiện đơn chênh lệch trọng lượng > 200g so với trọng lượng chuẩn.
2. Lọc các đơn hàng trạng thái 'Đã giao' nhưng cột 'Tiền COD đã trả' = 0.
3. Xuất ra file `Bien_ban_doi_soat_cuoc_van_chuyen.xlsx`.
