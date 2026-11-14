# CẨM NANG HƯỚNG DẪN DEMO: 34-CHIA-QUA-TANG-POSM-DAI-LY

## 1. Nỗi Đau & Bài Toán Thực Tế
Chia quà tặng cho hàng chục đại lý theo tỷ lệ doanh thu nhưng phải làm tròn theo thùng (20 cái/thùng) rất hay bị lệch tổng số lượng.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu chia theo tỷ lệ doanh thu ra 3.7 thùng áo mưa, bạn sẽ làm tròn lên 4 thùng hay làm tròn xuống 3 thùng khi tổng kho chỉ còn đúng 20 thùng?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Dựa vào file ton_kho_posm.xlsx, hãy phân bổ số lượng từng loại quà tặng POSM cho các đại lý theo tỷ trọng doanh số. Lưu ý: mỗi đại lý nhận tối thiểu 1 thùng, làm tròn theo quy cách đóng thùng, và tổng phân bổ khớp 100% tồn kho hiện có. Xuất file Bang_chia_qua_tang_POSM_Dai_Ly.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu làm tròn bằng hàm ROUND thông thường cho từng đại lý, tổng cộng các đại lý cộng lại sẽ bị thừa hoặc thiếu từ 1 đến 2 thùng so với kho thực tế.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Bang_chia_qua_tang_POSM_Dai_Ly.xlsx` có bảng chia hàng chuẩn chỉnh, không bị lẻ kiện và khớp số lượng tồn kho.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Giải quyết bài toán làm tròn phân bổ (Rounding Allocation) không bị lệch tổng — nỗi ám ảnh kinh điển của Excel.
