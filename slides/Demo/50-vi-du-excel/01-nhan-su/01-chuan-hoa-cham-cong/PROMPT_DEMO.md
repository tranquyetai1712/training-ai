# CẨM NANG HƯỚNG DẪN DEMO: 01-CHUAN-HOA-CHAM-CONG

## 1. Nỗi Đau & Bài Toán Thực Tế
Máy chấm công xuất file log thô 20.000 dòng, mỗi lần quẹt thẻ là 1 dòng. HR mất 4-5 tiếng dùng hàm mảng phức tạp để tìm giờ vào/ra và tính số phút đi muộn.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Theo các bạn, nếu một nhân viên quẹt thẻ 5 lần trong ngày thì làm sao Excel biết lần nào là Giờ Vào và lần nào là Giờ Ra nếu không viết code VBA?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Đọc file cham_cong_thang_10_raw.xlsx. Hãy gom nhóm theo từng Nhân viên và từng Ngày: lấy giờ quẹt sớm nhất làm Giờ vào, muộn nhất làm Giờ ra. Tính số phút đi muộn (nếu vào sau 08:30), số phút về sớm (nếu ra trước 17:30), và tổng số công trong ngày. Xuất ra file bang_cong_chuan_hoa.xlsx gồm 2 sheet: Chi tiết từng ngày và Bảng tổng hợp tháng của từng nhân viên, tô màu đỏ các dòng đi muộn quá 30 phút.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không dặn AI mốc giờ nghỉ trưa (12:00 - 13:00) hoặc không dặn quy tắc 'quẹt 1 lần trong ngày tính quên quẹt', AI có thể lấy nhầm giờ ăn trưa làm giờ ra về.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `bang_cong_chuan_hoa.xlsx` được tạo tự động với 2 sheets, các cột giờ vào/ra chuẩn chỉ, tính đúng số phút đi muộn và tô màu cảnh báo vi phạm.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Xử lý 20.000 dòng log thô trong 15 giây mà không cần viết bất kỳ công thức mảng hay VBA phức tạp nào.
