---
trigger: glob
globs: "*.xlsx"
description: "Quy chuẩn phân loại tồn kho ABC và cảnh báo hàng cận date"
---

# QUY CHUẨN PHÂN LOẠI TỒN KHO ABC & HẠN SỬ DỤNG
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Tính giá trị tồn kho = Số lượng tồn * Giá vốn.
2. Phân loại ABC theo tỷ lệ phần trăm tích lũy giá trị vốn.
3. Xuất ra file `Bao_cao_ton_kho_ABC_Canh_bao.xlsx` gồm 3 sheet: 'Phan_Nhom_ABC', 'Hang_Can_Date', 'Hang_Chet_Dead_Stock'.
