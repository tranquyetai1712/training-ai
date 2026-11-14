---
trigger: glob
globs: "*.xlsx, *.csv"
description: "Quy chuẩn thẩm mỹ, màu sắc, định dạng số và công thức sống cho bảng tính Excel văn phòng"
---

# QUY CHUẨN THẨM MỸ & CÔNG THỨC EXCEL CHUẨN VĂN PHÒNG
Khi tạo bất kỳ tệp tin bảng tính Excel (.xlsx) nào trong thư mục này, bạn BẮT BUỘC tuân thủ các tiêu chuẩn sau:

1. ĐỊNH DẠNG TIÊU ĐỀ (HEADER STYLING):
   - Font chữ đồng bộ: Arial hoặc Segoe UI, cỡ chữ 11pt, in đậm (Bold).
   - Màu nền tiêu đề (Header Fill): Màu xanh navy chuyên nghiệp `#1F497D`.
   - Màu chữ tiêu đề: Màu trắng `#FFFFFF`, căn giữa (Center Alignment) cả chiều ngang lẫn chiều dọc.

2. ĐỊNH DẠNG DỮ LIỆU SỐ & NGÀY THÁNG:
   - Số tiền tệ: Định dạng phân cách hàng nghìn `#,##0` (ví dụ: `15,000,000 VNĐ`), căn phải (Right Alignment).
   - Tỷ lệ phần trăm: Định dạng có 1 chữ số thập phân `0.0%` (ví dụ: `12.5%`).
   - Ngày tháng: Bắt buộc chuẩn hóa định dạng `DD/MM/YYYY` (ví dụ: `15/10/2026`).

3. TỰ ĐỘNG CĂN CHỈNH ĐỘ RỘNG CỘT (AUTO-FIT COLUMNS):
   - Bắt buộc tính toán độ rộng cột tự động dựa trên độ dài chuỗi dài nhất trong cột cộng thêm 4 ký tự đệm (padding), tuyệt đối không để xảy ra lỗi hiển thị `###` do cột quá hẹp.

4. CÔNG THỨC SỐNG (ACTIVE LIVE FORMULAS):
   - Luôn ưu tiên chèn công thức Excel sống (hàm `SUM`, `AVERAGE`, `IF`, `VLOOKUP`, `XLOOKUP`, `ROUND`) vào các ô tổng cộng hoặc tính toán, TUYỆT ĐỐI KHÔNG dán cứng giá trị tĩnh (Hardcoded static numbers) để bảng tính có tính tương tác cao khi người dùng kiểm tra.
