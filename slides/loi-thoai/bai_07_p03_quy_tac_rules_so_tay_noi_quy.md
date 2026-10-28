# KỊCH BẢN LỜI THOẠI BÀI HỌC 3.1
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 2:** Kho Vũ Khí 7 Trụ Cột Cho Dân Văn Phòng  
**Phần 3:** Trụ Cột 1 — Rules: Huấn Luyện AI Tuân Thủ Quy Chuẩn Văn Phòng  
**Tên bài:** Bài 3.1: Vì sao AI hay quên lời dặn? Sổ tay nội quy Rules cho dự án  
**Thời lượng dự kiến:** 08:00  
**Slide tương ứng:** `phan_03_tru_cot_rules.html` (Slide 1)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_03_tru_cot_rules.html` (Slide 1 và Slide 2).
* **Minh họa thư mục:** Mở sẵn thư mục `.gemini/config/rules/` trên File Explorer để sẵn sàng chỉ đường dẫn trực quan.
* **Tông giọng:** Vui vẻ, dí dỏm khi nói về tật "hay quên" của AI, sau đó chuyển sang tự tin khi giới thiệu giải pháp Rules.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD SCRIPT)

### [00:00 - 01:30] MỞ ĐẦU: CƠN ÁC MỘNG "NGÀY NÀO CŨNG PHẢI DẶN LẠI TỪ ĐẦU"
`[Hiển thị Slide 1: Trụ Cột 1 — Rules: Sổ Tay Nội Quy Dự Án]`  
`[Tông giọng hóm hỉnh, đồng cảm sâu sắc]`

"Chào mừng các bạn đến với **Khối 2: Kho Vũ Khí 7 Trụ Cột Cho Dân Văn Phòng**!  
Và chúng ta sẽ mở màn với vũ khí nền tảng số một: **Trụ Cột 1 — Rules Engine (Hệ Thống Quy Chuẩn & Nội Quy)**.

Để tôi đoán nhé: Có phải mỗi lần bạn mở ChatGPT hay bất kỳ công cụ AI nào lên, bạn đều cảm thấy vô cùng mệt mỏi vì cứ phải gõ đi gõ lại một điệp khúc quen thuộc:  
*'Nhớ trả lời bằng tiếng Việt nhé!'*  
*'Đừng viết dài dòng lan man nhé!'*  
*'Định dạng số tiền có dấu chấm phân cách hàng nghìn nhé!'*  
*'Viết theo phong cách trang trọng của công văn nhà nước nhé!'*

`[Nhấn mạnh]`  
Tại sao lại như vậy? Đó là vì các chatbot thông thường hoàn toàn **không có trí nhớ dài hạn**. Mỗi lần bạn tắt cửa sổ chat đi mở lại, nó trở về trạng thái 'mất trí nhớ tạm thời', giống như một nhân viên mới tinh bước vào công ty vào ngày đầu tiên và bạn lại phải cầm tay chỉ việc lại từ con số 0!  
Nhưng với Antigravity, bạn chỉ cần dặn **ĐÚNG MỘT LẦN DUY NHẤT** trong đời. Và công cụ giúp bạn làm được điều kỳ diệu đó chính là **Rules**!"

---

### [01:30 - 04:30] BẢN CHẤT CỦA RULES: CUỐN SỔ TAY NỘI QUY CÔNG TY
`[Chỉ chuột vào hình ảnh Cuốn Sổ Tay Nội Quy trên Slide 4]`  
`[Giải thích bản chất cực kỳ gần gũi với đời sống]`

"Vậy Rules thực chất là gì?  
Hãy hình dung Rules giống hệt như **Cuốn Sổ Tay Nội Quy Công Ty** được phát cho nhân viên mới vào ngày đầu tiên đi làm:
* Trong sổ tay ghi rõ: Giờ giấc làm việc thế nào, trang phục ra sao, văn phong viết email cho khách hàng phải lịch sự như thế nào.
* Nhân viên cầm cuốn sổ đó, đọc qua một lần và tự động khắc cốt ghi tâm trong suốt quá trình làm việc sau này.

Trong Antigravity:
* Bản chất của một file Rule **chỉ là một tệp văn bản bình thường** có đuôi mở rộng là `.md` (Markdown).
* Bạn viết vào đó bằng tiếng Việt hoàn toàn tự nhiên, không cần bất kỳ một dòng code lập trình nào.
* Và điều kỳ diệu là: **Mỗi khi bạn mở Antigravity lên hoặc bấm nút New Task, hệ thống sẽ tự động tải các file Rules này vào đầu não của AI trước khi nhận bất kỳ câu lệnh nào từ bạn!**  
Nhờ vậy, trợ lý AI luôn biết tự giác tuân thủ mọi nguyên tắc mà bạn không cần phải tốn công nhắc lại dù chỉ một lời!"

---

### [04:30 - 06:45] HAI TẦNG QUY TẮC THÔNG MINH: GLOBAL RULES & WORKSPACE RULES
`[Chuyển Slide 2: Phân Tầng Quy Tắc — Toàn Máy Tính vs Riêng Từng Dự Án]`  
`[Chỉ vào 2 tầng kiến trúc trên màn hình]`

"Để phục vụ linh hoạt cho công việc, Antigravity phân chia nội quy thành **2 cấp độ** cực kỳ thông minh:

#### 1. Cấp độ 1: Global Rules (Nội quy toàn máy tính)
* **Vị trí lưu:** Nằm tại thư mục cấu hình chung của bạn `~/.gemini/config/rules/`.
* **Phạm vi áp dụng:** Áp dụng cho **MỌI DỰ ÁN**, mọi lần bạn mở máy tính làm việc.
* **Ví dụ thực tế:** Những nguyên tắc bất di bất dịch của cá nhân bạn:  
  * *'Luôn xưng hô lịch sự, trả lời bằng tiếng Việt chuẩn ngữ pháp.'*  
  * *'Tuyệt đối không được xóa bất kỳ tệp tin nào trên máy tính khi chưa hỏi ý kiến tôi.'*

#### 2. Cấp độ 2: Workspace Rules (Nội quy riêng của từng dự án)
* **Vị trí lưu:** Nằm ngay bên trong thư mục dự án của bạn (thường là tệp `AGENTS.md` hoặc thư mục `.agents/rules/`).
* **Phạm vi áp dụng:** Chỉ áp dụng riêng cho thư mục công việc đó mà thôi.
* **Ví dụ thực tế:**  
  * Nếu bạn đang làm việc trong thư mục `Du_An_Bao_Cao_Tai_Chinh`: Bạn cài luật bắt buộc *'Mọi số tiền phải hiển thị đơn vị VNĐ và có dấu chấm phân cách (ví dụ: 10.000.000 VNĐ)'*.  
  * Nếu bạn chuyển sang thư mục `Du_An_Soan_Thao_Cong_Van`: Bạn cài luật bắt buộc *'Văn phong phải chuẩn thể thức Nghị định 30 của Chính phủ về văn bản hành chính'*.  
Khi bạn chuyển đổi giữa các dự án, AI sẽ tự động thích ứng với nội quy của dự án đó mà không hề bị nhầm lẫn!"

---

### [06:45 - 08:00] TỔNG KẾT BÀI & CÂU DẪN SANG THỰC HÀNH BÀI 3.2
`[Quay lại màn hình chính, nụ cười khuyến khích]`

"Như vậy là các bạn đã hiểu rõ nguyên lý: Vì sao Rules lại là chiếc chìa khóa vàng giúp AI không bao giờ quên bài và luôn tuân thủ chuẩn mực công sở của bạn.

Bây giờ, chúng ta sẽ bắt tay vào hành động thực tế!  
Ngay ở bài học tiếp theo — **Bài 3.2**, tôi sẽ cùng các bạn tự tay viết một tệp Rule hoàn chỉnh bằng tiếng Việt: Huấn luyện trợ lý AI luôn tự động định dạng số tiền VNĐ và viết hoa danh xưng chuẩn công văn hành chính.

Hãy sẵn sàng mở ứng dụng Antigravity Desktop, và chúng ta cùng thực hành ngay tại Bài 3.2!"
