---
name: doi-soat-sao-ke
description: "Use this skill to reconcile bank statement transaction rows against internal accounting ledgers."
---

# QUY TRÌNH ĐỐI SOÁT SAO KÊ NGÂN HÀNG VÀ SỔ QUỸ

Quy trình chuẩn từng bước để AI tự động thực thi tác vụ:

## Bước 1: Đọc 2 nguồn dữ liệu
Nạp file `sao_ke_vcb.xlsx` và `so_thu_chi.xlsx`.

## Bước 2: Đối soát khớp 1-1
So sánh mã đơn, số tiền và ngày giao dịch.

## Bước 3: Tìm kiếm tổ hợp gộp
Tìm các lệnh chuyển khoản bằng tổng tiền của nhiều hóa đơn chưa thanh toán.

## Bước 4: Xuất báo cáo đối soát
Phân loại 3 nhóm kết quả vào file `Ket_qua_doi_soat_T10.xlsx`.
