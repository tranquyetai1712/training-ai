# KỊCH BẢN LỜI THOẠI BÀI HỌC 4.1
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 2:** Kho Vũ Khí 7 Trụ Cột Cho Dân Văn Phòng  
**Phần 4:** Trụ Cột 2 — Skills: Trang Bị Thêm "Bí Kíp Chuyên Môn" Trong Vài Giây  
**Tên bài:** Bài 4.1: Khái niệm Skills - Tải thêm kỹ năng chuyên môn không lo đầy bộ nhớ  
**Thời lượng dự kiến:** 08:00  
**Slide tương ứng:** `phan_04_tru_cot_skills.html` (Slide 1)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_04_tru_cot_skills.html` (Slide 5 và Slide 6).
* **Minh họa thư mục:** Mở sẵn thư mục chứa Skills trên máy tính để minh họa cấu trúc tệp tin.
* **Tông giọng:** Sôi nổi, gợi mở, dùng hình ảnh ẩn dụ cuốn sách chuyên môn để người học dễ dàng phân biệt giữa Rules và Skills.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD SCRIPT)

### [00:00 - 01:30] MỞ ĐẦU: PHÂN BIỆT RÕ RÀNG GIỮA "NỘI QUY" VÀ "BÍ KÍP NGHỀ"
`[Hiển thị Slide 1: Trụ Cột 2 — Skills: Bí Kíp Chuyên Môn Đóng Gói]`  
`[Tông giọng hào hứng, tương tác với học viên]`

"Chào mừng các bạn đến với **Phần 4: Trụ Cột 2 — Skills (Kỹ Năng Nghiệp Vụ Chuyên Biệt)**!

Ở phần trước, chúng ta đã học về **Rules** — cuốn sổ tay nội quy. Nhưng có một câu hỏi rất hay mà học viên thường hỏi tôi:  
*'Thầy ơi, nếu tôi muốn AI biết làm những việc chuyên môn sâu — ví dụ: biết đọc ảnh chụp hóa đơn mờ, biết quét hợp đồng tìm lỗi pháp lý, hay biết dọn dẹp và đổi tên hàng trăm file lộn xộn — thì tôi có nên viết tất cả những thứ đó vào file Rules không?'*

`[Nhấn mạnh dứt khoát]`  
Câu trả lời là: **TUYỆT ĐỐI KHÔNG!**  
Bởi vì nếu bạn nhét hàng tá quy trình chuyên môn dài ngoằng vào Rules, bộ não của AI sẽ bị bội thực ngay từ khi vừa khởi động. Bạn chưa kịp giao việc gì thì bộ nhớ của nó đã đầy ắp lý thuyết rồi!

Và để giải quyết bài toán này, các kỹ sư Google mang đến cho chúng ta vũ khí số 2: **Skills — Tải kỹ năng chuyên môn theo nhu cầu (On-demand)**!"

---

### [01:30 - 04:30] ẨN DỤ DỄ HIỂU: CUỐN SÁCH KỸ THUẬT TRÊN GIÁ SÁCH
`[Chỉ chuột vào hình ảnh Giá Sách Kỹ Năng trên Slide 8]`  
`[Giải thích cơ chế nạp kỹ năng thông minh]`

"Để hiểu Skills hoạt động ra sao, bạn hãy tưởng tượng trong văn phòng của bạn có một chiếc **Giá sách nghiệp vụ**:
* Trên giá sách có cuốn: *'Cẩm nang Đổi tên file tự động'*, cuốn *'Sổ tay Kiểm toán nội bộ'*, cuốn *'Bí kíp Thiết kế biểu đồ báo cáo'*.
* Hàng ngày, nhân viên của bạn **không cần phải học thuộc lòng** cả cái giá sách đó.
* Khi nào bạn giao việc: *'Em ơi, dọn dẹp và đổi tên lại thư mục tài liệu cho ngăn nắp'*, nhân viên đó mới bước tới giá sách, rút đúng cuốn *'Cẩm nang Đổi tên file tự động'* ra đọc, làm xong việc thì cất sách lại lên giá!

Cơ chế này trong công nghệ gọi là **Nạp kỹ năng khi cần (Lazy Loading / On-demand)**:
* Khi không dùng, Skill nằm yên tĩnh trên ổ cứng máy tính của bạn, hoàn toàn không chiếm dụng dù chỉ 1 token bộ nhớ của AI.
* Chỉ khi nào bạn gọi đúng tên Skill đó, hoặc yêu cầu một công việc liên quan, Antigravity mới kích hoạt cuốn cẩm nang đó lên để xử lý nhiệm vụ. Nhờ vậy, máy tính của bạn luôn chạy mượt mà và bộ nhớ AI luôn thanh thoát!"

---

### [04:30 - 06:45] BÓC TÁCH CẤU TRÚC BÊN TRONG CỦA MỘT SKILL
`[Chuyển Slide 6: Cấu Trúc Giải Phẫu Một Thư Mục Skill Chuẩn Mực]`  
`[Rê chuột chỉ rõ 2 thành phần cốt lõi]`

"Một Skill trong Antigravity thực chất được cấu tạo như thế nào? Cực kỳ đơn giản:
* Nó là một thư mục mang tên kỹ năng đó (ví dụ: `doi-ten-file-tu-dong`).
* Bên trong thư mục, **thành phần bắt buộc duy nhất** là tệp `SKILL.md`.  
  Tệp này có 2 phần:
  1. **Phần thẻ thông tin trên cùng (Frontmatter):** Gồm tên kỹ năng (`name`) và mô tả ngắn gọn (`description`) cho biết kỹ năng này dùng để làm gì và khi nào nên kích hoạt.
  2. **Phần hướng dẫn quy trình bên dưới:** Chỉ dẫn chi tiết từng bước AI cần làm theo thứ tự 1, 2, 3, 4 y hệt như một quy trình thao tác chuẩn (SOP) trong doanh nghiệp.
* Ngoài ra, nếu kỹ năng đó cần tính toán hoặc xử lý file phức tạp, nó có thể đi kèm một thư mục phụ mang tên `scripts/` chứa các kịch bản tự động hóa sẵn có."

---

### [06:45 - 08:00] TỔNG KẾT BÀI & BƯỚC VÀO TRẢI NGHIỆM THỰC HÀNH BÀI 4.2
`[Quay lại màn hình camera, tông giọng hào hứng]`

"Bây giờ các bạn đã hiểu: Skills chính là những 'tuyệt kỹ võ công' mà chúng ta có thể nạp thêm cho trợ lý bất kỳ lúc nào để giải quyết những bài toán hóc búa nhất.

Và để các bạn thấy được sức mạnh thực chiến của Skills trong công việc văn phòng hàng ngày, ngay ở bài học tiếp theo — **Bài 4.2**, chúng ta sẽ cùng nhau thực hành trực tiếp một Skill thực tế cực kỳ đỉnh cao mang tên `doi-ten-file-tu-dong`!  
Nó sẽ giúp bạn đọc nội dung của hàng loạt ảnh chụp, file Word, file PDF mang tên lộn xộn và tự động chuẩn hóa lại tên file một cách thần kỳ!

Hãy chuẩn bị sẵn sàng, và cùng tôi bước sang Bài 4.2 ngay bây giờ!"
