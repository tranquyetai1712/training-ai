# KỊCH BẢN LỜI THOẠI BÀI HỌC 3.3
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 2:** Kho Vũ Khí 7 Trụ Cột Cho Dân Văn Phòng  
**Phần 3:** Trụ Cột 1 — Rules: Huấn Luyện AI Tuân Thủ Quy Chuẩn Văn Phòng  
**Tên bài:** Bài 3.3: Thực hành: Phối hợp AGENTS.md và rules/xx.md chuẩn hóa nhật ký cuộc gọi CSKH từ file thô  
**Thời lượng dự kiến:** 04:30 (Chuẩn Udemy Micro-Learning • Hands-on Walkthrough)  
**Slide tương ứng:** `phan_03_tru_cot_rules.html` (Slide 3)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_03_tru_cot_rules.html` (Slide 3: Thực Hành: Phối Hợp AGENTS.md & .agents/rules/ Xử Lý Nhật Ký Khiếu Nại).
* **Tài nguyên mẫu có sẵn:** Mở thư mục workspace độc lập `slides/Demo/xu-ly-khieu-nai-cskh/` trên Antigravity Desktop.
  * Đã chuẩn bị sẵn file thô: `ghi_chu_cuoc_goi_tho.txt`
  * Đã chuẩn bị sẵn Hiến pháp dự án: `AGENTS.md`
  * Đã chuẩn bị sẵn Luật chuyên ngành: `.agents/rules/phan_loai_khieu_nai.md`
* **Tông giọng:** Nhiệt tình, thực chiến, dẫn dắt từng thao tác trực quan để học viên thấy rõ sự phối hợp hoàn hảo trong một workspace chuẩn Antigravity.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD LEAN SCRIPT)

### [00:00 - 00:35] MỤC TIÊU THỰC HÀNH: PHỐI HỢP AGENTS.MD VÀ RULES/XX.MD TRÊN TỆP DỮ LIỆU THỰC TẾ
`[Slide 3: Thực Hành: Phối Hợp AGENTS.md & .agents/rules/ Xử Lý Nhật Ký Khiếu Nại]`  
`[Tông giọng hào hứng, thực chiến]`

"Chào mừng bạn đến với Bài 3.3 — bài thực hành khép lại Trụ Cột 1 về Rules!

Nếu chỉ gõ prompt trong ô chat thì chatbot thông thường cũng tự đoán được. **Thế nhưng sức mạnh độc bản của Google Antigravity là khả năng tự động đọc file và thực thi nội quy trực tiếp trên ổ cứng máy tính!**

Trong bài học này, chúng ta sẽ không mất thời gian ngồi gõ dữ liệu thô. Thay vào đó, tôi đã chuẩn bị sẵn một không gian làm việc mẫu độc lập, nơi bạn sẽ thấy rõ sự kết hợp hoàn hảo giữa **Bản Hiến Pháp chung `AGENTS.md`** và **Luật chuyên ngành `.agents/rules/phan_loai_khieu_nai.md`** để tự động xử lý một file nhật ký cuộc gọi CSKH ghi chép vội thành bảng báo cáo phân loại mức độ ưu tiên chuẩn 100% phong cách công sở.

Mời bạn mở Antigravity Desktop lên và cùng bắt tay vào làm với tôi ngay nhé!"

---

### [00:35 - 01:50] KHÁM PHÁ WORKSPACE MẪU XU-LY-KHIEU-NAI-CSKH & CẤU TRÚC CHUẨN GOOGLE
`[Chuyển màn hình sang Antigravity Desktop]`  
`[Mở thư mục slides/Demo/xu-ly-khieu-nai-cskh/ trên File Explorer]`

"Để bài học diễn ra mạch lạc và không làm bạn mất công tạo file từ đầu, trong thư mục cha `slides/Demo/`, tôi đã tạo riêng một thư mục dự án mang tên: `xu-ly-khieu-nai-cskh/`.

**Vì sao phải tách riêng như thế này?**  
Bởi vì sau này khóa học của chúng ta sẽ có rất nhiều bài thực hành khác nhau. Việc gom từng bài vào một thư mục con riêng biệt giúp từng workspace hoàn toàn độc lập, không bao giờ bị xung đột quy tắc với nhau!

Bây giờ bạn nhìn vào cấu trúc bên trong của `xu-ly-khieu-nai-cskh/`, đây chính là cấu trúc chuẩn chỉ nhất theo tài liệu Google:

1. **File dữ liệu thô (`ghi_chu_cuoc_goi_tho.txt`):**  
   Mở ra bạn sẽ thấy 3 dòng ghi chép vội của nhân viên trực ban:
   ```text
   1. khach hang nguyen anh tuan goi phan nan don hang ord9821 bi vo man hinh yeu cau doi gap sdt 0912345678 goi luc 9h sang ngay 10/24/2026
   2. tran thi thuy hoi ve don hang ord 9822 chua thay giao, khach chi hoi tham tien do sdt 0988776655 ngay 2026-10-25 luc 14:30
   3. le van duc khieu nai don hang ord-9823 giao sai mau ao, yeu cau hoan tien gap sdt 0905112233 ngay 26/10/2026 16:00
   ```
   Tên viết thường không dấu, mã đơn viết lung tung (`ord9821`, `ord 9822`, `ord-9823`), ngày tháng lẫn lộn kiểu Mỹ và ISO.

2. **Bản Hiến pháp dự án (`AGENTS.md` đặt tại thư mục gốc):**  
   Quy định ranh giới an toàn tối cao: *'Không sửa đè lên file thô gốc ghi_chu_cuoc_goi_tho.txt, luôn xuất kết quả phân loại ra file mới mang tên: bao_cao_xu_ly_khieu_nai.xlsx.'*

3. **Luật chuyên ngành (`.agents/rules/phan_loai_khieu_nai.md`):**  
   Nằm trong thư mục chuẩn `.agents/rules/` với khối khai báo YAML chuẩn Google:
   ```yaml
   ---
   trigger: glob
   globs: "*.txt, *.xlsx"
   description: "Quy chuẩn trích xuất và phân loại mức độ ưu tiên cuộc gọi CSKH"
   ---
   ```
   Bên dưới quy định 4 điều luật thép:
   * Mã đơn hàng bắt buộc viết hoa dạng `ORD-XXXX`.
   * Tự động gắn nhãn mức độ: **[HỎA TỐC]** khi vỡ hỏng hàng; **[KHẨN CẤP]** khi giao sai mẫu đòi hoàn tiền; và **[TIÊU CHUẨN]** khi khách chỉ hỏi tiến độ.
   * Chuẩn hóa họ tên viết hoa, số điện thoại `0xxx.xxx.xxx`, và thời gian chuẩn `HH:mm DD/MM/YYYY`.
   * **Và đặc biệt nhất là điều luật thứ 4 — Xuất trực tiếp bảng tính Excel (`.xlsx`) chuẩn văn phòng:** Xuất file bảng tính Excel `.xlsx` với đầy đủ các cột rõ ràng, dòng tiêu đề nổi bật, mở trực tiếp bằng Microsoft Excel làm việc ngay mà không lo lỗi font tiếng Việt hay vỡ định dạng như các tệp văn bản thông thường!"

---

### [01:50 - 02:40] CẢNH BÁO QUÉT PHẲNG (FLAT DIRECTORY SCANNING) CHUẨN GOOGLE
`[Quay lại Slide 3, chỉ chuột vào phần lưu ý kỹ thuật]`  
`[Tông giọng cảnh báo chuyên gia]`

"Trước khi bấm nút kiểm chứng, bạn hãy ghi nhớ **Quy tắc quét phẳng (Flat Directory Scanning)** từ tài liệu chính thức của Google:

* Tệp `AGENTS.md` bắt buộc phải nằm ngay ở tầng ngoài cùng của workspace dự án.
* Các file luật chuyên ngành phải nằm trực tiếp bên trong thư mục `.agents/rules/` (như `.agents/rules/phan_loai_khieu_nai.md`), tuyệt đối không tạo thư mục con lồng nhau như `.agents/rules/cskh/phan_loai.md` vì Antigravity sẽ bỏ qua không quét đến.
* Và luôn duy trì dung lượng file súc tích dưới 24KB để AI đọc hiểu trong chớp mắt."

---

### [02:40 - 03:50] KIỂM CHỨNG THỰC TẾ: RA LỆNH 1 DÒNG ➔ AI TỰ KÍCH HOẠT RULE & XUẤT FILE MỚI CHUẨN ĐÉT
`[Mở lại Antigravity Desktop trong workspace xu-ly-khieu-nai-cskh, bấm nút New Task]`  
`[Tông giọng hào hứng, chuẩn bị đón chờ kết quả]`

"**Và bây giờ là khoảnh khắc kỳ diệu nhất:** Chúng ta kiểm chứng xem hệ sinh thái Rules vận hành ra sao!

1. Trong thư mục dự án `xu-ly-khieu-nai-cskh/`, bạn bấm nút **New Task** mở một phiên làm việc mới toanh.
2. Gõ đúng một câu lệnh ngắn gọn duy nhất, không cần nhắc lại bất kỳ quy tắc nào:
   > *'Hãy xử lý file `ghi_chu_cuoc_goi_tho.txt` giúp tôi.'*
3. Nhấn phím `Enter` và cùng tôi quan sát màn hình!

`[Chỉ chuột vào màn hình Antigravity đang chạy]`  
**Bạn nhìn xem! Đây chính là phép màu của Trụ Cột Rules:**
* AI nhận diện bạn đang xử lý file có đuôi `.txt` ➔ Cơ chế `trigger: glob` lập tức kích hoạt file `.agents/rules/phan_loai_khieu_nai.md`!
* Đồng thời, AI đọc `AGENTS.md` và hiểu rằng không được sửa vào file gốc, nên ngay lập tức một file bảng tính Excel mới tinh mang tên `bao_cao_xu_ly_khieu_nai.xlsx` được sinh ra ngay trong thư mục — sẵn sàng để bạn nhấp đúp chuột mở thẳng lên bằng Microsoft Excel:
  * Toàn bộ mã đơn đã đồng nhất chuẩn: **ORD-9821**, **ORD-9822**, **ORD-9823**!
  * Tự động phân cấp chuẩn xác: Đơn vỡ màn hình được gắn nhãn **[HỎA TỐC]**, đơn sai áo gắn nhãn **[KHẨN CẤP]**, đơn hỏi tiến độ gắn nhãn **[TIÊU CHUẨN]**!
  * Kèm theo cột **Hành động đề xuất** cụ thể để nhân viên xử lý ngay mà không phải suy nghĩ!
* File gốc `ghi_chu_cuoc_goi_tho.txt` vẫn nguyên vẹn 100%!"

---

### [03:50 - 04:30] TỔNG KẾT PHẦN 3 VÀ CẦU NỐI TIẾN VÀO PHẦN 4: TRỤ CỘT 2 — SKILLS
`[Chỉ vào thanh Pro Matrix ở cuối Slide 3]`  
`[Tông giọng hào hứng, truyền cảm hứng]`

"**Đến đây, bạn có nhận ra điều kỳ diệu gì không?**
Hãy nhớ lại **Bài 2.2**, chúng ta đã học **Công thức 4 bước vàng ra lệnh**: Mục Tiêu ➔ Bối Cảnh ➔ Tiêu Chuẩn ➔ Giới Hạn. Bình thường nếu không có Rules, mỗi lần giao việc bạn sẽ phải gõ một đoạn prompt dài cả trang để nhồi nhét đủ 4 thành tố này!

**Thế nhưng ngày hôm nay, bạn hãy nhìn lại câu lệnh của chúng ta:**
* Bạn chỉ cần gõ đúng 1 dòng: *'Hãy xử lý file `ghi_chu_cuoc_goi_tho.txt` giúp tôi'* ➔ Đây chính là **Mục Tiêu**!
* Còn **Bối Cảnh** (tổng đài CSKH, 100% tiếng Việt lịch sự) và **Giới Hạn** (tuyệt đối không sửa đè file gốc) ➔ Đã được `AGENTS.md` âm thầm bảo vệ!
* Và **Tiêu Chuẩn** (mã đơn ORD-XXXX, phân cấp ưu tiên, xuất định dạng bảng tính Excel .xlsx chuẩn chỉnh) ➔ Đã được file Rules chuyên ngành tự động bơm vào đầu não AI!

**Nói cách khác:** Trụ Cột Rules chính là cỗ máy tự động hóa hoàn toàn Công thức 4 bước vàng — giúp bạn chỉ cần ra lệnh 1 chạm mà AI vẫn làm đúng ý 100%!

Chúc mừng bạn đã chinh phục trọn vẹn **Trụ Cột 1: Rules**!

**Thế nhưng, sau khi AI đã nắm vững nội quy rồi, làm thế nào để trang bị thêm cho AI những 'bí kíp chuyên môn' cao cấp hơn** — như tự động đọc nội dung hàng chục file văn phòng để chuẩn hóa tên file `snake_case` chỉ trong vài giây?

Chào mừng bạn bước tiếp sang **Phần 4: Trụ Cột 2 — Skills: Trang Bị Thêm Bí Kíp Chuyên Môn Trong Vài Giây**! Mời bạn bấm sang **Bài 4.1** ngay bây giờ!"
