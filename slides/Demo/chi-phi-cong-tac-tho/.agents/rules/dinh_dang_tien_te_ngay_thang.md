---
trigger: glob
globs: "*.txt, *.csv"
description: "Quy chuẩn định dạng tiền tệ VNĐ và ngày tháng Việt Nam khi xử lý file số liệu"
---

# QUY CHUẨN ĐỊNH DẠNG SỐ LIỆU VĂN PHÒNG
Khi đọc dữ liệu từ các tệp văn bản hoặc bảng tính, bạn BẮT BUỘC tuân thủ:

1. TIỀN TỆ: Mọi số tiền phải có dấu chấm phân cách hàng nghìn và đuôi "VNĐ" (Ví dụ: 3.500.000 VNĐ, 1.250.000 VNĐ).
2. NGÀY THÁNG: Bắt buộc định dạng chuẩn Việt Nam DD/MM/YYYY (Ví dụ: 24/10/2026, 25/10/2026).
3. HỌ TÊN: Viết hoa đầy đủ từng từ trang trọng (Ví dụ: Nguyễn Văn An, Trần Thị Mai, Lê Hoàng Nam).
