# KỊCH BẢN LỜI THOẠI BÀI HỌC 7.2
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 2:** Kho Vũ Khí 7 Trụ Cột Cho Dân Văn Phòng  
**Phần 7:** Trụ Cột 5 — MCP: Cổng Kết Nối Đưa Dữ Liệu Công Việc Thực Tế Vào AI  
**Tên bài:** Bài 7.2: Thực hành: Kết nối cổng Trello MCP — Dựng bảng, chuẩn hóa thẻ việc, bóc tách dữ liệu và điều phối tự động từ con số 0  
**Thời lượng dự kiến:** 06:00 (Chuẩn Udemy Micro-Learning • Live Zero-to-Hero Integration)  
**Slide tương ứng:** `phan_07_tru_cot_mcp.html` (Slide 2)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_07_tru_cot_mcp.html` (Slide 2: Thực Hành: Kết Nối Cổng Trello MCP).
* **Môi trường thực hành:** Mở Antigravity Desktop tại workspace độc lập `slides/Demo/ket-noi-mcp-trello/` đã có sẵn Skill `trello-task-standardizer`, file mẫu `ghi_chu_cuoc_hop_tho.txt` và sổ tay `HUONG_DAN_KET_NOI_TRELLO_MCP.md`.
* **Trình duyệt đối chứng:** Mở sẵn tab Trello với một tài khoản/không gian làm việc **trống hoàn toàn (chưa có bảng, chưa có cột, chưa có thẻ nào)** để học viên thấy rõ sự "biến hình" từ con số 0.
* **Trạng thái cổng kết nối:** Cổng `trello` MCP hiển thị trạng thái đã kết nối (*Connected*) thông qua giao diện Customization.
* **Tông giọng:** Tự tin, gãy gọn, nhấn mạnh cảm giác bất ngờ khi AI chuyển từ các thao tác cơ bản sang 3 kịch bản thông minh mà thao tác tay trên web hoàn toàn không thể làm được.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD LEAN SCRIPT)

### [00:00 - 00:45] TÀI KHOẢN TRELLO TRỐNG TRƠN & LỢI THẾ CỔNG MCP
`[Slide 2: Thực Hành: Kết Nối Cổng Trello MCP]`  
`[Chiếu nhanh tab trình duyệt Trello đang trống hoàn toàn, chưa có bảng hay thẻ nào]`  
`[Chuyển sang Antigravity Desktop tại workspace slides/Demo/ket-noi-mcp-trello/]`

"Chào mừng bạn đến với Bài 7.2!

Ở bài trước, chúng ta đã hiểu MCP chính là chiếc cổng cắm vạn năng giúp AI vươn tay ra thế giới phần mềm thực tế. Hôm nay, chúng ta sẽ cùng nhau thực hành cắm trực tiếp **Cổng Trello MCP**!

Và hãy nhìn màn hình Trello của tôi lúc này: **Hoàn toàn mới tinh, trống trơn chưa có bất kỳ một bảng, một cột hay một chiếc thẻ nào cả!**  
Tôi sẽ không bấm nút *Create Board*, không kéo thả chuột, cũng không gõ tay từng đầu việc trên web Trello.  
Từ giờ trở đi, tôi chỉ ngồi nguyên ở khung chat **Antigravity** và ra lệnh bằng tiếng Việt để xem trợ lý AI tự dựng cả hệ thống công việc từ con số 0 ra sao nhé!"

---

### [00:45 - 01:25] KÍCH HOẠT CỔNG TRELLO 1-CLICK TRÊN GIAO DIỆN CUSTOMIZATION
`[Chỉ khung KẾT NỐI 1-CHẠM TRỰC QUAN trên Slide 2]`  
`[Thao tác trên Antigravity Desktop: Mở tab Customization -> Plugins / MCP]`

"Đặc biệt, trong phiên bản Antigravity hiện tại, việc kết nối cổng Trello đã trở nên **dễ dàng như cài một ứng dụng trên điện thoại**:

Bạn hoàn toàn **không cần phải biết lập trình, không cần mò mẫm lấy API Key hay Token phức tạp, và cũng không cần chạm vào bất kỳ file cấu hình JSON nào cả!**

Tất cả chỉ gói gọn trong 3 bước trên màn hình:
1. Bạn mở mục **Customization** trong Antigravity.
2. Tìm cổng **Trello** và bấm nút **Connect (Đăng nhập)**.
3. Trình duyệt mở lên một cửa sổ xác thực an toàn, bạn bấm **Cho phép (Allow)** — Ngay lập tức, cổng chuyển sang trạng thái xanh **Connected**!

Chỉ với 1 cú click chuột, Antigravity đã được trao trọn bộ quyền năng điều phối Trello!"

---

### [01:25 - 03:15] 5 THAO TÁC NỀN TẢNG: LÀM CHỦ TRELLO KHÔNG CẦN CHẠM CHUỘT
`[Chuyển màn hình sang khung chat Antigravity Desktop, để chế độ chia đôi hoặc chuyển qua lại nhanh với tab Trello]`

"Bây giờ, chúng ta sẽ bắt đầu với **5 thao tác nền tảng** để bạn thấy AI làm chủ toàn bộ các chức năng cốt lõi trên Trello:

#### Nhịp 1 — Khởi tạo bảng & dựng cấu trúc cột từ trang giấy trắng
Tôi gõ lệnh đầu tiên:
> *'1. Dùng Trello MCP tạo cho tôi một bảng mới tên "Vận Hành Văn Phòng Q4", bên trong tạo 3 cột theo đúng thứ tự: "Cần Làm (To Do)", "Đang Thực Hiện" và "Hoàn Thành".'*

`[Enter — AI gọi create_board và add_list_to_board]`  
Chỉ mất đúng 3 giây! Sang tab Trello bấm F5: Bảng mới cùng 3 cột ngay ngắn đã mọc ra!

#### Nhịp 2 — Thêm nhanh các thẻ công việc
Tiếp tục trong khung chat, tôi ra lệnh thêm task:
> *'2. Thêm giúp tôi 3 thẻ việc vào cột "Cần Làm (To Do)": (1) Chốt báo giá thiết bị văn phòng, (2) Soạn dự thảo hợp đồng thuê mặt bằng, (3) Đặt vé máy bay công tác Đà Nẵng — kèm mô tả ngắn cho từng thẻ.'*

`[Enter — AI gọi add_card_to_list 3 lần]`  
F5 trên Trello: Cả 3 thẻ việc đã nằm gọn trong cột đầu tiên mà tôi không cần gõ một chữ nào trên web!

#### Nhịp 3 — Chỉnh sửa chi tiết: Đổi tên [KHẨN] & Gắn deadline
Khi có việc phát sinh gấp, tôi lệnh cho AI sửa trực tiếp:
> *'3. Chỉnh sửa thẻ "Chốt báo giá thiết bị văn phòng": Đổi tên thành "[KHẨN] Chốt báo giá thiết bị văn phòng", cập nhật mô tả là "Cần duyệt trước 17h hôm nay để kịp đặt hàng" và gắn hạn chót là ngày mai.'*

`[Enter — AI gọi update_card_details]`  
Quay sang Trello: Tiêu đề, mô tả và ngày hết hạn tự động cập nhật ngay tức thì!

#### Nhịp 4 — Sắp xếp thứ tự ưu tiên & Di chuyển thẻ giữa các cột
Tiếp theo, tôi yêu cầu AI điều phối lại trạng thái:
> *'4. Sắp xếp thẻ "[KHẨN] Chốt báo giá thiết bị văn phòng" lên vị trí trên cùng của cột, đồng thời chuyển thẻ "Soạn dự thảo hợp đồng thuê mặt bằng" sang cột "Đang Thực Hiện" và thẻ "Đặt vé máy bay công tác Đà Nẵng" sang cột "Hoàn Thành".'*

`[Enter — AI gọi move_card]`  
Nhìn trên Trello: Các thẻ tự động nhảy sang đúng cột và việc khẩn đã đứng đầu bảng!

#### Nhịp 5 — Cập nhật tiến độ bằng bình luận & checklist kiểm tra
Tôi tiếp tục giao thêm việc kiểm soát:
> *'5. Vào thẻ "Soạn dự thảo hợp đồng thuê mặt bằng", thêm một bình luận: "Đã gửi phòng pháp chế rà soát Điều 4, chờ phản hồi" và tạo checklist gồm 2 mục: Kiểm tra điều khoản cọc, Trình ký Giám đốc.'*

`[Enter — AI thêm comment và checklist vào đúng thẻ]`  
Bấm mở thẻ trên Trello: Bình luận và danh sách kiểm tra đã có sẵn y như một nhân viên thực thụ vừa cập nhật!"

---

### [03:15 - 05:15] 3 KỊCH BẢN ĐỘT PHÁ: THAO TÁC TAY "CHÀO THUA" SỨC MẠNH AI
`[Giọng hào hứng, đẩy cao trào]`

"Đến đây, bạn thấy AI đã thay bạn làm mọi thao tác bấm chuột.  
Nhưng nếu chỉ có vậy, bạn sẽ bảo: *'Tôi dùng chuột kéo thả trên web cũng nhanh vậy, gõ lệnh làm chi!'*  
Đúng vậy! Điểm khác biệt một trời một vực giữa **thao tác tay** và **sức mạnh AI** bắt đầu từ 3 kịch bản đột phá sau đây:

#### Nhịp 6 — Cú hích Skill: Biến văn bản thô cộc lốc thành Thẻ việc chuẩn Doanh nghiệp
Trong thực tế, nhân viên thường tạo task rất cẩu thả hoặc tốn 5–10 phút để copy template.  
Nhưng với Antigravity, chúng ta đã trang bị sẵn **Skill `trello-task-standardizer`** trong workspace.  
Bây giờ, tôi chỉ cần gõ một dòng văn bản thô lủng củng:
> *'6. Thêm thẻ Trello: làm hợp đồng thuê xe 29 chỗ chở nhân viên đi du lịch hè, ngân sách dưới 15 triệu, liên hệ 3 nhà xe, xong trước thứ 5.'*

`[Enter — AI kích hoạt Skill chuẩn hóa kết hợp Trello MCP]`  
Và hãy nhìn thẻ mới xuất hiện trên Trello:  
* Tiêu đề tự động chuẩn hóa: `[HÀNH CHÍNH] Ký hợp đồng thuê xe du lịch hè 29 chỗ`.  
* Mô tả tự động chia mục chuyên nghiệp: 🎯 **Mục tiêu rõ ràng** | 👤 **Hạn chót thứ 5** | 📋 **Checklist 4 bước hành động cụ thể** | ✅ **Tiêu chí nghiệm thu (DoD)** | ⚠️ **Ràng buộc ngân sách dưới 15 triệu**.  
Thao tác tay mất 10 phút để gõ định dạng này; AI làm chuẩn chỉ trong đúng 3 giây!

#### Nhịp 7 — Cầu nối đa nguồn: Biến file ghi chú cuộc họp lộn xộn trên máy tính thành loạt thẻ Trello
Sau cuộc họp giao ban, bạn có file `ghi_chu_cuoc_hop_tho.txt` lưu trên máy với hàng loạt đầu việc lộn xộn của các phòng ban.  
Nếu làm bằng tay, bạn phải mở file một bên, mở Trello một bên, copy-paste từng dòng rất dễ bỏ sót.  
Với Antigravity, tôi chỉ ra đúng 1 lệnh:
> *'7. Đọc tệp ghi chú cuộc họp "ghi_chu_cuoc_hop_tho.txt" trong thư mục này: tự động bóc tách các đầu việc của từng phòng ban, phân loại việc khẩn đưa lên đầu và nạp thành các thẻ việc ngay ngắn vào cột "Cần Làm"!'*

`[Enter — AI đọc file local, phân tích ngữ nghĩa và đẩy 3 thẻ việc lên Trello]`  
Quay sang Trello bấm F5: Cả 3 thẻ việc của Hành chính (thuê xe Ba Vì), Kế toán (hóa đơn VAT Digiworld) và Nhân sự (tuyển dụng chuyên viên AI) đã tự động mọc ra ngay ngắn! Đây là sức mạnh độc quyền: **Vừa đọc file trong máy, vừa có trí tuệ bóc tách, vừa đẩy thẳng lên đám mây Trello!**

#### Nhịp 8 — Trợ lý kiểm toán & Quét báo cáo tiến độ thông minh
Cuối tuần cần rà soát dự án, thay vì phải click mở từng thẻ kiểm tra ngày tháng, tôi ra lệnh cho AI đóng vai trò người quản lý:
> *'8. Hãy quét toàn bộ bảng "Vận Hành Văn Phòng Q4": thẻ nào có chữ [KHẨN] hoặc deadline trong hôm nay thì tự gắn nhãn Đỏ và thêm bình luận nhắc nhở tiến độ. Sau đó, lập bảng Markdown tóm tắt tiến độ toàn bộ dự án.'*

`[Enter — AI quét bảng, gắn nhãn cảnh báo và xuất bảng Markdown]`  
Ngay tức thì, toàn bộ bảng việc được kiểm toán và một báo cáo tiến độ chỉn chu hiện lên trong Antigravity:

| Cột Trạng Thái | Thẻ Công Việc | Đánh Giá Tiến Độ / Cảnh Báo |
| :--- | :--- | :--- |
| **Cần Làm (To Do)** | `[KHẨN] Chốt báo giá thiết bị văn phòng` | 🔴 Nhãn Đỏ • Deadline hôm nay • Đã gửi nhắc nhở |
| **Cần Làm (To Do)** | `[HÀNH CHÍNH] Ký hợp đồng thuê xe 29 chỗ` | Chuẩn hóa theo Skill • Hạn chót thứ 5 |
| **Cần Làm (To Do)** | `[KẾ TOÁN] Rà soát hóa đơn VAT Digiworld` | Bóc tách từ ghi chú họp • Hạn trước ngày 20 |
| **Cần Làm (To Do)** | `[NHÂN SỰ] Tuyển dụng chuyên viên AI` | Bóc tách từ ghi chú họp • Duyệt JD chiều mai |
| **Đang Thực Hiện** | `Soạn dự thảo hợp đồng thuê mặt bằng` | Đã có bình luận pháp chế & 2 checklist |
| **Hoàn Thành** | `Đặt vé máy bay công tác Đà Nẵng` | Đã xong toàn bộ thủ tục |

Một chu trình hoàn hảo mà không một thao tác thủ công nào có thể sánh kịp!"

---

### [05:15 - 06:00] TỔNG KẾT BÀI & CẦU NỐI SANG PHẦN 8 (PLUGINS & AUTOMATIONS)
`[Chỉ dòng Footer Bar trên Slide 2: Safe & Powerful Integration]`

"**Bạn thấy đấy, đó mới chính là đẳng cấp thực sự của MCP:**  
Từ một tài khoản Trello hoàn toàn trống trơn, kết nối chỉ bằng 1 cú click chuột, bạn vừa làm chủ các thao tác thêm sửa cơ bản, vừa kết hợp với **Skill** để chuẩn hóa thẻ việc, bóc tách tài liệu từ máy tính và kiểm toán tiến độ tự động.

**Thế nhưng bây giờ bạn hãy hình dung:**  
Bạn đã có Rules (nội quy), Skills (tay nghề), Hooks (chốt an toàn), và MCP (cổng kết nối). Nếu mỗi lần sang một máy tính mới hoặc muốn chia sẻ bộ công cụ này cho đồng nghiệp, bạn lại phải đi copy từng file thì rất mất thời gian.

**Làm thế nào để đóng gói toàn bộ kho vũ khí này thành 1 chiếc vali duy nhất, chỉ cần cài 1 click là có đủ?**  
Và làm thế nào để có một **'Trợ lý tàng hình'** chạy ngầm 24/7 để giám sát và nhắc việc tự động cho bạn?

Chào mừng bạn bước sang **Phần 8: Trụ Cột 6 & 7 — Plugins & Automations**!  
Hẹn gặp lại bạn ở Bài 8.1 ngay sau đây!"
