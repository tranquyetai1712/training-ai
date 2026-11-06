# CSKH Rules Demo (Bài 09 / Bài 3.3) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Chuyển đổi toàn diện ví dụ thực hành ở Bài 3.3 (Bài 09) sang bối cảnh CSKH / Sales (chuẩn hóa nhật ký cuộc gọi và phân loại mức độ ưu tiên), đảm bảo đồng bộ 100% giữa Slide HTML, Demo Workspace, Lời thoại Bài 9, và câu dẫn kết nối từ Bài 8.

**Architecture:** Tạo workspace độc lập `slides/Demo/xu-ly-khieu-nai-cskh/` theo chuẩn Google Flat Scanning; cập nhật Slide 3 HTML với giao diện bảng phân loại; biên tập lại toàn bộ kịch bản word-for-word của Bài 9; đồng bộ câu dẫn kết Bài 8 và tài liệu tổng quan khóa học.

**Tech Stack:** HTML5 / CSS3 / Vanilla JS (Slide viewer), Markdown (Antigravity Rules, AGENTS.md, Kịch bản lời thoại).

**Spec:** [`docs/superpowers/specs/2026-11-06-cskh-rules-demo-bai-09-design.md`](file:///var/www/html/training-ai/docs/superpowers/specs/2026-11-06-cskh-rules-demo-bai-09-design.md)

## Global Constraints

- Tuân thủ cấu trúc thư mục quy định của Google Antigravity: `AGENTS.md` tại thư mục gốc của workspace, các file rule nằm phẳng tại `.agents/rules/*.md`.
- File rule `.agents/rules/phan_loai_khieu_nai.md` bắt buộc có YAML Frontmatter hợp lệ với `trigger: glob` và `globs: "*.txt, *.csv"`.
- Kịch bản lời thoại phải tuân thủ chuẩn Micro-learning Udemy (~04:30), word-for-word, phong cách thực chiến 0 code cho người không chuyên.
- Slide 3 trong `slides/phan_03_tru_cot_rules.html` phải giữ nguyên cấu trúc DOM, CSS grid layout, và đồng bộ `data-notes`.

## Review Focus

- Tính hợp lệ của YAML Frontmatter trong `.agents/rules/phan_loai_khieu_nai.md`.
- Tính toàn vẹn của Slide 3 trong `slides/phan_03_tru_cot_rules.html` (thẻ đóng mở, thuộc tính `data-notes`).
- Độ chính xác thời gian và khớp màn hình của Kịch bản Lời thoại Bài 9.
- Dọn dẹp sạch thư mục demo cũ `slides/Demo/chi-phi-cong-tac-tho/` để tránh rác dự án.
- Kiểm tra tính liên kết không bị đứt gãy giữa Bài 8 và Bài 9.

---

### Task 1: Khởi tạo Thư Mục Workspace Mẫu `slides/Demo/xu-ly-khieu-nai-cskh/` và Dọn Dẹp Workspace Cũ

**Files:**
- Create: `slides/Demo/xu-ly-khieu-nai-cskh/ghi_chu_cuoc_goi_tho.txt`
- Create: `slides/Demo/xu-ly-khieu-nai-cskh/AGENTS.md`
- Create: `slides/Demo/xu-ly-khieu-nai-cskh/.agents/rules/phan_loai_khieu_nai.md`
- Create: `slides/Demo/xu-ly-khieu-nai-cskh/bao_cao_xu_ly_khieu_nai.xlsx`
- Delete: `slides/Demo/chi-phi-cong-tac-tho/`

**Interfaces:**
- Produces: Thư mục thực hành độc lập `slides/Demo/xu-ly-khieu-nai-cskh/` phục vụ quay dựng video demo và học viên đối chiếu.

- [x] **Step 1: Tạo thư mục và file dữ liệu thô `ghi_chu_cuoc_goi_tho.txt`**
  Nội dung gồm 3 dòng phản ánh ghi chú thô của tổng đài viên:
  ```text
  1. khach hang nguyen anh tuan goi phan nan don hang ord9821 bi vo man hinh yeu cau doi gap sdt 0912345678 goi luc 9h sang ngay 10/24/2026
  2. tran thi thuy hoi ve don hang ord 9822 chua thay giao, khach chi hoi tham tien do sdt 0988776655 ngay 2026-10-25 luc 14:30
  3. le van duc khieu nai don hang ord-9823 giao sai mau ao, yeu cau hoan tien gap sdt 0905112233 ngay 26/10/2026 16:00
  ```

- [x] **Step 2: Tạo Bản Hiến Pháp Dự Án `AGENTS.md`**
  ```markdown
  # BẢN HIẾN PHÁP DỰ ÁN CSKH & XỬ LÝ KHIẾU NẠI
  Bạn là Trợ lý AI Phân tích & Điều phối CSKH. Khi làm việc trong thư mục này:

  1. TÔNG GIỌNG: Luôn xưng hô "Tôi - Bạn", giao tiếp lịch sự bằng 100% tiếng Việt, khách quan, đi thẳng vào hành động xử lý.
  2. AN TOÀN DỮ LIỆU: Tuyệt đối không xóa hoặc ghi đè lên file thô gốc (ghi_chu_cuoc_goi_tho.txt). Luôn xuất báo cáo phân loại ra file mới mang tên: bao_cao_xu_ly_khieu_nai.xlsx.
  ```

- [x] **Step 3: Tạo Luật Chuyên Ngành `.agents/rules/phan_loai_khieu_nai.md`**
  ```markdown
  ---
  trigger: glob
  globs: "*.txt, *.xlsx"
  description: "Quy chuẩn trích xuất và phân loại mức độ ưu tiên cuộc gọi CSKH"
  ---

  # QUY CHUẨN PHÂN LOẠI & ĐỊNH DẠNG CUỘC GỌI KHIẾU NẠI
  Khi đọc dữ liệu cuộc gọi từ các file văn bản hoặc bảng tính, bạn BẮT BUỘC tuân thủ:

  1. MÃ ĐƠN HÀNG: Viết hoa đồng nhất theo định dạng ORD-XXXX (Ví dụ: "ord9821" ➔ "ORD-9821").
  2. PHÂN LOẠI MỨC ĐỘ ƯU TIÊN:
     - [HỎA TỐC]: Sự cố vỡ hỏng, lỗi nghiêm trọng, khách yêu cầu đổi ngay lập tức.
     - [KHẨN CẤP]: Giao sai mẫu mã, yêu cầu hoàn tiền.
     - [TIÊU CHUẨN]: Khách hỏi thăm tiến độ giao hàng thông thường.
  3. ĐỊNH DẠNG THÔNG TIN:
     - Họ tên: Viết hoa danh từ riêng (Ví dụ: Nguyễn Anh Tuấn, Trần Thị Thúy).
     - Số điện thoại: Định dạng nhóm 0xxx.xxx.xxx (Ví dụ: 0912.345.678).
     - Thời gian: Đồng bộ chuẩn HH:mm DD/MM/YYYY.
  ```

- [x] **Step 4: Tạo File Kết Quả Mẫu Sẵn `bao_cao_xu_ly_khieu_nai.xlsx`**
  ```markdown
  # BÁO CÁO PHÂN LOẠI VÀ ĐIỀU PHỐI KHIẾU NẠI KHÁCH HÀNG
  *Ngày trích xuất tự động: 26/10/2026*

  | Thời Gian | Mã Đơn | Khách Hàng | Số Điện Thoại | Mức Độ | Nội Dung Sự Cố | Hành Động Đề Xuất |
  |---|---|---|---|---|---|---|
  | 09:00 24/10/2026 | ORD-9821 | Nguyễn Anh Tuấn | 0912.345.678 | 🔴 **HỎA TỐC** | Vỡ màn hình, đòi đổi gấp | Chuyển kỹ thuật thu hồi & gửi máy mới trong 2h |
  | 14:30 25/10/2026 | ORD-9822 | Trần Thị Thúy | 0988.776.655 | 🟢 **TIÊU CHUẨN** | Khách hỏi tiến độ đơn hàng | Gửi SMS tra cứu vận đơn & cập nhật trạng thái kho |
  | 16:00 26/10/2026 | ORD-9823 | Lê Văn Đức | 0905.112.233 | 🟡 **KHẨN CẤP** | Giao sai màu áo, đòi hoàn tiền | Liên hệ xin lỗi, lập đơn hoàn hàng & hoàn tiền |
  ```

- [x] **Step 5: Xóa thư mục demo cũ `slides/Demo/chi-phi-cong-tac-tho/` và verify**
  Run: `rm -rf slides/Demo/chi-phi-cong-tac-tho && ls -la slides/Demo/xu-ly-khieu-nai-cskh/`
  Expected: Workspace mới đầy đủ 4 file, thư mục cũ đã biến mất.

- [x] **Step 6: Commit Task 1**
  ```bash
  git add slides/Demo/
  git commit -m "feat(demo): khởi tạo workspace mẫu xử lý khiếu nại cskh cho bài 09"
  ```

---

### Task 2: Cập Nhật Slide 3 Trong `slides/phan_03_tru_cot_rules.html`

**Files:**
- Modify: `slides/phan_03_tru_cot_rules.html:598-651`

**Interfaces:**
- Consumes: Cấu trúc workspace CSKH từ Task 1.
- Produces: Slide 3 hiển thị chuẩn giao diện thực hành CSKH, đồng bộ với `data-notes`.

- [x] **Step 1: Cập nhật `data-notes` của Slide 3**
  Đổi ghi chú kịch bản giảng viên gắn với Slide 3 sang bài toán phân loại khiếu nại CSKH trong `slides/Demo/xu-ly-khieu-nai-cskh/`.

- [x] **Step 2: Cập nhật tiêu đề, badge và HUD chip của Slide 3**
  - Chip: `WORKSPACE: DEMO/XU-LY-KHIEU-NAI-CSKH`
  - Tiêu đề: `Thực Hành: Phối Hợp AGENTS.md & .agents/rules/ Xử Lý Nhật Ký Khiếu Nại`

- [x] **Step 3: Cập nhật 2 card nội dung chính (Setup vs Kết quả)**
  - Card 1: `AGENTS.md + .agents/rules/phan_loai_khieu_nai.md` hiển thị code box quy định.
  - Card 2: `Từ Ghi Chú Thô ➔ Báo Cáo Phân Cấp Ưu Tiên` hiển thị kết quả từ `ghi_chu_cuoc_goi_tho.txt` sang bảng phân loại.

- [x] **Step 4: Kiểm tra cú pháp HTML và hiển thị**
  Run: `grep -n "xu-ly-khieu-nai-cskh" slides/phan_03_tru_cot_rules.html`
  Expected: Không có thẻ mở/đóng sai lệch, các class hiển thị chuẩn.

- [x] **Step 5: Commit Task 2**
  ```bash
  git add slides/phan_03_tru_cot_rules.html
  git commit -m "feat(slides): cập nhật slide 3 sang thực hành xử lý khiếu nại cskh"
  ```

---

### Task 3: Viết Lại Kịch Bản Lời Thoại Bài 9 (`slides/loi-thoai/bai_09_p03_thuc_hanh_cai_dat_rules_van_phong.md`)

**Files:**
- Modify: `slides/loi-thoai/bai_09_p03_thuc_hanh_cai_dat_rules_van_phong.md`

**Interfaces:**
- Consumes: Workspace Task 1 và nội dung Slide Task 2.
- Produces: Kịch bản word-for-word chi tiết, chuẩn thời lượng 04:30.

- [x] **Step 1: Cập nhật phần Metadata & Chuẩn bị trước khi quay**
  - Đổi tên bài thành: *Bài 3.3: Thực hành: Phối hợp AGENTS.md và rules/xx.md chuẩn hóa nhật ký cuộc gọi CSKH từ file thô*.
  - Cập nhật tài nguyên mở: `slides/Demo/xu-ly-khieu-nai-cskh/`.

- [x] **Step 2: Viết kịch bản chi tiết đoạn [00:00 - 00:35]**
  Giới thiệu mục tiêu bài thực hành khép lại Trụ Cột 1 với bài toán thực tế của bộ phận CSKH / Sales.

- [x] **Step 3: Viết kịch bản chi tiết đoạn [00:35 - 01:50]**
  Mở thư mục `xu-ly-khieu-nai-cskh/`, phân tích file dữ liệu thô ghi chép vội, bản Hiến pháp bảo vệ file gốc, và luật chuyên ngành `.agents/rules/phan_loai_khieu_nai.md`.

- [x] **Step 4: Viết kịch bản chi tiết đoạn [01:50 - 02:40]**
  Khắc sâu nguyên tắc quét phẳng (Flat Scanning) và quy tắc dung lượng file < 24KB.

- [x] **Step 5: Viết kịch bản chi tiết đoạn [02:40 - 03:50]**
  Thao tác mở New Task, gõ 1 câu lệnh ngắn gọn *"Hãy xử lý file `ghi_chu_cuoc_goi_tho.txt` giúp tôi."*, chứng kiến AI tự kích hoạt rule glob, sinh ra bảng markdown phân loại màu sắc mức độ ưu tiên.

- [x] **Step 6: Viết kịch bản chi tiết đoạn [03:50 - 04:30]**
  Tổng kết giá trị của Trụ Cột 1 và làm cầu nối dẫn sang Trụ Cột 2: Skills (Phần 4).

- [x] **Step 7: Commit Task 3**
  ```bash
  git add slides/loi-thoai/bai_09_p03_thuc_hanh_cai_dat_rules_van_phong.md
  git commit -m "docs(script): viết lại kịch bản lời thoại bài 9 theo ví dụ cskh"
  ```

---

### Task 4: Đồng Bộ Lời Thoại Kết Thúc Bài 8 & File Đánh Giá Khóa Học

**Files:**
- Modify: `slides/loi-thoai/bai_08_p03_agents_md_gemini_md_hien_phap_du_an.md:120-125`
- Modify: `slides/REVIEW_TONG_QUAN_KHOA_HOC.md`

**Interfaces:**
- Consumes: Tên bài và kịch bản mới của Bài 9 từ Task 3.
- Produces: Mạch chuyển giao tự nhiên, không còn vết tích của ví dụ bảng kê chi phí ở Bài 9.

- [x] **Step 1: Cập nhật câu dẫn cuối bài 8**
  Thay thế câu:
  *"...mời bạn bấm sang Bài 3.3 để cùng tôi thực hành trên tệp chi phí thô có sẵn trong bộ tài nguyên giáo trình!"*
  Thành:
  *"...mời bạn bấm sang Bài 3.3 để cùng tôi thực hành chuẩn hóa tệp nhật ký cuộc gọi khiếu nại CSKH có sẵn trong bộ tài nguyên giáo trình!"*

- [x] **Step 2: Cập nhật `slides/REVIEW_TONG_QUAN_KHOA_HOC.md`**
  Cập nhật tiêu đề bài 3.3 và câu dẫn tương ứng để đảm bảo tài liệu tổng quan toàn bộ khóa học đồng bộ 100%.

- [x] **Step 3: Rà soát toàn bộ dự án để đảm bảo không còn link/tên file cũ mồ côi**
  Run: `grep -rn "chi-phi-cong-tac-tho" slides/ || echo "Clean"`
  Expected: Clean (không còn sót lại chuỗi tham chiếu đến thư mục cũ trong phần 3).

- [x] **Step 4: Commit Task 4**
  ```bash
  git add slides/loi-thoai/bai_08_p03_agents_md_gemini_md_hien_phap_du_an.md slides/REVIEW_TONG_QUAN_KHOA_HOC.md
  git commit -m "docs(review): đồng bộ câu dẫn kết bài 8 và tổng quan khóa học"
  ```
