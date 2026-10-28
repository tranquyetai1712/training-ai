# KỊCH BẢN LỜI THOẠI BÀI HỌC 9.2
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 3:** Phòng Thí Nghiệm Thực Chiến Đỉnh Cao  
**Phần 9:** ⭐ Thực Chiến 01 — Trợ Lý Hộp Thư: Tự Động Phân Loại & Dán Nhãn Email Khẩn Cấp  
**Tên bài:** Bài 9.2: Thực hành: Trợ lý AI tự động đọc hiểu hộp thư đến, phân loại và gắn nhãn theo mức độ ưu tiên  
**Thời lượng dự kiến:** 10:00  
**Slide tương ứng:** `phan_09_thuc_chien_email.html` (Slide 2)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_09_thuc_chien_email.html` (Slide 2).
* **Màn hình chia đôi hoặc chuyển Alt+Tab:**  
  * Cửa sổ 1: Ứng dụng Antigravity Desktop.  
  * Cửa sổ 2: Trình duyệt web mở hòm thư Gmail thực tế đang có sẵn các email mẫu chưa được gắn nhãn.
* **Tông giọng:** Thực chiến, nhịp độ nhanh, dứt khoát, hướng dẫn chi tiết từng câu lệnh và thao tác kiểm chứng trực tiếp.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD SCRIPT)

### [00:00 - 01:20] MỞ ĐẦU: BẮT TAY VÀO DỌN DẸP HỘP THƯ GMAIL THỰC TẾ
`[Hiển thị Slide 2: Thực Hành: Hệ Thống 4 Nhãn Màu Tự Động]`  
`[Mở tab Gmail hiển thị danh sách thư chưa có nhãn]`

"Chào mừng các bạn đã quay trở lại với Bài 9.2!

Các bạn hãy nhìn vào màn hình của tôi:  
Đây là hòm thư Gmail của tôi với khoảng 10 bức thư chưa đọc đủ mọi thể loại: từ thông báo tuyển dụng, hóa đơn tiền cước điện thoại, đến email của khách hàng đối tác yêu cầu gửi hợp đồng gấp.  
Hiện tại, các bức thư này hoàn toàn chưa có bất kỳ một nhãn dán nào.

Bây giờ, chúng ta sẽ mở Antigravity Desktop lên và ra lệnh cho trợ lý AI quét qua toàn bộ hòm thư này để tự động dán nhãn thông minh nhé!"

---

### [01:20 - 04:00] BƯỚC 1: SOẠN CÂU LỆNH CHUẨN 4 BƯỚC VÀNG CHO TRỢ LÝ HỘP THƯ
`[Chuyển màn hình sang Antigravity Desktop]`  
`[Bấm nút New Task, mở khung nhập lệnh]`

"Các bạn hãy nhìn vào khung chat:  
Tôi sẽ áp dụng đúng **Công thức 4 bước vàng** mà chúng ta đã học ở Phần 2:

> *'Chào Antigravity, bạn hãy đóng vai trò là Trợ lý Hộp thư thông minh.*  
> *1. Bối cảnh: Hãy sử dụng công cụ Gmail MCP để đọc 10 email chưa đọc gần nhất trong hộp thư đến (Inbox) của tôi.*  
> *2. Mục tiêu: Phân tích nội dung thực tế của từng bức thư và tự động gắn nhãn (Label) theo 4 mức độ:*  
> *   - 🔴 `01-UuTien-KhanCap`: Email từ sếp, khách hàng VIP, hoặc yêu cầu phản hồi gấp trong ngày.*  
> *   - 🟡 `02-ChoXuLy`: Hợp đồng, tài liệu chuyên môn cần thời gian nghiên cứu.*  
> *   - 🟢 `03-HoaDon-ChungTu`: Hóa đơn điện tử, biên lai, sao kê tài chính.*  
> *   - ⚪ `04-ThamKhao-QuangCao`: Tin khuyến mãi, thông báo hệ thống.*  
> *3. Tiêu chuẩn đầu ra: Nếu nhãn nào chưa có trên Gmail, bạn hãy tự động tạo nhãn mới. Sau khi gắn nhãn xong, hãy xuất một bảng tổng hợp tóm tắt 10 email sang cửa sổ bên phải.*  
> *4. Giới hạn an toàn: Tuyệt đối KHÔNG xóa bất kỳ email nào, và KHÔNG được tự ý soạn hay gửi email trả lời khi chưa hỏi ý kiến tôi.'*

`[Nhấn phím Enter]`  
Và bây giờ, hãy xem Antigravity bắt đầu hành động!"

---

### [04:00 - 07:30] BƯỚC 2: QUAN SÁT AI TỰ ĐỘNG ĐỌC THƯ VÀ GẮN NHÃN
`[Chỉ chuột vào luồng thực thi của AI]`  
`[Giải thích chi tiết từng công cụ MCP đang được gọi ngầm]`

"Các bạn nhìn luồng suy nghĩ của AI trên màn hình:
1. `[AI gọi công cụ gmail_list_messages]` Nó quét qua 10 email gần nhất.
2. `[AI gọi công cụ gmail_read_message]` Nó đọc nội dung của từng bức thư:
   * Bức thư 1: Khách hàng yêu cầu: *'Gửi báo giá gấp trước 11h'*. AI lập tức xếp vào mức độ **01-UuTien-KhanCap**.
   * Bức thư 2: Thông báo cước internet Viettel tháng 10. AI nhận diện ngay là **03-HoaDon-ChungTu**.
   * Bức thư 3: Bản tin khuyến mãi vé máy bay. AI xếp vào **04-ThamKhao-QuangCao**.
3. `[AI gọi công cụ gmail_create_label và gmail_modify_email]`  
   Nó kiểm tra trên tài khoản Gmail: Nhãn `01-UuTien-KhanCap` chưa có, nó **tự động tạo nhãn mới**, sau đó **gắn chiếc cờ đỏ vào bức thư** ngay lập tức!"

---

### [07:30 - 09:15] BƯỚC 3: MỞ TAB GMAIL VÀ NGHIỆM THU THỰC TẾ
`[Chuyển màn hình sang tab trình duyệt Gmail]`  
`[Nhấn phím F5 làm mới trang web]`

"Bây giờ, chúng ta hãy cùng chuyển sang tab trình duyệt Gmail để nghiệm thu kết quả nhé!  
`[Bấm F5 refresh trang Gmail]`  
`[Tông giọng trầm trồ, vỗ tay hào hứng]`  
Ồ các bạn nhìn xem! Thật không thể tin được:
* Toàn bộ 10 bức thư vừa rồi đã được gắn các nhãn màu rực rỡ và ngăn nắp!
* Nhìn vào cột bên trái Gmail: 4 thư mục nhãn mới đã được tạo sẵn.
* Bức thư khẩn cấp của khách hàng đã nổi bật lên với chiếc nhãn đỏ `01-UuTien-KhanCap`.
* Và quay lại Antigravity: Ở cửa sổ bên phải, AI đã chuẩn bị sẵn một bảng tóm tắt 10 bức thư cực kỳ ngắn gọn, ghi rõ người gửi, nội dung cốt lõi và mức độ khẩn cấp để bạn nắm bắt toàn bộ tình hình chỉ trong vòng 30 giây đọc lướt!"

---

### [09:15 - 10:00] TỔNG KẾT BÀI & CÂU DẪN SANG BÀI 9.3
`[Quay lại màn hình camera, nụ cười rạng rỡ]`

"Chỉ với 1 câu lệnh duy nhất, 10 bức thư hỗn độn đã được phân loại hoàn hảo.  
Nhưng các bạn có đồng ý với tôi rằng: Sẽ còn tuyệt vời hơn nữa nếu bạn **hoàn toàn không cần phải mở máy tính lên gõ lệnh**?

Nếu bạn muốn: *'Cứ đúng 8h00 sáng mỗi ngày, trong lúc bạn đang thảnh thơi nhâm nhi tách cà phê sáng, trợ lý AI sẽ tự động thức dậy, tự dọn dẹp hòm thư và điểm tin cho bạn'* thì phải làm sao?

Chào mừng các bạn đến với **Bài 9.3: Lên lịch hẹn giờ tự động bằng lệnh `/schedule`**!  
Mời các bạn cùng bấm sang Bài 9.3 ngay bây giờ!"
