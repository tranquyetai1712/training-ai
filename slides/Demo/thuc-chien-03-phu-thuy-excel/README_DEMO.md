# 🧙‍♂️ THỰC CHIẾN 03: PHÙ THỦY BẢNG TÍNH EXCEL
## BÀI HỌC 8.3: XỬ LÝ SIÊU TỐC CÁC CÔNG THỨC EXCEL PHỨC TẠP (VLOOKUP, XLOOKUP, INDEX/MATCH)

> **Tài liệu thực hành đính kèm:**
> * **File bài tập (Input):** [`bao_cao_doanh_thu_thang_10.xlsx`](bao_cao_doanh_thu_thang_10.xlsx) (Các cột Tên SP, Đơn Giá, Thành Tiền, Tên KH đang để trống).
> * **File nghiệm thu chuẩn (Output):** [`bao_cao_doanh_thu_thang_10_Hoan_Thanh.xlsx`](bao_cao_doanh_thu_thang_10_Hoan_Thanh.xlsx) (100 dòng có sẵn **Công thức sống** tự động tính toán).

---

## 📌 1. CẤU TRÚC DỮ LIỆU FILE BẢNG TÍNH

File Excel `bao_cao_doanh_thu_thang_10.xlsx` gồm **3 Sheet liên kết**:

### Sheet 1: `DonHang` (100 Dòng Dữ Liệu Phát Sinh)
| Cột | Tên Cột | Trạng Thái Trong File Gốc | Mô Tả Nghiệp Vụ |
| :---: | :--- | :--- | :--- |
| **A** | Mã Đơn | Có sẵn (`DH1001` ➔ `DH1100`) | Mã định danh duy nhất của đơn hàng |
| **B** | Mã Sản Phẩm | Có sẵn (`SP01` ➔ `SP15`) | Khóa ngoại dò tìm sang `DanhMucSanPham` |
| **C** | Tên Sản Phẩm | **Trống (Cần điền)** | Dò từ `DanhMucSanPham` bằng `XLOOKUP` |
| **D** | Số Lượng | Có sẵn (1 ➔ 20) | Số lượng sản phẩm khách đặt |
| **E** | Đơn Giá | **Trống (Cần điền)** | Dò từ `DanhMucSanPham` bằng `XLOOKUP` |
| **F** | Thành Tiền | **Trống (Cần tính)** | `= Số Lượng * Đơn Giá * (1 - Chiết Khấu)` |
| **G** | Mã Khách Hàng | Có sẵn (`KH001` ➔ `KH020`) | Khóa ngoại dò tìm sang `KhachHang` |
| **H** | Tên Khách Hàng | **Trống (Cần điền)** | Dò từ `KhachHang` bằng `XLOOKUP` |
| **I** | Ngày Đặt | Có sẵn (`DD/MM/YYYY`) | Ngày phát sinh đơn hàng trong tháng 10/2026 |

---

### Sheet 2: `DanhMucSanPham` (15 Sản Phẩm Bảng Giá Chuẩn)
* **Cột A:** `Mã SP` (`SP01` đến `SP15`)
* **Cột B:** `Tên Sản Phẩm` (Màn hình 4K, Chuột công thái học, Bàn phím cơ, Tai nghe chống ồn...)
* **Cột C:** `Đơn Giá Niêm Yết` (Định dạng VND: `350,000 ₫` đến `11,800,000 ₫`)
* **Cột D:** `Tỷ Lệ Chiết Khấu` (Định dạng %: `0.0%` đến `15.0%`)

---

### Sheet 3: `KhachHang` (20 Khách Hàng Doanh Nghiệp)
* **Cột A:** `Mã Khách` (`KH001` đến `KH020`)
* **Cột B:** `Tên Khách Hàng` (Tập đoàn, Công ty TNHH, Ngân hàng, Bệnh viện...)
* **Cột C:** `Khu Vực` (Hà Nội, TP. Hồ Chí Minh, Đà Nẵng, Cần Thơ...)
* **Cột D:** `Số Điện Thoại` (Hotline liên hệ)

---

## 🎯 2. CÂU LỆNH PROMPT VÀNG 4 BƯỚC RA LỆNH CHO ANTIGRAVITY

Copy đoạn prompt chuẩn 4 bước vàng dưới đây và dán vào khung chat **Antigravity Desktop**:

```markdown
Chào Antigravity, hãy đóng vai một Chuyên gia Cao cấp về Phân tích Dữ liệu và Xử lý Bảng tính Excel. Hãy giúp tôi tạo một Kỹ Năng mới (Skill) mang tên `phu-thuy-excel` tại thư mục `skills/phu-thuy-excel/` với các yêu cầu chi tiết sau:

1. [Mục tiêu]: Tạo file `SKILL.md` hướng dẫn quy trình tự động đọc hiểu các file Excel (.xlsx) có cấu trúc nhiều Sheet liên kết, tự động viết và chèn các công thức tìm kiếm nâng cao (như XLOOKUP, VLOOKUP, INDEX/MATCH) để điền dữ liệu khuyết thiếu và tính toán thành tiền một cách tự động.
2. [Bối cảnh]: File dữ liệu của tôi là `bao_cao_doanh_thu_thang_10.xlsx` gồm 3 Sheet: `DonHang`, `DanhMucSanPham` và `KhachHang`. Cần điền tự động Tên SP, Đơn giá, Tên khách hàng và tính cột Thành Tiền = Số Lượng * Đơn Giá * (1 - Tỷ Lệ Chiết Khấu).
3. [Tiêu chuẩn]:
   - BẮT BUỘC chèn CÔNG THỨC EXCEL THẬT (công thức sống), tuyệt đối không điền giá trị số chết (hardcode value).
   - Mọi công thức tìm kiếm phải được bọc trong hàm bẫy lỗi `IFERROR(..., "Chưa có dữ liệu")` để tránh lỗi #N/A.
   - Định dạng cột tiền tệ chuẩn có dấu phân cách hàng nghìn (VND).
4. [Giới hạn & Bảo vệ]: Tuyệt đối KHÔNG ghi đè lên file Excel gốc. Hãy xuất ra một file mới có tên `bao_cao_doanh_thu_thang_10_Hoan_Thanh.xlsx` và in ra khung chat lời giải thích chi tiết các công thức đã sử dụng để tôi có thể tự tin báo cáo với sếp.
```

Sau khi Antigravity tạo xong skill, kích hoạt bằng lệnh:
```text
Hãy dùng skill phu-thuy-excel để hoàn thiện toàn bộ công thức cho file bao_cao_doanh_thu_thang_10.xlsx ngay bây giờ!
```

---

## 🔍 3. CHI TIẾT CÔNG THỨC SỐNG ĐƯỢC CHÈN VÀO FILE HOÀN THÀNH

File kết quả `bao_cao_doanh_thu_thang_10_Hoan_Thanh.xlsx` được thiết lập mặc định với công thức chuẩn **`VLOOKUP` / `INDEX & MATCH`** để tương thích 100% trên **mọi phiên bản Excel** (Excel 2013, 2016, 2019, 2021, Office 365, WPS Office, LibreOffice, Google Sheets):

### Công Thức Chuẩn Tương Thích 100% (Đang Có Trong File Hoàn Thành):
* **Ô C2 (Tên Sản Phẩm):**
  ```excel
  =IFERROR(VLOOKUP(B2, DanhMucSanPham!A:D, 2, 0), "Chưa có dữ liệu")
  ```
* **Ô E2 (Đơn Giá Niêm Yết):**
  ```excel
  =IFERROR(VLOOKUP(B2, DanhMucSanPham!A:D, 3, 0), 0)
  ```
* **Ô F2 (Thành Tiền Sau Chiết Khấu):**
  ```excel
  =D2 * E2 * (1 - IFERROR(VLOOKUP(B2, DanhMucSanPham!A:D, 4, 0), 0))
  ```
* **Ô H2 (Tên Khách Hàng):**
  ```excel
  =IFERROR(VLOOKUP(G2, KhachHang!A:B, 2, 0), "Chưa có dữ liệu")
  ```
* **Ô D102 & F102 (Dòng Tổng Cộng):**
  ```excel
  =SUM(D2:D101)
  =SUM(F2:F101)
  ```

---

> [!TIP]
> **💡 BÀI HỌC THỰC CHIẾN ĐẮT GIÁ: HIỆN TƯỢNG "CHƯA CÓ DỮ LIỆU" KHI DÙNG XLOOKUP**
> * Nếu bạn dùng hàm mới `=IFERROR(XLOOKUP(G2, KhachHang!A:A, KhachHang!B:B), "Chưa có dữ liệu")` trên các bản **Office 2016, Office 2019 hoặc WPS Office** chưa cập nhật, phần mềm sẽ không nhận diện được hàm `XLOOKUP` và báo lỗi `#NAME?`.
> * Khi đó, hàm bọc bên ngoài `IFERROR(..., "Chưa có dữ liệu")` sẽ tự động bắt lỗi `#NAME?` này và hiển thị ra chữ **"Chưa có dữ liệu"**!
> * Đó là lý do trong bài học này, bạn được dạy phối hợp linh hoạt cả **`VLOOKUP`**, **`INDEX/MATCH`** và **`XLOOKUP`** để bảng tính luôn chạy mượt mà trên máy của mọi sếp và đồng nghiệp!

---

## 🌟 4. CÁCH ÁP DỤNG SKILL CHO MỌI FILE KHÁC & MỌI HÀM TRONG THỰC TẾ

Skill `phu-thuy-excel` được thiết kế **Động 100% (Generic & Flexible)**. Bạn hoàn toàn có thể áp dụng cho bất kỳ bài toán văn phòng nào khác theo các mẫu câu lệnh sau:

### Ví Dụ 1: Bài Toán Quản Lý Kho & Dò Tìm Ngược Bằng `INDEX & MATCH`
> *"Hãy dùng skill `phu-thuy-excel` để xử lý file `ton_kho_thang_10.xlsx`. Tại Sheet `XuatKho`, hãy dùng cặp hàm `INDEX & MATCH` để dò tìm Tên Nhà Cung Cấp từ mã sản phẩm ở Sheet `DanhSachKho`, sau đó tính cột Giá Trị Xuất = Số Lượng * Đơn Giá Vốn. Bọc bẫy lỗi IFERROR và lưu ra file `ton_kho_thang_10_Hoan_Thanh.xlsx`."*

### Ví Dụ 2: Bài Toán Thống Kê Đa Điều Kiện Bằng `SUMIFS` & `COUNTIFS`
> *"Hãy dùng skill `phu-thuy-excel` để xử lý file `bao_cao_kinh_doanh.xlsx`. Tại Sheet `TongHop`, hãy viết công thức `SUMIFS` để tính tổng doanh thu theo từng Khu Vực (Hà Nội, TP.HCM, Đà Nẵng) trong tháng 10, và dùng `COUNTIFS` để đếm số lượng giao dịch thành công. Xuất ra file mới cho tôi."*

### Ví Dụ 3: Bài Toán Tính Lương & Xếp Hạng Nhân Viên Bằng `IF` Lồng Nhau
> *"Hãy dùng skill `phu-thuy-excel` để xử lý file `danh_gia_kpi_q4.xlsx`. Tại cột `Xếp Loại`, hãy viết công thức hàm `IF` lồng: Nếu Điểm KPI >= 90 là 'Xuất Sắc', >= 75 là 'Đạt', còn lại là 'Cần Cải Thiện'. Tại cột `Thưởng`, nếu Xuất Sắc thưởng 20% lương, Đạt thưởng 10%, Cần Cải Thiện thưởng 0%."*

### 💡 Mẹo Cho Người Không Nhớ Rõ Cấu Trúc File:
Nếu bạn nhận được một file Excel lạ từ đồng nghiệp mà chưa rõ các Sheet và cột gồm những gì, chỉ cần gõ:
> *"Hãy dùng skill `phu-thuy-excel` quét cấu trúc file `du_lieu_chua_ro.xlsx`, liệt kê cho tôi danh sách các Sheet, các cột còn trống và đề xuất giải pháp xử lý giúp tôi!"*  
AI sẽ tự động đọc header, in bảng phân tích ra khung chat và gợi ý công thức phù hợp nhất để bạn duyệt trước khi thực thi!
