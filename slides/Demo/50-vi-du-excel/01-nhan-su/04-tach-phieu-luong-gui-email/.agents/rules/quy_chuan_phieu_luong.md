---
trigger: glob
globs: "*.xlsx"
description: "Quy chuẩn tách phiếu lương cá nhân chuẩn Chasqui và định dạng email HTML"
---

# QUY CHUẨN ĐỊNH DẠNG PHIẾU LƯƠNG & TIÊU ĐỀ EMAIL
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Tiêu đề email theo cú pháp: [Phiếu Lương Tháng 10/2026] - [Họ và Tên] - [Mã NV].
2. Khi tách file Excel cá nhân vào thư mục `Phieu_Luong_Ca_Nhan/`, BẮT BUỘC tái tạo đúng layout, bảng màu (Header cam #FFC000, tổng xanh lá #92D050, cột nhóm xanh dương #0070C0) và công thức sống giống hệt file `_ket_qua_mau_chuan.xlsx`.
3. Nội dung email Gmail Draft trình bày bằng bảng HTML gọn gàng, liệt kê đầy đủ: Giờ công, Lương cơ bản, Các khoản trợ cấp (Ăn trưa, Điện thoại & Đi lại, Thuê nhà), Lương OT, Tổng Gross, Khấu trừ BHXH (10.5%), Giảm trừ gia cảnh, Thuế TNCN và Thực lĩnh.
