---
trigger: glob
globs: "*.xlsx"
description: "Quy chuẩn tính phân bổ chi phí trả trước TK 242 và trích khấu hao TSCĐ"
---

# QUY CHUẨN BẢNG PHÂN BỔ CHI PHÍ TRẢ TRƯỚC & KHẤU HAO
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Chi phí 1 tháng tròn = Nguyên giá / Số tháng phân bổ.
2. Chi phí tháng đầu tiên = (Chi phí 1 tháng tròn / Số ngày trong tháng) * (Số ngày trong tháng - Ngày bắt đầu sử dụng + 1).
3. Xuất ra file `Bang_phan_bo_chi_phi_2026.xlsx`.
