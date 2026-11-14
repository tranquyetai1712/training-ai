---
trigger: glob
globs: "*.xlsx"
description: "Quy chuẩn phân loại lý do mất khách từ nhật ký ghi chú"
---

# QUY CHUẨN PHÂN TÍCH LOST DEALS
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Gán nhãn chuẩn hóa vào cột mới `Nhóm Lý Do Thất Bại`.
2. Tạo bảng thống kê tỷ trọng % từng lý do theo dòng sản phẩm.
3. Xuất ra file `Phan_tich_Lost_Deals_CRM.xlsx`.
