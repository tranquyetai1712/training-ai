---
trigger: glob
globs: "*.xlsx"
description: "Quy chuẩn đối soát chi tiết phí sàn Shopee và tính lãi lỗ từng đơn"
---

# QUY CHUẨN ĐỐI SOÁT BÁN HÀNG SÀN TMĐT
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Tiền thực nhận = Doanh thu gốc - Tổng các loại phí sàn thu.
2. Lợi nhuận ròng = Tiền thực nhận - Giá vốn hàng bán (COGS).
3. Xuất ra file `Doi_soat_lai_lo_Shopee_T10.xlsx` kèm sheet `Canh_Bao_Ban_Lo` tô màu đỏ.
