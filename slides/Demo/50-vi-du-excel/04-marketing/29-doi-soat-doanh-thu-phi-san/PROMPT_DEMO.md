# CẨM NANG HƯỚNG DẪN DEMO: 29-DOI-SOAT-DOANH-THU-PHI-SAN

## 1. Nỗi Đau & Bài Toán Thực Tế
Bán hàng trên Shopee/TikTok Shop có hàng chục loại phí trừ lắt nhắt. Bán nghìn đơn nhưng không biết đơn nào thực lãi, đơn nào đang gồng lỗ.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Một chiếc áo thun bán giá 99k, sau khi trừ phí sàn cố định 7k, phí thanh toán 3k, voucher shop 30k và phí lệch ship 15k, shop còn thực nhận bao nhiêu tiền?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Kết hợp file shopee_orders.xlsx và gia_von.xlsx. Với từng đơn hàng và từng mã SKU, hãy tính: Doanh thu, Tổng phí sàn thu, Tiền thực nhận về ví, Giá vốn hàng bán, Lợi nhuận ròng thực tế và % Biên lợi nhuận. Lọc ra danh sách các đơn hàng hoặc mã SKU đang bị bán lỗ ra sheet riêng trong file Doi_soat_lai_lo_Shopee_T10.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu quên nhân giá vốn với cột Số lượng sản phẩm trên đơn hàng, toàn bộ bài toán tính lợi nhuận gộp sẽ bị sai lệch nghiêm trọng.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Doi_soat_lai_lo_Shopee_T10.xlsx` chỉ rõ từng đơn lãi/lỗ và cảnh báo mã sản phẩm đang âm tiền.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Bóc tách ma trận phí sàn TMĐT và chỉ điểm ngay những mã sản phẩm nhìn tưởng bán chạy nhưng thực chất đang gồng lỗ.
