# KỊCH BẢN LỜI THOẠI BÀI HỌC 5.1
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 2:** Kho Vũ Khí 7 Trụ Cột Cho Dân Văn Phòng  
**Phần 5:** Trụ Cột 3 — Subagents: Nhân Bản Đội Ngũ Trợ Lý Làm Việc Song Song  
**Tên bài:** Bài 5.1: Subagents là gì? Cách phân vai trợ lý lọc số liệu và trợ lý soạn văn bản  
**Thời lượng dự kiến:** 08:00  
**Slide tương ứng:** `phan_05_tru_cot_subagents.html` (Slide 1)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_05_tru_cot_subagents.html` (Slide 9 và Slide 10).
* **Minh họa sơ đồ:** Sơ đồ tổ chức phòng ban: 1 Giám đốc điều hành (Lead Agent) ở trên, điều phối 2 Trợ lý phụ chuyên trách ở dưới.
* **Tông giọng:** Hào hứng, uy quyền như một nhà lãnh đạo điều hành một đội ngũ nhân sự tinh nhuệ.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD SCRIPT)

### [00:00 - 01:30] MỞ ĐẦU: SAI LẦM KHI BẮT MỘT NGƯỜI ÔM ĐỒM MỌI VIỆC
`[Hiển thị Slide 1: Trụ Cột 3 — Subagents: Đội Ngũ Nhân Viên Ảo]`  
`[Tông giọng đồng cảm, gợi mở tình huống]`

"Chào mừng các bạn đến với **Phần 5: Trụ Cột 3 — Subagents (Đội Ngũ Trợ Lý Phụ Chuyên Môn)**!

Một sai lầm kinh điển nhất của những người mới dùng AI là:  
Bắt **đúng một con AI duy nhất** phải ôm đồm tất cả mọi thứ: Vừa bắt nó đọc 5 tài liệu nghiên cứu dày cộp, vừa bắt nó tính toán số liệu kế toán chi tiết, vừa bắt nó sáng tạo viết bài thuyết trình!  
Và kết quả là gì?  
Bộ nhớ ngắn hạn của AI bị quá tải nghiêm trọng. Nó bắt đầu bị 'tẩu hỏa nhập ma': Lấy số liệu của file này cắm vào báo cáo của file kia, câu trả lời bị cụt ngủn và tốc độ phản hồi chậm như rùa bò!

`[Nhấn mạnh]`  
Trong đời sống thực tế, một người giám đốc tài ba không bao giờ tự mình làm hết mọi việc. Giám đốc sẽ triệu tập một cuộc họp, giao việc cho 2 nhân viên cấp dưới:  
*'Cậu A chuyên ngồi đọc tài liệu và lọc số liệu; Cậu B chuyên ngồi viết bài báo cáo'*.  
Hai người cùng làm việc song song, sau đó bàn giao kết quả về cho Giám đốc nghiệm thu.  
Và trong Antigravity, chúng ta có một vũ khí mang tên **Subagents** hoạt động y hệt như vậy!"

---

### [01:30 - 04:30] CƠ CHẾ BẢO VỆ BỘ NHỚ: NGỮ CẢNH ĐỘC LẬP (ISOLATED CONTEXT)
`[Chuyển Slide 10: Ngữ Cảnh Độc Lập — Trợ Lý Chuyên Môn Làm Việc Trong Phòng Riêng]`  
`[Chỉ vào hình ảnh 2 phòng làm việc riêng biệt trên Slide]`

"Điểm thần kỳ nhất của **Subagents** là cơ chế **Ngữ cảnh độc lập (Isolated Context)**:
* Khi AI chính (Lead Agent) triệu hồi một Subagent (trợ lý phụ), hệ thống sẽ cấp cho trợ lý phụ đó một 'căn phòng làm việc riêng biệt' hoàn toàn:
  * Trợ lý phụ có thể đọc hàng trăm nghìn dòng dữ liệu thô, tìm kiếm tài liệu hàng giờ đồng hồ trong căn phòng đó.
  * Toàn bộ những dữ liệu rườm rà, nháp thử đó **hoàn toàn không làm ảnh hưởng** đến khung chat chính của bạn!
  * Khi làm việc xong, trợ lý phụ chỉ mang đúng **1 bản tóm tắt tinh hoa nhất** bước ra ngoài báo cáo cho AI chính.
* Nhờ cơ chế này:
  * Bộ nhớ làm việc chính của bạn luôn trong trẻo, sạch sẽ 100%.
  * Công việc được phân tách rõ ràng theo chuyên môn, không bao giờ lo bị lẫn lộn giữa việc tính toán số liệu và việc hành văn sáng tạo!"

---

### [04:30 - 06:45] CÁCH THIẾT LẬP VAI TRÒ CHUYÊN BIỆT: 0 CẦN BIẾT CODE
`[Chuyển Slide 11: Cách Tạo Một Subagent — Chỉ Cần Một File Markdown Đơn Giản]`  
`[Rê chuột chỉ vào cấu trúc file Markdown]`

"Nhiều bạn nghe chữ 'Subagent' thì tưởng là phải viết phần mềm phức tạp. Nhưng không!  
Bản chất của một Subagent trong Antigravity **chỉ là một tệp văn bản Markdown duy nhất (`.md`)** đặt trong thư mục `.gemini/agents/` hoặc thư mục dự án của bạn:
* Tệp này quy định rõ 3 điều:
  1. **Tên trợ lý (Name):** Ví dụ `chuyen_vien_so_lieu` hoặc `bien_tap_vien`.
  2. **Mô tả vai trò (Description):** Trợ lý này giỏi việc gì và khi nào sếp nên gọi bạn ấy vào việc.
  3. **Quyền hạn (Tools):** Bạn ấy được phép dùng những công cụ gì (được đọc file, hay được duyệt web, hay chỉ được viết lách).

Chỉ với vài dòng chỉ dẫn bằng tiếng Việt tự nhiên, bạn đã chính thức tuyển dụng thành công một chuyên viên AI về làm việc cho mình!"

---

### [06:45 - 08:00] TỔNG KẾT BÀI & CÂU DẪN SANG THỰC HÀNH BÀI 5.2
`[Quay lại màn hình camera, ánh mắt đầy phấn khởi]`

"Như vậy là các bạn đã nắm trọn vẹn tư duy lãnh đạo đội ngũ trợ lý AI: Không ôm đồm, phân vai rõ ràng và tận dụng sức mạnh làm việc song song.

Bây giờ, hãy cùng tôi bước vào **Bài 5.2: Thực hành điều phối 2 trợ lý chạy song song**!  
Chúng ta sẽ cùng trải nghiệm một bài toán thực tế: Một trợ lý chuyên tính toán số liệu doanh thu, và một trợ lý chuyên viết email báo cáo gửi Ban Giám Đốc — chạy cùng lúc trên màn hình của bạn!

Mời các bạn cùng bấm sang Bài 5.2 ngay bây giờ!"
