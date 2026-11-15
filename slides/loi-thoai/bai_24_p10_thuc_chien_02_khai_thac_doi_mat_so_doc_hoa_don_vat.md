# KỊCH BẢN LỜI THOẠI BÀI HỌC 10.2
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 3:** Phòng Thí Nghiệm Thực Chiến Đỉnh Cao  
**Phần 10:** ⭐ Thực Chiến 02 — Kế Toán Số: Quét Ảnh Hóa Đơn Tự Động Đổ Dữ Liệu Vào Excel  
**Tên bài:** Bài 10.2: Thực hành: Khai thác đôi mắt số của AI để đọc hàng loạt ảnh chụp hóa đơn mờ/scan, tự bóc tách số tiền và thuế VAT  
**Thời lượng dự kiến:** 10:00  
**Slide tương ứng:** `phan_10_thuc_chien_hoa_don_excel.html` (Slide 2)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_10_thuc_chien_hoa_don_excel.html` (Slide 3).
* **Thư mục thực hành:** Tạo sẵn thư mục `HoaDon_CongTac` chứa 4 file ảnh hóa đơn mẫu:
  1. `hd_01_an_trua.png`: Hóa đơn nhà hàng Cơm Niêu (chụp hơi nghiêng).
  2. `hd_02_taxi.png`: Phiếu thu taxi Mai Linh đi từ sân bay về khách sạn (chữ in nhiệt hơi mờ).
  3. `hd_03_khach_san.png`: Hóa đơn giá trị gia tăng khách sạn 2 đêm nghỉ.
  4. `hd_04_van_phong_pham.png`: Biên lai mua bút ký và sổ tay tiếp khách.
* **Tông giọng:** Sôi nổi, cuốn hút, làm nổi bật khả năng nhận diện thị giác siêu việt của AI.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD SCRIPT)

### [00:00 - 01:20] MỞ ĐẦU: KHÁM PHÁ CÁC TỆP ẢNH HÓA ĐƠN MẪU
`[Hiển thị Slide 2: Thực Hành: Trích Xuất Đa Định Dạng Hóa Đơn]`  
`[Mở thư mục HoaDon_CongTac lên màn hình, mở xem lướt từng ảnh]`

"Chào mừng các bạn đã quay trở lại với Bài 10.2!

Hãy nhìn vào màn hình của tôi:  
Trong thư mục `HoaDon_CongTac` này, tôi đã chuẩn bị sẵn 4 bức ảnh chụp hóa đơn thực tế:
* Tấm ảnh thứ nhất: Hóa đơn ăn trưa tiếp khách, chụp nghiêng và hơi sấp bóng đèn.
* Tấm ảnh thứ hai: Phiếu thu taxi in trên giấy nhiệt, chữ in có chỗ đậm chỗ nhạt.
* Tấm ảnh thứ ba: Hóa đơn đỏ khách sạn có thuế VAT 10%.
* Tấm ảnh thứ tư: Hóa đơn mua văn phòng phẩm.

Bình thường, nếu ngồi nhìn 4 tấm ảnh này để gõ số vào Excel, bạn sẽ mất ít nhất 15 phút. Bây giờ, chúng ta sẽ mở Antigravity lên và để AI tự 'soi' từng tấm ảnh nhé!"

---

### [01:20 - 04:00] BƯỚC 1: SOẠN CÂU LỆNH BÓC TÁCH DỮ LIỆU ĐA PHƯƠNG THỨC
`[Chuyển màn hình sang Antigravity Desktop]`  
`[Bấm New Task, thao tác gõ vào khung chat]`

"Chúng ta áp dụng đúng Công thức 4 bước vàng ra lệnh:

> *'Chào Antigravity, bạn hãy đóng vai trò là Chuyên viên Kế toán số.*  
> *1. Bối cảnh: Hãy quét toàn bộ các tệp ảnh chụp hóa đơn trong thư mục `HoaDon_CongTac`.*  
> *2. Mục tiêu: Khai thác khả năng thị giác (Vision) để đọc từng ảnh, tự động trích xuất các thông tin kế toán sau:*  
> *   - Ngày tháng lập hóa đơn*  
> *   - Đơn vị bán hàng (Nhà hàng, Hãng taxi, Khách sạn)*  
> *   - Nội dung chi phí*  
> *   - Số tiền trước thuế (VNĐ)*  
> *   - Thuế suất VAT (8% hoặc 10%)*  
> *   - Tiền thuế VAT (VNĐ)*  
> *   - Tổng số tiền thanh toán (VNĐ)*  
> *3. Tiêu chuẩn: Hãy lập một bảng Markdown tổng hợp chi tiết hiển thị sang cửa sổ bên phải để tôi nghiệm thu. Mọi số tiền phải định dạng có dấu chấm phân cách.*  
> *4. Giới hạn an toàn: Giữ nguyên vẹn các file ảnh gốc, không được xóa hay di chuyển.'*

`[Nhấn phím Enter]`  
Và bây giờ, hãy xem đôi mắt số của AI bắt đầu làm việc!"

---

### [04:00 - 07:30] BƯỚC 2: QUAN SÁT AI TỰ ĐỘNG ĐỌC VÀ BÓC TÁCH TỪNG ẢNH
`[Chỉ chuột vào luồng suy nghĩ của AI]`  
`[Giải thích cách AI bóc tách thông minh từng ảnh]`

"Các bạn hãy nhìn kỹ màn hình:
1. `[AI đọc ảnh hd_01_an_trua.png]`  
   AI nhận diện: 'Nhà hàng Cơm Niêu Sài Gòn'. Ngày: 12/10/2026.  
   Nó nhìn vào dòng thanh toán: Tiền trước thuế là 1.200.000 VNĐ. Thuế suất VAT 8% là 96.000 VNĐ. Tổng tiền thanh toán: 1.296.000 VNĐ!  
   Dù ảnh chụp bị bóng mờ một góc, AI vẫn tính toán và đối chiếu ngược cực kỳ chính xác!
2. `[AI đọc ảnh hd_02_taxi.png]`  
   Nó nhận diện: 'Công ty Cổ phần Tập đoàn Mai Linh'. Cuốc xe từ Sân bay Nội Bài về khách sạn. Tổng cước: 320.000 VNĐ.
3. `[AI đọc ảnh hd_03_khach_san.png]`  
   Nó nhận diện: 'Khách sạn Novotel'. Tiền phòng 2 đêm: 2.500.000 VNĐ. Thuế VAT 10% là 250.000 VNĐ. Tổng tiền: 2.750.000 VNĐ!
4. `[AI đọc ảnh hd_04_van_phong_pham.png]`  
   Nó nhận diện: 'Nhà sách Fahasa'. Mua sổ và bút ký: 450.000 VNĐ."

---

### [07:30 - 09:15] BƯỚC 3: NGHIỆM THU BẢNG BÁO CÁO BÓC TÁCH TRÊN CỬA SỔ PREVIEW
`[Chỉ chuột sang bảng Markdown hiển thị ở cửa sổ bên phải]`  
`[Tông giọng trầm trồ, khích lệ]`

"Chỉ trong vòng chưa đầy 20 giây!  
Ở cửa sổ bên phải, một bảng tổng hợp đẹp lung linh đã hiện ra:

| Ngày | Đơn Vị Phát Hành | Nội Dung Chi | Tiền Trước Thuế | VAT | Tổng Thanh Toán |
| :---: | :--- | :--- | :---: | :---: | :---: |
| 12/10/2026 | Nhà hàng Cơm Niêu | Ăn trưa tiếp khách | 1.200.000 VNĐ | 8% (96.000 VNĐ) | 1.296.000 VNĐ |
| 12/10/2026 | Taxi Mai Linh | Xe đưa đón sân bay | 320.000 VNĐ | 0 VNĐ | 320.000 VNĐ |
| 14/10/2026 | Khách sạn Novotel | Tiền phòng công tác | 2.500.000 VNĐ | 10% (250.000 VNĐ) | 2.750.000 VNĐ |
| 14/10/2026 | Nhà sách Fahasa | Văn phòng phẩm họp | 450.000 VNĐ | 0 VNĐ | 450.000 VNĐ |

Từng con số, từng tỷ lệ thuế VAT được bóc tách chuẩn xác 100%, không sai lệch dù chỉ 1 đồng!"

---

### [09:15 - 10:00] TỔNG KẾT BÀI & CÂU DẪN SANG BÀI 10.3
`[Quay lại màn hình camera, nụ cười rạng rỡ]`

"Có được bảng bóc tách số liệu này rồi thì quá tuyệt vời!  
Nhưng phòng Kế toán của công ty bạn sẽ không nhận một bản văn bản chat. Kế toán cần **một tệp bảng tính Excel chuẩn mực (`.xlsx`)**: có sẵn tiêu đề, kẻ khung viền đẹp mắt, và đặc biệt là phải có công thức hàm `=SUM(...)` để sếp kiểm tra!

Làm thế nào để yêu cầu AI tự động xuất toàn bộ bảng số liệu này thành một file Excel hoàn chỉnh sẵn sàng in nộp sếp?

Chào mừng các bạn đến với **Bài 10.3: Nghiệm thu thành phẩm: Xuất bảng tính Excel có sẵn công thức tính tổng**!  
Mời các bạn cùng bấm sang Bài 10.3 ngay bây giờ!"
