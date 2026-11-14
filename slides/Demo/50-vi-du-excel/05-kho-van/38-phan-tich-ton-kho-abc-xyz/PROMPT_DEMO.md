# CẨM NANG HƯỚNG DẪN DEMO: 38-PHAN-TICH-TON-KHO-ABC-XYZ

## 1. Nỗi Đau & Bài Toán Thực Tế
Kho có hàng nghìn mã hàng, thủ kho không rà soát kịp lô hàng nào sắp hết hạn hoặc mã nào đã nằm im 6 tháng không bán được.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Theo nguyên lý Pareto 80/20 trong quản trị kho, việc kiểm soát chặt chẽ 20% mặt hàng Nhóm A sẽ giúp kiểm soát bao nhiêu % tổng dòng vốn của công ty?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Phân tích file ton_kho_theo_lo.xlsx: (1) Phân nhóm ABC theo giá trị tồn (A: 80%, B: 15%, C: 5%); (2) Lọc các lô hàng còn hạn sử dụng dưới 90 ngày; (3) Lọc danh sách hàng chết nằm im trên 180 ngày không xuất bán. Xuất ra file Bao_cao_ton_kho_ABC_Canh_bao.xlsx gồm 3 sheet.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu sắp xếp dữ liệu tăng dần thay vì giảm dần theo Giá trị tồn kho trước khi tính % tích lũy, các mặt hàng giá trị nhỏ nhất sẽ bị gán nhầm thành Nhóm A.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Bao_cao_ton_kho_ABC_Canh_bao.xlsx` phân nhóm vốn rõ ràng và khoanh vùng hàng cận date, hàng tồn chết.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Giúp lãnh đạo nhìn thấy ngay hàng trăm triệu đồng đang nằm chết trong kho hoặc sắp hết hạn sử dụng.
