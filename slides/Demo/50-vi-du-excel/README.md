# CẨM NANG 50 KHÔNG GIAN THỰC HÀNH EXCEL VỚI ANTIGRAVITY (PHIÊN BẢN 2.0 HOÀN THIỆN)

Chào mừng bạn đến với bộ tài nguyên **50 Không Gian Thực Hành (Workspaces) Xử Lý Excel & Google Sheets Bằng Antigravity**.  
Bộ tài nguyên này được thiết kế "Turn-key" (sẵn sàng sử dụng ngay) phục vụ giảng dạy online, đào tạo doanh nghiệp và quay video demo với các lớp bảo vệ an toàn và tiêu chuẩn thẩm mỹ cao cấp nhất.

---

## 🛡️ HỆ THỐNG KIỂM SOÁT AN TOÀN & CHUẨN MỰC THẨM MỸ (PHIÊN BẢN 2.0)

Mỗi thư mục bài tập trong bộ 50 không gian thực hành này là một **Workspace độc lập hoàn chỉnh**, được trang bị sẵn 4 chốt chặn kiểm soát:

1. **PreToolUse Security Hook (`.agents/hooks.json` & `.agents/scripts/protect_raw_data.py`):**
   - Chặn đứng cứng (`decision: "deny"`) mọi hành vi cố tình ghi đè, sửa đổi hoặc xóa các file dữ liệu thô gốc (`_raw.xlsx`, `.csv`, `.txt`).
   - Đảm bảo học viên và giảng viên có thể chạy demo hàng trăm lần mà không bao giờ bị hỏng file dữ liệu ban đầu.

2. **Quy chuẩn Thẩm mỹ Bảng tính Văn phòng (`.agents/rules/chuan_muc_excel_van_phong.md`):**
   - Áp dụng bảng màu Nhận diện Doanh nghiệp Corporate Navy `#1F497D` (chữ trắng đậm, xen kẽ dòng zebra `#F2F5F9`).
   - Tự động căn chỉnh độ rộng cột (`Auto-fit column width`), không bao giờ để xảy ra lỗi tràn số `###`.
   - Định dạng số có dấu phân cách hàng nghìn (`#,##0`) và tiền tệ chuẩn mực.
   - Bắt buộc dùng công thức sống (`=SUM()`, `=AVERAGE()`) cho dòng tổng cộng, không ghi đè số cứng (hardcoded value).

3. **Tệp Kết quả Mẫu Đối chiếu Chuẩn (`_ket_qua_mau_chuan.xlsx`):**
   - Sinh sẵn trong từng thư mục bài tập để học viên và giảng viên có thể mở ra so sánh đối chiếu ngay sau khi AI hoàn thành nhiệm vụ.

4. **Cấu hình Liên thông MCP (`mcp_config.json`):**
   - Tích hợp cấu hình mẫu cho các bài toán liên thông thực tế (Gmail MCP cho bài 4, 6, 12, 27; Google Workspace MCP cho bài 14, 24, 35, 44, 47).

---

## 🚀 HƯỚNG DẪN 3 BƯỚC THỰC HÀNH NHANH CHO GIẢNG VIÊN

1. **Bước 1:** Mở một thư mục bài tập bất kỳ (ví dụ: `01-nhan-su/01-chuan-hoa-cham-cong/`) làm Workspace làm việc trong Antigravity hoặc mở terminal tại thư mục đó.
2. **Bước 2:** Mở file `PROMPT_DEMO.md` trong thư mục đó, sử dụng câu hỏi tại **Mục 2** để tương tác với học viên trước khi chạy, sau đó sao chép câu lệnh Prompt tại **Mục 3**.
3. **Bước 3:** Dán Prompt vào Antigravity. AI sẽ tự động đọc `AGENTS.md` (Hiến pháp), kích hoạt Rule trong `.agents/rules/` và chạy Skill trong `.agents/skills/` để xử lý file dữ liệu mẫu thành file Excel kết quả hoàn hảo ngay trước mắt học viên. Cuối cùng, mở file `_ket_qua_mau_chuan.xlsx` để học viên thấy sự chuẩn xác tuyệt đối!

---

## 🌟 TOP 5 BÀI DEMO "ĐINH" (SIGNATURE DEMOS) GÂY HIỆU ỨNG WOW MẠNH NHẤT

Khi mở đầu buổi học hoặc quay video ngắn (TikTok/Reels), hãy chọn 1 trong 5 bài sau:

| Thứ tự | Thư mục bài tập | Điểm "Wow" với học viên |
| :---: | :--- | :--- |
| **Demo 1** | [07-lam-sach-du-lieu-kham-suc-khoe](01-nhan-su/07-lam-sach-du-lieu-kham-suc-khoe/PROMPT_DEMO.md) | Xử lý triệt để các lỗi kinh điển: mất số 0 đầu SĐT/CCCD, loạn ngày tháng, thừa khoảng trắng trong 10 giây. |
| **Demo 2** | [02-gop-danh-gia-kpi](01-nhan-su/02-gop-danh-gia-kpi/PROMPT_DEMO.md) | Gộp 3 file Excel khác tên cột (Mã NV vs ID, Tổng điểm vs Điểm KPI) bằng nhận diện ngữ nghĩa AI. |
| **Demo 3** | [10-doi-soat-sao-ke-so-quy](02-ke-toan/10-doi-soat-sao-ke-so-quy/PROMPT_DEMO.md) | Khớp sao kê ngân hàng với sổ quỹ bằng Fuzzy Matching và phát hiện 1 lệnh chuyển khoản trả gộp 2 hóa đơn. |
| **Demo 4** | [42-kiem-ke-kho-lech-thuc-te](05-kho-van/42-kiem-ke-kho-lech-thuc-te/PROMPT_DEMO.md) | Phát hiện lỗi xuất nhầm chéo mã hàng (Áo size M thừa 5 cái, Áo size L thiếu đúng 5 cái). |
| **Demo 5** | [50-executive-summary-one-page](06-hanh-chinh/50-executive-summary-one-page/PROMPT_DEMO.md) | Tự động tóm tắt file Excel 10 sheets thành Dashboard 1 trang điều hành sang trọng kèm 4 gạch đầu dòng chiến lược. |

---

## 📋 MỤC LỤC CHI TIẾT 50 BÀI TẬP THEO 6 PHÒNG BAN

### 1. NHÂN SỰ - TUYỂN DỤNG - C&B (`01-nhan-su/` - 9 Bài)
- [Bài 01: Chuẩn hóa chấm công từ máy vân tay / FaceID](01-nhan-su/01-chuan-hoa-cham-cong/PROMPT_DEMO.md)
- [Bài 02: Gộp 12 bảng đánh giá KPI tháng đa phòng ban](01-nhan-su/02-gop-danh-gia-kpi/PROMPT_DEMO.md)
- [Bài 03: Tính lương Gross - Net, BHXH và Thuế TNCN lũy tiến](01-nhan-su/03-tinh-luong-gross-net-thue/PROMPT_DEMO.md)
- [Bài 04: Tách phiếu lương cá nhân và tạo bản nháp Gmail (Có MCP Gmail)](01-nhan-su/04-tach-phieu-luong-gui-email/PROMPT_DEMO.md)
- [Bài 05: Trích xuất hàng loạt CV ứng viên vào bảng theo dõi](01-nhan-su/05-trich-xuat-cv-ung-vien/PROMPT_DEMO.md)
- [Bài 06: Cảnh báo hợp đồng lao động sắp hết hạn (Có MCP Gmail)](01-nhan-su/06-canh-bao-het-han-hop-dong/PROMPT_DEMO.md)
- [Bài 07: Làm sạch dữ liệu đăng ký khám sức khỏe / bảo hiểm](01-nhan-su/07-lam-sach-du-lieu-kham-suc-khoe/PROMPT_DEMO.md)
- [Bài 08: Phân tích biến động nhân sự (Turnover Dashboard)](01-nhan-su/08-phan-tich-turnover-dashboard/PROMPT_DEMO.md)
- [Bài 09: Xếp lịch trực ca tự động theo ràng buộc nghỉ phép](01-nhan-su/09-xep-lich-truc-ca-tu-dong/PROMPT_DEMO.md)

### 2. KẾ TOÁN - TÀI CHÍNH (`02-ke-toan/` - 9 Bài)
- [Bài 10: Đối soát sao kê ngân hàng với sổ quỹ nội bộ](02-ke-toan/10-doi-soat-sao-ke-so-quy/PROMPT_DEMO.md)
- [Bài 11: Trích xuất hàng loạt hóa đơn điện tử vào bảng kê](02-ke-toan/11-trich-xuat-hoa-don-dien-tu/PROMPT_DEMO.md)
- [Bài 12: Phân loại tuổi nợ (AR Aging) và soạn email nhắc nợ (Có MCP Gmail)](02-ke-toan/12-phan-loai-tuoi-no-nhac-no/PROMPT_DEMO.md)
- [Bài 13: Phân bổ chi phí trả trước (242) và khấu hao TSCĐ](02-ke-toan/13-phan-bo-chi-phi-khau-hao/PROMPT_DEMO.md)
- [Bài 14: Hợp nhất báo cáo kết quả kinh doanh (P&L) đa chi nhánh (Có MCP Google Workspace)](02-ke-toan/14-hop-nhat-bao-cao-kinh-doanh/PROMPT_DEMO.md)
- [Bài 15: Phát hiện giao dịch bất thường và gian lận chi phí](02-ke-toan/15-phat-hien-gian-lan-chi-phi/PROMPT_DEMO.md)
- [Bài 16: Chuyển đổi số tiền bằng số sang chữ song ngữ Anh - Việt](02-ke-toan/16-chuyen-so-thanh-chu/PROMPT_DEMO.md)
- [Bài 17: Dự báo dòng tiền 12 tuần tới (Cashflow Forecast)](02-ke-toan/17-du-bao-dong-tien-12-tuan/PROMPT_DEMO.md)
- [Bài 18: Tự động hạch toán định khoản Nợ/Có theo Thông tư 200](02-ke-toan/18-dinh-khoan-no-co-tu-dong/PROMPT_DEMO.md)

### 3. KINH DOANH - CSKH (`03-kinh-doanh/` - 9 Bài)
- [Bài 19: Làm sạch, chuẩn hóa và lọc trùng dữ liệu CRM](03-kinh-doanh/19-lam-sach-chuan-hoa-crm/PROMPT_DEMO.md)
- [Bài 20: Tính hoa hồng sales lũy tiến nhiều tầng bậc](03-kinh-doanh/20-tinh-hoa-hong-luy-tien/PROMPT_DEMO.md)
- [Bài 21: Phân nhóm khách hàng VIP / Ngủ đông theo mô hình RFM](03-kinh-doanh/21-phan-nhom-khach-hang-rfm/PROMPT_DEMO.md)
- [Bài 22: Tự động tạo hàng loạt báo giá từ bảng yêu cầu](03-kinh-doanh/22-tao-hang-loat-bao-gia/PROMPT_DEMO.md)
- [Bài 23: Phân tích lý do mất khách (Lost Deals) từ text ghi chú](03-kinh-doanh/23-phan-tich-ly-do-mat-khach/PROMPT_DEMO.md)
- [Bài 24: Chia giỏ data khách hàng (Lead Routing) tự động (Có MCP Google Workspace)](03-kinh-doanh/24-chia-gio-lead-routing/PROMPT_DEMO.md)
- [Bài 25: Theo dõi tiến độ mục tiêu doanh số (Pacing & Run-rate)](03-kinh-doanh/25-theo-doi-pacing-runrate-sales/PROMPT_DEMO.md)
- [Bài 26: Tổng hợp khảo sát mức độ hài lòng khách hàng (NPS / CSAT)](03-kinh-doanh/26-tong-hop-khao-sat-nps-csat/PROMPT_DEMO.md)
- [Bài 27: Bóc tách danh thiếp (Namecard) và soạn thư kết nối (Có MCP Gmail)](03-kinh-doanh/27-quet-namecard-soan-mail/PROMPT_DEMO.md)

### 4. MARKETING - E-COMMERCE (`04-marketing/` - 8 Bài)
- [Bài 28: Gộp và chuẩn hóa báo cáo quảng cáo Facebook, Google, TikTok](04-marketing/28-gop-bao-cao-ads-da-kenh/PROMPT_DEMO.md)
- [Bài 29: Đối soát doanh thu và phí sàn TMĐT Shopee/TikTok Shop](04-marketing/29-doi-soat-doanh-thu-phi-san/PROMPT_DEMO.md)
- [Bài 30: Tự động tạo link UTM Tracking và mã QR hàng loạt](04-marketing/30-tao-link-utm-tracking-qr/PROMPT_DEMO.md)
- [Bài 31: Phân tích đánh giá 1-3 sao trên sàn TMĐT](04-marketing/31-phan-tich-danh-gia-san-tmdt/PROMPT_DEMO.md)
- [Bài 32: Lập kế hoạch phân bổ ngân sách Media Plan tối ưu](04-marketing/32-phan-bo-ngan-sach-media-plan/PROMPT_DEMO.md)
- [Bài 33: Gom cụm từ khóa SEO (Topic Cluster) và Search Intent](04-marketing/33-gom-cum-tu-khoa-seo/PROMPT_DEMO.md)
- [Bài 34: Kiểm tra tồn kho POSM và chia hàng làm tròn theo thùng](04-marketing/34-chia-qua-tang-posm-dai-ly/PROMPT_DEMO.md)
- [Bài 35: Tạo lịch Content Calendar và cấu trúc thư mục Google Drive (Có MCP Google Workspace)](04-marketing/35-tao-lich-content-folder-drive/PROMPT_DEMO.md)

### 5. KHO VẬN - CHUỖI CUNG ỨNG (`05-kho-van/` - 8 Bài)
- [Bài 36: So sánh báo giá từ nhiều nhà cung cấp (Bid Comparison)](05-kho-van/36-so-sanh-bao-gia-ncc/PROMPT_DEMO.md)
- [Bài 37: Cảnh báo hàng tồn kho sắp hết và tính Reorder Point](05-kho-van/37-canh-bao-reorder-point/PROMPT_DEMO.md)
- [Bài 38: Phân tích tồn kho ABC - XYZ và cảnh báo hàng cận date/chết](05-kho-van/38-phan-tich-ton-kho-abc-xyz/PROMPT_DEMO.md)
- [Bài 39: Tính toán nhu cầu nguyên vật liệu (BOM Explosion)](05-kho-van/39-tinh-nhu-cau-nguyen-lieu-bom/PROMPT_DEMO.md)
- [Bài 40: Đối soát bảng kê cước phí vận chuyển và tiền COD](05-kho-van/40-doi-soat-cuoc-phi-cod/PROMPT_DEMO.md)
- [Bài 41: Đối chiếu bộ chứng từ xuất nhập khẩu (Invoice, Packing List, B/L)](05-kho-van/41-doi-chieu-chung-tu-xnk/PROMPT_DEMO.md)
- [Bài 42: Kiểm kê kho thực tế và phát hiện xuất nhầm chéo mã](05-kho-van/42-kiem-ke-kho-lech-thuc-te/PROMPT_DEMO.md)
- [Bài 43: Tối ưu tải trọng xe tải và container theo khối/cân nặng](05-kho-van/43-chia-tai-trong-xe-container/PROMPT_DEMO.md)

### 6. HÀNH CHÍNH - DỰ ÁN (`06-hanh-chinh/` - 7 Bài)
- [Bài 44: Chuyển biên bản họp thành bảng Action Items (Có MCP Google Workspace)](06-hanh-chinh/44-bien-ban-hop-action-tracker/PROMPT_DEMO.md)
- [Bài 45: Xây dựng biểu đồ tiến độ dự án Gantt Chart trên Excel](06-hanh-chinh/45-ve-gantt-chart-excel/PROMPT_DEMO.md)
- [Bài 46: Quản lý và phân bổ chi phí taxi Grab, văn phòng phẩm](06-hanh-chinh/46-phan-bo-chi-phi-taxi-vpp/PROMPT_DEMO.md)
- [Bài 47: Tạo thư mục và phân quyền Google Drive hàng loạt (Có MCP Google Workspace)](06-hanh-chinh/47-tao-folder-phan-quyen-drive/PROMPT_DEMO.md)
- [Bài 48: Chuyển bảng biểu scan sang Excel và kiểm tra số học](06-hanh-chinh/48-ocr-bang-bieu-anh-pdf/PROMPT_DEMO.md)
- [Bài 49: Xếp sơ đồ bàn tiệc sự kiện và tạo mã check-in duy nhất](06-hanh-chinh/49-xep-so-do-ban-tiec-checkin/PROMPT_DEMO.md)
- [Bài 50: Tự động tóm tắt Executive Summary Dashboard 1 trang](06-hanh-chinh/50-executive-summary-one-page/PROMPT_DEMO.md)

---
*Tài liệu này được đồng bộ và cập nhật tự động bởi hệ thống Antigravity Demo Builder.*
