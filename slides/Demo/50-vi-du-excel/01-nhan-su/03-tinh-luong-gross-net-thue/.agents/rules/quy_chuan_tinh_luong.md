---
trigger: glob
globs: "*.xlsx"
description: "Quy chuẩn tính toán lương Gross, Net, bảo hiểm và thuế TNCN lũy tiến"
---

# QUY CHUẨN BẢNG TÍNH LƯƠNG & THUẾ THU NHẬP CÁ NHÂN
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Chèn công thức Excel trực tiếp vào các cột tính toán để kế toán có thể audit kiểm tra.
2. Thu nhập chịu thuế = Tổng thu nhập - Các khoản phụ cấp miễn thuế.
3. Thu nhập tính thuế = Thu nhập chịu thuế - Các khoản giảm trừ (Bảo hiểm + Bản thân + Người phụ thuộc).
4. Xuất ra file `Bang_luong_chi_tiet_T10.xlsx`.
