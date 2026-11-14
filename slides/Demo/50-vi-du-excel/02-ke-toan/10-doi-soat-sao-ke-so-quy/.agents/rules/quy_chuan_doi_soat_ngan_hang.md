---
trigger: glob
globs: "*.xlsx"
description: "Quy chuẩn đối soát giao dịch ngân hàng với sổ kế toán nội bộ"
---

# QUY CHUẨN ĐỐI SOÁT SAO KÊ NGÂN HÀNG
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Khớp 1-1: Cùng số tiền, ngày giao dịch chênh lệch tối đa 1 ngày làm việc, nội dung chứa Mã đơn hoặc Tên khách.
2. Khớp Gộp: 1 giao dịch ngân hàng bằng tổng số tiền của 2-3 hóa đơn cùng khách hàng.
3. Xuất file kết quả `Ket_qua_doi_soat_T10.xlsx` gồm 3 sheet: 'Da_Khop_1_1', 'Khop_Gop_Don', 'Chua_Khop_Can_Lam_Ro'.
