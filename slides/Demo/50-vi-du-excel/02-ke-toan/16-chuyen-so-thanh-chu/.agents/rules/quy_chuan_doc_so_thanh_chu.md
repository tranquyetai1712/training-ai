---
trigger: glob
globs: "*.xlsx"
description: "Quy chuẩn đọc số tiền thành chữ song ngữ trên chứng từ kế toán"
---

# QUY CHUẨN CHUYỂN ĐỔI SỐ TIỀN THÀNH CHỮ SONG NGỮ
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Chuyển đổi 100% chính xác các hàng tỷ, triệu, nghìn, đồng.
2. Thêm 2 cột mới vào file: `Bằng chữ (Tiếng Việt)` và `In Words (English)`.
3. Xuất ra file `Danh_sach_phieu_chi_chuan.xlsx`.
