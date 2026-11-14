# CẨM NANG HƯỚNG DẪN DEMO: 12-PHAN-LOAI-TUOI-NO-NHAC-NO

## 1. Nỗi Đau & Bài Toán Thực Tế
Kế toán công nợ phải lọc danh sách hóa đơn quá hạn, chia từng khung tuổi nợ rồi soạn email nhắc nợ cho từng khách hàng rất mất thời gian.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu một khách hàng có 3 hóa đơn quá hạn khác nhau, bạn sẽ gửi 3 email riêng rẽ hay gộp vào 1 email bảng kê tổng hợp?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Đọc file cong_no_phai_thu.xlsx. Tính số ngày quá hạn tính đến hôm nay và phân bổ số dư nợ vào các cột tuổi nợ: Trong hạn, Quá hạn 1-30 ngày, 31-60 ngày, 61-90 ngày, và Trên 90 ngày. Với những khách hàng quá hạn trên 15 ngày, hãy gom tất cả hóa đơn nợ của họ và tạo bản nháp email nhắc thanh toán lịch sự. Xuất file Bao_cao_tuoi_no_va_nhac_no.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không hướng dẫn lọc bỏ các hóa đơn có 'Còn Phải Thu = 0', AI có thể gửi nhầm email đòi nợ khách hàng đã thanh toán xong.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Bao_cao_tuoi_no_va_nhac_no.xlsx` có bảng Aging Report chuẩn và sheet bản nháp email nhắc nợ đã gom gộp hóa đơn.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Không chỉ tính toán tuổi nợ mà còn tự động gom gộp nhiều hóa đơn của cùng 1 khách hàng vào chung 1 email nhắc nợ chỉn chu.
