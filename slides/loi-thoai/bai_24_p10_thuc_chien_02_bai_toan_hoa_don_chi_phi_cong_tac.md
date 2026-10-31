# KỊCH BẢN LỜI THOẠI BÀI HỌC 10.1
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 3:** Phòng Thí Nghiệm Thực Chiến Đỉnh Cao  
**Phần 10:** ⭐ Thực Chiến 02 — Kế Toán Số: Quét Ảnh Hóa Đơn Tự Động Đổ Dữ Liệu Vào Excel  
**Tên bài:** Bài 10.1: Bài toán rà soát hóa đơn chi phí công tác của phòng Kế toán & Hành chính  
**Thời lượng dự kiến:** 10:00 (Video Preview - Mở xem thử miễn phí)  
**Slide tương ứng:** `phan_10_thuc_chien_hoa_don_excel.html` (Slide 1)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở tệp slide `slides/phan_10_thuc_chien_hoa_don_excel.html` (Slide 3: Thực Chiến 02 — Kế Toán Số: Bóc Tách Hóa Đơn Tự Động).
* **Hình ảnh đạo cụ:** Mở sẵn một thư mục chứa 4 bức ảnh chụp hóa đơn thực tế: hóa đơn taxi Mai Linh in nhiệt hơi mờ, hóa đơn tiếp khách ăn uống chụp nghiêng, hóa đơn khách sạn và hóa đơn mua văn phòng phẩm.
* **Tông giọng:** Thân thương, thực tế, xoáy sâu vào nỗi đau nhập liệu thủ công của dân công sở và nhân viên kế toán.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD SCRIPT)

### [00:00 - 01:45] MỞ ĐẦU: NỖI ÁM ẢNH HOÀN ỨNG CHI PHÍ CÔNG TÁC CUỐI THÁNG
`[Hiển thị Slide 1: Thực Chiến 2 — Kế Toán: Quét Hóa Đơn Tự Đổ Vào Excel]`  
`[Tông giọng thở dài, đồng cảm sâu sắc]`

"Chào mừng các bạn đến với **Phần 10: ⭐ Thực Chiến 02 — Kế Toán Số: Quét Ảnh Hóa Đơn Tự Động Đổ Dữ Liệu Vào Excel**!

Tôi tin chắc rằng: Dù bạn là nhân viên kinh doanh hay đi gặp khách hàng, là nhân viên kỹ thuật hay đi công tác, hay bạn chính là các anh chị em phòng Hành chính - Kế toán... thì **khoảng thời gian ngày 25 đến 30 hàng tháng luôn là một cực hình**!

Cực hình đó mang tên: **Làm Bảng Kê Hoàn Ứng Chi Phí**:
* Sau một chuyến công tác 3 ngày trở về, trong ví của bạn là một mớ hỗn độn:
  * Vé máy bay, cuống vé tàu xe.
  * Hóa đơn tiền ăn uống chụp vội trên bàn nhậu hơi mờ mực.
  * Phiếu thu tiền taxi in bằng giấy nhiệt đã bắt đầu bay màu chữ.
* Bạn phải làm gì?  
  Ngồi bệt xuống bàn, mở từng bức ảnh trên điện thoại, căng mắt ra nhìn từng con số mờ mờ, rồi một tay bấm phím số gõ từng dòng vào bảng tính Excel: Ngày nào, mua của ai, tiền trước thuế bao nhiêu, thuế VAT 8% hay 10%, tiền sau thuế bao nhiêu...
* Chỉ cần gõ nhầm một số 0, hoặc quên cộng tiền VAT, bảng tính lệch mất vài trăm nghìn là kế toán trả về bắt làm lại từ đầu! Mất đứt cả buổi chiều chỉ để làm một công việc thủ công nhàm chán!"

---

### [01:45 - 04:30] ĐÔI MẮT THỊ GIÁC SỐ CỦA AI (MULTIMODAL VISION): THAY ĐỔI CUỘC CHƠI
`[Chỉ chuột vào hình ảnh Quét Ảnh Hóa Đơn Mờ trên Slide 3]`  
`[Giải thích khả năng vượt trội của công nghệ thị giác máy tính]`

"Nếu bạn nghĩ AI chỉ biết đọc văn bản dạng chữ gõ thì bạn đã nhầm to!  
Trong Antigravity, mô hình ngôn ngữ lớn được trang bị **Đôi Mắt Số Đa Phương Thức (Multimodal Vision)** cực kỳ tinh tường:
* Nó có khả năng 'nhìn' vào bức ảnh chụp từ camera điện thoại:
  * Dù bức ảnh chụp bị nghiêng góc 45 độ.
  * Dù hóa đơn in nhiệt bị mờ một góc.
  * Dù chữ in bị nhăn nheo hay có chữ ký đè lên...
* Đôi mắt số của AI vẫn có thể nhận diện chuẩn xác từng trường thông tin quan trọng nhất:
  1. Tên đơn vị bán hàng (Nhà hàng, Hãng taxi, Khách sạn).
  2. Mã số thuế của doanh nghiệp.
  3. Ngày tháng lập hóa đơn.
  4. Số tiền trước thuế, tỷ lệ thuế VAT và tổng số tiền thanh toán cuối cùng.
* Nó đọc nhanh hơn con người gấp 50 lần, và đặc biệt: **Nó không bao giờ bị mỏi mắt hay gõ nhầm số 0!**"

---

### [04:30 - 07:15] QUY TRÌNH KẾ TOÁN SỐ HOÀN TOÀN TỰ ĐỘNG
`[Chỉ chuột vào sơ đồ 3 bước trên Slide 3: Nạp Ảnh -> Bóc Tách -> Xuất Excel]`  
`[Vạch rõ quy trình thực chiến]`

"Quy trình giải quyết bài toán này trong 2 bài học tới sẽ diễn ra như thế nào?

1. **Bước 1 — Ném dữ liệu thô:** Bạn chỉ cần ném toàn bộ 4 bức ảnh chụp hóa đơn vào một thư mục trên máy tính mang tên `HoaDon_CongTac`.
2. **Bước 2 — Trợ lý AI hành động:**  
   Antigravity sẽ tự động mở từng bức ảnh ra soi, tự bóc tách toàn bộ thông tin chi phí và lập bảng đối chiếu số liệu.
3. **Bước 3 — Xuất bảng tính Excel hoàn hảo:**  
   AI sẽ tự tay tạo ra một file Excel mang tên `bang_ke_chi_phi_cong_tac.xlsx`:
   * Có sẵn tiêu đề công ty trang trọng.
   * Có đầy đủ các cột: Ngày, Đơn vị, Nội dung chi, Tiền trước thuế, VAT, Tổng tiền.
   * Dưới đáy bảng tự động chèn sẵn công thức hàm `=SUM(...)` chuẩn chỉ để tính tổng tiền.
   * Định dạng tiền tệ VNĐ đẹp mắt từng dấu chấm.
* Bạn chỉ việc bấm nút In, ký tên vào góc và mang sang nộp phòng Kế toán để nhận tiền hoàn ứng. Không tốn dù chỉ một giọt mồ hôi!"

---

### [07:15 - 10:00] TỔNG KẾT BÀI & CÂU DẪN SANG THỰC HÀNH BÀI 10.2
`[Quay lại màn hình camera, nụ cười khích lệ]`

"Hãy tạm biệt vĩnh viễn những buổi chiều căng mắt gõ hóa đơn thủ công. Từ hôm nay, máy tính và trợ lý AI sẽ gánh vác toàn bộ công việc này thay bạn!

Trong **Bài 10.2** ngay sau đây, chúng ta sẽ bắt tay vào thực hành:  
Tận mắt chứng kiến đôi mắt số của Antigravity quét qua 4 bức ảnh hóa đơn mờ và bóc tách từng con số tiền bạc chuẩn xác đến từng đồng!

Mời các bạn mở sẵn Antigravity Desktop và cùng tôi bước sang Bài 10.2 ngay bây giờ!"
