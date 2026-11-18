# KỊCH BẢN LỜI THOẠI BÀI HỌC 8.3
**Khóa học:** Làm Chủ Google Antigravity Cho Người Không Chuyên  
**Khối 3:** Phòng Thí Nghiệm Thực Chiến Đỉnh Cao  
**Phần 8:** Dự Án Văn Phòng Đỉnh Cao  
**Tên bài:** Bài 8.3: Thực Chiến 03 — Phù Thủy Bảng Tính: Xử Lý Siêu Tốc Các Công Thức Excel Phức Tạp (VLOOKUP, XLOOKUP, INDEX/MATCH)  
**Thời lượng dự kiến:** 09:00  
**Slide tương ứng:** `phan_08_thuc_chien_van_phong_dinh_cao.html` (Slide 3: Phù Thủy Bảng Tính: Làm Chủ Công Thức Excel Khó)

---

## 🎬 1. CHUẨN BỊ TRƯỚC KHI QUAY
* **Cửa sổ trình chiếu:** Mở slide Thực Chiến 03 (Dự Án 3: Phù Thủy Bảng Tính Excel — Làm Chủ Công Thức Khó).
* **Màn hình chia đôi hoặc sẵn sàng chuyển tab:**  
  * Cửa sổ 1: Phần mềm **Microsoft Excel** (hoặc LibreOffice Calc / WPS) mở file mẫu `bao_cao_doanh_thu_thang_10.xlsx` gồm 2 Sheet:
    * Sheet 1: `DonHang` (gồm 100 dòng đơn: Mã Đơn, Ngày, Mã Khách, Mã Sản Phẩm, Số Lượng. Các cột còn trống: Tên Sản Phẩm, Đơn Giá, Thành Tiền, Tên Khách Hàng).
    * Sheet 2: `DanhMucSanPham` (Mã SP, Tên SP, Đơn Giá Niêm Yết, Tỷ Lệ Chiết Khấu).
    * Sheet 3: `KhachHang` (Mã Khách, Tên Khách Hàng, Khu Vực).
  * Cửa sổ 2: Ứng dụng **Antigravity Desktop** đang mở khung chat.
  * Cửa sổ 3: Phần mềm **Sublime Text** sẵn sàng mở thư mục `skills/phu-thuy-excel/`.
* **Tông giọng:** Sôi nổi, đầy hứng khởi, mang lại sự nhẹ nhõm và phấn khích tột độ khi tháo gỡ được "cơn ác mộng lớn nhất" của dân văn phòng với Excel.

---

## 🎙️ 2. KỊCH BẢN LỜI THOẠI CHI TIẾT (WORD-FOR-WORD SCRIPT)

### [00:00 - 01:45] NỖI SỢ CÔNG THỨC EXCEL & BÀI TOÁN GHÉP BẢNG THỰC TẾ
`[Hiển thị Slide Thực Chiến 03: Dự Án 3 - Phù Thủy Bảng Tính Excel]`  
`[Người hướng dẫn nhìn thẳng camera, nụ cười thấu hiểu]`

"Chào mừng các bạn đến với **Bài 8.3: Thực Chiến 03**!  
Nếu có một điều gì đó khiến 90% dân văn phòng — từ kế toán, nhân sự, chuyên viên kinh doanh cho đến hành chính — toát mồ hôi hột mỗi dịp cuối tháng, thì đó chắc chắn là: **Các công thức tính toán và ghép nối dữ liệu trong Microsoft Excel**!

Hãy nhìn vào màn hình của tôi: Đây là file `bao_cao_doanh_thu_thang_10.xlsx`.  
Một bài toán quen thuộc đến mức đau lòng:  
* Ở Sheet thứ nhất `DonHang`, chúng ta có 100 dòng phát sinh bán hàng, nhưng chỉ có `Mã Sản Phẩm` và `Mã Khách Hàng`.  
* Bảng giá chuẩn thì lại nằm ở Sheet thứ hai `DanhMucSanPham`.  
* Còn thông tin họ tên khách hàng thì lại nằm ở Sheet thứ ba `KhachHang`.  

Nhiệm vụ của bạn là: Làm sao để từ mã sản phẩm, điền tự động `Tên Sản Phẩm` và `Đơn Giá`? Sau đó lấy Số lượng nhân với Đơn giá trừ đi Chiết khấu để ra `Thành Tiền`? Và từ mã khách hàng, điền tự động `Tên Khách Hàng`?

Với cách làm thủ công:  
* Bạn phải nhớ cú pháp hàm `VLOOKUP`: Giá trị tìm kiếm là gì, bảng tham chiếu ở đâu, đếm cột thứ mấy, rồi phải nhớ bấm phím `F4` để khóa cố định vùng dữ liệu có dấu đô la `$`. Chỉ cần quên bấm F4 một cái là công thức trượt dòng, báo lỗi `#N/A` hàng loạt!  
* Đau đầu hơn, nếu cột cần lấy dữ liệu nằm bên trái cột dò tìm, `VLOOKUP` hoàn toàn bó tay! Bạn lại phải cầu cứu đến cặp hàm 'hack não' `INDEX` kết hợp `MATCH` lồng nhau hoa cả mắt!  
* Dành cả buổi chiều chỉ để sửa dấu phẩy, dấu chấm phẩy và bẫy lỗi `IFERROR`.

Hôm nay, tôi sẽ cho các bạn thấy: **Khi có Antigravity làm trợ lý, toàn bộ bài toán công thức khó này được giải quyết êm đẹp trong vòng đúng 15 giây**! Và tuyệt vời hơn, chúng ta sẽ cùng nhau **ra lệnh cho AI tạo ra một Skill chuyên nghiệp** để từ nay về sau, gặp bất kỳ bảng tính Excel nào, bạn cũng xử lý như một phù thủy dữ liệu!"

---

### [01:45 - 03:45] TƯ DUY XÂY DỰNG SKILL: ĐA NĂNG, LINH HOẠT VỚI MỌI FILE & MỌI HÀM
`[Chuyển màn hình sang Antigravity Desktop]`  
`[Mở Sublime Text cho học viên xem cấu trúc thư mục skills/]`

"Trước khi bắt tay vào viết câu lệnh, tôi muốn làm sáng tỏ một câu hỏi vô cùng đắt giá mà bất kỳ người đi làm thông minh nào cũng sẽ đặt ra:  
*'Thưa thầy, liệu kỹ năng này có bị gắn cứng chỉ dùng được cho mỗi file doanh thu tháng 10 này không? Nếu ngày mai tôi có file tính lương `bang_luong.xlsx`, file quản lý kho `ton_kho.xlsx`, hay tôi muốn dùng các hàm khác như SUMIFS, COUNTIFS, hàm logic IF thì sao?'*

Câu trả lời chắc nịch là: **Kỹ năng `phu-thuy-excel` mà chúng ta sắp tạo ra là một Trợ Lý Bảng Tính Đa Năng Động 100% (Generic & Flexible)**!  
File `bao_cao_doanh_thu_thang_10.xlsx` hôm nay chỉ đóng vai trò là một **Case Study thực tế điển hình** để các bạn tận mắt nhìn thấy quy trình hoạt động trực quan nhất. Còn bản chất của bộ kỹ năng này được thiết kế theo 3 nguyên lý đỉnh cao:
1. **Tiếp nhận file động bất kỳ**: Bạn truyền bất kỳ file `.xlsx` nào vào prompt — từ chấm công, doanh số, tồn kho đến ngân sách — AI sẽ tự động mở file ra, quét toàn bộ tên Sheet và tên các Cột để tự động nắm bắt bức tranh dữ liệu.
2. **Linh hoạt mọi nhóm hàm Excel**: 
   * Bạn muốn dùng **`INDEX & MATCH`** hay **`VLOOKUP`** để tương thích 100% mọi phiên bản Excel? Nó viết chuẩn xác.
   * Bạn muốn dùng **`XLOOKUP`** hiện đại trên Office 365? Nó tuân thủ ngay.
   * Bạn muốn tính tổng doanh thu theo điều kiện bằng **`SUMIFS`**, đếm số lượng bằng **`COUNTIFS`**, hay xếp hạng khách hàng bằng hàm **`IF`** lồng nhau? Nó đều xử lý mượt mà và luôn bọc bẫy lỗi `IFERROR` an toàn tuyệt đối.
3. **Bảo vệ công thức sống & Dữ liệu gốc**: BẮT BUỘC chèn công thức Excel thật để khi sếp bạn đổi số thì kết quả tự nhảy, và luôn xuất ra file mới `_Hoan_Thanh.xlsx` để file gốc của bạn không bao giờ bị ghi đè!

Bây giờ, hãy cùng tôi soạn một **Prompt Vàng 4 bước chuẩn mực** để biến Antigravity thành Phù Thủy Bảng Tính!"

---

### [03:45 - 05:45] SOẠN PROMPT VÀNG & BÓC TÁCH: TẠI SAO ĐÂY LÀ PROMPT TỐT?
`[Quay màn hình khung chat Antigravity Desktop]`  
`[Dán đoạn prompt mẫu lên màn hình]`

"Hãy quan sát kỹ câu prompt tôi gửi vào Antigravity:

> *'Chào Antigravity, hãy đóng vai một Chuyên gia Cao cấp về Phân tích Dữ liệu và Xử lý Bảng tính Excel. Hãy giúp tôi tạo một Kỹ Năng mới (Skill) mang tên `phu-thuy-excel` tại thư mục `skills/phu-thuy-excel/` với các yêu cầu chi tiết sau:*  
> *1. [Mục tiêu]: Tạo file `SKILL.md` hướng dẫn quy trình tự động đọc hiểu các file Excel (.xlsx) có cấu trúc nhiều Sheet liên kết, tự động viết và chèn các công thức tìm kiếm nâng cao (như XLOOKUP, VLOOKUP, INDEX/MATCH) để điền dữ liệu khuyết thiếu và tính toán thành tiền một cách tự động.*  
> *2. [Bối cảnh]: File dữ liệu của tôi là `bao_cao_doanh_thu_thang_10.xlsx` gồm 3 Sheet: `DonHang`, `DanhMucSanPham` và `KhachHang`. Cần điền tự động Tên SP, Đơn giá, Tên khách hàng và tính cột Thành Tiền = Số Lượng * Đơn Giá * (1 - Tỷ Lệ Chiết Khấu).*  
> *3. [Tiêu chuẩn]:*  
> *   - BẮT BUỘC chèn CÔNG THỨC EXCEL THẬT (công thức sống), tuyệt đối không điền giá trị số chết (hardcode value).*  
> *   - Mọi công thức tìm kiếm phải được bọc trong hàm bẫy lỗi `IFERROR(..., "Chưa có dữ liệu")` để tránh lỗi #N/A.*  
> *   - Định dạng cột tiền tệ chuẩn có dấu phân cách hàng nghìn (VND).*  
> *4. [Giới hạn & Bảo vệ]: Tuyệt đối KHÔNG ghi đè lên file Excel gốc. Hãy xuất ra một file mới có tên `bao_cao_doanh_thu_thang_10_Hoan_Thanh.xlsx` và in ra khung chat lời giải thích chi tiết các công thức đã sử dụng để tôi có thể tự tin báo cáo với sếp.'*

`[Dừng lại 5 giây, phân tích sắc nét từng điểm]`  
Hãy nhìn lại 4 bước vàng trong câu prompt này:
* **Mục tiêu (Goal):** Nêu đích danh việc tạo ra skill `phu-thuy-excel`, giải quyết bài toán liên kết đa bảng bằng công thức tự động.
* **Bối cảnh (Context):** Liệt kê chi tiết tên file và các Sheet cần xử lý.  
  *💡 Mẹo thực chiến cho bạn: Khi đi làm thực tế, nếu bạn cần xử lý file chấm công hay file lương, bạn chỉ cần thay tên file của bạn vào phần Bối cảnh này, ví dụ: 'File của tôi là `bang_luong_thang_11.xlsx` gồm 2 Sheet `ChamCong` và `HeSoLuong`...'. AI sẽ lập tức hiểu cấu trúc mới mà không gặp bất kỳ trở ngại nào!*
* **Tiêu chuẩn (Standard):** Yêu cầu công thức Excel sống, bẫy lỗi `IFERROR`, định dạng số tiền tệ.  
  *💡 Mẹo chọn hàm: Nếu bạn muốn ép AI dùng chính xác một hàm cụ thể như 'Dùng hàm INDEX & MATCH' hoặc 'Dùng hàm SUMIFS', bạn chỉ việc ghi rõ vào mục Tiêu chuẩn này! AI sẽ tuân thủ 100% chỉ định của bạn.*
* **Giới hạn (Boundary):** Chốt chặn sinh tử bảo vệ file gốc: Tạo file mới `_Hoan_Thanh.xlsx` và yêu cầu AI giải thích công thức."

---

### [05:45 - 07:15] QUAN SÁT AI TẠO SKILL & THỰC THI TRONG CHỚP MẮT
`[Bấm Enter gửi câu prompt]`  
`[Antigravity phân tích và tạo file SKILL.md]`

"Các bạn thấy chưa? Antigravity lập tức tạo thư mục `skills/phu-thuy-excel/SKILL.md`.  
Bên trong, nó hướng dẫn sử dụng thư viện xử lý Excel mạnh mẽ của Python (`openpyxl`), chuẩn bị sẵn các hàm chèn công thức `XLOOKUP` và `INDEX/MATCH` cực kỳ chuẩn xác.

Bây giờ, chúng ta hãy kích hoạt ngay kỹ năng này để xử lý file bảng tính doanh thu:  
Tôi chỉ cần nhắn:  
> *'Hãy dùng skill `phu-thuy-excel` để hoàn thiện toàn bộ công thức cho file `bao_cao_doanh_thu_thang_10.xlsx` ngay bây giờ!'*  
`[Bấm Enter]`

`[Chỉ chuột vào màn hình Antigravity]`  
Nhìn xem các bạn:  
* AI đọc dữ liệu cả 3 Sheet.  
* Nó tự động viết công thức dò tìm Tên sản phẩm từ cột `Mã SP` (linh hoạt lựa chọn VLOOKUP hoặc INDEX/MATCH tương thích 100%).  
* Nó viết công thức dò tìm Đơn giá và Chiết khấu.  
* Nó ghép công thức tính Thành tiền.  
* Và xuất ra file `bao_cao_doanh_thu_thang_10_Hoan_Thanh.xlsx`!  
Toàn bộ quá trình cho 100 dòng dữ liệu diễn ra trong đúng **12 giây**!"

---

### [07:15 - 08:30] MỞ FILE EXCEL NGHIỆM THU: CÔNG THỨC SỐNG NẰM TRONG TỪNG Ô!
`[Chuyển màn hình sang Microsoft Excel]`  
`[Mở file bao_cao_doanh_thu_thang_10_Hoan_Thanh.xlsx]`

"Bây giờ, hãy mở file kết quả lên trong Excel để xem điều kỳ diệu!  
`[Phóng to bảng tính Excel lên 120%]`  
`[Nhấp chuột vào ô Tên Sản Phẩm C2]`  
Các bạn hãy nhìn lên thanh công thức (Formula Bar) phía trên:  
Công thức hiện ra rõ ràng: `=IFERROR(VLOOKUP(B2, DanhMucSanPham!A:D, 2, 0), "Chưa có dữ liệu")` (hoặc với Office 365 mới là `XLOOKUP`)!  
`[Nhấp chuột vào ô Tên Khách Hàng H2]`  
Công thức: `=IFERROR(VLOOKUP(G2, KhachHang!A:B, 2, 0), "Chưa có dữ liệu")` — Tên khách hàng 'Doanh nghiệp Tư nhân Vận tải & Logistics Tân Phát' hiển thị đầy đủ, không hề bị lỗi!  
`[Nhấp chuột vào ô Thành Tiền F2]`  
Công thức: `=D2 * E2 * (1 - IFERROR(VLOOKUP(B2, DanhMucSanPham!A:D, 4, 0), 0))`!

Một điểm cực kỳ tinh tế mà tôi muốn dặn các bạn:  
Nếu máy tính của bạn hoặc của sếp dùng bản Office 2016, 2019 hoặc WPS Office chưa có hàm `XLOOKUP`, nếu bạn cố gõ XLOOKUP thì phần mềm sẽ báo lỗi `#NAME?`, và khi đó hàm `IFERROR` sẽ bẫy lỗi và hiển thị ra chữ 'Chưa có dữ liệu'!  
Đó là lý do vì sao kỹ năng `phu-thuy-excel` này thông minh đến mức nó biết ưu tiên dùng cặp hàm chuẩn mực `VLOOKUP` và `INDEX/MATCH` để dù mở trên bất kỳ máy tính nào trong công ty, kết quả vẫn luôn hiển thị chính xác 100%!

Tất cả 100 dòng đều có công thức sống!  
Bây giờ nếu tôi đổi số lượng ở dòng 2 từ 3 thành 10 ➔ Nhìn xem, cột Thành tiền tự động nhảy số tức thì!  
Nếu sếp bạn có kiểm tra file, sếp sẽ hoàn toàn bị thuyết phục bởi độ chính xác và chuyên nghiệp này!"

---

### [08:30 - 09:00] TỔNG KẾT & DẪN SANG BÀI THỰC CHIẾN 04
`[Quay lại camera, tông giọng hào hứng]`

"Một công việc mà trước đây có thể khiến bạn đánh vật cả buổi chiều, loay hoay sửa lỗi `#N/A` đến toát mồ hôi, giờ đây được giải quyết gọn gàng, chuẩn xác từng ly chỉ sau 15 giây! Đó chính là sức mạnh giải phóng của Trí Tuệ Nhân Tạo khi bạn biết cách làm chủ và ra lệnh chuẩn chỉnh!

Nhưng chưa hết! Sau khi đã có số liệu báo cáo đẹp mắt từ Excel, bài toán tiếp theo của mọi người đi làm là gì?  
Đó là **Làm slide thuyết trình để báo cáo với sếp hoặc trình bày trước khách hàng**!  
Bạn đã quá chán ngấy những mẫu slide PowerPoint nhàm chán, generic hoặc tốn hàng giờ chỉnh sửa từng khối hộp?  
Ở bài học tiếp theo — **Bài 8.4: Thực Chiến 04**, chúng ta sẽ cùng tạo ra một **Skill Đỉnh Cao: Tự Động Sinh Slide Thuyết Trình HTML Động Đẳng Cấp 0-Dependency** với hiệu ứng chuyển trang cực kỳ hiện đại và mượt mà!

Mời các bạn cùng bấm sang **Bài 8.4** để khám phá bí kíp này!"
