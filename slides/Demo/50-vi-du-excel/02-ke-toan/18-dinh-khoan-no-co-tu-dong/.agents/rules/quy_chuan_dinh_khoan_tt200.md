---
trigger: glob
globs: "*.xlsx"
description: "Quy chuẩn tự động định khoản tài khoản kế toán từ nội dung diễn giải"
---

# QUY CHUẨN HẠCH TOÁN ĐỊNH KHOẢN THEO THÔNG TƯ 200
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Rút tiền gửi ngân hàng nộp quỹ tiền mặt: Nợ 1111 / Có 1121.
2. Thanh toán tiền điện/nước/văn phòng phẩm: Nợ 642 / Có 1111 hoặc 1121.
3. Thu tiền bán hàng của khách hàng: Nợ 1121 / Có 131.
4. Trả tiền nhà cung cấp: Nợ 331 / Có 1121.
5. Chi trả lương nhân viên: Nợ 334 / Có 1121.
6. Xuất ra file `Giao_dich_da_dinh_khoan_import_misa.xlsx`.
