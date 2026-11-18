# KỊCH BẢN LỜI THOẠI BÀI HỌC 8.2
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 3:** Phòng Thí Nghiệm Thực Chiến Đỉnh Cao  
**Phần 8:** Dự Án Văn Phòng Đỉnh Cao  
**Tên bài:** Bài 8.2: Thực Chiến 02 — Trợ Lý Hộp Thư: Đọc Hiểu, Phân Loại Email & Gán Nhãn Tự Động  
**Thời lượng dự kiến:** 08:30  
**Slide tương ứng:** `phan_08_thuc_chien_van_phong_dinh_cao.html` (Slide 2: Trợ Lý Hộp Thư: Phân Loại & Gán Nhãn Gmail)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở slide Thực Chiến 02 (Dự Án 2: Trợ Lý Hộp Thư Thông Minh Gmail).
* **Màn hình chia đôi hoặc sẵn sàng chuyển tab:**  
  * Cửa sổ 1: Ứng dụng **Antigravity Desktop** đang mở khung chat.  
  * Cửa sổ 2: Trình duyệt web mở hòm thư **Gmail** cá nhân/công việc với một số email mẫu chưa đọc (1 email khiếu nại đối tác, 1 email báo giá hợp đồng, 1 thư nội bộ phòng ban, 1 thư tin tức quảng cáo).  
  * Cửa sổ 3: Phần mềm **Sublime Text** sẵn sàng mở thư mục `skills/` để kiểm tra mã nguồn kỹ năng.
* **Tông giọng:** Chuyên nghiệp, sắc bén, nhấn mạnh vào giá trị tiết kiệm hàng giờ đồng hồ mỗi ngày cho người làm việc văn phòng.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD SCRIPT)

### [00:00 - 01:30] NỖI ĐAU HỘP THƯ GMAIL & BÀI TOÁN PHÂN LOẠI MỖI SÁNG
`[Hiển thị Slide Thực Chiến 02: Dự Án 2 - Trợ Lý Hộp Thư Gmail]`  
`[Người hướng dẫn nhìn thẳng camera, giọng đồng cảm]`

"Chào mừng các bạn đến với **Bài 8.2: Thực Chiến 02**!  
Có bao giờ bạn vừa mở máy tính vào lúc 8 giờ sáng, vừa nhấp một ngụm cà phê thì đập vào mắt là một hòm thư Gmail ngập ngụa với 50 đến 100 email chưa đọc?  
Trong mớ hỗn độn đó:
* Có email khiếu nại khẩn cấp của khách hàng đòi xử lý ngay trong sáng nay.
* Có email yêu cầu báo giá của đối tác tiềm năng cần phản hồi sớm.
* Có các thông báo nội bộ của phòng hành chính nhân sự.
* Và xen lẫn là hàng tá email quảng cáo, tin khuyến mãi không quan trọng.

Nếu làm thủ công: Bạn phải bấm vào từng thư, đọc lướt nội dung, rồi tự tay tạo nhãn (Label), gắn nhãn màu hoặc kéo thả vào từng thư mục. Làm xong việc lọc thư này thì đồng hồ đã điểm 9 giờ 30 sáng — bạn mất toi buổi sáng năng suất nhất trong ngày! Thậm chí tệ hơn, vì hoa mắt, bạn có thể bỏ lỡ một email khẩn cấp khiến công ty bị phạt hợp đồng!

Hôm nay, chúng ta sẽ chấm dứt hoàn toàn cảnh tượng đó. Tôi sẽ hướng dẫn các bạn cách **ra lệnh cho Antigravity tự thiết kế một Kỹ Năng mang tên `tro-ly-hop-thu-thong-minh`**: Tự động đọc hiểu ngữ nghĩa nội dung tiếng Việt của từng bức thư, tự động phân loại vào 4 nhóm nhãn chuẩn chỉnh và gắn nhãn trực tiếp trên Gmail chỉ sau 30 giây!"

---

### [01:30 - 03:45] TƯ DUY THIẾT KẾ SKILL: ĐÓNG GÓI NGHIỆP VỤ HỘP THƯ
`[Chuyển màn hình sang Antigravity Desktop]`  
`[Mở Sublime Text trỏ vào thư mục làm việc]`

"Cũng giống như bài học trước, chúng ta không dùng một câu lệnh tạm bợ. Chúng ta muốn một kỹ năng nằm sẵn trên máy để sáng nào bật máy lên cũng dùng được ngay!  
Để giải quyết bài toán phân loại email, kỹ năng `tro-ly-hop-thu-thong-minh` của chúng ta cần hội tụ 3 thành phần:
1. **File nghiệp vụ `SKILL.md`**: Hướng dẫn AI cách dùng cổng Gmail MCP để tìm các email chưa đọc (`is:unread`), đọc tiêu đề và nội dung tóm tắt.
2. **Bộ quy tắc phân loại (`Rules`)**: Định nghĩa tiêu chí phân loại 4 nhóm nhãn:
   * 🔴 `1_Khan_Cap`: Thư có yếu tố phàn nàn, sự cố hệ thống, deadline trong ngày.
   * 🟡 `2_Kinh_Doanh_Bao_Gia`: Yêu cầu báo giá, hợp đồng, đàm phán thương mại.
   * 🟢 `3_Noi_Bo`: Thông báo hành chính, lịch họp, phê duyệt nội bộ.
   * ⚪ `4_Tham_Khao`: Thư bản tin công nghệ, tài liệu tham khảo.
3. **Chốt chặn an toàn (`Hooks` & Giới hạn)**: Đây là hòm thư thật của bạn, vì vậy quy tắc an toàn số 1 là: **Tuyệt đối không bao giờ xóa email** (`delete_email`), và **không được tự tiện gửi email trả lời** khi chưa có lệnh rõ ràng của bạn!

Bây giờ, hãy cùng xem cách biến toàn bộ yêu cầu khắt khe này thành một **Prompt Vàng 4 bước chuẩn mực**!"

---

### [03:45 - 05:45] SOẠN PROMPT VÀNG & GIẢI MÃ: TẠI SAO ĐÂY LÀ PROMPT TỐT?
`[Quay màn hình khung chat Antigravity Desktop]`  
`[Dán đoạn prompt mẫu lên màn hình]`

"Hãy nhìn vào câu lệnh tôi gửi cho Antigravity:

> *'Chào Antigravity, hãy đóng vai một Chuyên gia Quản trị Hộp thư Doanh nghiệp. Hãy giúp tôi tạo một Kỹ Năng mới (Skill) mang tên `tro-ly-hop-thu-thong-minh` tại thư mục `skills/tro-ly-hop-thu-thong-minh/` với các yêu cầu cụ thể sau:*  
> *1. [Mục tiêu]: Tạo file `SKILL.md` hướng dẫn quy trình tự động quét tối đa 10 email chưa đọc gần nhất trong hộp thư đến bằng Gmail MCP (`search_emails`), phân tích ngữ nghĩa nội dung bằng AI, tự tạo các nhãn tương ứng nếu chưa có và gán nhãn cho từng email bằng `modify_email`.*  
> *2. [Bối cảnh]: Hộp thư của tôi là hộp thư kinh doanh & vận hành. Cần phân loại email thành đúng 4 nhóm nhãn chuẩn:*  
> *   - `🔴 Khẩn Cấp`: Chứa từ khóa khiếu nại, sự cố kỹ thuật, hỏng hóc, cần xử lý trong ngày.*  
> *   - `🟡 Báo Giá & Hợp Đồng`: Thư yêu cầu báo giá, trao đổi hợp đồng, ký kết.*  
> *   - `🟢 Nội Bộ`: Thư từ đồng nghiệp, nhân sự, lịch họp công ty.*  
> *   - `⚪ Tin Tức & Khác`: Thư quảng cáo, newsletter, thông báo tự động.*  
> *3. [Tiêu chuẩn]: File `SKILL.md` phải có đầy đủ cú pháp YAML frontmatter chuẩn. Sau khi phân loại xong, AI phải in ra một bảng báo cáo tóm tắt trên khung chat gồm: Tên người gửi, Tiêu đề, Nhãn được gán, và Tóm tắt 1 câu nội dung chính.*  
> *4. [Giới hạn & An toàn]: BẮT BUỘC tuân thủ: Chỉ sử dụng quyền đọc và gán nhãn (`search_emails`, `read_email`, `modify_email`, `create_label`). Tuyệt đối KHÔNG được dùng bất kỳ công cụ nào để xóa email (`delete_email`) hoặc tự động gửi email phản hồi (`send_email`).'*

`[Dừng lại 5 giây, nhấn mạnh từng luận điểm]`  
Hãy bóc tách xem: **Tại sao đây lại là một prompt mẫu mực?**
* **Mục tiêu (Goal):** Nêu rõ hành động cần làm: Quét 10 thư chưa đọc ➔ Phân tích ngữ nghĩa ➔ Tạo nhãn ➔ Gán nhãn. Không có bất kỳ khoảng trống mơ hồ nào.
* **Bối cảnh (Context):** Cung cấp chính xác 4 nhóm nhãn với màu sắc và ngữ cảnh cụ thể. AI sẽ dựa vào đây để phân loại chính xác theo tư duy con người chứ không phân loại máy móc theo từ khóa thô sơ.
* **Tiêu chuẩn (Standard):** Yêu cầu chuẩn YAML cho Skill và định dạng bảng tóm tắt 4 cột trực quan để người dùng kiểm tra kết quả ngay trong khung chat.
* **Giới hạn (Boundary):** Chốt chặn sinh tử! Khóa chặt quyền xóa và quyền gửi mail. Điều này giúp bạn hoàn toàn yên tâm 100% khi trao hòm thư cá nhân cho AI quản lý!"

---

### [05:45 - 07:00] AI TẠO SKILL & THỰC THI THỬ NGHIỆM TRÊN HÒM THƯ THẬT
`[Bấm Enter gửi prompt]`  
`[Quan sát AI tạo file SKILL.md trong Sublime Text]`

"Chỉ sau khoảng 10 giây, Antigravity đã tạo xong toàn bộ thư mục `skills/tro-ly-hop-thu-thong-minh/SKILL.md` với đầy đủ các hướng dẫn logic.

Bây giờ, hãy thử nghiệm ngay trên hòm thư Gmail thật của tôi nhé!  
Tôi chỉ cần gõ một câu lệnh ngắn:  
> *'Hãy sử dụng skill `tro-ly-hop-thu-thong-minh` để quét và phân loại các email chưa đọc trong hộp thư của tôi!'*  
`[Bấm Enter]`

Các bạn nhìn màn hình thực thi:  
1. Antigravity gọi Gmail MCP quét hộp thư đến: Phát hiện 4 email chưa đọc.  
2. Nó đọc nội dung từng bức thư:  
   * Bức thư 1: Khách hàng báo 'Hệ thống thanh toán bị lỗi không bấm được nút Mua hàng' ➔ AI phân tích: Đây là sự cố nghiêm trọng ➔ Gán nhãn `🔴 Khẩn Cấp`!  
   * Bức thư 2: Công ty X xin bảng báo giá dịch vụ đào tạo tháng 11 ➔ Gán nhãn `🟡 Báo Giá & Hợp Đồng`!  
   * Bức thư 3: Phòng Nhân sự thông báo lịch khám sức khỏe định kỳ ➔ Gán nhãn `🟢 Nội Bộ`!  
   * Bức thư 4: Thư thông báo ưu đãi Black Friday ➔ Gán nhãn `⚪ Tin Tức & Khác`!  
3. Nó tự động tạo các nhãn mới trên Gmail và gắn đúng nhãn vào từng thư."

---

### [07:00 - 08:00] MỞ GMAIL NGHIỆM THU TRỰC TIẾP TRÊN TRÌNH DUYỆT
`[Chuyển màn hình sang tab trình duyệt web đang mở Gmail]`  
`[Bấm F5 refresh trang Gmail]`

"Và bây giờ, khoảnh khắc kỳ diệu nhất! Hãy cùng tôi sang tab Gmail trên Chrome và bấm F5 tải lại trang!  
`[Màn hình Gmail hiện lên]`  
Các bạn nhìn xem!  
Tại cột bên trái của Gmail: 4 nhãn màu tuyệt đẹp đã xuất hiện!  
Và ngay trong Hộp thư đến: Từng bức thư đã được gắn đúng chiếc nhãn rực rỡ tương ứng!  
Bức thư khiếu nại đã mang nhãn đỏ `🔴 Khẩn Cấp` nổi bần bật ngay trên cùng! Nhìn vào một cái là bạn biết ngay bức thư nào cần mở ra xử lý trước, bức thư nào có thể để lại đọc sau.  
Không còn cảnh hoang mang, không còn nỗi sợ bỏ sót việc!"

---

### [08:00 - 08:30] TỔNG KẾT & DẪN SANG BÀI THỰC CHIẾN 03
`[Quay lại màn hình camera, ánh mắt đầy phấn khởi]`

"Như vậy là chỉ với một câu prompt chuẩn 4 bước vàng, bạn đã tự tạo ra cho mình một Trợ lý Hộp thư thông minh làm việc 24/7, giúp bạn giải phóng hoàn toàn khỏi nỗi ám ảnh email mỗi sáng!

Và nếu phân loại email đã giúp bạn tiết kiệm 1 tiếng mỗi ngày, thì ở bài học tiếp theo, chúng ta sẽ bước vào một bài toán còn 'hại não' hơn gấp bội đối với dân văn phòng: **Nỗi sợ các công thức tính toán phức tạp trong Excel như VLOOKUP, XLOOKUP, INDEX/MATCH hay các bảng tính khổng lồ hàng nghìn dòng**!  
Ở **Bài 8.3: Thực Chiến 03**, chúng ta sẽ biến Antigravity thành một **Phù Thủy Bảng Tính**, giải quyết siêu tốc mọi công thức hóc búa chỉ trong tích tắc!

Mời các bạn cùng bấm sang **Bài 8.3** để chinh phục thế giới Excel ngay bây giờ!"
