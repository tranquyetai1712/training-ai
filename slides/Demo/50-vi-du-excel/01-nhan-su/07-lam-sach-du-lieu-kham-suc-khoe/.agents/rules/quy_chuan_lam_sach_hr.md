---
trigger: glob
globs: "*.xlsx, *.csv"
description: "Quy chuẩn làm sạch và chuẩn hóa dữ liệu nhân sự văn phòng"
---

# QUY CHUẨN LÀM SẠCH DỮ LIỆU HỌ TÊN, CCCD, SĐT
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Họ tên: Bỏ khoảng trắng thừa ở đầu/cuối và giữa các từ; viết hoa chữ cái đầu mỗi từ.
2. Ngày sinh: Chuyển các định dạng (YYYY-MM-DD, DD.MM.YYYY, DD/MM/YY) về chuẩn DD/MM/YYYY.
3. Số điện thoại: Đủ 10 số bắt đầu bằng số 0.
4. Số CCCD: Đủ 12 số bắt đầu bằng số 0 (nếu bị mất phải bù lại).
5. Xuất ra file `danh_sach_chuan_gui_benh_vien.xlsx`.
