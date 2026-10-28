# KỊCH BẢN LỜI THOẠI BÀI HỌC 7.2
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 2:** Kho Vũ Khí 7 Trụ Cột Cho Dân Văn Phòng  
**Phần 7:** Trụ Cột 5 — MCP: Cổng Kết Nối Đưa Dữ Liệu Công Việc Thực Tế Vào AI  
**Tên bài:** Bài 7.2: Thực hành: Cho phép AI kết nối thư mục hồ sơ để tự tìm kiếm & đối chiếu dữ liệu  
**Thời lượng dự kiến:** 12:00  
**Slide tương ứng:** `phan_07_tru_cot_mcp.html` (Slide 2)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_07_tru_cot_mcp.html` (Slide 16).
* **Thư mục mẫu ngoài dự án:** Chuẩn bị sẵn một thư mục riêng biệt tại đường dẫn `D:/Kho_Hop_Dong_2026/` chứa tệp `hop_dong_cong_ty_abc.pdf`.
* **Cấu hình MCP:** Tệp `mcp_config.json` đã khai báo quyền truy cập tới thư mục lưu trữ ngoài này.
* **Tông giọng:** Thực tế, cuốn hút, nhấn mạnh sự tiện lợi vượt bậc khi không còn phải làm thao tác thủ công copy file giữa các ổ đĩa.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD SCRIPT)

### [00:00 - 01:30] MỞ ĐẦU: BÀI TOÁN "TÀI LIỆU NẰM RẢI RÁC Ở NHIỀU Ổ ĐĨA"
`[Hiển thị Slide 2: Thực Hành MCP: Đọc Thư Mục Hợp Đồng Cục Bộ]`  
`[Tông giọng đồng cảm, đưa ra tình huống văn phòng điển hình]`

"Chào mừng các bạn đến với Bài 7.2!

Hãy tưởng tượng một tình huống rất quen thuộc trong công việc hàng ngày:  
Bạn đang làm việc trong thư mục dự án `Thang_10` trên màn hình Antigravity. Bạn có một bảng kê công nợ khách hàng cần thanh toán.  
Thế nhưng, tệp hợp đồng kinh tế gốc của đối tác 'Công ty ABC' lại không nằm ở đây, mà nó đang nằm ở tít trong ổ đĩa `D:/Kho_Hop_Dong_2026/` của công ty.

Trước đây, bạn sẽ phải làm gì?  
Mở cửa sổ File Explorer lên, gõ tìm kiếm, tìm được file PDF rồi copy nó, dán vào thư mục dự án, rồi mới tải lên cho AI đọc. Rất lích kích và làm nhân bản rác file khắp máy tính!  
Nhưng hôm nay, với **Cổng kết nối MCP**, chúng ta sẽ cho phép AI tự động vươn tay sang ổ đĩa khác để đọc và đối chiếu hợp đồng chỉ trong một nốt nhạc!"

---

### [01:30 - 04:30] BƯỚC 1: KHAI BÁO CỔNG KẾT NỐI MCP TRONG MCP_CONFIG.JSON
`[Chuyển màn hình sang Antigravity Desktop]`  
`[Mở tệp mcp_config.json]`

"Các bạn hãy nhìn vào tệp `mcp_config.json` trên màn hình của tôi:  
Chúng ta chỉ cần khai báo một khối thông tin cực kỳ ngắn gọn thế này:

```json
{
  "mcpServers": {
    "kho_tai_lieu": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "D:/Kho_Hop_Dong_2026"]
    }
  }
}
```

`[Giải thích bằng ngôn ngữ bình dân]`  
Đoạn khai báo này có nghĩa là gì?  
Nó đơn giản là một chiếc giấy phép thông hành:  
*'Này Antigravity, tôi cấp cho bạn một chiếc cổng USB mang tên `kho_tai_lieu`. Cổng này cho phép bạn được quyền đọc các tệp tin lưu tại thư mục `D:/Kho_Hop_Dong_2026` trên máy tính của tôi!'*

Ngay khi bạn lưu file này lại, Antigravity Desktop sẽ tự động kích hoạt chiếc cổng cắm này ngầm bên dưới mà bạn không cần phải khởi động lại máy tính!"

---

### [04:30 - 08:30] BƯỚC 2: RA LỆNH CHO AI TỰ VƯƠN TAY ĐỌC FILE TỪ XA
`[Bấm nút New Task trong Antigravity Desktop]`  
`[Gõ câu lệnh đối chiếu vào khung chat]`

"Bây giờ, chúng ta hãy cùng nhau ra lệnh nhé:

> *'Chào Antigravity, trong bảng tính thanh toán hiện tại của tôi có khoản chi 50 triệu đồng cho Công ty ABC.*  
> *Hãy sử dụng kết nối MCP để truy cập vào kho hợp đồng `D:/Kho_Hop_Dong_2026`, tìm tệp hợp đồng của Công ty ABC, đọc kỹ điều khoản thanh toán và đối chiếu xem con số 50 triệu này có đúng theo tiến độ đợt 2 quy định trong hợp đồng hay không?'*

`[Nhấn phím Enter dứt khoát]`  
Các bạn hãy quan sát luồng thực thi của AI!

`[Chỉ chuột vào từng bước AI gọi công cụ MCP]`  
* Bước 1: AI gọi công cụ `mcp_kho_tai_lieu_search_files`: Nó tự động quét ổ D và tìm thấy file `hop_dong_cong_ty_abc.pdf`.
* Bước 2: Nó gọi công cụ `mcp_kho_tai_lieu_read_file`: Nó tự động mở file PDF từ xa ra đọc mà **hoàn toàn không cần copy file đó vào thư mục hiện tại**!
* Bước 3: Nó lật tới Điều 4 — Điều khoản thanh toán: Phát hiện hợp đồng ghi rõ 'Đợt 2 thanh toán 30% giá trị hợp đồng, tương đương 50.000.000 VNĐ sau khi nghiệm thu giai đoạn 1'.
* Bước 4: `[Bảng đối chiếu xuất hiện ở cửa sổ bên phải]`  
  AI xuất ra một bảng đối chiếu cực kỳ đẹp mắt:

| Hạng Mục | Số Tiền Trên Bảng Kê | Quy Định Trong Hợp Đồng Gốc | Kết Quả Đối Chiếu |
| :--- | :---: | :---: | :---: |
| Thanh toán đợt 2 Công ty ABC | 50.000.000 VNĐ | 50.000.000 VNĐ (Điều 4.2) | ✅ **HOÀN TOÀN KHỚP** |

Và nó còn kèm theo trích dẫn chính xác số trang hợp đồng cho bạn kiểm chứng!"

---

### [08:30 - 12:00] TỔNG KẾT BÀI & CÂU DẪN SANG TRỤ CỘT 6 & 7: PLUGINS & SIDECARS
`[Quay lại màn hình camera, tươi cười hài lòng]`

"Các bạn thấy sức mạnh của MCP khủng khiếp như thế nào chưa?  
Dữ liệu của bạn có thể nằm ở bất kỳ đâu — trên ổ cứng máy tính, trên Google Drive hay trong hòm thư — chỉ cần một cổng cắm MCP, trợ lý AI sẽ tự động tìm kiếm, đối chiếu và phục vụ bạn chu đáo từ A đến Z!

Nhưng bây giờ hãy tưởng tượng:  
Bạn đã có Rules (nội quy), bạn có Skills (tay nghề), bạn có Hooks (chốt chặn an toàn), bạn có MCP (cổng kết nối).  
Nếu mỗi lần bạn sang một máy tính mới, hoặc bạn muốn chia sẻ toàn bộ bộ công cụ tuyệt vời này cho đồng nghiệp trong phòng ban, chẳng lẽ bạn lại phải đi copy từng file một gửi cho họ?  
Làm thế nào để **đóng gói tất cả thành 1 chiếc vali duy nhất**, đồng nghiệp chỉ cần bấm 1 click chuột là có ngay trọn bộ vũ khí?

Và làm thế nào để có một **'Trợ lý tàng hình'** chạy ngầm 24/7 để giám sát và nhắc việc cho bạn?

Chào mừng các bạn đến với **Phần 8: Trụ Cột 6 & 7 — Plugins & Sidecars — Chiếc Vali Đóng Gói All-in-One & Trợ Lý Tàng Hình**!  
Hẹn gặp lại các bạn ở Bài 8.1 ngay sau đây!"
