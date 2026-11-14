# CẨM NANG HƯỚNG DẪN DEMO: 19-LAM-SACH-CHUAN-HOA-CRM

## 1. Nỗi Đau & Bài Toán Thực Tế
Nhiều nhân viên sales cùng nhập khách hàng: SĐT người có dấu chấm, người có +84, tên công ty viết tắt lung tung làm 1 khách bị nhiều sales gọi trùng.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu gộp 2 dòng khách hàng trùng nhau, bạn sẽ xóa bỏ dòng cũ hay làm sao để không làm mất nhật ký cuộc gọi của sales trước đó?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Làm sạch file data_khach_hang_raw.xlsx: Chuẩn hóa toàn bộ SĐT về dạng 10 số bắt đầu bằng 0 (xóa dấu chấm, đổi +84 thành 0). Chuẩn hóa tên công ty (đưa 'Cty', 'CT TNHH' về 'Công ty TNHH'). Phát hiện các khách hàng trùng SĐT hoặc tên tương đồng, giữ lại dòng mới nhất và gộp lịch sử ghi chú vào chung 1 ô. Xuất ra Data_CRM_Chuan_Hoa.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không hướng dẫn AI nối chuỗi ghi chú (String Concatenation), AI sẽ ghi đè ghi chú mới và xóa sạch toàn bộ lịch sử chăm sóc trước đây.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Data_CRM_Chuan_Hoa.xlsx` sạch sẽ, không còn dòng trùng lặp, tên công ty đồng nhất và ghi chú được bảo toàn.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Xử lý trùng lặp thông minh và không làm mất lịch sử ghi chú chăm sóc khách hàng khi gộp dòng.
