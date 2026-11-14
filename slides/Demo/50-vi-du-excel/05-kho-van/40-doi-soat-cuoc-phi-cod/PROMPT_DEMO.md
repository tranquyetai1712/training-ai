# CẨM NANG HƯỚNG DẪN DEMO: 40-DOI-SOAT-CUOC-PHI-COD

## 1. Nỗi Đau & Bài Toán Thực Tế
Hàng tháng nhận bảng kê 5.000 vận đơn từ ViettelPost/GiaoHangNhanh, shop hay bị tính sai cân nặng hoặc sót tiền COD thu hộ.

## 2. Câu Hỏi Gợi Mở Tương Tác Với Học Viên (Interactive Hook)
> 🎙️ **Giảng viên đặt câu hỏi trước khi chạy AI:**  
> "Một chiếc áo sơ mi đóng hộp nặng 300g nhưng bưu cục cân vọt lên 950g và nhảy bậc cước, shop của bạn mất bao nhiêu tiền cước oan uổng?"

## 3. Câu Lệnh Prompt Mẫu (Copy dán trực tiếp vào Antigravity)
```text
Đối soát bảng kê bang_ke_van_chuyen.xlsx: Hãy kiểm tra đơn nào bị hãng cân vọt trọng lượng so với trọng lượng chuẩn nội bộ, và đơn nào trạng thái 'Đã giao' nhưng chưa nhận được tiền COD. Xuất danh sách chênh lệch ra file Bien_ban_doi_soat_cuoc_van_chuyen.xlsx để làm việc với bưu cục.
```

## 4. Phân Tích Lỗi Thường Gặp Nếu Viết Prompt Sai (Prompt Pitfalls)
> ⚠️ **Học viên cần lưu ý:**  
> Nếu không quy định ngưỡng sai số cho phép của bao bì (Tolerance threshold, ví dụ 50g cho túi niêm phong), AI sẽ bắt bớ cả những đơn chỉ lệch vài gram bình thường.

## 5. Kết Quả Kỳ Vọng & File Đối Chiếu (Verification)
- **Tệp tin kết quả kỳ vọng:** `_ket_qua_mau_chuan.xlsx` (đã tạo sẵn trong thư mục để đối chiếu).
- **Chi tiết đầu ra:** File `Bien_ban_doi_soat_cuoc_van_chuyen.xlsx` chỉ rõ từng mã vận đơn bị tính lố cước và sót tiền COD.

## 6. Điểm "Wow" Thuyết Trình
> 💡 **Điểm nhấn giảng viên cần lưu ý:**  
> Giúp doanh nghiệp thu hồi lại ngay tiền cước bị tính lố và tiền COD bị sót mỗi tháng.
