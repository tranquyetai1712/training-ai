# CẨM NANG HƯỚNG DẪN DEMO: 41-DOI-CHIEU-CHUNG-TU-XNK

## 1. Nỗi Đau & Bài Toán Thực Tế
Trước khi truyền tờ khai hải quan phải dò từng con số Gross Weight, Net Weight, CBM giữa Invoice, Packing List và B/L. Lệch 1 số là kẹt hàng ở cảng.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu Gross Weight trên Packing List ghi 1.400 KGS nhưng trên Vận đơn (Bill of Lading) lại in 1.450 KGS, hậu quả pháp lý gì có thể xảy ra khi thông quan hải quan?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Đọc và đối chiếu chéo 3 chứng từ: Invoice.xlsx, PackingList.xlsx và BillOfLading.txt. Kiểm tra xem Tên hàng, Số lượng kiện, Trọng lượng Gross Weight, Net Weight, Số khối CBM có khớp nhau 100% không. Liệt kê bất kỳ điểm sai lệch nào tìm thấy vào file Bien_ban_doi_chieu_chung_tu_XNK.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu bỏ qua việc kiểm tra đơn vị tính trọng lượng (ví dụ LBS sang KGS), việc sai lệch hệ đo lường sẽ dẫn đến mức phạt hành chính rất nặng từ cơ quan Hải quan.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Bien_ban_doi_chieu_chung_tu_XNK.xlsx` chỉ ra các điểm khớp và cảnh báo sai lệch số liệu giữa các chứng từ.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Đối chiếu chéo giữa Excel và PDF/Text chuẩn xác từng con số thập phân, cứu dân XNK khỏi những lỗi sai chứng từ đắt giá.
