# KỊCH BẢN LỜI THOẠI BÀI HỌC 11.3
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 3:** Phòng Thí Nghiệm Thực Chiến Đỉnh Cao  
**Phần 11:** ⭐ Thực Chiến 03 — Thư Ký Họp AI: Nghe File Ghi Âm Tự Viết Biên Bản & Phân Công Việc  
**Tên bài:** Bài 11.3: Tự động tạo thẻ việc phân công trên Trello và bắn thông báo vào nhóm Slack  
**Thời lượng dự kiến:** 10:00  
**Slide tương ứng:** `phan_11_thuc_chien_thu_ky_hop.html` (Slide 3)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_11_thuc_chien_thu_ky_hop.html` (Slide 5: Tự Động Tạo Thẻ Trello & Bắn Thông Báo Slack).
* **Màn hình chia đôi hoặc sẵn sàng chuyển tab:**  
  * Cửa sổ 1: Ứng dụng Antigravity Desktop.  
  * Cửa sổ 2: Trình duyệt web mở bảng công việc Trello (Bảng "Chiến Dịch Tháng 10").  
  * Cửa sổ 3: Nhóm chat nội bộ Slack (kênh `#thong-bao-chung` của công ty.
* **Tông giọng:** Đỉnh cao năng lượng, hào sảng, mang lại cảm xúc vỡ òa khi toàn bộ quy trình tự động hóa khép kín hoạt động trơn tru trước mắt học viên.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD SCRIPT)

### [00:00 - 01:25] MỞ ĐẦU: BƯỚC NHẢY VỌT TỪ TRANG GIẤY RA HÀNH ĐỘNG THỰC TẾ
`[Hiển thị Slide 3: Đồng Bộ Đa Kênh: Trello & Bắn Tin Slack]`  
`[Tông giọng hào hứng, dẫn dắt câu chuyện]`

"Chào mừng các bạn đến với Bài 11.3 — bài thực chiến đỉnh cao và được mong chờ nhất trong toàn bộ khóa học!

Ở bài trước, chúng ta đã có một bản Biên bản cuộc họp với bảng phân công công việc (Action Items) chuẩn không cần chỉnh.  
Nhưng một bản kế hoạch dù hay đến mấy, nếu nó chỉ nằm im trên file văn bản thì công việc vẫn chưa thể tự chạy.  
Trong môi trường doanh nghiệp hiện đại:
* Người quản lý phải mở bảng công việc **Trello** lên, tạo từng thẻ việc, gõ tên người phụ trách, gắn nhãn màu đỏ/vàng, và chọn ngày hết hạn (Deadline).
* Sau đó, lại phải mở **Slack** lên, soạn một đoạn tin nhắn ngắn gọn thông báo: *'Cuộc họp sáng nay đã chốt 3 việc sau đây, đề nghị các bộ phận nắm bắt và triển khai'*.

Nếu làm bằng tay cả 2 việc này, bạn lại tốn thêm 20 phút nữa.  
Hôm nay, chúng ta sẽ để Antigravity kết nối đa nền tảng: **Tự động tạo thẻ việc Trello và tự động bắn tin nhắn Slack** chỉ trong đúng một nốt nhạc!"

---

### [01:25 - 04:00] BƯỚC 1: SOẠN CÂU LỆNH ĐIỀU PHỐI ĐA NỀN TẢNG
`[Chuyển màn hình sang Antigravity Desktop]`  
`[Tiếp tục phiên làm việc đang có sẵn bảng Action Items từ Bài 11.2]`

"Tại chính phiên làm việc này, tôi sẽ gõ một câu lệnh điều phối đỉnh cao:

> *'Chào Antigravity, dựa trên bảng phân công hành động (Action Items) vừa lập từ cuộc họp, hãy thực hiện 2 nhiệm vụ tự động hóa sau:*  
> *1. Nhiệm vụ 1 — Tạo thẻ Trello: Sử dụng Trello MCP để truy cập vào bảng `Chiến Dịch Tháng 10`. Tại cột `Cần Làm (To Do)`, hãy tạo 3 thẻ việc mới tương ứng cho Hoàng Anh, Thu Trang và Tuấn Vũ, ghi rõ nội dung công việc và gắn đúng hạn chót (Deadline).*  
> *2. Nhiệm vụ 2 — Bắn thông báo nội bộ: Sử dụng Slack MCP để gửi một tin nhắn tóm tắt ngắn gọn gồm 3 quyết định cốt lõi và danh sách việc cần làm vào kênh `#thong-bao-chung` để toàn thể công ty nắm bắt.*  
> *Báo cáo lại cho tôi sau khi hoàn tất!'*

`[Nhấn phím Enter dứt khoát]`  
Và các bạn hãy cùng tôi nín thở theo dõi luồng thực thi!"

---

### [04:00 - 07:00] BƯỚC 2: QUAN SÁT AI TỰ ĐỘNG GỌI CÁC CÔNG CỤ NGOẠI VI
`[Chỉ chuột vào từng bước AI gọi công cụ MCP trên màn hình]`  
`[Giải thích sinh động từng chuyển động]`

"Các bạn hãy nhìn kỹ màn hình:
1. `[AI gọi công cụ trello_create_card]`  
   * Thẻ 1: Tạo thẻ 'Thiết kế Landing Page sản phẩm' ➔ Gán cho Hoàng Anh, Deadline: 18/10/2026.
   * Thẻ 2: Tạo thẻ 'Kịch bản quảng cáo Facebook & TikTok' ➔ Gán cho Thu Trang, Deadline: 20/10/2026.
   * Thẻ 3: Tạo thẻ 'Kiểm kê tồn kho hàng mẫu' ➔ Gán cho Tuấn Vũ, Deadline: 22/10/2026.
2. `[AI gọi công cụ slack_post_message]`  
   * Nó tự động soạn tin nhắn với icon đẹp mắt:  
     🔔 **[THÔNG BÁO GIAO BAN ĐẦU TUẦN - CHIẾN DỊCH 25/10]**  
     Nêu rõ 3 quyết định của Giám đốc và tag tên các nhân sự phụ trách.
   * Bấm 'Gửi' trực tiếp vào kênh chat chung của công ty!"

---

### [07:00 - 09:15] BƯỚC 3: MỞ TRELLO & SLACK ĐỂ NGHIỆM THU THỰC TẾ
`[Chuyển màn hình sang tab Trello]`  
`[Bấm F5 refresh trang Trello]`

"Bây giờ, hãy cùng tôi kiểm chứng ngoài đời thực nhé!  
`[Màn hình Trello mở lên]`  
`[Tông giọng vỡ òa, chỉ chuột vào 3 chiếc thẻ việc mới tinh]`  
Ồ các bạn nhìn xem! Tại cột 'To Do' của bảng Trello:  
Cả 3 thẻ công việc đã nằm ngay ngắn ở đây! Nhấp vào thẻ của Hoàng Anh: Đã có sẵn ngày hết hạn 18/10, có phần mô tả công việc rõ ràng!

`[Chuyển sang cửa sổ Slack]`  
`[Chỉ vào tin nhắn vừa được AI gửi đến]`  
Và trên kênh chat công ty: Tin nhắn tóm tắt vừa được gửi tới lúc này! Toàn bộ nhân viên trong công ty đã nhận được thông báo mà không cần bạn phải copy dán một dòng nào!

Từ một file ghi âm âm thanh thô sơ ➔ Đến bản biên bản họp sắc bén ➔ Đến các thẻ việc phân công trên Trello ➔ Và thông báo tức thì trên kênh Slack...  
**Toàn bộ chuỗi quy trình khép kín đó diễn ra trong vòng chưa đầy 2 phút!**"

---

### [09:15 - 10:00] TỔNG KẾT KHỐI 3 & DẪN SANG KHỐI 4: TỔNG KẾT & TỐT NGHIỆP
`[Quay lại màn hình camera, nụ cười rạng rỡ và ánh mắt đầy tự hào]`

"Kính thưa các bạn học viên, chúng ta đã xuất sắc chinh phục trọn vẹn cả **3 Dự Án Thực Chiến Đỉnh Cao**:
1. Dự án 1: Trợ lý Hộp thư tự động dán nhãn email và điểm tin 8h00 sáng.
2. Dự án 2: Kế toán số quét ảnh hóa đơn mờ tự động bóc tách đổ vào Excel có sẵn công thức tính tổng.
3. Dự án 3: Thư ký họp AI nghe file ghi âm tự viết biên bản, tạo thẻ Trello và gửi tin nhắn Slack!

Các bạn đã biến những điều tưởng chừng chỉ có trong phim khoa học viễn tưởng thành hiện thực ngay trên bàn làm việc của mình!

Và bây giờ, chỉ còn một chặng đường ngắn cuối cùng:  
Chúng ta sẽ cùng nhau bước sang **Phần 12: Đúc Kết Khóa Học & Bàn Giao Bộ Tài Nguyên Văn Phòng** — nơi tôi sẽ trao tặng cho bạn trọn bộ template mẫu có sẵn và hướng dẫn bạn nhận Chứng chỉ tốt nghiệp!

Hẹn gặp lại các bạn ở Bài 12.1 ngay sau đây!"
