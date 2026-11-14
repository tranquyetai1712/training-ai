# CẨM NANG HƯỚNG DẪN DEMO: 43-CHIA-TAI-TRONG-XE-CONTAINER

## 1. Nỗi Đau & Bài Toán Thực Tế
Có hàng chục đơn hàng giao trong ngày, điều vận phải tính nhẩm thể tích và cân nặng để biết cần thuê bao nhiêu xe tải và xếp đơn nào đi với nhau.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Nếu một đơn hàng thể tích chỉ 3 CBM nhưng nặng tới 1.800 kg, đơn hàng này đang chiếm dụng tải trọng theo Khối lượng (Weight) hay Thể tích (Volume)?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Dựa vào danh_sach_don_giao.xlsx, hãy gom các đơn hàng theo cụm Quận gần nhau để chia vào các chuyến xe tải (mỗi xe tối đa 2.000 kg và 12 CBM). Tối ưu sao cho số chuyến xe ít nhất và lập bảng danh sách giao hàng cho từng xe vào file Ke_hoach_dieu_xe_giao_hang.xlsx.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu chỉ tối ưu về mặt cân nặng mà quên kiểm tra thể tích CBM, hàng hóa cồng kềnh sẽ bị tràn thùng xe dù cân nặng vẫn chưa chạm ngưỡng tải trọng.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Ke_hoach_dieu_xe_giao_hang.xlsx` có lịch phân chuyến cho từng xe tải đảm bảo không xe nào bị quá tải hay quá khổ.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Tự động gom tuyến và giải bài toán tải trọng vận chuyển xe tải chỉ trong tích tắc.
