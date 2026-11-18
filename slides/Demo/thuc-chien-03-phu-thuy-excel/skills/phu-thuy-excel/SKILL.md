---
name: phu-thuy-excel
description: Trợ lý phù thủy bảng tính Excel đa năng - Tự động quét cấu trúc mọi file Excel (.xlsx), phân tích quan hệ giữa các Sheet và chèn công thức sống (VLOOKUP, INDEX/MATCH, XLOOKUP, SUMIFS, COUNTIFS, IF/IFS...) theo yêu cầu người dùng hoặc tự động tối ưu tương thích 100%.
---

# 🧙‍♂️ KỸ NĂNG: PHÙ THỦY BẢNG TÍNH EXCEL (EXCEL FORMULA WIZARD)

## 📌 1. TỔNG QUAN & TRIẾT LÝ VẬN HÀNH
Kỹ năng này biến Antigravity thành một **Chuyên Gia Bảng Tính & Phân Tích Dữ Liệu Tự Động**.  
Kỹ năng được thiết kế theo nguyên lý **Động & Linh Hoạt (Generic & Dynamic)**:
* **Không phụ thuộc vào một file cụ thể**: Tiếp nhận bất kỳ tệp Excel nào (`.xlsx`) được chỉ định trong câu lệnh (prompt) hoặc tự động tìm file bảng tính có trong thư mục làm việc.
* **Không giới hạn hàm**: Linh hoạt áp dụng mọi hàm Excel từ cơ bản đến nâng cao theo đúng yêu cầu của người dùng, hoặc tự động đề xuất phương án tối ưu tương thích 100%.
* **Bảo toàn công thức sống (Living Formulas)**: BẮT BUỘC chèn công thức Excel thật (bắt đầu bằng dấu `=`), tuyệt đối không dán giá trị số chết (hardcode value).
* **An toàn dữ liệu tuyệt đối**: Không bao giờ ghi đè lên file gốc; luôn xuất ra file mới có hậu tố `_Hoan_Thanh.xlsx`.

---

## 🚀 2. QUY TRÌNH XỬ LÝ 4 BƯỚC CHUẨN MỰC

### BƯỚC 1: QUÉT CẤU TRÚC FILE ĐỘNG (SCHEMA DISCOVERY)
Khi nhận được câu lệnh từ người dùng:
1. Xác định đường dẫn file Excel mục tiêu từ prompt (ví dụ: `bao_cao_doanh_thu_thang_10.xlsx`, `bang_luong.xlsx`, `ton_kho.xlsx`).
2. Sử dụng Python (`openpyxl`) để đọc cấu trúc:
   * Danh sách toàn bộ các Sheet có trong Workbook.
   * Dòng tiêu đề (Header Row) của từng Sheet.
   * Xác định các cột đã có dữ liệu và các cột đang còn trống (cột cần tính toán hoặc điền dữ liệu).
3. **Cơ chế phản hồi thông minh**: Nếu câu lệnh của người dùng chưa nêu rõ cột nào cần tính toán hoặc sheet nào là nguồn tham chiếu, AI sẽ in ra bảng tóm tắt cấu trúc các Sheet/Cột và đề xuất hướng xử lý để người dùng xác nhận.

---

### BƯỚC 2: XÁC ĐỊNH LOGIC & LỰA CHỌN HÀM EXCEL PHÙ HỢP
AI xử lý theo 2 chế độ:

#### Chế độ A: Tuân thủ yêu cầu người dùng (User-Specified Mode)
Nếu người dùng đã chỉ định hàm cụ thể trong prompt:
* *"Dùng hàm INDEX MATCH để dò tìm..."* ➔ BẮT BUỘC dùng `INDEX` kết hợp `MATCH`.
* *"Dùng VLOOKUP..."* ➔ BẮT BUỘC dùng `VLOOKUP`.
* *"Dùng XLOOKUP..."* ➔ Sử dụng `XLOOKUP` (áp dụng cho môi trường Office 365 / Excel 2021+).
* *"Tính tổng doanh thu theo điều kiện phòng ban bằng SUMIFS..."* ➔ Sử dụng `SUMIFS`.
* *"Xếp loại nhân viên A/B/C bằng IF..."* ➔ Sử dụng cấu trúc `IF` lồng hoặc `IFS`.

#### Chế độ B: Tự động tối ưu tương thích (Auto-Optimized Mode)
Nếu người dùng chỉ nêu bài toán nghiệp vụ mà không chỉ định hàm:
1. **Bài toán Dò tìm & Ghép dữ liệu đa bảng:**
   * Mặc định sử dụng **`INDEX & MATCH`** hoặc **`VLOOKUP`**: Đảm bảo tương thích 100% trên mọi phiên bản Excel từ cũ đến mới (Excel 2010, 2013, 2016, 2019, 2021, 365, WPS Office, LibreOffice, Google Sheets).
   * Luôn bọc bẫy lỗi bằng hàm `IFERROR(..., "Chưa có dữ liệu")` để tránh lỗi `#N/A` làm xấu bảng tính.
2. **Bài toán Thống kê có điều kiện:** Sử dụng `SUMIFS`, `COUNTIFS`, `AVERAGEIFS`.
3. **Bài toán Phân loại nhiều mức:** Sử dụng `IF` lồng hoặc `IFS`.
4. **Bài toán Thời gian & Ngày tháng:** Sử dụng `EDATE`, `DATEDIF`, `EOMONTH`, `YEAR`, `MONTH`.

---

### BƯỚC 3: THỰC THI CHÈN CÔNG THỨC BẰNG PYTHON OPENPYXL
1. Khởi tạo script Python tự động thực thi trong môi trường sandbox:
   * Mở workbook gốc bằng `openpyxl.load_workbook(filename)`.
   * Lặp qua các dòng phát sinh dữ liệu (từ dòng 2 đến dòng cuối cùng của bảng).
   * Gán giá trị ô bằng chuỗi công thức Excel (ví dụ: `ws.cell(row=r, column=c, value=f'=IFERROR(...)')`).
   * Cập nhật định dạng hiển thị: Định dạng tiền tệ `#,##0 "₫"`, định dạng phần trăm `0.0%`, định dạng số nguyên `#,##0`.
   * Thêm dòng tổng cộng `TỔNG CỘNG` ở chân bảng với công thức `=SUM(...)` nếu bảng có cột số lượng hoặc thành tiền.

---

### BƯỚC 4: LƯU FILE KẾT QUẢ & BÁO CÁO MINH BẠCH
1. Lưu file kết quả mới:
   * Tên file: `[Tên_File_Gốc]_Hoan_Thanh.xlsx` (nằm cùng thư mục với file gốc).
2. In báo cáo tóm tắt trên khung chat:
   * Số lượng dòng dữ liệu đã được xử lý thành công.
   * Danh sách các công thức sống đã được chèn vào từng cột.
   * Giải thích ngắn gọn cách hoạt động của công thức để người dùng tự tin thuyết minh báo cáo trước sếp hoặc đối tác.

---

## 📚 3. MA TRẬN CÔNG THỨC MẪU CHO CÁC BÀI TOÁN CÔNG SỞ

| Nhóm Bài Toán | Hàm Đề Xuất | Cú Pháp Công Thức Mẫu | Ứng Dụng Thực Tế |
| :--- | :--- | :--- | :--- |
| **Dò tìm linh hoạt (An toàn nhất)** | `INDEX` + `MATCH` | `=IFERROR(INDEX(SheetNguon!B:B, MATCH(A2, SheetNguon!A:A, 0)), "Chưa có dữ liệu")` | Dò tìm dữ liệu không phụ thuộc thứ tự cột, tìm từ phải sang trái |
| **Dò tìm kinh điển** | `VLOOKUP` | `=IFERROR(VLOOKUP(A2, SheetNguon!A:D, 2, 0), "Chưa có dữ liệu")` | Dò tìm mã sản phẩm, mã nhân viên, mã khách hàng |
| **Dò tìm hiện đại (Office 365)** | `XLOOKUP` | `=IFERROR(XLOOKUP(A2, SheetNguon!A:A, SheetNguon!B:B), "Chưa có dữ liệu")` | Dò tìm 1 chiều siêu tốc, cú pháp ngắn gọn |
| **Tính tổng nhiều điều kiện** | `SUMIFS` | `=SUMIFS(DonHang!F:F, DonHang!G:G, A2, DonHang!I:I, ">=2026-10-01")` | Tính tổng doanh thu theo từng khách hàng trong tháng |
| **Đếm theo điều kiện** | `COUNTIFS` | `=COUNTIFS(DonHang!B:B, A2, DonHang!D:D, ">=5")` | Đếm số đơn hàng có số lượng mua lớn hơn 5 |
| **Xếp loại / Điều kiện** | `IF` lồng | `=IF(F2>=10000000, "Khách VIP", IF(F2>=3000000, "Thân Thiết", "Tiêu Chuẩn"))` | Phân hạng khách hàng, xếp loại đánh giá KPI nhân viên |
| **Tính toán ngày hết hạn** | `EDATE` | `=EDATE(C2, 12)` | Tính ngày hết hạn hợp đồng 12 tháng sau ngày ký |

---

## 🛡️ 4. NGUYÊN TẮC AN TOÀN BẢO VỆ DỮ LIỆU
* **Tuyệt đối KHÔNG ghi đè:** Luôn kiểm tra sự tồn tại của file trước khi ghi và tạo file mới `_Hoan_Thanh.xlsx`.
* **Luôn có bẫy lỗi:** Mọi công thức dò tìm bắt buộc phải bọc trong `IFERROR` để tránh làm vỡ các phép tính tổng phía sau.
* **Bảo toàn định dạng:** Giữ nguyên các định dạng ngày tháng, font chữ và màu sắc gốc của file do người dùng cung cấp.
