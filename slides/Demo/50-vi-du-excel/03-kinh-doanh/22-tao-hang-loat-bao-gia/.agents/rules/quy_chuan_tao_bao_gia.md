---
trigger: glob
globs: "*.xlsx"
description: "Quy chuẩn lập báo giá bán hàng tự động"
---

# QUY CHUẨN BÁO GIÁ SẢN PHẨM & CHIẾT KHẤU
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Lấy thông tin khách hàng từ file yêu cầu báo giá.
2. Tra cứu đơn giá từ file bảng giá chuẩn.
3. Xuất ra từng file báo giá riêng trong thư mục `Bao_Gia_Xuat/` theo cú pháp: `Bao_Gia_[MaKH]_[Ngay].xlsx`.
