---
name: boc-tach-hoa-don-excel
description: "Đọc hiểu hàng loạt ảnh chụp hóa đơn (ảnh nghiêng, mờ, VAT), bóc tách ngày tháng, đơn vị bán, tiền trước thuế, VAT, tổng tiền; xuất bảng đối chiếu Markdown và tạo file Excel (.xlsx) chuẩn doanh nghiệp có sẵn công thức =SUM()."
---

# Quy Trình Đọc Ảnh Hóa Đơn & Xuất Bảng Kê Excel

Hướng dẫn Agent thực hiện quy trình Kế toán số từ bước đọc ảnh hóa đơn đến khi xuất file Excel hoàn chỉnh đúng chuẩn [quy-chuan-bang-ke-excel.md](../../rules/quy-chuan-bang-ke-excel.md).

---

## I. CÁC BƯỚC THỰC THI

### Bước 1: Kiểm tra thư mục ảnh hóa đơn
- Liệt kê toàn bộ ảnh (`.png`, `.jpg`, `.jpeg`) trong thư mục người dùng chỉ định (ví dụ `HoaDon_CongTac`).
- Giữ nguyên vẹn 100% file ảnh gốc, không xóa, đổi tên hoặc di chuyển.

### Bước 2: Đọc và bóc tách dữ liệu từng ảnh bằng Thị giác (Vision)
- Mở đọc trực tiếp từng bức ảnh hóa đơn.
- Trích xuất đủ các trường:
  - `ngay`: Ngày lập hóa đơn (`DD/MM/YYYY`)
  - `don_vi`: Tên đơn vị phát hành (nhà hàng, hãng taxi, khách sạn, nhà sách...)
  - `noi_dung`: Nội dung chi phí ngắn gọn
  - `tien_truoc_thue`: Số tiền trước thuế (số nguyên VNĐ)
  - `vat_phan_tram`: Thuế suất (`0`, `8`, `10`...)
  - `tien_vat`: Tiền thuế VAT (số nguyên VNĐ)
  - `tong_tien`: Tổng tiền thanh toán (`tien_truoc_thue + tien_vat`)
- Đối chiếu lại phép cộng trên hóa đơn để đảm bảo không sai lệch dù chỉ 1 đồng.

### Bước 3: Xuất bảng đối chiếu Markdown cho người dùng nghiệm thu
- Trình bày bảng Markdown rõ ràng với các cột:
  `Ngày | Đơn Vị Phát Hành | Nội Dung Chi | Tiền Trước Thuế | VAT | Tổng Thanh Toán`
- Hiển thị thêm dòng tổng cộng để người dùng dễ kiểm tra nhanh trước khi xuất Excel.

### Bước 4: Xuất file Excel `.xlsx` chuẩn doanh nghiệp (khi người dùng yêu cầu hoặc trong quy trình trọn gói)
- Chuẩn bị dữ liệu JSON các dòng hóa đơn đã bóc tách.
- Gọi script chuẩn `scripts/tao_bang_ke_excel.py` (dùng `openpyxl`) để sinh tệp Excel:
  ```powershell
  python "<SKILL_DIR>/scripts/tao_bang_ke_excel.py" --input "<duong_dan_json>" --output "<ten_file.xlsx>"
  ```
- Đảm bảo file `.xlsx` sinh ra có:
  - Tiêu đề 2 dòng trang trọng (`CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM` & `BẢNG KÊ THANH TOÁN CHI PHÍ CÔNG TÁC...`).
  - Kẻ khung viền bảng, tô nền xanh xám nhạt cho hàng tiêu đề, định dạng số `#,##0 "VNĐ"`.
  - Hàng `TỔNG CỘNG` dùng công thức `=SUM(...)` thật sự cho cột Tiền trước thuế, Thuế VAT và Tổng thanh toán.
  - 3 vị trí ký tên: `Người Lập Bảng`, `Kế Toán Trưởng`, `Giám Đốc Phê Duyệt`.

### Bước 5: Báo cáo kết quả
- Xác nhận đường dẫn tệp Excel vừa tạo và tóm tắt tổng số hóa đơn, tổng chi phí để người dùng mở kiểm tra trực tiếp trong Microsoft Excel.
