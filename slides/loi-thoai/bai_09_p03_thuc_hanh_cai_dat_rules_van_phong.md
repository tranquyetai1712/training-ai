# KỊCH BẢN LỜI THOẠI BÀI HỌC 3.3
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 2:** Kho Vũ Khí 7 Trụ Cột Cho Dân Văn Phòng  
**Phần 3:** Trụ Cột 1 — Rules: Huấn Luyện AI Tuân Thủ Quy Chuẩn Văn Phòng  
**Tên bài:** Bài 3.3: Thực hành: Phối hợp AGENTS.md và rules/xx.md chuẩn hóa bảng kê chi phí từ file thô  
**Thời lượng dự kiến:** 04:30 (Chuẩn Udemy Micro-Learning • Hands-on Walkthrough)  
**Slide tương ứng:** `phan_03_tru_cot_rules.html` (Slide 3)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_03_tru_cot_rules.html` (Slide 3: Thực Hành: Phối Hợp AGENTS.md & rules/xx.md Xử Lý File Bảng Kê Chuẩn Chỉ).
* **Tài nguyên mẫu có sẵn:** Mở thư mục workspace độc lập `slides/Demo/chi-phi-cong-tac-tho/` trên Antigravity Desktop.
  * Đã chuẩn bị sẵn file thô: `chi_phi_cong_tac_tho.txt`
  * Đã chuẩn bị sẵn Hiến pháp: `AGENTS.md`
  * Đã chuẩn bị sẵn Luật chuyên ngành: `.agents/rules/dinh_dang_tien_te_ngay_thang.md`
* **Tông giọng:** Nhiệt tình, thực chiến, dẫn dắt từng thao tác trực quan để học viên thấy rõ sự phối hợp hoàn hảo trong một workspace chuẩn Antigravity.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD LEAN SCRIPT)

### [00:00 - 00:35] MỤC TIÊU THỰC HÀNH: PHỐI HỢP AGENTS.MD VÀ RULES/XX.MD TRÊN TỆP DỮ LIỆU THỰC TẾ
`[Slide 3: Thực Hành: Phối Hợp AGENTS.md & rules/xx.md Xử Lý File Bảng Kê Chuẩn Chỉ]`  
`[Tông giọng hào hứng, thực chiến]`

"Chào mừng bạn đến với Bài 3.3 — bài thực hành khép lại Trụ Cột 1 về Rules!

Nếu chỉ gõ prompt trong ô chat thì chatbot thông thường cũng tự đoán được. **Thế nhưng sức mạnh độc bản của Antigravity là khả năng tự động đọc file và thực thi nội quy trực tiếp trên ổ cứng máy tính!**

Trong bài học này, chúng ta sẽ không mất thời gian ngồi gõ dữ liệu thô. Thay vào đó, tôi đã chuẩn bị sẵn một không gian làm việc mẫu độc lập, nơi bạn sẽ thấy rõ sự kết hợp hoàn hảo giữa **Bản Hiến Pháp chung `AGENTS.md`** và **Luật chuyên ngành `.agents/rules/dinh_dang_tien_te_ngay_thang.md`** để tự động xử lý một file chi phí công tác lộn xộn thành bảng kê chuẩn 100% phong cách công sở.

Mời bạn mở Antigravity Desktop lên và cùng bắt tay vào làm với tôi ngay nhé!"

---

### [00:35 - 01:50] KHÁM PHÁ WORKSPACE MẪU CHI-PHI-CONG-TAC-THO & CẤU TRÚC CHUẨN GOOGLE
`[Chuyển màn hình sang Antigravity Desktop]`  
`[Mở thư mục slides/Demo/chi-phi-cong-tac-tho/ trên File Explorer]`

"Để bài học diễn ra mạch lạc và không làm bạn mất công tạo file, trong thư mục cha `slides/Demo/`, tôi đã tạo riêng một thư mục dự án mang tên: `chi-phi-cong-tac-tho/`.

**Vì sao phải tách riêng như thế này?**  
Bởi vì sau này khóa học của chúng ta sẽ có rất nhiều bài thực hành khác nhau. Việc gom từng bài vào một thư mục con riêng biệt giúp từng workspace hoàn toàn độc lập, không bao giờ bị xung đột quy tắc với nhau!

Bây giờ bạn nhìn vào cấu trúc bên trong của `chi-phi-cong-tac-tho/`, đây chính là cấu trúc chuẩn chỉ nhất theo tài liệu Google:

1. **File dữ liệu thô (`chi_phi_cong_tac_tho.txt`):**  
   Mở ra bạn sẽ thấy 3 dòng ghi chép cực kỳ lộn xộn:
   ```text
   1. ve may bay cho nguyen van an: 3500000 vao ngay 10/24/2026
   2. an trua tiep khach cua tran thi mai: 1250000 vao ngay 2026-10-25
   3. khach san cua le hoang nam: 2400000 vao ngay 26/10/2026
   ```
   Tên viết thường, tiền thiếu dấu chấm, ngày tháng lẫn lộn kiểu Mỹ `10/24/2026` và ISO `2026-10-25`.

2. **Bản Hiến pháp dự án (`AGENTS.md` đặt tại thư mục gốc):**  
   Quy định ranh giới an toàn tối cao: *'Không sửa đè lên file thô gốc chi_phi_cong_tac_tho.txt, luôn xuất kết quả ra file mới: bang_ke_chi_phi_chuan.md.'*

3. **Luật chuyên ngành (`.agents/rules/dinh_dang_tien_te_ngay_thang.md`):**  
   Nằm trong thư mục chuẩn `.agents/rules/` với khối khai báo YAML chuẩn Google:
   ```yaml
   ---
   trigger: glob
   globs: "*.txt, *.csv"
   description: "Quy chuẩn định dạng tiền tệ VNĐ và ngày tháng Việt Nam"
   ---
   ```
   Bên dưới quy định 3 điều luật: Tiền tệ bắt buộc có dấu chấm và đuôi 'VNĐ', Ngày tháng chuẩn DD/MM/YYYY, Họ tên viết hoa đầy đủ."

---

### [01:50 - 02:40] CẢNH BÁO QUÉT PHẲNG (FLAT DIRECTORY SCANNING) CHUẨN GOOGLE
`[Quay lại Slide 3, chỉ chuột vào phần lưu ý kỹ thuật]`  
`[Tông giọng cảnh báo chuyên gia]`

"Trước khi bấm nút kiểm chứng, bạn hãy ghi nhớ **Quy tắc quét phẳng (Flat Directory Scanning)** từ tài liệu chính thức của Google:

* Tệp `AGENTS.md` bắt buộc phải nằm ngay ở tầng ngoài cùng của workspace dự án.
* Các file luật chuyên ngành phải nằm trực tiếp bên trong thư mục `.agents/rules/` (như `.agents/rules/dinh_dang_tien_te_ngay_thang.md`), tuyệt đối không tạo thư mục con lồng nhau như `.agents/rules/ke_toan/tien_te.md` vì Antigravity sẽ bỏ qua không quét đến.
* Và luôn duy trì dung lượng file súc tích dưới 24KB để AI đọc hiểu trong chớp mắt."

---

### [02:40 - 03:50] KIỂM CHỨNG THỰC TẾ: RA LỆNH 1 DÒNG ➔ AI TỰ KÍCH HOẠT RULE & XUẤT FILE MỚI CHUẨN ĐÉT
`[Mở lại Antigravity Desktop trong workspace chi-phi-cong-tac-tho, bấm nút New Task]`  
`[Tông giọng hào hứng, chuẩn bị đón chờ kết quả]`

"**Và bây giờ là khoảnh khắc kỳ diệu nhất:** Chúng ta kiểm chứng xem hệ sinh thái Rules vận hành ra sao!

1. Trong thư mục dự án `chi-phi-cong-tac-tho/`, bạn bấm nút **New Task** mở một phiên làm việc mới toanh.
2. Gõ đúng một câu lệnh ngắn gọn duy nhất, không cần nhắc lại bất kỳ quy tắc nào:
   > *'Hãy xử lý file `chi_phi_cong_tac_tho.txt` giúp tôi.'*
3. Nhấn phím `Enter` và cùng tôi quan sát màn hình!

`[Chỉ chuột vào màn hình Antigravity đang chạy]`  
**Bạn nhìn xem! Đây chính là phép màu của Trụ Cột Rules:**
* AI nhận diện bạn đang xử lý file có đuôi `.txt` ➔ Cơ chế `trigger: glob` lập tức kích hoạt file `.agents/rules/dinh_dang_tien_te_ngay_thang.md`!
* Đồng thời, AI đọc `AGENTS.md` và hiểu rằng không được sửa vào file gốc, nên ngay lập tức một file mới tinh mang tên `bang_ke_chi_phi_chuan.md` được sinh ra ngay trong thư mục:
  * Toàn bộ họ tên đã được viết hoa trang trọng: **Nguyễn Văn An**, **Trần Thị Mai**, **Lê Hoàng Nam**!
  * Ngày tháng đã đồng bộ chuẩn Việt Nam: **24/10/2026**, **25/10/2026**, **26/10/2026**!
  * Tiền tệ chuẩn dấu chấm phân cách hàng nghìn và đuôi **VNĐ**, kèm dòng tổng cộng **7.150.000 VNĐ**!
* File gốc `chi_phi_cong_tac_tho.txt` vẫn nguyên vẹn 100%!"

---

### [03:50 - 04:30] TỔNG KẾT PHẦN 3 VÀ CẦU NỐI TIẾN VÀO PHẦN 4: TRỤ CỘT 2 — SKILLS
`[Chỉ vào thanh Pro Standard ở cuối Slide 3]`  
`[Tông giọng hào hứng, truyền cảm hứng]`

"**Bạn thấy đấy:** Nhờ việc tổ chức không gian làm việc chuẩn chỉ với **Hiến pháp `AGENTS.md`** và **Luật chuyên ngành trong `.agents/rules/`**, AI đã tự giác hoàn thiện một bảng kê chi phí thanh toán đạt chuẩn 100% mà bạn không cần phải cầm tay chỉ việc lại từ đầu!

Chúc mừng bạn đã chinh phục trọn vẹn **Trụ Cột 1: Rules**!

**Thế nhưng, sau khi AI đã nắm vững nội quy rồi, làm thế nào để trang bị thêm cho AI những 'bí kíp chuyên môn' cao cấp hơn** — như tự động đọc nội dung hàng chục file văn phòng để chuẩn hóa tên file `snake_case` chỉ trong vài giây?

Chào mừng bạn bước tiếp sang **Phần 4: Trụ Cột 2 — Skills: Trang Bị Thêm Bí Kíp Chuyên Môn Trong Vài Giây**! Mời bạn bấm sang **Bài 4.1** ngay bây giờ!"
