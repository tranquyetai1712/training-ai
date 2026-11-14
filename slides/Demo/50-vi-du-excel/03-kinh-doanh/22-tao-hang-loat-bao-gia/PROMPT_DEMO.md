# CẨM NANG HƯỚNG DẪN DEMO: 22-TAO-HANG-LOAT-BAO-GIA

## 1. Nỗi Đau & Bài Toán Thực Tế
Sales Admin mỗi ngày phải làm 15-20 báo giá: tra mã sản phẩm, gõ thông tin khách hàng, tính chiết khấu rất mất thì giờ.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu một khách hàng mua 3 mặt hàng khác nhau trong 1 yêu cầu báo giá, làm sao để tính chiết khấu 5% trên tổng giá trị đơn thay vì chiết khấu từng dòng lẻ?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Dựa vào yêu cầu trong yeu_cau_bao_gia.xlsx, hãy tra cứu đơn giá từ bang_gia.xlsx, áp dụng chiết khấu 5% cho khách mua trên 50 triệu, và tạo từng file báo giá riêng trong thư mục Bao_Gia_Xuat theo tên Bao_Gia_[MaKH].xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không hướng dẫn tính thuế GTGT (10%) sau khi trừ tiền chiết khấu, giá trị tổng thanh toán sẽ bị chênh lệch so với chuẩn kế toán.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** Các file báo giá chuẩn chỉnh được tạo tự động trong thư mục `Bao_Gia_Xuat/`.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Tạo hàng loạt báo giá đúng chuẩn nhận diện thương hiệu chỉ trong vài giây.
