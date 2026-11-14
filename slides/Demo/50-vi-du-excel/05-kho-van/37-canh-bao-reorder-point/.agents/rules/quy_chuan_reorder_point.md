---
trigger: glob
globs: "*.xlsx"
description: "Quy chuẩn tính toán điểm đặt hàng lại và lượng hàng cần bổ sung"
---

# QUY CHUẨN HOẠCH ĐỊNH ĐẶT HÀNG REORDER POINT
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Tồn hiệu dụng = Tồn kho hiện tại + Hàng đang về.
2. Cảnh báo Đặt hàng: Nếu Tồn hiệu dụng <= ROP.
3. Xuất ra file `Ke_hoach_dat_hang_ROP.xlsx`.
