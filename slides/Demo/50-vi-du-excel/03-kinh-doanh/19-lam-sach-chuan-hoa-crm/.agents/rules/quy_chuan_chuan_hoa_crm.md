---
trigger: glob
globs: "*.xlsx"
description: "Quy chuẩn làm sạch số điện thoại và lọc trùng dữ liệu CRM"
---

# QUY CHUẨN CHUẨN HÓA DỮ LIỆU KHÁCH HÀNG CRM
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. SĐT: Loại bỏ dấu chấm, dấu cách, đổi mã quốc gia +84 thành số 0 ở đầu.
2. Tên công ty: Đồng bộ 'Cty', 'CT TNHH' về chuẩn 'Công ty TNHH'.
3. Xuất ra file `Data_CRM_Chuan_Hoa.xlsx`.
