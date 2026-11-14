---
trigger: glob
globs: "*.xlsx"
description: "Quy chuẩn xử lý chênh lệch kiểm kê kho thực tế và sổ sách"
---

# QUY CHUẨN BIÊN BẢN XỬ LÝ CHÊNH LỆCH KIỂM KÊ
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Chênh lệch = Thực đếm - Tồn sổ sách ERP.
2. Phát hiện nghi vấn nhầm chéo: Mã hàng thừa và mã hàng thiếu cùng số lượng và cùng nhóm hàng.
3. Xuất ra file `Bien_ban_kiem_ke_xu_ly_chenh_lech.xlsx`.
