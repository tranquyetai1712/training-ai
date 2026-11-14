---
trigger: glob
globs: "*.csv, *.xlsx"
description: "Quy chuẩn gộp báo cáo Facebook Ads, Google Ads, TikTok Ads"
---

# QUY CHUẨN BÁO CÁO QUẢNG CÁO ĐA KÊNH
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Chuyển đổi bảng mã CSV UTF-8 đúng font tiếng Việt.
2. Tự động tính: CTR = Clicks / Impressions * 100%, CPA = Chi phí / Chuyển đổi.
3. Xuất ra file `Master_Ads_Report_T10.xlsx`.
