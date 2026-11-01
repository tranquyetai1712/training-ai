# BÁO CÁO KIỂM TOÁN & CẢNH BÁO RỦI RO CHI PHÍ CÔNG TÁC QUÝ 3/2026
*(Bản mẫu kết quả sau khi duyệt nút **Proceed** từ lệnh `/plan`)*

- **Tệp dữ liệu kiểm toán:** `chi_phi_quy_3_2026.xlsx` (3 Sheet: `Thang_7`, `Thang_8`, `Thang_9`)
- **Căn cứ đối chiếu:** `dinh_muc_chi_tieu_noi_bo.md`
- **Tổng số giao dịch rà soát:** 14 khoản chi (Tổng giá trị kê khai: **90.200.000 VNĐ**)
- **Tổng giá trị giao dịch có rủi ro / sai phạm:** **60.850.000 VNĐ** (chiếm **67,46%** tổng chi phí)

---

## 🚨 1. CẢNH BÁO ĐỎ: NGHI VẤN THANH TOÁN TRÙNG LẶP (CẦN THU HỒI NGAY)

Phát hiện **01 cặp giao dịch trùng lặp 100%** về nhân sự, ngày chi, nội dung và số tiền trong `Thang_8`:

| Mã GD | Ngày chi | Nhân viên | Phòng ban | Nội dung | Số tiền (VNĐ) | Đề xuất xử lý |
| :---: | :---: | :--- | :--- | :--- | ---: | :--- |
| `GD-0803` | 14/08/2026 | Vũ Phương Thảo | Marketing | Thuê gian hàng Hội chợ Triển lãm Thương mại Q3 | 18.500.000 | Giữ lại (nhưng cần giải trình vượt trần) |
| `GD-0804` | 14/08/2026 | Vũ Phương Thảo | Marketing | Thuê gian hàng Hội chợ Triển lãm Thương mại Q3 (Bản sao) | **18.500.000** | **Xuất toán / Thu hồi ngay 18.500.000 VNĐ** |

---

## ⚠️ 2. NHÓM VI PHẠM VƯỢT ĐỊNH MỨC CHI TIÊU NỘI BỘ (06 KHOẢN CHI)

| Mã GD | Tháng | Nhân viên | Hạng mục | Thực chi (VNĐ) | Định mức tối đa (VNĐ) | Mức vượt trần (VNĐ) | Ghi chú sai phạm |
| :---: | :---: | :--- | :--- | ---: | ---: | ---: | :--- |
| `GD-0703` | Tháng 7 | Trần Thị Mai | Tiếp khách | 7.800.000 | 5.000.000 | **+2.800.000** | Vượt 56%, chưa có chữ ký phê duyệt của GĐ Khối |
| `GD-0801` | Tháng 8 | Đỗ Tuấn Anh | Vé máy bay | 6.200.000 | 4.500.000 | **+1.700.000** | Tự ý đặt hạng Thương gia sát giờ bay |
| `GD-0802` | Tháng 8 | Đỗ Tuấn Anh | Khách sạn | 2.400.000 | 1.500.000 | **+900.000** | Thuê Resort vượt trần 900.000 VNĐ/đêm |
| `GD-0803` | Tháng 8 | Vũ Phương Thảo | Sự kiện | 18.500.000 | 15.000.000 | **+3.500.000** | Thuê gian hàng góc vượt định mức sự kiện |
| `GD-0901` | Tháng 9 | Nguyễn Văn An | Tiếp khách | 6.500.000 | 5.000.000 | **+1.500.000** | Vượt định mức tiếp khách + Không có hóa đơn VAT |
| `GD-0902` | Tháng 9 | Trần Thị Mai | Di chuyển nội đô | 1.450.000 | 1.000.000 | **+450.000** | Vượt trần di chuyển nội đô 450.000 VNĐ/đợt |
| — | — | **TỔNG VƯỢT TRẦN** | — | **42.850.000** | **32.000.000** | **+10.850.000** | — |

---

## 🧾 3. NHÓM RỦI RO THUẾ: THIẾU HÓA ĐƠN VAT HỢP LỆ (03 KHOẢN CHI)

Theo Mục 2 (`dinh_muc_chi_tieu_noi_bo.md`), mọi khoản chi ≥ 200.000 VNĐ bắt buộc phải có Hóa đơn VAT. Phát hiện **03 khoản chi (Tổng: 9.850.000 VNĐ)** không đủ điều kiện khấu trừ thuế:

1. **`GD-0704` (18/07/2026) — Lê Hoàng Nam (Phòng Kỹ Thuật):** 950.000 VNĐ (Thuê taxi khảo sát trạm tỉnh) ➔ *Trạng thái: Biên lai viết tay*.
2. **`GD-0802` (05/08/2026) — Đỗ Tuấn Anh (Phòng Kinh Doanh):** 2.400.000 VNĐ (Resort 1 đêm tại Đà Nẵng) ➔ *Trạng thái: Chưa có hóa đơn*.
3. **`GD-0901` (08/09/2026) — Nguyễn Văn An (Phòng Kinh Doanh):** 6.500.000 VNĐ (Ăn tối ký hợp đồng đại lý) ➔ *Trạng thái: Chưa có hóa đơn*.

---

## ✅ 4. KIẾN NGHỊ TRÌNH BAN GIÁM ĐỐC PHÊ DUYỆT
1. **Thu hồi ngay 18.500.000 VNĐ** từ bút toán nhập đúp `GD-0804` của Phòng Marketing.
2. **Yêu cầu bổ sung Hóa đơn VAT trước ngày 05/10/2026** đối với 2 khoản chi `GD-0802` (2.400.000 VNĐ) và `GD-0901` (6.500.000 VNĐ); nếu không bổ sung kịp, chuyển sang trừ vào thu nhập cá nhân của nhân sự tạm ứng.
3. **Yêu cầu giải trình bổ sung chữ ký Giám đốc Khối** cho các khoản vượt định mức của Trần Thị Mai (`GD-0703`, `GD-0902`) và Đỗ Tuấn Anh (`GD-0801`).
