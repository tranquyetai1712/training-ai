# CẨM NANG HƯỚNG DẪN DEMO: 31-PHAN-TICH-DANH-GIA-SAN-TMDT

## 1. Nỗi Đau & Bài Toán Thực Tế
Tải về hàng nghìn bình luận của khách nhưng không biết sản phẩm bị chê vì giao hàng chậm, móp hộp hay do chất lượng vải lỗi.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu khách chấm 2 sao kèm bình luận 'Đặt size L mà giao size M, shop làm ăn tắc trách', lỗi này thuộc về Bộ phận Đóng gói Kho hay Chất lượng Nhà xưởng?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Phân tích file shopee_reviews.xlsx. Với các đánh giá từ 1 đến 3 sao, hãy đọc nội dung bình luận để phân loại nguyên nhân vào các nhóm: Chất lượng SP, Đóng gói, Vận chuyển, Tư vấn, Sai mẫu. Lập bảng ma trận thống kê từng Mã sản phẩm bị lỗi nào nhiều nhất vào file Phan_tich_Danh_Gia_Shopee_T10.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không hướng dẫn lọc bỏ các đánh giá 4-5 sao hài lòng, bảng phân tích nguyên nhân gốc rễ (Root Cause) sẽ bị loãng bởi các nhận xét tích cực.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Phan_tich_Danh_Gia_Shopee_T10.xlsx` bóc tách chính xác từng nhóm lỗi theo từng mã hàng để làm việc với kho và xưởng may.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Biến hàng nghìn bình luận cảm tính thành bảng số liệu định lượng rõ ràng phục vụ cải tiến sản phẩm.
