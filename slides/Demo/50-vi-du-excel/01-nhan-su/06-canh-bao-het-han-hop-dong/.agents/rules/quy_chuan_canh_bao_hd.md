---
trigger: glob
globs: "*.xlsx"
description: "Quy chuẩn phát hiện và cảnh báo hợp đồng lao động sắp hết hạn"
---

# QUY CHUẨN QUẢN LÝ THỜI HẠN HỢP ĐỒNG LAO ĐỘNG
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Tính số ngày còn lại tính từ Ngày hiện tại đến Ngày kết thúc HĐ.
2. Phân loại cảnh báo: 'Sắp hết hạn trong 15 ngày' (Màu Đỏ), 'Hết hạn trong 16-30 ngày' (Màu Vàng).
3. Xuất ra sheet mới mang tên `Canh_Bao_Gia_Han`.
