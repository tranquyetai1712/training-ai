# 50 Ví Dụ Thực Tế Ứng Dụng Antigravity Xử Lý Excel & Google Sheets Cho Dân Văn Phòng

Tài liệu này được thiết kế chuyên biệt cho giảng viên đào tạo AI thực chiến với **Antigravity** (kết hợp xử lý file trực tiếp trên ổ cứng máy tính và kết nối **Google Drive / Google Sheets / Gmail / Calendar**).

* **Tỷ lệ cấu trúc:** ~70% bài toán thuần xử lý bảng tính (Làm sạch, Chuẩn hóa, Gộp/Tách file, Đối soát, Báo cáo & Biểu đồ) + ~30% bài toán liên thông đa định dạng & đa ứng dụng (PDF/Ảnh/Word $\leftrightarrow$ Excel/Sheets $\leftrightarrow$ Gmail/Drive/Calendar).
* **Phân bổ 6 phòng ban:**
  1. Nhân sự - Tuyển dụng - C&B (9 ví dụ)
  2. Kế toán - Tài chính (9 ví dụ)
  3. Kinh doanh - Chăm sóc khách hàng (9 ví dụ)
  4. Marketing - Thương mại điện tử (8 ví dụ)
  5. Mua hàng - Kho vận - Chuỗi cung ứng (8 ví dụ)
  6. Hành chính - Quản lý dự án - Văn phòng chung (7 ví dụ)

---

## PHẦN 1: NHÂN SỰ - TUYỂN DỤNG - C&B (9 Ví dụ)

### Ví dụ 1: Chuẩn hóa dữ liệu chấm công xuất từ máy vân tay/FaceID (Thuần Excel)
* **Bài toán & Nỗi đau:** Máy chấm công xuất ra file log thô hàng chục nghìn dòng (mỗi lần quẹt thẻ là 1 dòng, nhân viên quẹt 4-5 lần/ngày). HR mất cả buổi dùng hàm `MIN/MAX`, `VLOOKUP` để tìm giờ vào đầu tiên, giờ ra cuối cùng và tính số phút đi muộn/về sớm.
* **Đầu vào (Input):** File `cham_cong_thang_10.xlsx` (Cột: Mã NV, Họ tên, Ngày giờ quẹt thẻ dạng `2026-10-05 08:42:11`) và quy định ca làm việc (08:30 - 17:30, nghỉ trưa 12:00 - 13:00).
* **Prompt mẫu Antigravity:**
  > "Đọc file `cham_cong_thang_10.xlsx`. Hãy gom nhóm theo từng Nhân viên và từng Ngày: lấy giờ quẹt sớm nhất làm Giờ vào, muộn nhất làm Giờ ra. Tính số phút đi muộn (nếu vào sau 08:30), số phút về sớm (nếu ra trước 17:30), và tổng số công trong ngày. Xuất ra file `bang_cong_chuan_hoa.xlsx` gồm 2 sheet: Chi tiết từng ngày và Bảng tổng hợp tháng của từng nhân viên, tô màu đỏ các dòng đi muộn quá 30 phút."
* **Output & Điểm "Wow" khi Demo:** Chỉ 1 câu lệnh, Antigravity xử lý xong 20.000 dòng log thô thành bảng chấm công chuẩn có định dạng màu sắc trong 15 giây mà không cần viết bất kỳ công thức mảng nào.

### Ví dụ 2: Gộp 12 bảng đánh giá KPI tháng của các phòng ban thành báo cáo năm (Thuần Excel)
* **Bài toán & Nỗi đau:** Cuối năm, mỗi trưởng phòng gửi 1 file Excel đánh giá KPI nhân sự, cấu trúc cột hơi lệch nhau (chỗ ghi "Mã NV", chỗ ghi "ID", thứ tự cột khác nhau). HR phải mở từng file copy-paste thủ công rất dễ nhầm cột.
* **Đầu vào (Input):** Thư mục `/KPI_2026` chứa 12 file `.xlsx` của các phòng ban khác nhau.
* **Prompt mẫu Antigravity:**
  > "Quét toàn bộ các file Excel trong thư mục `/KPI_2026`. Dù tên cột giữa các file có hơi khác nhau (ví dụ: 'Mã NV'/'ID', 'Điểm KPI'/'Tổng điểm'), hãy tự động nhận diện và ánh xạ về chuẩn chung gồm: Mã NV, Họ tên, Phòng ban, Điểm từng quý, Điểm trung bình năm. Gộp tất cả vào file `Tong_hop_KPI_Nam_2026.xlsx` và tự động xếp loại A/B/C/D theo thang điểm."
* **Output & Điểm "Wow" khi Demo:** AI tự hiểu ngữ nghĩa tên cột bị lệch giữa các file để gộp chính xác — điều mà Power Query hoặc VBA thông thường sẽ báo lỗi ngay lập tức.

### Ví dụ 3: Tính lương Gross - Net, BHXH và Thuế TNCN lũy tiến tự động (Thuần Excel)
* **Bài toán & Nỗi đau:** Công thức tính thuế TNCN 7 bậc lũy tiến trên Excel cực kỳ dài (`IF` lồng nhau) và dễ sai khi nhân viên có thay đổi số người phụ thuộc, lương OT chịu thuế và không chịu thuế.
* **Đầu vào (Input):** File `du_lieu_luong_thang.xlsx` chứa: Lương cơ bản, Phụ cấp ăn trưa, Phụ cấp điện thoại, Giờ OT ngày thường/cuối tuần, Số người phụ thuộc.
* **Prompt mẫu Antigravity:**
  > "Dựa vào file `du_lieu_luong_thang.xlsx`, hãy tính bảng lương hoàn chỉnh theo luật hiện hành: trừ BHXH/BHYT/BHTN (10.5% trên lương đóng BH), trừ giảm trừ gia cảnh bản thân (11 triệu) và người phụ thuộc (4.4 triệu/người), miễn thuế phần phụ cấp ăn trưa tối đa 730.000đ và phần chênh lệch lương OT. Tính thuế TNCN theo biểu lũy tiến 7 bậc và lương Net thực nhận. Hãy chèn trực tiếp công thức Excel vào các cột để kế toán kiểm tra được."
* **Output & Điểm "Wow" khi Demo:** Antigravity không chỉ điền kết quả tĩnh mà **ghi trực tiếp công thức Excel chuẩn** vào từng ô, giúp học viên mở file lên click vào ô thấy ngay công thức hoạt động.

### Ví dụ 4: Tách bảng lương tổng thành 100 phiếu lương riêng biệt & gửi Gmail (Liên thông Excel + Gmail)
* **Bài toán & Nỗi đau:** Sau khi chốt bảng lương tổng, C&B phải tách dòng của từng người ra để gửi email cá nhân. Nếu copy nhầm dòng của người này gửi cho người kia sẽ gây khủng hoảng nhân sự.
* **Đầu vào (Input):** File `Bang_luong_chot.xlsx` (có cột Email nhân viên) trên máy hoặc Google Sheets.
* **Prompt mẫu Antigravity:**
  > "Đọc file `Bang_luong_chot.xlsx`. Với mỗi nhân viên, hãy tạo một bảng chi tiết phiếu lương đẹp mắt và tạo bản nháp (Draft) trên Gmail gửi tới địa chỉ email của nhân viên đó với tiêu đề '[Phiếu lương Tháng 11] - [Họ tên]'. Tuyệt đối chỉ gửi thông tin của đúng cá nhân đó."
* **Output & Điểm "Wow" khi Demo:** Kết hợp xử lý Excel với Gmail MCP: trong 1 phút tạo sẵn hàng chục bản nháp email cá nhân hóa có bảng HTML phiếu lương chỉnh chu, an toàn 100% vì HR vẫn duyệt lại trước khi bấm gửi.

### Ví dụ 5: Đọc hàng loạt CV (PDF/Word) trong thư mục và trích xuất vào bảng Excel theo dõi ứng viên (Liên thông PDF/Word -> Excel)
* **Bài toán & Nỗi đau:** Tuyển dụng nhận về 50 CV định dạng PDF/DOCX mỗi ngày. Ngồi mở từng CV để gõ Họ tên, SĐT, Email, Số năm kinh nghiệm, Trường đại học, Kỹ năng vào file Excel Tracking mất 2-3 tiếng.
* **Đầu vào (Input):** Thư mục `/CV_Ung_Vien` chứa 30 file PDF và Word.
* **Prompt mẫu Antigravity:**
  > "Đọc toàn bộ các file CV trong thư mục `/CV_Ung_Vien`. Trích xuất thông tin từng ứng viên gồm: Họ tên, SĐT (chuẩn hóa về dạng 09xx), Email, Vị trí ứng tuyển, Số năm kinh nghiệm, Công ty gần nhất, Học vấn, Kỹ năng chính, và chấm điểm độ phù hợp (thang 100) so với yêu cầu tuyển dụng Senior Marketing. Xuất ra file `Tracking_Ung_Vien.xlsx` sắp xếp từ điểm cao xuống thấp."
* **Output & Điểm "Wow" khi Demo:** Biến một đống file PDF lộn xộn thành bảng Excel sạch đẹp, có sẵn điểm đánh giá và nhận xét tóm tắt cho từng ứng viên.

### Ví dụ 6: Kiểm tra và cảnh báo hợp đồng lao động sắp hết hạn từ Google Sheets (Liên thông Sheets + Calendar/Gmail)
* **Bài toán & Nỗi đau:** HR lưu danh sách nhân sự trên Google Sheets nhưng thường quên ngày hết hạn thử việc hoặc hết hạn hợp đồng 1 năm, dẫn đến bị động khi gia hạn hoặc chấm dứt hợp đồng.
* **Đầu vào (Input):** File Google Sheets `Danh_sach_Nhan_su` trên Google Drive có cột `Ngày kết thúc HĐ`.
* **Prompt mẫu Antigravity:**
  > "Kết nối tới file Google Sheets `Danh_sach_Nhan_su` trên Google Drive. Lọc ra tất cả nhân sự có Hợp đồng thử việc hoặc Hợp đồng chính thức sẽ hết hạn trong vòng 30 ngày tới. Tạo một sheet mới tên `Canh_Bao_Gia_Han` trong file đó, đồng thời đặt lịch nhắc nhở trên Google Calendar của tôi trước ngày hết hạn 7 ngày cho từng trường hợp."
* **Output & Điểm "Wow" khi Demo:** Học viên thấy Antigravity tự động đọc Google Sheets, lọc ngày tháng thông minh và tạo thẳng sự kiện nhắc việc lên Google Calendar.

### Ví dụ 7: Làm sạch danh sách nhân sự đăng ký khám sức khỏe / bảo hiểm (Thuần Excel)
* **Bài toán & Nỗi đau:** Nhân viên tự điền form đăng ký khám sức khỏe: tên người viết hoa hết, người viết thường, ngày sinh người ghi `12/05/1995`, người ghi `1995-05-12`, người ghi `12.5.95`, số CCCD bị mất số `0` ở đầu, khoảng trắng thừa khắp nơi.
* **Đầu vào (Input):** File `dang_ky_kham_suc_khoe_raw.xlsx` đầy lỗi định dạng.
* **Prompt mẫu Antigravity:**
  > "Làm sạch file `dang_ky_kham_suc_khoe_raw.xlsx`: chuẩn hóa Họ tên viết hoa chữ cái đầu mỗi từ và bỏ khoảng trắng thừa; chuẩn hóa Ngày sinh về đúng định dạng `DD/MM/YYYY`; thêm lại số `0` ở đầu cho cột SĐT (đủ 10 số) và CCCD (đủ 12 số) dưới dạng Text; phát hiện và đánh dấu các dòng bị trùng lặp CCCD. Lưu thành file `danh_sach_chuan_gui_benh_vien.xlsx`."
* **Output & Điểm "Wow" khi Demo:** Những lỗi kinh điển nhất của Excel (mất số 0 đầu, loạn định dạng ngày tháng, lỗi viết hoa/thường) được xử lý sạch bóng không cần dùng `TRIM`, `PROPER`, `TEXT`, `DATEVALUE`.

### Ví dụ 8: Phân tích biến động nhân sự (Turnover Rate) và vẽ Dashboard nhân sự (Thuần Excel)
* **Bài toán & Nỗi đau:** Sếp yêu cầu báo cáo tỷ lệ nghỉ việc theo phòng ban, theo thâm niên và lý do nghỉ việc kèm biểu đồ trực quan, nhưng HR chỉ có danh sách nhân viên nghỉ việc thô.
* **Đầu vào (Input):** File `nhan_su_2026.xlsx` (Danh sách tổng và danh sách nghỉ việc kèm ngày vào, ngày nghỉ, phòng ban, lý do).
* **Prompt mẫu Antigravity:**
  > "Phân tích file `nhan_su_2026.xlsx` để lập báo cáo biến động nhân sự: tính tỷ lệ nghỉ việc (Turnover Rate) theo từng tháng, theo từng phòng ban, theo nhóm thâm niên (<6 tháng, 6-12 tháng, >1 năm) và thống kê tỷ trọng lý do nghỉ việc. Xuất ra file `HR_Turnover_Report.xlsx` có sẵn bảng tổng hợp và biểu đồ cột/tròn trực quan."
* **Output & Điểm "Wow" khi Demo:** Tạo ra ngay một file Excel có sẵn biểu đồ chuyên nghiệp (Native Excel Charts) để mang đi họp giao ban.

### Ví dụ 9: Tự động xếp lịch trực ca cho nhân viên theo ràng buộc (Thuần Excel)
* **Bài toán & Nỗi đau:** Xếp lịch trực 3 ca (Sáng, Chiều, Tối) cho 20 nhân viên trong tháng sao cho: không ai làm ca tối rồi sáng hôm sau làm ca sáng, mỗi người nghỉ ít nhất 1 ngày cuối tuần, và tích hợp danh sách ngày xin nghỉ phép cá nhân.
* **Đầu vào (Input):** File `danh_sach_nv_va_ngay_nghi_phep.xlsx`.
* **Prompt mẫu Antigravity:**
  > "Dựa trên danh sách nhân viên và ngày đăng ký nghỉ phép trong file `danh_sach_nv_va_ngay_nghi_phep.xlsx`, hãy xếp lịch phân ca tháng 11 (Ca Sáng: 3 người, Ca Chiều: 3 người, Ca Tối: 2 người mỗi ngày). Đảm bảo công bằng tổng số ca giữa các nhân viên, không ai trực Ca Tối hôm trước mà phải trực Ca Sáng hôm sau. Xuất ra bảng phân ca theo ma trận Ngày x Nhân viên, tô màu theo từng ca."
* **Output & Điểm "Wow" khi Demo:** Giải bài toán tối ưu hóa tổ hợp cực khó mà làm tay mất cả ngày tẩy xóa.

---

## PHẦN 2: KẾ TOÁN - TÀI CHÍNH (9 Ví dụ)

### Ví dụ 10: Đối soát sao kê ngân hàng với sổ quỹ nội bộ (Thuần Excel)
* **Bài toán & Nỗi đau:** Cuối tháng kế toán phải dò hàng nghìn giao dịch giữa file Sao kê ngân hàng và Sổ theo dõi thu chi nội bộ. Khó nhất là nội dung chuyển khoản ngân hàng viết tắt, dính chữ, hoặc khách chuyển gộp 2 hóa đơn làm 1 lệnh nên `VLOOKUP` bó tay.
* **Đầu vào (Input):** File `sao_ke_vietcombank.xlsx` và `so_thu_chi_noi_bo.xlsx`.
* **Prompt mẫu Antigravity:**
  > "Đối soát 2 file `sao_ke_vietcombank.xlsx` và `so_thu_chi_noi_bo.xlsx`. Hãy khớp các giao dịch dựa trên Số tiền, Ngày giao dịch (cho phép lệch tối đa 1 ngày) và nhận diện mờ (fuzzy matching) Mã hóa đơn/Tên khách hàng trong nội dung chuyển khoản. Tìm ra cả các trường hợp 1 lệnh chuyển khoản bằng tổng của 2-3 hóa đơn của cùng khách hàng. Xuất file `Ket_qua_doi_soat.xlsx` gồm 3 sheet: Đã khớp 1-1, Khớp gộp đơn, và Chênh lệch chưa rõ nguyên nhân."
* **Output & Điểm "Wow" khi Demo:** Khả năng Fuzzy Matching + tìm tổ hợp tổng tiền gộp hóa đơn làm kế toán "vỡ òa" vì bình thường phải ngồi dò bằng mắt từng dòng.

### Ví dụ 11: Trích xuất hàng loạt Hóa đơn điện tử (PDF/XML/Ảnh) vào bảng kê Excel (Liên thông PDF/Ảnh -> Excel)
* **Bài toán & Nỗi đau:** Nhân viên đi công tác mang về hàng chục hóa đơn PDF và ảnh chụp biên lai. Kế toán phải mở từng file gõ Số hóa đơn, Ngày, MST người bán, Tên công ty, Tiền trước thuế, Thuế suất, Tiền thuế, Tổng tiền vào Excel.
* **Đầu vào (Input):** Thư mục `/Hoa_Don_Thang_11` chứa các file PDF và ảnh chụp hóa đơn GTGT.
* **Prompt mẫu Antigravity:**
  > "Quét tất cả file PDF và ảnh trong thư mục `/Hoa_Don_Thang_11`. Trích xuất thông tin từng hóa đơn gồm: Ký hiệu, Số hóa đơn, Ngày lập, Tên đơn vị bán, Mã số thuế, Mặt hàng chính, Tiền chưa thuế, Thuế suất GTGT (8% hay 10%), Tiền thuế, Tổng thanh toán. Kiểm tra xem Tiền chưa thuế + Tiền thuế có khớp Tổng thanh toán không. Xuất ra file `Bang_ke_mua_vao_T11.xlsx`."
* **Output & Điểm "Wow" khi Demo:** Nhập liệu tự động 100% kèm bước tự kiểm tra chéo (cross-check) cộng trừ đúng sai trên hóa đơn.

### Ví dụ 12: Phân loại tuổi nợ (AR Aging Report) và tự động tạo email nhắc nợ khách hàng (Liên thông Excel + Gmail)
* **Bài toán & Nỗi đau:** Kế toán công nợ phải lọc danh sách hóa đơn chưa thanh toán, chia theo khung quá hạn (1-30 ngày, 31-60 ngày, 61-90 ngày, >90 ngày) rồi soạn email nhắc nợ với giọng văn tương ứng mức độ quá hạn.
* **Đầu vào (Input):** File `cong_no_phai_thu.xlsx` (Khách hàng, Email, Số HĐ, Ngày đến hạn, Số tiền phải thu, Đã thu).
* **Prompt mẫu Antigravity:**
  > "Đọc file `cong_no_phai_thu.xlsx`. Tính số ngày quá hạn tính đến hôm nay và phân bổ số dư nợ vào các cột tuổi nợ: Trong hạn, Quá hạn 1-30 ngày, 31-60 ngày, 61-90 ngày, và Trên 90 ngày. Sau đó, với những khách hàng quá hạn trên 15 ngày, hãy gom tất cả các hóa đơn nợ của họ lại và tạo bản nháp email nhắc thanh toán lịch sự trên Gmail."
* **Output & Điểm "Wow" khi Demo:** Ra ngay bảng Báo cáo tuổi nợ chuẩn kế toán quản trị, đồng thời tự gom nhiều hóa đơn của cùng 1 khách vào chung 1 email nhắc nợ.

### Ví dụ 13: Tự động phân bổ chi phí trả trước (242) và khấu hao TSCĐ hàng tháng (Thuần Excel)
* **Bài toán & Nỗi đau:** Theo dõi hàng trăm công cụ dụng cụ (máy tính, bàn ghế, phần mềm bản quyền) mua ở các ngày khác nhau trong tháng, thời gian phân bổ 12-24-36 tháng khác nhau, rất dễ tính sai số ngày sử dụng thực tế của tháng đầu tiên và tháng cuối cùng.
* **Đầu vào (Input):** File `danh_muc_chi_phi_tra_truoc.xlsx` (Tên tài sản, Ngày ghi tăng, Nguyên giá, Số tháng phân bổ).
* **Prompt mẫu Antigravity:**
  > "Từ file `danh_muc_chi_phi_tra_truoc.xlsx`, hãy lập bảng tính phân bổ chi phí từng tháng cho cả năm 2026. Lưu ý: tháng đầu tiên tính phân bổ theo số ngày thực tế sử dụng trong tháng, các tháng tiếp theo phân bổ tròn tháng, và kiểm tra không bao giờ phân bổ vượt quá Nguyên giá. Xuất ra file `Bang_phan_bo_242_2026.xlsx`."
* **Output & Điểm "Wow" khi Demo:** Xử lý gọn gàng logic ngày lẻ tháng đầu/tháng cuối và đảm bảo giá trị còn lại không bị âm.

### Ví dụ 14: Hợp nhất báo cáo P&L (Kết quả kinh doanh) từ nhiều chi nhánh/cửa hàng trên Google Drive (Liên thông Drive/Sheets)
* **Bài toán & Nỗi đau:** Công ty có 10 cửa hàng, mỗi cửa hàng cập nhật doanh thu - chi phí trên 1 file Google Sheets riêng trong thư mục Google Drive. Kế toán trưởng phải mở 10 tab trình duyệt để gom số liệu lên báo cáo hợp nhất.
* **Đầu vào (Input):** Thư mục Google Drive `Bao_Cao_Chi_Nhanh_T11` chứa 10 file Google Sheets.
* **Prompt mẫu Antigravity:**
  > "Truy cập thư mục `Bao_Cao_Chi_Nhanh_T11` trên Google Drive, đọc toàn bộ 10 file Google Sheets của các chi nhánh. Tổng hợp số liệu Doanh thu, Giá vốn, Chi phí bán hàng, Chi phí thuê mặt bằng, Chi phí nhân sự và Lợi nhuận ròng của từng chi nhánh vào một file Google Sheets tổng tên `Bao_Cao_P&L_Hop_Nhat_T11`, kèm cột tính tỷ suất lợi nhuận (% Margin) và xếp hạng chi nhánh hiệu quả nhất."
* **Output & Điểm "Wow" khi Demo:** Không cần tải file về máy, Antigravity làm việc trực tiếp với đám mây Google Drive để tổng hợp báo cáo tài chính hợp nhất.

### Ví dụ 15: Phát hiện giao dịch bất thường / gian lận chi phí trong bảng kê thanh toán (Thuần Excel)
* **Bài toán & Nỗi đau:** Khi duyệt bảng kê hoàn ứng công tác phí hàng nghìn dòng, kế toán khó phát hiện các hóa đơn bị kê khai trùng 2 lần (khác ngày nộp nhưng cùng số hóa đơn), hoặc chi vượt định mức quy định, hoặc tách nhỏ hóa đơn trong cùng 1 ngày để lách quyền phê duyệt.
* **Đầu vào (Input):** File `de_nghi_thanh_toan_Q3.xlsx` và quy chế chi tiêu (ví dụ: tiếp khách tối đa 500k/người, hóa đơn trên 20 triệu phải chuyển khoản).
* **Prompt mẫu Antigravity:**
  > "Kiểm toán file `de_nghi_thanh_toan_Q3.xlsx`: Hãy tìm và đánh dấu (Highlight màu vàng/đỏ) các dòng có dấu hiệu rủi ro sau: (1) Trùng số hóa đơn + MST nhà cung cấp dù khác người đề nghị, (2) Hóa đơn từ 20 triệu trở lên nhưng hình thức thanh toán là Tiền mặt, (3) Cùng 1 nhân viên thanh toán nhiều hóa đơn cùng 1 nhà cung cấp trong cùng 1 ngày có tổng trên 20 triệu (nghi vấn tách hóa đơn), (4) Chi phí tiếp khách vượt 500.000đ/người. Xuất báo cáo các lỗi phát hiện ra sheet riêng."
* **Output & Điểm "Wow" khi Demo:** Biến AI thành "Kiểm toán viên nội bộ" rà soát 100% giao dịch trong vài giây thay vì chỉ kiểm tra chọn mẫu.

### Ví dụ 16: Chuyển đổi số tiền bằng số sang chữ tiếng Việt/tiếng Anh hàng loạt trên phiếu thu/chi (Thuần Excel)
* **Bài toán & Nỗi đau:** Excel mặc định không có hàm đọc số thành chữ tiếng Việt ("Một trăm hai mươi lăm triệu đồng chẵn"). Dân văn phòng thường phải cài Add-in lạ dễ dính virus hoặc lỗi font VNI/TCVN3.
* **Đầu vào (Input):** File `danh_sach_phieu_chi.xlsx` có cột `Số tiền`.
* **Prompt mẫu Antigravity:**
  > "Đọc file `danh_sach_phieu_chi.xlsx`. Thêm 2 cột mới: `Bằng chữ (Tiếng Việt)` và `In Words (English)` đọc chính xác số tiền ở cột `Số tiền` theo đúng chuẩn kế toán (viết hoa chữ cái đầu, có chữ 'đồng chẵn' ở cuối). Sau đó tự động điền thông tin từng dòng vào mẫu Phiếu Chi ở sheet `Template` để sẵn sàng in."
* **Output & Điểm "Wow" khi Demo:** Không cần cài bất kỳ Add-in hay VBA Macro nào mà vẫn có cột đọc số thành chữ chuẩn xác cả tiếng Việt lẫn tiếng Anh.

### Ví dụ 17: Dự báo dòng tiền (Cashflow Forecast) 12 tuần tới từ lịch thu - chi (Thuần Excel)
* **Bài toán & Nỗi đau:** Doanh nghiệp có lãi trên giấy tờ nhưng hết tiền mặt để trả lương vì lệch kỳ hạn thu tiền khách hàng và kỳ hạn trả tiền nhà cung cấp.
* **Đầu vào (Input):** File `ke_hoach_dong_tien.xlsx` gồm 3 sheet: Số dư tiền đầu kỳ, Lịch phải thu khách hàng, Lịch phải trả nhà cung cấp & chi phí cố định (lương, thuê nhà, thuế).
* **Prompt mẫu Antigravity:**
  > "Dựa trên 3 sheet trong file `ke_hoach_dong_tien.xlsx`, hãy lập bảng Dự báo dòng tiền (Cashflow Forecast) theo từng tuần trong 12 tuần tới. Giả định 2 kịch bản: Kịch bản Cơ sở (khách trả đúng hạn) và Kịch bản Thận trọng (30% khách hàng lớn trả chậm 2 tuần). Cảnh báo màu đỏ những tuần nào Số dư tiền cuối kỳ rơi xuống dưới mức an toàn 500 triệu đồng."
* **Output & Điểm "Wow" khi Demo:** Tạo ngay mô hình tài chính đa kịch bản (Scenario Modeling) giúp sếp và kế toán nhìn thấy trước điểm "đứt dòng tiền".

### Ví dụ 18: Tự động hạch toán định khoản Nợ/Có từ nội dung diễn giải giao dịch (Thuần Excel)
* **Bài toán & Nỗi đau:** Kế toán viên mới hoặc kế toán dịch vụ phải ngồi gõ tay Tài khoản Nợ / Tài khoản Có (theo Thông tư 200 hoặc 133) cho hàng trăm dòng giao dịch thu chi ngân hàng và tiền mặt trước khi import vào phần mềm MISA/Fast.
* **Đầu vào (Input):** File `giao_dich_thang_11_raw.xlsx` chỉ có Ngày, Nội dung diễn giải, Số tiền Thu/Chi và File mẫu import của MISA.
* **Prompt mẫu Antigravity:**
  > "Đọc file `giao_dich_thang_11_raw.xlsx`. Dựa vào cột Nội dung diễn giải (ví dụ: 'Thanh toán tiền điện T10', 'Thu tiền hàng công ty ABC', 'Trả lương NV T10', 'Nộp BHXH'), hãy tự động điền Tài khoản Nợ và Tài khoản Có tương ứng theo Thông tư 200, sau đó định dạng lại đúng chuẩn các cột của file mẫu Import MISA `misa_import_template.xlsx`."
* **Output & Điểm "Wow" khi Demo:** AI đọc hiểu tiếng Việt trong diễn giải giao dịch để tự định khoản kế toán và xuất ra đúng chuẩn file import phần mềm kế toán.

---

## PHẦN 3: KINH DOANH - CHĂM SÓC KHÁCH HÀNG (9 Ví dụ)

### Ví dụ 19: Làm sạch, chuẩn hóa và lọc trùng dữ liệu khách hàng (CRM Data Cleaning) (Thuần Excel)
* **Bài toán & Nỗi đau:** Nhiều nhân viên Sales cùng nhập danh sách khách hàng: SĐT người có `+84`, người có dấu chấm `0912.345.678`, tên công ty người ghi `Công ty TNHH ABC`, người ghi `Cty ABC`, dẫn đến 1 khách hàng bị 2-3 Sales cùng gọi điện làm phiền.
* **Đầu vào (Input):** File `data_khach_hang_tong_hop.xlsx` (5.000 dòng lộn xộn).
* **Prompt mẫu Antigravity:**
  > "Làm sạch file `data_khach_hang_tong_hop.xlsx`: Chuẩn hóa toàn bộ SĐT về dạng 10 số bắt đầu bằng số 0 (xóa dấu chấm, dấu gạch ngang, đổi +84 thành 0). Chuẩn hóa tên công ty (đưa 'Cty', 'CT TNHH' về chuẩn 'Công ty TNHH'). Phát hiện các khách hàng trùng SĐT hoặc tên công ty tương đồng trên 85%, giữ lại dòng có cập nhật mới nhất và gộp lịch sử ghi chú chăm sóc vào chung 1 ô."
* **Output & Điểm "Wow" khi Demo:** Xử lý trùng lặp thông minh (cả trùng SĐT lẫn trùng tên công ty viết tắt) và **không làm mất ghi chú lịch sử** khi gộp dòng.

### Ví dụ 20: Tính hoa hồng lũy tiến nhiều tầng cho đội ngũ Sales và Trưởng nhóm (Thuần Excel)
* **Bài toán & Nỗi đau:** Chính sách hoa hồng phức tạp: Đạt <80% KPI không có thưởng; 80-100% hưởng 3%; phần vượt 100-120% hưởng 5%; phần vượt >120% hưởng 8%; cộng thêm thưởng nóng nếu bán được sản phẩm chiến lược, và trích 1.5% doanh số cả nhóm cho Team Leader.
* **Đầu vào (Input):** File `doanh_so_sales_T11.xlsx` (Danh sách đơn hàng, Nhân viên, Nhóm, Nhóm sản phẩm, Doanh thu thực thu) và bảng chỉ tiêu KPI từng người.
* **Prompt mẫu Antigravity:**
  > "Từ file `doanh_so_sales_T11.xlsx`, hãy tính bảng thưởng hoa hồng tháng 11 cho từng Sales và Team Leader theo đúng chính sách bậc thang lũy tiến của công ty. Lưu ý chỉ tính hoa hồng trên các đơn hàng có trạng thái 'Đã thu đủ tiền'. Xuất ra file `Bang_tinh_hoa_hong_T11.xlsx` hiển thị rõ từng phần hoa hồng theo từng bậc để Sales dễ đối chiếu."
* **Output & Điểm "Wow" khi Demo:** Minh bạch hóa từng bậc hoa hồng ra các cột riêng biệt, xóa bỏ hoàn toàn tranh cãi giữa Sales và Kế toán mỗi kỳ tính thưởng.

### Ví dụ 21: Phân nhóm khách hàng VIP / Ngủ đông bằng mô hình RFM (Recency - Frequency - Monetary) (Thuần Excel)
* **Bài toán & Nỗi đau:** Công ty có danh sách 20.000 đơn hàng trong 2 năm qua nhưng không biết khách nào là VIP sắp rời bỏ để chăm sóc lại, khách nào mua thường xuyên, khách nào chỉ mua 1 lần rồi mất hút.
* **Đầu vào (Input):** File `lich_su_don_hang_2025_2026.xlsx` (Mã KH, Tên KH, SĐT, Ngày mua, Giá trị đơn hàng).
* **Prompt mẫu Antigravity:**
  > "Áp dụng mô hình RFM lên file `lich_su_don_hang_2025_2026.xlsx`: Tính số ngày từ lần mua cuối (Recency), tổng số lần mua (Frequency), và tổng tiền đã chi (Monetary) của từng khách hàng. Chấm điểm R, F, M theo thang 1-5 và phân loại khách hàng thành các nhóm: 'VIP/Champions', 'Khách trung thành', 'Khách lớn có nguy cơ rời bỏ (At Risk)', 'Khách ngủ đông'. Xuất danh sách từng nhóm ra các sheet riêng kèm gợi ý kịch bản chăm sóc."
* **Output & Điểm "Wow" khi Demo:** Đưa một kỹ thuật phân tích dữ liệu cao cấp (Data Analytics RFM) xuống thành 1 câu lệnh đơn giản cho dân văn phòng không biết code.

### Ví dụ 22: Tự động tạo 20 file Báo giá / Hợp đồng (Excel/PDF) từ bảng danh sách yêu cầu của khách (Liên thông Excel -> Báo giá)
* **Bài toán & Nỗi đau:** Mỗi ngày Sales Admin phải làm 15-20 báo giá theo file mẫu của công ty: tra mã sản phẩm lấy đơn giá, tính chiết khấu theo số lượng, điền thông tin khách hàng, căn chỉnh trang in rồi xuất PDF gửi cho Sales.
* **Đầu vào (Input):** File `danh_sach_yeu_cau_bao_gia.xlsx`, `bang_gia_san_pham.xlsx` và `mau_bao_gia_chuan.xlsx`.
* **Prompt mẫu Antigravity:**
  > "Dựa vào các yêu cầu báo giá trong `danh_sach_yeu_cau_bao_gia.xlsx`, hãy tra cứu đơn giá từ `bang_gia_san_pham.xlsx`, áp dụng chiết khấu 5% cho đơn hàng trên 50 triệu, và tự động điền vào `mau_bao_gia_chuan.xlsx`. Xuất ra từng file báo giá riêng biệt cho từng khách hàng theo tên `Bao_Gia_[Ten_Khach_Hang]_[Ngay].xlsx` trong thư mục `/Bao_Gia_Da_Tao`."
* **Output & Điểm "Wow" khi Demo:** Tạo hàng loạt file báo giá chuẩn chỉnh theo đúng nhận diện thương hiệu (giữ nguyên logo, khung viền, công thức tổng cộng) chỉ trong vài giây.

### Ví dụ 23: Phân tích nguyên nhân mất khách (Win/Loss Analysis) từ ghi chú tự do của Sales (Thuần Excel + AI Text Analysis)
* **Bài toán & Nỗi đau:** Cột "Ghi chú lý do khách từ chối" trên file CRM chứa hàng nghìn câu văn tự do của Sales ("khách chê đắt hơn bên X", "gọi không nghe máy 3 lần", "sếp khách chưa duyệt ngân sách", "cần tính năng Y mà mình chưa có"). Quản lý không thể dùng PivotTable để thống kê cột văn bản tự do này.
* **Đầu vào (Input):** File `crm_lost_deals.xlsx` có cột `Ghi chú của Sales`.
* **Prompt mẫu Antigravity:**
  > "Đọc cột `Ghi chú của Sales` trong file `crm_lost_deals.xlsx`. Hãy phân tích nội dung từng ghi chú và gán nhãn chuẩn hóa vào cột mới `Nhóm lý do thất bại` gồm: Giá cao, Thiếu tính năng, Đối thủ cạnh tranh, Không liên lạc được, Chưa có ngân sách, Lý do khác. Sau đó lập bảng Pivot thống kê tỷ lệ % từng nhóm lý do theo từng dòng sản phẩm."
* **Output & Điểm "Wow" khi Demo:** Điểm mạnh tuyệt đối của AI so với Excel truyền thống: biến dữ liệu văn bản lộn xộn (Unstructured Text) thành danh mục chuẩn hóa (Structured Categories) để làm PivotTable.

### Ví dụ 24: Chia giỏ Data khách hàng (Lead Routing) tự động lên Google Sheets và phân quyền cho từng Sales (Liên thông Drive/Sheets)
* **Bài toán & Nỗi đau:** Marketing đổ về 500 leads mới mỗi tuần. Trưởng phòng Sales phải chia đều data theo khu vực (Miền Bắc/Miền Nam) và ngành hàng cho 10 bạn Sales, sau đó copy vào từng file Google Sheets riêng của từng bạn để bảo mật thông tin khách hàng.
* **Đầu vào (Input):** File `lead_moi_tuan_45.xlsx` và danh sách 10 file Google Sheets cá nhân của 10 Sales trên Google Drive.
* **Prompt mẫu Antigravity:**
  > "Đọc file `lead_moi_tuan_45.xlsx`. Hãy chia đều các leads khu vực Hà Nội cho 5 Sales miền Bắc và TP.HCM cho 5 Sales miền Nam theo hình thức xoay vòng (Round-robin), ưu tiên các lead có quy mô >100 nhân sự cho các Senior Sales. Sau đó tự động nối (append) danh sách lead đã chia vào đúng file Google Sheets cá nhân của từng bạn trên Google Drive."
* **Output & Điểm "Wow" khi Demo:** Tự động hóa trọn vẹn quy trình chia Lead phức tạp và đẩy thẳng lên Google Sheets của từng nhân viên mà không sợ lộ data tổng.

### Ví dụ 25: Theo dõi tiến độ mục tiêu doanh số từng ngày (Run-rate & Pacing Dashboard) (Thuần Excel)
* **Bài toán & Nỗi đau:** Đang ở ngày 18 của tháng, Giám đốc kinh doanh muốn biết với tốc độ bán hàng hiện tại thì cuối tháng từng nhân viên và từng khu vực dự kiến đạt bao nhiêu % KPI, ai cần phải tăng tốc bao nhiêu tiền mỗi ngày còn lại.
* **Đầu vào (Input):** File `doanh_so_luy_ke_ngay_18.xlsx` và `kpi_thang_11.xlsx`.
* **Prompt mẫu Antigravity:**
  > "Kết hợp 2 file doanh số lũy kế đến ngày 18/11 và bảng KPI tháng 11. Hãy tính: % Hoàn thành hiện tại, Doanh số trung bình/ngày đã đạt, Dự phóng doanh số cuối tháng (Run-rate) theo số ngày làm việc thực tế, và Doanh số mục tiêu cần đạt mỗi ngày trong các ngày làm việc còn lại của tháng để cán đích 100% KPI. Định dạng Data Bars và Icon Sets trực quan trên bảng."
* **Output & Điểm "Wow" khi Demo:** Tạo ra báo cáo quản trị điều hành sắc bén kèm Conditional Formatting (Data Bars / Icon đèn giao thông Xanh-Vàng-Đỏ) ngay trong file Excel.

### Ví dụ 26: Tổng hợp báo cáo khảo sát mức độ hài lòng khách hàng (CSAT / NPS) (Thuần Excel)
* **Bài toán & Nỗi đau:** Sau sự kiện hoặc sau mua hàng, bộ phận CSKH xuất file kết quả từ Google Forms gồm điểm số (1-10) và câu trả lời góp ý mở. Cần tính chỉ số NPS (% Promoters trừ % Detractors) và tóm tắt các phàn nàn chính.
* **Đầu vào (Input):** File `khao_sat_khach_hang_Q4.xlsx`.
* **Prompt mẫu Antigravity:**
  > "Phân tích file `khao_sat_khach_hang_Q4.xlsx`: Phân loại khách hàng chấm 9-10 điểm là Promoters, 7-8 là Passives, 0-6 là Detractors để tính chỉ số NPS chung và NPS theo từng chi nhánh. Đồng thời phân tích cột 'Ý kiến đóng góp' để gom nhóm Top 5 vấn đề khách hàng phàn nàn nhiều nhất kèm trích dẫn tiêu biểu."
* **Output & Điểm "Wow" khi Demo:** Vừa tính toán chỉ số thống kê NPS, vừa đọc hiểu tiếng Việt để rút trích insight khách hàng trong cùng 1 báo cáo Excel.

### Ví dụ 27: Chuyển ảnh chụp danh thiếp (Namecard) tại hội thảo thành danh sách Excel & soạn email kết nối (Liên thông Ảnh -> Excel + Gmail)
* **Bài toán & Nỗi đau:** Đi hội thảo về cầm theo 40 tấm danh thiếp (Namecard). Ngồi gõ từng tên, chức danh, công ty, SĐT, email vào Excel rồi gửi mail chào hỏi mất cả buổi sáng hôm sau.
* **Đầu vào (Input):** Thư mục `/Namecards_Hoi_Thao` chứa ảnh chụp các danh thiếp (có thể chụp 4-5 danh thiếp trong 1 bức ảnh).
* **Prompt mẫu Antigravity:**
  > "Đọc tất cả ảnh trong thư mục `/Namecards_Hoi_Thao`. Trích xuất thông tin từng danh thiếp ra file `Danh_ba_doi_tac_hoi_thao.xlsx` gồm: Họ tên, Chức vụ, Công ty, SĐT, Email, Website, Địa chỉ. Sau đó tạo sẵn bản nháp Gmail gửi lời chào kết nối sau hội thảo được cá nhân hóa theo Tên và Chức vụ của từng người."
* **Output & Điểm "Wow" khi Demo:** Chụp 5 cái namecard trong 1 tấm ảnh, AI vẫn bóc tách chuẩn thành 5 dòng Excel và tạo xong 5 email nháp.

---

## PHẦN 4: MARKETING - THƯƠNG MẠI ĐIỆN TỬ (8 Ví dụ)

### Ví dụ 28: Gộp và chuẩn hóa báo cáo quảng cáo đa kênh (Facebook Ads, Google Ads, TikTok Ads) (Thuần Excel)
* **Bài toán & Nỗi đau:** Mỗi nền tảng quảng cáo xuất ra file CSV/Excel với tên cột và đơn vị khác nhau (Facebook gọi là `Amount Spent`, Google gọi là `Cost`, TikTok gọi là `Total Cost`; định dạng ngày tháng khác nhau). Marketer mất hàng giờ mỗi sáng để gộp lại tính tổng chi phí và ROAS.
* **Đầu vào (Input):** 3 file `fb_ads_export.csv`, `google_ads_export.csv`, `tiktok_ads_export.xlsx`.
* **Prompt mẫu Antigravity:**
  > "Đọc 3 file báo cáo quảng cáo từ Facebook, Google và TikTok. Hãy chuẩn hóa về cùng cấu trúc cột: Ngày, Kênh (Platform), Tên chiến dịch, Chi phí (VNĐ), Lượt hiển thị (Impressions), Lượt nhấp (Clicks), CTR (%), Số chuyển đổi (Conversions), Chi phí/Chuyển đổi (CPA). Gộp tất cả vào file `Master_Ads_Report.xlsx` và tạo bảng tổng hợp so sánh hiệu quả giữa 3 kênh."
* **Output & Điểm "Wow" khi Demo:** Xử lý sạch lỗi lệch bảng mã CSV (UTF-8), lệch tên cột tiếng Anh/Việt và tự tính các chỉ số phái sinh (CTR, CPC, CPA).

### Ví dụ 29: Đối soát doanh thu và phí sàn Thương mại điện tử (Shopee, TikTok Shop, Lazada) (Thuần Excel)
* **Bài toán & Nỗi đau:** Bán hàng trên Shopee/TikTok Shop có hàng chục loại phí trừ lắt nhắt (phí cố định, phí thanh toán, phí hoa hồng tiếp thị liên kết Affiliate, phí chương trình hoàn xu, mã giảm giá shop tài trợ, phí vận chuyển chênh lệch). Nhiều shop bán nghìn đơn nhưng không biết đơn nào thực lãi, đơn nào đang lỗ.
* **Đầu vào (Input):** File `doanh_thu_shopee_thang_10.xlsx` (xuất từ Seller Centre) và `bang_gia_von_sku.xlsx`.
* **Prompt mẫu Antigravity:**
  > "Kết hợp file báo cáo đơn hàng Shopee `doanh_thu_shopee_thang_10.xlsx` và bảng giá vốn `bang_gia_von_sku.xlsx`. Với từng đơn hàng và từng mã SKU, hãy tính: Doanh thu gốc, Tổng các loại phí sàn thu, Tiền thực nhận về ví, Giá vốn hàng bán, Lợi nhuận ròng thực tế và % Biên lợi nhuận. Lọc ra danh sách các đơn hàng hoặc mã SKU đang bị bán lỗ (Lợi nhuận âm) ra một sheet cảnh báo riêng."
* **Output & Điểm "Wow" khi Demo:** Bóc tách "ma trận" phí sàn TMĐT và chỉ điểm ngay những mã sản phẩm nhìn tưởng bán chạy nhưng thực chất đang gồng lỗ.

### Ví dụ 30: Tự động tạo link UTM Tracking hàng loạt cho chiến dịch Marketing (Thuần Excel)
* **Bài toán & Nỗi đau:** Khi chạy chiến dịch lớn với 50 bài đăng qua 10 KOLs, 5 kênh mạng xã hội và 3 landing page khác nhau, việc gắn tham số `utm_source`, `utm_medium`, `utm_campaign`, `utm_content` thủ công rất dễ gõ dấu cách, dấu tiếng Việt hoặc viết hoa/thường không đồng nhất làm hỏng báo cáo Google Analytics.
* **Đầu vào (Input):** File `ke_hoach_content_kols.xlsx` (Cột: Link gốc, Tên chiến dịch, Kênh, Tên KOL, Định dạng bài).
* **Prompt mẫu Antigravity:**
  > "Đọc file `ke_hoach_content_kols.xlsx`. Hãy tự động chuẩn hóa các cột Tên chiến dịch, Kênh, Tên KOL về dạng chữ thường không dấu, nối bằng dấu gạch ngang (`snake_case` hoặc `kebab-case`), sau đó ghép thành đường dẫn Full UTM URL hoàn chỉnh và tạo thêm công thức tạo mã QR cho từng link."
* **Output & Điểm "Wow" khi Demo:** Tự động bỏ dấu tiếng Việt, chuẩn hóa quy tắc đặt tên UTM không sai 1 ký tự cho hàng trăm link chiến dịch.

### Ví dụ 31: Phân tích bình luận / đánh giá 1-5 sao của khách hàng trên sàn TMĐT (Thuần Excel + AI Sentiment)
* **Bài toán & Nỗi đau:** Tải về 3.000 đánh giá (Reviews) của khách hàng trên Shopee/Google Maps. Làm sao biết sản phẩm bị chê vì "giao hàng chậm", "đóng gói móp méo" hay vì "chất lượng sản phẩm lỗi" để cải thiện?
* **Đầu vào (Input):** File `shopee_reviews_export.xlsx` (Mã SP, Số sao, Nội dung bình luận).
* **Prompt mẫu Antigravity:**
  > "Phân tích file `shopee_reviews_export.xlsx`. Với các đánh giá từ 1 đến 3 sao, hãy đọc nội dung bình luận để phân loại nguyên nhân phàn nàn vào các nhóm: Chất lượng sản phẩm, Đóng gói/Bao bì, Giao hàng/Vận chuyển, Tư vấn CSKH, Sai mẫu/Thiếu hàng. Lập bảng ma trận thống kê từng Mã sản phẩm đang bị lỗi nào nhiều nhất."
* **Output & Điểm "Wow" khi Demo:** Biến hàng nghìn dòng bình luận cảm tính thành bảng số liệu định lượng rõ ràng để làm việc với bộ phận Kho và Sản xuất.

### Ví dụ 32: Lập kế hoạch phân bổ ngân sách Marketing (Media Plan) tự động theo mục tiêu KPI (Thuần Excel)
* **Bài toán & Nỗi đau:** Sếp giao ngân sách 500 triệu cho Quý 4 với mục tiêu mang về 2.500 khách hàng tiềm năng (Leads). Marketer phải ngồi thử từng con số trên Excel dựa vào đơn giá CPL (Cost per Lead) lịch sử của từng kênh để chia tiền sao cho tối ưu.
* **Đầu vào (Input):** File `lich_su_hieu_qua_kenh.xlsx` (Chứa CPL trung bình, tỷ lệ chuyển đổi từ Lead sang Khách mua và giới hạn ngân sách tối đa của từng kênh).
* **Prompt mẫu Antigravity:**
  > "Dựa trên dữ liệu hiệu quả lịch sử trong `lich_su_hieu_qua_kenh.xlsx`, hãy lập bảng Media Plan phân bổ 500 triệu VNĐ vào các kênh (Facebook, Google Search, TikTok, Zalo, KOLs) theo từng tháng trong Quý 4 sao cho tối đa hóa số lượng Khách hàng mua thực tế, đồng thời không vượt quá ngưỡng bão hòa ngân sách của từng kênh. Đưa ra 2 phương án: Tối ưu số lượng Lead và Tối ưu Doanh thu."
* **Output & Điểm "Wow" khi Demo:** Thay thế công cụ Solver phức tạp của Excel bằng lời giải tối ưu hóa ngân sách kèm bảng Media Plan sẵn sàng trình sếp.

### Ví dụ 33: Nghiên cứu từ khóa SEO: Gom nhóm chủ đề (Keyword Clustering) và phân loại Search Intent (Thuần Excel)
* **Bài toán & Nỗi đau:** Xuất từ công cụ Ahrefs/Semrush ra 2.000 từ khóa kèm Volume tìm kiếm. Người làm Content SEO mất cả tuần để ngồi lọc từ khóa trùng ý nghĩa và chia thành các nhóm bài viết (Topic Clusters).
* **Đầu vào (Input):** File `keywords_export_ahrefs.xlsx` (Keyword, Search Volume, Keyword Difficulty).
* **Prompt mẫu Antigravity:**
  > "Đọc danh sách từ khóa trong `keywords_export_ahrefs.xlsx`. Hãy phân loại Ý định tìm kiếm (Search Intent: Informational, Commercial, Transactional), gom các từ khóa có cùng chủ đề ngữ nghĩa vào chung một `Topic Cluster` (chọn từ khóa có Volume cao nhất làm Từ khóa chính - Primary Keyword, các từ còn lại làm Secondary Keywords), và gợi ý Tiêu đề bài viết chuẩn SEO cho từng nhóm."
* **Output & Điểm "Wow" khi Demo:** Rút ngắn 1 tuần làm kế hoạch Content SEO xuống còn 1 phút chạy lệnh.

### Ví dụ 34: Kiểm tra tồn kho quà tặng sự kiện (POSM) và tự động lên danh sách chia hàng cho các điểm bán (Thuần Excel)
* **Bài toán & Nỗi đau:** Trước chiến dịch khuyến mãi Tết, Trade Marketing phải chia 15 loại quà tặng (áo mưa, mũ bảo hiểm, standee, voucher) về 80 đại lý theo tỷ lệ doanh số của từng đại lý, nhưng phải làm tròn theo quy cách đóng thùng (ví dụ: 1 thùng = 20 cái).
* **Đầu vào (Input):** File `ton_kho_posm_va_doanh_so_dai_ly.xlsx`.
* **Prompt mẫu Antigravity:**
  > "Dựa vào file `ton_kho_posm_va_doanh_so_dai_ly.xlsx`, hãy phân bổ số lượng từng loại quà tặng POSM cho 80 đại lý theo tỷ trọng doanh số Quý 3. Lưu ý: mỗi đại lý phải nhận tối thiểu 1 thùng, số lượng làm tròn theo quy cách đóng thùng của từng vật phẩm, và tổng số lượng phân bổ phải khớp đúng 100% số lượng tồn kho hiện có."
* **Output & Điểm "Wow" khi Demo:** Giải quyết bài toán làm tròn phân bổ (Rounding Allocation) không bị lệch tổng — nỗi ám ảnh kinh điển khi dùng hàm `ROUND` trong Excel.

### Ví dụ 35: Tự động tạo lịch đăng bài (Content Calendar) trên Google Sheets và tạo thư mục chứa ảnh/video trên Google Drive (Liên thông Sheets + Drive)
* **Bài toán & Nỗi đau:** Khi lên kế hoạch 30 bài đăng trong tháng trên Google Sheets, Content phải vào Google Drive tạo tay 30 thư mục con theo mã bài viết rồi copy link từng thư mục dán ngược lại vào cột "Link Asset" trên Google Sheets cho Designer bỏ ảnh vào.
* **Đầu vào (Input):** File Google Sheets `Content_Calendar_T11` chứa danh sách 30 bài viết dự kiến.
* **Prompt mẫu Antigravity:**
  > "Đọc danh sách 30 bài viết trong file Google Sheets `Content_Calendar_T11`. Với mỗi bài viết, hãy tự động tạo một thư mục con tương ứng theo cú pháp `[Mã bài] - [Ngày đăng] - [Chủ đề]` bên trong thư mục Google Drive `/Marketing_Assets_T11`, sau đó lấy đường link của từng thư mục vừa tạo điền trực tiếp vào cột `Link Thư mục Thiết kế` trên file Google Sheets."
* **Output & Điểm "Wow" khi Demo:** Màn trình diễn kết nối Google Drive + Google Sheets cực kỳ ấn tượng: thư mục tự sinh ra trên mây và link tự nhảy vào từng dòng bảng tính.

---

## PHẦN 5: MUA HÀNG - KHO VẬN - CHUỖI CUNG ỨNG (8 Ví dụ)

### Ví dụ 36: So sánh báo giá từ 5 Nhà cung cấp (Vendor Quotation Comparison) để chọn phương án mua tối ưu (Thuần Excel)
* **Bài toán & Nỗi đau:** Cần mua 50 mặt hàng vật tư. 5 nhà cung cấp gửi về 5 file báo giá: chỗ báo giá đã gồm VAT, chỗ chưa VAT, chiết khấu thương mại khác nhau, phí vận chuyển và thời gian công nợ (Payment Term) khác nhau.
* **Đầu vào (Input):** Thư mục `/Bao_Gia_NCC` chứa 5 file Excel báo giá của 5 nhà cung cấp.
* **Prompt mẫu Antigravity:**
  > "Đọc 5 file báo giá trong thư mục `/Bao_Gia_NCC`. Quy đổi toàn bộ đơn giá của 50 mặt hàng về cùng mặt bằng: Đơn giá thực tế sau chiết khấu, chưa VAT, đã cộng phân bổ phí vận chuyển. Tạo bảng Ma trận so sánh giá giữa 5 NCC, tô màu xanh lá cho NCC có giá thấp nhất ở từng mặt hàng, và đề xuất 2 phương án: (1) Mua tối ưu giá từng món và (2) Mua trọn gói tại 1 NCC có tổng chi phí thấp nhất."
* **Output & Điểm "Wow" khi Demo:** Tự động chuẩn hóa đơn giá về cùng hệ quy chiếu và lập bảng so sánh báo giá (Bid Tabulation) chuẩn quy trình đấu thầu mua hàng.

### Ví dụ 37: Cảnh báo hàng tồn kho sắp hết (Reorder Point) và tính số lượng cần đặt hàng tự động (Thuần Excel)
* **Bài toán & Nỗi đau:** Nhân viên mua hàng thường đặt hàng theo cảm tính: mặt hàng bán chạy thì đứt kho (Out of stock), mặt hàng bán chậm thì tồn đọng vốn.
* **Đầu vào (Input):** File `ton_kho_va_toc_do_ban.xlsx` (Mã hàng, Tồn hiện tại, Hàng đang về, Lịch sử xuất kho 90 ngày qua, Thời gian giao hàng của NCC - Lead time).
* **Prompt mẫu Antigravity:**
  > "Từ file `ton_kho_va_toc_do_ban.xlsx`, hãy tính tốc độ tiêu thụ trung bình/ngày của từng mã hàng, mức tồn kho an toàn (Safety Stock = 7 ngày bán), và Điểm đặt hàng lại (Reorder Point = Tốc độ bán x Lead time + Safety Stock). Lọc ra các mã hàng cần phải đặt mua ngay hôm nay và tính số lượng cần đặt để đủ bán trong 45 ngày tới (làm tròn theo MOQ - số lượng đặt tối thiểu của NCC)."
* **Output & Điểm "Wow" khi Demo:** Biến file tồn kho tĩnh thành hệ thống hoạch định mua hàng thông minh (MRP thu nhỏ).

### Ví dụ 38: Phân tích tồn kho ABC - XYZ và cảnh báo hàng cận Date / hàng chết (Dead Stock) (Thuần Excel)
* **Bài toán & Nỗi đau:** Kho có 2.000 mã hàng kèm hạn sử dụng (Shelf-life). Thủ kho không kịp rà soát lô hàng nào sắp hết hạn sử dụng trong 3-6 tháng tới hoặc mã hàng nào đã nằm im 180 ngày không xuất bán.
* **Đầu vào (Input):** File `ton_kho_chi_tiet_theo_lo.xlsx` (Mã SKU, Số lô, Ngày sản xuất, Hạn sử dụng, Số lượng tồn, Giá trị tồn, Ngày xuất kho gần nhất).
* **Prompt mẫu Antigravity:**
  > "Phân tích file `ton_kho_chi_tiet_theo_lo.xlsx`: (1) Phân nhóm ABC theo giá trị tồn kho (Nhóm A chiếm 80% giá trị, B chiếm 15%, C chiếm 5%); (2) Lọc ra các lô hàng có thời hạn sử dụng còn lại dưới 90 ngày hoặc dưới 30% tổng vòng đời sản phẩm; (3) Lọc ra danh sách Hàng chậm luân chuyển (Slow-moving >90 ngày không xuất) và Hàng chết (Dead stock >180 ngày). Xuất báo cáo ra 3 sheet kèm biểu đồ tổng hợp giá trị vốn bị đọng."
* **Output & Điểm "Wow" khi Demo:** Giúp chủ doanh nghiệp và kế toán kho nhìn thấy ngay bao nhiêu trăm triệu đồng đang nằm chết trong kho hoặc sắp hết hạn.

### Ví dụ 39: Tính toán nhu cầu nguyên vật liệu (BOM Explosion) từ kế hoạch sản xuất/đơn hàng (Thuần Excel)
* **Bài toán & Nỗi đau:** Khách đặt 5 loại thành phẩm với số lượng khác nhau. Mỗi thành phẩm lại cấu thành từ hàng chục linh kiện/nguyên liệu (định mức BOM nhiều cấp, có tỷ lệ hao hụt riêng). Tính tay rất dễ đặt thiếu nguyên liệu làm đình trệ chuyền sản xuất.
* **Đầu vào (Input):** File `ke_hoach_san_xuat.xlsx`, `dinh_muc_bom.xlsx` và `ton_kho_nguyen_lieu.xlsx`.
* **Prompt mẫu Antigravity:**
  > "Kết hợp 3 file: Kế hoạch sản xuất, Định mức BOM (gồm cả % hao hụt định mức) và Tồn kho nguyên vật liệu. Hãy tính tổng nhu cầu từng loại nguyên vật liệu cần dùng, đối chiếu với tồn kho thực tế để tính ra số lượng nguyên vật liệu còn thiếu cần mua thêm, và cho biết nếu không mua kịp thì tối đa sản xuất được bao nhiêu thành phẩm với lượng tồn hiện có."
* **Output & Điểm "Wow" khi Demo:** Xử lý bài toán nổ định mức BOM (BOM Explosion) và bài toán giới hạn năng lực sản xuất cực nhanh.

### Ví dụ 40: Đối soát bảng kê cước phí vận chuyển (Giao Hàng Nhanh / ViettelPost / J&T) và tiền thu hộ COD (Thuần Excel)
* **Bài toán & Nỗi đau:** Cuối tháng đơn vị vận chuyển gửi bảng kê 5.000 vận đơn. Shop/Công ty thường bị tính sai trọng lượng quy đổi, thu sai phí vùng sâu vùng xa, hoặc đơn hoàn về nhưng vẫn bị tính phí hai chiều, hoặc tiền COD thu hộ chưa chuyển trả đủ.
* **Đầu vào (Input):** File `bang_ke_cuoc_vtp.xlsx`, `danh_sach_don_gui_di.xlsx` (có trọng lượng chuẩn của từng SP) và `bang_gia_hop_dong_van_chuyen.xlsx`.
* **Prompt mẫu Antigravity:**
  > "Đối soát bảng kê của hãng vận chuyển `bang_ke_cuoc_vtp.xlsx` với dữ liệu đơn hàng nội bộ và bảng giá hợp đồng. Hãy kiểm tra: (1) Đơn nào bị hãng vận chuyển cân vọt trọng lượng so với trọng lượng chuẩn của sản phẩm trong đơn, (2) Đơn nào tính sai bậc cước phí theo tỉnh/thành, (3) Đơn nào trạng thái 'Đã giao thành công' nhưng chưa thấy trong danh sách đối soát trả tiền COD. Xuất danh sách các vận đơn chênh lệch để làm biên bản khiếu nại."
* **Output & Điểm "Wow" khi Demo:** Giúp doanh nghiệp thu hồi lại ngay tiền cước bị tính lố và tiền COD bị sót mỗi tháng.

### Ví dụ 41: Đối chiếu Bộ chứng từ Xuất nhập khẩu (Invoice - Packing List - Bill of Lading - Tờ khai Hải quan) (Liên thông PDF/Excel)
* **Bài toán & Nỗi đau:** Nhân viên XNK (Logistics/Purchasing) trước khi truyền tờ khai hải quan phải dò từng mã HS Code, Tên hàng, Số lượng, Đơn giá, Tổng tiền, Trọng lượng Gross Weight / Net Weight giữa file Excel Invoice, Packing List và file PDF vận đơn (Bill of Lading). Chỉ lệch 1 con số là bị kẹt hàng ở cảng.
* **Đầu vào (Input):** File `Commercial_Invoice.xlsx`, `Packing_List.xlsx` và file `Bill_of_Lading_Draft.pdf`.
* **Prompt mẫu Antigravity:**
  > "Đọc và đối chiếu chéo 3 chứng từ: `Commercial_Invoice.xlsx`, `Packing_List.xlsx` và `Bill_of_Lading_Draft.pdf`. Kiểm tra xem Tên người mua/người bán, Số lượng kiện (Packages), Trọng lượng tịnh (Net Weight), Trọng lượng cả bì (Gross Weight), Số khối (CBM) và Mã hàng có khớp nhau 100% giữa 3 tài liệu không. Liệt kê bất kỳ điểm sai lệch (Discrepancy) nào tìm thấy."
* **Output & Điểm "Wow" khi Demo:** Đối chiếu chéo giữa Excel và PDF chuẩn xác đến từng con số thập phân, cứu dân XNK khỏi những lỗi sai chứng từ đắt giá.

### Ví dụ 42: Kiểm kê kho thực tế so với sổ sách và tự động lập Biên bản xử lý chênh lệch kiểm kê (Thuần Excel)
* **Bài toán & Nỗi đau:** Sau buổi kiểm kê cuối tháng, 4 nhóm kiểm kê nộp 4 phiếu đếm tay (hoặc 4 file Excel rời rạc, một mặt hàng nằm ở 3 kệ khác nhau nên xuất hiện ở 3 dòng). Phải cộng gộp số thực đếm rồi so với tồn trên phần mềm.
* **Đầu vào (Input):** 4 file phiếu kiểm kê theo khu vực kệ và file `ton_so_sach_erp.xlsx`.
* **Prompt mẫu Antigravity:**
  > "Gộp 4 file kết quả đếm kho thực tế tại các kệ, cộng tổng số lượng thực đếm theo từng Mã hàng, sau đó đối chiếu với file `ton_so_sach_erp.xlsx`. Tính số lượng và giá trị Thừa/Thiếu cho từng mặt hàng, phân loại nguyên nhân nghi ngờ (ví dụ: lệch chẵn thùng, hoặc lệch chéo giữa 2 mã hàng có tên/màu sắc gần giống nhau) và tạo sẵn sheet `Bien_Ban_Kiem_Ke` đúng mẫu ký duyệt."
* **Output & Điểm "Wow" khi Demo:** Điểm cực kỳ thông minh là AI phát hiện được **lỗi xuất nhầm chéo mã hàng** (ví dụ: Áo size M thừa 5 cái, Áo size L thiếu đúng 5 cái).

### Ví dụ 43: Tối ưu hóa đóng hàng vào thùng / Container (Load Planning cơ bản) (Thuần Excel)
* **Bài toán & Nỗi đau:** Có danh sách đơn hàng cần đóng vào container 20ft/40ft hoặc xe tải 2.5 tấn. Nhân viên điều vận phải tính tổng thể tích (CBM) và tổng trọng lượng (tấn) để biết cần đặt bao nhiêu xe và xếp đơn nào lên xe nào theo tuyến đường giao hàng.
* **Đầu vào (Input):** File `danh_sach_don_giao_ngay_mai.xlsx` (Mã đơn, Quận/Huyện giao, Số thùng, Thể tích CBM, Trọng lượng kg).
* **Prompt mẫu Antigravity:**
  > "Dựa vào `danh_sach_don_giao_ngay_mai.xlsx`, hãy gom các đơn hàng theo cụm Quận/Huyện gần nhau để chia vào các chuyến xe tải (mỗi xe tối đa 2.000 kg và tối đa 12 CBM). Tối ưu sao cho tổng số chuyến xe cần thuê là ít nhất và lập bảng danh sách giao hàng (Delivery Manifest) cho từng tài xế."
* **Output & Điểm "Wow" khi Demo:** Tự động gom tuyến và chia tải trọng xe hợp lý chỉ trong tích tắc.

---

## PHẦN 6: HÀNH CHÍNH - QUẢN LÝ DỰ ÁN - VĂN PHÒNG CHUNG (7 Ví dụ)

### Ví dụ 44: Chuyển biên bản cuộc họp (Word/Text/Audio Transcript) thành bảng Action Items trên Excel & đặt lịch nhắc việc (Liên thông Text/Word -> Excel + Calendar)
* **Bài toán & Nỗi đau:** Sau cuộc họp giao ban 2 tiếng, thư ký dự án có 1 biên bản họp dài 5 trang chữ. Phải ngồi lọc ra ai làm việc gì, deadline ngày nào để nhập vào file Excel theo dõi dự án (Action Tracker).
* **Đầu vào (Input):** File `bien_ban_hop_giao_ban.docx` (hoặc text ghi chú cuộc họp) và file Google Sheets / Excel `Project_Action_Tracker.xlsx`.
* **Prompt mẫu Antigravity:**
  > "Đọc file `bien_ban_hop_giao_ban.docx`. Trích xuất toàn bộ các đầu việc cần làm (Action Items) và cập nhật vào file `Project_Action_Tracker.xlsx` theo các cột: STT, Hạng mục công việc, Phòng ban, Người phụ trách (PIC), Ngày bắt đầu, Deadline, Mức độ ưu tiên, Trạng thái. Đồng thời tạo lịch nhắc Deadline trên Google Calendar cho các đầu việc có mức ưu tiên Cao."
* **Output & Điểm "Wow" khi Demo:** Từ văn bản cuộc họp dài dòng biến ngay thành bảng quản lý tiến độ công việc chuẩn chỉnh trên Excel kèm lịch nhắc tự động.

### Ví dụ 45: Xây dựng biểu đồ tiến độ dự án (Gantt Chart) và tính đường găng (Critical Path) trên Excel (Thuần Excel)
* **Bài toán & Nỗi đau:** Khách hàng hoặc Sếp yêu cầu lập bảng tiến độ dự án (Gantt Chart) trên Excel có tô màu các thanh thời gian theo tuần/ngày, tự động trừ ngày nghỉ lễ/cuối tuần khi tính ngày kết thúc của từng hạng mục phụ thuộc nhau.
* **Đầu vào (Input):** File `danh_sach_hang_muc_du_an.xlsx` (Tên công việc, Số ngày thực hiện, Công việc tiền đề phải xong trước).
* **Prompt mẫu Antigravity:**
  > "Từ danh sách hạng mục trong `danh_sach_hang_muc_du_an.xlsx`, hãy tính Ngày bắt đầu và Ngày kết thúc cho từng hạng mục (bỏ qua Thứ 7, Chủ nhật và ngày lễ), xác định các hạng mục nằm trên Đường găng (Critical Path), và tạo biểu đồ Gantt trực quan ngay trên lưới ô Excel bằng Conditional Formatting."
* **Output & Điểm "Wow" khi Demo:** Tạo ra một Gantt Chart động cực đẹp trên Excel mà người xem không cần tốn hàng giờ kẻ ô tô màu.

### Ví dụ 46: Quản lý chi phí văn phòng phẩm, điện nước, taxi công tác và phân bổ về từng bộ phận (Thuần Excel)
* **Bài toán & Nỗi đau:** Cuối tháng Hành chính (Admin) nhận bảng kê thẻ Taxi doanh nghiệp (Grab/XanhSM/Mai Linh), hóa đơn chuyển phát nhanh, văn phòng phẩm. Phải tra xem chuyến xe đó của nhân viên nào, thuộc phòng ban nào, có đi ngoài giờ làm việc hay cuối tuần không để phân bổ chi phí.
* **Đầu vào (Input):** File `bang_ke_grab_for_business.xlsx` và `danh_sach_nhan_su_phong_ban.xlsx`.
* **Prompt mẫu Antigravity:**
  > "Kết hợp bảng kê Grab `bang_ke_grab_for_business.xlsx` và danh sách nhân sự. Hãy ánh xạ từng chuyến xe về đúng Phòng ban của nhân viên, tổng hợp chi phí di chuyển theo từng phòng ban, và lọc riêng các chuyến xe phát sinh sau 22h đêm hoặc vào ngày Chủ nhật/Lễ không có mã dự án đi kèm để Admin xác minh lại."
* **Output & Điểm "Wow" khi Demo:** Tự động gán trung tâm chi phí (Cost Center) và lọc ngay các cuốc xe nghi vấn dùng cho mục đích cá nhân.

### Ví dụ 47: Tự động tổ chức và phân quyền hàng loạt thư mục/file dự án trên Google Drive từ danh sách Excel (Liên thông Excel + Google Drive)
* **Bài toán & Nỗi đau:** Khi khởi động dự án mới hoặc học kỳ mới với 30 khách hàng / lớp học, Admin phải tạo 30 bộ thư mục chuẩn trên Google Drive, copy các file biểu mẫu vào trong, rồi bấm Share quyền Editor/Viewer cho từng email trong danh sách Excel.
* **Đầu vào (Input):** File `danh_sach_du_an_va_email_thanh_vien.xlsx`.
* **Prompt mẫu Antigravity:**
  > "Đọc file `danh_sach_du_an_va_email_thanh_vien.xlsx`. Với mỗi dự án trong danh sách, hãy tạo một thư mục trên Google Drive gồm 3 thư mục con (`01_Hop_dong`, `02_Tai_lieu_ky_thuat`, `03_Nghiem_thu`), phân quyền Editor cho email Quản lý dự án và quyền Viewer cho email Khách hàng tương ứng, sau đó ghi lại đường link thư mục vào cột `Link Google Drive` trong file Excel."
* **Output & Điểm "Wow" khi Demo:** Tiết kiệm hàng trăm cú click chuột tạo folder và phân quyền thủ công trên Google Drive.

### Ví dụ 48: Chuyển bảng dữ liệu từ ảnh chụp màn hình / báo cáo PDF không copy được sang file Excel giữ nguyên cấu trúc (Liên thông Ảnh/PDF Scan -> Excel)
* **Bài toán & Nỗi đau:** Đối tác hoặc cơ quan nhà nước gửi văn bản, bảng biểu dưới dạng file PDF scan hoặc ảnh chụp bảng số liệu (có các ô gộp Merge Cells phức tạp). Gõ lại tay mất hàng giờ và dễ nhìn nhầm hàng.
* **Đầu vào (Input):** File `bao_cao_thong_ke_scan.pdf` hoặc ảnh chụp bảng số liệu.
* **Prompt mẫu Antigravity:**
  > "Đọc bảng số liệu ở trang 3 và trang 4 của file `bao_cao_thong_ke_scan.pdf`. Chuyển toàn bộ sang file Excel `bang_so_lieu_chuyen_doi.xlsx`, giữ đúng cấu trúc tiêu đề cột gộp (Merged Headers), chuyển các con số về đúng định dạng Number, và tự động dùng hàm `SUM` kiểm tra lại dòng Tổng cộng ở cuối bảng xem bản gốc có cộng sai số nào không."
* **Output & Điểm "Wow" khi Demo:** Không chỉ OCR chuyển ảnh thành bảng Excel mà còn **tự kiểm tra xem bảng gốc trên giấy có cộng sai không**.

### Ví dụ 49: Chuẩn bị danh sách khách mời sự kiện, xếp bàn tiệc (Seating Arrangement) và tạo mã Check-in (Thuần Excel)
* **Bài toán & Nỗi đau:** Tổ chức hội nghị 200 khách mời. Admin phải xếp khách vào 20 bàn tròn (10 người/bàn) sao cho: khách VIP ngồi bàn đầu, người cùng công ty hoặc cùng ngành nghề ngồi chung bàn, đối thủ cạnh tranh không ngồi chung một bàn, và xuất danh sách phục vụ lễ tân check-in.
* **Đầu vào (Input):** File `danh_sach_khach_moi_su_kien.xlsx` (Họ tên, Chức vụ, Công ty, Phân hạng VIP/Standard, Ngành nghề, Ghi chú ăn chay/mặn).
* **Prompt mẫu Antigravity:**
  > "Dựa vào `danh_sach_khach_moi_su_kien.xlsx`, hãy tạo Mã Check-in duy nhất cho từng khách, xếp 200 khách vào 20 bàn (Bàn 1-3 dành cho VIP, các bàn còn lại gom theo ngành nghề tương đồng và ưu tiên người cùng công ty ngồi cạnh nhau). Thống kê số suất ăn chay/mặn theo từng bàn để báo cho nhà hàng và xuất file `So_do_ban_va_Checkin.xlsx`."
* **Output & Điểm "Wow" khi Demo:** Giải quyết trọn gói bài toán hậu cần sự kiện rắc rối của dân Hành chính - Sự kiện.

### Ví dụ 50: Tự động tóm tắt file Excel nhiều sheet thành Báo cáo điều hành 1 trang (Executive Summary) gửi Sếp (Liên thông Excel -> Báo cáo/Slide/Email)
* **Bài toán & Nỗi đau:** Cuối tuần/cuối tháng, nhân viên tổng hợp được 1 file Excel nặng 10 sheets đầy số liệu chi tiết của các bộ phận, nhưng Sếp bận chỉ muốn đọc 1 trang tóm tắt những con số nổi bật nhất, nguyên nhân tăng/giảm và các vấn đề cần Sếp phê duyệt ngay trên điện thoại.
* **Đầu vào (Input):** File `Bao_cao_tong_hop_hoat_dong_T11.xlsx` (gồm các sheet Doanh thu, Chi phí, Nhân sự, Tồn kho, Dự án).
* **Prompt mẫu Antigravity:**
  > "Đọc toàn bộ các sheet trong file `Bao_cao_tong_hop_hoat_dong_T11.xlsx`. Hãy tạo thêm một sheet đầu tiên tên là `00_Executive_Summary` được thiết kế gọn gàng trong 1 trang nhìn (One-page Dashboard) gồm các KPI cốt lõi so với tháng trước và cùng kỳ. Đồng thời, viết một bản tóm tắt quản trị ngắn gọn (5 gạch đầu dòng: Điểm sáng, Điểm nghẽn, Cảnh báo rủi ro và Đề xuất hành động) để tôi gửi email/tin nhắn báo cáo Ban Giám đốc."
* **Output & Điểm "Wow" khi Demo:** Cái kết hoàn hảo cho buổi học: biến người làm Excel từ một "thợ nhập liệu/gõ hàm" thành một "chuyên gia phân tích tham mưu cho lãnh đạo".

---

## Gợi Ý Chọn 5 Bài "Đinh" (Signature Demos) Để Mở Đầu Khóa Học

Nếu bạn cần chọn ra **5 ví dụ mở màn** gây ấn tượng mạnh nhất trong 15 phút đầu buổi học hoặc dùng làm video quảng cáo khóa học:

| Thứ tự | Ví dụ nên chọn | Lý do gây hiệu ứng "Wow" mạnh nhất với học viên |
| :--- | :--- | :--- |
| **Demo 1** | **Ví dụ 7 hoặc 19:** Làm sạch bảng dữ liệu "rác" (sai ngày tháng, mất số 0 đầu SĐT, lệch tên viết tắt) | Ai đi làm văn phòng cũng từng khổ sở vì lỗi này; thấy kết quả sạch đẹp ngay trong 10 giây. |
| **Demo 2** | **Ví dụ 2 hoặc 28:** Gộp 10 file Excel khác tên cột từ 1 thư mục thành 1 báo cáo chuẩn | Chứng minh sức mạnh vượt trội của Antigravity khi làm việc trực tiếp với thư mục máy tính so với ChatGPT web. |
| **Demo 3** | **Ví dụ 10:** Đối soát sao kê ngân hàng với sổ nội bộ (Fuzzy Matching + Gộp đơn) | Chạm đúng "nỗi đau kinh hoàng" nhất của Kế toán và Sales Admin. |
| **Demo 4** | **Ví dụ 5 hoặc 11:** Quét cả thư mục PDF (CV ứng viên hoặc Hóa đơn đỏ) đổ tự động vào bảng Excel | Cho thấy AI xóa nhòa ranh giới giữa file PDF/Ảnh và file Excel. |
| **Demo 5** | **Ví dụ 4 hoặc 35:** Từ Excel/Google Sheets tự động tạo thư mục Google Drive và tạo nháp Gmail hàng loạt | Phô diễn sức mạnh kết nối hệ sinh thái Google Workspace của Antigravity. |
