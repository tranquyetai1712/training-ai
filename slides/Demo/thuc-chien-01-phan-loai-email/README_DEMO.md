# 📬 DEMO MẪU: 10 EMAIL PHÂN LOẠI GMAIL & BÁO CÁO SLACK (PLUGIN `q-email`)

Bộ **10 email mẫu** này được thiết kế khớp **100%** với bộ quy tắc của Plugin `q-email` (`.agents/plugins/q-email/`):
- **Skill:** `phan-loai-gan-nhan-email`
- **Quy tắc nhãn:** `quy-tac-gan-nhan.md` (8 nhãn nghiệp vụ phòng ban + nhãn chống trùng lặp `AI_DaPhanLoai`)
- **Quy chuẩn Slack:** `quy-chuan-slack-notification.md` (điều hướng đúng kênh phòng ban & chặn spam không bắn lên Slack)

---

## 🎯 1. Bảng Đáp Án Chuẩn Của 10 Email Mẫu

| File mẫu | Người gửi | Tiêu đề | Nhãn Gmail gắn thêm | Kênh Slack nhận tin | Ghi chú demo |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `email_01_khancap_su_co_giao_nham_hang.md` | Lê Hoàng Minh - Công ty ABC | Phản ánh giao nhầm lô hàng sáng nay — cần xử lý ngay | `KhanCap` + `AI_DaPhanLoai` | `#urgent` | Khiếu nại sự cố gấp |
| `email_02_khancap_khach_vip_khieu_nai.md` | Trần Lan Anh - Đối tác VIP | Chậm bàn giao hệ thống ảnh hưởng vận hành bên chị | `KhanCap` + `AI_DaPhanLoai` | `#urgent` | **Không có chữ "khẩn cấp"** nhưng là khiếu nại gay gắt |
| `email_03_kinhdoanh_bao_gia_may_in.md` | Phòng Mua hàng - Công ty Minh Tâm | Yêu cầu gửi báo giá 05 máy in văn phòng và gói bảo trì | `KinhDoanh/BaoGia` + `AI_DaPhanLoai` | `#sales` | Hỏi giá sản phẩm/dịch vụ |
| `email_04_kinhdoanh_hop_tac_b2b.md` | Ban Đối ngoại - Tập đoàn Sao Mai | Đề xuất hợp tác phân phối B2B và đồng tài trợ sự kiện Q4 | `KinhDoanh/HopTac` + `AI_DaPhanLoai` | `#sales` | Đề xuất hợp tác B2B |
| `email_05_ketoan_hoa_don_viettel.md` | Viettel Telecom | Thông báo phát hành Hóa đơn điện tử (VAT) tháng 10/2026 | `KeToan/HoaDon` + `AI_DaPhanLoai` | `#finance` | Hóa đơn điện tử VAT |
| `email_06_congno_nhac_thanh_toan_thue_vp.md` | Ban Quản lý Tòa nhà Central | Nhắc thanh toán phí thuê văn phòng & dịch vụ tháng 10 | `CongNo/ThanhToan` + `AI_DaPhanLoai` | `#finance` | Nhắc nợ / hạn thanh toán |
| `email_07_nhansu_ung_vien_nop_cv.md` | Nguyễn Thu Hà | Ứng tuyển vị trí Chuyên viên Hành chính Nhân sự — CV đính kèm | `NhanSu/Tuyendung` + `AI_DaPhanLoai` | `#hr` | Hồ sơ ứng tuyển, CV |
| `email_08_hanhchinh_gia_han_dich_vu.md` | Bộ phận Vận hành Hệ thống | Thông báo gia hạn gói tên miền & lưu trữ dữ liệu nội bộ | `HanhChinh/ThongBao` + `AI_DaPhanLoai` | `#email-notifications` | Thông báo gia hạn hệ thống |
| `email_09_quangcao_bay_tu_khoa.md` | Học viện Kỹ năng Số | KHẨN CẤP: Cơ hội cuối cùng nhận học bổng 50% duy nhất hôm nay! | `QuangCao_Spam` + `AI_DaPhanLoai` | *(Không gửi Slack)* | **Bẫy từ khóa "KHẨN CẤP"** — AI nhận diện là quảng cáo, không bắn Slack |
| `email_10_quangcao_ban_tin_khuyen_mai.md` | Siêu thị Văn phòng Phẩm | Siêu sale cuối tháng — Giảm đến 40% giấy in và đồ dùng văn phòng | `QuangCao_Spam` + `AI_DaPhanLoai` | *(Không gửi Slack)* | Quảng cáo hàng loạt, chỉ cất gọn trên Gmail |

---

## 🚀 2. Cách Chuẩn Bị & Chạy Demo Cho Bài 9.1

### Bước 1: Đưa 10 email mẫu vào hộp thư Gmail Demo (chỉ làm 1 lần trước khi quay)
Mở Antigravity trong thư mục `Demo` (đã bật plugin **Gmail**), gõ yêu cầu:
> *"Hãy đọc 10 file mẫu trong thư mục `thuc-chien-01-phan-loai-email/10_email_mau`, sau đó gửi lần lượt cả 10 email đó tới địa chỉ `<ĐIỀN_EMAIL_DEMO_CỦA_BẠN>` (giữ nguyên tiêu đề và nội dung, ghi rõ dòng Người gửi mẫu ở đầu thư) để tôi làm dữ liệu test."*

*(Nếu tự gửi cho chính mình, nhớ đánh dấu Chưa đọc và đảm bảo chúng chưa có nhãn `AI_DaPhanLoai`.)*

### Bước 2: Câu lệnh quay trực tiếp trong Bài 9.1 (ngắn gọn, tự nhiên)
Vì trong thư mục `Demo` đã cài sẵn plugin **`q-email`** (gồm kỹ năng `phan-loai-gan-nhan-email` và 2 file quy tắc), bạn chỉ cần gõ một câu tiếng Việt rất ngắn:
> *"Hãy kiểm tra tối đa 20 email mới chưa được phân loại trong hộp thư Gmail của tôi, tự động đọc hiểu để gắn nhãn theo từng phòng ban và gửi tóm tắt 2 câu sang đúng kênh Slack tương ứng giúp tôi nhé."*

### Bước 3: Kiểm chứng kết quả khi quay
1. **Trên màn hình Antigravity:** Xem bảng tổng hợp 10 email kèm nhãn Gmail và trạng thái từng kênh Slack.
2. **Trên tab Gmail (bấm `F5`):** Thấy đủ 8 nhãn nghiệp vụ + nhãn kiểm soát `AI_DaPhanLoai`.
3. **Trên Slack:** Thấy các kênh `#urgent`, `#sales`, `#finance`, `#hr`, `#email-notifications` nhận đúng tin tóm tắt 2 câu kèm link mở thẳng email; riêng 2 thư quảng cáo (kể cả thư giật tít *"KHẨN CẤP"*) hoàn toàn không làm phiền Slack!
