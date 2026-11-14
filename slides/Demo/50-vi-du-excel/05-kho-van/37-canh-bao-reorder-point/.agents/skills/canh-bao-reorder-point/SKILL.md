---
name: canh-bao-reorder-point
description: "Use this skill to monitor inventory safety stock levels, calculate reorder points (ROP), and generate purchase recommendations."
---

# QUY TRÌNH CẢNH BÁO ĐIỂM ĐẶT HÀNG LẠI

Quy trình chuẩn từng bước để AI tự động thực thi tác vụ:

## Bước 1: Đọc dữ liệu tồn và tốc độ bán
Nạp file `ton_kho_toc_do_ban.xlsx`.

## Bước 2: Tính toán ROP và tồn an toàn
Xác định các mã hàng rơi xuống dưới điểm đặt hàng lại.

## Bước 3: Tính số lượng cần mua
Làm tròn theo MOQ và lưu file `Ke_hoach_dat_hang_ROP.xlsx`.
