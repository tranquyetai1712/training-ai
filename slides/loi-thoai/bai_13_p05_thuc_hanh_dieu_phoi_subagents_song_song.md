# KỊCH BẢN LỜI THOẠI BÀI HỌC 5.2
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 2:** Kho Vũ Khí 7 Trụ Cột Cho Dân Văn Phòng  
**Phần 5:** Trụ Cột 3 — Subagents: Nhân Bản Đội Ngũ Trợ Lý Làm Việc Song Song  
**Tên bài:** Bài 5.2: Thực hành: Điều phối 2 trợ lý chạy song song tăng gấp đôi tốc độ xử lý việc  
**Thời lượng dự kiến:** 04:30 (Chuẩn Udemy Micro-Learning • Parallel Subagent Execution)  
**Slide tương ứng:** `phan_05_tru_cot_subagents.html` (Slide 2)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_05_tru_cot_subagents.html` (Slide 2: Thực Hành: Điều Phối 2 Trợ Lý Ảo Song Song).
* **Môi trường thực hành:** Mở Antigravity Desktop tại workspace độc lập `slides/Demo/dieu-phoi-subagents-song-song/`. Tệp bảng tính `doanh_thu_thang_10.xlsx` đã có sẵn dữ liệu thực tế của 10 nhân viên (Top 3: Nguyễn Văn An 120 triệu, Trần Thị Mai 95 triệu, Lê Hoàng Nam 88 triệu; tổng 520 triệu). Giảng viên mở workspace ra là thực hành trực tiếp ngay.
* **Tông giọng:** Sôi nổi, dứt khoát của một người chỉ huy đang điều hành các trợ lý tác chiến trên màn hình.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD LEAN SCRIPT)

### [00:00 - 00:45] BÀI TOÁN DOANH SỐ CUỐI THÁNG & NỖI ĐAU THỦ CÔNG
`[Slide 2: Thực Hành: Điều Phối 2 Trợ Lý Ảo Song Song]`  
`[Mở Antigravity Desktop tại workspace slides/Demo/dieu-phoi-subagents-song-song/]`  
`[Chỉ vào file doanh_thu_thang_10.xlsx đã chuẩn bị sẵn bên thanh File Explorer]`

"Chào mừng bạn quay trở lại với Bài 5.2!

Hãy nhìn vào workspace demo trên màn hình của tôi: Chúng ta đã chuẩn bị sẵn tệp `doanh_thu_thang_10.xlsx`. Đây là một bài toán vô cùng quen thuộc vào mỗi dịp cuối tháng tại bất kỳ doanh nghiệp nào:
* **Nhiệm vụ 1:** Mở bảng tính Excel ra, lọc ra Top 3 nhân viên có thành tích xuất sắc nhất và tính tổng doanh thu toàn công ty.
* **Nhiệm vụ 2:** Dựa trên số liệu đó, soạn ngay một bức thư email vinh danh khen thưởng gửi tới toàn thể cán bộ nhân viên, với văn phong hào hứng, ấm áp và truyền cảm hứng mạnh mẽ.

**Thế nhưng thực tế là,** nếu bạn ngồi mở file tính toán rồi tự gõ email một mình, bạn sẽ mất ít nhất 30 đến 45 phút.

**Chính vì thế hôm nay,** chúng ta sẽ xem cách Antigravity **tự động phân rã bài toán và kích hoạt Subagents chạy ngầm** để hoàn tất toàn bộ công việc này trong chưa đầy 2 phút!"

---

### [00:45 - 02:00] THAO TÁC RA LỆNH THEO MỤC TIÊU ĐẦU RA (OUTCOME-DRIVEN)
`[Chuyển màn hình sang khung chat Antigravity Desktop tại workspace slides/Demo/dieu-phoi-subagents-song-song/]`  
`[Thao tác gõ câu lệnh ngắn gọn tự nhiên]`

"Tại khung chat Antigravity, bạn hoàn toàn không cần phải ra lệnh máy móc hay cấu hình phức tạp. Với tư cách là một Tổng Chỉ Huy, bạn chỉ cần giao việc tự nhiên theo đúng mục tiêu kết quả mong muốn:

> *'Từ tệp `doanh_thu_thang_10.xlsx`, hãy lọc ra Top 3 nhân viên xuất sắc nhất tháng và soạn một bức email vinh danh truyền cảm hứng gửi toàn thể công ty.'*

`[Nhấn Enter và cùng học viên quan sát AI tự động xử lý]`  
Ngay khi bạn nhấn Enter, bạn hãy chú ý quan sát những gì diễn ra trên màn hình!"

---

### [02:00 - 03:45] QUAN SÁT CƠ CHẾ TỰ ĐỘNG PHÂN RÃ & CHẠY SUBAGENTS NGẦM
`[Chỉ chuột vào các thẻ Subagent Task xuất hiện ngầm trên màn hình]`

"**Bạn hãy nhìn kỹ luồng xử lý tự hành của Antigravity:**
* AI chính không hề ôm đồm việc nạp cả bảng tính vào khung chat này! Nó tự động nhận diện bài toán gồm 2 công đoạn chuyên biệt:
  * **Công đoạn 1:** Phân tích dữ liệu bảng tính. Antigravity tự động kích hoạt một Subagent chạy ngầm trong căn phòng riêng biệt, mở file `doanh_thu_thang_10.xlsx` và thực hiện tính toán.
  * **Công đoạn 2:** Sáng tạo nội dung truyền thông. Ngay khi Subagent số liệu hoàn thành, dữ liệu sạch được chuyển tiếp sang luồng soạn thảo văn bản.
* **Và hãy nhìn vào tốc độ kinh ngạc này:**  
  Chỉ sau vài giây, kết quả bóc tách Top 3 đã hoàn tất chuẩn xác 100%:
  1. Nguyễn Văn An: 120.000.000 VNĐ.
  2. Trần Thị Mai: 95.000.000 VNĐ.
  3. Lê Hoàng Nam: 88.000.000 VNĐ.  
  Tổng doanh thu đạt: 520.000.000 VNĐ!
* **Ngay lập tức,** bức thư email vinh danh được xuất hiện cực kỳ bắt mắt bên cửa sổ kết quả:  
  `[Chỉ vào cửa sổ bên phải màn hình]`  
  *'VINH DANH NHỮNG NGÔI SAO SÁNG THÁNG 10 — CHÚC MỪNG TOP 3 BÙNG NỔ DOANH SỐ!'*  
  Từng con số, từng họ tên nhân viên và từng lời chúc mừng được viết chỉn chu, trang trọng và đầy lửa nhiệt huyết!"

---

### [03:45 - 04:30] NGHIỆM THU KẾT QUẢ & CẦU NỐI SANG PHẦN 6 (HOOKS)
`[Rê chuột chỉ vào khung chat chính sạch bóng và dòng Footer Bar trên Slide 2]`

"**Bạn thấy đấy, kết quả ở đây vô cùng ấn tượng:**
* Toàn bộ quá trình tính toán hàng nghìn ô dữ liệu Excel diễn ra ngầm trong phòng riêng của Subagent, **khung chat chính của bạn hoàn toàn sạch bóng**.
* Bạn chỉ nhận được đúng thành phẩm cuối cùng: Bảng Top 3 ngăn nắp và bức thư email hoàn chỉnh sẵn sàng copy gửi đi!  
Tốc độ hoàn thành công việc nhanh gấp đôi, bạn hoàn toàn rảnh tay mà không cần phải nhọc công phân công thủ công.

**Thế nhưng khi các trợ lý AI tự động chạy ngầm trên máy tính, một mối lo ngại lớn sẽ nảy sinh:**  
*Nếu một trợ lý nào đó vô tình chạy nhầm lệnh sửa đè lên file hợp đồng gốc hoặc xóa mất dữ liệu quan trọng trên ổ đĩa thì sao?*

**Làm thế nào để cài đặt một 'Vòng kim cô' tự động khóa chặt mọi hành động nguy hiểm của AI trước khi nó kịp chạm vào dữ liệu của bạn?**  
Câu trả lời nằm ở **Phần 6: Trụ Cột 4 — Hooks**!

Hẹn gặp lại bạn ở Bài 6.1 ngay sau đây!"
