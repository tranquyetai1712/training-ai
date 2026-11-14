# CẨM NANG HƯỚNG DẪN DEMO: 26-TONG-HOP-KHAO-SAT-NPS-CSAT

## 1. Nỗi Đau & Bài Toán Thực Tế
Xuất file khảo sát Google Forms gồm điểm số 1-10 và câu góp ý dài dòng, rất khó tính nhanh NPS và tìm ra khách đang phàn nàn gì nhất.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu khách hàng chấm 7 hoặc 8 điểm thì điểm số này có được tính vào công thức Net Promoter Score (NPS) không?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Phân tích file khao_sat_khach_hang.xlsx: Phân loại điểm 9-10 (Promoters), 7-8 (Passives), 0-6 (Detractors) để tính chỉ số NPS chung. Đọc cột Ý kiến đóng góp để tìm Top 3 vấn đề khách hàng chưa hài lòng nhất kèm câu trích dẫn tiêu biểu. Xuất file Bao_cao_khao_sat_NPS.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu nhầm công thức NPS thành điểm trung bình cộng (Mean Average), báo cáo sẽ không phản ánh đúng tỷ lệ người ủng hộ ròng theo chuẩn quản trị quốc tế.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Bao_cao_khao_sat_NPS.xlsx` có bảng điểm NPS và danh sách các nhóm phản hồi của khách hàng.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Vừa tính toán định lượng chỉ số NPS vừa đọc hiểu tiếng Việt để rút trích insight khách hàng trong cùng 1 báo cáo.
