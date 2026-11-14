---
trigger: glob
globs: "*.txt, *.xml, *.pdf"
description: "Quy chuẩn bóc tách hóa đơn GTGT vào bảng kê mua vào"
---

# QUY CHUẨN BẢNG KÊ HÓA ĐƠN GIÁ TRỊ GIA TĂNG MUA VÀO
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Trích xuất đủ 9 trường: Ký hiệu mẫu, Số HĐ, Ngày lập, Tên NCC, MST, Mặt hàng, Tiền chưa thuế, Thuế GTGT, Tổng tiền.
2. Kiểm tra chéo: Nếu Tiền chưa thuế + Thuế GTGT lệch Tổng tiền > 10 đồng, đánh dấu 'Cần kiểm tra lại'.
3. Xuất ra file `Bang_ke_mua_vao_T10.xlsx`.
