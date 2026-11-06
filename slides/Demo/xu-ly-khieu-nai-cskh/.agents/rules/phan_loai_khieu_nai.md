---
trigger: glob
globs: "*.txt, *.xlsx"
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
4. ĐỊNH DẠNG BẢNG TÍNH EXCEL (.XLSX):
   - Xuất trực tiếp ra file bảng tính Excel (.xlsx) chuẩn văn phòng với đầy đủ các cột: Thời Gian, Mã Đơn, Khách Hàng, Số Điện Thoại, Mức Độ, Nội Dung Sự Cố, Hành Động Đề Xuất.
   - Dòng tiêu đề rõ ràng, dữ liệu trình bày gọn gàng, súc tích để mở ngay trên Microsoft Excel mà không lo lỗi font tiếng Việt hay vỡ định dạng.
