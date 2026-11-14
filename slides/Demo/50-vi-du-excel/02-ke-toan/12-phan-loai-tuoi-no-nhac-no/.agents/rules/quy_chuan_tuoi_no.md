---
trigger: glob
globs: "*.xlsx"
description: "Quy chuẩn phân bổ tuổi nợ phải thu và lập báo cáo quản trị công nợ"
---

# QUY CHUẨN BÁO CÁO TUỔI NỢ PHẢI THU (AR AGING REPORT)
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Tính số ngày quá hạn = Hôm nay - Ngày đến hạn thanh toán.
2. Phân bổ số dư nợ còn lại vào đúng cột tuổi nợ tương ứng.
3. Xuất ra file `Bao_cao_tuoi_no_va_nhac_no.xlsx` kèm bản nháp email nhắc nợ cho các khách hàng quá hạn > 15 ngày.
