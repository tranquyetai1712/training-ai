# KỊCH BẢN LỜI THOẠI BÀI HỌC 7.2
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 2:** Kho Vũ Khí 7 Trụ Cột Cho Dân Văn Phòng  
**Phần 7:** Trụ Cột 5 — MCP: Cổng Kết Nối Đưa Dữ Liệu Công Việc Thực Tế Vào AI  
**Tên bài:** Bài 7.2: Thực hành: Kết nối cổng Gmail MCP — Biến AI thành thư ký tự động quét & tóm tắt email công việc quan trọng  
**Thời lượng dự kiến:** 04:30 (Chuẩn Udemy Micro-Learning • Live Cloud Integration)  
**Slide tương ứng:** `phan_07_tru_cot_mcp.html` (Slide 2)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_07_tru_cot_mcp.html` (Slide 2: Thực Hành: Kết Nối Cổng Gmail MCP).
* **Môi trường thực hành:** Mở Antigravity Desktop tại workspace độc lập `slides/Demo/ket-noi-mcp-gmail/` đã có sẵn file cấu hình `mcp_config.json` và sổ tay `HUONG_DAN_KET_NOI_GMAIL_MCP.md`.
* **Trạng thái cổng kết nối:** Cổng `gmail` MCP server hiển thị trạng thái đã kết nối (*Connected*).
* **Tông giọng:** Phấn khích, thực tế, nhấn mạnh sự tiện lợi vượt bậc khi không còn phải tự mình mở hàng chục email để đọc thủ công.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD LEAN SCRIPT)

### [00:00 - 00:45] NỖI ÁM ẢNH HỘP THƯ GMAIL QUÁ TẢI MỖI SÁNG
`[Slide 2: Thực Hành: Kết Nối Cổng Gmail MCP]`  
`[Mở Antigravity Desktop tại workspace slides/Demo/ket-noi-mcp-gmail/]`  
`[Chỉ vào biểu tượng cổng kết nối Gmail MCP đã sẵn sàng trên màn hình]`

"Chào mừng bạn đến với Bài 7.2!

Hãy tưởng tượng một buổi sáng thứ Hai điển hình của bạn:  
Bạn vừa mở máy tính lên, hòm thư Gmail đã báo hơn 50 email chưa đọc: Nào là thư quảng cáo, thông báo hệ thống, thư đối tác gửi báo giá, khách hàng hỏi hợp đồng...  
Trước đây, bạn sẽ phải làm gì? Ngồi lướt từng email, mở từng thư lên đọc lướt xem có việc gì gấp không. Vừa mất cả tiếng đồng hồ, vừa mỏi mắt và rất dễ bỏ sót những email quan trọng của sếp hay đối tác lớn!

**Thế nhưng hôm nay, với Cổng kết nối Gmail MCP,** chúng ta sẽ giao phó toàn bộ công việc này cho trợ lý AI: Tự động lướt hòm thư và lọc ra những việc khẩn cấp chỉ trong chưa đầy 30 giây!"

---

### [00:45 - 01:50] KHÁM PHÁ CỔNG GMAIL MCP TRONG MCP_CONFIG.JSON
`[Chỉ khung CẤU HÌNH MCP trên Slide 2]`  
`[Mở tệp mcp_config.json trong workspace demo]`

"Các bạn hãy nhìn vào tệp `mcp_config.json` trong workspace demo trên màn hình của tôi:  
Toàn bộ bí quyết chỉ nằm ở một khối cấu hình cực kỳ gọn gàng:

```json
{
  "mcpServers": {
    "gmail": {
      "command": "npx",
      "args": ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
    }
  }
}
```

Đoạn khai báo này có nghĩa là gì? Nó đóng vai trò như một **chiếc thẻ thông hành**:  
*'Này Antigravity, tôi cho phép bạn kết nối với hòm thư Gmail của tôi để thực thi các tác vụ tìm kiếm, đọc thư và phân loại khi tôi yêu cầu.'*

Ngay khi bạn lưu file này và đăng nhập cấp quyền một lần duy nhất, Antigravity Desktop sẽ tự động nhận diện các công cụ chuyên dụng: `search_emails`, `read_email` và `draft_email` mà bạn không cần phải viết bất kỳ một dòng mã lập trình nào!"

---

### [01:50 - 03:45] THAO TÁC THỰC CHIẾN: AI TỰ ĐỘNG QUÉT & LẬP BẢNG TÓM TẮT EMAIL
`[Chuyển màn hình sang khung chat Antigravity Desktop]`  
`[Thao tác gõ câu lệnh tự nhiên và nhấn Enter]`

"Bây giờ, chúng ta hãy cùng nhau ra lệnh cho trợ lý AI nhé!  
Tại khung chat, tôi chỉ cần gõ đúng một câu lệnh tự nhiên:

> *'Hãy sử dụng kết nối Gmail MCP kiểm tra các email gửi đến trong 24 giờ qua. Lọc ra những thư có chứa từ khóa \"Báo giá\" hoặc \"Hợp đồng\", và lập bảng tóm tắt: Người gửi, Tiêu đề, Thời gian và Tóm tắt yêu cầu chính giúp tôi.'*

`[Nhấn Enter và cùng học viên quan sát AI tác chiến]`  
Ngay tức thì, bạn hãy nhìn vào luồng xử lý trên màn hình:
* Bước 1: AI kích hoạt công cụ `search_emails`, tự động tìm kiếm trên hòm thư Gmail với bộ lọc thời gian và từ khóa.
* Bước 2: Nó gọi công cụ `read_email` để đọc nội dung của 3 bức thư quan trọng nhất.
* Bước 3: `[Chỉ vào bảng kết quả xuất hiện bên phải]`  
  Một bảng Markdown cực kỳ ngăn nắp hiện ra ngay lập tức:

| STT | Người Gửi | Tiêu Đề Thư | Thời Gian | Tóm Tắt Yêu Cầu Chính |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `nguyen.hoa@abctech.vn` | Báo giá phần mềm kế toán Q4 | 08:15 Sáng | Gửi bảng giá gói Enterprise 45 triệu, xin phản hồi trước 17h. |
| 2 | `phapche@doitacxyz.com` | Dự thảo Hợp đồng thuê văn phòng | 09:30 Sáng | Điều chỉnh Điều 4 về tiến độ thanh toán đợt 2, chờ sếp ký. |
| 3 | `ketoan@congty.com` | Yêu cầu đối chiếu hóa đơn VAT | 10:05 Sáng | Nhắc gửi biên bản nghiệm thu trước ngày 31/10 để thanh toán. |

Toàn bộ 50 email lộn xộn đã được thu gọn thành đúng 3 dòng việc gấp cần xử lý!"

---

### [03:45 - 04:30] TỔNG KẾT BÀI & CẦU NỐI SANG PHẦN 8 (PLUGINS & SIDECARS)
`[Chỉ dòng Footer Bar trên Slide 2: Safe & Powerful Integration]`

"**Bạn thấy đấy, sức mạnh của MCP thực sự mang tính cách mạng:**  
Từ một trợ lý AI chỉ biết ngồi một chỗ trong máy tính, giờ đây nó đã có thể vươn tay ra thế giới dịch vụ đám mây bên ngoài để giải quyết trọn vẹn công việc hàng ngày cho bạn.

**Thế nhưng bây giờ bạn hãy hình dung:**  
Bạn đã có Rules (nội quy), Skills (tay nghề), Hooks (chốt an toàn), và MCP (cổng kết nối). Nếu mỗi lần sang một máy tính mới hoặc muốn chia sẻ bộ công cụ này cho đồng nghiệp, bạn lại phải đi copy từng file thì rất mất thời gian.

**Làm thế nào để đóng gói toàn bộ kho vũ khí này thành 1 chiếc vali duy nhất, chỉ cần cài 1 click là có đủ?**  
Và làm thế nào để có một **'Trợ lý tàng hình'** chạy ngầm 24/7 để giám sát và nhắc việc tự động cho bạn?

Chào mừng bạn bước sang **Phần 8: Trụ Cột 6 & 7 — Plugins & Sidecars**!  
Hẹn gặp lại bạn ở Bài 8.1 ngay sau đây!"
