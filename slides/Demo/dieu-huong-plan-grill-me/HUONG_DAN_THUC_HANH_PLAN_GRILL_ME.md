# HƯỚNG DẪN THỰC HÀNH BÀI 2.3: BỘ ĐÔI LỆNH `/plan` VÀ `/grill-me`

Thư mục thực hành: `slides/Demo/dieu-huong-plan-grill-me/`

---

## 📂 1. Danh sách các file có sẵn trong thư mục thực hành

| Tên file | Vai trò trong bài thực hành | Dùng cho lệnh nào? |
| :--- | :--- | :---: |
| `chi_phi_quy_3_2026.xlsx` | Bảng kê 14 khoản chi công tác Quý 3 (gồm 3 sheet: `Thang_7`, `Thang_8`, `Thang_9`) có cài sẵn các khoản vượt định mức, thiếu hóa đơn VAT và nhập trùng. | `/plan` |
| `dinh_muc_chi_tieu_noi_bo.md` | Văn bản quy định trần chi tiêu công tác và quy tắc hóa đơn VAT của công ty. | `/plan` |
| `bao_cao_rui_ro_chi_phi_quy_3_MAU.md` | File kết quả mẫu được sinh ra sau khi bạn bấm nút **Proceed** trên bản kế hoạch của lệnh `/plan`. | `/plan` |
| `de_xuat_tu_dong_hoa_email_cskh.md` | Bản đề xuất gửi 5.000 email CSKH (cố tình chứa 5 lỗ hổng vận hành nghiêm trọng để AI phản biện). | `/grill-me` |

---

## 🛠️ 2. BÀI THỰC HÀNH SỐ 1: LỆNH `/plan` (LẬP KẾ HOẠCH TÁC CHIẾN & DUYỆT NÚT `PROCEED`)

### Bước 1: Mở thư mục thực hành
Mở ứng dụng **Antigravity Desktop** tại thư mục `slides/Demo/dieu-huong-plan-grill-me/`.

### Bước 2: Gõ lệnh `/plan` vào khung Chat
Copy và dán nguyên văn câu lệnh dưới đây vào khung chat:

```text
/plan Hãy đối chiếu dữ liệu 3 tháng trong file chi_phi_quy_3_2026.xlsx với quy định tại file dinh_muc_chi_tieu_noi_bo.md để lập báo cáo kiểm toán rủi ro chi phí Quý 3 nộp Ban Giám đốc, xuất ra file bao_cao_rui_ro_chi_phi_quy_3.md
```

### Bước 3: Quan sát Plan Artifact & Nhấn nút `Proceed`
1. **Ngay lập tức**, AI sẽ **không** tạo file báo cáo vội, mà mở ra một bảng **Implementation Plan (Plan Artifact)** ở khung bên phải kèm nút bấm màu xanh **Proceed**.
2. Bản kế hoạch sẽ trình bày rõ 4 giai đoạn:
   - **Giai đoạn 1:** Đọc quy định hạn mức từ `dinh_muc_chi_tieu_noi_bo.md`.
   - **Giai đoạn 2:** Quét toàn bộ 3 sheet (`Thang_7`, `Thang_8`, `Thang_9`) trong `chi_phi_quy_3_2026.xlsx`.
   - **Giai đoạn 3:** Phân loại 3 nhóm vi phạm: (1) Vượt định mức chi tiêu, (2) Thiếu hóa đơn VAT hợp lệ, (3) Nghi vấn thanh toán trùng lặp.
   - **Giai đoạn 4:** Tổng hợp số liệu thiệt hại tài chính và xuất file `bao_cao_rui_ro_chi_phi_quy_3.md` (cam kết giữ nguyên file gốc).
3. Bạn kiểm tra kế hoạch, có thể bình luận chỉnh sửa nếu muốn, sau đó bấm nút **Proceed** để AI chính thức bắt tay vào chạy và xuất ra file báo cáo!

---

## 🔥 3. BÀI THỰC HÀNH SỐ 2: LỆNH `/grill-me` (CHUYÊN GIA PHẢN BIỆN BÓC TRẦN LỖ HỔNG)

### Bước 1: Xem qua bản đề xuất sơ sài
Mở file `de_xuat_tu_dong_hoa_email_cskh.md` để xem kế hoạch dự kiến bắn 5.000 email mã giảm giá `VIP20` vào sáng Thứ Hai.

### Bước 2: Gõ lệnh `/grill-me` vào khung Chat
Copy và dán câu lệnh dưới đây vào khung chat:

```text
/grill-me Hãy đọc file de_xuat_tu_dong_hoa_email_cskh.md và đóng vai Giám đốc Vận hành khó tính để phản biện, chất vấn tôi từng điểm rủi ro một trước khi tôi cho chạy chiến dịch này vào sáng Thứ Hai.
```

### Bước 3: Trải nghiệm màn "Phỏng vấn phản biện" và hoàn thiện kế hoạch
AI sẽ không khen ngợi xã giao mà lập tức đặt các câu hỏi sắc bén (bạn có thể trả lời trực tiếp từng câu):
1. **Về rủi ro khóa tài khoản & Spam:** *"Bạn định dùng 1 tài khoản Gmail thông thường để bắn 5.000 email trong 1 buổi sáng — bạn có biết giới hạn của Google Workspace chỉ cho phép tối đa 2.000 mail/ngày và gửi dồn dập sẽ khiến tên miền công ty bị liệt vào danh sách đen (Blacklist) ngay lập tức không? Phương án chia nhỏ lô gửi (batching) của bạn là gì?"*
2. **Về dữ liệu bẩn trong Excel:** *"Nếu trong 5.000 dòng của `danh_sach_khach_hang_2024_2026.xlsx` có những dòng bị trống cột `Ten_Khach_Hang`, email gửi đi sẽ hiển thị là 'Chào anh/chị ,'. Bạn xử lý giá trị mặc định (fallback) thế nào?"*
3. **Về rủi ro tài chính từ mã `VIP20`:** *"Mã `VIP20` giảm 20% dùng chung cho mọi người và không giới hạn số lần nhập — nếu khách hàng tung mã này lên hội nhóm săn sale hoặc áp dụng cho mặt hàng biên lợi nhuận thấp dưới 15%, công ty sẽ lỗ nặng. Bạn đặt trần giảm tối đa bao nhiêu tiền?"*

👉 **Cách trả lời mẫu của bạn để chốt phương án với AI:**
```text
Cảm ơn bạn đã chỉ ra! Hãy giúp tôi cập nhật lại file de_xuat_tu_dong_hoa_email_cskh.md với 3 chốt chặn:
1. Chia làm 10 đợt gửi (mỗi ngày 500 email), có chạy thử 5 email nội bộ trước.
2. Nếu trống tên khách hàng thì tự động đổi thành "Quý khách hàng thân mến", và lọc bỏ toàn bộ khách đã Unsubscribe.
3. Mã VIP20 giảm 20% nhưng tối đa không quá 200.000 VNĐ/đơn và mỗi email chỉ dùng được 1 lần.
```
