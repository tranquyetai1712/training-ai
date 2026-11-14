---
trigger: glob
globs: "*.xlsx, *.csv"
description: "Quy chuẩn xử lý dữ liệu chấm công thô từ máy vân tay / FaceID"
---

# QUY CHUẨN TÍNH GIỜ VÀO RA & SỐ PHÚT ĐI MUỘN
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Chuyển đổi cột Ngày giờ về đúng định dạng datetime chuẩn ISO.
2. Gom nhóm (Group by) theo Mã NV và Ngày để tính MIN(Giờ quẹt) = Giờ Vào, MAX(Giờ quẹt) = Giờ Ra.
3. Nếu chỉ có 1 lần quẹt trong ngày: ghi chú 'Quên quẹt Vào/Ra' và tính 0.5 công.
4. Xuất ra file kết quả `bang_cong_chuan_hoa.xlsx` gồm 2 sheet: 'Chi_Tiet_Hang_Ngay' và 'Tong_Hop_Thang'.
