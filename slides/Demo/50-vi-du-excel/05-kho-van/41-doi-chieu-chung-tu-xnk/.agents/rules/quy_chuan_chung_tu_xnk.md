---
trigger: glob
globs: "*.xlsx, *.txt, *.pdf"
description: "Quy chuẩn đối chiếu chéo bộ chứng từ hải quan xuất nhập khẩu"
---

# QUY CHUẨN KIỂM TRA CHÉO CHỨNG TỪ XNK
Khi đọc và xử lý dữ liệu cho bài toán này, bạn BẮT BUỘC tuân thủ các quy tắc sau:

1. Khớp mã HS Code, Tên hàng tiếng Anh, Số lượng kiện giữa Invoice và Packing List.
2. Khớp Gross Weight và CBM giữa Packing List và Bill of Lading.
3. Xuất ra file `Bien_ban_doi_chieu_chung_tu_XNK.xlsx`.
