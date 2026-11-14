---
trigger: glob
globs: "*.xlsx"
description: "Quy chuẩn rà soát phát hiện rủi ro và gian lận trong bảng kê hoàn ứng chi phí"
---

# QUY CHUẨN KIỂM TOÁN BẢNG KÊ THANH TOÁN
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Cảnh báo Đỏ (Gian lận): Trùng Số HĐ + MST người bán.
2. Cảnh báo Vàng (Vi phạm quy chế): Thanh toán tiền mặt từ 20 triệu trở lên.
3. Cảnh báo Cam (Nghi vấn lách luật): Tách hóa đơn cùng ngày cùng NCC tổng > 20tr.
4. Xuất kết quả kiểm toán ra file `Bao_cao_kiem_toan_chi_phi_Q3.xlsx`.
