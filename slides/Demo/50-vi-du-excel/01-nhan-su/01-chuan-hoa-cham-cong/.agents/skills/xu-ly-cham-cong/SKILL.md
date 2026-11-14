---
name: xu-ly-cham-cong
description: "Use this skill when processing raw biometric attendance logs into monthly timesheet reports."
---

# QUY TRÌNH XỬ LÝ BẢNG CHẤM CÔNG VÂN TAY

Quy trình chuẩn từng bước để AI tự động thực thi tác vụ:

## Bước 1: Đọc dữ liệu thô
Kiểm tra cấu trúc file `cham_cong_thang_10_raw.xlsx`, xác định các cột Mã NV, Tên NV, Thời gian quẹt.

## Bước 2: Làm sạch & Gom nhóm
Tách Ngày và Giờ, gom theo từng nhân viên trong từng ngày để tìm mốc quẹt đầu tiên và cuối cùng.

## Bước 3: Tính toán công & Phút vi phạm
So sánh với mốc 08:30 và 17:30 để tính số phút đi muộn, về sớm và quy đổi công chuẩn.

## Bước 4: Xuất bảng tính chuẩn
Tạo file `bang_cong_chuan_hoa.xlsx`, kẻ khung viền, tô màu các ô vi phạm và tính dòng tổng cộng.
