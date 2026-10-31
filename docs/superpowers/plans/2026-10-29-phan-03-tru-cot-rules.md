# Phần 3: Trụ Cột 1 — Rules Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Chuẩn hóa toàn bộ kịch bản lời thoại và slide HTML Phần 3: Trụ Cột 1 — Rules (Bài 3.1, 3.2, 3.3) theo chuẩn Udemy Lean Script (12 phút tổng cộng).

**Architecture:** Refactor 3 file kịch bản Markdown sang định dạng word-for-word lean script; cập nhật thuộc tính `data-notes` trong slide trình chiếu HTML độc lập; đồng bộ ma trận đối chiếu trong `KHUNG_SUON_CHUONG_TRINH_HOC.md` và `REVIEW_TONG_QUAN_KHOA_HOC.md`.

**Tech Stack:** Markdown, HTML5, Vanilla JavaScript.

**Spec:** `docs/superpowers/specs/2026-10-29-phan-03-tru-cot-rules-design.md`

## Global Constraints

- Chuẩn phong cách: Udemy Lean Script (solo screencast, trực diện, không dùng văn mẫu diễn giả, 3-5 phút/bài).
- Xưng hô: "Tôi - Bạn" chuyên nghiệp, thân thiện, hướng dẫn trực quan.
- Ngôn ngữ: Toàn bộ kịch bản và tài liệu bằng tiếng Việt; code comment bằng tiếng Anh.
- Thời lượng: Bài 3.1 (03:30), Bài 3.2 (04:00), Bài 3.3 (04:30). Tổng Phần 3: 12 phút.

## Review Focus

1. Kịch bản không chứa câu từ sáo rỗng hay chào hỏi lặp lại lê thê.
2. Từng phân đoạn thời gian (timeline timestamp) khớp với tốc độ đọc thực tế (~130-150 từ/phút).
3. Thao tác thực hành ở Bài 3.3 rõ ràng, ai cũng làm theo được mà không bị lỗi thư mục con.
4. Thẻ `data-notes` trên cả 3 slide HTML phản ánh trung thực ý chính của từng bài.
5. Ma trận đối chiếu chéo không bị lệch thời lượng hay link file.

---

### Task 1: Tinh Gọn Kịch Bản Bài 3.1 (`bai_07_p03_quy_tac_rules_so_tay_noi_quy.md`)

**Files:**
- Modify: `slides/loi-thoai/bai_07_p03_quy_tac_rules_so_tay_noi_quy.md`

- [ ] **Step 1: Soạn thảo kịch bản word-for-word Bài 3.1**
Viết lại nội dung kịch bản với thời lượng 03:30 (~480 từ), 4 mốc thời gian:
  - `[00:00 - 00:40]` Nỗi đau "ngày nào cũng phải dặn lại từ đầu" do bản chất mất trí nhớ ngắn hạn của AI thông thường.
  - `[00:40 - 01:50]` Bản chất Rules: Cuốn sổ tay nội quy dự án (file Markdown tự động inject vào bộ nhớ trước mọi câu lệnh).
  - `[01:50 - 02:50]` Hai tầng phân cấp: Global Rules (`~/.gemini/config/rules/` toàn máy) vs Workspace Rules (`AGENTS.md` riêng dự án).
  - `[02:50 - 03:30]` Quy tắc vàng từ Google: Dung lượng dưới 24KB để tiết kiệm token và nạp siêu tốc; câu nối sang Bài 3.2.

- [ ] **Step 2: Ghi file và kiểm tra số từ**
Chạy lệnh kiểm tra số từ: `wc -w slides/loi-thoai/bai_07_p03_quy_tac_rules_so_tay_noi_quy.md` (mục tiêu: 450 - 520 từ).

---

### Task 2: Tinh Gọn Kịch Bản Bài 3.2 (`bai_08_p03_agents_md_gemini_md_hien_phap_du_an.md`)

**Files:**
- Modify: `slides/loi-thoai/bai_08_p03_agents_md_gemini_md_hien_phap_du_an.md`

- [ ] **Step 1: Soạn thảo kịch bản word-for-word Bài 3.2**
Viết lại nội dung kịch bản với thời lượng 04:00 (~560 từ), 4 mốc thời gian:
  - `[00:00 - 00:35]` Đặt tên file chuẩn chính thức của Google: `AGENTS.md` hoặc `GEMINI.md` — Bản Hiến Pháp Dự Án.
  - `[00:35 - 01:30]` Mục Vàng 1 — Tông giọng & Ngôn ngữ (100% tiếng Việt, xưng hô Tôi - Bạn, dẹp bỏ chào hỏi sáo rỗng).
  - `[01:30 - 02:40]` Mục Vàng 2 — Chuẩn dữ liệu văn phòng (Tiền tệ có dấu chấm và đuôi `VNĐ`, chuẩn công văn Nghị định 30).
  - `[02:40 - 03:25]` Mục Vàng 3 — Ranh giới an toàn dữ liệu (Tuyệt đối không tự ý xóa file gốc, xuất preview trước khi sửa).
  - `[03:25 - 04:00]` Tổng kết giá trị "Dặn một lần — Nhớ cả đời" và câu dẫn sang thực hành Bài 3.3.

- [ ] **Step 2: Ghi file và kiểm tra số từ**
Chạy lệnh kiểm tra số từ: `wc -w slides/loi-thoai/bai_08_p03_agents_md_gemini_md_hien_phap_du_an.md` (mục tiêu: 520 - 600 từ).

---

### Task 3: Tinh Gọn Kịch Bản Bài 3.3 (`bai_09_p03_thuc_hanh_cai_dat_rules_van_phong.md`)

**Files:**
- Modify: `slides/loi-thoai/bai_09_p03_thuc_hanh_cai_dat_rules_van_phong.md`

- [ ] **Step 1: Soạn thảo kịch bản word-for-word Bài 3.3**
Viết lại nội dung kịch bản với thời lượng 04:30 (~620 từ), 4 mốc thời gian:
  - `[00:00 - 00:30]` Mục tiêu thực hành: Tự tay tạo file `AGENTS.md` và nghiệm thu kết quả chuẩn 100%.
  - `[00:30 - 02:00]` Thao tác thực tế: Tạo file `AGENTS.md` tại thư mục dự án, soạn 3 quy chuẩn (tiền tệ VNĐ, viết hoa danh xưng, an toàn file gốc).
  - `[02:00 - 02:45]` Cảnh báo kỹ thuật quan trọng: Quy tắc trải phẳng (Flat Rules), tránh bẫy tạo thư mục con lồng nhau khiến AI không đọc được.
  - `[02:45 - 03:50]` Kiểm chứng thực tế: Mở New Task, gõ lệnh tính thưởng nhân viên viết thường không dấu ➔ AI tự động format chuẩn tiền tệ và họ tên.
  - `[03:50 - 04:30]` Tổng kết Phần 3 và cầu nối tiến vào Phần 4: Trụ Cột 2 — Skills.

- [ ] **Step 2: Ghi file và kiểm tra số từ**
Chạy lệnh kiểm tra số từ: `wc -w slides/loi-thoai/bai_09_p03_thuc_hanh_cai_dat_rules_van_phong.md` (mục tiêu: 580 - 660 từ).

---

### Task 4: Đồng Bộ Thuộc Tính `data-notes` Trong Slide HTML (`slides/phan_03_tru_cot_rules.html`)

**Files:**
- Modify: `slides/phan_03_tru_cot_rules.html`

- [ ] **Step 1: Cập nhật `data-notes` cho Slide 1, 2, 3**
Đảm bảo nội dung trong `data-notes` tóm tắt súc tích, mạch lạc theo đúng timeline của kịch bản mới.
- [ ] **Step 2: Kiểm tra tính toàn vẹn của mã HTML**
Đảm bảo cấu trúc thẻ đóng/mở cân bằng, script đếm slide và mở drawer hoạt động chuẩn.

---

### Task 5: Đồng Bộ `KHUNG_SUON_CHUONG_TRINH_HOC.md` & `REVIEW_TONG_QUAN_KHOA_HOC.md`

**Files:**
- Modify: `KHUNG_SUON_CHUONG_TRINH_HOC.md`
- Modify: `slides/REVIEW_TONG_QUAN_KHOA_HOC.md`

- [ ] **Step 1: Cập nhật `KHUNG_SUON_CHUONG_TRINH_HOC.md`**
Cập nhật thời lượng Phần 3 từ 28m thành 12m (Bài 3.1: 3.5m, Bài 3.2: 4m, Bài 3.3: 4.5m). Tổng Khối 2: 1h39m.
- [ ] **Step 2: Cập nhật `slides/REVIEW_TONG_QUAN_KHOA_HOC.md`**
Cập nhật chi tiết mục `bai_07`, `bai_08`, `bai_09` với thời lượng và timeline mới.
- [ ] **Step 3: Kiểm tra chéo toàn bộ diff**
Chạy `git diff --stat` để nghiệm thu thay đổi.
