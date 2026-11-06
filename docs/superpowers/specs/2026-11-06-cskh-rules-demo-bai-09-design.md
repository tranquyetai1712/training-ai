# Design Document: Chuyển đổi Ví Dụ Thực Hành Bài 9 (Bài 3.3) sang CSKH / Sales

- **Ngày tạo:** 2026-11-06
- **Tác giả:** AI Coding Assistant & Giảng viên
- **Chủ đề:** Khóa học "Làm Chủ Google Antigravity Cho Người Không Chuyên" - Phần 3 (Trụ Cột 1: Rules)

---

## 1. Bối cảnh & Mục tiêu

### 1.1 Vấn đề
- Bài 3.2 (Bài 8) đã sử dụng ví dụ về định dạng tiền tệ VNĐ và ngày tháng (Bảng kê chi phí) để giải thích cơ chế `always_on` và `glob`.
- Bài 3.3 (Bài 9 - thực hành) trước đây cũng dùng lại ví dụ bảng kê chi phí công tác (`chi_phi_cong_tac_tho.txt`), gây trùng lặp nội dung bài giảng và giảm tính phong phú, hấp dẫn đối với học viên.

### 1.2 Mục tiêu
- Đổi ví dụ thực hành ở Bài 3.3 sang tình huống thực tế văn phòng mới: **CSKH / Sales — Chuẩn hóa ghi chú cuộc gọi khiếu nại thô thành Báo cáo xử lý & Phân loại mức độ ưu tiên**.
- Đồng bộ trọn gói 4 thành phần:
  1. Thư mục mẫu thực hành độc lập `slides/Demo/xu-ly-khieu-nai-cskh/`.
  2. Slide 3 trong `slides/phan_03_tru_cot_rules.html`.
  3. Kịch bản lời thoại chi tiết Bài 9 (`slides/loi-thoai/bai_09_p03_thuc_hanh_cai_dat_rules_van_phong.md`).
  4. Câu dẫn chuyển tiếp ở cuối Bài 8 (`slides/loi-thoai/bai_08_p03_agents_md_gemini_md_hien_phap_du_an.md`) và cập nhật `slides/REVIEW_TONG_QUAN_KHOA_HOC.md`.

---

## 2. Chi tiết Thiết kế Kỹ thuật & Dữ liệu

### 2.1 Workspace Mẫu: `slides/Demo/xu-ly-khieu-nai-cskh/`

#### File 1: `ghi_chu_cuoc_goi_tho.txt`
Dữ liệu thô thực tế không qua format:
```text
1. khach hang nguyen anh tuan goi phan nan don hang ord9821 bi vo man hinh yeu cau doi gap sdt 0912345678 goi luc 9h sang ngay 10/24/2026
2. tran thi thuy hoi ve don hang ord 9822 chua thay giao, khach chi hoi tham tien do sdt 0988776655 ngay 2026-10-25 luc 14:30
3. le van duc khieu nai don hang ord-9823 giao sai mau ao, yeu cau hoan tien gap sdt 0905112233 ngay 26/10/2026 16:00
```

#### File 2: `AGENTS.md` (Bản Hiến Pháp Dự Án - always_on)
```markdown
# BẢN HIẾN PHÁP DỰ ÁN CSKH & XỬ LÝ KHIẾU NẠI
Bạn là Trợ lý AI Phân tích & Điều phối CSKH. Khi làm việc trong thư mục này:

1. TÔNG GIỌNG: Luôn xưng hô "Tôi - Bạn", giao tiếp lịch sự bằng 100% tiếng Việt, khách quan, đi thẳng vào hành động xử lý.
2. AN TOÀN DỮ LIỆU: Tuyệt đối không xóa hoặc ghi đè lên file thô gốc (ghi_chu_cuoc_goi_tho.txt). Luôn xuất báo cáo phân loại ra file mới mang tên: bao_cao_xu_ly_khieu_nai.csv.
```

#### File 3: `.agents/rules/phan_loai_khieu_nai.md` (Luật chuyên ngành - trigger glob)
```markdown
---
trigger: glob
globs: "*.txt, *.csv"
description: "Quy chuẩn trích xuất và phân loại mức độ ưu tiên cuộc gọi CSKH"
---

# QUY CHUẨN PHÂN LOẠI & ĐỊNH DẠNG CUỘC GỌI KHIẾU NẠI
Khi đọc dữ liệu cuộc gọi từ các file văn bản hoặc bảng tính, bạn BẮT BUỘC tuân thủ:

1. MÃ ĐƠN HÀNG: Viết hoa đồng nhất theo định dạng ORD-XXXX (Ví dụ: "ord9821" ➔ "ORD-9821").
2. PHÂN LOẠI MỨC ĐỘ ƯU TIÊN:
   - [HỎA TỐC]: Sự cố vỡ hỏng, lỗi nghiêm trọng, khách yêu cầu đổi ngay lập tức.
   - [KHẨN CẤP]: Giao sai mẫu mã, yêu cầu hoàn tiền.
   - [TIÊU CHUẨN]: Khách hỏi thăm tiến độ giao hàng thông thường.
3. ĐỊNH DẠNG THÔNG TIN:
   - Họ tên: Viết hoa danh từ riêng (Ví dụ: Nguyễn Anh Tuấn, Trần Thị Thúy).
   - Số điện thoại: Định dạng nhóm 0xxx.xxx.xxx (Ví dụ: 0912.345.678).
   - Thời gian: Đồng bộ chuẩn HH:mm DD/MM/YYYY.
```

#### File 4: Kết quả mẫu sẵn: `bao_cao_xu_ly_khieu_nai.csv`
Được tạo sẵn trong thư mục để học viên có thể đối chiếu ngay sau khi thực hành:
```markdown
# BÁO CÁO PHÂN LOẠI VÀ ĐIỀU PHỐI KHIẾU NẠI KHÁCH HÀNG
*Ngày trích xuất tự động: 26/10/2026*

| Thời Gian | Mã Đơn | Khách Hàng | Số Điện Thoại | Mức Độ | Nội Dung Sự Cố | Hành Động Đề Xuất |
|---|---|---|---|---|---|---|
| 09:00 24/10/2026 | ORD-9821 | Nguyễn Anh Tuấn | 0912.345.678 | 🔴 **HỎA TỐC** | Vỡ màn hình, đòi đổi gấp | Chuyển kỹ thuật thu hồi & gửi máy mới trong 2h |
| 14:30 25/10/2026 | ORD-9822 | Trần Thị Thúy | 0988.776.655 | 🟢 **TIÊU CHUẨN** | Khách hỏi tiến độ đơn hàng | Gửi SMS tra cứu vận đơn & cập nhật trạng thái kho |
| 16:00 26/10/2026 | ORD-9823 | Lê Văn Đức | 0905.112.233 | 🟡 **KHẨN CẤP** | Giao sai màu áo, đòi hoàn tiền | Liên hệ xin lỗi, lập đơn hoàn hàng & hoàn tiền |
```

---

### 2.2 Slide 3 trong `slides/phan_03_tru_cot_rules.html`

- Đổi nội dung Slide 3:
  - Header Chip: `WORKSPACE: DEMO/XU-LY-KHIEU-NAI-CSKH`
  - Tiêu đề: `Thực Hành: Phối Hợp AGENTS.md & .agents/rules/ Xử Lý Nhật Ký Khiếu Nại`
  - Cột 1 (Cấu trúc cài đặt):
    - Khối `AGENTS.md`: Không sửa đè `ghi_chu_cuoc_goi_tho.txt`, xuất file mới `bao_cao_xu_ly_khieu_nai.csv`.
    - Khối `.agents/rules/phan_loai_khieu_nai.md`: trigger `glob: "*.txt, *.csv"`, mã đơn `ORD-XXXX`, phân loại `HỎA TỐC / KHẨN CẤP / TIÊU CHUẨN`.
  - Cột 2 (Kết quả trên file):
    - Câu lệnh 1 dòng: *"Hãy xử lý file ghi_chu_cuoc_goi_tho.txt giúp tôi."*
    - File thô input vs File markdown phân cấp output.
  - Cập nhật thuộc tính `data-notes` của Slide 3 tương ứng với nội dung mới.

---

### 2.3 Kịch bản Lời thoại Bài 9 (`slides/loi-thoai/bai_09_p03_thuc_hanh_cai_dat_rules_van_phong.md`)

- Cập nhật kịch bản lời thoại word-for-word:
  - `[00:00 - 00:35]`: Mục tiêu thực hành: Phối hợp `AGENTS.md` và `rules/xx.md` trên dữ liệu nhật ký cuộc gọi CSKH.
  - `[00:35 - 01:50]`: Khám phá workspace mẫu `xu-ly-khieu-nai-cskh/`, phân tích file thô, `AGENTS.md` và rule glob.
  - `[01:50 - 02:40]`: Cảnh báo quét phẳng (Flat Scanning) và quy tắc dung lượng < 24KB.
  - `[02:40 - 03:50]`: Thực chứng ra lệnh 1 câu ➔ AI tự nạp rule glob phân loại mã đơn, gán nhãn mức độ và xuất file mới.
  - `[03:50 - 04:30]`: Tổng kết Trụ Cột 1 (Rules) và dẫn dắt sang Trụ Cột 2 (Skills - Phần 4).

---

### 2.4 Đồng bộ Bài 8 & Tổng quan khóa học

- `slides/loi-thoai/bai_08_p03_agents_md_gemini_md_hien_phap_du_an.md`: Cập nhật câu dẫn cuối bài dẫn vào bài thực hành nhật ký khiếu nại CSKH.
- `slides/REVIEW_TONG_QUAN_KHOA_HOC.md`: Cập nhật tiêu đề và mô tả của Bài 3.3.

---

## 3. Tiêu chí Kiểm Thử Thành Công (Verification Checklist)

- [ ] Folder `slides/Demo/xu-ly-khieu-nai-cskh/` được tạo đầy đủ với 4 file (`ghi_chu_cuoc_goi_tho.txt`, `AGENTS.md`, `.agents/rules/phan_loai_khieu_nai.md`, `bao_cao_xu_ly_khieu_nai.csv`).
- [ ] Thư mục cũ `slides/Demo/chi-phi-cong-tac-tho/` được dọn dẹp hoặc giữ lại an toàn không ảnh hưởng.
- [ ] Slide 3 trong `slides/phan_03_tru_cot_rules.html` hiển thị đúng nội dung CSKH, script hoạt động trơn tru, không lỗi HTML syntax.
- [ ] Lời thoại Bài 9 khớp từng giây với Slide 3 và cấu trúc folder mới.
- [ ] Câu kết Bài 8 mượt mà, chuyển tiếp tự nhiên sang Bài 9.
