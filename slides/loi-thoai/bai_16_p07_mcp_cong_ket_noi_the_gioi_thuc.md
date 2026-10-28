# KỊCH BẢN LỜI THOẠI BÀI HỌC 7.1
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 2:** Kho Vũ Khí 7 Trụ Cột Cho Dân Văn Phòng  
**Phần 7:** Trụ Cột 5 — MCP: Cổng Kết Nối Đưa Dữ Liệu Công Việc Thực Tế Vào AI  
**Tên bài:** Bài 7.1: MCP là gì? Mở rộng giác quan kết nối Drive, Gmail, Bảng tính và Thư mục máy  
**Thời lượng dự kiến:** 08:00  
**Slide tương ứng:** `phan_07_tru_cot_mcp.html` (Slide 1)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_07_tru_cot_mcp.html` (Slide 15 và Slide 16).
* **Hình ảnh minh họa:** Chiếc cổng cắm USB đa năng kết nối máy tính với các thiết bị ngoại vi (Gmail, Drive, Slack, Cơ sở dữ liệu).
* **Tông giọng:** Mở mang, hào hứng, giải thích một khái niệm công nghệ đỉnh cao bằng lăng kính đời thường dễ hiểu nhất.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD SCRIPT)

### [00:00 - 01:30] MỞ ĐẦU: NỖI KHỔ CỦA CON AI "BỊ NHỐT TRONG PHÒNG KÍN"
`[Hiển thị Slide 1: Trụ Cột 5 — MCP: Cổng Kết Nối Vạn Năng]`  
`[Tông giọng đồng cảm, gợi mở tình huống]`

"Chào mừng các bạn đến với **Phần 7: Trụ Cột 5 — Model Context Protocol (viết tắt là MCP)**!

Các bạn thân mến, từ trước đến nay, khi dùng các công cụ AI, bạn có từng cảm thấy bức bối thế này không:  
AI thì cực kỳ thông minh, nhưng nó lại giống như một **thiên tài bị nhốt trong một căn phòng kín không có cửa sổ**:
* Bạn muốn nó kiểm tra email giúp bạn, nó bảo: *'Tôi không thể truy cập vào hòm thư Gmail của bạn được'*.
* Bạn muốn nó lấy số liệu từ bảng tính online trên Google Drive, nó bảo: *'Tôi không có quyền mở đường link Drive này'*.
* Bạn muốn nó gửi một thông báo tóm tắt vào kênh chat Slack của phòng ban, nó bảo: *'Tôi chỉ là một mô hình ngôn ngữ, bạn hãy tự copy chữ này dán vào Zalo nhé'*.

Rốt cuộc, AI chỉ biết 'ngồi một chỗ', còn bạn thì cứ phải làm chân chạy vặt: vừa tải file xuống, vừa copy dán ngược dán xuôi.  
Và đó chính là lý do vì sao một cuộc cách mạng mang tên **MCP** ra đời để phá tan bức tường ngăn cách đó!"

---

### [01:30 - 04:30] ẨN DỤ ĐẮT GIÁ: CỔNG CẮM USB VẠN NĂNG CHO BỘ NÃO AI
`[Chỉ chuột vào hình ảnh Cổng USB Chuẩn Hóa trên Slide 15]`  
`[Giải thích bản chất công nghệ bằng hình ảnh đời thường]`

"MCP thực chất là gì? Đừng để những từ ngữ tiếng Anh dài dòng làm bạn bối rối!  
Hãy hình dung MCP giống hệt như một chiếc **Cổng cắm USB vạn năng (Universal Port)**:
* Chiếc máy tính xách tay của bạn: Khi bạn cắm chuột máy tính vào cổng USB, máy tính có thêm bàn tay để rê chuột; khi bạn cắm Webcam vào, máy tính có thêm đôi mắt để nhìn; khi bạn cắm loa vào, máy tính có thêm đôi tai và giọng nói.
* Với bộ não của Trợ lý AI cũng vậy:
  * Khi bạn 'cắm' **Cổng Gmail MCP** vào: Trợ lý AI lập tức có khả năng mở hòm thư Gmail ra đọc, lọc thư và dán nhãn tự động!
  * Khi bạn 'cắm' **Cổng Google Drive MCP** vào: Nó tự động tải tài liệu từ trên đám mây về máy tính để xử lý!
  * Khi bạn 'cắm' **Cổng Slack MCP** vào: Nó tự tay soạn và gửi tin nhắn báo cáo trực tiếp vào nhóm chat của công ty bạn!

Tất cả các dịch vụ phần mềm trên thế giới hiện nay đều đang cùng nhau áp dụng chung một chuẩn kết nối duy nhất mang tên MCP này. Nhờ đó, Antigravity có thể kết nối với hầu như mọi công cụ làm việc quen thuộc mà bạn đang dùng hàng ngày!"

---

### [04:30 - 06:45] TỆP CẤU HÌNH MCP_CONFIG.JSON: KẾT NỐI CHỈ TRONG 1 PHÚT
`[Chuyển Slide 16: Cấu Trúc Kết Nối MCP — Tệp mcp_config.json]`  
`[Rê chuột chỉ vào cấu trúc tệp JSON đơn giản]`

"Để kết nối một công cụ bên ngoài vào Antigravity, chúng ta chỉ cần một tệp cấu hình duy nhất mang tên `mcp_config.json` nằm tại thư mục `.gemini/config/mcp_config.json`:
* Trong tệp này, bạn chỉ cần khai báo 3 thông tin ngắn gọn:
  1. Tên công cụ bạn muốn kết nối (ví dụ: `gmail`, `slack`, `filesystem`).
  2. Đường dẫn kết nối.
  3. Quyền hạn mà bạn cho phép AI sử dụng.
* Khi Antigravity khởi động, nó sẽ tự động nhận diện các 'cổng cắm' này và cấp thêm các công cụ tương ứng cho trợ lý AI. Bạn hoàn toàn không cần phải viết một dòng code kết nối API phức tạp nào cả!"

---

### [06:45 - 08:00] TỔNG KẾT BÀI & CÂU DẪN SANG THỰC HÀNH BÀI 7.2
`[Quay lại màn hình camera, ánh mắt đầy phấn khởi]`

"Như vậy là các bạn đã hiểu: MCP chính là đôi mắt và đôi bàn tay giúp AI vươn ra thế giới phần mềm bên ngoài để giải phóng toàn diện sức lao động cho bạn.

Ngay ở bài học tiếp theo — **Bài 7.2**, chúng ta sẽ cùng nhau thực hành kết nối Antigravity với một cổng MCP Thư mục hồ sơ lưu trữ: Giúp trợ lý AI tự động truy cập vào kho dữ liệu ngoài, tìm kiếm hợp đồng và đối chiếu số liệu chỉ trong tích tắc!

Mời các bạn cùng bấm sang Bài 7.2 để bắt đầu trải nghiệm nhé!"
