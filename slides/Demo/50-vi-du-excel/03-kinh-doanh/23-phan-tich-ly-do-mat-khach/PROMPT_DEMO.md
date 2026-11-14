# CẨM NANG HƯỚNG DẪN DEMO: 23-PHAN-TICH-LY-DO-MAT-KHACH

## 1. Nỗi Đau & Bài Toán Thực Tế
Cột ghi chú lý do mất khách trên CRM chứa hàng nghìn câu văn tự do lộn xộn, quản lý không thể dùng PivotTable thống kê được.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu một nhân viên ghi chú 'Khách bảo bên Fast bán rẻ hơn 15%', nguyên nhân chính là 'Giá cao' hay 'Đối thủ cạnh tranh'?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Đọc cột Ghi chú của Sales trong file crm_lost_deals.xlsx. Hãy phân tích và gán nhãn chuẩn hóa vào cột mới 'Nhóm lý do thất bại' gồm: Giá cao, Thiếu tính năng, Đối thủ cạnh tranh, Chưa có ngân sách, Không liên lạc được. Lập bảng thống kê tỷ lệ % từng nhóm lý do vào file Phan_tich_Lost_Deals_CRM.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không quy định danh mục nhãn cố định (Closed Taxonomy), AI sẽ tự nghĩ ra hàng chục nhãn khác nhau làm loãng dữ liệu thống kê.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Phan_tich_Lost_Deals_CRM.xlsx` với các nhãn nguyên nhân chuẩn hóa và bảng PivotTable thống kê chi tiết.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Sức mạnh tuyệt đối của AI: biến văn bản tự do lộn xộn (Unstructured Text) thành danh mục định lượng để làm PivotTable.
