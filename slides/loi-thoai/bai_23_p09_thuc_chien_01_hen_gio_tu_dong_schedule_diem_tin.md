# KỊCH BẢN LỜI THOẠI BÀI HỌC 9.3
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 3:** Phòng Thí Nghiệm Thực Chiến Đỉnh Cao  
**Phần 9:** ⭐ Thực Chiến 01 — Trợ Lý Hộp Thư: Tự Động Phân Loại & Dán Nhãn Email Khẩn Cấp  
**Tên bài:** Bài 9.3: Lên lịch hẹn giờ tự động bằng lệnh /schedule: 8h00 sáng AI tự thức dậy điểm tin  
**Thời lượng dự kiến:** 10:00  
**Slide tương ứng:** `phan_09_thuc_chien_email.html` (Slide 3)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_09_thuc_chien_email.html` (Slide 2).
* **Ứng dụng thực tế:** Mở Antigravity Desktop, chuẩn bị sẵn câu lệnh `/schedule` để gõ trực tiếp vào khung chat.
* **Tông giọng:** Hào hứng, say mê, mở ra đỉnh cao của tự động hóa: Biến AI thành một cỗ máy làm việc hoàn toàn tự động theo lịch trình.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD SCRIPT)

### [00:00 - 01:20] MỞ ĐẦU: ĐỈNH CAO TỰ ĐỘNG HÓA LÀ "KHÔNG CẦN CHẠM TAY"
`[Hiển thị Slide 3: Lên Lịch Hẹn Giờ: Cứ 8h00 Sáng AI Tự Điểm Tin]`  
`[Tông giọng trầm ấm, gợi cảm hứng]`

"Chào mừng các bạn đến với Bài 9.3 — bài học hoàn thiện trọn vẹn Dự Án Thực Chiến 01!

Ở bài trước, chúng ta đã thấy Antigravity phân loại email kỳ diệu như thế nào. Nhưng nếu mỗi sáng bạn vẫn phải nhớ mở phần mềm lên, gõ lại câu lệnh đó thì mức độ tự động hóa mới chỉ đạt 50%.  
Đỉnh cao của tự động hóa là gì?  
Đó là **Bạn hoàn toàn không cần phải bận tâm nhớ đến nó**!  
Cứ đúng 8h00 sáng từ Thứ 2 đến Thứ 6 hàng tuần — khi bạn vừa bước vào văn phòng hoặc đang trên đường đi làm — trợ lý AI đã tự động thức dậy, tự quét hộp thư và chuẩn bị sẵn một bản điểm tin ngắn gọn chờ bạn duyệt!

Và 'phép màu' giúp bạn làm được điều đó chính là lệnh: **`/schedule`**!"

---

### [01:20 - 04:00] GIẢI MÃ LỆNH HẸN GIỜ `/schedule`: ĐƠN GIẢN VÀ DỄ DÙNG
`[Chuyển màn hình sang Antigravity Desktop]`  
`[Mở khung nhập lệnh, giải thích cú pháp bình dân]`

"Lệnh `/schedule` trong Antigravity là công cụ giúp bạn lên lịch cho AI chạy định kỳ theo thời gian:
* Cú pháp hẹn giờ chạy hàng ngày có cấu trúc như sau:
  `0 8 * * 1-5`  
  Đừng lo lắng, con số này rất dễ nhớ:
  * Số `0` là phút 0.
  * Số `8` là 8 giờ sáng.
  * `1-5` là từ Thứ Hai đến Thứ Sáu trong tuần (ngày đi làm của dân văn phòng).
* Bạn chỉ cần gõ vào khung chat một dòng lệnh duy nhất:

> `/schedule CronExpression="0 8 * * 1-5" IsDaemon=true Prompt="Hãy dùng Gmail MCP quét các email chưa đọc trong đêm qua, phân loại nhãn và tạo một bản tin tóm tắt 3 email khẩn cấp nhất gửi thông báo cho tôi."`

`[Nhấn phím Enter dứt khoát]`  
Hệ thống báo: *'Đã kích hoạt lịch trình tự động thành công!'*"

---

### [04:00 - 07:30] CƠ CHẾ HOẠT ĐỘNG: AI "THỨC DẬY" LÀM VIỆC NHƯ THẾ NÀO?
`[Chỉ chuột vào thẻ Task Scheduler trong bảng quản trị]`  
`[Mô tả trải nghiệm thực tế mỗi sáng]`

"Khi lịch trình này đã được kích hoạt, chuyện gì sẽ xảy ra vào 8h00 sáng mai?
1. **Đúng 8h00 sáng:** Antigravity sẽ tự động kích hoạt tiến trình ngầm (Daemon Task).
2. **Tự động quét hòm thư:** Nó vươn tay vào hòm thư Gmail, phát hiện có 15 email mới gửi đến đêm qua.
3. **Tự động dán nhãn:** Nó gắn nhãn đỏ cho email khiếu nại của khách hàng VIP và gắn nhãn xanh cho các hóa đơn tiền điện.
4. **Tự động xuất bản điểm tin sáng:**  
   `[Chỉ vào mẫu bản tin trên màn hình]`  
   Một thông báo trang trọng hiện lên ngay ngắn trên màn hình của bạn:  
   > ☀️ **[BẢN TIN ĐIỂM TIN SÁNG 8H00 - CHÚC BẠN MỘT NGÀY LÀM VIỆC HIỆU QUẢ!]**  
   > *Hôm nay bạn có 15 email mới, đã được phân loại gọn gàng. Có 2 việc khẩn cấp cần bạn lưu ý ngay:*  
   > *1. Email từ Giám đốc Nguyễn Văn An: Yêu cầu chuẩn bị số liệu dự toán trước 10h sáng.*  
   > *2. Email từ Khách hàng Đối tác ABC: Đề nghị xác nhận lịch họp ký kết vào 14h chiều.*  
   > *Các email còn lại là hóa đơn và tin tức đã được gom vào thư mục lưu trữ.*

Bạn thấy đấy: Thay vì ngập trong 15 bức thư dài dằng dặc, bạn chỉ mất đúng 15 giây đọc lướt là đã nắm trọn vẹn 100% công việc quan trọng nhất trong ngày!"

---

### [07:30 - 10:00] TỔNG KẾT DỰ ÁN 01 & DẪN SANG DỰ ÁN 02: KẾ TOÁN SỐ OCR
`[Quay lại màn hình camera, tươi cười đắc thắng]`

"Chúc mừng các bạn! Chúng ta đã xuất sắc hoàn thành **Dự Án Thực Chiến 01 — Trợ Lý Hộp Thư Tự Động**!  
Chỉ riêng dự án này đã có thể giúp bạn tiết kiệm ít nhất 5 đến 7 tiếng đồng hồ mỗi tuần.

Nhưng công việc văn phòng không chỉ có email.  
Có một 'cơn ác mộng' khác còn kinh hoàng hơn rất nhiều đối với các bạn làm hành chính, kế toán, hay nhân sự sau mỗi đợt công tác hoặc cuối tháng:  
*Đó là một túi nilon chứa đầy hóa đơn ăn uống, vé tàu xe, phiếu thu tiền taxi chụp vội bằng điện thoại... mờ mờ, nhăn nheo, và bạn phải ngồi căng mắt gõ tay từng con số vào bảng tính Excel!*

Làm thế nào để ném toàn bộ đống ảnh hóa đơn đó vào cho AI, và chỉ 1 phút sau nhận về một bảng tính Excel có sẵn công thức tính tổng, thuế VAT chuẩn chỉ từng xu?

Chào mừng các bạn đến với **Phần 10: ⭐ Thực Chiến 02 — Kế Toán Số: Quét Ảnh Hóa Đơn Tự Động Đổ Dữ Liệu Vào Excel**!  
Hãy bấm sang Bài 10.1 ngay bây giờ để cùng giải mã bí mật này nhé!"
