# Demo 04 Payroll Upgrade & MCP Cleanup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Nâng cấp bài thực hành `04-tach-phieu-luong-gui-email` lên 15 cột dữ liệu chuẩn Chasqui kèm file kết quả mẫu `_ket_qua_mau_chuan.xlsx` tái tạo giao diện PAYROLL SLIP (cam/xanh lá/xanh dương + công thức sống), đồng thời xóa toàn bộ file `mcp_config.json` rời và thư mục `ket-noi-mcp-gmail/` do Antigravity đã tích hợp sẵn MCP.

**Architecture:** Cập nhật `generator_core.py` để loại bỏ `write_mcp_config()` và bổ sung helper tạo phiếu lương chuẩn PAYROLL SLIP (hoặc hàm chuyên biệt cho bài 04 trong `dept_01_nhan_su.py`), gỡ `write_mcp_config()` ở các script `dept_*.py`, cập nhật `verify_50_demos.py` và `50-vi-du-excel/README.md`, xóa các file `mcp_config.json` cũ và chạy lại generator + verifier để xác nhận 50/50 workspace pass.

**Tech Stack:** Python 3, `openpyxl` (formatting, formulas, cell merging), `verify_50_demos.py`.

**Spec:** [2026-11-17-demo-04-payroll-and-mcp-cleanup-design.md](file:///var/www/html/training-ai/slides/Demo/docs/superpowers/specs/2026-11-17-demo-04-payroll-and-mcp-cleanup-design.md)

## Global Constraints
- Không được xóa hoặc ghi đè làm mất dữ liệu gốc ngoài phạm vi thiết kế; kết quả bài 04 phải sinh qua script generator để đồng bộ.
- Mọi giá trị tổng hợp/tính toán trong `_ket_qua_mau_chuan.xlsx` và `bang_luong_chot.xlsx` (cột Gross, Trừ BHXH, Thực Lĩnh) phải dùng công thức Excel sống (`=SUM(...)`, `=F2*0.105`, `=K2-L2-N2`), không dán cứng giá trị tĩnh.
- Màu sắc bắt buộc cho `_ket_qua_mau_chuan.xlsx` bài 04: Header bảng cam `#FFC000`, dòng tổng/nhóm chính xanh lá `#92D050`, cột nhóm dọc bên trái xanh dương `#0070C0`.
- Không còn bất kỳ file `mcp_config.json` nào trong `slides/Demo/50-vi-du-excel/` sau khi hoàn tất.
- Chạy `python3 slides/Demo/scripts/verify_50_demos.py` phải đạt 100% PASS (exit code 0).

## Review Focus
- Công thức Excel trong `bang_luong_chot.xlsx` và `_ket_qua_mau_chuan.xlsx` bị sai tham chiếu ô (dẫn đến `#VALUE!` hoặc lệch số `27,825,000` / `1,113,000` / `26,712,000` của NV `019CQ`).
- Định dạng số `0` hiển thị số `0` thay vì dấu `-` (`#,##0;(#,##0);"-"`), hoặc độ rộng cột quá hẹp gây lỗi `###`.
- Còn sót file `mcp_config.json` ở một trong 9 bài tập tích hợp dù đã xóa khỏi script generator (do `generate_50_demos.py` không tự xóa file cũ).
- Script `verify_50_demos.py` vẫn báo lỗi thiếu `mcp_config.json` nếu quên gỡ bỏ check ở bước 8.
- Chức năng `create_excel` chung trong `generator_core.py` bị ảnh hưởng làm hỏng các bài tập khác trong 50 ví dụ.

---

### Task 1: Cập nhật `generator_core.py` và các script `dept_*.py` để gỡ `mcp_config.json`

**Files:**
- Modify: `slides/Demo/scripts/generator_core.py:1-12,176-210`
- Modify: `slides/Demo/scripts/depts/dept_01_nhan_su.py:294,441`
- Modify: `slides/Demo/scripts/depts/dept_02_ke_toan.py:211,352`
- Modify: `slides/Demo/scripts/depts/dept_03_kinh_doanh.py:398,605`
- Modify: `slides/Demo/scripts/depts/dept_04_marketing.py:549`
- Modify: `slides/Demo/scripts/depts/dept_06_hanh_chinh.py:41,261`

**Interfaces:**
- Removes: `WorkspaceBuilder.write_mcp_config(self, mcp_type: str = "gmail")`

- [ ] **Step 1: Xóa `write_mcp_config` khỏi `generator_core.py`**

Xóa dòng mô tả `- mcp_config.json` trong docstring đầu file và xóa toàn bộ method `write_mcp_config` (dòng 176-209) trong `slides/Demo/scripts/generator_core.py`.

- [ ] **Step 2: Gỡ toàn bộ lệnh gọi `.write_mcp_config(...)` trong 5 file `dept_*.py`**

Xóa các dòng gọi `write_mcp_config`:
- `dept_01_nhan_su.py`: dòng 294 (`b4.write_mcp_config("gmail")`) và dòng 441 (`b6.write_mcp_config("google_workspace")`)
- `dept_02_ke_toan.py`: dòng 211 (`b12.write_mcp_config("gmail")`) và dòng 352 (`b14.write_mcp_config("google_workspace")`)
- `dept_03_kinh_doanh.py`: dòng 398 (`b24.write_mcp_config("google_workspace")`) và dòng 605 (`b27.write_mcp_config("gmail")`)
- `dept_04_marketing.py`: dòng 549 (`b35.write_mcp_config("google_workspace")`)
- `dept_06_hanh_chinh.py`: dòng 41 (`b44.write_mcp_config("google_workspace")`) và dòng 261 (`b47.write_mcp_config("google_workspace")`)

- [ ] **Step 3: Kiểm tra không còn tham chiếu `write_mcp_config` trong `scripts/`**

Run: `grep -rn "write_mcp_config" /var/www/html/training-ai/slides/Demo/scripts/ || echo "CLEAN"`
Expected: `CLEAN`

---

### Task 2: Nâng cấp dữ liệu, format PAYROLL SLIP, rule, skill và prompt cho Bài 04 trong `dept_01_nhan_su.py`

**Files:**
- Modify: `slides/Demo/scripts/dept_01_nhan_su.py` (hoặc `slides/Demo/scripts/depts/dept_01_nhan_su.py:272-334`)

**Interfaces:**
- Produces: `bang_luong_chot.xlsx` (15 cột, 4 dòng nhân viên với công thức sống ở cột K, L, O) và `_ket_qua_mau_chuan.xlsx` (Sheet `PhieuLuong_019CQ` format PAYROLL SLIP chuẩn Chasqui).

- [ ] **Step 1: Cập nhật Rule, Skill, Prompt Demo của Bài 04 trong `dept_01_nhan_su.py`**

Cập nhật `b4.write_rule`, `b4.write_skill`, `b4.write_prompt_demo`:
- `quy_chuan_phieu_luong.md`: Quy định format file Excel cá nhân trong `Phieu_Luong_Ca_Nhan/` phải giữ đúng layout & bảng màu chuẩn của `_ket_qua_mau_chuan.xlsx` (Header cam `#FFC000`, dòng tổng xanh lá `#92D050`, cột nhóm xanh dương `#0070C0`, công thức sống) và bảng HTML email Gmail Draft liệt kê đầy đủ các khoản (Giờ công, Lương CB, TC Ăn trưa, TC ĐT & Đi lại, TC Thuê nhà, OT, Tổng Gross, Trừ BHXH 10.5%, Giảm trừ gia cảnh, Thuế TNCN, Thực lĩnh).
- `tach-phieu-luong-email/SKILL.md`: Cập nhật 3 bước thực thi dùng trực tiếp Gmail tích hợp sẵn trong Antigravity, tạo file Excel cá nhân chuẩn format `_ket_qua_mau_chuan.xlsx` và tạo Gmail Draft.
- `PROMPT_DEMO.md`: Cập nhật prompt mẫu nhắc tới tạo phiếu lương Excel chi tiết chuẩn mẫu và Gmail Draft trực tiếp (không nhắc cấu hình MCP rời).

- [ ] **Step 2: Cập nhật `bang_luong_chot.xlsx` lên 15 cột với công thức sống**

Sử dụng `openpyxl` (hoặc mở rộng hàm tạo) để ghi 15 cột cho 4 nhân viên (`019CQ` - Trần Văn Quyết, `020CQ` - Nguyễn Văn An, `021CQ` - Trần Thị Mai, `022CQ` - Lê Văn Đức), trong đó:
- Cột K (`Tổng Thu Nhập (Gross)`): `=SUM(F{r}:J{r})`
- Cột L (`Trừ BHXH (10.5%)`): `=ROUND(F{r}*0.105,0)`
- Cột O (`Thực Lĩnh`): `=K{r}-L{r}-N{r}`

- [ ] **Step 3: Viết hàm tạo `_ket_qua_mau_chuan.xlsx` tái tạo giao diện PAYROLL SLIP chuẩn Chasqui**

Tạo sheet `PhieuLuong_019CQ` với `openpyxl`:
- Header công ty: `Công ty TNHH CHASQUI VIỆT NAM`, `PAYROLL SLIP`, `01/10/2026 - 31/10/2026`, `Họ và tên: Trần Văn Quyết`, `Mã nhân viên: 019CQ`, `Phòng ban: Kỹ thuật`.
- Bảng 4 cột (`A`: Nhóm dọc nền `#0070C0` chữ trắng `THÔNG TIN CƠ BẢN` / `LƯƠNG & KHẤU TRỪ`; `B`: `Diễn giải`; `C`: `Công thức tính`; `D`: `Số tiền`).
- Dòng header bảng: nền `#FFC000`, chữ đen bold, căn giữa.
- Các dòng tổng/nhóm chính (`Lương cơ bản`, `Tổng trợ cấp`, `Tổng lương gộp (Gross)`, `Bảo hiểm khấu trừ lương nhân viên`, `Tổng giảm trừ gia cảnh`, `Thuế thu nhập cá nhân`, `Tổng lương thuần được nhận`): nền `#92D050`, chữ bold.
- Công thức sống ở cột D:
  - `Tổng trợ cấp`: `=SUM(D12:D14)` (`17,225,000`)
  - `Tổng lương gộp (Gross)`: `=D10+D11+D15` (`27,825,000`)
  - `Bảo hiểm xã hội (8%)`: `=ROUND(D10*0.08,0)` (`848,000`)
  - `Bảo hiểm y tế (1.5%)`: `=ROUND(D10*0.015,0)` (`159,000`)
  - `Bảo hiểm thất nghiệp (1%)`: `=ROUND(D10*0.01,0)` (`106,000`)
  - `Bảo hiểm khấu trừ lương nhân viên`: `=SUM(D18:D20)` (`1,113,000`)
  - `Tổng lương thuần được nhận`: `=D16-D17-D22` (`26,712,000`)
- Number format: `#,##0;(#,##0);"-"` cho các ô tiền tệ, `0.0` cho giờ công (`176.0`).
- Auto-fit độ rộng cột đủ rộng để không bị `###`.
- Footer chữ ký: `Received by` (`Trần Văn Quyết`) và `Approved by` (`Fujioka Jun`).

---

### Task 3: Cập nhật `verify_50_demos.py` và `50-vi-du-excel/README.md`

**Files:**
- Modify: `slides/Demo/scripts/verify_50_demos.py:96-106,215-220`
- Modify: `slides/Demo/50-vi-du-excel/README.md:25-27,58-95`

- [ ] **Step 1: Cập nhật `verify_50_demos.py`**

- Bỏ kiểm tra bắt buộc tồn tại `mcp_config.json` tại mục 8.
- Thay bằng kiểm tra **không được tồn tại** file `mcp_config.json` dư thừa trong `ws_dir` (`if (ws_dir / "mcp_config.json").exists(): errors.append(...)`).

- [ ] **Step 2: Cập nhật `50-vi-du-excel/README.md`**

- Đổi mục 4 từ `Cấu hình Liên thông MCP (mcp_config.json)` thành `Liên thông MCP Tích hợp sẵn (Gmail & Google Workspace)` — ghi chú rõ Antigravity đã tích hợp sẵn nên không cần file cấu hình `mcp_config.json` rời.
- Cập nhật mô tả các bài trong mục lục từ `(Có MCP Gmail)` / `(Có MCP Google Workspace)` sang `(Tích hợp Gmail)` / `(Tích hợp Google Workspace)` cho đồng bộ.

---

### Task 4: Xóa các file `mcp_config.json` cũ, xóa `ket-noi-mcp-gmail/`, sinh lại dữ liệu và kiểm chứng toàn bộ

**Files:**
- Delete: `slides/Demo/50-vi-du-excel/**/mcp_config.json` (9 files)
- Delete: `slides/Demo/ket-noi-mcp-gmail/`

- [ ] **Step 1: Xóa 9 file `mcp_config.json` cũ và thư mục `ket-noi-mcp-gmail/`**

```bash
find /var/www/html/training-ai/slides/Demo/50-vi-du-excel -name "mcp_config.json" -delete
rm -rf /var/www/html/training-ai/slides/Demo/ket-noi-mcp-gmail
```

- [ ] **Step 2: Chạy lại script sinh toàn bộ 50 bài tập**

Run: `python3 /var/www/html/training-ai/slides/Demo/scripts/generate_50_demos.py`
Expected: Hoàn tất không lỗi.

- [ ] **Step 3: Chạy `verify_50_demos.py` và kiểm tra số liệu thực tế của Bài 04**

Run:
```bash
python3 /var/www/html/training-ai/slides/Demo/scripts/verify_50_demos.py
```
Expected: Exit code 0 (`ALL CHECKS PASSED PERFECTLY`).

Sau đó chạy script Python kiểm tra riêng `bang_luong_chot.xlsx` (15 cột, công thức sống ở K, L, O) và `_ket_qua_mau_chuan.xlsx` (màu sắc `#FFC000`, `#92D050`, `#0070C0`, công thức sống ở cột D, không lỗi `###`) cũng như đảm bảo `find .../50-vi-du-excel -name "mcp_config.json"` trả về rỗng.
