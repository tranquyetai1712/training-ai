# Chuẩn Bị Tài Nguyên & Kịch Bản Livestream `/schedule` Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Xây dựng trọn bộ tài nguyên chuẩn bị cho buổi livestream hướng dẫn lệnh `/schedule` gồm: 2 bộ dữ liệu mock data thực chiến (`danh_sach_hop_dong.xlsx`, `tu_vung_ielts.txt`), tài liệu quà tặng Cheat Sheet 30 Prompt mẫu, và Sổ tay kịch bản người dẫn (Speaker Notes & Cue Sheet) kèm bộ kiểm thử tự động.

**Architecture:** Sử dụng Python (`pandas`/`openpyxl`) để tạo dữ liệu Excel giả lập có logic ngày tháng động chính xác phục vụ Demo 2; chuẩn bị tệp flashcard cấu trúc chuẩn cho Demo 3; xuất bản tài liệu Markdown định dạng chuyên nghiệp phục vụ phát sóng trực tiếp; và viết bộ kiểm thử pytest/python unittest để xác thực tính toàn vẹn của tất cả tài nguyên trước buổi live.

**Tech Stack:** Python 3, OpenPyXL / Pandas, Markdown, Pytest / Unittest, Git.

**Spec:** [docs/superpowers/specs/2026-11-13-schedule-livestream-guide-design.md](file:///var/www/html/training-ai/slides/Demo/docs/superpowers/specs/2026-11-13-schedule-livestream-guide-design.md)

## Global Constraints

- Toàn bộ file mock data đặt ngay tại thư mục gốc workspace (`/var/www/html/training-ai/slides/Demo`) để đảm bảo lệnh prompt trên live ngắn gọn, không bị lỗi đường dẫn.
- Dữ liệu ngày tháng trong `danh_sach_hop_dong.xlsx` phải đảm bảo có ít nhất 2 bản ghi sắp hết hạn trong vòng 3-7 ngày tính từ thời điểm chạy live.
- File `tu_vung_ielts.txt` phải có cấu trúc nhất quán gồm phiên âm, từ loại, định nghĩa tiếng Việt và ví dụ ngữ cảnh văn phòng.
- Tài liệu Cheat Sheet phải đủ 30 kịch bản được phân chia theo đúng 4 nhóm ngành như trong bản thiết kế spec.
- Không commit các file trong thư mục `docs/skills/` lên git theo quy tắc dự án.

## Review Focus

1. **Ngày hết hạn động (Dynamic Expiration Date):** File Excel nếu fix cứng ngày trong quá khứ sẽ làm AI lọc sai kết quả khi demo trực tiếp.
2. **Ký tự đặc biệt & Unicode trong Excel/Text:** Tránh lỗi mã hóa tiếng Việt có dấu khi AI đọc file qua tool shell/python.
3. **Cú pháp Cron 5 trường chuẩn:** Toàn bộ 30 câu prompt trong cheat sheet phải có cú pháp cron chuẩn xác đi kèm ví dụ ngôn ngữ tự nhiên.
4. **Tính nhất quán giữa Speaker Notes và Spec:** Mốc timeline 60 phút trong speaker notes phải khớp từng phút với timeline trong spec.
5. **Kịch bản Failsafe khả thi:** Mọi lỗi tiềm ẩn trên live (mạng lag, AI đọc sai cột) phải có sẵn câu trả lời mẫu cứu nguy trong speaker notes.

---

### Task 1: Tạo Script Sinh & Kiểm Thử Dữ Liệu Excel Hợp Đồng (`danh_sach_hop_dong.xlsx`)

**Files:**
- Create: `scripts/generate_contract_mock.py`
- Create: `tests/test_mock_data.py`
- Produces: `danh_sach_hop_dong.xlsx`

**Interfaces:**
- Consumes: Cấu trúc cột từ Spec: `Mã NV`, `Họ và Tên`, `Phòng Ban`, `Loại Hợp Đồng`, `Ngày Hết Hạn`.
- Produces: File Excel `danh_sach_hop_dong.xlsx` tại gốc workspace với ít nhất 5 nhân viên, trong đó 2 nhân viên có ngày hết hạn sau 3-5 ngày tính từ ngày hiện tại.

- [ ] **Step 1: Viết test kiểm tra tính hợp lệ của file Excel mock data**

Viết file `tests/test_mock_data.py` kiểm tra file `danh_sach_hop_dong.xlsx` tồn tại, đủ các cột cần thiết và có ít nhất 2 bản ghi sắp hết hạn trong vòng 7 ngày.

```python
import os
import openpyxl
from datetime import datetime, timedelta

def test_contract_excel_structure():
    file_path = "danh_sach_hop_dong.xlsx"
    assert os.path.exists(file_path), f"File {file_path} does not exist"
    
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    headers = [cell.value for cell in sheet[1]]
    expected_headers = ["Mã NV", "Họ và Tên", "Phòng Ban", "Loại Hợp Đồng", "Ngày Hết Hạn"]
    assert headers == expected_headers, f"Headers mismatch: {headers} vs {expected_headers}"
    
    rows = list(sheet.iter_rows(min_row=2, values_only=True))
    assert len(rows) >= 5, "Dataset must contain at least 5 rows"
    
    now = datetime.now()
    expiring_soon_count = 0
    for row in rows:
        exp_date_val = row[4]
        if isinstance(exp_date_val, datetime):
            diff = (exp_date_val - now).days
            if 0 <= diff <= 7:
                expiring_soon_count += 1
        elif isinstance(exp_date_val, str):
            exp_date = datetime.strptime(exp_date_val, "%Y-%m-%d")
            diff = (exp_date - now).days
            if 0 <= diff <= 7:
                expiring_soon_count += 1
                
    assert expiring_soon_count >= 2, f"Expected at least 2 expiring records within 7 days, got {expiring_soon_count}"
```

- [ ] **Step 2: Chạy test để xác nhận test FAIL (do chưa có file excel)**

Run: `python3 -m pytest tests/test_mock_data.py -v`
Expected: FAIL với lỗi file không tồn tại.

- [ ] **Step 3: Viết script `scripts/generate_contract_mock.py` và chạy tạo file Excel**

```python
import os
from datetime import datetime, timedelta
import openpyxl

def generate_mock_excel(filename="danh_sach_hop_dong.xlsx"):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "TheoDoiHopDong"
    
    headers = ["Mã NV", "Họ và Tên", "Phòng Ban", "Loại Hợp Đồng", "Ngày Hết Hạn"]
    ws.append(headers)
    
    today = datetime.now()
    
    employees = [
        ("NV001", "Nguyễn Văn An", "Marketing", "Thử việc 2 tháng", (today + timedelta(days=3)).strftime("%Y-%m-%d")),
        ("NV002", "Trần Thị Bích", "Kỹ thuật", "Thử việc 2 tháng", (today + timedelta(days=5)).strftime("%Y-%m-%d")),
        ("NV003", "Lê Hoàng Nam", "Kinh doanh", "Chính thức 1 năm", (today + timedelta(days=45)).strftime("%Y-%m-%d")),
        ("NV004", "Phạm Thu Thảo", "Nhân sự", "Thử việc 2 tháng", (today + timedelta(days=20)).strftime("%Y-%m-%d")),
        ("NV005", "Vũ Minh Quân", "Thiết kế", "Chính thức 1 năm", (today + timedelta(days=90)).strftime("%Y-%m-%d")),
        ("NV006", "Đặng Thùy Dung", "Kế toán", "Chính thức 1 năm", (today - timedelta(days=10)).strftime("%Y-%m-%d")),
    ]
    
    for emp in employees:
        ws.append(list(emp))
        
    wb.save(filename)
    print(f"Generated {filename} successfully with {len(employees)} records.")

if __name__ == "__main__":
    generate_mock_excel()
```

Chạy script tạo file: `python3 scripts/generate_contract_mock.py`

- [ ] **Step 4: Chạy lại test để xác nhận PASS**

Run: `python3 -m pytest tests/test_mock_data.py -v`
Expected: PASS

- [ ] **Step 5: Commit task 1**

```bash
git add scripts/generate_contract_mock.py tests/test_mock_data.py danh_sach_hop_dong.xlsx
git commit -m "feat(mock-data): add script and test for contract excel dataset"
```

---

### Task 2: Tạo & Kiểm Thử Dữ Liệu Flashcard Từ Vựng (`tu_vung_ielts.txt`)

**Files:**
- Create: `tu_vung_ielts.txt`
- Create: `tests/test_flashcards.py`

**Interfaces:**
- Produces: `tu_vung_ielts.txt` tại gốc workspace với tối thiểu 8-10 từ vựng chuyên nghiệp theo cấu trúc chuẩn.

- [ ] **Step 1: Viết test kiểm tra tính hợp lệ của file `tu_vung_ielts.txt`**

```python
import os

def test_flashcard_file():
    file_path = "tu_vung_ielts.txt"
    assert os.path.exists(file_path), f"File {file_path} does not exist"
    
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]
        
    assert len(lines) >= 8, f"Expected at least 8 vocab entries, got {len(lines)}"
    for line in lines:
        assert "/" in line, f"Line missing pronunciation slash: {line}"
        assert ":" in line, f"Line missing colon separator: {line}"
```

- [ ] **Step 2: Chạy test để xác nhận test FAIL**

Run: `python3 -m pytest tests/test_flashcards.py -v`
Expected: FAIL

- [ ] **Step 3: Tạo nội dung `tu_vung_ielts.txt`**

Tạo file `tu_vung_ielts.txt` chứa 10 từ vựng thực tế ứng dụng trong môi trường văn phòng & học tập:
```text
# Danh sách từ vựng IELTS & Business English ôn tập ngắt quãng
1. Ubiquitous /juːˈbɪk.wə.təs/ (adj): Có mặt ở khắp mọi nơi (e.g. AI tools are becoming ubiquitous in modern office work).
2. Procrastinate /prəʊˈkræs.tɪ.neɪt/ (verb): Trì hoãn công việc (e.g. Do not procrastinate on setting up automated workflows).
3. Resilience /rɪˈzɪl.jəns/ (noun): Khả năng phục hồi, kiên cường (e.g. The company demonstrated great resilience during the crisis).
4. Streamline /ˈstriːm.laɪn/ (verb): Tinh gọn hóa quy trình (e.g. We use Antigravity schedule to streamline our daily reporting).
5. Paradigm /ˈpær.ə.daɪm/ (noun): Mô hình, hình mẫu mẫu mực (e.g. Autonomous AI agents represent a new paradigm of productivity).
6. Pragmatic /præɡˈmæt.ɪk/ (adj): Thực tế, thực dụng (e.g. We need a pragmatic approach to project deadline management).
7. Leverage /ˈliː.vər.ɪdʒ/ (verb): Đòn bẩy, tận dụng tối đa (e.g. Workers who leverage AI schedule will outpace traditional workers).
8. Discrepancy /dɪˈskrep.ən.si/ (noun): Sự sai lệch, khác biệt (e.g. The agent detected a discrepancy in the invoice total).
9. Bottleneck /ˈbɒt.əl.nek/ (noun): Điểm nghẽn quy trình (e.g. Daily standup schedules help identify workflow bottlenecks early).
10. Synchronous /ˈsɪŋ.krə.nəs/ (adj): Đồng bộ (e.g. Non-blocking schedules free users from synchronous waiting).
```

- [ ] **Step 4: Chạy lại test để xác nhận PASS**

Run: `python3 -m pytest tests/test_flashcards.py -v`
Expected: PASS

- [ ] **Step 5: Commit task 2**

```bash
git add tu_vung_ielts.txt tests/test_flashcards.py
git commit -m "feat(mock-data): add vocab flashcard dataset and unit tests"
```

---

### Task 3: Xây Dựng Bản Cheat Sheet 30 Prompt Thực Chiến (`docs/schedule-livestream/cheat-sheet-30-prompts.md`)

**Files:**
- Create: `docs/schedule-livestream/cheat-sheet-30-prompts.md`
- Create: `tests/test_cheat_sheet.py`

**Interfaces:**
- Produces: Tài liệu Markdown hoàn chỉnh, có mục lục, chia 4 nhóm rõ ràng, mỗi prompt có cú pháp tự nhiên, biểu thức cron tương ứng, và chú thích công cụ liên quan.

- [ ] **Step 1: Viết test kiểm tra tệp Cheat Sheet**

```python
import os

def test_cheat_sheet_contents():
    file_path = "docs/schedule-livestream/cheat-sheet-30-prompts.md"
    assert os.path.exists(file_path), f"File {file_path} does not exist"
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    for i in range(1, 31):
        assert f"### Ví dụ {i}:" in content or f"### {i}." in content, f"Missing prompt example {i}"
        
    assert "Nhóm 1:" in content or "Văn Phòng" in content
    assert "Nhóm 2:" in content or "Học Tập" in content
    assert "Nhóm 3:" in content or "Marketing" in content
    assert "Nhóm 4:" in content or "Năng Suất" in content
```

- [ ] **Step 2: Chạy test để xác nhận test FAIL**

Run: `python3 -m pytest tests/test_cheat_sheet.py -v`
Expected: FAIL

- [ ] **Step 3: Soạn thảo toàn bộ nội dung file `docs/schedule-livestream/cheat-sheet-30-prompts.md`**

Đầy đủ 30 kịch bản, mỗi kịch bản có:
- Tên tình huống thực tế
- Khung lệnh copy-paste (ngôn ngữ tự nhiên)
- Biểu thức Cron tương đương
- Các tool hỗ trợ (Gmail, Sheets, Slack, Search...)
- Ghi chú mẹo sử dụng.

- [ ] **Step 4: Chạy lại test để xác nhận PASS**

Run: `python3 -m pytest tests/test_cheat_sheet.py -v`
Expected: PASS

- [ ] **Step 5: Commit task 3**

```bash
git add docs/schedule-livestream/cheat-sheet-30-prompts.md tests/test_cheat_sheet.py
git commit -m "docs(livestream): add comprehensive 30 prompt cheat sheet for audience"
```

---

### Task 4: Xây Dựng Sổ Tay Kịch Bản Người Dẫn (`docs/schedule-livestream/live-speaker-notes.md`)

**Files:**
- Create: `docs/schedule-livestream/live-speaker-notes.md`
- Create: `tests/test_speaker_notes.py`

**Interfaces:**
- Produces: Kịch bản từng phút (Minute-by-minute Host Script) có lời thoại gợi ý (Talking points), hành động kỹ thuật trên màn hình (On-screen actions), các câu hỏi tương tác với khán giả (Audience hooks), và bảng xử lý sự cố trực tiếp (Failsafe checklist).

- [ ] **Step 1: Viết test kiểm tra tệp Speaker Notes**

```python
import os

def test_speaker_notes():
    file_path = "docs/schedule-livestream/live-speaker-notes.md"
    assert os.path.exists(file_path), f"File {file_path} does not exist"
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    required_sections = [
        "TIMELINE TỪNG PHÚT",
        "HERO DEMO 1",
        "HERO DEMO 2",
        "HERO DEMO 3",
        "TASK MANAGER",
        "FAILSAFE"
    ]
    for sec in required_sections:
        assert sec in content.upper(), f"Missing required section: {sec}"
```

- [ ] **Step 2: Chạy test để xác nhận test FAIL**

Run: `python3 -m pytest tests/test_speaker_notes.py -v`
Expected: FAIL

- [ ] **Step 3: Soạn thảo nội dung `docs/schedule-livestream/live-speaker-notes.md`**

Bao gồm:
- Checklist trước giờ lên sóng 15 phút (âm thanh, màn hình, terminal, reset workspace).
- Lời thoại mở màn giật gân, so sánh sự khác biệt.
- Cues chuyển slide và thao tác gõ terminal.
- Lời kêu gọi khán giả tương tác (comment, thả tim, chọn đáp án quiz).
- Các câu hỏi xử lý tình huống hóc búa (tắt máy có chạy không, giới hạn token, cách debug).

- [ ] **Step 4: Chạy lại test để xác nhận PASS**

Run: `python3 -m pytest tests/test_speaker_notes.py -v`
Expected: PASS

- [ ] **Step 5: Commit task 4**

```bash
git add docs/schedule-livestream/live-speaker-notes.md tests/test_speaker_notes.py
git commit -m "docs(livestream): add complete live speaker notes and host cue sheet"
```

---

### Task 5: Kiểm Thử Toàn Diện Bộ Tài Nguyên Livestream (End-to-End Verification)

**Files:**
- Create: `tests/test_e2e_livestream_assets.py`

- [ ] **Step 1: Viết test E2E kiểm tra toàn bộ hệ thống tài nguyên**

```python
import os
import openpyxl

def test_all_livestream_assets_ready():
    required_files = [
        "danh_sach_hop_dong.xlsx",
        "tu_vung_ielts.txt",
        "docs/schedule-livestream/cheat-sheet-30-prompts.md",
        "docs/schedule-livestream/live-speaker-notes.md",
        "docs/superpowers/specs/2026-11-13-schedule-livestream-guide-design.md"
    ]
    for rf in required_files:
        assert os.path.exists(rf), f"Asset missing: {rf}"
        assert os.path.getsize(rf) > 0, f"Asset empty: {rf}"
        
    print("All livestream assets verified successfully!")
```

- [ ] **Step 2: Chạy toàn bộ test suite**

Run: `python3 -m pytest tests/ -v`
Expected: 100% PASS

- [ ] **Step 3: Commit task 5**

```bash
git add tests/test_e2e_livestream_assets.py
git commit -m "test(livestream): add end-to-end asset verification suite"
```
