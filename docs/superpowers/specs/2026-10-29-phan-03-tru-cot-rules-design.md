# Design Spec: Chuẩn Hóa Phần 3 — Trụ Cột 1: Rules (Huấn Luyện AI Tuân Thủ Quy Chuẩn Văn Phòng)

- **Ngày tạo:** 2026-10-29
- **Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên
- **Khối 2:** Kho Vũ Khí 7 Trụ Cột Cho Dân Văn Phòng
- **Phần 3:** Trụ Cột 1 — Rules (Bài 3.1, Bài 3.2, Bài 3.3)
- **Chuẩn định dạng:** Udemy Lean Script (Solo screencast, no-fluff, 3–5 phút/bài)

---

## 1. Mục Tiêu & Phạm Vi

1. Tinh gọn kịch bản lời thoại từ thời lượng cũ (28 phút) xuống chuẩn Udemy Micro-Learning (**12 phút** tổng cộng cho 3 bài).
2. Xây dựng kịch bản word-for-word chi tiết, tự nhiên, bỏ toàn bộ văn mẫu rườm rà.
3. Đồng bộ hoàn hảo giữa 3 bài học:
   - Bài 3.1: Tổng quan khái niệm Rules, nỗi đau AI hay quên lời dặn, 2 tầng Global Rules vs Workspace Rules.
   - Bài 3.2: Chi tiết tệp `AGENTS.md` & `GEMINI.md` — Bản Hiến Pháp Dự Án với 3 Mục Vàng cho dân văn phòng.
   - Bài 3.3: Hướng dẫn thực hành từng bước tạo file `AGENTS.md`, lưu ý cấu trúc trải phẳng (flat rules) và kiểm chứng thực tế bằng lệnh tính tiền thưởng.
4. Đồng bộ `data-notes` trong slide trình chiếu `slides/phan_03_tru_cot_rules.html`.
5. Cập nhật `KHUNG_SUON_CHUONG_TRINH_HOC.md` và `slides/REVIEW_TONG_QUAN_KHOA_HOC.md`.

---

## 2. Chi Tiết Từng Bài Học

### Bài 3.1: Vì sao AI hay quên lời dặn? Sổ tay nội quy Rules cho dự án
- **Thời lượng:** 03:30 (~480 từ)
- **Slide tham chiếu:** `phan_03_tru_cot_rules.html` (Slide 1)
- **Timeline:**
  - `[00:00 - 00:40]` Nỗi đau "ngày nào cũng phải dặn lại từ đầu" do bản chất mất trí nhớ ngắn hạn của AI thông thường.
  - `[00:40 - 01:50]` Bản chất Rules: Cuốn sổ tay nội quy dự án (file Markdown tự động inject vào bộ nhớ trước mọi câu lệnh).
  - `[01:50 - 02:50]` Hai tầng phân cấp: Global Rules (`~/.gemini/config/rules/` toàn máy) vs Workspace Rules (`AGENTS.md` riêng dự án).
  - `[02:50 - 03:30]` Quy tắc vàng từ Google: Dung lượng dưới 24KB để tiết kiệm token và nạp siêu tốc; câu nối sang Bài 3.2.

### Bài 3.2: Khám Phá AGENTS.md & GEMINI.md: Bản Hiến Pháp Dự Án
- **Thời lượng:** 04:00 (~560 từ)
- **Slide tham chiếu:** `phan_03_tru_cot_rules.html` (Slide 2)
- **Timeline:**
  - `[00:00 - 00:35]` Đặt tên file chuẩn chính thức của Google: `AGENTS.md` hoặc `GEMINI.md` — Bản Hiến Pháp Dự Án.
  - `[00:35 - 01:30]` Mục Vàng 1 — Tông giọng & Ngôn ngữ (100% tiếng Việt, xưng hô Tôi - Bạn, dẹp bỏ chào hỏi sáo rỗng).
  - `[01:30 - 02:40]` Mục Vàng 2 — Chuẩn dữ liệu văn phòng (Tiền tệ có dấu chấm và đuôi `VNĐ`, chuẩn công văn Nghị định 30).
  - `[02:40 - 03:25]` Mục Vàng 3 — Ranh giới an toàn dữ liệu (Tuyệt đối không tự ý xóa file gốc, xuất preview trước khi sửa).
  - `[03:25 - 04:00]` Tổng kết giá trị "Dặn một lần — Nhớ cả đời" và câu dẫn sang thực hành Bài 3.3.

### Bài 3.3: Thực Hành: Cài Đặt AGENTS.md Chuẩn Văn Phòng (VNĐ & Danh Xưng)
- **Thời lượng:** 04:30 (~620 từ)
- **Slide tham chiếu:** `phan_03_tru_cot_rules.html` (Slide 3)
- **Timeline:**
  - `[00:00 - 00:30]` Mục tiêu thực hành: Tự tay tạo file `AGENTS.md` và nghiệm thu kết quả chuẩn 100%.
  - `[00:30 - 02:00]` Thao tác thực tế: Tạo file `AGENTS.md` tại thư mục dự án, soạn 3 quy chuẩn (tiền tệ VNĐ, viết hoa danh xưng, an toàn file gốc).
  - `[02:00 - 02:45]` Cảnh báo kỹ thuật quan trọng: Quy tắc trải phẳng (Flat Rules), tránh bẫy tạo thư mục con lồng nhau khiến AI không đọc được.
  - `[02:45 - 03:50]` Kiểm chứng thực tế: Mở New Task, gõ lệnh tính thưởng nhân viên viết thường không dấu ➔ AI tự động format chuẩn tiền tệ và họ tên.
  - `[03:50 - 04:30]` Tổng kết Phần 3 và cầu nối tiến vào Phần 4: Trụ Cột 2 — Skills.

---

## 3. Danh Sách Tệp Tác Động

1. `docs/superpowers/specs/2026-10-29-phan-03-tru-cot-rules-design.md` (Tệp spec này)
2. `slides/loi-thoai/bai_07_p03_quy_tac_rules_so_tay_noi_quy.md` (Ghi đè kịch bản Bài 3.1)
3. `slides/loi-thoai/bai_08_p03_agents_md_gemini_md_hien_phap_du_an.md` (Ghi đè kịch bản Bài 3.2)
4. `slides/loi-thoai/bai_09_p03_thuc_hanh_cai_dat_rules_van_phong.md` (Ghi đè kịch bản Bài 3.3)
5. `slides/phan_03_tru_cot_rules.html` (Cập nhật `data-notes` của Slide 1, 2, 3)
6. `KHUNG_SUON_CHUONG_TRINH_HOC.md` (Cập nhật thời lượng Phần 3 thành 12m)
7. `slides/REVIEW_TONG_QUAN_KHOA_HOC.md` (Cập nhật thông tin chi tiết Bài 3.1, 3.2, 3.3)
