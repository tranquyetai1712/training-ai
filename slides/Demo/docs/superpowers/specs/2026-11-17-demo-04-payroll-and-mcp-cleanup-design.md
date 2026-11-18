# Thiết Kế Nâng Cấp Demo 04 (Tách Phiếu Lương Gửi Email) & Dọn Dẹp Cấu Hình MCP Rời

**Ngày tạo:** 2026-11-17  
**Phạm vi:** Bộ 50 Ví Dụ Excel (`slides/Demo/50-vi-du-excel`) & Bộ Script Sinh Dữ Liệu (`slides/Demo/scripts`)

---

## 1. Bối Cảnh & Mục Tiêu

1. **Loại bỏ cấu hình `mcp_config.json` rời không cần thiết:**
   - Trong môi trường Antigravity, các MCP Server như `gmail` và `google_workspace` đã được tích hợp sẵn (built-in native integration).
   - Việc sinh file `mcp_config.json` trong từng thư mục bài tập (như bài `04-tach-phieu-luong-gui-email` và 8 bài liên thông khác) cùng thư mục hướng dẫn `Demo/ket-noi-mcp-gmail/` gây dư thừa và dễ làm học viên hiểu nhầm rằng phải cấu hình thủ công từng thư mục.
2. **Nâng cấp dữ liệu & format Phiếu lương bài `04-tach-phieu-luong-gui-email` theo chuẩn mẫu Chasqui:**
   - Nâng cấp file đầu vào `bang_luong_chot.xlsx` lên **15 cột** (bổ sung 7 cột nghiệp vụ cốt lõi từ bản mẫu **PAYROLL SLIP - Công ty TNHH CHASQUI VIỆT NAM**).
   - Tái tạo file kết quả `_ket_qua_mau_chuan.xlsx` (và quy chuẩn cho các file Excel cá nhân tách ra trong `Phieu_Luong_Ca_Nhan/`) **có giao diện, màu sắc, bố cục bảng và công thức sống giống bản mẫu PDF Chasqui** (Header công ty, tiêu đề `PAYROLL SLIP`, cột nhóm màu xanh dương, header bảng màu cam, các dòng tổng màu xanh lá, khung chữ ký `Received by` / `Approved by`).

---

## 2. Thiết Kế Chi Tiết Phần 1: Cấu Trúc Bảng Lương & Format Phiếu Lương Excel (Bài 04)

### 2.1. Cấu trúc 15 cột của `bang_luong_chot.xlsx` (Sheet `LuongChot`)

| STT | Cột Excel | Tên Cột | Ý Nghĩa / Nguồn Từ Mẫu Chasqui | Định Dạng |
|:---:|:---:|---|---|---|
| 1 | A | `Mã NV` | Mã định danh nhân viên (`019CQ`, `020CQ`...) | Text (Center) |
| 2 | B | `Họ và Tên` | Họ tên nhân viên | Text (Left) |
| 3 | C | `Email` | Địa chỉ email nhận phiếu lương | Text (Left) |
| 4 | D | `Phòng Ban` | Bộ phận công tác | Text (Left) |
| 5 | E | `Giờ Công` | Số giờ làm việc thực tế trong tháng (`Time`) | Number (`#,##0`) |
| 6 | F | `Lương Cơ Bản` | Lương cơ bản đóng BHXH (`A1`) | Currency (`#,##0`) |
| 7 | G | `TC Ăn Trưa` | Trợ cấp ăn trưa (`C1 + D4`) | Currency (`#,##0`) |
| 8 | H | `TC Điện Thoại & Đi Lại` | Trợ cấp điện thoại (`C4`) + đi lại (`D5`) | Currency (`#,##0`) |
| 9 | I | `TC Thuê Nhà` | Trợ cấp thuê nhà (`D3`) | Currency (`#,##0`) |
| 10 | J | `Lương Làm Thêm (OT)` | Tổng trợ cấp làm thêm giờ (`LTCb`) | Currency (`#,##0`) |
| 11 | K | `Tổng Thu Nhập (Gross)` | Tổng lương gộp (`=SUM(F{r}:J{r})`) | Currency (`#,##0`) |
| 12 | L | `Trừ BHXH (10.5%)` | BHXH 8% + BHYT 1.5% + BHTN 1% (`=F{r}*0.105`) | Currency (`#,##0`) |
| 13 | M | `Giảm Trừ Gia Cảnh` | Giảm trừ bản thân (`GT1`) + Người phụ thuộc (`GT2`) | Currency (`#,##0`) |
| 14 | N | `Thuế TNCN` | Thuế TNCN khấu trừ trong tháng | Currency (`#,##0`) |
| 15 | O | `Thực Lĩnh` | Lương thuần thực nhận (`=K{r}-L{r}-N{r}`) | Currency (`#,##0`) |

### 2.2. Dữ liệu mẫu (4 nhân viên)

1. **`019CQ` - Trần Văn Quyết** (`quyet.tran@chasqui.vn` - Kỹ thuật):
   - Khớp số liệu thực tế từ bản mẫu PDF Chasqui:
   - Giờ công: `176` | Lương CB: `10,600,000` | TC Ăn trưa: `3,000,000` | TC ĐT & Đi lại: `8,000,000` | TC Thuê nhà: `6,225,000` | OT: `0`
   - Gross: `27,825,000` | Trừ BHXH (10.5%): `1,113,000` | Giảm trừ gia cảnh: `34,100,000` | Thuế TNCN: `0` | Thực lĩnh: `26,712,000`
2. **`020CQ` - Nguyễn Văn An** (`an.nguyen@chasqui.vn` - Kỹ thuật):
   - Giờ công: `176` | Lương CB: `15,000,000` | TC Ăn trưa: `3,000,000` | TC ĐT & Đi lại: `6,000,000` | TC Thuê nhà: `7,500,000` | OT: `2,500,000`
   - Gross: `34,000,000` | Trừ BHXH (10.5%): `1,575,000` | Giảm trừ gia cảnh: `15,400,000` | Thuế TNCN: `1,353,750` | Thực lĩnh: `31,071,250`
3. **`021CQ` - Trần Thị Mai** (`mai.tran@chasqui.vn` - Kinh doanh):
   - Giờ công: `176` | Lương CB: `12,000,000` | TC Ăn trưa: `2,500,000` | TC ĐT & Đi lại: `5,000,000` | TC Thuê nhà: `4,500,000` | OT: `1,200,000`
   - Gross: `25,200,000` | Trừ BHXH (10.5%): `1,260,000` | Giảm trừ gia cảnh: `11,000,000` | Thuế TNCN: `784,000` | Thực lĩnh: `23,156,000`
4. **`022CQ` - Lê Văn Đức** (`duc.le@chasqui.vn` - Marketing):
   - Giờ công: `168` | Lương CB: `10,000,000` | TC Ăn trưa: `2,200,000` | TC ĐT & Đi lại: `4,000,000` | TC Thuê nhà: `3,800,000` | OT: `0`
   - Gross: `20,000,000` | Trừ BHXH (10.5%): `1,050,000` | Giảm trừ gia cảnh: `19,800,000` | Thuế TNCN: `0` | Thực lĩnh: `18,950,000`

### 2.3. Thiết kế format & cấu trúc `_ket_qua_mau_chuan.xlsx` (Sheet `PhieuLuong_019CQ`)

Tái tạo trực tiếp giao diện bảng **PAYROLL SLIP** từ bản mẫu PDF vào Excel (không xuất PDF):

- **Phần Header (Dòng 1–6):**
  - Dòng 1: `Công ty TNHH CHASQUI VIỆT NAM` (Bold, size 12, căn trái).
  - Dòng 2: `PAYROLL SLIP` (Bold, size 14, căn giữa từ cột A–D).
  - Dòng 3: Kỳ lương `01/10/2026 - 31/10/2026` (Bold, căn giữa).
  - Dòng 4: `Họ và tên:` | `Trần Văn Quyết` (Bold).
  - Dòng 5: `Mã nhân viên:` | `019CQ` (Bold).
  - Dòng 6: `Phòng ban:` | `Kỹ thuật`.
- **Phần Bảng Chính (4 cột: Cột A = Nhóm dọc | Cột B = `Diễn giải` | Cột C = `Công thức tính` | Cột D = `Số tiền`):**
  - **Dòng tiêu đề bảng (Header Row):** Nền cam (`#FFC000`), chữ đen in đậm, căn giữa, viền mỏng (`thin`).
  - **Cột A (Cột phân nhóm bên trái):** Nền xanh dương (`#0070C0`), chữ trắng in đậm, gộp ô theo 2 nhóm chính:
    - Nhóm 1 (`THÔNG TIN CƠ BẢN`): Số giờ làm việc thực tế (`176.0`).
    - Nhóm 2 (`LƯƠNG & KHẤU TRỪ`): Các dòng Lương cơ bản, Trợ cấp, OT, Gross, Bảo hiểm, Giảm trừ, Thuế TNCN, Thực lĩnh.
  - **Các dòng nổi bật màu xanh lá (`#92D050`), chữ in đậm:**
    - `Lương cơ bản` (`A1`) — `10,600,000`
    - `Tổng trợ cấp` (`LTC = C1+D4 + C4+D5 + D3`) — công thức `=SUM(...)` (`17,225,000`)
    - `Tổng lương gộp (Gross)` (`Gross = Lương CB + Tổng trợ cấp + OT`) — công thức `=D10+D11+D15` (`27,825,000`)
    - `Bảo hiểm khấu trừ lương nhân viên` (`Total BH = BHXH 8% + BHYT 1.5% + BHTN 1%`) — công thức `=SUM(...)` (`1,113,000`)
    - `Tổng giảm trừ gia cảnh` (`GT = GT1 + GT2`) — `34,100,000`
    - `Thuế thu nhập cá nhân` (`Thuế = TNTT * Thuế suất`) — `0`
    - `Tổng lương thuần được nhận` (`Thực nhận = Gross - Total BH - Thuế`) — công thức `=D16-D17-D22` (`26,712,000`)
  - **Các dòng chi tiết (nền trắng, chữ thường, thụt lề nhẹ hoặc căn trái):**
    - `Trợ cấp ăn trưa` (`3,000,000`)
    - `Trợ cấp điện thoại & đi lại` (`8,000,000`)
    - `Trợ cấp thuê nhà` (`6,225,000`)
    - `Lương làm thêm giờ (OT)` (`0`)
    - `Bảo hiểm xã hội (8%)` — công thức `=LươngCB*8%` (`848,000`)
    - `Bảo hiểm y tế (1.5%)` — công thức `=LươngCB*1.5%` (`159,000`)
    - `Bảo hiểm thất nghiệp (1%)` — công thức `=LươngCB*1%` (`106,000`)
  - **Định dạng số:** `#,##0;(#,##0);"-"` để giá trị `0` hiển thị dấu `-` giống y hệt bản mẫu PDF.
- **Phần Footer Chữ Ký (Cuối bảng):**
  - 2 cột chữ ký `Received by` (bên trái: `Trần Văn Quyết`) và `Approved by` (bên phải: `Fujioka Jun`).

### 2.4. Cập nhật Rules, Skill và Prompt Demo của Bài 04
- Cập nhật `.agents/rules/quy_chuan_phieu_luong.md` yêu cầu:
  - Khi xuất file Excel phiếu lương cá nhân vào `Phieu_Luong_Ca_Nhan/`, phải giữ đúng layout & bảng màu chuẩn của `_ket_qua_mau_chuan.xlsx` (Header cam `#FFC000`, tổng xanh lá `#92D050`, cột nhóm xanh dương `#0070C0`, công thức sống).
  - Nội dung Gmail Draft là bảng HTML gọn gàng liệt kê đầy đủ các khoản từ `bang_luong_chot.xlsx` (Giờ công, Lương cơ bản, từng khoản Trợ cấp, OT, Gross, BHXH 10.5%, Giảm trừ gia cảnh, Thuế TNCN, Thực lĩnh) và có thể đính kèm file Excel cá nhân tương ứng nếu cần.
- Cập nhật `.agents/skills/tach-phieu-luong-email/SKILL.md` và `PROMPT_DEMO.md` khớp với quy trình mới.

---

## 3. Thiết Kế Chi Tiết Phần 2: Dọn Dẹp `mcp_config.json` Toàn Hệ Thống Demo

1. **Xóa các file `mcp_config.json` đã sinh và thư mục hướng dẫn cũ:**
   - Xóa `mcp_config.json` tại 9 bài tập tích hợp trong `50-vi-du-excel`:
     - `01-nhan-su/04-tach-phieu-luong-gui-email/mcp_config.json`
     - `01-nhan-su/06-canh-bao-het-han-hop-dong/mcp_config.json`
     - `02-ke-toan/12-phan-loai-tuoi-no-nhac-no/mcp_config.json`
     - `02-ke-toan/14-hop-nhat-bao-cao-kinh-doanh/mcp_config.json`
     - `03-kinh-doanh/24-chia-gio-lead-routing/mcp_config.json`
     - `03-kinh-doanh/27-quet-namecard-soan-mail/mcp_config.json`
     - `04-marketing/35-tao-lich-content-folder-drive/mcp_config.json`
     - `06-hanh-chinh/44-bien-ban-hop-action-tracker/mcp_config.json`
     - `06-hanh-chinh/47-tao-folder-phan-quyen-drive/mcp_config.json`
   - Xóa thư mục `/var/www/html/training-ai/slides/Demo/ket-noi-mcp-gmail/`.
2. **Cập nhật bộ Script Generator & Verification:**
   - `slides/Demo/scripts/generator_core.py`: Xóa hàm `write_mcp_config()` và docstring liên quan.
   - `slides/Demo/scripts/depts/dept_01_nhan_su.py`, `dept_02_ke_toan.py`, `dept_03_kinh_doanh.py`, `dept_04_marketing.py`, `dept_06_hanh_chinh.py`: Xóa các lệnh gọi `.write_mcp_config(...)`. Trong `dept_01_nhan_su.py`, cập nhật phần sinh dữ liệu bài 04 (`bang_luong_chot.xlsx` 15 cột và `_ket_qua_mau_chuan.xlsx` format PAYROLL SLIP chuẩn Chasqui).
   - `slides/Demo/scripts/verify_50_demos.py`: Bỏ kiểm tra tồn tại file `mcp_config.json` (và kiểm tra không còn file `mcp_config.json` dư thừa trong `50-vi-du-excel/`).
   - `slides/Demo/50-vi-du-excel/README.md`: Cập nhật mục 4 sang "Liên thông MCP Tích hợp sẵn (Gmail & Google Workspace)" — giải thích rõ Antigravity đã tích hợp sẵn nên sử dụng trực tiếp.

---

## 4. Tiêu Chí Kiểm Thử (Verification Criteria)

1. Chạy lại script sinh dữ liệu hoàn tất không lỗi.
2. Chạy `python3 slides/Demo/scripts/verify_50_demos.py` đạt **100% PASS** trên toàn bộ 50 bài tập.
3. Kiểm tra thực tế `bang_luong_chot.xlsx` có đúng 15 cột, 4 nhân viên; `_ket_qua_mau_chuan.xlsx` có đầy đủ màu sắc (`#FFC000`, `#92D050`, `#0070C0`), công thức Excel sống, và số liệu dòng `019CQ` khớp bản mẫu PDF Chasqui (`Gross = 27,825,000`, `BHXH = 1,113,000`, `Thực lĩnh = 26,712,000`).
4. Không còn bất kỳ file `mcp_config.json` nào trong `50-vi-du-excel/` và thư mục `ket-noi-mcp-gmail/` đã bị xóa.
