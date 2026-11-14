# KỊCH BẢN LỜI THOẠI BÀI HỌC 7.2
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 2:** Kho Vũ Khí 7 Trụ Cột Cho Dân Văn Phòng  
**Phần 7:** Trụ Cột 5 — MCP: Cổng Kết Nối Đưa Dữ Liệu Công Việc Thực Tế Vào AI  
**Tên bài:** Bài 7.2: Thực hành: Kết nối cổng Trello MCP — Dựng bảng, thêm sửa, sắp xếp công việc từ con số 0 chỉ bằng câu lệnh  
**Thời lượng dự kiến:** 05:30 (Chuẩn Udemy Micro-Learning • Live Zero-to-Hero Integration)  
**Slide tương ứng:** `phan_07_tru_cot_mcp.html` (Slide 2)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_07_tru_cot_mcp.html` (Slide 2: Thực Hành: Kết Nối Cổng Trello MCP).
* **Môi trường thực hành:** Mở Antigravity Desktop tại workspace độc lập `slides/Demo/ket-noi-mcp-trello/` đã có sẵn file `mcp_config.json` và sổ tay `HUONG_DAN_KET_NOI_TRELLO_MCP.md`.
* **Trình duyệt đối chứng:** Mở sẵn tab Trello với một tài khoản/không gian làm việc **trống hoàn toàn (chưa có bảng, chưa có cột, chưa có thẻ nào)** để học viên thấy rõ sự "biến hình" từ con số 0.
* **Trạng thái cổng kết nối:** Cổng `trello` MCP server hiển thị trạng thái đã kết nối (*Connected*).
* **Tông giọng:** Hào hứng, bất ngờ, nhấn mạnh cảm giác "chỉ ngồi yên tại Antigravity ra lệnh bằng tiếng Việt, không cần đụng tay vào giao diện Trello".

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD LEAN SCRIPT)

### [00:00 - 00:50] TÀI KHOẢN TRELLO TRỐNG TRƠN & LÝ DO CHỌN TRELLO MCP
`[Slide 2: Thực Hành: Kết Nối Cổng Trello MCP]`  
`[Chiếu nhanh tab trình duyệt Trello đang trống hoàn toàn, chưa có bảng hay thẻ nào]`  
`[Chuyển sang Antigravity Desktop tại workspace slides/Demo/ket-noi-mcp-trello/]`

"Chào mừng bạn đến với Bài 7.2!

Trước khi bắt đầu, có một điểm rất hay bạn cần biết: Với các dịch vụ như Gmail hay Google Drive, Google Antigravity đã tích hợp sẵn **Plugin mặc định** để bạn bật lên dùng ngay. Vì vậy, để trải nghiệm đúng sức mạnh tự cắm cổng MCP tùy chỉnh cho một phần mềm bên ngoài, hôm nay chúng ta sẽ kết nối với **Trello**!

Và hãy nhìn màn hình Trello của tôi lúc này: **Hoàn toàn mới tinh, trống trơn chưa có bất kỳ một bảng, một cột hay một chiếc thẻ nào cả!**  
Tôi sẽ không bấm nút *Create Board*, không gõ tay từng cột, cũng không kéo thả chuột trên web Trello.  
Từ giờ trở đi, tôi chỉ ngồi nguyên ở khung chat **Antigravity** và gõ đúng 6 câu lệnh tự nhiên để xem trợ lý AI tự dựng cả hệ thống công việc từ con số 0 ra sao nhé!"

---

### [00:50 - 01:45] KHÁM PHÁ CỔNG TRELLO MCP TRONG MCP_CONFIG.JSON
`[Chỉ khung CẤU HÌNH MCP trên Slide 2]`  
`[Mở tệp mcp_config.json trong workspace demo]`

"Bí quyết chỉ nằm gọn trong tệp `mcp_config.json` tại workspace demo trên màn hình:

```json
{
  "mcpServers": {
    "trello": {
      "command": "npx",
      "args": ["-y", "@delorenj/mcp-server-trello"],
      "env": {
        "TRELLO_API_KEY": "<API_KEY>",
        "TRELLO_TOKEN": "<TOKEN>"
      }
    }
  }
}
```

Bạn chỉ cần lấy `API_KEY` và `TOKEN` tại trang `trello.com/app-key` dán vào đây. Ngay lập tức, Antigravity được trao trọn bộ quyền năng thao tác từ **tạo bảng, tạo cột, thêm thẻ, chỉnh sửa, sắp xếp vị trí cho đến chuyển trạng thái** trên Trello!"

---

### [01:45 - 04:45] THỰC CHIẾN 6 NHỊP LIÊN HOÀN: TỪ CON SỐ 0 ĐẾN BẢNG VIỆC HOÀN CHỈNH
`[Chuyển màn hình sang khung chat Antigravity Desktop, để chế độ chia đôi hoặc chuyển qua lại nhanh với tab Trello]`

"Bây giờ, bạn hãy theo dõi chuỗi **6 câu lệnh thực chiến** ngay tại khung chat Antigravity:

#### Nhịp 1 — Khởi tạo bảng & dựng cấu trúc cột từ trang giấy trắng
Tôi gõ lệnh đầu tiên:
> *'1. Dùng Trello MCP tạo cho tôi một bảng mới tên \"Vận Hành Văn Phòng Q4\", bên trong tạo 3 cột theo đúng thứ tự: \"Cần Làm (To Do)\", \"Đang Thực Hiện\" và \"Hoàn Thành\".'*

`[Enter — AI gọi create_board và add_list_to_board]`  
Xong trong 3 giây! Sang tab Trello bấm F5: Bảng mới cùng 3 cột ngay ngắn đã mọc ra!

#### Nhịp 2 — Thêm mới hàng loạt 5 thẻ công việc
Tiếp tục ngay trong khung chat, tôi ra lệnh thêm thẻ:
> *'2. Thêm giúp tôi 5 thẻ công việc vào cột \"Cần Làm (To Do)\": (1) Chốt báo giá thiết bị văn phòng, (2) Soạn dự thảo hợp đồng thuê mặt bằng, (3) Đối chiếu hóa đơn VAT tháng 10, (4) Lên lịch họp giao ban đầu tuần, (5) Đặt vé máy bay công tác Đà Nẵng — kèm mô tả ngắn cho từng thẻ.'*

`[Enter — AI gọi add_card_to_list 5 lần liên tiếp]`  
F5 trên Trello: Cả 5 thẻ việc kèm phần mô tả chi tiết đã nằm gọn trong cột đầu tiên mà tôi không cần gõ một chữ nào trên web!

#### Nhịp 3 — Chỉnh sửa nội dung, gắn mức độ ưu tiên & hạn chót
Bây giờ có việc phát sinh gấp, tôi lệnh cho AI sửa trực tiếp:
> *'3. Chỉnh sửa thẻ \"Chốt báo giá thiết bị văn phòng\": Đổi tên thành \"[KHẨN] Chốt báo giá thiết bị văn phòng\", cập nhật mô tả là \"Cần duyệt trước 17h hôm nay để kịp đặt hàng\" và gắn hạn chót (deadline) là ngày mai.'*

`[Enter — AI gọi update_card_details]`  
Quay sang Trello: Tiêu đề, mô tả và ngày hết hạn tự động đổi ngay lập tức!

#### Nhịp 4 — Sắp xếp thứ tự ưu tiên & di chuyển thẻ giữa các cột
Tiếp theo, tôi yêu cầu AI điều phối lại trạng thái và thứ tự thẻ:
> *'4. Sắp xếp thẻ \"[KHẨN] Chốt báo giá thiết bị văn phòng\" lên vị trí trên cùng của cột, đồng thời di chuyển thẻ \"Soạn dự thảo hợp đồng thuê mặt bằng\" sang cột \"Đang Thực Hiện\" và thẻ \"Đặt vé máy bay công tác Đà Nẵng\" sang cột \"Hoàn Thành\".'*

`[Enter — AI gọi move_card và cập nhật vị trí thẻ]`  
Nhìn trên Trello lúc này: Các thẻ tự động nhảy sang đúng cột tương ứng và thẻ khẩn đã đứng đầu bảng!

#### Nhịp 5 — Cập nhật tiến độ bằng bình luận / checklist ngay trong thẻ
Tôi tiếp tục giao thêm chi tiết kiểm tra:
> *'5. Vào thẻ \"Soạn dự thảo hợp đồng thuê mặt bằng\", thêm một bình luận ghi chú: \"Đã gửi phòng pháp chế rà soát Điều 4, chờ phản hồi\" và tạo checklist gồm 2 mục: Kiểm tra điều khoản cọc, Trình ký Giám đốc.'*

`[Enter — AI thêm comment và checklist vào đúng thẻ]`  
Bấm mở thẻ trên Trello ra xem thử: Bình luận và danh sách checklist đã có sẵn y như một nhân viên thực thụ vừa cập nhật!

#### Nhịp 6 — Quét toàn bộ bảng & xuất báo cáo tổng hợp
Cuối cùng, sau khi mọi thứ đã vận hành trơn tru, tôi ra lệnh chốt sổ:
> *'6. Hãy quét lại toàn bộ bảng \"Vận Hành Văn Phòng Q4\" và lập cho tôi một bảng Markdown tóm tắt trạng thái từng thẻ việc theo từng cột.'*

`[Enter — AI gọi get_lists & get_cards_by_list_id, xuất bảng Markdown gọn gàng]`  
Toàn bộ bảng báo cáo hiện lên ngay trong Antigravity:

| Cột Trạng Thái | Tên Thẻ Công Việc | Ghi Chú / Trạng Thái |
| :--- | :--- | :--- |
| **Cần Làm (To Do)** | `[KHẨN] Chốt báo giá thiết bị văn phòng` | Đã xếp đầu cột • Deadline ngày mai |
| **Cần Làm (To Do)** | `Đối chiếu hóa đơn VAT tháng 10` | Chờ kế toán xử lý |
| **Cần Làm (To Do)** | `Lên lịch họp giao ban đầu tuần` | Chuẩn bị phòng họp & tài liệu |
| **Đang Thực Hiện** | `Soạn dự thảo hợp đồng thuê mặt bằng` | Đã có bình luận pháp chế & 2 checklist |
| **Hoàn Thành** | `Đặt vé máy bay công tác Đà Nẵng` | Đã chuyển sang cột Hoàn Thành |

Thậm chí trong thực tế, bạn có thể **gộp cả 6 yêu cầu này vào chung 1 câu lệnh duy nhất**, AI cũng tự làm tuần tự từ A đến Z cho bạn mà bạn không cần rời khỏi màn hình Antigravity!"

---

### [04:45 - 05:30] TỔNG KẾT BÀI & CẦU NỐI SANG PHẦN 8 (PLUGINS & SIDECARS)
`[Chỉ dòng Footer Bar trên Slide 2: Safe & Powerful Integration]`

"**Bạn thấy đấy, đó mới chính là đẳng cấp thực sự của MCP:**  
Từ một tài khoản Trello hoàn toàn trống trơn, bạn chỉ cần ngồi ở Antigravity ra lệnh tự nhiên để **tạo mới, chỉnh sửa, sắp xếp, chuyển cột và báo cáo** — biến AI thành người điều phối dự án thực thụ.

**Thế nhưng bây giờ bạn hãy hình dung:**  
Bạn đã có Rules (nội quy), Skills (tay nghề), Hooks (chốt an toàn), và MCP (cổng kết nối). Nếu mỗi lần sang một máy tính mới hoặc muốn chia sẻ bộ công cụ này cho đồng nghiệp, bạn lại phải đi copy từng file thì rất mất thời gian.

**Làm thế nào để đóng gói toàn bộ kho vũ khí này thành 1 chiếc vali duy nhất, chỉ cần cài 1 click là có đủ?**  
Và làm thế nào để có một **'Trợ lý tàng hình'** chạy ngầm 24/7 để giám sát và nhắc việc tự động cho bạn?

Chào mừng bạn bước sang **Phần 8: Trụ Cột 6 & 7 — Plugins & Sidecars**!  
Hẹn gặp lại bạn ở Bài 8.1 ngay sau đây!"
