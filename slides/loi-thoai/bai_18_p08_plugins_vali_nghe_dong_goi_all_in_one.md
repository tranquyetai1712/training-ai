# KỊCH BẢN LỜI THOẠI BÀI HỌC 8.1
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 2:** Kho Vũ Khí 7 Trụ Cột Cho Dân Văn Phòng  
**Phần 8:** Trụ Cột 6 & 7 — Plugins & Sidecars: Vali Nghề & Trợ Lý Tàng Hình  
**Tên bài:** Bài 8.1: Plugins: Đóng gói toàn bộ Rules, Skills thành 1 bộ cài duy nhất qua plugin.json  
**Thời lượng dự kiến:** 08:00  
**Slide tương ứng:** `phan_08_tru_cot_plugins_sidecars.html` (Slide 1)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_08_tru_cot_plugins_sidecars.html` (Slide 17 và Slide 18).
* **Minh họa thư mục:** Mở thư mục Plugin `D:\Project\workflow\plugins\q-file-organizer` để chỉ rõ cấu trúc tệp tin thực tế.
* **Tông giọng:** Hào hứng, chuyên nghiệp, khơi gợi tư duy đóng gói sản phẩm và chia sẻ tài sản công nghệ trong đội ngũ.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD SCRIPT)

### [00:00 - 01:30] MỞ ĐẦU: BÀI TOÁN "CHIA SẺ VŨ KHÍ CHO ĐỒNG NGHIỆP"
`[Hiển thị Slide 1: Trụ Cột 6 — Plugins: Chiếc Vali Vũ Khí Số]`  
`[Tông giọng vui vẻ, gợi mở tình huống]`

"Chào mừng các bạn đến với **Phần 8: Trụ Cột 6 & 7 — Plugins & Sidecars**!

Sau khi học xong 5 trụ cột vừa qua: Bạn đã tự tay viết được Rules định dạng công văn, bạn biết nạp Skills đổi tên file, bạn biết cài Hooks chống xóa file và kết nối MCP đọc dữ liệu từ xa.  
Bây giờ, bạn mang toàn bộ sự tự hào này lên công ty, và đồng nghiệp trong phòng ban đều trầm trồ thán phục:  
*'Ôi hay quá! Bạn cài cho máy tính của mình với!'*

Lúc này, chẳng lẽ bạn lại phải ngồi cả buổi sáng: copy từng file `.md`, chỉ cho bạn ấy từng đường dẫn thư mục ẩn, cấu hình từng dòng file JSON? Quá mất thời gian và rất dễ bị lỗi!  
Làm thế nào để bạn có thể nén toàn bộ trí tuệ đó vào **đúng một thư mục duy nhất**, gửi qua Zalo hay USB cho đồng nghiệp, và họ chỉ cần bấm 1 click chuột là máy tính của họ có đầy đủ mọi tính năng siêu việt như máy tính của bạn?  
Đó chính là lý do vì sao chúng ta cần đến **Plugins — Chiếc vali đồ nghề All-in-One**!"

---

### [01:30 - 04:30] CẤU TRÚC GIẢI PHẪU CỦA MỘT PLUGIN: TẤM GIẤY KHAI SINH PLUGIN.JSON
`[Chuyển Slide 18: Giải Phẫu Cấu Trúc Plugin Chuẩn Mực]`  
`[Mở thư mục D:\Project\workflow\plugins\q-file-organizer trên màn hình thực tế]`

"Các bạn hãy nhìn vào màn hình của tôi:  
Đây là thư mục của một Plugin thực tế mang tên `q-file-organizer`. Hãy xem bên trong nó có những gì:
1. **Thành phần bắt buộc duy nhất — Tệp `plugin.json`:**  
   `[Mở file plugin.json lên xem]`  
   Đây chính là 'Tờ giấy khai sinh' của gói công cụ, chỉ gồm vài dòng cực kỳ ngắn gọn:
   ```json
   {
     "name": "q-file-organizer",
     "version": "1.1.0",
     "description": "Plugin tự động phân loại và đổi tên tệp tin thông minh dựa trên phân tích nội dung thực tế."
   }
   ```
2. **Các ngăn chứa vũ khí bên trong:**
   * Ngăn chứa `skills/`: Chứa các kỹ năng chuyên môn đóng gói sẵn.
   * Ngăn chứa `rules/`: Chứa nội quy văn phòng.
   * Ngăn chứa `hooks/`: Chứa trạm gác an ninh.
   * Ngăn chứa `mcp/`: Chứa các cổng kết nối dữ liệu.

Tất cả nằm gọn gàng trong một thư mục duy nhất! Bạn không cần phải phân tán các file đi khắp nơi nữa."

---

### [04:30 - 06:45] QUẢN LÝ PLUGIN DỄ DÀNG NHƯ BẬT TIỆN ÍCH TRÊN GOOGLE CHROME
`[Chuyển Slide 19: Bật / Tắt Tiện Ích Trong 1 Cú Click Chuột]`  
`[Rê chuột minh họa giao diện quản trị Plugin]`

"Cách thức sử dụng Plugin trong Antigravity dễ dàng hệt như việc bạn bật/tắt các tiện ích mở rộng (Extension) trên trình duyệt Google Chrome vậy:
* Hôm nay bạn cần dọn dẹp thư mục máy tính: Bạn chỉ cần gạt công tắc **BẬT** gói `q-file-organizer`. Ngay lập tức, toàn bộ các kỹ năng phân loại và đổi tên file sẽ sẵn sàng phục vụ bạn.
* Khi nào bạn không cần dùng đến: Bạn chỉ cần gạt công tắc **TẮT**. Toàn bộ các công cụ đó sẽ được giải phóng khỏi bộ nhớ, trả lại không gian thanh thoát cho máy tính của bạn.
* Một cú click chuột là cài đặt xong, không cần cài đặt lại từ đầu!"

---

### [06:45 - 08:00] TỔNG KẾT BÀI & CÂU DẪN SANG THỰC HÀNH BÀI 8.2
`[Quay lại màn hình camera, tươi cười rạng rỡ]`

"Thật là tuyệt vời đúng không các bạn? Plugins chính là cấp độ cao nhất của việc đóng gói và nhân bản tri thức tự động hóa trong doanh nghiệp.

Và để các bạn thấy được trọn vẹn sức mạnh của một Plugin hoàn chỉnh ngoài đời thực, ngay ở bài học tiếp theo — **Bài 8.2**, chúng ta sẽ cùng nhau kích hoạt Plugin `q-file-organizer`: Kết hợp cả 2 kỹ năng `phan-loai-file-tu-dong` và `doi-ten-file-tu-dong` để dọn sạch bóng một thư mục Downloads ngập rác trong vòng 1 phút!

Mời các bạn cùng bấm sang Bài 8.2 để thực chiến ngay bây giờ!"
