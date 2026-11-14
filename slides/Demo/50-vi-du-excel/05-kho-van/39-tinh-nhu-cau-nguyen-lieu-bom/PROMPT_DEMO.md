# CẨM NANG HƯỚNG DẪN DEMO: 39-TINH-NHU-CAU-NGUYEN-LIEU-BOM

## 1. Nỗi Đau & Bài Toán Thực Tế
Khách đặt nhiều loại thành phẩm, mỗi món lại cấu thành từ hàng chục linh kiện có tỷ lệ hao hụt khác nhau, tính tay rất dễ đặt thiếu linh kiện.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu định mức may 1 áo là 1.4m vải với tỷ lệ hao hụt cắt vải 3%, thì để may 1.000 áo bạn cần chuẩn bị chính xác bao nhiêu mét vải?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Kết hợp file ke_hoach_sx.xlsx và dinh_muc_bom.xlsx. Hãy tính tổng nhu cầu từng loại nguyên vật liệu cần dùng (gồm cả hao hụt), đối chiếu với tồn kho để tính số lượng cần mua thêm, và cho biết tối đa sản xuất được bao nhiêu thành phẩm nếu không mua thêm. Xuất file Nhu_cau_nguyen_vat_lieu_BOM.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không tính tỷ lệ hao hụt vào công thức, phân xưởng may khi vào chuyền sẽ bị hụt vải và không hoàn thành đủ số lượng áo theo đơn hàng.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Nhu_cau_nguyen_vat_lieu_BOM.xlsx` liệt kê chi tiết từng linh kiện thiếu hụt và năng lực sản xuất tối đa.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Xử lý bài toán nổ định mức BOM (BOM Explosion) và nút thắt cổ chai sản xuất cực nhanh.
