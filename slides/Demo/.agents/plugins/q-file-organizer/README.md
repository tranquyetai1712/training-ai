# Plugin `q-file-organizer` - Quản Lý, Phân Loại & Đổi Tên Tệp Tin Tự Động Bằng AI

Plugin hỗ trợ tự động hóa dọn dẹp, phân loại và chuẩn hóa tên tệp tin thông minh dựa trên việc **đọc và hiểu nội dung thực tế** bên trong (hình ảnh, tài liệu PDF, Word, bảng tính Excel, mã nguồn, tệp đa phương tiện) thay vì chỉ dựa vào tên hay phần mở rộng ban đầu.

---

## 📁 Cấu Trúc Thư Mục

```text
q-file-organizer/
├── plugin.json                                      # Khai báo thông tin plugin (version 1.1.0)
├── README.md                                        # Tài liệu hướng dẫn sử dụng plugin
└── skills/
    ├── doi-ten-file-tu-dong/                        # Skill 1: Đổi tên tệp tin theo nội dung
    │   ├── SKILL.md
    │   └── scripts/
    │       └── rename_helper.py                     # Script Python trích xuất nội dung & đổi tên
    └── phan-loai-file-tu-dong/                      # Skill 2: Phân loại & gom nhóm thư mục
        ├── SKILL.md
        └── scripts/
            ├── organize_files.py                    # Script phân loại bằng Python
            └── organize_files.js                    # Script phân loại bằng Node.js
```

---

## 🛠 Danh Sách Skills & Chức Năng

Plugin cung cấp 2 kỹ năng chuyên biệt:

### 1. `doi-ten-file-tu-dong` (Đổi Tên Tệp Tin Thông Minh)

Tự động quét tệp tin, trích xuất nội dung và đề xuất tên mới có ý nghĩa, dễ tìm kiếm.

* **Khả năng phân tích đa định dạng:**
  - **Hình ảnh (`.png`, `.jpg`, `.jpeg`, `.webp`, `.gif`):** AI Vision quan sát đối tượng, bối cảnh, hành động và sự kiện thực tế trong ảnh.
  - **Tài liệu văn bản & Mã nguồn (`.txt`, `.md`, `.json`, `.csv`, `.py`, `.js`, `.ts`, `.html`,...):** Trích đoạn đọc nội dung, mục đích và chức năng chính.
  - **Tài liệu PDF (`.pdf`):** Đọc trang đầu để lấy tiêu đề tài liệu hoặc bản tóm tắt nội dung.
  - **Tài liệu Office (`.docx`, `.xlsx`, `.pptx`):** Trích xuất tiêu đề văn bản qua thư viện hỗ trợ.
  - **Media & Tệp nén (`.mp3`, `.mp4`, `.zip`, `.rar`):** Đọc metadata và danh sách thành phần bên trong.

* **Tiêu chuẩn đặt tên mới (Naming Conventions):**
  - Định dạng: Tiếng Việt không dấu chuẩn `snake_case` (ví dụ: `bao_cao_tai_chinh_q3_2026.pdf`, `hop_dong_thue_nha_mat_bang.docx`).
  - Độ dài: Từ 3 đến 6 từ ngắn gọn, trọng tâm.
  - Phần mở rộng: Giữ nguyên đuôi tệp tin gốc.
  - Chống trùng lặp: Tự động thêm hậu tố `_1`, `_2` nếu trùng tên trong cùng thư mục.

* **Cơ chế an toàn (Dry-Run Preview Gate):**
  - Hiển thị bảng so sánh đối chiếu: `Tên cũ ➡️ Tóm tắt nội dung ➡️ Tên mới đề xuất`.
  - **Chỉ thực thi khi người dùng xác nhận đồng ý** ("Có", "Đồng ý", "OK"). Tuyệt đối không tự ý đổi tên trước khi có sự chấp thuận.

---

### 2. `phan-loai-file-tu-dong` (Phân Loại & Dọn Dẹp Thư Mục)

Tự động quét các tệp tin nằm rải rác từ thư mục Nguồn (ví dụ: `Downloads`, `Desktop`) và di chuyển ngăn nắp vào các thư mục con chuyên biệt trong thư mục Đích (ví dụ: `Documents/TaiLieu`).

* **Hệ thống danh mục phân loại tự động (`CATEGORIES`):**
  - `KeToan_TaiChinh`: Hóa đơn điện tử, invoice, VAT, sao kê ngân hàng, phiếu thu chi, biên lai thanh toán.
  - `NhanSu_TuyenDung`: CV ứng viên, sơ yếu lý lịch, bảng chấm công, phiếu lương, hợp đồng lao động.
  - `HocTap_NghienCuu`: Giáo trình, tài liệu tham khảo, luận văn, bài giảng, slide bài tập, ebook.
  - `CongViec_DuAn`: Bản chào giá, proposal, biên bản cuộc họp, đặc tả kỹ thuật dự án.
  - `Media_GiaiTri`: Hình ảnh, video, audio ca nhạc (`.png`, `.jpg`, `.mp4`, `.mp3`,...).
  - `PhanMem_CaiDat`: Bộ cài đặt phần mềm (`.exe`, `.msi`, `.deb`, `.dmg`, `.iso`, `.apk`,...).
  - `TepTinKhac`: Các tệp tin không nhận diện được từ khóa hoặc định dạng đặc biệt.

* **Cơ chế an toàn doanh nghiệp (Enterprise Safety):**
  - **Dry-Run Preview Gate:** Luôn chạy chế độ preview trước để xuất danh sách đường dẫn gốc và đường dẫn đích dự kiến. Bắt buộc hỏi xác nhận người dùng trước khi tiến hành di chuyển thật.
  - **Chống ghi đè (Collision Prevention):** Tự động phát hiện trùng tên ở thư mục đích và thêm hậu tố số tăng dần (`_1`, `_2`) thay vì ghi đè mất file.
  - **Lọc tệp rác hệ thống:** Tự động bỏ qua file tạm, file lock (`~$*`, `.tmp`), file hệ thống (`.DS_Store`, `Thumbs.db`, `desktop.ini`).
  - **Hoàn tác an toàn (Undo / Rollback):** Tự động ghi lại lịch sử di chuyển vào file `.organize_history_<timestamp>.json`, hỗ trợ phục hồi 100% nguyên trạng với cờ `--undo`.

---

## 🚀 Hướng Dẫn Sử Dụng

### 1. Sử Dụng Trực Tiếp Qua Chat AI (Khuyên Dùng)

#### Đổi tên tệp tin:
```text
"Hãy đổi tên các file ảnh và tài liệu trong thư mục D:\Downloads\ChuaPhanLoai theo nội dung của chúng."
```

#### Phân loại và dọn dẹp thư mục:
```text
"Dọn dẹp và phân loại tự động các file trong thư mục C:\Users\SingPC\Downloads sang thư mục D:\TaiLieu."
```

---

### 2. Sử Dụng Qua Dòng Lệnh (CLI)

#### A. Đổi tên tệp tin với `rename_helper.py`:
```bash
# 1. Quét thông tin và trích xuất tóm tắt nội dung các file trong thư mục
python skills/doi-ten-file-tu-dong/scripts/rename_helper.py --path "D:/Downloads/Temp"

# 2. Thực thi đổi tên theo chuỗi JSON mapping
python skills/doi-ten-file-tu-dong/scripts/rename_helper.py --path "D:/Downloads/Temp" --execute --rename-mapping "{\"IMG_001.png\": \"co_gai_picnic_cong_vien.png\", \"Doc1.docx\": \"bao_cao_doanh_thu_q3_2026.docx\"}"
```

#### B. Phân loại tệp tin với Python (`organize_files.py`):
```bash
# 1. Chạy chế độ xem trước (Dry-Run Preview)
python skills/phan-loai-file-tu-dong/scripts/organize_files.py --source "D:/Downloads" --dest "D:/TaiLieu" --dry-run

# 2. Thực thi di chuyển thật sau khi đã kiểm tra (tự sinh file log history)
python skills/phan-loai-file-tu-dong/scripts/organize_files.py --source "D:/Downloads" --dest "D:/TaiLieu" --execute

# 3. Hoàn tác đưa các file về lại vị trí cũ khi cần
python skills/phan-loai-file-tu-dong/scripts/organize_files.py --undo "D:/TaiLieu/.organize_history_20261022_165503.json"
```

#### C. Phân loại tệp tin với Node.js (`organize_files.js`):
```bash
# 1. Chạy chế độ xem trước (Dry-Run Preview)
node skills/phan-loai-file-tu-dong/scripts/organize_files.js --source "D:/Downloads" --dest "D:/TaiLieu" --dry-run

# 2. Thực thi di chuyển thật
node skills/phan-loai-file-tu-dong/scripts/organize_files.js --source "D:/Downloads" --dest "D:/TaiLieu" --execute

# 3. Hoàn tác đưa các file về lại vị trí cũ
node skills/phan-loai-file-tu-dong/scripts/organize_files.js --undo "D:/TaiLieu/.organize_history_20261022_165503.json"
```

---

## 📋 Bảng So Sánh Các Skill Trong Plugin

| Tiêu Chí | `doi-ten-file-tu-dong` | `phan-loai-file-tu-dong` |
|---|---|---|
| **Mục đích** | Chuẩn hóa tên file theo nội dung | Gom nhóm file vào các thư mục theo chủ đề |
| **Công nghệ chính** | AI Vision + Text Snippet + Python Slug | Keyword Search + File Extension Matching |
| **Thao tác tệp** | Đổi tên file tại chỗ (`Rename`) | Di chuyển file sang thư mục đích (`Move`) |
| **Cơ chế an toàn** | Bảng Preview Markdown + Chờ xác nhận | Tham số `--dry-run` + Bảng Preview + Chờ xác nhận |
| **Runtime hỗ trợ** | Python 3 | Python 3 & Node.js |
