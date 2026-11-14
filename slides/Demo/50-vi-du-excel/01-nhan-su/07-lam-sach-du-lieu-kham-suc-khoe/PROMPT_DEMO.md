# CẨM NANG HƯỚNG DẪN DEMO: 07-LAM-SACH-DU-LIEU-KHAM-SUC-KHOE

## 1. Nỗi Đau & Bài Toán Thực Tế
Nhân viên tự điền form: tên người viết hoa hết, người viết thường, ngày sinh lộn xộn, CCCD bị mất số 0 đầu.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Bao nhiêu bạn ở đây từng mở file Excel lên và thấy cột Số điện thoại bị mất sạch số 0 ở đầu hoặc biến thành dạng 9.123E+08?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Làm sạch file dang_ky_kham_suc_khoe_raw.xlsx: chuẩn hóa Họ tên viết hoa chữ cái đầu mỗi từ và bỏ khoảng trắng thừa; chuẩn hóa Ngày sinh về đúng định dạng DD/MM/YYYY; thêm lại số 0 ở đầu cho cột SĐT (đủ 10 số) và CCCD (đủ 12 số) dưới dạng Text; phát hiện và đánh dấu các dòng bị trùng lặp CCCD. Lưu thành file danh_sach_chuan_gui_benh_vien.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không dặn AI lưu cột CCCD/SĐT dưới định dạng Text (chuỗi ký tự), Excel sẽ tự động ép kiểu thành số (Number) và làm biến mất số 0 đầu lần nữa.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `danh_sach_chuan_gui_benh_vien.xlsx` sạch bóng lỗi: họ tên chuẩn đẹp, số điện thoại và CCCD đủ số 0 đầu, ngày sinh đồng bộ.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Giải quyết các lỗi kinh điển nhất của Excel (mất số 0 đầu, sai ngày tháng, thừa dấu cách) chỉ bằng 1 câu lệnh đơn giản.
