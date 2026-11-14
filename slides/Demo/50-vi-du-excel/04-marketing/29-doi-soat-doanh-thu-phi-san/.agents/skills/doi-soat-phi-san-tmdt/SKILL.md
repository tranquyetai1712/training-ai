---
name: doi-soat-phi-san-tmdt
description: "Use this skill to reconcile marketplace deductions, calculate net unit margins, and identify loss-making SKUs."
---

# QUY TRÌNH ĐỐI SOÁT DOANH THU VÀ PHÍ SÀN TMĐT

Quy trình chuẩn từng bước để AI tự động thực thi tác vụ:

## Bước 1: Đọc báo cáo đơn sàn & giá vốn
Nạp file `shopee_orders.xlsx` và `gia_von.xlsx`.

## Bước 2: Bóc tách ma trận phí
Tính tổng các khoản phí sàn và đối trừ giá vốn.

## Bước 3: Khoanh vùng đơn hàng lỗ
Lọc các đơn hàng có lợi nhuận âm và lưu file `Doi_soat_lai_lo_Shopee_T10.xlsx`.
