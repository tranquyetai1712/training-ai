# KỊCH BẢN LỜI THOẠI BÀI HỌC 8.1
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 3:** Phòng Thí Nghiệm Thực Chiến Đỉnh Cao  
**Phần 8:** Dự Án Văn Phòng Đỉnh Cao  
**Tên bài:** Bài 8.1: Thực Chiến 01 — Điều Phối Đa Kênh: Tự Tạo Thẻ Trello & Bắn Thông Báo Slack  
**Thời lượng dự kiến:** 09:00  
**Slide tương ứng:** `phan_08_thuc_chien_van_phong_dinh_cao.html` (Slide 1: Điều Phối Đa Kênh: Trello & Slack)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở slide Thực Chiến 01 (Dự Án 1: Điều Phối Đa Kênh Trello & Slack).
* **Màn hình chia đôi hoặc sẵn sàng chuyển tab:**  
  * Cửa sổ 1: Ứng dụng **Antigravity Desktop** đang mở thư mục làm việc, có sẵn file kế hoạch tuần `ke_hoach_giao_ban_tuan.md` (3 Action Items: Hoàng Anh - Landing Page; Thu Trang - Kịch bản Video; Tuấn Vũ - Kiểm kê tồn kho).  
  * Cửa sổ 2: Trình duyệt web mở bảng công việc **Trello** (Bảng *"Chiến Dịch Q4"*).  
  * Cửa sổ 3: Nhóm chat nội bộ **Slack** (kênh `#thong-bao-chung` của công ty).
* **Tông giọng:** Khí thế, bản lĩnh, phân tích sắc sảo như một chuyên gia tư vấn quy trình tự động hóa; truyền cảm hứng cho người học về tư duy "tự chế tạo vũ khí cho riêng mình".

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD SCRIPT)

### [00:00 - 01:45] CHÀO MỪNG ĐẾN KHỐI 3 & BÀI TOÁN THỰC TẾ ĐẦU TUẦN
`[Hiển thị Slide Thực Chiến 01: Dự Án 1 - Điều Phối Đa Kênh Trello & Slack]`  
`[Người hướng dẫn nhìn thẳng camera, ánh mắt đầy tự tin và hào hứng]`

"Chào mừng tất cả các bạn đã chính thức đặt chân vào **Khối 3: Phòng Thí Nghiệm Thực Chiến Đỉnh Cao**!  
Nếu như ở Khối 2, chúng ta đã thu thập đủ 6 viên ngọc bảo bối — từ Rules, Skills, Hooks, MCP cho đến Plugins và Automations — thì bước vào Khối 3, chúng ta sẽ không nói về lý thuyết công cụ nữa. Ở đây chỉ có **Bài toán thực tế của công sở** và **Cách ra lệnh cho AI giải quyết trọn vẹn trong chớp mắt**!

Hãy bắt đầu ngay với một bài toán kinh điển mà bất kỳ người đi làm nào cũng từng nếm trải: **Nỗi ám ảnh giao ban sáng thứ Hai**!  
Sáng nay, sau cuộc họp giao ban, sếp duyệt một bản kế hoạch tóm tắt được lưu trong tệp `ke_hoach_giao_ban_tuan.md`. Trong đó có 3 đầu việc lớn cần phân công khẩn cấp:
* Hoàng Anh thiết kế Landing Page chiến dịch.
* Thu Trang viết kịch bản Video quảng cáo.
* Tuấn Vũ kiểm kê số liệu tồn kho.

Quy trình bình thường của dân văn phòng là gì?
1. Bạn mở phần mềm quản lý việc **Trello** lên, bấm tạo từng chiếc thẻ việc (Card), gõ tên nhân sự, copy mô tả việc, chọn hạn chót (Deadline) và gắn nhãn màu.
2. Xong Trello, bạn lại phải mở ứng dụng chat **Slack** lên, gõ một tin nhắn tóm tắt thật chỉn chu, tag tên mọi người vào kênh `#thong-bao-chung` để thông báo cho toàn thể công ty.

Làm tay 2 việc này ngốn của bạn 20 đến 30 phút mỗi đầu tuần, lại rất dễ gõ nhầm ngày giờ hoặc sót tên nhân sự!  
Hôm nay, chúng ta sẽ giải quyết bài toán này. Nhưng không phải bằng cách ra lệnh một câu tạm bợ dùng một lần — mà chúng ta sẽ **dạy AI tự thiết kế ra một Kỹ Năng (Skill) chuẩn chỉnh** để từ nay về sau, cứ mỗi sáng thứ Hai, bạn chỉ cần gõ đúng một câu lệnh là toàn bộ công việc tự động hoàn tất 100%!"

---

### [01:45 - 04:15] NÂNG CẤP TƯ DUY: TẠI SAO NÊN RA LỆNH CHO AI TẠO SKILL?
`[Chuyển màn hình sang Antigravity Desktop]`  
`[Mở thư mục dự án và file ke_hoach_giao_ban_tuan.md cho học viên xem]`

"Nhiều người dùng AI thường mắc một sai lầm: Mỗi lần có việc lại ngồi nghĩ ra một câu prompt dài dòng, tuần sau gặp lại việc đó lại phải ngồi gõ lại từ đầu. Đó là cách làm của người mới bắt đầu!  
Cách làm của một nhân viên số chuyên nghiệp là: **Khi phát hiện một quy trình lặp lại, hãy yêu cầu AI đóng gói nó thành một Kỹ năng (Skill)**.  

Một kỹ năng hoàn chỉnh giải quyết bài toán này sẽ bao gồm:
1. File hướng dẫn nghiệp vụ `SKILL.md` (chỉ rõ cách đọc kế hoạch, cách gọi Trello MCP và Slack MCP).
2. Quy tắc an toàn (`Rules`): Quy định thẻ Trello phải luôn có đủ Deadline và định dạng Markdown chuẩn, tin nhắn Slack phải lịch sự, không được gửi nhầm vào kênh cấm.
3. Chốt chặn bảo vệ (`Hooks`): Ngăn không cho xóa nhầm bảng Trello hoặc gửi thông báo rác khi chưa xác nhận.

Bây giờ, làm thế nào để ra lệnh cho Antigravity tự tạo ra toàn bộ bộ kỹ năng này?  
Hãy cùng tôi áp dụng **Công thức 4 bước vàng ra lệnh** mà chúng ta đã học ở Bài 2.2!"

---

### [04:15 - 06:15] SOẠN PROMPT VÀNG & BÓC TÁCH: TẠI SAO ĐÂY LÀ PROMPT TỐT?
`[Quay màn hình khung chat Antigravity Desktop]`  
`[Dán câu prompt mẫu lên màn hình, làm nổi bật từng phần bằng các màu sắc tương ứng]`

"Đây là câu prompt tôi gửi cho Antigravity để yêu cầu tạo kỹ năng:

> *'Chào Antigravity, tôi muốn bạn đóng vai một Chuyên gia Kỹ thuật Tự động hóa. Hãy giúp tôi tạo một Kỹ Năng mới (Skill) mang tên `dieu-phoi-trello-slack` nằm trong thư mục `skills/dieu-phoi-trello-slack/` với các yêu cầu sau:*  
> *1. [Mục tiêu]: Tạo file `SKILL.md` hướng dẫn quy trình tự động đọc file kế hoạch công việc bất kỳ (dạng .md hoặc .txt) trong thư mục làm việc, trích xuất danh sách công việc, sau đó tự động tạo thẻ việc trên Trello qua Trello MCP và gửi thông báo tóm tắt vào Slack qua Slack MCP.*  
> *2. [Bối cảnh]: Dự án của tôi sử dụng bảng Trello tên là `Chiến Dịch Q4`, danh sách mặc định cần thêm thẻ là cột `Cần Làm (To Do)`. Kênh Slack công ty là `#thong-bao-chung`.*  
> *3. [Tiêu chuẩn]: Thẻ Trello bắt buộc phải có đầy đủ: Tiêu đề việc, Người phụ trách, Mô tả chi tiết và Hạn chót (Deadline theo định dạng YYYY-MM-DD). Tin nhắn Slack phải được định dạng đẹp mắt với icon thông báo, có lời chào đầu tuần, danh sách gạch đầu dòng rõ ràng từng người và đính kèm link tới bảng Trello.*  
> *4. [Giới hạn & An toàn]: Tích hợp quy tắc an toàn: Tuyệt đối không xóa bất kỳ thẻ cũ nào trên Trello; nếu file kế hoạch thiếu thông tin người phụ trách hoặc hạn chót, AI phải hỏi lại người dùng để xác nhận chứ không được tự tiện bịa đặt.'*

`[Dừng lại 5 giây, chỉ chuột vào từng đoạn prompt]`  
Các bạn hãy nhìn kỹ lại prompt này! **Tại sao đây lại là một prompt xuất sắc?**  
Hãy đối chiếu với 4 bước vàng:
* **Bước 1 — Mục tiêu cụ thể (Goal):** Chúng ta không nói chung chung 'hãy tự động hóa Trello và Slack'. Chúng ta chỉ đích danh: *Tạo một Skill mang tên `dieu-phoi-trello-slack`, tạo file `SKILL.md` để kết nối 2 cổng Trello MCP và Slack MCP*. AI hiểu ngay sản phẩm đầu ra cần tạo là gì!
* **Bước 2 — Bối cảnh rõ ràng (Context):** Cung cấp chính xác tên bảng Trello (`Chiến Dịch Q4`), tên cột (`To Do`), tên kênh Slack (`#thong-bao-chung`). AI không phải đoán mò hay hỏi đi hỏi lại.
* **Bước 3 — Tiêu chuẩn đầu ra (Standard):** Yêu cầu cụ thể từng trường dữ liệu của thẻ Trello (Tiêu đề, Người phụ trách, Hạn chót chuẩn ISO), và quy chuẩn thẩm mỹ của tin nhắn Slack (icon, lời chào, gạch đầu dòng, link bảng).
* **Bước 4 — Giới hạn an toàn (Boundary):** Đặt 'vòng kim cô' cấm xóa thẻ cũ, cấm bịa đặt thông tin khi thiếu dữ liệu.

Một prompt đầy đủ 4 yếu tố này giúp AI thực thi chính xác 100% ngay ở lần đầu tiên mà không bị lạc đề!"

---

### [06:15 - 07:30] AI TỰ ĐỘNG SINH KỸ NĂNG VÀ KIỂM TRA BẰNG SUBLIME TEXT
`[Bấm Enter gửi câu prompt]`  
`[Camera quay trực tiếp quá trình Antigravity tạo thư mục và viết file]`

"Các bạn nhìn xem! Ngay sau khi nhận lệnh, Antigravity phân tích và lập tức hành động:
1. Nó tạo thư mục `skills/dieu-phoi-trello-slack/`.
2. Bên trong, nó viết file `SKILL.md` với đầy đủ frontmatter, hướng dẫn gọi các công cụ `trelloWriteCard`, `slack_post_message`, và kịch bản xử lý từng bước.
3. Nó còn bổ sung sẵn một file quy tắc nhỏ đi kèm `rules/trello_safety.md` để đảm bảo thẻ việc luôn được đặt đúng cột!

Bây giờ tôi mở **Sublime Text** lên: Thư mục `skills/dieu-phoi-trello-slack` đã xuất hiện nguyên vẹn, cấu trúc chuẩn xác như một lập trình viên kỳ cựu vừa viết ra!"

---

### [07:30 - 08:30] THỰC THI KIỂM CHỨNG: 1 CÂU LỆNH GIẢI QUYẾT BÀI TOÁN GIAO BAN
`[Mở lại khung chat Antigravity Desktop]`  
`[Gõ câu lệnh kích hoạt skill vừa tạo]`

"Bây giờ là lúc tận hưởng thành quả! Kỹ năng đã sẵn sàng trên máy. Sáng thứ Hai đến, tôi chỉ cần gõ đúng một câu ngắn gọn:  
> *'Hãy dùng skill `dieu-phoi-trello-slack` để xử lý kế hoạch giao ban trong tệp `ke_hoach_giao_ban_tuan.md` cho tôi!'*  
`[Bấm Enter]`

Các bạn nhìn màn hình thực thi:  
* AI đọc file kế hoạch ➔ Nhận diện ngay 3 nhân sự: Hoàng Anh, Thu Trang, Tuấn Vũ.  
* Nó kích hoạt Trello MCP ➔ Bắn 3 thẻ việc mới vào đúng cột `To Do` của bảng `Chiến Dịch Q4`.  
* Nó kích hoạt Slack MCP ➔ Định dạng tin nhắn chào tuần mới và gửi thẳng vào kênh `#thong-bao-chung`.

`[Mở tab Trello và tab Slack lên kiểm chứng]`  
Hãy nhìn sang Trello: 3 chiếc thẻ việc mới tinh đã nằm ngay ngắn, đủ hạn chót, đủ nhãn màu!  
Nhìn sang Slack: Ting một tiếng! Tin nhắn thông báo đẹp như mơ đã hiển thị trước mắt toàn bộ phòng ban!  
**Toàn bộ quy trình chỉ mất đúng 35 giây!**"

---

### [08:30 - 09:00] TỔNG KẾT & DẪN SANG BÀI THỰC CHIẾN 02
`[Quay lại màn hình camera, nụ cười rạng rỡ]`

"Thật tuyệt vời đúng không các bạn? Từ việc loay hoay làm tay 30 phút mỗi sáng thứ Hai, bạn đã biến Antigravity thành một Điều phối viên tự động hóa đa nền tảng chỉ bằng cách biết cách ra lệnh tạo Skill chuẩn chỉnh!

Và chưa dừng lại ở đó! Một bài toán kinh điển thứ hai mà ai đi làm cũng đau đầu chính là **Hộp thư Gmail ngập ngụa hàng trăm email mỗi ngày**: thư báo giá, thư khiếu nại, thư đối tác, thư quảng cáo lẫn lộn vào nhau.  
Ở bài học tiếp theo — **Bài 8.2: Thực Chiến 02**, chúng ta sẽ tiếp tục ra lệnh cho AI tạo ra một **Skill Trợ Lý Hộp Thư: Đọc Hiểu, Phân Loại Email & Gán Nhãn Tự Động**!

Mời các bạn cùng bấm sang **Bài 8.2** để tiếp tục khám phá!"
