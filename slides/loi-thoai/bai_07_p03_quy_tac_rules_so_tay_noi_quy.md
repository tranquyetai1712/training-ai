# KỊCH BẢN LỜI THOẠI BÀI HỌC 3.1
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 2:** Kho Vũ Khí 7 Trụ Cột Cho Dân Văn Phòng  
**Phần 3:** Trụ Cột 1 — Rules: Huấn Luyện AI Tuân Thủ Quy Chuẩn Văn Phòng  
**Tên bài:** Bài 3.1: Vì sao AI hay quên lời dặn? Sổ tay nội quy Rules cho dự án  
**Thời lượng dự kiến:** 03:30 • **Slide:** `phan_03_tru_cot_rules.html` (Slide 1)

---

## 🎬 1. CHUẨN BỊ
* Trình chiếu: Slide 1 (`slides/phan_03_tru_cot_rules.html`).
* Tông giọng: Điềm tĩnh, dứt khoát, phong thái ủy thác.

---

## 🎙️ 2. LỜI THOẠI CHI TIẾT (WORD-FOR-WORD SCRIPT)

### [00:00 - 00:40] NỖI ĐAU AI HAY QUÊN & CĂN BỆNH MẤT TRÍ NHỚ NGẮN HẠN CỦA CHATBOT CŨ
`[Slide 1: Trụ Cột 1 — Rules: Sổ Tay Nội Quy Dự Án]`

"Chào mừng bạn đến với **Khối 2: Kho Vũ Khí 7 Trụ Cột**!

Có bao giờ bạn bực mình vì mở chatbot lên phải dặn lại: *'Nói tiếng Việt'*, *'Ghi VNĐ'*, hay *'Đừng lan man'*?

Đó là chứng mất trí nhớ ngắn hạn của chatbot cũ. Hết phiên chat là quên sạch, bắt bạn dặn lại từ đầu.

Antigravity chấm dứt điều này nhờ **Trụ Cột 1: Rules Engine** — dặn một lần, nhớ suốt đời."

---

### [00:40 - 01:50] BẢN CHẤT CỦA RULES: CUỐN SỔ TAY NỘI QUY DỰ ÁN
`[Chỉ hình Sổ Tay Nội Quy trên Slide 1]`

"Rules thực chất như **Cuốn Sổ Tay Nội Quy** phát cho nhân viên mới: Giờ giấc, trang phục, văn phong. Đọc một lần là tự giác tuân thủ.

Trong Antigravity, Rules chỉ là file Markdown (`.md`) viết bằng tiếng Việt, không cần code.

Nhờ cơ chế **Auto-inject**, khi mở dự án, Antigravity tự nạp file này vào bộ não AI trước khi nhận lệnh. Trợ lý AI tự giác làm đúng chuẩn mà bạn không cần nhắc lại."

---

### [01:50 - 02:50] HAI TẦNG PHÂN CẤP: GLOBAL RULES (~/.gemini/config/rules/) VS WORKSPACE RULES (AGENTS.md)
`[Chỉ 2 cột Cấp độ trên Slide 1]`

"Nội quy trong Antigravity chia làm hai tầng:

* **Global Rules (`~/.gemini/config/rules/`):** Toàn máy, áp dụng mọi dự án. Ví dụ: *'Luôn dùng tiếng Việt'*, *'Không tự xóa file'*.
* **Workspace Rules (`AGENTS.md`):** Đặt trong thư mục dự án, áp dụng riêng dự án đó. Ví dụ: Kế toán cần đuôi `VNĐ`; Hành chính theo Nghị định 30.

Đổi dự án, AI tự thích ứng chuẩn mực tương ứng."

---

### [02:50 - 03:30] QUY TẮC VÀNG DƯỚI 24KB & BƯỚC ĐỆM CHUYỂN TIẾP SANG BÀI 3.2
`[Chỉ thanh lưu ý cuối Slide 1]`

"Google khuyến nghị một quy tắc vàng: **Dung lượng file Rules phải dưới 24KB**. Quy tắc ngắn gọn giúp tiết kiệm ngữ cảnh và nạp siêu tốc.

Đó là bản chất của Rules — sổ tay giúp AI không bao giờ quên việc.

Vậy file nội quy dự án viết chuẩn ra sao? Mời bạn sang **Bài 3.2** cùng tôi khám phá **AGENTS.md — Bản Hiến Pháp Dự Án**!"
