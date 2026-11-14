---
trigger: glob
globs: "*.xlsx"
description: "Quy chuẩn phân nhóm khách hàng bằng mô hình RFM"
---

# QUY CHUẨN PHÂN NHÓM KHÁCH HÀNG RFM
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Chấm điểm R, F, M từ 1 đến 5.
2. Khách VIP (Champions): R >= 4, F >= 4, M >= 4.
3. Khách Nguy cơ rời bỏ (At-risk): R <= 2, F >= 3, M >= 4.
4. Xuất ra file `Phan_khuc_khach_hang_RFM.xlsx` kèm gợi ý kịch bản chăm sóc.
