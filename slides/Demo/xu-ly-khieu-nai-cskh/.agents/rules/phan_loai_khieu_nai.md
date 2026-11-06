---
trigger: glob
globs: "*.txt, *.csv"
description: "Quy chuẩn trích xuất và phân loại mức độ ưu tiên cuộc gọi CSKH"
---

# QUY CHUẨN PHÂN LOẠI & ĐỊNH DẠNG CUỘC GỌI KHIẾU NẠI
Khi đọc dữ liệu cuộc gọi từ các file văn bản hoặc bảng tính, bạn BẮT BUỘC tuân thủ:

1. MÃ ĐƠN HÀNG: Viết hoa đồng nhất theo định dạng ORD-XXXX (Ví dụ: "ord9821" ➔ "ORD-9821").
2. PHÂN LOẠI MỨC ĐỘ ƯU TIÊN:
   - [HỎA TỐC]: Sự cố vỡ hỏng, lỗi nghiêm trọng, khách yêu cầu đổi ngay lập tức.
   - [KHẨN CẤP]: Giao sai mẫu mã, yêu cầu hoàn tiền.
   - [TIÊU CHUẨN]: Khách hỏi thăm tiến độ giao hàng thông thường.
3. ĐỊNH DẠNG THÔNG TIN:
   - Họ tên: Viết hoa danh từ riêng (Ví dụ: Nguyễn Anh Tuấn, Trần Thị Thúy).
   - Số điện thoại: Định dạng nhóm 0xxx.xxx.xxx (Ví dụ: 0912.345.678).
   - Thời gian: Đồng bộ chuẩn HH:mm DD/MM/YYYY.
4. AN TOÀN FILE CSV (CHỐNG LỖI NHẢY CỘT TRÊN EXCEL):
   - Bên trong nội dung của từng ô, TUYỆT ĐỐI KHÔNG sử dụng dấu phẩy (,) để ngắt câu.
   - Thay thế toàn bộ dấu phẩy trong câu văn bằng dấu gạch ngang (-) hoặc từ nối (Ví dụ: "Vỡ màn hình - đòi đổi gấp", "Giao sai màu áo - đòi hoàn tiền", "Liên hệ xin lỗi - lập đơn hoàn hàng & hoàn tiền").
