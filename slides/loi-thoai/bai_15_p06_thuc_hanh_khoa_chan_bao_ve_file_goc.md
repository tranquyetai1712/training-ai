# KỊCH BẢN LỜI THOẠI BÀI HỌC 6.2
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 2:** Kho Vũ Khí 7 Trụ Cột Cho Dân Văn Phòng  
**Phần 6:** Trụ Cột 4 — Hooks: Vòng Kim Cô Bảo Vệ An Toàn Dữ Liệu Tuyệt Đối  
**Tên bài:** Bài 6.2: Thực hành: Cài chốt chặn PreToolUse ngăn AI sửa đè file gốc  
**Thời lượng dự kiến:** 12:00  
**Slide tương ứng:** `phan_06_tru_cot_hooks.html` (Slide 2)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_06_tru_cot_hooks.html` (Slide 14).
* **Thư mục thực hành:** Chuẩn bị sẵn một tệp tính mẫu mang tên `du_lieu_goc_khach_hang.xlsx` trong thư mục làm việc.
* **Cấu hình Hook:** Đảm bảo file cấu hình Hook bảo vệ tệp gốc đã sẵn sàng để demo hành động chặn.
* **Tông giọng:** Hồi hộp, kịch tính khi thực hiện thử nghiệm ra lệnh nguy hiểm, sau đó chuyển sang thở phào nhẹ nhõm và phấn khích khi hệ thống tự động ngăn chặn thành công.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD SCRIPT)

### [00:00 - 01:30] MỞ ĐẦU: THỬ NGHIỆM TÌNH HUỐNG NGUY HIỂM NHẤT TRONG CÔNG TY
`[Hiển thị Slide 2: Thực Hành: Cài Đặt Hook Chặn Xóa Dữ Liệu]`  
`[Tông giọng hồi hộp, gợi cảm giác thử nghiệm mạo hiểm]`

"Chào mừng các bạn đến với Bài 6.2!

Hôm nay, tôi muốn cùng các bạn làm một việc mà trong công ty bình thường không ai dám làm:  
**Cố tình ra lệnh cho trợ lý AI phá hủy dữ liệu gốc!**

Hãy nhìn vào màn hình của tôi: Trong thư mục làm việc đang có một tệp tính cực kỳ quan trọng mang tên `du_lieu_goc_khach_hang.xlsx`. Đây là danh sách toàn bộ khách hàng trung thành của công ty trong suốt 5 năm qua.  
Nếu một nhân viên thực tập lỡ tay mở file này ra và bấm nút Xóa (Delete) rồi nhấn Lưu đè lên, thì coi như toàn bộ dữ liệu biến mất vĩnh viễn!

Bây giờ, chúng ta hãy thử xem: Khi đã trang bị Trạm gác Hooks `PreToolUse`, Antigravity sẽ phản ứng ra sao trước một câu lệnh nguy hiểm như vậy nhé!"

---

### [01:30 - 05:00] BƯỚC 1: CỐ TÌNH RA LỆNH NGUY HIỂM TRÊN KHUNG CHAT
`[Chuyển màn hình sang Antigravity Desktop]`  
`[Bấm New Task, thao tác gõ vào khung chat]`

"Các bạn hãy nhìn vào khung chat:  
Tôi sẽ gõ một câu lệnh cực kỳ bất cẩn:

> *'Hãy mở tệp `du_lieu_goc_khach_hang.xlsx` ra, lọc và xóa bỏ toàn bộ những khách hàng nào chưa phát sinh đơn hàng trong tháng 10 này giúp tôi.'*

`[Nhấn phím Enter dứt khoát]`  
Các bạn hãy nín thở quan sát màn hình!

`[Chỉ chuột vào luồng suy nghĩ của AI xuất hiện cảnh báo]`  
1. Trợ lý AI nhận lệnh và bắt đầu khởi động công cụ chỉnh sửa tệp tin `edit_file`. Nó chuẩn bị ghi đè lên file `du_lieu_goc_khach_hang.xlsx`.
2. Nhưng ngay tại giây phút đó! Trước khi ngón tay của nó kịp chạm vào file, **Trạm gác Hook `PreToolUse` lập tức kích hoạt**!
3. `[Một thông báo màu đỏ viền vàng bật lên trên luồng thực thi]`  
   > ⛔ **[CẢNH BÁO AN NINH]: THAO TÁC BỊ CHẶN ĐỨNG!**  
   > *Tệp tin `du_lieu_goc_khach_hang.xlsx` chứa tiền tố `goc_`, thuộc danh sách tài sản được bảo vệ bất khả xâm phạm. Lệnh sửa đổi trực tiếp đã bị hủy bỏ.*"

---

### [05:00 - 08:30] BƯỚC 2: AI TỰ ĐỘNG "QUAY ĐẦU LÀ BỜ" ĐỂ BẢO VỆ DỮ LIỆU
`[Tông giọng phấn khích, chỉ vào phản ứng thông minh của AI]`

"Các bạn hãy nhìn xem phản ứng thông minh của trợ lý AI sau khi bị Hook chặn lại:  
Nó không hề bị đơ máy hay báo lỗi crash ứng dụng. Nó tự đọc dòng thông báo chặn của Hook và tự nói với chính mình:  
*'Thao tác chỉnh sửa file gốc đã bị hệ thống an ninh ngăn chặn để bảo vệ dữ liệu.'*

Và ngay lập tức, AI quay sang nhắn tin cho tôi cực kỳ nhã nhặn:  
> *'Thưa bạn, tệp tin `du_lieu_goc_khach_hang.xlsx` là tệp dữ liệu gốc được bảo vệ an toàn. Tôi không được phép chỉnh sửa trực tiếp lên tệp này.*  
> *Để đáp ứng yêu cầu của bạn một cách an toàn nhất, tôi đề xuất tạo ra một bản sao mới mang tên `khach_hang_chua_mua_thang_10.xlsx` để trích xuất danh sách khách hàng riêng, giữ nguyên vẹn 100% dữ liệu gốc cho bạn. Bạn có đồng ý không?'*

`[Vỗ tay, tươi cười rạng rỡ]`  
Tuyệt vời trên cả tuyệt vời đúng không các bạn?  
Bạn thấy đấy: Trạm gác Hooks hoạt động như một phản xạ tự nhiên của cơ thể. Nó bảo vệ bạn khỏi chính những lúc bạn mệt mỏi, đãng trí hoặc lỡ tay gõ nhầm lệnh nguy hiểm!"

---

### [08:30 - 12:00] TỔNG KẾT BÀI & CÂU DẪN SANG TRỤ CỘT 5: MCP
`[Quay lại Slide 14, đúc kết ngắn gọn]`

"Qua bài thực hành vừa rồi, các bạn đã tận mắt chứng kiến tấm khiên sắt bảo vệ dữ liệu vững chắc như thế nào. Dù bất kỳ tình huống nào xảy ra, dữ liệu của bạn trên máy tính luôn an toàn tuyệt đối 100%.

Nhưng từ đầu khóa học đến giờ, trợ lý AI của chúng ta mới chỉ làm việc với các file nằm sẵn trong một thư mục nhỏ trên máy tính.  
Trong khi thực tế công việc hàng ngày của bạn:
* Dữ liệu bán hàng lại nằm trên bảng tính Google Sheet của công ty.
* Hàng trăm email quan trọng lại nằm trong hộp thư Gmail.
* Tin nhắn trao đổi công việc lại nằm trong nhóm chat Slack hay Zalo.

Làm thế nào để 'nối dài cánh tay' của AI ra thế giới bên ngoài, giúp nó tự mở hòm thư Gmail, tự đọc bảng tính online và tự gửi tin nhắn báo cáo cho đồng nghiệp?

Chào mừng các bạn đến với **Phần 7: Trụ Cột 5 — Model Context Protocol (MCP) — Chiếc Cầu Nối Vạn Năng Đưa Dữ Liệu Thực Tế Vào AI**!  
Hẹn gặp lại các bạn ở Bài 7.1 ngay sau đây!"
