# Kế Hoạch Triển Khai: Starter Kit Skill Tạo Slide HTML Tương Tác (Bài 2.5)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Xây dựng trọn gói thư mục Starter Kit Workspace `bai-2.5-tao-slide/` phục vụ bài giảng "Đọc tài liệu thô ➔ Tự sinh Slide HTML tương tác" trong khóa học Antigravity cho người không chuyên.

**Architecture:** Áp dụng mô hình "Khung Vỏ Động Cơ" (Hybrid Template-Engine) tách bạch 3 tầng: `SKILL.md` (Bộ não điều khiển quy trình 2 bước Human-in-the-loop), `engine.html` (Khung gầm CSS Glassmorphism + JS điều hướng & ngăn kéo lời thoại), và `components.md` (Thư viện 6 khối bố cục Lego chuẩn hóa).

**Tech Stack:** HTML5, Modern CSS (Glassmorphism, CSS Custom Properties, Staggered Micro-animations, Print-to-PDF), Vanilla JavaScript (Zero-dependency, Keyboard Event Listeners), Markdown (`SKILL.md`).

**Spec:** [`docs/superpowers/specs/2026-10-13-skill-tao-slide-thuyet-trinh-design.md`](file:///d:/Project/training-ai/docs/superpowers/specs/2026-10-13-skill-tao-slide-thuyet-trinh-design.md)

## Global Constraints
- **Zero-Dependency 100%:** File slide xuất ra phải là single-file `.html` chạy trực tiếp trên Chrome/Edge/Safari bằng giao thức `file:///`, không cần cài Node.js, Web Server hay bất kỳ thư viện ngoài nào.
- **Human-in-the-Loop Gate:** Skill bắt buộc dừng lại ở Bước 1 xuất Bảng Dàn ý và kịch bản người nói, chỉ khi người dùng xác nhận mới sinh HTML.
- **Không lỗi vỡ layout:** Toàn bộ thẻ HTML phải đóng mở cân bằng tuyệt đối; slide đầu tiên có class `active`, các slide sau không có.

---

### Task 1: Xây Dựng Khung Gầm Động Cơ `engine.html`

**Files:**
- Create: `bai-2.5-tao-slide/.agents/skills/tao-slide-thuyet-trinh/templates/engine.html`

**Interfaces:**
- Produces: Mẫu khung gầm HTML hoàn chỉnh chứa placeholder `{{PRESENTATION_TITLE}}`, `{{THEME_CLASS}}`, `{{TOPIC_TAG}}`, `{{TOTAL_SLIDES}}`, `{{COPYRIGHT_TEXT}}`, `{{SLIDES_CONTENT}}`.
- Tích hợp sẵn CSS Glassmorphism, 3 Themes màu, hệ thống chuyển động vi mô, điều hướng phím mũi tên / Space, ngăn kéo lời thoại diễn giả (Phím `S`), toàn màn hình (Phím `F`), và CSS `@media print` A4 landscape.

- [ ] **Step 1: Viết file `engine.html` với đầy đủ tính năng tương tác độc lập**
  - Tạo cấu trúc HTML5 chuẩn utf-8.
  - Nhúng font Google Fonts (`Plus Jakarta Sans` & `JetBrains Mono`) kèm fallback system fonts khi không có mạng.
  - CSS Glassmorphism: Variables `:root`, theme classes (`theme-cyber-dark`, `theme-deep-navy`, `theme-clean-light`).
  - JS điều khiển phím: `ArrowRight`, `ArrowLeft`, `Space`, `Backspace`, `KeyS` (toggle Speaker Notes drawer), `KeyF` (toggle Fullscreen).
  - Placeholder tokens: `{{PRESENTATION_TITLE}}`, `{{SLIDES_CONTENT}}`, `{{TOTAL_SLIDES}}`, `{{TOPIC_TAG}}`.

- [ ] **Step 2: Kiểm tra cú pháp và cấu trúc thẻ trong file `engine.html`**
  - Chạy lệnh PowerShell kiểm tra sự tồn tại của file và kiểm tra các placeholder cần thiết:
    ```powershell
    Get-Content "bai-2.5-tao-slide/.agents/skills/tao-slide-thuyet-trinh/templates/engine.html" | Select-String "{{SLIDES_CONTENT}}"
    ```
  - Kỳ vọng: Tìm thấy token `{{SLIDES_CONTENT}}`.

- [ ] **Step 3: Commit**
  ```bash
  git add bai-2.5-tao-slide/.agents/skills/tao-slide-thuyet-trinh/templates/engine.html
  git commit -m "feat(skill): add engine.html template for interactive slides"
  ```

---

### Task 2: Xây Dựng Thư Viện Bố Cục Chuẩn `components.md`

**Files:**
- Create: `bai-2.5-tao-slide/.agents/skills/tao-slide-thuyet-trinh/references/components.md`

**Interfaces:**
- Consumes: Cấu trúc wrapper `<div class="slide" data-slide="X" data-notes="...">` từ Task 1.
- Produces: 6 mẫu bố cục Lego HTML snippets chuẩn hóa:
  1. `Cover / Hero Slide` (Mở đầu với Thực trạng vs Mục tiêu)
  2. `Split Comparison 2 Cột` (Cũ/Sai vs Mới/Chuẩn)
  3. `Grid-3 Cột` (Quy trình 3 bước hoặc 3 trụ cột)
  4. `KPI Stats Slide` (3 số liệu đột phá lớn)
  5. `Bảng Ma Trận So Sánh` (Table với Badge pills)
  6. `Summary & Q&A Slide` (3 đúc kết cốt lõi & Hộp liên hệ)

- [ ] **Step 1: Viết file `components.md` với đầy đủ mã nguồn HTML snippets**
  - Cung cấp mã mẫu hoàn chỉnh cho từng component.
  - Hướng dẫn rõ ràng cách đặt `data-notes="..."` chứa kịch bản người nói.
  - Hướng dẫn quy tắc class `active` cho slide số 1.

- [ ] **Step 2: Kiểm tra file `components.md`**
  - Chạy lệnh kiểm tra sự tồn tại của 6 mẫu component:
    ```powershell
    Select-String -Path "bai-2.5-tao-slide/.agents/skills/tao-slide-thuyet-trinh/references/components.md" -Pattern "## [1-6]\."
    ```
  - Kỳ vọng: Tìm thấy đủ 6 đề mục component.

- [ ] **Step 3: Commit**
  ```bash
  git add bai-2.5-tao-slide/.agents/skills/tao-slide-thuyet-trinh/references/components.md
  git commit -m "feat(skill): add 6 standardized slide layout components"
  ```

---

### Task 3: Xây Dựng Bộ Não Điều Khiển `SKILL.md`

**Files:**
- Create: `bai-2.5-tao-slide/.agents/skills/tao-slide-thuyet-trinh/SKILL.md`

**Interfaces:**
- Consumes: `templates/engine.html` và `references/components.md`.
- Produces: Bản mô tả kỹ năng chuẩn cho Agentic AI gồm Frontmatter metadata và Quy trình 2 bước Human-in-the-loop.

- [ ] **Step 1: Soạn thảo `SKILL.md` chuẩn mực**
  - Frontmatter metadata: `name: tao-slide-thuyet-trinh`, description kích hoạt tự nhiên.
  - Triết lý cốt lõi: 0-Dependency, Glassmorphism, Micro-animations, Speaker Notes Drawer, Print-to-PDF.
  - Bước 1: Phân tích tài liệu, lập bảng Dàn ý Markdown gồm 6-8 slide kèm Lời thoại Diễn giả theo công thức 3 phần (Hook ➔ Insight ➔ Action).
  - Cổng chờ kiểm duyệt (Hard Gate): Câu thoại thân thiện chờ học viên gõ "OK".
  - Bước 2: Đọc `engine.html`, chọn Lego từ `components.md`, thay thế placeholders, xuất file `slide_<ten_file>.html`.

- [ ] **Step 2: Kiểm tra nội dung `SKILL.md`**
  - Chạy lệnh kiểm tra Frontmatter và Hard Gate:
    ```powershell
    Select-String -Path "bai-2.5-tao-slide/.agents/skills/tao-slide-thuyet-trinh/SKILL.md" -Pattern "name: tao-slide-thuyet-trinh|HARD GATE|Bước 1|Bước 2"
    ```
  - Kỳ vọng: Đầy đủ các tiêu chí quan trọng.

- [ ] **Step 3: Commit**
  ```bash
  git add bai-2.5-tao-slide/.agents/skills/tao-slide-thuyet-trinh/SKILL.md
  git commit -m "feat(skill): add SKILL.md defining 2-phase slide generation protocol"
  ```

---

### Task 4: Xây Dựng Kho Tài Liệu Mẫu Thực Hành & Cẩm Nang Học Viên

**Files:**
- Create: `bai-2.5-tao-slide/tai-lieu-thuc-hanh/de-xuat-du-an.md`
- Create: `bai-2.5-tao-slide/tai-lieu-thuc-hanh/quy-trinh-onboarding.md`
- Create: `bai-2.5-tao-slide/tai-lieu-thuc-hanh/y-tuong-khoi-nghiep.txt`
- Create: `bai-2.5-tao-slide/README.md`

**Interfaces:**
- Produces: Dữ liệu thô văn phòng phong phú để học viên test ngay tại lớp; file `README.md` hướng dẫn 1 trang siêu dễ hiểu cho người non-tech.

- [ ] **Step 1: Tạo các file tài liệu thô mẫu trong `tai-lieu-thuc-hanh/`**
  - File 1 (`de-xuat-du-an.md`): Đề xuất triển khai dự án tự động hóa số liệu quý 4 (có thực trạng, giải pháp, ngân sách, lộ trình 3 giai đoạn).
  - File 2 (`quy-trinh-onboarding.md`): Cẩm nang hội nhập nhân sự mới (3 bước: Tuần 1, Tháng 1, Tháng 3; các lưu ý văn hóa).
  - File 3 (`y-tuong-khoi-nghiep.txt`): Ghi chú thô sơ, gạch đầu dòng về ý tưởng kinh doanh chuỗi cà phê công nghệ.

- [ ] **Step 2: Viết `bai-2.5-tao-slide/README.md` (Cheat-sheet cho học viên)**
  - Giới thiệu mục tiêu bài học trong 3 câu.
  - Hướng dẫn cách dùng 1 câu lệnh (Cách 1: Gõ tự nhiên; Cách 2: Kéo thả file).
  - Bảng tra cứu phím tắt trình chiếu (`Space`, Mũi tên, `S`, `F`, `Ctrl + P`).
  - Hướng dẫn "giải phẫu" tùy biến đổi phong cách lời thoại cho học viên.

- [ ] **Step 3: Commit**
  ```bash
  git add bai-2.5-tao-slide/tai-lieu-thuc-hanh/ bai-2.5-tao-slide/README.md
  git commit -m "feat(starter-kit): add sample practice documents and student cheat-sheet"
  ```

---

### Task 5: Kiểm Thử Toàn Trình (End-to-End Verification & Demo Slide Test)

**Files:**
- Create: `bai-2.5-tao-slide/slide_demo_de_xuat_du_an.html` (Sản phẩm mẫu tham chiếu cho giảng viên)

**Interfaces:**
- Consumes: Toàn bộ Starter Kit từ Task 1 đến Task 4.
- Produces: File HTML hoàn chỉnh chạy thử nghiệm từ tài liệu `de-xuat-du-an.md`, đóng vai trò là "Bản mẫu mẫu mực" để giảng viên chiếu ngay đầu buổi học.

- [ ] **Step 1: Sinh file `slide_demo_de_xuat_du_an.html` tuân thủ 100% quy trình của Skill**
  - 7 slides hoàn chỉnh tương ứng với tài liệu đề xuất dự án.
  - Slide 1: Hero Cover (`class="slide active"`).
  - Slide 2: Split so sánh Thực trạng cũ vs Đề xuất mới.
  - Slide 3: Grid 3 bước lộ trình triển khai.
  - Slide 4: KPI Stats số liệu cam kết (Tiết kiệm 65% thời gian, ROI 3.2x).
  - Slide 5: Bảng ma trận ngân sách & phân bổ.
  - Slide 6: Rủi ro & Giải pháp phòng ngừa.
  - Slide 7: Summary & Kêu gọi hành động.
  - Mọi slide đều có thuộc tính `data-notes` chứa kịch bản lời thoại diễn giả tự nhiên.

- [ ] **Step 2: Kiểm thử tính toàn vẹn kỹ thuật (Automated Verification Script)**
  - Chạy script kiểm tra:
    - [x] File tồn tại và dung lượng > 10KB.
    - [x] Thẻ đóng mở `<div>`, `<section>` cân bằng.
    - [x] Có đúng 1 slide mang class `active`.
    - [x] Tất cả 7 slide đều có thuộc tính `data-notes`.
    - [x] Phím tắt `KeyS`, `ArrowRight` có trong mã nguồn JS.
  ```powershell
  $content = Get-Content "bai-2.5-tao-slide/slide_demo_de_xuat_du_an.html" -Raw
  $activeCount = ([regex]::Matches($content, 'class="slide active"')).Count
  $notesCount = ([regex]::Matches($content, 'data-notes="')).Count
  Write-Host "Active slides: $activeCount (Expected: 1)"
  Write-Host "Notes count: $notesCount (Expected: 7)"
  ```

- [ ] **Step 3: Commit**
  ```bash
  git add bai-2.5-tao-slide/slide_demo_de_xuat_du_an.html
  git commit -m "feat(demo): add reference slide output for instructor live demo"
  ```
