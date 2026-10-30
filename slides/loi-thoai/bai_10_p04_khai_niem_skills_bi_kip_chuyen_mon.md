# KỊCH BẢN LỜI THOẠI BÀI HỌC 4.1
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 2:** Kho Vũ Khí 7 Trụ Cột Cho Dân Văn Phòng  
**Phần 4:** Trụ Cột 2 — Skills: Trang Bị Thêm "Bí Kíp Chuyên Môn" Trong Vài Giây  
**Tên bài:** Bài 4.1: Khái niệm Skills - Tải thêm kỹ năng chuyên môn không lo đầy bộ nhớ  
**Thời lượng dự kiến:** 03:30 (Chuẩn Udemy Micro-Learning • Modular Skill Engine)  
**Slide tương ứng:** `phan_04_tru_cot_skills.html` (Slide 1)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_04_tru_cot_skills.html` (Slide 1: Trụ Cột 2 — Skills: Bí Kíp Chuyên Môn Đóng Gói).
* **Tông giọng:** Sôi nổi, gợi mở, giải thích rành mạch sự khác biệt giữa "Nội quy" và "Cẩm nang chuyên môn".

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD LEAN SCRIPT)

### [00:00 - 00:40] PHÂN BIỆT RÕ RÀNG GIỮA "NỘI QUY" VÀ "BÍ KÍP NGHỀ"
`[Slide 1: Trụ Cột 2 — Skills: Bí Kíp Chuyên Môn Đóng Gói]`  
`[Tông giọng gợi mở, khơi gợi câu hỏi]`

"Chào mừng bạn đến với **Phần 4: Trụ Cột 2 — Skills (Kỹ Năng Nghiệp Vụ Chuyên Biệt)**!

Ở phần trước, chúng ta đã biến AI thành một nhân viên chuẩn mực nhờ cuốn sổ tay Rules. **Thế nhưng lúc này,** chắc hẳn bạn sẽ băn khoăn: *Nếu tôi muốn AI biết làm việc chuyên sâu — như đọc ảnh chụp hóa đơn mờ, rà soát hợp đồng pháp lý, hay dọn dẹp hàng trăm file lộn xộn — thì có nên nhét hết vào Rules không?*

**Câu trả lời dứt khoát là: Tuyệt đối không!**

**Bởi vì trên thực tế,** nếu bạn nhét hàng chục quy trình dài dòng vào Rules, bộ não của AI sẽ bị bội thực token ngay khi vừa khởi động. Bạn chưa kịp giao việc gì thì bộ nhớ ngắn hạn của nó đã quá tải rồi!

**Và để giải quyết triệt để vấn đề này,** Google Antigravity mang đến cho chúng ta vũ khí số hai: **Skills — Tải kỹ năng chuyên môn theo nhu cầu!**"

---

### [00:40 - 01:50] ẨN DỤ DỄ HIỂU: CUỐN SÁCH KỸ THUẬT TRÊN GIÁ SÁCH & CƠ CHẾ LAZY LOADING
`[Chỉ hình ảnh Thẻ BẢN CHẤT & TIẾT KIỆM BỘ NHỚ trên Slide 1]`

"**Vậy cơ chế hoạt động của Skills khác với Rules như thế nào?**

Bạn hãy hình dung trong văn phòng làm việc có một **Giá sách nghiệp vụ**:
* Trên giá có sẵn cuốn: *'Cẩm nang Đổi tên file'*, cuốn *'Sổ tay Kiểm toán nội bộ'*, và cuốn *'Bí kíp Vẽ biểu đồ báo cáo'*.
* Hàng ngày, nhân viên của bạn **hoàn toàn không cần phải học thuộc lòng** toàn bộ số sách vở đó.
* **Chỉ khi nào** bạn giao nhiệm vụ: *'Dọn dẹp lại thư mục hồ sơ cho ngăn nắp'*, nhân viên mới bước tới giá sách, rút đúng cuốn *'Cẩm nang Đổi tên file'* ra đọc, làm xong việc thì cất sách về vị trí cũ!

**Trong công nghệ,** cơ chế thông minh này được gọi là **Lazy Loading — Nạp kỹ năng khi cần**:
* Khi bạn không dùng đến, Skill nằm yên tĩnh trên ổ cứng máy tính, hoàn toàn không tốn dù chỉ một token bộ nhớ của AI.
* **Và điều kỳ diệu ở đây là:** Chỉ khi bạn gọi tên kỹ năng hoặc yêu cầu một công việc liên quan, Antigravity mới kích hoạt cuốn cẩm nang đó lên để xử lý nhiệm vụ. **Kết quả là,** bạn có thể cài đặt hàng trăm kỹ năng khác nhau mà máy tính vẫn chạy nhẹ tênh, cực kỳ thanh thoát!"

---

### [01:50 - 02:50] BÓC TÁCH CẤU TRÚC BÊN TRONG CỦA MỘT SKILL
`[Chỉ Thẻ CẤU TRÚC SKILL trên Slide 1: Tệp SKILL.md]`

"**Cấu tạo bên trong của một Skill thực chất gồm những gì?**

Nói tóm lại, nó vô cùng đơn giản và trực quan:
* Mỗi Skill là một thư mục mang tên kỹ năng đó theo dạng gạch nối chữ thường, ví dụ: `doi-ten-file-tu-dong`.
* Bên trong thư mục, **thành phần bắt buộc duy nhất** là tệp văn bản `SKILL.md`.  
  Tệp này gồm hai phần cốt lõi:
  1. **Thẻ thông tin trên cùng (Frontmatter):** Khai báo tên kỹ năng (`name`) và mô tả ngắn gọn (`description`) giúp AI tự nhận biết khi nào nên kích hoạt kỹ năng này.
  2. **Quy trình thao tác chuẩn (SOP) bên dưới:** Hướng dẫn chi tiết từng bước 1, 2, 3, 4 bằng tiếng Việt rõ ràng để AI làm theo một cách kỷ luật.
* **Ngoài ra,** nếu kỹ năng đó cần tính toán phức tạp hoặc thao tác file chuyên sâu, nó có thể đi kèm một thư mục phụ mang tên `scripts/` chứa các kịch bản chạy ngầm tự động."

---

### [02:50 - 03:30] TỔNG KẾT BÀI & CẦU NỐI SANG THỰC HÀNH BÀI 4.2
`[Chỉ dòng Footer Bar trên Slide 1: Quy tắc vàng SKILL.md]`

"**Trước khi kết thúc bài học,** bạn hãy ghi nhớ một quy tắc kỹ thuật sống còn:  
Tên tệp cẩm nang bên trong thư mục **bắt buộc phải viết hoa toàn bộ: `SKILL.md`**. Nếu bạn viết thường, Antigravity sẽ không thể nhận diện được kỹ năng đó!

**Nói tóm lại,** Skills chính là những 'tuyệt kỹ võ công' đóng gói sẵn, giúp AI mở rộng năng lực không giới hạn mà không làm nghẽn bộ nhớ.

**Và để kiểm chứng ngay sức mạnh này trong thực tế công sở,** mời bạn cùng tôi bước sang **Bài 4.2**: Chúng ta sẽ kích hoạt trực tiếp Skill `doi-ten-file-tu-dong` để chứng kiến AI tự đọc nội dung hàng loạt tài liệu lộn xộn và chuẩn hóa tên file trong chớp mắt!

Mời bạn cùng bấm sang Bài 4.2 ngay bây giờ!"
