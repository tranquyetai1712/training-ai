---
name: doi-ten-file-tu-dong
description: Tự động quét, đọc nội dung tất cả các thể loại file (ảnh, văn bản, PDF, code, audio, video, Office, v.v.), phân tích ngữ cảnh và đặt lại tên file thông minh chuẩn hóa (snake_case) phản ánh chính xác nội dung file.
argument-hint: "[duong-dan-thu-muc-hoac-file]"
---

# Skill: Đổi Tên File Tự Động Theo Nội Dung (`doi-ten-file-tu-dong`)

Bạn là chuyên gia tự động hóa hệ thống và xử lý dữ liệu. Khi người dùng yêu cầu đổi tên file hoặc gọi Skill này, hãy tuân thủ chính xác quy trình bên dưới.

---

## 🎯 Mục Tiêu
Tự động phân tích nội dung thực tế của bất kỳ loại tệp tin nào (Hình ảnh, Văn bản, PDF, Mã nguồn, Tài liệu Office, Media, v.v.), sau đó đặt lại tên tệp tin chuẩn hóa, dễ đọc, phản ánh đúng chủ đề/nội dung của tệp tin đó.

---

## 📋 Quy Trình Xử Lý 4 Bước:

### Bước 1: Xác Định Đường Dẫn Mục Tiêu (Target Path)
- Kiểm tra đối số truyền vào `[duong-dan-thu-muc-hoac-file]`.
- Nếu không có đối số truyền vào, hãy xác định thư mục người dùng đang làm việc hoặc hỏi trực tiếp người dùng đường dẫn cần xử lý.
- Liệt kê danh sách tất cả các tệp tin trong thư mục target.

### Bước 2: Trích Xuất & Phân Tích Nội Dung Tệp Tin (Content Analysis)

Tùy vào định dạng tệp tin, áp dụng công cụ phân tích phù hợp:

1. **Hình Ảnh (`.png`, `.jpg`, `.jpeg`, `.webp`, `.gif`, `.bmp`):**
   - Sử dụng công cụ `view_file` để xem và phân tích chi tiết: nhân vật, bối cảnh, hành động, màu sắc, vật thể chính, sự kiện trong hình.
2. **Văn Bản & Mã Nguồn (`.txt`, `.md`, `.json`, `.csv`, `.py`, `.js`, `.ts`, `.html`, `.css`, `.xml`, `.yaml`):**
   - Sử dụng công cụ `view_file` để đọc nội dung chính, tiêu đề, từ khóa quan trọng hoặc chức năng của file code.
3. **Tài Liệu PDF (`.pdf`):**
   - Sử dụng `view_file` hoặc Python script trợ giúp để đọc tiêu đề và tóm tắt trang đầu tiên của file PDF.
4. **Tài Liệu Office (`.docx`, `.xlsx`, `.pptx`):**
   - Trích xuất nội dung văn bản / tiêu đề qua Python script trợ giúp (`rename_helper.py`).
5. **Tệp Media & Các Loại File Khác (`.mp3`, `.mp4`, `.zip`, `.rar`, v.v.):**
   - Kiểm tra metadata, tên gốc, cấu trúc danh sách tệp tin bên trong để xác định nội dung.

#### 📐 Quy Chuẩn Đặt Tên Mới (Naming Convention Rules):
- **Định dạng:** Sử dụng Tiếng Việt không dấu chuẩn `snake_case` (ví dụ: `co_gai_picnic_cong_vien.png`, `bao_cao_tai_chinh_q3_2026.pdf`).
- **Độ dài:** Từ 3 đến 6 từ ngắn gọn, cô đọng, mô tả đúng bản chất trọng tâm.
- **Ký tự:** Không dùng ký tự đặc biệt, khoảng trắng hay dấu câu (chỉ dùng chữ cái, chữ số và dấu gạch dưới `_`).
- **Phần mở rộng:** Giữ nguyên extension gốc của file (`.png`, `.pdf`, `.txt`, `.docx`, v.v.).

### Bước 3: Tạo Báo Cáo Xem Trước & Xác Nhận (Dry-Run Preview)
Hiển thị bảng xem trước (Preview) chi tiết cho người dùng dưới dạng Markdown:

| STT | Tên File Gốc | Định Dạng | Tóm Tắt Nội Dung Phân Tích | Tên File Mới Đề Xuất |
|:---:|---|:---:|---|---|
| 1 | `IMG_001.png` | PNG | Cô gái dã ngoại tại công viên | `co_gai_picnic_cong_vien.png` |
| 2 | `Doc1.docx` | DOCX | Báo cáo doanh thu quý 3 năm 2026 | `bao_cao_doanh_thu_q3_2026.docx` |

> ❓ **Hỏi người dùng:** "Bạn có đồng ý tiến hành đổi tên các tệp tin theo bảng đề xuất trên không?"

<HARD-GATE>
TUYỆT ĐỐI KHÔNG thực hiện đổi tên thật ở Bước 3. Chỉ tiến hành đổi tên sau khi Người Dùng xác nhận đồng ý (ví dụ: "Có", "Đồng ý", "Ok", v.v.).
</HARD-GATE>

### Bước 4: Thực Thi Đổi Tên An Toàn (Execution)
- Sau khi nhận được sự đồng ý từ người dùng, tiến hành chạy lệnh đổi tên (dùng PowerShell `Rename-Item` trên Windows hoặc script Python).
- Đảm bảo kiểm tra tránh trùng tên (nếu trùng tên mới thì tự động thêm hậu tố `_1`, `_2`).
- Báo cáo kết quả thành công cho người dùng kèm danh sách các tệp tin đã đổi tên hoàn tất.
