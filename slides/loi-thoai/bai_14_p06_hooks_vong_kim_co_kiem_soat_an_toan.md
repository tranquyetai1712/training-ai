# KỊCH BẢN LỜI THOẠI BÀI HỌC 6.1
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 2:** Kho Vũ Khí 7 Trụ Cột Cho Dân Văn Phòng  
**Phần 6:** Trụ Cột 4 — Hooks: Vòng Kim Cô Bảo Vệ An Toàn Dữ Liệu Tuyệt Đối  
**Tên bài:** Bài 6.1: Hooks là gì? Người gác cổng giám sát hành động của AI  
**Thời lượng dự kiến:** 08:00  
**Slide tương ứng:** `phan_06_tru_cot_hooks.html` (Slide 1)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_06_tru_cot_hooks.html` (Slide 12 và Slide 13).
* **Hình ảnh ẩn dụ:** Hình ảnh Trạm kiểm soát an ninh sân bay (người gác cổng soi chiếu hành lý trước khi lên máy bay).
* **Tông giọng:** Nghiêm túc, an tâm, toát lên sự an toàn và kỷ luật sắt của hệ thống.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD SCRIPT)

### [00:00 - 01:30] MỞ ĐẦU: VÌ SAO CHÚNG TA CẦN MỘT "NGƯỜI GÁC CỔNG AN NINH"?
`[Hiển thị Slide 1: Trụ Cột 4 — Hooks: Vòng Kim Cô Giám Sát AI]`  
`[Tông giọng trầm ấm, đặt vấn đề bảo mật thực tế]`

"Chào mừng các bạn đến với **Phần 6: Trụ Cột 4 — Hooks (Vòng Kim Cô Bảo Vệ An Toàn Dữ Liệu Tuyệt Đối)**!

Trong công việc, có một quy luật luôn đúng:  
*'Nhân viên càng nhiệt tình, càng xông xáo... thì nguy cơ làm ẩu, làm sai càng cao!'*  
Và trợ lý AI cũng không ngoại lệ. Khi bạn giao cho nó một nhiệm vụ lớn, nó sẽ lao vào làm việc rất nhanh. Nhưng nếu lỡ nó hiểu nhầm một câu lệnh và định **ghi đè lên file dữ liệu gốc của khách hàng**, hoặc vô tình **sửa đổi một hợp đồng pháp lý quan trọng** thì hậu quả sẽ khôn lường!

Làm thế nào để dù bạn có lỡ tay ra lệnh sai, máy tính của bạn vẫn có một **'Cơ chế tự vệ tự động'** để chặn đứng hành vi nguy hiểm đó ngay từ trong trứng nước?  
Đó chính là sứ mệnh của **Hooks** — Trạm gác an ninh tự động của Antigravity!"

---

### [01:30 - 04:30] ẨN DỤ DỄ HIỂU: TRẠM KIỂM SOÁT AN NINH SÂN BAY
`[Chỉ chuột vào hình ảnh Trạm Gác An Ninh 2 Lớp trên Slide 12]`  
`[Giải thích sinh động 2 chốt chặn PreToolUse và PostToolUse]`

"Để hiểu Hooks hoạt động ra sao, bạn hãy tưởng tượng quy trình đi máy bay tại sân bay:
* Khi bạn chuẩn bị bước lên máy bay, bạn phải đi qua **Cửa kiểm tra an ninh (PreToolUse)**: Nhân viên an ninh soi hành lý của bạn. Nếu bạn mang theo đồ cấm (như dao kéo hay chất lỏng quá mức), họ sẽ chặn bạn lại ngay lập tức và không cho bạn bước tiếp!
* Khi máy bay hạ cánh và bạn lấy hành lý ra, có một **Cửa kiểm tra hải quan (PostToolUse)**: Nhân viên đối chiếu hành lý xem có đúng tem phiếu không rồi mới cho bạn ra khỏi sân bay.

Trong Antigravity:
* Mỗi khi AI muốn dùng một công cụ — ví dụ: công cụ sửa file, công cụ xóa file, hay công cụ gửi email — nó **BẮT BUỘC phải đi qua Trạm gác Hooks**:
  1. **Chốt chặn 1 — Trước khi hành động (PreToolUse):**  
     Hook sẽ soi xét: *'AI định mở file nào? Định làm gì?'*. Nếu AI định xóa một file có chữ `goc_` hoặc `backup_`, Hook lập tức **thổi còi báo động, chặn đứng lệnh đó lại** và báo cho bạn!
  2. **Chốt chặn 2 — Sau khi hành động (PostToolUse):**  
     Sau khi AI tạo ra một file báo cáo, Hook sẽ tự động quét lại một lượt: *'Báo cáo này có đủ các cột số liệu bắt buộc không? Có bị thiếu dòng nào không?'*. Nếu phát hiện thiếu, Hook sẽ yêu cầu AI phải bổ sung ngay trước khi mang ra nộp cho bạn!"

---

### [04:30 - 06:45] FILE CẤU HÌNH HOOKS.JSON: ĐƠN GIẢN VÀ DỄ DÙNG
`[Chuyển Slide 13: Cấu Trúc Của Tệp hooks.json]`  
`[Rê chuột chỉ vào vị trí lưu tệp]`

"Toàn bộ luật lệ của Trạm gác an ninh này được đặt gọn gàng trong một file cấu hình mang tên `hooks.json` tại thư mục `.gemini/config/hooks.json` trên máy tính của bạn:
* Bạn chỉ cần khai báo rất ngắn gọn:
  * Sự kiện cần gác cổng: Ví dụ `PreToolUse` (trước khi dùng công cụ sửa file).
  * Điều kiện kiểm tra: Nếu tên file nằm trong danh sách được bảo vệ.
  * Hành động: Dừng lại ngay lập tức và xuất cảnh báo!
* Bạn hoàn toàn không cần phải thức đêm trông chừng AI. Trạm gác Hooks sẽ thay bạn làm nhiệm vụ bảo vệ tài sản dữ liệu 24/7!"

---

### [06:45 - 08:00] TỔNG KẾT BÀI & CÂU DẪN SANG THỰC HÀNH BÀI 6.2
`[Quay lại màn hình camera, nụ cười an tâm]`

"Khi đã có Hooks, bạn có thể hoàn toàn thở phào nhẹ nhõm: Dữ liệu của bạn được bảo vệ bởi một tấm khiên sắt kiên cố, không ai — kể cả một con AI thông minh nhất — có thể vô tình phá hỏng tệp gốc của bạn!

Bây giờ, hãy cùng tôi bước vào **Bài 6.2: Thực hành cài chốt chặn PreToolUse ngăn AI sửa đè file gốc**!  
Chúng ta sẽ cùng thiết lập một kịch bản thực tế: Cố tình ra lệnh cho AI sửa vào file dữ liệu gốc, và tận mắt chứng kiến Trạm gác Hooks thổi còi chặn đứng hành vi đó như thế nào!

Mời các bạn bấm sang Bài 6.2 ngay bây giờ!"
