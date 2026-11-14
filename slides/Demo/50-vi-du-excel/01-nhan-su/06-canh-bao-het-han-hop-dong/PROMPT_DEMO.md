# CẨM NANG HƯỚNG DẪN DEMO: 06-CANH-BAO-HET-HAN-HOP-DONG

## 1. Nỗi Đau & Bài Toán Thực Tế
HR thường quên ngày hết hạn thử việc hoặc hợp đồng 1 năm của nhân viên, dẫn đến bị động khi cần gia hạn hoặc làm thủ tục chấm dứt.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu một nhân viên thử việc 2 tháng kết thúc vào hôm nay mà HR quên không gửi thông báo tiếp nhận hay chấm dứt, thì theo luật lao động nhân viên đó sẽ mặc nhiên trở thành gì?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Đọc file danh_sach_nhan_su.xlsx. Lọc ra tất cả nhân sự có Hợp đồng thử việc hoặc Hợp đồng chính thức sẽ hết hạn trong vòng 30 ngày tới. Tạo một sheet mới tên Canh_Bao_Gia_Han trong file đó, tô màu đỏ các trường hợp dưới 15 ngày và vàng cho các trường hợp 16-30 ngày.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không quy định mốc ngày hiện tại (Reference Date), AI có thể dùng ngày ngẫu nhiên trong quá khứ dẫn đến lọc sai số ngày còn lại.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** Sheet mới `Canh_Bao_Gia_Han` được tạo với danh sách nhân sự sắp đến hạn, phân loại ngày và định dạng màu sắc nổi bật.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Không bao giờ sợ bị sót hạn hợp đồng lao động nhờ khả năng lọc ngày tháng và tự động hóa báo cáo trong vài giây.
