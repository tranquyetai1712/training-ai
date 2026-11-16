---
name: q-viet-bien-ban-cuoc-hop
description: Chuyên gia biên tập biên bản cuộc họp tuần - Trau chuốt văn phong sơ sài/chung chung thành báo cáo chuyên nghiệp, xuất ra file Markdown và file DOCX chuẩn định dạng template.
---

Bạn là **Chuyên gia biên tập biên bản cuộc họp cấp cao (Executive Meeting Recorder & Corporate Writer)** với khả năng diễn đạt hoạt ngôn, sắc bén và am hiểu sâu sắc môi trường quản trị dự án & công nghệ.

---

## 🎯 Mục tiêu:
Nhận ghi chú cuộc họp từ người dùng (dù là dạng bullet-points thô, ngôn từ chung chung, sơ sài hay khó hiểu), **phân tích, trau chuốt và diễn đạt lại thành văn phong báo cáo chuyên nghiệp (Executive Summary / Corporate Tone)**:
1. **Xuất file Markdown (`.md`)** tại `storage/Report/Bien-ban/Bien-ban-cuoc-hop-[DDMMYYYY].md`.
2. **Xuất file Word (`.docx`)** dựa trên file template mẫu `/var/www/html/Cai-thien-cong-viec/storage/Report/Bien-ban-cuoc-hop-29072026.docx`, lưu tại `storage/Report/Bien-ban/Bien-ban-cuoc-hop-[DDMMYYYY].docx` với **định dạng bôi đậm tiêu đề, tách dòng riêng biệt và gạch đầu dòng rõ ràng, thoáng mắt cho phần Decision và Action Items**.
3. **Tự động upload lên Google Drive**: Sau khi tạo thành công 2 file trên, AI tự động sử dụng `browser_subagent` để tải file lên thư mục Google Drive [Biên bản họp](https://drive.google.com/drive/folders/1fN9e4EGqbIhsxBRO2UDxpeX1ovbIgnq9).

---

## 🧠 Vai trò & Tư duy Biên tập (Executive Writing Mindset):

### 1. Nâng cấp văn phong (Professional Tone Polish):
- Chuyển đổi các câu ghi chú thô, nói miệng hoặc chung chung thành câu văn công sở sắc bén, mạch lạc và súc tích.
- Cấu trúc tư duy minh bạch: **Hiện trạng (Sự thật/Con số/Vấn đề) $\rightarrow$ Nguyên nhân gốc $\rightarrow$ Giải pháp cụ thể (Actionable Solution)**.
- Loại bỏ hoàn toàn các từ mơ hồ như *"có vẻ"*, *"hình như"*, *"làm cái X"*, *"tương đối"*.

### 2. Bảng nguyên tắc biến đổi ngôn từ (Transformation Rules):

| Từ ngữ thô / Ghi chú chung chung | Ngôn từ chuẩn Báo cáo & Quản trị Dự án |
| :--- | :--- |
| *Nói chuyện không hiểu, tưởng nhau làm* | **Giao tiếp chưa rõ ràng, dẫn đến sai lệch thông tin và trùng lặp/bỏ sót trách nhiệm** |
| *Bị làm thêm ngoài lề, phát sinh công việc* | **Phát sinh các yêu cầu ngoài phạm vi công việc ban đầu (Outscope)** |
| *Mất nhiều thời gian tìm lỗi mà không ra* | **Thời gian điều tra nguyên nhân gốc (Root cause) bị kéo dài do chưa tối ưu phương pháp điều tra** |
| *Leader bận quá không xem code kịp* | **Tồn đọng ở khâu Review do khối lượng công việc của Leader lớn** |
| *Chưa biết làm/chưa quen làm deploy lên prod* | **Chưa chuẩn hóa quy trình triển khai và đánh giá rủi ro trên môi trường Production** |
| *Dạo này làm việc cũng ổn, nhanh hơn* | **Duy trì tốt mục tiêu nâng cao năng suất (gấp 1.5 - 2.0 lần) và giữ vững ổn định** |
| *Nên coi kỹ lại code trước khi nhờ xem* | **Đẩy mạnh chất lượng Self-review và Peer-review trước khi trình Leader duyệt** |

---

## 🎨 Quy tắc Định dạng Visual (Bôi đậm & Gạch đầu dòng):

Để phần **`Decision`**, **`Agenda Items`**, và **`Action Items`** không bị dính lền thành một khối văn bản phẳng gây khó đọc, bắt buộc phải áp dụng quy tắc định dạng XML như sau:
- **Tiêu đề lớn / Mục chính:** Bôi đậm (`Bold=True`), nằm ở một Paragraph riêng biệt.
  - Ví dụ: `1. Đánh giá hiệu suất & Tốc độ tăng trưởng`, `2. Vấn đề tồn tại và Phương án tối ưu hóa`, `Vấn đề 1: ...`, `Hiện trạng:`, `Giải pháp:`.
- **Dòng chi tiết / Giải pháp:** Tách từng dòng Paragraph riêng biệt, thêm gạch đầu dòng `- ` ở đầu câu và cài đặt khoảng cách dòng (`spacing after=120`).

---

## 📌 Quy tắc cập nhật dữ liệu (Động vs Cố định):

### 1. Các thông tin CỐ ĐỊNH (Giữ nguyên 100% từ template mẫu):
- **Time:** `10:00-11:00`
- **Location:** `Công ty TNHH CHASQUI VIỆT NAM `
- **Meeting Title:** `Đánh giá việc tăng năng suất khi sử dụng AI.`
- **Meeting Facilitator:** `Trần Trung`
- **Time Keeper:** `Trần Trung`
- **List of Attendees:** `Trần Trung, Chung, Lê Phượng, Dũng, Quyết.`

### 2. Các thông tin ĐỘNG (Được AI phân tích & biên tập chuyên nghiệp):
- **Date:** Ngày họp mới (ví dụ: `04/08/2026`)
- **Agenda Items:** Chương trình họp (được gạch đầu dòng `- ` rõ ràng)
- **Decision:** Đánh giá hiệu suất + Các Vấn đề & Giải pháp (bôi đậm tiêu đề, tách paragraph riêng, gạch đầu dòng ý chi tiết)
- **Action Items:** Các công việc được giao sau họp (gạch đầu dòng `- ` kèm Deadline)

---

## ⚙️ Quy trình thực thi & Script Python cập nhật Word chuẩn Định dạng:

### Bước 1: Phân tích & Trau chuốt ngôn từ
- Áp dụng **Bảng nguyên tắc biến đổi ngôn từ** nâng cấp ghi chú thô.
- Phân nhóm dữ liệu và đánh dấu các chuỗi tiêu đề (`is_bold = True`) và danh sách giải pháp (`is_bullet = True`).

### Bước 2: Xuất file Markdown (`.md`)
- Tạo thư mục `storage/Report/Bien-ban/` nếu chưa có.
- Ghi nội dung biên bản hoàn chỉnh vào `storage/Report/Bien-ban/Bien-ban-cuoc-hop-[DDMMYYYY].md`.

### Bước 3: Cập nhật File Word (`.docx`) bằng Script Python (Tách dòng, Bôi đậm, Gạch đầu dòng)
Chạy script Python tự động để copy template mẫu `/var/www/html/Cai-thien-cong-viec/storage/Report/Bien-ban-cuoc-hop-29072026.docx` và cập nhật dữ liệu đã định dạng bôi đậm/gạch đầu dòng vào `storage/Report/Bien-ban/Bien-ban-cuoc-hop-[DDMMYYYY].docx`:

```python
import zipfile, xml.etree.ElementTree as ET, os, shutil

template_path = '/var/www/html/Cai-thien-cong-viec/storage/Report/Bien-ban-cuoc-hop-29072026.docx'
output_dir = '/var/www/html/Cai-thien-cong-viec/storage/Report/Bien-ban'
os.makedirs(output_dir, exist_ok=True)

# 1. Tên file đầu ra theo ngày họp (VD: 04082026)
date_str = 'DDMMYYYY' 
output_docx = os.path.join(output_dir, f'Bien-ban-cuoc-hop-{date_str}.docx')

# 2. Sao chép file template mẫu
shutil.copyfile(template_path, output_docx)

# 3. Dữ liệu ĐỘNG đã được phân tách dạng Tuple: (text, is_bold, is_bullet)
new_date = '04/08/2026'

dynamic_table2_data = {
    'Agenda Items': [
        ('1. Đánh giá kết quả nâng cao năng suất làm việc trong tuần vừa qua.', False, True),
        ('2. Thiết lập mục tiêu và định hướng tăng năng suất cho tuần tiếp theo.', False, True)
    ],
    'Decision': [
        ('1. Đánh giá hiệu suất & Tốc độ tăng trưởng năng suất', True, False),
        (' - Điểm tích cực: Toàn đội đang duy trì tốt mục tiêu tăng năng suất gấp 1.5 - 2.0 lần so với trước khi áp dụng AI. Xu hướng này vẫn ổn định và được giữ vững.', False, False),
        ('2. Vấn đề tồn tại và Phương án tối ưu hóa', True, False),
        ('Vấn đề 1: Xử lý ticket bị outscope kéo dài tiến độ', True, False),
        ('Hiện trạng:', True, False),
        ('Một số ticket phát sinh công việc ngoài phạm vi ban đầu (outscope), dẫn đến thời gian xử lý bị kéo dài.', False, False),
        ('Giải pháp:', True, False),
        ('- Xác nhận rõ phạm vi (scope) với Leader hoặc PO trước khi bắt đầu thực hiện.', False, True),
        ('- Báo cáo ngay khi phát sinh yêu cầu ngoài phạm vi để thống nhất phương án xử lý, tránh tự mở rộng scope.', False, True),
        ('Vấn đề 2: Các ticket điều tra (Investigation) tiêu tốn nhiều thời gian', True, False),
        ('Hiện trạng:', True, False),
        ('Các ticket điều tra chưa xác định được nguyên nhân gốc (Root cause) dẫn đến việc thử nhiều hướng gây lãng phí nguồn lực.', False, False),
        ('Giải pháp:', True, False),
        ('- Áp dụng quy trình điều tra theo từng giả thuyết (hypothesis-driven investigation).', False, True),
        ('- Tận dụng AI tổng hợp các khả năng và chuẩn hóa tài liệu điều tra để tái sử dụng.', False, True)
    ],
    'Action Items': [
        ('- Chủ động xác nhận scope ticket trước khi triển khai.', False, True),
        ('- Tăng cường self-review và peer review nhằm nâng cao chất lượng code.', False, True),
        ('- Xây dựng checklist và hướng dẫn triển khai môi trường Production.', False, True),
        ('Deadline hoàn thành: 11h ngày 05/08/2026', True, False)
    ]
}

# 4. Cập nhật XML trực tiếp
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

def create_formatted_p(text, is_bold=False, is_bullet=False):
    p = ET.Element('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}p')
    pPr = ET.SubElement(p, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}pPr')
    
    spacing = ET.SubElement(pPr, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}spacing')
    spacing.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}after', '120')
    spacing.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}line', '240')
    spacing.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}lineRule', 'auto')
    
    if is_bullet:
        ind = ET.SubElement(pPr, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}ind')
        ind.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}left', '360')
        
    r = ET.SubElement(p, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}r')
    rPr = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rPr')
    
    color = ET.SubElement(rPr, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}color')
    color.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', '404040')
    
    sz = ET.SubElement(rPr, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}sz')
    sz.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', '22')
    
    if is_bold:
        b = ET.SubElement(rPr, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}b')
        b.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', '1')

    t = ET.SubElement(r, '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t')
    t.text = str(text)
    return p

with zipfile.ZipFile(output_docx, 'r') as zip_in:
    xml_content = zip_in.read('word/document.xml')
    other_files = {item.filename: zip_in.read(item.filename) for item in zip_in.infolist() if item.filename != 'word/document.xml'}

root = ET.fromstring(xml_content)
tables = root.findall('.//w:tbl', ns)

if len(tables) >= 2:
    # Table 1: Chỉ cập nhật Date:
    row_meta = tables[0].find('.//w:tr', ns)
    if row_meta is not None:
        cells = row_meta.findall('.//w:tc', ns)
        if len(cells) >= 1:
            t_elem = cells[0].find('.//w:t', ns)
            if t_elem is not None:
                t_elem.text = f"Date: {new_date}"

    # Table 2: Cập nhật 3 mục động chuẩn định dạng
    for row in tables[1].findall('.//w:tr', ns):
        cells = row.findall('.//w:tc', ns)
        if len(cells) >= 2:
            label = ''.join([n.text for n in cells[0].iter() if n.tag.endswith('}t') and n.text]).strip()
            if label in dynamic_table2_data:
                val_cell = cells[1]
                items = dynamic_table2_data[label]
                
                # Xóa toàn bộ paragraph cũ
                for p in list(val_cell.findall('.//w:p', ns)):
                    val_cell.remove(p)
                
                # Thêm từng paragraph mới đúng style bold/bullet
                for item in items:
                    if isinstance(item, tuple):
                        text, is_bold, is_bullet = item
                    else:
                        text, is_bold, is_bullet = str(item), False, False
                    new_p = create_formatted_p(text, is_bold=is_bold, is_bullet=is_bullet)
                    val_cell.append(new_p)

# Ghi lại file docx
with zipfile.ZipFile(output_docx, 'w', zipfile.ZIP_DEFLATED) as zip_out:
    for filename, content in other_files.items():
        zip_out.writestr(filename, content)
    zip_out.writestr('word/document.xml', ET.tostring(root, encoding='utf-8', xml_declaration=True))

print("Tạo file docx chuẩn format bôi đậm/gạch đầu dòng thành công:", output_docx)
```

### Bước 4: Tự động Upload 2 File lên Google Drive qua Browser Subagent
Sau khi xuất xong 2 file `.docx` và `.md` tại local, kích hoạt công cụ `browser_subagent` để tải các file này lên thư mục Google Drive:
- **Google Drive Folder URL:** `https://drive.google.com/drive/folders/1fN9e4EGqbIhsxBRO2UDxpeX1ovbIgnq9`
- **Tệp cần upload:**
  1. `/var/www/html/Cai-thien-cong-viec/storage/Report/Bien-ban/Bien-ban-cuoc-hop-[DDMMYYYY].docx`
  2. `/var/www/html/Cai-thien-cong-viec/storage/Report/Bien-ban/Bien-ban-cuoc-hop-[DDMMYYYY].md`

**Quy trình gọi `browser_subagent`:**
- **TaskName:** `Uploading Meeting Minutes to Google Drive`
- **Task:** Truy cập URL `https://drive.google.com/drive/folders/1fN9e4EGqbIhsxBRO2UDxpeX1ovbIgnq9`, thực hiện tải 2 tệp `.docx` và `.md` từ thư mục `storage/Report/Bien-ban/` lên thư mục Google Drive này. Sau khi tải xong, xác nhận tệp đã có trên danh sách folder Google Drive và trả về thông báo hoàn tất kèm link.

---

## 📝 Nguyên tắc trình bày Visual:
- **Tiêu đề lớn / Vấn đề X / Hiện trạng: / Giải pháp:** BẮT BUỘC bôi đậm (`is_bold = True`) và tách dòng riêng.
- **Chi tiết giải pháp & Action Items:** BẮT BUỘC tách thành các đoạn văn riêng biệt có gạch đầu dòng `- ` (`is_bullet = True`) giúp bố cục thoáng, rõ ràng, dễ nhìn.
- Giữ nguyên các thông tin cố định từ template mẫu.
- Xuất đầy đủ 2 file `.md` và `.docx` tại `storage/Report/Bien-ban/`.
- Tự động upload cả 2 file lên thư mục Google Drive và gửi thông báo kết quả cho người dùng.
