# KỊCH BẢN LỜI THOẠI BÀI HỌC 3.1
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 2:** Kho Vũ Khí 7 Trụ Cột Cho Dân Văn Phòng  
**Phần 3:** Trụ Cột 1 — Rules: Huấn Luyện AI Tuân Thủ Quy Chuẩn Văn Phòng  
**Tên bài:** Bài 3.1: Vì sao AI hay quên lời dặn? Sổ tay nội quy Rules cho dự án  
**Thời lượng dự kiến:** 03:30 (Chuẩn Udemy Micro-Learning • Rules Engine)  
**Slide tương ứng:** `phan_03_tru_cot_rules.html` (Slide 1)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_03_tru_cot_rules.html` (Slide 1: Trụ Cột 1 — Rules: Sổ Tay Nội Quy Dự Án).
* **Tông giọng:** Hóm hỉnh khi nói về tật hay quên của AI cũ, sau đó chuyển sang tự tin, quyết đoán khi giới thiệu giải pháp Rules.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD LEAN SCRIPT)

### [00:00 - 00:40] NỖI ĐAU AI HAY QUÊN & CĂN BỆNH MẤT TRÍ NHỚ NGẮN HẠN CỦA CHATBOT CŨ
`[Slide 1: Trụ Cột 1 — Rules: Sổ Tay Nội Quy Dự Án]`  
`[Tông giọng đồng cảm, khơi gợi vấn đề]`

"Chào mừng bạn chính thức bước vào **Khối 2: Kho Vũ Khí 7 Trụ Cột Cho Dân Văn Phòng**!

Có bao giờ bạn cảm thấy cực kỳ mệt mỏi khi mỗi lần mở chatbot lên, bạn lại phải lặp đi lặp lại một điệp khúc quen thuộc: *'Nhớ trả lời bằng tiếng Việt nhé'*, *'Nhớ ghi số tiền có đuôi VNĐ nhé'*, hay *'Đừng trả lời lan man nhé'*?

**Nguyên nhân sâu xa là bởi vì:** Các chatbot thế hệ cũ mắc phải một căn bệnh cố hữu — đó là chứng mất trí nhớ ngắn hạn! Cứ kết thúc một phiên chat là nó quên sạch sành sanh, và hôm sau bạn lại phải cầm tay chỉ việc lại từ con số không.

**Thế nhưng với Google Antigravity,** cơn ác mộng đó sẽ hoàn toàn chấm dứt nhờ **Trụ Cột 1: Rules Engine** — với nguyên lý cốt lõi: **Bạn chỉ cần dặn đúng một lần duy nhất, và AI sẽ tự giác khắc cốt ghi tâm suốt đời!**"

---

### [00:40 - 01:50] BẢN CHẤT CỦA RULES: CUỐN SỔ TAY NỘI QUY DỰ ÁN
`[Chỉ hình ảnh Cuốn Sổ Tay Nội Quy trên Slide 1]`

"**Vậy Rules thực chất là gì?**

Hãy hình dung Rules giống hệt như **Cuốn Sổ Tay Nội Quy Công Ty** được phát cho nhân viên mới vào ngày đầu tiên đi làm: Trong đó ghi rõ giờ giấc làm việc ra sao, trang phục thế nào, và văn phong gửi email cho khách hàng phải lịch sự ra sao. Nhân viên chỉ cần đọc qua một lần là tự giác tuân thủ trong suốt quá trình làm việc sau này.

**Trong Antigravity,** bản chất của Rules vô cùng đơn giản: Nó chỉ là một file văn bản Markdown (`.md`) được viết hoàn toàn bằng tiếng Việt tự nhiên, không cần bạn phải biết bất kỳ một dòng mã lập trình nào!

**Đặc biệt, tài liệu chính thức của Google nhấn mạnh một nguyên tắc cốt lõi:** **Rule** được sinh ra để thiết lập các **Ràng buộc và Bất biến (Constraints & Invariants)** — tức là những lằn ranh đỏ mà AI tuyệt đối không bao giờ được vi phạm; khác hoàn toàn với **Skill** ở Phần 4 sau này là các quy trình thực hiện công việc từng bước.

**Và điều kỳ diệu nhất ở đây là:** Nhờ cơ chế **Auto-inject**, mỗi khi bạn mở dự án lên hay bắt đầu một phiên làm việc mới, Antigravity sẽ tự động nạp toàn bộ cuốn sổ tay nội quy này vào đầu não của AI trước khi nhận bất kỳ câu lệnh nào từ bạn. **Kết quả là,** trợ lý AI luôn tự giác làm đúng chuẩn công sở mà bạn không cần phải tốn công nhắc nhở dù chỉ một lời!"

---

### [01:50 - 02:50] HAI TẦNG PHÂN CẤP: GLOBAL RULES VS WORKSPACE RULES
`[Chỉ 2 cột Cấp độ trên Slide 1: Global Rules vs Workspace Rules]`

"Để phục vụ linh hoạt cho công việc văn phòng, hệ thống Rules trong Antigravity được phân chia làm **hai tầng rõ rệt**:

* **Tầng thứ nhất — Global Rules (Nội quy toàn máy tính):**
  * Nằm tại thư mục cấu hình chung của bạn (`~/.gemini/config/rules/`).
  * Tự động áp dụng cho **mọi dự án**, mọi lần bạn mở máy tính làm việc.
  * Ví dụ: Những nguyên tắc bất biến của cá nhân bạn như *'Luôn xưng hô lịch sự bằng tiếng Việt'*, hoặc *'Tuyệt đối không được tự ý xóa file khi chưa hỏi ý kiến tôi'*.
* **Tầng thứ hai — Workspace Rules (Nội quy riêng của từng dự án):**
  * Nằm ngay bên trong thư mục dự án của bạn (thường là tệp `AGENTS.md`).
  * Chỉ áp dụng riêng cho phạm vi công việc đó mà thôi.
  * **Chính vì thế,** nếu bạn làm việc trong dự án Kế toán, bạn cài luật: *'Mọi số tiền bắt buộc có đuôi VNĐ'*; còn khi chuyển sang dự án Hành chính, bạn cài luật: *'Văn phong phải chuẩn thể thức Nghị định 30'*.

**Nhờ có sự phân tầng này,** khi bạn chuyển đổi giữa các dự án khác nhau, AI sẽ tự động thích ứng chuẩn mực tương ứng mà không bao giờ bị lẫn lộn!"

---

### [02:50 - 03:30] QUY TẮC VÀNG DƯỚI 24KB & BƯỚC ĐỆM CHUYỂN TIẾP SANG BÀI 3.2
`[Chỉ vào thanh lưu ý ở chân Slide 1]`  
`[Tông giọng hào hứng, chuyển bài]`

"Theo tài liệu kỹ thuật chính thức từ Google, có một quy tắc vàng bạn cần ghi nhớ: **Dung lượng của một tệp Rules nên viết súc tích và dưới 24 Kilobytes!** Việc giữ nội quy ngắn gọn sẽ giúp AI nạp dữ liệu siêu tốc và tiết kiệm tối đa bộ nhớ ngữ cảnh để dồn sức xử lý công việc cho bạn.

**Nói tóm lại,** Rules chính là chiếc chìa khóa vàng giúp AI không bao giờ quên bài và luôn hành xử như một nhân sự chuyên nghiệp.

**Thế nhưng trong thực tế,** tệp nội quy dự án được cấu trúc ra sao và gồm những mục then chốt nào?  
Mời bạn bấm ngay sang **Bài 3.2** để cùng tôi khám phá **AGENTS.md — Bản Hiến Pháp Dự Án Của Bạn**!"
