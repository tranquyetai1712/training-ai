# KỊCH BẢN LỜI THOẠI BÀI HỌC 9.1
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 3:** Phòng Thí Nghiệm Thực Chiến Đỉnh Cao  
**Phần 9:** ⭐ Thực Chiến 01 — Trợ Lý Hộp Thư: Tự Động Phân Loại Gmail & Báo Cáo Slack Theo Phòng Ban  
**Tên bài:** Bài 9.1: Thực hành: Trợ lý AI đọc hiểu 10 email mẫu, gắn nhãn phòng ban trên Gmail và báo cáo tóm tắt sang Slack  
**Thời lượng dự kiến:** 10:00 (Video Preview - Mở xem thử miễn phí)  
**Slide tương ứng:** `phan_09_thuc_chien_email.html` (Slide 1)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_09_thuc_chien_email.html` (Slide 1).
* **Dự án & Plugin sẵn sàng:** Mở thư mục `Demo` trên Antigravity Desktop — nơi đã cài sẵn Plugin **`q-email`** (gồm kỹ năng `phan-loai-gan-nhan-email` và 2 file quy tắc `quy-tac-gan-nhan.md`, `quy-chuan-slack-notification.md`).
* **Dữ liệu Demo có sẵn:** Bộ **10 email mẫu** trong `Demo/thuc-chien-01-phan-loai-email/10_email_mau` đã được gửi sẵn vào hộp thư Gmail Demo (chưa có nhãn `AI_DaPhanLoai`).
* **Màn hình chuyển đổi:** Antigravity Desktop • Trình duyệt Gmail • Ứng dụng/Tab Slack (có các kênh `#urgent`, `#sales`, `#finance`, `#hr`, `#email-notifications`).
* **Tông giọng:** Thực chiến, tự nhiên, hoàn toàn dùng ngôn ngữ đời thường cho dân văn phòng — không đọc tên hàm code hay cú pháp kỹ thuật.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD SCRIPT)

### [00:00 - 01:30] MỞ ĐẦU: BÀI TOÁN HỘP THƯ ĐẾN & GIỚI THIỆU BỘ 10 EMAIL MẪU
`[Hiển thị Slide 1: Thực Chiến 1 — Phân Loại Gmail & Báo Cáo Slack]`  
`[Mở tab Gmail hiển thị 10 email mẫu chưa được phân loại]`

"Chào mừng các bạn đến với **Khối 3: Phòng Thí Nghiệm Thực Chiến Đỉnh Cao** — và mở màn với **Dự Án Thực Chiến 01: Trợ Lý Hộp Thư Tự Động**!

Mỗi sáng mở máy tính lúc 8 giờ, nhìn hộp thư Gmail trộn lẫn đủ thứ: từ khách hàng báo sự cố giao nhầm hàng, đối tác hỏi báo giá, phòng kế toán nhận hóa đơn điện tử, ứng viên gửi CV xin việc, cho đến hàng loạt thư quảng cáo... việc đọc tay và chuyển tiếp cho từng phòng ban ngốn mất cả tiếng đồng hồ.

Bộ lọc từ khóa truyền thống của Gmail thì rất máy móc: một email khách VIP phản ánh chậm bàn giao nhưng **không viết chữ 'khẩn cấp'** sẽ dễ bị bỏ sót; ngược lại, thư quảng cáo học bổng giật tít **'KHẨN CẤP'** thì lại báo nhầm!

Hôm nay, tôi đã chuẩn bị sẵn **bộ 10 email mẫu** y hệt tình huống công sở thật trên màn hình Gmail này. Chúng ta sẽ cho trợ lý AI đọc hiểu toàn bộ, phân loại về đúng phòng ban và tự động nhắn tin tóm tắt sang Slack luôn nhé!"

---

### [01:30 - 04:00] BƯỚC 1: RA LỆNH 1 CÂU NGẮN GỌN NHỜ BỘ QUY TẮC ĐÓNG GÓI SẴN
`[Chuyển màn hình sang Antigravity Desktop đang mở thư mục Demo]`  
`[Chỉ nhanh vào Plugin q-email đã trang bị sẵn, rồi bấm + New Conversation]`

"Điểm sướng nhất khi bạn đã áp dụng **Skills, Rules và Plugins** từ Khối 2 là gì?  
Là bạn **không cần phải ngồi gõ lại một câu lệnh dài dằng dặc 20 dòng** để dặn đi dặn lại từng phòng ban nữa!

Trong thư mục `Demo` này đã có sẵn gói tiện ích **`q-email`** chứa kỹ năng phân loại email cùng 2 bộ nội quy rõ ràng:
* **Nội quy 1 — Chia đúng 8 nhóm nhãn phòng ban** (từ *Khẩn cấp*, *Kinh doanh Báo giá / Hợp tác*, *Kế toán Hóa đơn*, *Công nợ*, *Nhân sự Tuyển dụng*, *Hành chính* cho tới *Quảng cáo Spam*) cộng thêm một nhãn đánh dấu **`AI_DaPhanLoai`** để lần sau AI không quét trùng lại thư cũ.
* **Nội quy 2 — Báo cáo đúng kênh Slack:** Thư khẩn cấp vào `#urgent`, báo giá hợp tác vào `#sales`, hóa đơn công nợ vào `#finance`, hồ sơ ứng viên vào `#hr`, thông báo nội bộ vào `#email-notifications` — còn thư quảng cáo thì **tuyệt đối không gửi lên Slack** cho đỡ làm phiền cả công ty!

Vì mọi luật chơi đã được lưu sẵn như vậy rồi, nên ở khung trò chuyện bạn chỉ cần gõ đúng **1 câu tiếng Việt tự nhiên** thế này thôi:

> *'Hãy kiểm tra tối đa 20 email mới chưa được phân loại trong hộp thư Gmail của tôi, tự động đọc hiểu để gắn nhãn theo từng phòng ban và gửi tóm tắt 2 câu sang đúng kênh Slack tương ứng giúp tôi nhé.'*

`[Nhấn phím Enter]`  
Bây giờ hãy xem trợ lý AI thực thi liên hoàn toàn bộ quy trình này!"

---

### [04:00 - 07:15] BƯỚC 2: XEM AI ĐỌC HIỂU, GẮN NHÃN CHỐNG TRÙNG LẶP & ĐIỀU PHỐI SLACK
`[Chỉ chuột theo tiến trình làm việc của AI trên Antigravity]`  
`[Giải thích bằng ngôn ngữ bình dân, không đọc thuật ngữ code]`

"Các bạn quan sát quy trình làm việc cực kỳ bài bản của AI trên màn hình:
1. **Lọc đúng những thư chưa từng xử lý:**  
   AI tự động bỏ qua những email đã có nhãn đánh dấu `AI_DaPhanLoai` trước đó, chỉ tập trung vào 10 email mẫu mới đến nên không bao giờ gửi thông báo trùng lặp.
2. **Đọc hiểu ngữ cảnh thật và tóm tắt gọn trong 2 câu:**  
   Nó đọc tiêu đề, người gửi, nội dung chính lẫn danh sách file đính kèm, rồi chắt lọc thành một đoạn tóm tắt đúng 2 câu nổi bật việc cần làm:
   * Bức thư báo giao nhầm lô hàng và bức thư chị Lan Anh đối tác VIP phản ánh lỗi đăng nhập (dù không hề có chữ 'khẩn cấp') ➔ AI hiểu ngay mức độ nghiêm trọng và xếp vào **`KhanCap`**.
   * Thư hỏi mua 5 máy in ➔ **`KinhDoanh/BaoGia`**; thư mời hợp tác B2B ➔ **`KinhDoanh/HopTac`**.
   * Hóa đơn điện tử Viettel ➔ **`KeToan/HoaDon`**; thư nhắc tiền thuê văn phòng ➔ **`CongNo/ThanhToan`**.
   * Email nộp CV ứng tuyển ➔ **`NhanSu/Tuyendung`**; thông báo gia hạn tên miền ➔ **`HanhChinh/ThongBao`**.
   * Đặc biệt, bức thư quảng cáo học bổng cố tình giật tít chữ *'KHẨN CẤP'* ➔ AI đọc ruột bên trong là biết ngay 'bẫy quảng cáo', xếp thẳng vào **`QuangCao_Spam`**!
3. **Tự tạo nhãn mới trên Gmail & gắn song song 2 lớp nhãn:**  
   Kiểm tra thấy trên Gmail chưa có nhãn nào trong bộ 8 nhãn trên, AI tự động tạo mới hết rồi gắn đồng thời **nhãn phòng ban** và **nhãn kiểm soát `AI_DaPhanLoai`** vào từng bức thư.
4. **Phân luồng tin nhắn thông minh sang từng kênh Slack:**  
   Sau khi gắn nhãn xong, AI tự động gửi bản tóm tắt 2 câu kèm đường link bấm vào là mở thẳng email lên đúng từng kênh Slack của các phòng ban — riêng 2 email **`QuangCao_Spam`** được lọc sạch ngay tại cổng, **không hề bắn sang Slack**!
5. **Xuất bảng tổng kết nghiệm thu:**  
   Cuối cùng, một bảng tổng hợp gọn gàng gồm tiêu đề, người gửi, nhãn đã gắn và trạng thái gửi Slack hiện ra ngay trên màn hình để bạn kiểm soát toàn bộ."

---

### [07:15 - 09:15] BƯỚC 3: KIỂM CHỨNG THỰC TẾ TRÊN GMAIL & SLACK
`[Chuyển sang tab Gmail bấm F5, sau đó chuyển sang cửa sổ Slack lướt qua các kênh]`  
`[Tông giọng phấn khích]`

"Bây giờ chúng ta đi nghiệm thu thực tế từng nơi nhé!
* **Đầu tiên trên Gmail (`Bấm F5`):** Nhìn sang cột bên trái, toàn bộ các nhãn phòng ban từ `KhanCap`, `KinhDoanh`, `KeToan`, `CongNo`, `NhanSu`, `HanhChinh` cùng nhãn kiểm soát `AI_DaPhanLoai` đã được tạo sẵn và gắn chuẩn xác cho cả 10 email mẫu!
* **Tiếp theo sang Slack:**
  * Mở kênh **`#urgent`**: Thấy ngay 2 cảnh báo đỏ nổi bật báo sự cố giao nhầm hàng và khiếu nại từ khách VIP kèm tóm tắt 2 câu và link mở thẳng thư gốc.
  * Mở kênh **`#sales`**: Bộ phận kinh doanh đã nhận sẵn tin báo giá 5 máy in và lời mời hợp tác B2B.
  * Mở kênh **`#finance`**: Kế toán đã có ngay tin báo hóa đơn Viettel và lịch nhắc tiền thuê văn phòng.
  * Mở kênh **`#hr`**: Nhân sự nhận ngay thông tin ứng viên nộp CV.
  * Và tuyệt vời nhất là cả Slack hoàn toàn sạch bóng 2 thư quảng cáo khuyến mãi!"

---

### [09:15 - 10:00] TỔNG KẾT BÀI & CÂU DẪN SANG BÀI 9.2
`[Quay lại màn hình camera, nụ cười rạng rỡ]`

"Bạn thấy sức mạnh khi kết hợp bộ quy tắc có sẵn với trợ lý AI chưa? Chỉ 1 câu tiếng Việt ngắn gọn, toàn bộ hộp thư đã tự phân về đúng phòng ban trên Gmail lẫn Slack trong tích tắc!

Nhưng làm sao để bạn **không cần phải tự mở Antigravity lên gõ câu lệnh này mỗi sáng** nữa?  
Ở **Bài 9.2** ngay sau đây, chúng ta sẽ đưa quy trình vừa rồi lên **`Automations`** để đúng 8h00 sáng mỗi ngày, AI tự thức dậy dọn hộp thư, báo Slack và tóm tắt việc gấp cho bạn trước khi bạn bước vào bàn làm việc!

Mời bạn bấm sang **Bài 9.2** ngay bây giờ!"
