# CẨM NANG HƯỚNG DẪN DEMO: 09-XEP-LICH-TRUC-CA-TU-DONG

## 1. Nỗi Đau & Bài Toán Thực Tế
Xếp lịch trực 3 ca cho hàng chục nhân viên sao cho vừa đủ người mỗi ca, vừa không trùng lịch xin nghỉ phép, vừa công bằng rất dễ bị sót.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Có ai từng xếp lịch trực ca xong thì bị nhân viên khiếu nại vì vừa trực ca tối đêm hôm trước mà sáng hôm sau 8h đã phải có mặt đi làm không?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Dựa trên danh sách nhân viên và ngày đăng ký nghỉ phép trong file danh_sach_nv_va_nghi_phep.xlsx, hãy xếp lịch phân ca tháng 11 (Ca Sáng: 2 người, Ca Chiều: 2 người, Ca Tối: 1 người mỗi ngày). Đảm bảo công bằng tổng số ca, không ai trực Ca Tối hôm trước mà phải trực Ca Sáng hôm sau. Xuất ra bảng phân ca theo ma trận Ngày x Nhân viên vào file Lich_Phan_Ca_Thang_11.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Quên kiểm tra ràng buộc liên tiếp (No Back-to-Back: Tối hôm trước -> Sáng hôm sau) khiến nhân viên không đủ thời gian ngủ nghỉ phục hồi sức khỏe.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Lich_Phan_Ca_Thang_11.xlsx` dạng ma trận lịch trực cả tháng, tuân thủ 100% các ràng buộc nghỉ phép và quy định ca.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Giải quyết bài toán tổ hợp tối ưu hóa phức tạp trong chớp mắt mà làm tay mất cả ngày tẩy xóa.
