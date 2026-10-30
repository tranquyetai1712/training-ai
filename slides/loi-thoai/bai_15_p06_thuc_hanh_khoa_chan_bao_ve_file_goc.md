# KỊCH BẢN LỜI THOẠI BÀI HỌC 6.2
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 2:** Kho Vũ Khí 7 Trụ Cột Cho Dân Văn Phòng  
**Phần 6:** Trụ Cột 4 — Hooks: Vòng Kim Cô Bảo Vệ An Toàn Dữ Liệu Tuyệt Đối  
**Tên bài:** Bài 6.2: Thực hành: Cài chốt chặn PreToolUse ngăn AI sửa đè file gốc  
**Thời lượng dự kiến:** 04:30 (Chuẩn Udemy Micro-Learning • Practical Safety Guard)  
**Slide tương ứng:** `phan_06_tru_cot_hooks.html` (Slide 2)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_06_tru_cot_hooks.html` (Slide 2: Thực Hành: Cài Đặt Hook Chặn Xóa Dữ Liệu).
* **Môi trường thực hành:** Mở Antigravity Desktop tại workspace độc lập `slides/Demo/chot-chan-bao-ve-file-goc/`. Tệp bảng tính `du_lieu_goc_khach_hang.xlsx` đã có sẵn dữ liệu thực tế 10 khách hàng, và hệ thống đã nạp sẵn cấu hình `.agents/hooks.json` có chốt chặn `PreToolUse`. Giảng viên mở workspace là thực hành được ngay.
* **Tông giọng:** Hồi hộp, kịch tính khi thử nghiệm câu lệnh nguy hiểm, sau đó chuyển sang thở phào nhẹ nhõm và tự tin khi thấy AI tự động phanh gấp.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD LEAN SCRIPT)

### [00:00 - 00:45] THỬ NGHIỆM TÌNH HUỐNG MẠO HIỂM NHẤT TRONG DOANH NGHIỆP
`[Slide 2: Thực Hành: Cài Đặt Hook Chặn Xóa Dữ Liệu]`  
`[Mở Antigravity Desktop tại workspace slides/Demo/chot-chan-bao-ve-file-goc/]`  
`[Chỉ vào file du_lieu_goc_khach_hang.xlsx đã chuẩn bị sẵn bên thanh File Explorer]`

"Chào mừng bạn đến với Bài 6.2!

Hôm nay, tôi muốn cùng bạn làm một việc mà trong môi trường công sở bình thường không ai dám thử:  
**Cố tình ra lệnh cho trợ lý AI phá hủy tệp dữ liệu gốc của công ty!**

Hãy nhìn vào màn hình của tôi: Trong workspace demo này đang có một tệp bảng tính cực kỳ quý giá mang tên `du_lieu_goc_khach_hang.xlsx`. Đây là danh bạ toàn bộ khách hàng trung thành của công ty trong suốt 5 năm qua.  
Nếu một nhân viên bất cẩn mở file này ra, nhấn nút Xóa rồi lưu đè lên, thì toàn bộ dữ liệu kinh doanh sẽ bốc hơi vĩnh viễn!

**Thế nhưng khi đã có Trạm gác Hooks `PreToolUse` cài sẵn trong `.agents/hooks.json`,** Antigravity sẽ phản ứng ra sao trước một câu lệnh nguy hiểm như vậy? Chúng ta hãy cùng nhau thử nghiệm ngay bây giờ!"

---

### [00:45 - 02:00] THAO TÁC CỐ TÌNH RA LỆNH NGUY HIỂM TRÊN KHUNG CHAT
`[Chuyển màn hình sang khung chat Antigravity Desktop tại workspace slides/Demo/chot-chan-bao-ve-file-goc/]`  
`[Bấm nút New Task và gõ câu lệnh mạo hiểm]`

"Tại khung chat Antigravity, tôi sẽ gõ một câu lệnh cực kỳ bất cẩn mà người dùng rất dễ mắc phải khi đãng trí:

> *'Hãy mở tệp `du_lieu_goc_khach_hang.xlsx` ra, lọc và xóa bỏ toàn bộ những khách hàng nào chưa phát sinh đơn hàng trong tháng 10 này giúp tôi.'*

`[Nhấn Enter dứt khoát và theo dõi luồng an ninh]`  
Các bạn hãy nín thở quan sát màn hình!

Ngay khi nhận lệnh, trợ lý AI bắt đầu kích hoạt công cụ can thiệp tệp tin. Nó chuẩn bị ghi đè lên file `du_lieu_goc_khach_hang.xlsx`.  
**Thế nhưng ngay tại tích tắc đó — trước khi ngón tay số của AI kịp chạm vào dữ liệu,** Trạm gác Hook `PreToolUse` lập tức kích hoạt!"

---

### [02:00 - 03:45] TRẠM GÁC HOOK THỔI CÒI & PHẢN XẠ "QUAY ĐẦU LÀ BỜ" CỦA AI
`[Chỉ thông báo cảnh báo màu đỏ viền vàng bật lên trên luồng thực thi]`

"**Bạn hãy nhìn vào thông báo cảnh báo xuất hiện trên màn hình:**
> ⛔ **[CẢNH BÁO AN NINH]: THAO TÁC BỊ CHẶN ĐỨNG!**  
> *Tệp tin `du_lieu_goc_khach_hang.xlsx` thuộc danh mục dữ liệu gốc được bảo vệ nghiêm ngặt. Lệnh can thiệp trực tiếp đã bị hủy bỏ!*

**Và điều tuyệt vời nhất ở đây là phản ứng thông minh của trợ lý AI:**  
Nó không hề bị đơ máy hay làm văng ứng dụng! Nó tự đọc lý do bị chặn của Hook và lập tức 'quay đầu là bờ'.

Nó lịch sự gửi lại tin nhắn cho tôi:  
> *'Thưa bạn, tệp tin `du_lieu_goc_khach_hang.xlsx` là dữ liệu gốc được bảo vệ nghiêm ngặt, tôi không được phép sửa đổi trực tiếp.*  
> *Để đáp ứng nhu cầu của bạn một cách an toàn nhất, tôi đề xuất tạo ra một bản sao mới mang tên `khach_hang_chua_mua_thang_10.xlsx` để lọc danh sách riêng, bảo toàn nguyên vẹn 100% dữ liệu gốc cho bạn. Bạn có đồng ý không?'*

`[Vỗ tay mỉm cười]`  
Bạn thấy đấy, Trạm gác Hooks hoạt động chính xác như một phản xạ tự vệ tự nhiên của cơ thể: Nó bảo vệ bạn khỏi chính những lúc bạn lỡ tay, đãng trí hoặc mệt mỏi!"

---

### [03:45 - 04:30] BÀI HỌC VỀ SỰ AN TÂM TUYỆT ĐỐI & CẦU NỐI SANG PHẦN 7 (MCP)
`[Chỉ dòng Footer Bar trên Slide 2: An toàn tuyệt đối Safety First]`

"**Nói tóm lại,** với Trụ cột Hooks, bạn có thể tự tin 100% khi giao việc cho AI chạy ngầm hoặc chạy qua đêm mà không bao giờ phải nơm nớp lo sợ rủi ro mất mát dữ liệu.

**Thế nhưng từ đầu khóa học đến giờ,** các trợ lý AI của chúng ta mới chỉ tác chiến bên trong các tệp tin cục bộ nằm sẵn trên ổ cứng máy tính.  
Trong khi thực tế công việc hàng ngày:
* Dữ liệu bán hàng lại nằm trên bảng tính trực tuyến Google Sheet.
* Hàng trăm email quan trọng lại nằm trong hộp thư Gmail.
* Và các trao đổi công việc lại nằm trong nhóm chat Slack hay Drive.

**Làm thế nào để 'nối dài cánh tay' của AI ra thế giới internet bên ngoài?**  
Chào mừng bạn bước sang **Phần 7: Trụ Cột 5 — MCP (Model Context Protocol) — Chiếc Cầu Nối Vạn Năng Đưa Dữ Liệu Thực Tế Vào AI**!

Hẹn gặp lại bạn ở Bài 7.1 ngay sau đây!"
