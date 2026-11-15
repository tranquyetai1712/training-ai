# Quy Chuẩn Bảng Kê Chi Phí & Xuất Excel Kế Toán

Tài liệu quy định tiêu chuẩn định dạng số liệu, bảo toàn dữ liệu gốc và cấu trúc file Excel đầu ra cho plugin `q-ke-toan-hoa-don`.

---

## I. AN TOÀN DỮ LIỆU GỐC
1. **Tuyệt đối không xóa, sửa đè hoặc di chuyển** các file ảnh hóa đơn gốc (`.png`, `.jpg`, `.jpeg`, `.pdf`).
2. Mọi kết quả tổng hợp chỉ được xuất ra tệp mới (`.md` hoặc `.xlsx`).

---

## II. ĐỊNH DẠNG SỐ LIỆU & TIỀN TỆ
1. **Ngày tháng:** Chuẩn Việt Nam `DD/MM/YYYY` (ví dụ: `12/10/2026`).
2. **Tiền tệ trên bảng Markdown xem trước:** Sử dụng dấu chấm `.` phân cách hàng nghìn và đơn vị `VNĐ` (ví dụ: `1.200.000 VNĐ`).
3. **Số liệu trong Excel (`.xlsx`):** Lưu dưới dạng **số nguyên** (`int`/`float`) để công thức tính toán hoạt động chính xác, kết hợp định dạng hiển thị `#,##0 "VNĐ"`.

---

## III. CẤU TRÚC BẮT BUỘC CỦA FILE EXCEL ĐẦU RA
1. **Dòng 1:** `CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM` (in hoa, đậm, căn giữa).
2. **Dòng 2:** `BẢNG KÊ THANH TOÁN CHI PHÍ CÔNG TÁC THÁNG 10/2026` (hoặc tháng tương ứng, in hoa, đậm, cỡ chữ lớn).
3. **Bảng dữ liệu gồm 7 cột chuẩn:**
   `STT` | `Ngày` | `Đơn Vị Phát Hành` | `Nội Dung Chi` | `Tiền Trước Thuế` | `Thuế VAT` | `Tổng Thanh Toán`
4. **Dòng cuối cùng — `TỔNG CỘNG`:**
   - **BẮT BUỘC** dùng công thức Excel thật (`=SUM(...)`) cho các cột tiền (`Tiền Trước Thuế`, `Thuế VAT`, `Tổng Thanh Toán`).
   - Tuyệt đối không ghi số chết (hardcoded).
5. **Chân trang ký duyệt:** Có đủ 3 vị trí ký trang trọng:
   `Người Lập Bảng` — `Kế Toán Trưởng` — `Giám Đốc Phê Duyệt`.
