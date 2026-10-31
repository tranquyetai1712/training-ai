# KỊCH BẢN LỜI THOẠI BÀI HỌC 6.1
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 2:** Kho Vũ Khí 7 Trụ Cột Cho Dân Văn Phòng  
**Phần 6:** Trụ Cột 4 — Hooks: Vòng Kim Cô Bảo Vệ An Toàn Dữ Liệu Tuyệt Đối  
**Tên bài:** Bài 6.1: Hooks là gì? Người gác cổng giám sát hành động của AI  
**Thời lượng dự kiến:** 03:30 (Chuẩn Udemy Micro-Learning • System Security Engine)  
**Slide tương ứng:** `phan_06_tru_cot_hooks.html` (Slide 1)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_06_tru_cot_hooks.html` (Slide 1: Trụ Cột 4 — Hooks: Vòng Kim Cô Giám Sát AI).
* **Tông giọng:** Nghiêm túc, điềm tĩnh, toát lên sự an tâm và kỷ luật thép của hệ thống an ninh.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD LEAN SCRIPT)

### [00:00 - 00:40] NỖI SỢ NHÂN VIÊN AI LÀM ẨU & NGUY CƠ PHÁ HỎNG DỮ LIỆU GỐC
`[Slide 1: Trụ Cột 4 — Hooks: Vòng Kim Cô Giám Sát AI]`  
`[Tông giọng trầm ấm, đặt vấn đề bảo mật thực tế]`

"Chào mừng bạn đến với **Phần 6: Trụ Cột 4 — Hooks (Vòng Kim Cô Bảo Vệ An Toàn Dữ Liệu Tuyệt Đối)**!

Trong quản trị nhân sự, có một quy luật luôn đúng: *'Nhân viên càng xông xáo, càng nhiệt tình... thì nguy cơ làm ẩu, làm sai lại càng cao!'*  
Và trợ lý AI tự hành cũng không phải ngoại lệ. Khi bạn giao cho nó một nhiệm vụ lớn, nó sẽ lao vào thực thi rất nhanh. 

**Thế nhưng thực tế là,** nếu lỡ nó hiểu nhầm một câu lệnh và định ghi đè lên file dữ liệu gốc của khách hàng, hoặc vô tình xóa mất một hợp đồng pháp lý quan trọng thì hậu quả sẽ khôn lường!

**Chính vì thế,** để bạn luôn có thể kê cao gối ngủ ngon mà không sợ mất dữ liệu, Antigravity mang đến vũ khí số bốn: **Hooks — Người gác cổng an ninh tự động của hệ thống!**"

---

### [00:40 - 01:50] ẨN DỤ TRẠM AN NINH SÂN BAY & 2 CHỐT CHẶN PRETOOLUSE VS POSTTOOLUSE
`[Chỉ Thẻ KIỂM SOÁT ĐẦU VÀO và KIỂM SOÁT ĐẦU RA trên Slide 1]`

"**Để hiểu Hooks hoạt động ra sao, bạn hãy tưởng tượng quy trình đi máy bay tại sân bay:**

* Khi bạn chuẩn bị bước lên máy bay, bạn bắt buộc phải đi qua **Cửa soi chiếu an ninh (PreToolUse)**: Nhân viên an ninh quét hành lý của bạn. Nếu bạn mang theo đồ vật nguy hiểm, họ sẽ chặn bạn lại ngay lập tức và không cho phép bạn bước tiếp!
* Sau khi máy bay hạ cánh, có thêm một **Cửa hải quan kiểm tra (PostToolUse)**: Nhân viên đối chiếu tem phiếu xem hành lý của bạn có đúng quy chuẩn không rồi mới cho bạn rời sân bay.

**Trong Antigravity, cơ chế hoạt động cũng y hệt như vậy:**  
Mỗi khi AI muốn kích hoạt một công cụ — ví dụ: công cụ sửa file, xóa file, hay gửi email — nó **bắt buộc phải đi qua Trạm gác Hooks**:
* **Chốt chặn 1 — Trước khi hành động (PreToolUse):**  
  Hook sẽ soi xét: *'AI định mở file nào? Định làm gì?'*. Nếu AI định xóa một file có chữ `goc_` hoặc `backup_`, Hook lập tức **thổi còi báo động, chặn đứng lệnh đó lại** ngay tại chỗ!
* **Chốt chặn 2 — Sau khi hành động (PostToolUse):**  
  Sau khi AI tạo ra một file báo cáo, Hook tự động quét lại một lượt: *'Báo cáo này đã đủ các cột số liệu bắt buộc chưa? File bảng tính có bị thiếu công thức không?'*. Nếu phát hiện sai sót, Hook sẽ bắt AI phải sửa ngay trước khi nộp cho bạn!"

---

### [01:50 - 02:50] CẤU HÌNH HOOKS.JSON: NGƯỜI GÁC CỔNG 24/7
`[Chỉ Thẻ AN NINH TẦNG HỆ THỐNG trên Slide 1]`

"**Vậy cài đặt Trạm gác an ninh này có khó không?**

Nói tóm lại, nó cực kỳ đơn giản và nhẹ nhàng!  
Toàn bộ quy định của Trạm gác được đặt gọn gàng trong một tệp cấu hình mang tên `hooks.json` nằm ngay trong thư mục `.agents/hooks.json` của dự án (hoặc áp dụng toàn cục trên máy tính).

Trong đó, bạn chỉ cần khai báo 3 điều ngắn gọn:
1. **Sự kiện cần giám sát:** Ví dụ `PreToolUse` (trước khi AI kích hoạt công cụ chạy lệnh hoặc sửa file).
2. **Đối tượng soi chiếu (Matcher):** Soi các công cụ can thiệp tệp tin như `run_command`, `write_to_file`, `replace_file_content`.
3. **Quyết định an ninh (Decision):** Nếu phát hiện can thiệp vào tài liệu gốc, lập tức trả về `deny` để chặn đứng thao tác và gửi thông báo cảnh báo cho bạn!

**Nhờ có Trạm gác Hooks chạy ngầm 24/7,** bạn hoàn toàn không cần phải thức đêm trông chừng AI, vì mọi hành vi nguy hiểm đều bị chặn đứng trước khi chạm vào ổ cứng của bạn!"

---

### [02:50 - 03:30] PHÂN BIỆT RULES VS HOOKS & CẦU NỐI SANG THỰC HÀNH BÀI 6.2
`[Chỉ dòng Footer Bar trên Slide 1: Sự khác biệt Rules vs Hooks]`

"**Để đúc kết bài học này, bạn hãy nhớ một sự khác biệt cốt lõi:**  
* **Rules** là cuốn sổ tay nội quy — giống như **'Biển báo giao thông'** chỉ đường nhắc nhở.
* Còn **Hooks** là chốt chặn kỹ thuật — giống như **'Gờ giảm tốc và Barie tự động'** nâng lên hạ xuống, có tác dụng cản phá vật lý thực sự!

**Và để kiểm chứng tận mắt sức mạnh phanh gấp của Hooks,** mời bạn cùng tôi bước sang **Bài 6.2**: Chúng ta sẽ cùng nhau làm một việc mạo hiểm nhất — cố tình ra lệnh cho AI phá hủy file dữ liệu gốc, để xem Trạm gác Hooks thổi còi và chặn đứng hành vi đó như thế nào!

Mời bạn cùng bấm sang Bài 6.2 ngay bây giờ!"
