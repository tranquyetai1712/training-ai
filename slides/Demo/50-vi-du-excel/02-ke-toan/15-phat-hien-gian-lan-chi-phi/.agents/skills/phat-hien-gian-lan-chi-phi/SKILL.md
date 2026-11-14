---
name: phat-hien-gian-lan-chi-phi
description: "Use this skill to audit employee expense claims for duplicates, policy violations, and suspicious splitting."
---

# QUY TRÌNH KIỂM TOÁN PHÁT HIỆN GIAN LẬN CHI PHÍ

Quy trình chuẩn từng bước để AI tự động thực thi tác vụ:

## Bước 1: Nạp bảng kê đề nghị thanh toán
Đọc file `de_nghi_thanh_toan_q3.xlsx`.

## Bước 2: Chạy thuật toán kiểm tra rủi ro
Quét trùng lặp hóa đơn, kiểm tra ngưỡng thanh toán tiền mặt 20 triệu và phát hiện tách đơn.

## Bước 3: Xuất báo cáo kiểm toán
Tạo sheet phân loại các khoản chi rủi ro vào file `Bao_cao_kiem_toan_chi_phi_Q3.xlsx`.
